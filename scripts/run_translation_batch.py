#!/usr/bin/env python3
"""Run weekly or monthly translation batches from translation-tiers.json."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIERS_PATH = ROOT / "translation-tiers.json"
CADENCE_PATH = ROOT / ".translation-cadence.json"
TRANSLATE_SCRIPT = ROOT / "scripts" / "translate_docs.py"
LOCALIZE_EN_US_SCRIPT = ROOT / "scripts" / "localize_en_us.py"
CADENCE_DAYS = {
    "weekly": 7,
    "monthly": 28,
}


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dedupe(items: list[str]) -> list[str]:
    result: list[str] = []
    seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def parse_iso_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def should_skip_for_cadence(tier: str, force: bool) -> bool:
    if force:
        return False

    cadence = load_json(CADENCE_PATH, {"last_runs": {}})
    last_run = cadence.get("last_runs", {}).get(tier)
    if not last_run:
        return False

    last_date = parse_iso_date(last_run)
    if not last_date:
        return False

    next_date = last_date + timedelta(days=CADENCE_DAYS[tier])
    today = date.today()
    if today < next_date:
        print(
            f"{tier} translations last ran on {last_date.isoformat()}; "
            f"next scheduled run is {next_date.isoformat()}. "
            "Use --force-cadence for an urgent rerun."
        )
        return True

    return False


def record_cadence(tier: str) -> None:
    cadence = load_json(CADENCE_PATH, {"last_runs": {}})
    cadence.setdefault("last_runs", {})[tier] = date.today().isoformat()
    if tier == "monthly":
        cadence["last_runs"]["weekly"] = date.today().isoformat()
    write_json(CADENCE_PATH, cadence)


def require_provider_key(args: argparse.Namespace) -> None:
    provider = args.provider or os.environ.get("TRANSLATE_PROVIDER", "openai")
    key_name = "OPENAI_API_KEY" if provider == "openai" else "ANTHROPIC_API_KEY"
    if provider not in {"openai", "anthropic"}:
        raise SystemExit(f"Unknown translation provider: {provider}")
    if not os.environ.get(key_name):
        raise SystemExit(f"{key_name} is not set.")


def run(command: list[str], skip: bool = False) -> None:
    print(" ".join(command), flush=True)
    if skip:
        return
    subprocess.run(command, cwd=ROOT, check=True)


def translate_command(locale: str, args: argparse.Namespace) -> list[str]:
    command = [
        sys.executable,
        str(TRANSLATE_SCRIPT.relative_to(ROOT)),
        locale,
        "--mode",
        "stale",
    ]

    if args.dry_run:
        command.append("--dry-run")
    if args.stale_strategy:
        command.extend(["--stale-strategy", args.stale_strategy])
    if args.allow_full_fallback:
        command.append("--allow-full-fallback")
    if args.provider:
        command.extend(["--provider", args.provider])
    if args.model:
        command.extend(["--model", args.model])
    if args.reasoning_effort:
        command.extend(["--reasoning-effort", args.reasoning_effort])
    if args.since:
        command.extend(["--since", args.since])
    if args.paths_from_git:
        command.extend(["--paths-from-git", args.paths_from_git])
    if args.limit:
        command.extend(["--limit", str(args.limit)])

    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a configured translation update batch.")
    parser.add_argument("tier", choices=["weekly", "monthly"], help="Translation tier to run.")
    parser.add_argument("--dry-run", action="store_true", help="Print and dry-run translation commands.")
    parser.add_argument("--locale", action="append", help="Override tier locales. May be passed more than once.")
    parser.add_argument("--skip-en-us", action="store_true", help="Do not regenerate generated English variants.")
    parser.add_argument("--force-cadence", action="store_true", help="Bypass the weekly/monthly cadence guard.")
    parser.add_argument(
        "--stale-strategy",
        choices=["blocks", "diff", "full"],
        help="Passed through to translate_docs.py.",
    )
    parser.add_argument("--allow-full-fallback", action="store_true", help="Passed through to translate_docs.py.")
    parser.add_argument("--provider", choices=["openai", "anthropic"], help="Passed through to translate_docs.py.")
    parser.add_argument("--model", help="Passed through to translate_docs.py.")
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh"],
        help="Passed through to translate_docs.py.",
    )
    parser.add_argument("--since", help="Only update source Markdown changed between this ref and HEAD.")
    parser.add_argument("--paths-from-git", help="Only update source Markdown changed in this commit or range.")
    parser.add_argument("--limit", type=int, help="Translate at most this many files per locale.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tiers = load_json(TIERS_PATH, {})
    locales = dedupe(args.locale or tiers.get(args.tier, []))
    generated = dedupe(tiers.get("generated", []))

    if not locales:
        raise SystemExit(f"No locales configured for {args.tier}.")

    if not args.dry_run:
        if should_skip_for_cadence(args.tier, args.force_cadence):
            return
        require_provider_key(args)

    print(f"Translation batch: {args.tier}")
    print(f"Locales: {', '.join(locales)}")

    if not args.skip_en_us and "en-US" in generated:
        run([sys.executable, str(LOCALIZE_EN_US_SCRIPT.relative_to(ROOT))], skip=args.dry_run)

    for locale in locales:
        run(translate_command(locale, args))

    if not args.dry_run:
        record_cadence(args.tier)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
