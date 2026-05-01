#!/usr/bin/env python3
"""Check and optionally fix mechanical style rules in the British English source."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SOURCE_ROOT = Path("en-GB")

FRONTMATTER_PATTERN = re.compile(r"\A---\n.*?\n---\n", re.S)
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_PATTERN = re.compile(r"(`+[^`\n]*`+)")
MARKDOWN_LINK_PATTERN = re.compile(r"(!?)\[([^\]]*)\]\(([^)]*)\)")
URL_PATTERN = re.compile(r"\b(?:https?|mailto|tel):[^\s<>)\"]+")
HTML_PATH_ATTR_PATTERN = re.compile(r"\b(?:src|href)=(\"[^\"]*\"|'[^']*')", re.IGNORECASE)

STYLE_REPLACEMENTS = {
    "the the": "the",
    "you're laser": "your laser",
    "an horizontal": "a horizontal",
    "along side": "alongside",
    "fastforward": "fast-forward",
    "half decent": "half-decent",
    "art-net set up": "Art-Net setup",
    "laser set up": "laser setup",
    "hardware set up": "hardware setup",
    "current set up": "current setup",
    "default set up": "default setup",
    "ideal set up": "ideal setup",
    "indoor set up": "indoor setup",
    "multi-laser set up": "multi-laser setup",
    "apc40 set up": "APC40 setup",
    "own set up": "own setup",
    "this set up": "this setup",
    "your set up": "your setup",
    "the set up": "the setup",
    "a set up": "a setup",
    "set up of": "setup of",
    "tempo set up in": "tempo set in",
    "set-up": "setup",
    "pre-set": "preset",
    "check boxes": "checkboxes",
    "check box": "checkbox",
    "right clicking": "right-clicking",
    "right click": "right-click",
    "double clicking": "double-clicking",
    "double click": "double-click",
    "click / drag": "click and drag",
    "click/drag": "click and drag",
    "click-drag": "click and drag",
    "on screen buttons": "on-screen buttons",
    "on screen slider": "on-screen slider",
    "drop down": "drop-down",
    "dropdown": "drop-down",
    "pop up menu": "pop-up menu",
    "pop up that": "pop-up that",
    "opens a pop up": "opens a pop-up",
    "64 bit": "64-bit",
    "32 bit": "32-bit",
    "high spec": "high-spec",
    "counter-clockwise": "anti-clockwise",
    "counterclockwise": "anti-clockwise",
    "centered": "centred",
    "centers": "centres",
    "center": "centre",
    "multi laser": "multi-laser",
    "cover over": "cover",
    "built in to": "built into",
    "downloads folder": "Downloads folder",
    "requesters": "permission prompts",
    "requester": "permission prompt",
    "apc 40": "APC40",
    "laser cube": "LaserCube",
    "artnet": "Art-Net",
    "art net": "Art-Net",
    "midi": "MIDI",
    "ie": "i.e.",
    "synch": "sync",
    "clipdeck": "clip deck",
    "windows will probably pop up a bunch of requesters.": (
        "Windows will probably show a few permission prompts."
    ),
}

STYLE_PATTERN = re.compile(
    r"(?<![A-Za-z])("
    + "|".join(re.escape(term) for term in sorted(STYLE_REPLACEMENTS, key=len, reverse=True))
    + r")(?![A-Za-z])",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    found: str
    replacement: str


def match_case(source: str, replacement: str) -> str:
    if any(char.isupper() for char in replacement[1:]):
        return replacement
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def replacement_for(match: re.Match[str]) -> str:
    source = match.group(1)
    replacement = STYLE_REPLACEMENTS[source.lower()]
    return match_case(source, replacement)


def protect_paths(text: str) -> tuple[str, list[str]]:
    placeholders: list[str] = []

    def protect_match(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"\u0000{len(placeholders) - 1}\u0000"

    text = HTML_PATH_ATTR_PATTERN.sub(protect_match, text)
    text = URL_PATTERN.sub(protect_match, text)
    return text, placeholders


def restore_paths(text: str, placeholders: list[str]) -> str:
    for index, original in enumerate(placeholders):
        text = text.replace(f"\u0000{index}\u0000", original)
    return text


def transform_plain_segment(segment: str) -> str:
    protected, placeholders = protect_paths(segment)
    transformed = STYLE_PATTERN.sub(replacement_for, protected)
    return restore_paths(transformed, placeholders)


def transform_non_code_segment(segment: str) -> str:
    result: list[str] = []
    position = 0

    for match in MARKDOWN_LINK_PATTERN.finditer(segment):
        result.append(transform_plain_segment(segment[position : match.start()]))
        marker, label, target = match.groups()
        transformed_label = label if is_slug_or_filename(label) else transform_plain_segment(label)
        result.append(f"{marker}[{transformed_label}]({target})")
        position = match.end()

    result.append(transform_plain_segment(segment[position:]))
    return "".join(result)


def is_slug_or_filename(text: str) -> bool:
    stripped = text.strip()
    stripped = stripped.replace("**", "").replace("__", "").replace("*", "").replace("_", "")
    return (
        stripped.endswith(".md")
        or re.fullmatch(r"#?[A-Za-z0-9][A-Za-z0-9._/-]*", stripped) is not None
        or re.fullmatch(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+", stripped) is not None
    )


def transform_markdown_line(line: str) -> str:
    parts = INLINE_CODE_PATTERN.split(line)
    return "".join(
        part if index % 2 else transform_non_code_segment(part)
        for index, part in enumerate(parts)
    )


def transform_markdown(text: str) -> str:
    frontmatter = ""
    match = FRONTMATTER_PATTERN.match(text)
    if match:
        frontmatter = match.group(0)
        text = text[match.end() :]

    output: list[str] = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        if FENCE_PATTERN.match(line):
            output.append(line)
            in_fence = not in_fence
            continue
        output.append(line if in_fence else transform_markdown_line(line))

    return frontmatter + "".join(output)


def markdown_files() -> list[Path]:
    return sorted(path for path in SOURCE_ROOT.rglob("*.md") if path.is_file())


def find_issues(path: Path, original: str, transformed: str) -> list[Issue]:
    issues: list[Issue] = []
    original_lines = original.splitlines()
    transformed_lines = transformed.splitlines()

    for index, (source, fixed) in enumerate(zip(original_lines, transformed_lines), start=1):
        if source == fixed:
            continue
        for match in STYLE_PATTERN.finditer(source):
            issues.append(Issue(path, index, match.group(1), replacement_for(match)))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Rewrite mechanical style issues in en-GB.")
    parser.add_argument("--limit", type=int, default=120, help="Maximum issues to print.")
    args = parser.parse_args()

    if not SOURCE_ROOT.exists():
        raise SystemExit(f"Missing source folder: {SOURCE_ROOT}")

    issues: list[Issue] = []
    changed = 0

    for path in markdown_files():
        original = path.read_text(encoding="utf-8")
        transformed = transform_markdown(original)
        if original == transformed:
            continue
        file_issues = find_issues(path, original, transformed)
        issues.extend(file_issues)
        if args.fix:
            path.write_text(transformed, encoding="utf-8")
            changed += 1

    if args.fix:
        print(f"Fixed English style issues in {changed} files.")
        issues = []
        for path in markdown_files():
            original = path.read_text(encoding="utf-8")
            transformed = transform_markdown(original)
            if original != transformed:
                issues.extend(find_issues(path, original, transformed))

    print(f"English style issues: {len(issues)}")
    for issue in issues[: args.limit]:
        print(f"- {issue.path}:{issue.line}: {issue.found!r} -> {issue.replacement!r}")
    if len(issues) > args.limit:
        print(f"... {len(issues) - args.limit} more")

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
