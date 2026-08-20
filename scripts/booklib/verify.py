"""Structural and fidelity verification for the recovered Markdown source."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from .epub_source import read_epub


REQUIRED_FIELDS = {
    "id",
    "volume",
    "part",
    "title",
    "source",
    "level",
    "volatile_facts",
    "reference_links",
}
IMAGE_LINK = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
NORMAL_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
CHAPTER_REFERENCE = re.compile(r"第\s*(\d{1,3})\s*章")


@dataclass(frozen=True)
class VerificationReport:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    metrics: dict[str, int | float]


def _tag(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def _xhtml_visible(element: ET.Element) -> str:
    if _tag(element) == "nav":
        return element.tail or ""
    pieces = [element.text or ""]
    for child in element:
        pieces.append(_xhtml_visible(child))
        pieces.append(child.tail or "")
    return "".join(pieces)


def _markdown_visible(markdown: str) -> str:
    text = IMAGE_LINK.sub("", markdown)
    text = re.sub(r"(?<!!)\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^\s*```.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s{0,3}(?:#{1,6}|>|[-+*]|\d+\.)\s*", "", text, flags=re.MULTILINE)
    text = text.replace("|", "")
    text = re.sub(r"[*_`~]", "", text)
    return text


def _nonwhitespace_count(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def _relative_target(source: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return None
    path = href.split("#", 1)[0]
    if not path:
        return None
    return (source.parent / path).resolve()


def verify_source(
    book_dir: Path,
    epub_path: Path,
    txt_path: Path,
    *,
    enforce_recovery_fidelity: bool = True,
) -> VerificationReport:
    book_dir = book_dir.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, int | float] = {}

    manifest_path = book_dir / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return VerificationReport((f"invalid manifest: {exc}",), (), {})

    chapters = manifest.get("chapters")
    if not isinstance(chapters, list):
        return VerificationReport(("manifest chapters must be a list",), (), {})

    ids = [item.get("id") for item in chapters if isinstance(item, dict)]
    duplicate_ids = sorted({item for item in ids if ids.count(item) > 1})
    if duplicate_ids:
        errors.append(f"duplicate chapter ids: {', '.join(map(str, duplicate_ids))}")
    missing_ids = sorted(set(range(1, 105)) - set(ids))
    extra_ids = sorted(set(ids) - set(range(1, 105)))
    if missing_ids:
        errors.append(f"missing chapter ids: {', '.join(map(str, missing_ids))}")
    if extra_ids:
        errors.append(f"chapter ids outside 1-104: {', '.join(map(str, extra_ids))}")
    metrics["chapter_count"] = len(chapters)

    markdown_by_id: dict[int, str] = {}
    path_by_id: dict[int, Path] = {}
    for item in chapters:
        if not isinstance(item, dict):
            errors.append("manifest chapter entry is not an object")
            continue
        absent = sorted(REQUIRED_FIELDS - set(item))
        if absent:
            errors.append(f"chapter {item.get('id', '?')} missing fields: {', '.join(absent)}")
            continue
        chapter_id = item["id"]
        source = book_dir / item["source"]
        path_by_id[chapter_id] = source
        if not source.is_file():
            errors.append(f"missing chapter source {chapter_id:03d}: {item['source']}")
            continue
        markdown = source.read_text(encoding="utf-8")
        markdown_by_id[chapter_id] = markdown
        heading = re.search(r"^#\s+(.+?)\s*$", markdown, flags=re.MULTILINE)
        heading_text = "" if heading is None else _markdown_visible(heading.group(1)).strip()
        if heading_text != item["title"]:
            errors.append(f"chapter {chapter_id:03d} title does not match manifest")

        for href in IMAGE_LINK.findall(markdown):
            target = _relative_target(source, href)
            if target is not None and not target.is_file():
                errors.append(f"missing image in chapter {chapter_id:03d}: {href}")
        for href in NORMAL_LINK.findall(markdown):
            target = _relative_target(source, href)
            if target is not None and not target.is_file():
                errors.append(f"broken link in chapter {chapter_id:03d}: {href}")
        for reference in CHAPTER_REFERENCE.findall(markdown):
            target_id = int(reference)
            if target_id not in range(1, 105):
                errors.append(
                    f"chapter {chapter_id:03d} references missing chapter {target_id}"
                )

    epub = read_epub(epub_path)
    epub_by_id = {chapter.id: chapter for chapter in epub.chapters}
    if set(epub_by_id) != set(range(1, 105)):
        errors.append("EPUB chapter ids are not exactly 1-104")
    epub_chars = 0
    markdown_chars = 0
    for chapter_id, chapter in epub_by_id.items():
        epub_chars += _nonwhitespace_count(_xhtml_visible(chapter.body))
        markdown = markdown_by_id.get(chapter_id)
        if markdown is not None:
            markdown_chars += _nonwhitespace_count(_markdown_visible(markdown))
        item = next((entry for entry in chapters if entry.get("id") == chapter_id), None)
        if item is not None and item.get("title") != chapter.title:
            errors.append(f"chapter {chapter_id:03d} title differs from EPUB")

    delta = abs(markdown_chars - epub_chars) / max(epub_chars, 1) * 100
    metrics["epub_visible_chars"] = epub_chars
    metrics["markdown_visible_chars"] = markdown_chars
    metrics["epub_text_delta_percent"] = round(delta, 4)
    if enforce_recovery_fidelity and len(markdown_by_id) == 104 and delta > 0.5:
        errors.append(f"Markdown visible-text delta exceeds 0.5%: {delta:.4f}%")

    try:
        txt_chars = _nonwhitespace_count(txt_path.read_text(encoding="utf-8"))
        metrics["txt_nonwhitespace_chars"] = txt_chars
        metrics["txt_to_markdown_delta_percent"] = round(
            abs(txt_chars - markdown_chars) / max(txt_chars, 1) * 100, 4
        )
    except OSError as exc:
        warnings.append(f"TXT comparison unavailable: {exc}")

    return VerificationReport(tuple(errors), tuple(warnings), metrics)
