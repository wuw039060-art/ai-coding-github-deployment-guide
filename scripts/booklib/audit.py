"""Read-only editorial baseline audit for the recovered book source."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re

from .verify import CHAPTER_REFERENCE, IMAGE_LINK, NORMAL_LINK, _markdown_visible


RISK_PATTERNS = (
    (re.compile(r"(?:^|\s)(?:sudo|rm)(?:\s|$)"), "privileged or destructive shell command"),
    (re.compile(r"docker\s+system\s+prune", re.IGNORECASE), "Docker bulk cleanup"),
    (re.compile(r"\bDROP\s+(?:TABLE|DATABASE)\b", re.IGNORECASE), "destructive SQL"),
    (re.compile(r"\b(?:ufw|iptables|firewall-cmd)\b"), "firewall change"),
    (re.compile(r"\b(?:migrate|migration|数据库迁移)\b", re.IGNORECASE), "database migration"),
)
VOLATILE_PATTERN = re.compile(
    r"(?:截至|价格|费用|政策|配额|免费额度|审核要求|支持版本|\b20\d{2}年|\bv\d+(?:\.\d+){0,2}\b|\b\d+\.\d+(?:\.\d+)?\b)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ChapterStats:
    id: int
    volume: int
    title: str
    source: str
    visible_chars: int
    paragraphs: int
    code_blocks: int
    images: int
    links: int


@dataclass(frozen=True)
class DuplicateParagraph:
    text: str
    chapter_ids: tuple[int, ...]
    locations: tuple[str, ...]


@dataclass(frozen=True)
class Finding:
    chapter_id: int
    source: str
    line: int
    reason: str
    text: str


@dataclass(frozen=True)
class AuditReport:
    chapters: tuple[ChapterStats, ...]
    volume_chars: dict[int, int]
    total_chars: int
    exact_duplicates: tuple[DuplicateParagraph, ...]
    risk_candidates: tuple[Finding, ...]
    volatile_candidates: tuple[Finding, ...]
    invalid_references: tuple[Finding, ...]


def _paragraphs(markdown: str) -> list[tuple[int, str]]:
    paragraphs: list[tuple[int, str]] = []
    line_number = 1
    for block in re.split(r"\n\s*\n", markdown):
        stripped = block.strip()
        if stripped:
            paragraphs.append((line_number, re.sub(r"\s+", " ", stripped)))
        line_number += block.count("\n") + 2
    return paragraphs


def audit_source(book_dir: Path) -> AuditReport:
    book_dir = book_dir.resolve()
    manifest = json.loads((book_dir / "manifest.json").read_text(encoding="utf-8"))
    stats: list[ChapterStats] = []
    volume_chars: defaultdict[int, int] = defaultdict(int)
    paragraph_occurrences: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)
    risks: list[Finding] = []
    volatile: list[Finding] = []
    invalid_references: list[Finding] = []

    for item in manifest["chapters"]:
        chapter_id = int(item["id"])
        source_name = item["source"]
        markdown = (book_dir / source_name).read_text(encoding="utf-8")
        visible_chars = len(re.sub(r"\s+", "", _markdown_visible(markdown)))
        paragraphs = _paragraphs(markdown)
        chapter_stats = ChapterStats(
            id=chapter_id,
            volume=int(item["volume"]),
            title=item["title"],
            source=source_name,
            visible_chars=visible_chars,
            paragraphs=len(paragraphs),
            code_blocks=len(re.findall(r"^```", markdown, flags=re.MULTILINE)) // 2,
            images=len(IMAGE_LINK.findall(markdown)),
            links=len(NORMAL_LINK.findall(markdown)),
        )
        stats.append(chapter_stats)
        volume_chars[chapter_stats.volume] += visible_chars

        for line, paragraph in paragraphs:
            visible = re.sub(r"\s+", "", _markdown_visible(paragraph))
            if len(visible) > 80 and not paragraph.startswith(("#", "```", "|")):
                paragraph_occurrences[visible].append(
                    (chapter_id, f"{source_name}:{line}")
                )

        in_code_block = False
        for line_number, line in enumerate(markdown.splitlines(), start=1):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
            for pattern, reason in RISK_PATTERNS:
                if pattern.search(line):
                    risks.append(
                        Finding(chapter_id, source_name, line_number, reason, line.strip())
                    )
                    break
            if VOLATILE_PATTERN.search(line):
                volatile.append(
                    Finding(
                        chapter_id,
                        source_name,
                        line_number,
                        "time-sensitive fact candidate",
                        line.strip(),
                    )
                )
            if not in_code_block:
                for target in CHAPTER_REFERENCE.findall(line):
                    if int(target) not in range(1, 105):
                        invalid_references.append(
                            Finding(
                                chapter_id,
                                source_name,
                                line_number,
                                f"missing chapter {target}",
                                line.strip(),
                            )
                        )

    duplicates = []
    for text, occurrences in paragraph_occurrences.items():
        chapter_ids = tuple(sorted({chapter_id for chapter_id, _ in occurrences}))
        if len(chapter_ids) < 2:
            continue
        duplicates.append(
            DuplicateParagraph(
                text=text,
                chapter_ids=chapter_ids,
                locations=tuple(location for _, location in occurrences),
            )
        )
    duplicates.sort(key=lambda item: (-len(item.text), item.chapter_ids))

    return AuditReport(
        chapters=tuple(sorted(stats, key=lambda item: item.id)),
        volume_chars=dict(sorted(volume_chars.items())),
        total_chars=sum(item.visible_chars for item in stats),
        exact_duplicates=tuple(duplicates),
        risk_candidates=tuple(risks),
        volatile_candidates=tuple(volatile),
        invalid_references=tuple(invalid_references),
    )
