#!/usr/bin/env python3
"""Check only the locales covered by a translation batch."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIERS_PATH = ROOT / "translation-tiers.json"
CHECK_SCRIPT = ROOT / "scripts" / "check_translations.py"


def load_tiers() -> dict:
    if not TIERS_PATH.exists():
        raise SystemExit(f"Missing translation tier config: {TIERS_PATH.relative_to(ROOT)}")
    return json.loads(TIERS_PATH.read_text(encoding="utf-8"))


def dedupe(items: list[str]) -> list[str]:
    result: list[str] = []
    seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check translation freshness for one configured batch.")
    parser.add_argument("tier", choices=["weekly", "monthly"], help="Translation tier to check.")
    parser.add_argument("--locale", action="append", help="Override tier locales. May be passed more than once.")
    parser.add_argument("--skip-en-us", action="store_true", help="Do not include generated English variants.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if selected locales are stale.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tiers = load_tiers()
    locales = dedupe(args.locale or tiers.get(args.tier, []))
    generated = [] if args.skip_en_us else tiers.get("generated", [])
    targets = dedupe([*generated, *locales])

    if not targets:
        raise SystemExit(f"No locales configured for {args.tier}.")

    command = [sys.executable, str(CHECK_SCRIPT.relative_to(ROOT))]
    if args.strict:
        command.append("--strict")
    for target in targets:
        command.extend(["--target", target])

    subprocess.run(command, cwd=ROOT, check=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
