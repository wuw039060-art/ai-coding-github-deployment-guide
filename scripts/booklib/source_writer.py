"""Generate the reviewable Markdown baseline from a versioned EPUB."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import posixpath
import re
import shutil
import tempfile
import unicodedata
import zipfile

from .epub_source import ChapterSource, DocumentSource, read_epub
from .xhtml_markdown import to_markdown


class SourceWriteError(RuntimeError):
    """Raised when source generation would overwrite non-generated changes."""


VOLUME_RANGES = (
    (1, 4, 1),
    (5, 12, 2),
    (13, 20, 3),
    (21, 28, 4),
    (29, 35, 5),
    (36, 43, 6),
    (44, 50, 7),
    (51, 58, 8),
    (59, 68, 9),
    (69, 104, 10),
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
EXTERNAL_LINK = re.compile(r"\]\((https?://[^)\s]+)\)")


def _volume(chapter_id: int) -> int:
    for start, end, volume in VOLUME_RANGES:
        if start <= chapter_id <= end:
            return volume
    raise SourceWriteError(f"chapter id is outside 1-104: {chapter_id}")


def _part(chapter_id: int) -> str | None:
    if 69 <= chapter_id <= 74:
        return "与 AI 安全协作"
    if 75 <= chapter_id <= 84:
        return "项目开始变复杂以后"
    if 85 <= chapter_id <= 96:
        return "真实用户与稳定运行"
    if 97 <= chapter_id <= 104:
        return "成熟项目与长期治理"
    return None


def _level(chapter_id: int) -> str:
    if chapter_id <= 74:
        return "core"
    if chapter_id <= 84:
        return "optional"
    if chapter_id <= 96:
        return "advanced"
    return "reference"


def _slug(title: str, chapter_id: int) -> str:
    title = unicodedata.normalize("NFC", title)
    title = re.sub(rf"^第\s*{chapter_id}\s*章[\s　:：—-]*", "", title).strip()
    title = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title, flags=re.UNICODE)
    title = re.sub(r"-+", "-", title).strip("-_").lower()
    return title[:60].rstrip("-") or "chapter"


def _tree_digest(root: Path) -> str:
    digest = sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def _rewrite_links(
    markdown: str,
    *,
    source_href: str,
    output_path: str,
    target_by_href: dict[str, str],
) -> str:
    def replace(match: re.Match[str]) -> str:
        label, href = match.groups()
        if "://" in href or href.startswith(("mailto:", "#")):
            return match.group(0)
        path, separator, fragment = href.partition("#")
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source_href), path))
        target = target_by_href.get(resolved)
        if target is None:
            return match.group(0)
        relative = posixpath.relpath(target, posixpath.dirname(output_path))
        suffix = f"#{fragment}" if separator else ""
        return f"[{label}]({relative}{suffix})"

    return MARKDOWN_LINK.sub(replace, markdown)


def _target_paths(
    chapters: tuple[ChapterSource, ...], frontmatter: tuple[DocumentSource, ...]
) -> dict[str, str]:
    targets: dict[str, str] = {}
    for document in frontmatter:
        targets[posixpath.normpath(document.href)] = f"frontmatter/{document.id}.md"
    for chapter in chapters:
        filename = f"{chapter.id:03d}-{_slug(chapter.title, chapter.id)}.md"
        targets[posixpath.normpath(chapter.href)] = f"chapters/{filename}"
    return targets


def _copy_assets(epub_path: Path, rootfile: str, destination: Path) -> None:
    package_dir = posixpath.dirname(rootfile)
    prefix = f"{package_dir}/assets/" if package_dir else "assets/"
    with zipfile.ZipFile(epub_path) as archive:
        for info in sorted(archive.infolist(), key=lambda item: item.filename):
            if info.is_dir() or not info.filename.startswith(prefix):
                continue
            relative = info.filename[len(prefix) :]
            target = destination / "assets" / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(info))


def _generate_tree(epub_path: Path, destination: Path) -> dict[str, object]:
    book = read_epub(epub_path)
    targets = _target_paths(book.chapters, book.frontmatter)
    (destination / "chapters").mkdir(parents=True)
    (destination / "frontmatter").mkdir(parents=True)

    for document in book.frontmatter:
        output_path = targets[posixpath.normpath(document.href)]
        markdown = to_markdown(document.body, document.href)
        markdown = _rewrite_links(
            markdown,
            source_href=document.href,
            output_path=output_path,
            target_by_href=targets,
        )
        (destination / output_path).write_text(markdown, encoding="utf-8", newline="\n")

    manifest_chapters: list[dict[str, object]] = []
    for chapter in book.chapters:
        output_path = targets[posixpath.normpath(chapter.href)]
        markdown = to_markdown(chapter.body, chapter.href)
        markdown = _rewrite_links(
            markdown,
            source_href=chapter.href,
            output_path=output_path,
            target_by_href=targets,
        )
        (destination / output_path).write_text(markdown, encoding="utf-8", newline="\n")
        manifest_chapters.append(
            {
                "id": chapter.id,
                "volume": _volume(chapter.id),
                "part": _part(chapter.id),
                "title": chapter.title,
                "source": output_path,
                "level": _level(chapter.id),
                "volatile_facts": [],
                "reference_links": sorted(set(EXTERNAL_LINK.findall(markdown))),
            }
        )

    _copy_assets(epub_path, book.rootfile, destination)
    manifest: dict[str, object] = {
        "schema_version": 1,
        "source_epub": epub_path.name,
        "source_sha256": sha256(epub_path.read_bytes()).hexdigest(),
        "chapters": manifest_chapters,
    }
    (destination / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def write_source(epub_path: Path, output_dir: Path) -> dict[str, object]:
    """Generate a source tree, refusing to overwrite any changed baseline."""

    epub_path = epub_path.resolve()
    output_dir = output_dir.resolve()
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{output_dir.name}-source-", dir=output_dir.parent)
    )
    try:
        manifest = _generate_tree(epub_path, temporary)
        if output_dir.exists():
            if _tree_digest(output_dir) == _tree_digest(temporary):
                return manifest
            raise SourceWriteError(
                f"refusing to replace changed source tree: {output_dir}"
            )
        os.replace(temporary, output_dir)
        return manifest
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
