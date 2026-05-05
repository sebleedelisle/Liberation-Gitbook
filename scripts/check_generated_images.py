#!/usr/bin/env python3
"""Validate generated HonKit image assets before deployment."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK_ROOT = REPO_ROOT / "_book"
LANGS_PATH = REPO_ROOT / "LANGS.md"
PAGES_WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "honkit-pages.yml"
EXTERNAL_SCHEMES = {"data", "http", "https", "javascript", "mailto", "tel"}


class ImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.srcs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "img":
            return
        attrs_by_name = {name.lower(): value for name, value in attrs}
        src = attrs_by_name.get("src")
        if src:
            self.srcs.append(src)


def language_roots() -> list[str]:
    roots: list[str] = []
    for line in LANGS_PATH.read_text(encoding="utf-8").splitlines():
        match = re.search(r"\[[^\]]+\]\(([^)]+)\)", line)
        if not match:
            continue
        root = match.group(1).split("#", 1)[0].strip().rstrip("/")
        if root and "://" not in root:
            roots.append(root)
    return roots


def iter_html_files() -> list[Path]:
    return sorted(BOOK_ROOT.rglob("*.html"))


def resolve_local_src(src: str, html_file: Path) -> Path | None:
    parsed = urlsplit(src)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or src.startswith("//"):
        return None

    src_path = unquote(parsed.path)
    if not src_path:
        return None

    if src_path.startswith("/"):
        return (BOOK_ROOT / src_path.lstrip("/")).resolve()
    return (html_file.parent / src_path).resolve()


def is_hidden_output_path(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(BOOK_ROOT.resolve())
    except ValueError:
        return False
    return any(part.startswith(".") and part not in {".", ".."} for part in relative.parts)


def pages_upload_includes_hidden_files() -> bool:
    if not PAGES_WORKFLOW_PATH.exists():
        return False

    workflow = PAGES_WORKFLOW_PATH.read_text(encoding="utf-8")
    if "actions/upload-pages-artifact" not in workflow:
        return False
    return re.search(r"(?m)^\s*include-hidden-files:\s*true\s*$", workflow) is not None


def check_local_image_sources() -> tuple[int, list[str], bool]:
    checked = 0
    missing: list[str] = []
    has_hidden_refs = False

    for html_file in iter_html_files():
        parser = ImageParser()
        parser.feed(html_file.read_text(encoding="utf-8", errors="ignore"))

        for src in parser.srcs:
            resolved = resolve_local_src(src, html_file)
            if resolved is None:
                continue

            checked += 1
            has_hidden_refs = has_hidden_refs or is_hidden_output_path(resolved)
            if not resolved.exists():
                missing.append(
                    f"{html_file.relative_to(BOOK_ROOT)}: {src} -> "
                    f"{resolved.relative_to(BOOK_ROOT)}"
                )

    return checked, missing, has_hidden_refs


def check_language_asset_sets() -> list[str]:
    roots = language_roots()
    if not roots:
        return ["No language roots found in LANGS.md"]

    default_root = roots[0]
    default_assets = BOOK_ROOT / default_root / ".gitbook" / "assets"
    if not default_assets.exists():
        return [f"Missing default asset folder: {default_assets.relative_to(REPO_ROOT)}"]

    expected = {
        path.relative_to(default_assets)
        for path in default_assets.rglob("*")
        if path.is_file()
    }
    if not expected:
        return [f"No files found in default asset folder: {default_assets.relative_to(REPO_ROOT)}"]

    issues: list[str] = []
    for root in roots:
        assets = BOOK_ROOT / root / ".gitbook" / "assets"
        if not assets.exists():
            issues.append(f"Missing asset folder: {assets.relative_to(REPO_ROOT)}")
            continue

        present = {
            path.relative_to(assets)
            for path in assets.rglob("*")
            if path.is_file()
        }
        missing = sorted(expected - present)
        if missing:
            preview = ", ".join(str(path) for path in missing[:8])
            suffix = "" if len(missing) <= 8 else f", ... plus {len(missing) - 8} more"
            issues.append(
                f"{assets.relative_to(REPO_ROOT)} is missing {len(missing)} default "
                f"asset(s): {preview}{suffix}"
            )

    return issues


def main() -> int:
    if not BOOK_ROOT.exists():
        print("Missing _book. Run `npm run build:site` first.")
        return 1

    checked, missing_images, has_hidden_refs = check_local_image_sources()
    asset_issues = check_language_asset_sets()
    workflow_issue = (
        has_hidden_refs and not pages_upload_includes_hidden_files()
    )

    print(f"Checked {len(iter_html_files())} generated HTML files")
    print(f"Checked {checked} local image references")

    if not missing_images and not asset_issues and not workflow_issue:
        print("Generated image assets are deployable")
        return 0

    if missing_images:
        print("Missing generated image files:")
        for issue in missing_images[:50]:
            print(f"- {issue}")
        if len(missing_images) > 50:
            print(f"- ... plus {len(missing_images) - 50} more")

    if asset_issues:
        print("Generated asset folder issues:")
        for issue in asset_issues:
            print(f"- {issue}")

    if workflow_issue:
        print(
            "Generated HTML references hidden asset folders such as `.gitbook`, "
            "but the Pages upload workflow does not set `include-hidden-files: true`."
        )

    return 1


if __name__ == "__main__":
    sys.exit(main())
