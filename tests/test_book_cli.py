import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_epub_source import build_epub


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class BookCliTests(unittest.TestCase):
    def test_source_command_generates_requested_output(self):
        """The public CLI must call the same safe generator used by tests."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            epub = build_epub(root, [(1, "第 1 章 标题")])
            output = root / "book"

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPOSITORY_ROOT / "scripts/book.py"),
                    "source",
                    "--epub",
                    str(epub),
                    "--output",
                    str(output),
                ],
                cwd=REPOSITORY_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            summary = json.loads(result.stdout)
            self.assertEqual(summary["chapters"], 1)
            self.assertTrue((output / "manifest.json").is_file())

    def test_verify_command_writes_a_human_readable_report(self):
        """Verification must be usable from Make and leave reviewable evidence."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            chapters = [(number, f"第 {number} 章 标题") for number in range(1, 105)]
            epub = build_epub(root, chapters)
            book = root / "book"
            from scripts.booklib.source_writer import write_source

            write_source(epub, book)
            txt = root / "book.txt"
            txt.write_text("".join(f"chapter {number}" for number in range(1, 105)), encoding="utf-8")
            report = root / "VERIFICATION.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPOSITORY_ROOT / "scripts/book.py"),
                    "verify",
                    "--version",
                    "2.3.0",
                    "--book",
                    str(book),
                    "--epub",
                    str(epub),
                    "--txt",
                    str(txt),
                    "--report",
                    str(report),
                ],
                cwd=REPOSITORY_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PASS", report.read_text(encoding="utf-8"))
            self.assertIn('"errors": 0', result.stdout)

    def test_audit_command_writes_baseline_tables(self):
        """The audit CLI must preserve chapter and volume baselines for editors."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            epub = build_epub(root, [(1, "第 1 章 标题")])
            book = root / "book"
            from scripts.booklib.source_writer import write_source

            write_source(epub, book)
            report = root / "AUDIT-v2.3.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPOSITORY_ROOT / "scripts/book.py"),
                    "audit",
                    "--version",
                    "2.3.0",
                    "--book",
                    str(book),
                    "--report",
                    str(report),
                ],
                cwd=REPOSITORY_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            text = report.read_text(encoding="utf-8")
            self.assertIn("## Volume baseline", text)
            self.assertIn("## Chapter baseline", text)
            self.assertIn("| 001 |", text)


if __name__ == "__main__":
    unittest.main()
