#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


SOURCE_ROOT = Path("en-GB")
DEFAULT_TARGETS = [Path("zh-CN")]
STATUS_MARKERS = ("✅", "🟩", "🟧", "◼️")
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def status_marker(label):
    for marker in STATUS_MARKERS:
        if label.startswith(marker):
            return marker
    return ""


def summary_entries(path):
    entries = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = LINK_PATTERN.search(line)
        if not match:
            continue
        label, target = match.groups()
        entries[target] = {
            "line": line_no,
            "label": label,
            "marker": status_marker(label),
        }
    return entries


def target_roots(args):
    if args.target:
        return [Path(target) for target in args.target]

    langs = Path("LANGS.md")
    if not langs.exists():
        return DEFAULT_TARGETS

    targets = []
    for line in langs.read_text(encoding="utf-8").splitlines():
        if "](" not in line or ")" not in line:
            continue
        target = line.split("](", 1)[1].split(")", 1)[0].strip()
        if not target or target == str(SOURCE_ROOT):
            continue
        root = Path(target)
        if root.exists():
            targets.append(root)

    return targets or DEFAULT_TARGETS


def check_target(source_entries, target_root):
    summary = target_root / "SUMMARY.md"
    if not summary.exists():
        return [f"{summary}: missing translated summary"]

    target_entries = summary_entries(summary)
    errors = []
    for target, source_entry in source_entries.items():
        expected = source_entry["marker"]
        if not expected:
            continue
        if target not in target_entries:
            errors.append(
                f"{summary}: missing entry for {target} "
                f"(English line {source_entry['line']} uses {expected})"
            )
            continue

        actual = target_entries[target]["marker"]
        if actual != expected:
            actual_text = actual or "no marker"
            entry = target_entries[target]
            errors.append(
                f"{summary}:{entry['line']}: {target} should start with {expected}, "
                f"found {actual_text}: [{entry['label']}]"
            )

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Check translated SUMMARY.md files preserve English status emoji prefixes."
    )
    parser.add_argument(
        "--target",
        action="append",
        help="Target language root to check. May be passed more than once. Defaults to LANGS.md targets.",
    )
    args = parser.parse_args()

    source_summary = SOURCE_ROOT / "SUMMARY.md"
    if not source_summary.exists():
        raise SystemExit(f"{source_summary}: missing source summary")

    source_entries = summary_entries(source_summary)
    errors = []
    for target_root in target_roots(args):
        errors.extend(check_target(source_entries, target_root))

    if errors:
        print("Summary status icon issues:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Summary status icon issues: 0")


if __name__ == "__main__":
    main()
