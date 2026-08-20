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
            report = verify_source(args.book, args.epub, args.txt)
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
    except SourceWriteError as exc:
        print(f"source error: {exc}", file=sys.stderr)
        return 1
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
