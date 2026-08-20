from hashlib import sha256
import json
from pathlib import Path
import tempfile
import unittest

from scripts.booklib.source_writer import SourceWriteError, write_source
from tests.test_epub_source import build_epub


def tree_digest(root: Path) -> str:
    digest = sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


class SourceWriterTests(unittest.TestCase):
    def test_generates_deterministic_chapters_and_manifest(self):
        """Nondeterministic filenames or JSON would make editorial diffs untrustworthy."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            epub = build_epub(root, [(1, "第 1 章 软件来到用户面前"), (69, "第 69 章 安全协作")])
            output = root / "book"

            first = write_source(epub, output)
            first_digest = tree_digest(output)
            second = write_source(epub, output)

            self.assertEqual(first, second)
            self.assertEqual(first_digest, tree_digest(output))
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual([item["id"] for item in manifest["chapters"]], [1, 69])
            self.assertEqual(manifest["chapters"][0]["volume"], 1)
            self.assertEqual(manifest["chapters"][1]["part"], "与 AI 安全协作")
            self.assertTrue((output / manifest["chapters"][0]["source"]).is_file())

    def test_refuses_to_replace_an_edited_source_tree(self):
        """Rerunning recovery must not erase editorial work made after extraction."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            epub = build_epub(root, [(1, "第 1 章 标题")])
            output = root / "book"
            write_source(epub, output)
            chapter = next((output / "chapters").glob("001-*.md"))
            chapter.write_text("作者修改\n", encoding="utf-8")

            with self.assertRaisesRegex(SourceWriteError, "refusing to replace"):
                write_source(epub, output)

    def test_rewrites_internal_links_and_copies_referenced_assets(self):
        """Recovered Markdown must not retain XHTML links or point at absent images."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            epub = build_epub(
                root,
                [(1, "第 1 章 起点"), (2, "第 2 章 终点")],
                chapter_bodies={
                    1: (
                        "<h1>第 1 章 起点</h1>"
                        "<p><a href='ch002.xhtml#check'>第 2 章</a></p>"
                        "<figure><img src='../assets/diagrams/map.png' alt='地图'/></figure>"
                    )
                },
                assets={"assets/diagrams/map.png": b"png-fixture"},
            )

            manifest = write_source(epub, root / "book")

            chapter_path = root / "book" / manifest["chapters"][0]["source"]
            target_name = Path(manifest["chapters"][1]["source"]).name
            text = chapter_path.read_text(encoding="utf-8")
            self.assertIn(f"]({target_name}#check)", text)
            self.assertNotIn(".xhtml", text)
            self.assertTrue((root / "book/assets/diagrams/map.png").is_file())


if __name__ == "__main__":
    unittest.main()
