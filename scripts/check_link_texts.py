#!/usr/bin/env python3
"""Check translated internal Markdown links use translated destination titles."""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SOURCE_LOCALE = "en-GB"
LOCALE_PATTERN = re.compile(r"^[a-z]{2}-[A-Z]{2}$")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
SKIP_DIRS = {"_book", "node_modules"}
EXTERNAL_TARGET_PATTERN = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
EMOJI_PREFIX_PATTERN = re.compile(r"^[\s\u2600-\u27BF\U0001F300-\U0001FAFF]+")
STATUS_PREFIX_PATTERN = re.compile(r"^((?:[\u2600-\u27BF\U0001F300-\U0001FAFF]\ufe0f?\s*)+)")


@dataclass(frozen=True)
class Heading:
    text: str
    slug: str
    level: int


@dataclass(frozen=True)
class LinkIssue:
    locale: str
    path: Path
    line: int
    target: Path
    link_text: str
    replacement: str
    reason: str


def strip_markdown(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    for marker in ("**", "__", "*", "_", "`"):
        text = text.replace(marker, "")
    text = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|])", r"\1", text)
    return EMOJI_PREFIX_PATTERN.sub("", text).strip()


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFKC", strip_markdown(text)).casefold()
    text = text.replace("&", "and")
    text = re.sub(r"[\u2010-\u2015]", "-", text)
    text = re.sub(r"[^\w\s]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def slugified(text: str) -> str:
    text = unicodedata.normalize("NFKD", strip_markdown(text))
    text = text.encode("ascii", "ignore").decode("ascii").casefold()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def link_label_slug(text: str) -> str:
    text = strip_markdown(text).strip()
    text = text.removesuffix(".md")
    text = text.strip("#/")
    return slugified(text)


def is_slug_or_filename(text: str) -> bool:
    text = strip_markdown(text).strip().casefold()
    return (
        text.endswith(".md")
        or re.fullmatch(r"#?[a-z0-9][a-z0-9._/-]*", text) is not None
        or re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", text) is not None
    )


def target_part(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target:
        first, rest = target.split(" ", 1)
        if rest.lstrip().startswith(('"', "'")):
            target = first
    return target.strip("<>")


def iter_locales(root: Path) -> list[str]:
    return sorted(
        path.name
        for path in root.iterdir()
        if path.is_dir() and LOCALE_PATTERN.fullmatch(path.name) and path.name != SOURCE_LOCALE
    )


def iter_markdown_files(locale_root: Path) -> Iterable[Path]:
    for path in locale_root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def headings(path: Path) -> list[Heading]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []

    found = []
    for match in HEADING_PATTERN.finditer(text):
        title = strip_markdown(match.group(2))
        found.append(Heading(title, slugified(title), len(match.group(1))))
    return found


def destination_title(path: Path, anchor: str | None) -> str | None:
    found = headings(path)
    if not found:
        return None

    if anchor:
        anchor_slug = slugified(anchor)
        for heading in found:
            if heading.slug == anchor_slug:
                return heading.text

    for heading in found:
        if heading.level == 1:
            return heading.text
    return found[0].text


def split_title_segments(title: str) -> list[str]:
    return [
        part.strip()
        for part in re.split(r"\s+(?:/|／|:|–|\|)\s+|\s*[／/]\s*|\s*:\s*", strip_markdown(title))
        if normalized(part)
    ]


def contains_normalized_phrase(text: str, phrase: str) -> bool:
    return f" {phrase} " in f" {text} "


def resolve_target(root: Path, locale: str, rel_file: Path, raw_target: str) -> tuple[Path, str | None] | None:
    target = target_part(raw_target)
    if not target or target.startswith("#") or target.startswith("//") or EXTERNAL_TARGET_PATTERN.match(target):
        return None

    path_part, _, anchor = target.partition("#")
    locale_root = root / locale
    candidate = (
        locale_root / path_part.lstrip("/")
        if path_part.startswith("/")
        else locale_root / rel_file.parent / path_part
    )

    try:
        rel_target = candidate.resolve().relative_to(locale_root.resolve())
    except ValueError:
        return None

    if (locale_root / rel_target).is_dir() or path_part.endswith("/"):
        rel_target = rel_target / "README.md"
    elif rel_target.suffix == "":
        if (locale_root / rel_target / "README.md").exists() or (
            root / SOURCE_LOCALE / rel_target / "README.md"
        ).exists():
            rel_target = rel_target / "README.md"
        else:
            rel_target = rel_target.with_suffix(".md")

    if rel_target.suffix.lower() != ".md":
        return None
    return rel_target, anchor or None


def preserve_label_style(original: str, replacement: str) -> str:
    stripped = original.strip()
    leading = original[: len(original) - len(original.lstrip())]
    trailing = original[len(original.rstrip()) :]

    wrappers = (("**", "**"), ("__", "__"), ("*", "*"), ("_", "_"), ("`", "`"))
    for prefix, suffix in wrappers:
        if stripped.startswith(prefix) and stripped.endswith(suffix) and len(stripped) > len(prefix) + len(suffix):
            inner = stripped[len(prefix) : -len(suffix)]
            status_match = STATUS_PREFIX_PATTERN.match(inner)
            if status_match and not STATUS_PREFIX_PATTERN.match(replacement):
                replacement = f"{status_match.group(1)}{replacement}"
            return f"{leading}{prefix}{replacement}{suffix}{trailing}"
    status_match = STATUS_PREFIX_PATTERN.match(stripped)
    if status_match and not STATUS_PREFIX_PATTERN.match(replacement):
        replacement = f"{status_match.group(1)}{replacement}"
    return f"{leading}{replacement}{trailing}"


def replacement_for_label(label: str, english_title: str, translated_title: str) -> tuple[str, str] | None:
    plain_label = strip_markdown(label)
    label_norm = normalized(plain_label)
    english_norm = normalized(english_title)
    translated_norm = normalized(translated_title)

    if not label_norm or label_norm == translated_norm:
        return None

    translated_segments = split_title_segments(translated_title)
    if any(label_norm == normalized(segment) for segment in translated_segments):
        return None

    if label_norm == english_norm and english_norm != translated_norm:
        return translated_title, "English destination title"

    english_segments = split_title_segments(english_title)
    for index, english_segment in enumerate(english_segments):
        translated_segment = (
            translated_segments[index]
            if index < len(translated_segments)
            else translated_title
        )
        english_segment_norm = normalized(english_segment)
        translated_segment_norm = normalized(translated_segment)
        if label_norm == normalized(english_segment) or link_label_slug(plain_label) == slugified(english_segment):
            if strip_markdown(plain_label) != translated_segment:
                return translated_segment, "English destination title segment"
        if (
            english_segment_norm
            and english_segment_norm != translated_segment_norm
            and contains_normalized_phrase(label_norm, english_segment_norm)
            and not contains_normalized_phrase(label_norm, translated_segment_norm)
        ):
            return translated_title, "Mixed English destination title segment"

    if is_slug_or_filename(plain_label):
        return translated_title, "Filename or slug link text"

    return None


def find_issues(root: Path) -> list[LinkIssue]:
    issues: list[LinkIssue] = []
    source_root = root / SOURCE_LOCALE

    for locale in iter_locales(root):
        locale_root = root / locale
        for markdown_path in sorted(iter_markdown_files(locale_root)):
            rel_file = markdown_path.relative_to(locale_root)
            content = markdown_path.read_text(encoding="utf-8")

            for match in MARKDOWN_LINK_PATTERN.finditer(content):
                resolved = resolve_target(root, locale, rel_file, match.group(2))
                if not resolved:
                    continue
                rel_target, anchor = resolved
                english_title = destination_title(source_root / rel_target, anchor)
                translated_title = destination_title(locale_root / rel_target, anchor)
                if not english_title or not translated_title:
                    continue

                replacement = replacement_for_label(match.group(1), english_title, translated_title)
                if not replacement:
                    continue

                replacement_text, reason = replacement
                issues.append(
                    LinkIssue(
                        locale=locale,
                        path=rel_file,
                        line=content.count("\n", 0, match.start()) + 1,
                        target=rel_target,
                        link_text=strip_markdown(match.group(1)),
                        replacement=replacement_text,
                        reason=reason,
                    )
                )

    return issues


def fix_file(root: Path, locale: str, rel_file: Path) -> int:
    locale_root = root / locale
    source_root = root / SOURCE_LOCALE
    markdown_path = locale_root / rel_file
    content = markdown_path.read_text(encoding="utf-8")
    replacements: list[tuple[int, int, str]] = []

    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        resolved = resolve_target(root, locale, rel_file, match.group(2))
        if not resolved:
            continue
        rel_target, anchor = resolved
        english_title = destination_title(source_root / rel_target, anchor)
        translated_title = destination_title(locale_root / rel_target, anchor)
        if not english_title or not translated_title:
            continue
        replacement = replacement_for_label(match.group(1), english_title, translated_title)
        if not replacement:
            continue
        replacement_text, _ = replacement
        replacements.append((match.start(1), match.end(1), preserve_label_style(match.group(1), replacement_text)))

    if not replacements:
        return 0

    updated = content
    for start, end, replacement in reversed(replacements):
        updated = updated[:start] + replacement + updated[end:]
    markdown_path.write_text(updated, encoding="utf-8")
    return len(replacements)


def fix_issues(root: Path, issues: list[LinkIssue]) -> int:
    files = sorted({(issue.locale, issue.path) for issue in issues})
    return sum(fix_file(root, locale, rel_file) for locale, rel_file in files)


def print_report(issues: list[LinkIssue], limit: int) -> None:
    print(f"Translated link text issues: {len(issues)}")
    if not issues:
        return

    by_locale: dict[str, int] = {}
    for issue in issues:
        by_locale[issue.locale] = by_locale.get(issue.locale, 0) + 1
    print("By locale:")
    for locale, count in sorted(by_locale.items(), key=lambda item: (-item[1], item[0])):
        print(f"- {locale}: {count}")

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
    parser.add_argument("--fix", action="store_true", help="Rewrite stale link labels in translated docs.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum issues to print.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    issues = find_issues(root)

    if args.fix and issues:
        fixed = fix_issues(root, issues)
        print(f"Fixed {fixed} translated link labels.")
        issues = find_issues(root)

    print_report(issues, args.limit)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
