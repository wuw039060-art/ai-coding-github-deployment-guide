"""Convert the semantic subset used by the v2.2 EPUB into Markdown."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET


class ConversionError(ValueError):
    """Raised when XHTML cannot be represented without silent data loss."""


def _tag(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def _inline(element: ET.Element) -> str:
    parts = [element.text or ""]
    for child in element:
        tag = _tag(child)
        content = _inline(child)
        if tag in {"strong", "b"}:
            parts.append(f"**{content}**")
        elif tag in {"em", "i"}:
            parts.append(f"*{content}*")
        elif tag == "code":
            parts.append(f"`{content}`")
        elif tag == "span":
            parts.append(content)
        elif tag == "a":
            href = child.get("href")
            if not href:
                raise ConversionError("XHTML link is missing href")
            parts.append(f"[{content}]({href})")
        else:
            raise ConversionError(f"unsupported inline XHTML tag: {tag}")
        parts.append(child.tail or "")
    return "".join(parts)


def _block(element: ET.Element) -> str:
    tag = _tag(element)
    if re.fullmatch(r"h[1-6]", tag):
        return f"{'#' * int(tag[1])} {_inline(element).strip()}"
    if tag == "p":
        return _inline(element).strip()
    if tag == "figure":
        image = next((child for child in element if _tag(child) == "img"), None)
        if image is None or not image.get("src"):
            raise ConversionError("XHTML figure is missing an image source")
        alt = image.get("alt", "")
        blocks = [f"![{alt}]({image.get('src')})"]
        caption = next(
            (child for child in element if _tag(child) == "figcaption"), None
        )
        if caption is not None:
            text = _inline(caption).strip()
            if text:
                blocks.append(f"*{text}*")
        return "\n\n".join(blocks)
    if tag in {"ul", "ol"}:
        lines = []
        for index, item in enumerate(element, start=1):
            if _tag(item) != "li":
                raise ConversionError(f"unexpected {tag} child: {_tag(item)}")
            marker = "-" if tag == "ul" else f"{index}."
            lines.append(f"{marker} {_inline(item).strip()}")
        return "\n".join(lines)
    if tag == "blockquote":
        quoted = "\n\n".join(_block(child) for child in element)
        return "\n".join(">" if not line else f"> {line}" for line in quoted.splitlines())
    if tag == "pre":
        code = "".join(element.itertext()).strip("\n")
        return f"```\n{code}\n```"
    if tag == "table":
        rows: list[list[str]] = []
        header_flags: list[bool] = []
        for row in (node for node in element.iter() if _tag(node) == "tr"):
            cells = [node for node in row if _tag(node) in {"th", "td"}]
            if not cells:
                continue
            rows.append([_inline(cell).strip().replace("|", "\\|") for cell in cells])
            header_flags.append(all(_tag(cell) == "th" for cell in cells))
        if not rows or not header_flags[0]:
            raise ConversionError("Markdown table requires a header row")
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            raise ConversionError("XHTML table rows have inconsistent cell counts")
        lines = [f"| {' | '.join(rows[0])} |", f"| {' | '.join(['---'] * width)} |"]
        lines.extend(f"| {' | '.join(row)} |" for row in rows[1:])
        return "\n".join(lines)
    if tag == "nav":
        return ""
    raise ConversionError(f"unsupported block XHTML tag: {tag}")


def to_markdown(body: ET.Element, source_href: str) -> str:
    """Serialize one XHTML body with stable whitespace and one final newline."""

    del source_href  # Reserved for relative-link validation and diagnostics.
    blocks = [_block(child) for child in body]
    content = "\n\n".join(block for block in blocks if block)
    return content.rstrip() + "\n"
