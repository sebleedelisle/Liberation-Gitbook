#!/usr/bin/env python3
import argparse
import difflib
import subprocess
from pathlib import Path


SOURCE_ROOT = Path("en-GB")
TARGET_ROOT = Path("zh-CN")


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


def markdown_files(root):
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def classify():
    current = []
    missing = []
    stale = []
    untracked = []

    for source in markdown_files(SOURCE_ROOT):
        rel = source.relative_to(SOURCE_ROOT)
        target = TARGET_ROOT / rel

        if not target.exists():
            missing.append(rel)
            continue

        commit = last_commit(target)
        if not commit:
            untracked.append(rel)
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
        path.relative_to(TARGET_ROOT)
        for path in markdown_files(TARGET_ROOT)
        if path.relative_to(TARGET_ROOT) not in source_rels
    ]

    return {
        "current": current,
        "missing": missing,
        "stale": stale,
        "untracked": untracked,
        "orphaned": orphaned,
    }


def print_status(status):
    print("Translation status: zh-CN vs en-GB")
    print()
    print(f"Current:   {len(status['current'])}")
    print(f"Stale:     {len(status['stale'])}")
    print(f"Missing:   {len(status['missing'])}")
    print(f"Untracked: {len(status['untracked'])}")
    print(f"Orphaned:  {len(status['orphaned'])}")

    if status["stale"]:
        print("\nStale:")
        for rel, commit, reason in status["stale"]:
            print(f"- {rel} ({reason}; zh-CN last touched {commit[:7]})")

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


def print_diff(rel):
    source = SOURCE_ROOT / rel
    target = TARGET_ROOT / rel

    if not source.exists():
        raise SystemExit(f"English source does not exist: {source}")
    if not target.exists():
        raise SystemExit(f"Chinese translation does not exist: {target}")

    commit = last_commit(target)
    if not commit:
        raise SystemExit(f"Chinese translation has no git history yet: {target}")
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
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if translations are stale or missing.")
    parser.add_argument("--diff", metavar="PATH", help="Show English source diff since the matching zh-CN page was last touched.")
    args = parser.parse_args()

    if args.diff:
        print_diff(Path(args.diff))
        return

    status = classify()
    print_status(status)

    if args.strict and (
        status["stale"] or status["missing"] or status["untracked"] or status["orphaned"]
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
