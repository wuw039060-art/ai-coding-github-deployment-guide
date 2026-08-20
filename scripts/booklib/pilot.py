"""Acceptance checks for the v2.3 six-chapter reduction pilot."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re

from .verify import NORMAL_LINK, _markdown_visible, _relative_target


@dataclass(frozen=True)
class PilotSpec:
    id: int
    title: str
    source: str
    baseline_chars: int
    minimum_chars: int
    maximum_chars: int


@dataclass(frozen=True)
class PilotChapterResult:
    spec: PilotSpec
    visible_chars: int

    @property
    def reduction_percent(self) -> float:
        return (self.spec.baseline_chars - self.visible_chars) / self.spec.baseline_chars * 100


@dataclass(frozen=True)
class PilotReport:
    chapters: tuple[PilotChapterResult, ...]
    errors: tuple[str, ...]


PILOT_SPECS = (
    PilotSpec(1, "从本地文件到公开可用的产品", "chapters/001-从本地文件到公开可用的产品.md", 8364, 4600, 5018),
    PilotSpec(19, "浏览器开发者工具、状态码和网络请求", "chapters/019-浏览器开发者工具-状态码和网络请求.md", 8825, 4854, 5295),
    PilotSpec(40, "systemd、systemctl、journalctl 和服务日志", "chapters/040-systemd-systemctl-journalctl-和服务日志.md", 11399, 6269, 6839),
    PilotSpec(54, "Google Play 内部测试与发布流程", "chapters/054-google-play-内部测试与发布流程.md", 9316, 5124, 5590),
    PilotSpec(70, "计划、权限、Diff、测试和验证证据", "chapters/070-计划-权限-diff-测试和验证证据.md", 8795, 4837, 5277),
    PilotSpec(91, "SLI、SLO、SLA 与 Error Budget", "chapters/091-sli-slo-sla-与-error-budget.md", 5015, 2758, 3009),
)


def validate_pilot(book_dir: Path) -> PilotReport:
    book_dir = book_dir.resolve()
    errors: list[str] = []
    results: list[PilotChapterResult] = []
    try:
        manifest = json.loads((book_dir / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return PilotReport((), (f"invalid manifest: {exc}",))
    entries = {
        item.get("id"): item
        for item in manifest.get("chapters", [])
        if isinstance(item, dict)
    }

    for spec in PILOT_SPECS:
        entry = entries.get(spec.id)
        if entry is None:
            errors.append(f"chapter {spec.id:03d} missing from manifest")
            continue
        if entry.get("title") != spec.title:
            errors.append(f"chapter {spec.id:03d} title differs from pilot baseline")
        if entry.get("source") != spec.source:
            errors.append(f"chapter {spec.id:03d} source differs from pilot baseline")
        source = book_dir / spec.source
        if not source.is_file():
            errors.append(f"chapter {spec.id:03d} source is missing: {spec.source}")
            continue
        markdown = source.read_text(encoding="utf-8")
        heading = re.search(r"^#\s+(.+?)\s*$", markdown, flags=re.MULTILINE)
        heading_text = "" if heading is None else _markdown_visible(heading.group(1)).strip()
        if heading_text != spec.title:
            errors.append(f"chapter {spec.id:03d} heading differs from pilot baseline")
        visible_chars = len(re.sub(r"\s+", "", _markdown_visible(markdown)))
        results.append(PilotChapterResult(spec, visible_chars))
        if not spec.minimum_chars <= visible_chars <= spec.maximum_chars:
            errors.append(
                f"chapter {spec.id:03d} visible characters {visible_chars} "
                f"outside {spec.minimum_chars}-{spec.maximum_chars}"
            )
        for href in NORMAL_LINK.findall(markdown):
            target = _relative_target(source, href)
            if target is not None and not target.is_file():
                errors.append(f"broken link in chapter {spec.id:03d}: {href}")

    return PilotReport(tuple(results), tuple(errors))
