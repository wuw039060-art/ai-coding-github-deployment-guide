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


if __name__ == "__main__":
    unittest.main()
