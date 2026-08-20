import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PILOT_CHAPTERS = (
    (1, "从本地文件到公开可用的产品", "chapters/001-从本地文件到公开可用的产品.md", 4600),
    (19, "浏览器开发者工具、状态码和网络请求", "chapters/019-浏览器开发者工具-状态码和网络请求.md", 4854),
    (40, "systemd、systemctl、journalctl 和服务日志", "chapters/040-systemd-systemctl-journalctl-和服务日志.md", 6269),
    (54, "Google Play 内部测试与发布流程", "chapters/054-google-play-内部测试与发布流程.md", 5124),
    (70, "计划、权限、Diff、测试和验证证据", "chapters/070-计划-权限-diff-测试和验证证据.md", 4837),
    (91, "SLI、SLO、SLA 与 Error Budget", "chapters/091-sli-slo-sla-与-error-budget.md", 2758),
)


def write_pilot_fixture(root: Path) -> Path:
    book = root / "book"
    (book / "chapters").mkdir(parents=True)
    references = root / "references"
    references.mkdir()
    (references / "guide.md").write_text("# 参考", encoding="utf-8")
    manifest = {"chapters": []}
    for chapter_id, title, source_name, target in PILOT_CHAPTERS:
        manifest["chapters"].append(
            {"id": chapter_id, "title": title, "source": source_name}
        )
        visible_title = len("".join(title.split()))
        link_label = "继续查"
        filler = "字" * (target - visible_title - len(link_label))
        (book / source_name).write_text(
            f"# {title}\n\n{filler}\n\n[{link_label}](../../references/guide.md)\n",
            encoding="utf-8",
        )
    (book / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
    )
    return book


class PilotCliTests(unittest.TestCase):
    def test_accepts_each_chapter_at_its_inclusive_lower_bound(self):
        """Using a shared total must not hide a chapter outside its own range."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book = write_pilot_fixture(root)
            report = root / "PILOT.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPOSITORY_ROOT / "scripts/book.py"),
                    "pilot",
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
            self.assertIn("**Status:** PASS", report.read_text(encoding="utf-8"))
            self.assertIn('"chapters": 6', result.stdout)

    def test_rejects_out_of_range_identity_changes_and_broken_links(self):
        """A pilot cannot pass by changing chapter identity or leaving moved details unreachable."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            book = write_pilot_fixture(root)
            manifest_path = book / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["chapters"][5]["title"] = "被替换的标题"
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            first = book / PILOT_CHAPTERS[0][2]
            first.write_text(
                first.read_text(encoding="utf-8") + "超" * 419,
                encoding="utf-8",
            )
            nineteenth = book / PILOT_CHAPTERS[1][2]
            nineteenth.write_text(
                nineteenth.read_text(encoding="utf-8")
                + "\n[坏链接](../../references/missing.md)\n",
                encoding="utf-8",
            )
            report = root / "PILOT.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPOSITORY_ROOT / "scripts/book.py"),
                    "pilot",
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

            self.assertEqual(result.returncode, 1, result.stderr)
            text = report.read_text(encoding="utf-8")
            self.assertIn("chapter 001 visible characters", text)
            self.assertIn("chapter 091 title differs from pilot baseline", text)
            self.assertIn("broken link in chapter 019", text)


if __name__ == "__main__":
    unittest.main()
