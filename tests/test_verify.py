from pathlib import Path
import tempfile
import unittest

from scripts.booklib.source_writer import write_source
from scripts.booklib.verify import verify_source
from tests.test_epub_source import build_epub


class VerifySourceTests(unittest.TestCase):
    def test_rejects_missing_chapter_and_broken_image(self):
        """A complete manifest must not hide a missing file or an unresolved asset."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            chapters = [(number, f"第 {number} 章 标题") for number in range(1, 105)]
            epub = build_epub(root, chapters)
            book = root / "book"
            manifest = write_source(epub, book)
            missing = book / manifest["chapters"][53]["source"]
            missing.unlink()
            first = book / manifest["chapters"][0]["source"]
            first.write_text(
                first.read_text(encoding="utf-8")
                + "\n![缺失](../assets/diagrams/missing.png)\n",
                encoding="utf-8",
            )
            txt = root / "book.txt"
            txt.write_text("校对基准", encoding="utf-8")

            report = verify_source(book, epub, txt)

            self.assertTrue(any("missing chapter source" in item and "054" in item for item in report.errors))
            self.assertTrue(any("missing image" in item for item in report.errors))

    def test_accepts_a_complete_recovered_fixture(self):
        """Correct numbering and faithful recovered text should pass without errors."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            chapters = [(number, f"第 {number} 章 标题") for number in range(1, 105)]
            epub = build_epub(
                root,
                chapters,
                chapter_bodies={
                    12: "<h1><code>.gitignore</code> 与秘密</h1><p>chapter 12</p>"
                },
            )
            book = root / "book"
            write_source(epub, book)
            txt = root / "book.txt"
            txt.write_text("".join(f"chapter {number}" for number in range(1, 105)), encoding="utf-8")

            report = verify_source(book, epub, txt)

            self.assertEqual(report.errors, ())
            self.assertEqual(report.metrics["chapter_count"], 104)
            self.assertLessEqual(report.metrics["epub_text_delta_percent"], 0.5)


if __name__ == "__main__":
    unittest.main()
