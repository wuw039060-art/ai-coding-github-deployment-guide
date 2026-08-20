from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts.booklib.epub_source import SourceError, read_epub


CONTAINER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
  <rootfiles>
    <rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml" />
  </rootfiles>
</container>
"""


def build_epub(
    directory: Path,
    chapters: list[tuple[int, str]],
    *,
    missing_manifest_id: int | None = None,
    malformed_id: int | None = None,
    include_untitled_cover: bool = False,
) -> Path:
    epub_path = directory / "fixture.epub"
    manifest_items = []
    spine_items = []
    documents: dict[str, str] = {}

    for chapter_id, title in chapters:
        item_id = f"ch{chapter_id:03d}"
        href = f"text/{item_id}.xhtml"
        if chapter_id != missing_manifest_id:
            manifest_items.append(
                f'<item id="{item_id}" href="{href}" media-type="application/xhtml+xml" />'
            )
        spine_items.append(f'<itemref idref="{item_id}" />')
        documents[href] = (
            "<html xmlns=\"http://www.w3.org/1999/xhtml\"><body>"
            f"<h1>{title}</h1><p>chapter {chapter_id}</p></body></html>"
        )

    if include_untitled_cover:
        manifest_items.insert(
            0,
            '<item id="cover" href="text/cover.xhtml" media-type="application/xhtml+xml" />',
        )
        spine_items.insert(0, '<itemref idref="cover" />')
        documents["text/cover.xhtml"] = (
            '<html xmlns="http://www.w3.org/1999/xhtml"><body>'
            '<img src="../assets/cover.png" alt="封面"/></body></html>'
        )

    if malformed_id is not None:
        documents[f"text/ch{malformed_id:03d}.xhtml"] = "<html><body><h1>broken"

    package = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0">
  <manifest>{''.join(manifest_items)}</manifest>
  <spine>{''.join(spine_items)}</spine>
</package>
"""

    with zipfile.ZipFile(epub_path, "w") as archive:
        archive.writestr("META-INF/container.xml", CONTAINER_XML)
        archive.writestr("OEBPS/package.opf", package)
        for href, document in documents.items():
            archive.writestr(f"OEBPS/{href}", document)
    return epub_path


class ReadEpubTests(unittest.TestCase):
    def test_returns_numbered_chapters_in_spine_order(self):
        """A parser that sorts filenames instead of following the spine must fail."""
        with tempfile.TemporaryDirectory() as temp_dir:
            epub = build_epub(Path(temp_dir), [(2, "第二章"), (1, "第一章")])

            book = read_epub(epub)

        self.assertEqual([chapter.id for chapter in book.chapters], [2, 1])
        self.assertEqual([chapter.title for chapter in book.chapters], ["第二章", "第一章"])

    def test_rejects_spine_reference_missing_from_manifest(self):
        """Silently skipping an unresolved spine item would lose a chapter."""
        with tempfile.TemporaryDirectory() as temp_dir:
            epub = build_epub(Path(temp_dir), [(1, "第一章")], missing_manifest_id=1)

            with self.assertRaisesRegex(SourceError, "spine.*ch001.*manifest"):
                read_epub(epub)

    def test_rejects_malformed_chapter_xhtml_with_filename(self):
        """A broken chapter must name the source file instead of disappearing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            epub = build_epub(Path(temp_dir), [(1, "第一章")], malformed_id=1)

            with self.assertRaisesRegex(SourceError, "text/ch001.xhtml"):
                read_epub(epub)

    def test_accepts_frontmatter_without_a_heading(self):
        """A cover can be valid XHTML even though it has no editorial title."""
        with tempfile.TemporaryDirectory() as temp_dir:
            epub = build_epub(
                Path(temp_dir), [(1, "第一章")], include_untitled_cover=True
            )

            book = read_epub(epub)

        self.assertEqual(book.frontmatter[0].id, "cover")
        self.assertEqual(book.frontmatter[0].title, "")


if __name__ == "__main__":
    unittest.main()
