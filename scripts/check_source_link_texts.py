#!/usr/bin/env python3
"""Check en-GB internal Markdown links use destination titles."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import check_link_texts


def replacement_for_source_label(label: str, title: str) -> tuple[str, str] | None:
    label_norm = check_link_texts.normalized(label)
    title_norm = check_link_texts.normalized(title)
    if not label_norm or label_norm == title_norm:
        return None

    title_segments = check_link_texts.split_title_segments(title)
    if any(label_norm == check_link_texts.normalized(segment) for segment in title_segments):
        return None

    return title, "Destination title"


def find_issues(root: Path) -> list[check_link_texts.LinkIssue]:
    issues: list[check_link_texts.LinkIssue] = []
    locale = check_link_texts.SOURCE_LOCALE
    source_root = root / locale

    for markdown_path in sorted(check_link_texts.iter_markdown_files(source_root)):
        rel_file = markdown_path.relative_to(source_root)
        content = markdown_path.read_text(encoding="utf-8")
        for match in check_link_texts.MARKDOWN_LINK_PATTERN.finditer(content):
            resolved = check_link_texts.resolve_target(root, locale, rel_file, match.group(2))
            if not resolved:
                continue
            rel_target, anchor = resolved
            title = check_link_texts.destination_title(source_root / rel_target, anchor)
            if not title:
                continue
            replacement = replacement_for_source_label(match.group(1), title)
            if not replacement:
                continue
            replacement_text, reason = replacement
            issues.append(
                check_link_texts.LinkIssue(
                    locale=locale,
                    path=rel_file,
                    line=content.count("\n", 0, match.start()) + 1,
                    target=rel_target,
                    link_text=check_link_texts.strip_markdown(match.group(1)),
                    replacement=replacement_text,
                    reason=reason,
                )
            )

    return issues


def fix_file(root: Path, rel_file: Path) -> int:
    locale = check_link_texts.SOURCE_LOCALE
    source_root = root / locale
    markdown_path = source_root / rel_file
    content = markdown_path.read_text(encoding="utf-8")
    replacements: list[tuple[int, int, str]] = []

    for match in check_link_texts.MARKDOWN_LINK_PATTERN.finditer(content):
        resolved = check_link_texts.resolve_target(root, locale, rel_file, match.group(2))
        if not resolved:
            continue
        rel_target, anchor = resolved
        title = check_link_texts.destination_title(source_root / rel_target, anchor)
        if not title:
            continue
        replacement = replacement_for_source_label(match.group(1), title)
        if not replacement:
            continue
        replacement_text, _ = replacement
        replacements.append(
            (
                match.start(1),
                match.end(1),
                check_link_texts.preserve_label_style(match.group(1), replacement_text),
            )
        )

    if not replacements:
        return 0

    updated = content
    for start, end, replacement in reversed(replacements):
        updated = updated[:start] + replacement + updated[end:]
    markdown_path.write_text(updated, encoding="utf-8")
    return len(replacements)


def fix_issues(root: Path, issues: list[check_link_texts.LinkIssue]) -> int:
    files = sorted({issue.path for issue in issues})
    return sum(fix_file(root, rel_file) for rel_file in files)


def print_report(issues: list[check_link_texts.LinkIssue], limit: int) -> None:
    print(f"Source link text issues: {len(issues)}")
    if not issues:
        return

    print("Examples:")
    for issue in issues[:limit]:
        print(
            f"- {issue.locale}/{issue.path}:{issue.line}: "
            f"{issue.link_text!r} -> {issue.replacement!r} "
            f"({issue.reason}; target {issue.target})"
        )
    if len(issues) > limit:
        print(f"... {len(issues) - limit} more")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Rewrite stale link labels in en-GB docs.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum issues to print.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    issues = find_issues(root)

    if args.fix and issues:
        fixed = fix_issues(root, issues)
        print(f"Fixed {fixed} source link labels.")
        issues = find_issues(root)

    print_report(issues, args.limit)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
