#!/usr/bin/env python3
"""
Check Markdown files for internal links that point to missing targets.
Exits with a non-zero status if any broken links are found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable


IGNORED_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")
MARKDOWN_PATTERN = re.compile(r"\[([^\]]+)\]\(([^()\s]+[^()]*)\)")
SKIP_DIRS = {"_book", "node_modules"}


def iter_markdown_files(root: Path) -> Iterable[Path]:
    """Yield Markdown files, skipping build output and dependencies."""
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def link_targets(md_path: Path, content: str) -> Iterable[str]:
    for match in MARKDOWN_PATTERN.finditer(content):
        target = match.group(2)
        if target.startswith(IGNORED_PREFIXES):
            continue
        if '"' in target:
            target = target.split('"', 1)[0]
        target = target.strip()
        path_part = target.split("#", 1)[0]
        if not path_part or "://" in path_part:
            continue
        yield path_part


def find_broken_links(md_files: Iterable[Path]) -> list[tuple[Path, str]]:
    broken: list[tuple[Path, str]] = []
    for md in md_files:
        content = md.read_text(encoding="utf-8", errors="ignore")
        for path_part in link_targets(md, content):
            resolved = (md.parent / path_part).resolve()
            if resolved.exists():
                continue
            candidate_dir = md.parent / path_part
            if candidate_dir.suffix == "" and (candidate_dir / "README.md").resolve().exists():
                continue
            broken.append((md, path_part))
    return broken


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    md_files = sorted(iter_markdown_files(repo_root))
    broken = find_broken_links(md_files)

    print(f"Checked {len(md_files)} Markdown files:")
    for md in md_files:
        print(f"- {md}")

    if not broken:
        print("No broken internal links found")
        return 0

    print("Broken internal links:")
    for md, target in sorted(broken):
        print(f"- {md}: {target}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
