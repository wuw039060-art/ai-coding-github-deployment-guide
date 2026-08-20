import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def write_fixture(root: Path, *, volume_1_chars: int = 100, volume_2_chars: int = 250):
    book = root / "book"
    (book / "chapters").mkdir(parents=True)
    entries = []
    for chapter_id, volume, visible_chars in (
        (1, 1, volume_1_chars),
        (2, 2, volume_2_chars),
    ):
        title = f"章节{chapter_id}"
        source = f"chapters/{chapter_id:03d}.md"
        heading_chars = len(title)
        (book / source).write_text(
            f"# {title}\n\n" + "字" * (visible_chars - heading_chars) + "\n",
            encoding="utf-8",
        )
        entries.append(
            {
                "id": chapter_id,
                "volume": volume,
                "title": title,
                "source": source,
                "level": "core",
            }
        )
    (book / "manifest.json").write_text(
        json.dumps({"chapters": entries}, ensure_ascii=False), encoding="utf-8"
    )
    plan = root / "editorial-plan.json"
    plan.write_text(
        json.dumps(
            {
                "version": "test",
                "baseline_visible_chars": 400,
                "target_total": {"minimum": 290, "maximum": 330},
                "volumes": [
                    {"id": 1, "baseline": 150, "minimum": 90, "maximum": 110},
                    {"id": 2, "baseline": 250, "minimum": 180, "maximum": 220},
                ],
            }
        ),
        encoding="utf-8",
    )
    return book, plan


def editorial_api():
    try:
        from scripts.booklib.editorial import evaluate_editorial, load_editorial_plan
    except ImportError as exc:
        raise AssertionError("editorial progress API is missing") from exc
    return evaluate_editorial, load_editorial_plan


class EditorialProgressTests(unittest.TestCase):
    def test_completed_volume_passes_without_blocking_on_pending_volume(self):
        """A later unfinished volume outside budget must not block a completed batch."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book, plan_path = write_fixture(root)
            evaluate_editorial, load_editorial_plan = editorial_api()

            report = evaluate_editorial(
                book, load_editorial_plan(plan_path), frozenset({1})
            )

            self.assertEqual(report.errors, ())
            self.assertEqual(report.volumes[0].status, "PASS")
            self.assertEqual(report.volumes[1].status, "PENDING")

    def test_completed_volume_outside_range_is_an_error(self):
        """Declaring a volume complete must enforce its own literal target range."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book, plan_path = write_fixture(root, volume_1_chars=80)
            evaluate_editorial, load_editorial_plan = editorial_api()

            report = evaluate_editorial(
                book, load_editorial_plan(plan_path), frozenset({1})
            )

            self.assertTrue(
                any("volume 1" in item and "outside 90-110" in item for item in report.errors)
            )

    def test_full_completion_enforces_total_range(self):
        """Individually valid volumes cannot bypass the full-book total requirement."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book, plan_path = write_fixture(
                root, volume_1_chars=100, volume_2_chars=200
            )
            evaluate_editorial, load_editorial_plan = editorial_api()
            plan = load_editorial_plan(plan_path)
            plan_path.write_text(
                plan_path.read_text(encoding="utf-8").replace(
                    '"minimum": 290, "maximum": 330',
                    '"minimum": 310, "maximum": 330',
                ),
                encoding="utf-8",
            )
            plan = load_editorial_plan(plan_path)

            report = evaluate_editorial(book, plan, frozenset({1, 2}))

            self.assertTrue(any("total visible characters 300" in item for item in report.errors))

    def test_rejects_unknown_completed_volume(self):
        """A misspelled volume ID must fail instead of silently weakening the gate."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book, plan_path = write_fixture(root)
            evaluate_editorial, load_editorial_plan = editorial_api()

            with self.assertRaisesRegex(ValueError, "unknown completed volume.*3"):
                evaluate_editorial(
                    book, load_editorial_plan(plan_path), frozenset({3})
                )

    def test_cli_writes_reviewable_report_and_uses_failure_exit_code(self):
        """Batch automation must receive a nonzero exit and a human-readable reason."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book, plan = write_fixture(root, volume_1_chars=80)
            report = root / "EDITORIAL.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPOSITORY_ROOT / "scripts/book.py"),
                    "progress",
                    "--book",
                    str(book),
                    "--plan",
                    str(plan),
                    "--completed-volumes",
                    "1",
                    "--report",
                    str(report),
                ],
                cwd=REPOSITORY_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 1, result.stderr)
            text = report.read_text(encoding="utf-8")
            self.assertIn("**Status:** FAIL", text)
            self.assertIn("| 1 | 150 | 80 |", text)
            self.assertIn("volume 1 visible characters 80 outside 90-110", text)


if __name__ == "__main__":
    unittest.main()
