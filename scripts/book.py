#!/usr/bin/env python3
"""Command-line entry point for v2.3 book source operations."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.booklib.source_writer import SourceWriteError, write_source
from scripts.booklib.audit import AuditReport, audit_source
from scripts.booklib.pilot import PilotReport, validate_pilot
from scripts.booklib.verify import VerificationReport, verify_source


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="book.py")
    commands = parser.add_subparsers(dest="command", required=True)
    source = commands.add_parser("source", help="recover Markdown from an EPUB")
    source.add_argument("--epub", required=True, type=Path)
    source.add_argument("--output", default=Path("book"), type=Path)
    verify = commands.add_parser("verify", help="verify recovered Markdown")
    verify.add_argument("--version", required=True)
    verify.add_argument("--book", default=Path("book"), type=Path)
    verify.add_argument(
        "--epub", default=Path("AI 写代码之后-v2.2.0.epub"), type=Path
    )
    verify.add_argument("--txt", default=Path("AI 写代码之后-v2.2.0.txt"), type=Path)
    verify.add_argument("--report", default=Path("VERIFICATION.md"), type=Path)
    verify.add_argument(
        "--recovery-fidelity",
        action="store_true",
        help="fail when edited Markdown differs from the recovery EPUB by over 0.5%%",
    )
    audit = commands.add_parser("audit", help="freeze the editorial baseline")
    audit.add_argument("--version", required=True)
    audit.add_argument("--book", default=Path("book"), type=Path)
    audit.add_argument("--report", default=Path("AUDIT-v2.3.md"), type=Path)
    pilot = commands.add_parser("pilot", help="validate the six-chapter reduction pilot")
    pilot.add_argument("--book", default=Path("book"), type=Path)
    pilot.add_argument("--report", default=Path("PILOT-v2.3.md"), type=Path)
    return parser


def _file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _write_verification_report(
    report: VerificationReport,
    *,
    version: str,
    epub: Path,
    txt: Path,
    destination: Path,
) -> None:
    status = "PASS" if not report.errors else "FAIL"
    metrics = report.metrics
    lines = [
        f"# v{version} Verification",
        "",
        f"**Status:** {status}",
        "",
        "## Recovery baseline",
        "",
        f"- EPUB: `{epub.name}`",
        f"- EPUB SHA256: `{_file_sha256(epub)}`",
        f"- TXT: `{txt.name}`",
        f"- TXT SHA256: `{_file_sha256(txt)}`",
        f"- Chapters: {metrics.get('chapter_count', 0)}",
        f"- EPUB visible characters: {metrics.get('epub_visible_chars', 0)}",
        f"- Markdown visible characters: {metrics.get('markdown_visible_chars', 0)}",
        f"- EPUB/Markdown delta: {metrics.get('epub_text_delta_percent', 0)}%",
        f"- TXT non-whitespace characters: {metrics.get('txt_nonwhitespace_chars', 0)}",
        "",
        "## Errors",
        "",
    ]
    lines.extend(f"- {item}" for item in report.errors)
    if not report.errors:
        lines.append("- None")
    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {item}" for item in report.warnings)
    if not report.warnings:
        lines.append("- None")
    lines.extend(
        [
            "",
            "## Deferred v2.3 release checks",
            "",
            "- PDF page count, typography, blank final page and 104 bookmark targets",
            "- EPUB TOC and internal links rebuilt from the edited Markdown",
            "- Release assets, filenames and SHA256SUMS correspondence",
            "",
        ]
    )
    destination.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def _cell(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def _write_audit_report(
    report: AuditReport, *, version: str, book: Path, destination: Path
) -> None:
    page_targets = {
        1: "22–25",
        2: "36–40",
        3: "38–42",
        4: "34–38",
        5: "30–34",
        6: "42–48",
        7: "32–36",
        8: "40–46",
        9: "40–44",
        10: "90–100",
    }
    target_midpoint = 400_000
    reduction = (report.total_chars - target_midpoint) / max(report.total_chars, 1) * 100
    lines = [
        f"# 《AI 写代码之后》v{version} Editorial Audit",
        "",
        "**Status:** FROZEN — recovered v2.2.0 baseline; no chapter prose compressed yet.",
        "",
        f"- Manifest SHA256: `{_file_sha256(book / 'manifest.json')}`",
        f"- Chapters audited: {len(report.chapters)}",
        f"- Recovered visible characters: {report.total_chars}",
        "- v2.3 target: 380000–420000 visible characters",
        f"- Reduction required to 400000-character midpoint: {reduction:.2f}%",
        f"- Exact duplicate paragraphs over 80 characters: {len(report.exact_duplicates)}",
        f"- Risk-command candidates: {len(report.risk_candidates)}",
        f"- Volatile-fact candidates: {len(report.volatile_candidates)}",
        f"- Invalid chapter references: {len(report.invalid_references)}",
        "",
        "## Volume baseline",
        "",
        "| Volume | Visible characters | v2.3 page target |",
        "|---:|---:|---:|",
    ]
    for volume, chars in report.volume_chars.items():
        lines.append(f"| {volume} | {chars} | {page_targets.get(volume, '—')} |")

    lines.extend(
        [
            "",
            "## Six-chapter pilot baseline",
            "",
            "| Chapter | Current chars | 40% reduction | 45% reduction | Source |",
            "|---:|---:|---:|---:|---|",
        ]
    )
    for chapter in report.chapters:
        if chapter.id in {1, 19, 40, 54, 70, 91}:
            lines.append(
                f"| {chapter.id:03d} | {chapter.visible_chars} | "
                f"{round(chapter.visible_chars * 0.60)} | {round(chapter.visible_chars * 0.55)} | "
                f"`{chapter.source}` |"
            )

    lines.extend(
        [
            "",
            "## Chapter baseline",
            "",
            "| ID | Volume | Level | Visible chars | Paragraphs | Code blocks | Images | Links | Title |",
            "|---:|---:|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    manifest = json.loads((book / "manifest.json").read_text(encoding="utf-8"))
    levels = {item["id"]: item["level"] for item in manifest["chapters"]}
    for chapter in report.chapters:
        lines.append(
            f"| {chapter.id:03d} | {chapter.volume} | {levels.get(chapter.id, '')} | "
            f"{chapter.visible_chars} | {chapter.paragraphs} | {chapter.code_blocks} | "
            f"{chapter.images} | {chapter.links} | {_cell(chapter.title)} |"
        )

    lines.extend(["", "## Exact duplicate paragraphs (>80 chars)", ""])
    if report.exact_duplicates:
        for index, duplicate in enumerate(report.exact_duplicates, start=1):
            excerpt = duplicate.text[:160] + ("…" if len(duplicate.text) > 160 else "")
            lines.extend(
                [
                    f"### Duplicate {index}",
                    "",
                    f"- Chapters: {', '.join(f'{item:03d}' for item in duplicate.chapter_ids)}",
                    f"- Locations: {', '.join(f'`{item}`' for item in duplicate.locations)}",
                    f"- Text: {_cell(excerpt)}",
                    "",
                ]
            )
    else:
        lines.append("- None")

    def add_findings(title: str, findings: tuple) -> None:
        lines.extend(["", f"## {title}", ""])
        if not findings:
            lines.append("- None")
            return
        lines.extend(["| Chapter | Location | Reason | Candidate |", "|---:|---|---|---|"])
        for finding in findings:
            excerpt = finding.text[:180] + ("…" if len(finding.text) > 180 else "")
            lines.append(
                f"| {finding.chapter_id:03d} | `{finding.source}:{finding.line}` | "
                f"{_cell(finding.reason)} | {_cell(excerpt)} |"
            )

    add_findings("Risk-command candidates", report.risk_candidates)
    add_findings("Volatile-fact candidates", report.volatile_candidates)
    add_findings("Invalid chapter references", report.invalid_references)
    lines.extend(
        [
            "",
            "## Repository and release baseline",
            "",
            "- Canonical Markdown and build scripts were absent from the v2.2.0 branch before this recovery.",
            "- Existing top-level v2.2.0 EPUB, TXT, DOCX, AZW3, FB2, HTMLZ, KEPUB and MOBI remain immutable inputs/artifacts.",
            "- README and START-HERE positioning changes are deferred until the recovered baseline and pilot chapters are accepted.",
            "- PDF page count/bookmarks and Release attachment correspondence remain deferred release checks.",
            "",
        ]
    )
    destination.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def _write_pilot_report(report: PilotReport, *, destination: Path) -> None:
    status = "PASS" if not report.errors else "FAIL"
    lines = [
        "# 《AI 写代码之后》v2.3 Six-Chapter Pilot",
        "",
        f"**Status:** {status}",
        "",
        "| Chapter | Baseline | Current | Reduction | Target |",
        "|---:|---:|---:|---:|---:|",
    ]
    for result in report.chapters:
        spec = result.spec
        lines.append(
            f"| {spec.id:03d} | {spec.baseline_chars} | {result.visible_chars} | "
            f"{result.reduction_percent:.2f}% | {spec.minimum_chars}–{spec.maximum_chars} |"
        )
    baseline_total = sum(item.spec.baseline_chars for item in report.chapters)
    current_total = sum(item.visible_chars for item in report.chapters)
    reduction = (baseline_total - current_total) / max(baseline_total, 1) * 100
    lines.extend(
        [
            f"| **Total** | **{baseline_total}** | **{current_total}** | "
            f"**{reduction:.2f}%** | **28442–31028** |",
            "",
            "## Errors",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in report.errors)
    if not report.errors:
        lines.append("- None")
    lines.append("")
    destination.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "source":
            manifest = write_source(args.epub, args.output)
            print(
                json.dumps(
                    {
                        "chapters": len(manifest["chapters"]),
                        "output": str(args.output),
                        "source_sha256": manifest["source_sha256"],
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 0
        if args.command == "verify":
            report = verify_source(
                args.book,
                args.epub,
                args.txt,
                enforce_recovery_fidelity=args.recovery_fidelity,
            )
            _write_verification_report(
                report,
                version=args.version,
                epub=args.epub,
                txt=args.txt,
                destination=args.report,
            )
            print(
                json.dumps(
                    {
                        "errors": len(report.errors),
                        "report": str(args.report),
                        "warnings": len(report.warnings),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 1 if report.errors else 0
        if args.command == "audit":
            report = audit_source(args.book)
            _write_audit_report(
                report,
                version=args.version,
                book=args.book,
                destination=args.report,
            )
            print(
                json.dumps(
                    {
                        "chapters": len(report.chapters),
                        "duplicates": len(report.exact_duplicates),
                        "report": str(args.report),
                        "risk_candidates": len(report.risk_candidates),
                        "volatile_candidates": len(report.volatile_candidates),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 0
        if args.command == "pilot":
            report = validate_pilot(args.book)
            _write_pilot_report(report, destination=args.report)
            print(
                json.dumps(
                    {
                        "chapters": len(report.chapters),
                        "errors": len(report.errors),
                        "report": str(args.report),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 1 if report.errors else 0
    except SourceWriteError as exc:
        print(f"source error: {exc}", file=sys.stderr)
        return 1
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
