import json
from pathlib import Path
import tempfile
import unittest

from scripts.booklib.audit import audit_source


class AuditSourceTests(unittest.TestCase):
    def test_reports_exact_duplicate_paragraphs_over_80_characters(self):
        """Long copy-pasted prose in two chapters must be visible before editing starts."""
        repeated = "这是一个用于验证完全重复检测的长段落，它必须足够长并且在两个章节中逐字一致。" * 4
        with tempfile.TemporaryDirectory() as temp_dir:
            book = Path(temp_dir) / "book"
            chapters = book / "chapters"
            chapters.mkdir(parents=True)
            entries = []
            for chapter_id in (1, 2):
                source = f"chapters/{chapter_id:03d}-chapter.md"
                (book / source).write_text(
                    f"# 第 {chapter_id} 章\n\n{repeated}\n", encoding="utf-8"
                )
                entries.append(
                    {
                        "id": chapter_id,
                        "volume": 1,
                        "part": None,
                        "title": f"第 {chapter_id} 章",
                        "source": source,
                        "level": "core",
                        "volatile_facts": [],
                        "reference_links": [],
                    }
                )
            (book / "manifest.json").write_text(
                json.dumps({"chapters": entries}, ensure_ascii=False), encoding="utf-8"
            )

            report = audit_source(book)

            self.assertEqual(len(report.exact_duplicates), 1)
            duplicate = report.exact_duplicates[0]
            self.assertEqual(duplicate.chapter_ids, (1, 2))
            self.assertGreater(len(duplicate.text), 80)

    def test_volatile_scan_keeps_versions_and_policies_but_ignores_plain_current(self):
        """The word 当前 alone is too common to be a useful fact-verification signal."""
        with tempfile.TemporaryDirectory() as temp_dir:
            book = Path(temp_dir) / "book"
            (book / "chapters").mkdir(parents=True)
            source = "chapters/001-chapter.md"
            (book / source).write_text(
                "# 标题\n\n当前目录不等于仓库。\n\nGoogle Play 审核政策可能变化。\n\nNode.js v22 需要核验。\n",
                encoding="utf-8",
            )
            entry = {
                "id": 1,
                "volume": 1,
                "part": None,
                "title": "标题",
                "source": source,
                "level": "core",
                "volatile_facts": [],
                "reference_links": [],
            }
            (book / "manifest.json").write_text(
                json.dumps({"chapters": [entry]}, ensure_ascii=False), encoding="utf-8"
            )

            report = audit_source(book)

            self.assertEqual(len(report.volatile_candidates), 2)
            self.assertFalse(
                any("当前目录" in item.text for item in report.volatile_candidates)
            )


if __name__ == "__main__":
    unittest.main()
