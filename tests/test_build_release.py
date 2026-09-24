from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts.build_release import remove_navigation_from_reading_order


class EpubReleaseTests(unittest.TestCase):
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
