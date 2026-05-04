#!/usr/bin/env python3
import argparse
import difflib
import hashlib
import json
import subprocess
from pathlib import Path


SOURCE_ROOT = Path("en-GB")
TRANSLATION_STATUS_PATH = Path(".translation-status.json")
DEFAULT_TARGETS = [Path("zh-CN")]


def git(*args, check=True):
    result = subprocess.run(
        ["git", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def git_bytes(*args, check=True):
    result = subprocess.run(
        ["git", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def last_commit(path):
    commit = git("log", "-1", "--format=%H", "--", str(path), check=False)
    return commit or None


def path_exists_at(commit, path):
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}:{path}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def content_at(commit, path):
    return git_bytes("show", f"{commit}:{path}")


def source_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_translation_status():
    if not TRANSLATION_STATUS_PATH.exists():
        return {"entries": {}}
    return json.loads(TRANSLATION_STATUS_PATH.read_text(encoding="utf-8"))


def marked_current(status, target, source):
    entry = status.get("entries", {}).get(str(target))
    return bool(
        entry
        and entry.get("source") == str(source)
        and entry.get("source_sha256") == source_sha256(source)
    )


def markdown_files(root):
    return sorted(path for path in root.rglob("*.md") if path.is_file())


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


def classify(target_root):
    current = []
    missing = []
    stale = []
    untracked = []
    translation_status = load_translation_status()

    for source in markdown_files(SOURCE_ROOT):
        rel = source.relative_to(SOURCE_ROOT)
        target = target_root / rel

        if not target.exists():
            missing.append(rel)
            continue

        commit = last_commit(target)
        if not commit:
            untracked.append(rel)
            continue

        if marked_current(translation_status, target, source):
            current.append(rel)
            continue

        if not path_exists_at(commit, source):
            stale.append((rel, commit, "source added after translation commit"))
            continue

        if content_at(commit, source) == source.read_bytes():
            current.append(rel)
        else:
            stale.append((rel, commit, "source changed since translation commit"))

    source_rels = {path.relative_to(SOURCE_ROOT) for path in markdown_files(SOURCE_ROOT)}
    orphaned = [
        path.relative_to(target_root)
        for path in markdown_files(target_root)
        if path.relative_to(target_root) not in source_rels
    ]

    return {
        "current": current,
        "missing": missing,
        "stale": stale,
        "untracked": untracked,
        "orphaned": orphaned,
    }


def print_status(target_root, status):
    print(f"Translation status: {target_root} vs {SOURCE_ROOT}")
    print()
    print(f"Current:   {len(status['current'])}")
    print(f"Stale:     {len(status['stale'])}")
    print(f"Missing:   {len(status['missing'])}")
    print(f"Untracked: {len(status['untracked'])}")
    print(f"Orphaned:  {len(status['orphaned'])}")

    if status["stale"]:
        print("\nStale:")
        for rel, commit, reason in status["stale"]:
            print(f"- {rel} ({reason}; {target_root} last touched {commit[:7]})")

    if status["missing"]:
        print("\nMissing:")
        for rel in status["missing"]:
            print(f"- {rel}")

    if status["untracked"]:
        print("\nUntracked translations:")
        for rel in status["untracked"]:
            print(f"- {rel}")

    if status["orphaned"]:
        print("\nOrphaned translations:")
        for rel in status["orphaned"]:
            print(f"- {rel}")


def print_diff(target_root, rel):
    source = SOURCE_ROOT / rel
    target = target_root / rel

    if not source.exists():
        raise SystemExit(f"English source does not exist: {source}")
    if not target.exists():
        raise SystemExit(f"Translation does not exist: {target}")

    commit = last_commit(target)
    if not commit:
        raise SystemExit(f"Translation has no git history yet: {target}")
    if not path_exists_at(commit, source):
        old_lines = []
    else:
        old_lines = content_at(commit, source).decode("utf-8", "replace").splitlines()

    new_lines = source.read_text(encoding="utf-8").splitlines()
    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=f"{commit[:7]}:{source}",
        tofile=str(source),
        lineterm="",
    )
    print("\n".join(diff))


def main():
    parser = argparse.ArgumentParser(description="Report translation freshness from git history.")
    parser.add_argument(
        "--target",
        action="append",
        help="Target language root to check. May be passed more than once. Defaults to LANGS.md targets.",
    )
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if translations are stale or missing.")
    parser.add_argument("--diff", metavar="PATH", help="Show English source diff since the matching translated page was last touched.")
    args = parser.parse_args()
    targets = target_roots(args)

    if args.diff:
        if len(targets) != 1:
            raise SystemExit("--diff requires exactly one --target when multiple targets are configured.")
        print_diff(targets[0], Path(args.diff))
        return

    statuses = []
    for index, target_root in enumerate(targets):
        if index:
            print()
        status = classify(target_root)
        statuses.append(status)
        print_status(target_root, status)

    if args.strict and any(
        status["stale"] or status["missing"] or status["untracked"] or status["orphaned"]
        for status in statuses
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
