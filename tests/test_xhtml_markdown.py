import unittest
import xml.etree.ElementTree as ET

from scripts.booklib.xhtml_markdown import to_markdown


def parse_body(fragment: str) -> ET.Element:
    document = ET.fromstring(
        f'<html xmlns="http://www.w3.org/1999/xhtml"><body>{fragment}</body></html>'
    )
    body = document.find("{http://www.w3.org/1999/xhtml}body")
    assert body is not None
    return body


class XhtmlMarkdownTests(unittest.TestCase):
    def test_converts_headings_paragraphs_and_inline_emphasis(self):
        """Dropping inline markup or heading levels would change chapter meaning."""
        body = parse_body(
            "<h1>第 1 章 标题</h1>"
            "<h2>判断边界</h2>"
            "<p>普通 <strong>重点</strong>、<em>术语</em> 与 <code>x = 1</code>。</p>"
        )

        text = to_markdown(body, "text/ch001.xhtml")

        self.assertEqual(
            text,
            "# 第 1 章 标题\n\n## 判断边界\n\n普通 **重点**、*术语* 与 `x = 1`。\n",
        )

    def test_preserves_links_and_figure_meaning(self):
        """A converter that keeps text but loses destinations or alt text is lossy."""
        body = parse_body(
            "<p>继续阅读 <a href='ch002.xhtml#check'>第 2 章</a>。</p>"
            "<figure><img src='../assets/diagrams/map.png' alt='发布地图'/>"
            "<figcaption>从本地到用户</figcaption></figure>"
        )

        text = to_markdown(body, "text/ch001.xhtml")

        self.assertEqual(
            text,
            "继续阅读 [第 2 章](ch002.xhtml#check)。\n\n"
            "![发布地图](../assets/diagrams/map.png)\n\n*从本地到用户*\n",
        )

    def test_converts_lists_without_flattening_order(self):
        """Changing an ordered procedure into plain paragraphs is a content bug."""
        body = parse_body(
            "<ul><li>位置</li><li>证据</li></ul>"
            "<ol><li>先备份</li><li>再修改</li></ol>"
        )

        text = to_markdown(body, "text/ch001.xhtml")

        self.assertEqual(text, "- 位置\n- 证据\n\n1. 先备份\n2. 再修改\n")

    def test_converts_each_blockquote_line(self):
        """Only prefixing the first line would leak part of a warning outside its box."""
        body = parse_body(
            "<blockquote><p>证据边界</p><p>成功不代表用户可用。</p></blockquote>"
        )

        text = to_markdown(body, "text/ch001.xhtml")

        self.assertEqual(text, "> 证据边界\n>\n> 成功不代表用户可用。\n")

    def test_converts_tables_and_preformatted_code(self):
        """Flattening table cells or code newlines would corrupt operational evidence."""
        body = parse_body(
            "<table><thead><tr><th>项目</th><th>证据</th></tr></thead>"
            "<tbody><tr><td>构建</td><td><code>exit 0</code></td></tr></tbody></table>"
            "<pre><code>git status\ngit diff</code></pre>"
        )

        text = to_markdown(body, "text/ch001.xhtml")

        self.assertEqual(
            text,
            "| 项目 | 证据 |\n| --- | --- |\n| 构建 | `exit 0` |\n\n"
            "```\ngit status\ngit diff\n```\n",
        )

    def test_removes_epub_chapter_navigation(self):
        """EPUB previous/next controls must not become editorial chapter content."""
        body = parse_body(
            "<p>正文。</p><nav class='chapter-nav'><a href='nav.xhtml'>返回目录</a></nav>"
        )

        text = to_markdown(body, "text/ch001.xhtml")

        self.assertEqual(text, "正文。\n")


if __name__ == "__main__":
    unittest.main()
