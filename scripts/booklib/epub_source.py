"""Read ordered XHTML documents from an EPUB without third-party packages."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile


CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"
OPF_NS = "http://www.idpf.org/2007/opf"
XHTML_NS = "http://www.w3.org/1999/xhtml"
CHAPTER_ID = re.compile(r"ch(?P<id>\d{3})$")


class SourceError(ValueError):
    """Raised when an EPUB cannot be recovered without losing structure."""


@dataclass(frozen=True)
class ChapterSource:
    id: int
    href: str
    title: str
    body: ET.Element


@dataclass(frozen=True)
class DocumentSource:
    id: str
    href: str
    title: str
    body: ET.Element


@dataclass(frozen=True)
class EpubBook:
    rootfile: str
    chapters: tuple[ChapterSource, ...]
    frontmatter: tuple[DocumentSource, ...]


def _read_xml(archive: zipfile.ZipFile, name: str) -> ET.Element:
    try:
        payload = archive.read(name)
    except KeyError as exc:
        raise SourceError(f"EPUB entry is missing: {name}") from exc
    try:
        return ET.fromstring(payload)
    except ET.ParseError as exc:
        raise SourceError(f"invalid XML in {name}: {exc}") from exc


def _document_body_and_title(root: ET.Element, href: str) -> tuple[ET.Element, str]:
    body = root.find(f".//{{{XHTML_NS}}}body")
    if body is None:
        body = root.find(".//body")
    if body is None:
        raise SourceError(f"XHTML body is missing: {href}")

    heading = body.find(f".//{{{XHTML_NS}}}h1")
    if heading is None:
        heading = body.find(".//h1")
    title = "" if heading is None else "".join(heading.itertext()).strip()
    if not title:
        raise SourceError(f"XHTML title is missing: {href}")
    return body, title


def read_epub(path: Path) -> EpubBook:
    """Return chapter documents in EPUB spine order.

    The parser rejects incomplete references rather than silently omitting text.
    """

    try:
        archive = zipfile.ZipFile(path)
    except (FileNotFoundError, zipfile.BadZipFile) as exc:
        raise SourceError(f"cannot open EPUB {path}: {exc}") from exc

    with archive:
        container = _read_xml(archive, "META-INF/container.xml")
        rootfile_node = container.find(f".//{{{CONTAINER_NS}}}rootfile")
        if rootfile_node is None or not rootfile_node.get("full-path"):
            raise SourceError("EPUB container does not declare a rootfile")
        rootfile = rootfile_node.get("full-path", "")
        package = _read_xml(archive, rootfile)
        package_dir = posixpath.dirname(rootfile)

        manifest: dict[str, str] = {}
        for item in package.findall(f".//{{{OPF_NS}}}manifest/{{{OPF_NS}}}item"):
            item_id = item.get("id")
            href = item.get("href")
            if not item_id or not href:
                raise SourceError("EPUB manifest item is missing id or href")
            if item_id in manifest:
                raise SourceError(f"duplicate EPUB manifest id: {item_id}")
            manifest[item_id] = href

        chapters: list[ChapterSource] = []
        frontmatter: list[DocumentSource] = []
        seen_chapters: set[int] = set()
        for itemref in package.findall(f".//{{{OPF_NS}}}spine/{{{OPF_NS}}}itemref"):
            item_id = itemref.get("idref", "")
            if item_id not in manifest:
                raise SourceError(f"spine item {item_id} is missing from manifest")

            href = manifest[item_id].split("#", 1)[0]
            archive_href = posixpath.normpath(posixpath.join(package_dir, href))
            document = _read_xml(archive, archive_href)
            body, title = _document_body_and_title(document, href)
            match = CHAPTER_ID.fullmatch(item_id)
            if match is None:
                frontmatter.append(DocumentSource(item_id, href, title, body))
                continue

            chapter_id = int(match.group("id"))
            if chapter_id in seen_chapters:
                raise SourceError(f"duplicate chapter id in spine: {chapter_id}")
            seen_chapters.add(chapter_id)
            chapters.append(ChapterSource(chapter_id, href, title, body))

    return EpubBook(rootfile, tuple(chapters), tuple(frontmatter))
