#!/usr/bin/env python3
"""Command-line entry point for v2.3 book source operations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.booklib.source_writer import SourceWriteError, write_source


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="book.py")
    commands = parser.add_subparsers(dest="command", required=True)
    source = commands.add_parser("source", help="recover Markdown from an EPUB")
    source.add_argument("--epub", required=True, type=Path)
    source.add_argument("--output", default=Path("book"), type=Path)
    return parser


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
    except SourceWriteError as exc:
        print(f"source error: {exc}", file=sys.stderr)
        return 1
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
