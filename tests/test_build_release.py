from pathlib import Path
from unittest.mock import patch
import tempfile
import unittest
import zipfile

from scripts.build_release import BOOK, book_contents, pandoc, remove_navigation_from_reading_order


class EpubReleaseTests(unittest.TestCase):
    def test_visible_contents_lists_every_numbered_chapter(self):
        contents = book_contents()
        self.assertIn("# 目录 {#contents}", contents)
        self.assertEqual(contents.count("](#ch-"), 104)

    def test_epub_uses_one_custom_title_page(self):
        with patch("scripts.build_release.subprocess.run") as run:
            pandoc(Path("book.md"), Path("book.epub"), fmt="epub", toc=True)

        command = run.call_args.args[0]
        self.assertIn("--epub-title-page=false", command)
        self.assertIn(str(BOOK / "assets" / "styles" / "v2.3-epub.css"), command)

    def test_epub_styles_do_not_force_extra_pages(self):
        css = (BOOK / "assets" / "styles" / "v2.3-epub.css").read_text(encoding="utf-8")
        self.assertNotIn("break-before: page", css)
        self.assertNotIn("page-break-before: always", css)
        self.assertNotIn("page-break-inside: avoid", css)

    def test_navigation_does_not_consume_body_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            epub = Path(directory) / "book.epub"
            with zipfile.ZipFile(epub, "w") as archive:
                archive.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
                archive.writestr(
                    "EPUB/content.opf",
                    '<spine><itemref idref="cover_xhtml" /><itemref idref="nav" />'
                    '<itemref idref="ch001_xhtml" /></spine>',
                )
                archive.writestr("EPUB/nav.xhtml", "<nav>Directory</nav>")

            remove_navigation_from_reading_order(epub)

            with zipfile.ZipFile(epub) as archive:
                spine = archive.read("EPUB/content.opf").decode()
                self.assertIn('<itemref idref="nav" linear="no" />', spine)
                self.assertIn('<itemref idref="ch001_xhtml" />', spine)
                self.assertEqual(archive.namelist()[0], "mimetype")
                self.assertEqual(archive.getinfo("mimetype").compress_type, zipfile.ZIP_STORED)


if __name__ == "__main__":
    unittest.main()
