#!/usr/bin/env python3
"""Check Markdown links are separated from following prose."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]\n]+\]\([^\)\n]+\)")
SKIP_DIRS = {".git", ".screenshot-work", "_book", "node_modules"}


@dataclass(frozen=True)
class LinkSpacingIssue:
    path: Path
    line: int
    next_char: str


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def is_joined_to_word(char: str) -> bool:
    return char in {"_", "("} or (char.isascii() and char.isalnum())


def find_issues(root: Path) -> list[LinkSpacingIssue]:
    issues: list[LinkSpacingIssue] = []
    for path in sorted(iter_markdown_files(root)):
        content = path.read_text(encoding="utf-8", errors="ignore")
        for match in MARKDOWN_LINK_PATTERN.finditer(content):
            if match.end() >= len(content):
                continue
            next_char = content[match.end()]
            if not is_joined_to_word(next_char):
                continue
            issues.append(
                LinkSpacingIssue(
                    path=path.relative_to(root),
                    line=content.count("\n", 0, match.start()) + 1,
                    next_char=next_char,
                )
            )
    return issues


def fix_file(path: Path) -> int:
    content = path.read_text(encoding="utf-8")
    insert_positions: list[int] = []
    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        if match.end() < len(content) and is_joined_to_word(content[match.end()]):
            insert_positions.append(match.end())

    if not insert_positions:
        return 0

    updated = content
    for position in reversed(insert_positions):
        updated = updated[:position] + " " + updated[position:]
    path.write_text(updated, encoding="utf-8")
    return len(insert_positions)


def fix_issues(root: Path, issues: list[LinkSpacingIssue]) -> int:
    files = sorted({issue.path for issue in issues})
    return sum(fix_file(root / path) for path in files)


def print_report(issues: list[LinkSpacingIssue], limit: int) -> None:
    print(f"Markdown link spacing issues: {len(issues)}")
    if not issues:
        return

    print("Examples:")
    for issue in issues[:limit]:
        print(f"- {issue.path}:{issue.line}: link is immediately followed by {issue.next_char!r}")
    if len(issues) > limit:
        print(f"... {len(issues) - limit} more")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Insert spaces after joined Markdown links.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum issues to print.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    issues = find_issues(root)

    if args.fix and issues:
        fixed = fix_issues(root, issues)
        print(f"Fixed {fixed} Markdown link spacing issues.")
        issues = find_issues(root)

    print_report(issues, args.limit)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
