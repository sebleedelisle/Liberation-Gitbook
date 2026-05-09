#!/usr/bin/env python3
import json
import posixpath
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_book"
SOURCE_ROOT = "en-GB"


def load_json(path):
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def languages():
    result = []
    pattern = re.compile(r"\* \[([^\]]+)\]\(([^)]+)\)")

    for line in (ROOT / "LANGS.md").read_text(encoding="utf-8").splitlines():
        match = pattern.search(line)
        if not match:
            continue

        title = match.group(1).strip()
        lang = match.group(2).strip().strip("/")
        if lang and (ROOT / lang / "SUMMARY.md").exists():
            result.append((lang, title))

    if not result:
        raise SystemExit("No languages found in LANGS.md")

    return result


def copy_missing_directory(source, target):
    if not source.exists():
        return

    target.mkdir(parents=True, exist_ok=True)
    for child in source.iterdir():
        destination = target / child.name
        if child.is_dir():
            copy_missing_directory(child, destination)
        elif not destination.exists():
            shutil.copy2(child, destination)


def write_language_book_json(language_root, temp_book):
    root_config = load_json(ROOT / "book.json")
    language_config = load_json(ROOT / language_root / "book.json")

    config = dict(root_config)
    config["title"] = language_config.get("title", root_config.get("title", "Liberation User Manual"))
    config["language"] = language_root

    (temp_book / "book.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def build_language(language_root):
    with tempfile.TemporaryDirectory(prefix=f"liberation-{language_root}-") as temp_dir:
        temp_book = Path(temp_dir) / language_root
        shutil.copytree(ROOT / language_root, temp_book)

        copy_missing_directory(ROOT / SOURCE_ROOT / ".gitbook", temp_book / ".gitbook")
        write_language_book_json(language_root, temp_book)

        output_dir = OUTPUT / language_root
        if output_dir.exists():
            shutil.rmtree(output_dir)

        subprocess.run(
            ["npx", "honkit", "build", str(temp_book), str(output_dir)],
            cwd=ROOT,
            check=True,
        )


def render_redirect_page(href, title):
    escaped_href = href.replace("&", "&amp;").replace('"', "&quot;")
    escaped_title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="en">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            '<meta name="robots" content="noindex">',
            f'<meta http-equiv="refresh" content="0; url={escaped_href}">',
            f'<link rel="canonical" href="{escaped_href}">',
            f"<title>{escaped_title}</title>",
            "<script>",
            f"var target = {json.dumps(href)} + window.location.search + window.location.hash;",
            "window.location.replace(target);",
            "</script>",
            "</head>",
            "<body>",
            f'<p><a href="{escaped_href}">{escaped_title}</a></p>',
            "</body>",
            "</html>",
            "",
        ]
    )


def write_root_language_index(language_entries):
    default_root = language_entries[0][0]
    links = "\n".join(
        f'<li><a href="{lang}/">{title}</a></li>'
        for lang, title in language_entries
    )

    (OUTPUT / "index.html").write_text(
        "\n".join(
            [
                "<!doctype html>",
                '<html lang="en">',
                "<head>",
                '<meta charset="utf-8">',
                '<meta name="viewport" content="width=device-width, initial-scale=1">',
                '<meta name="robots" content="noindex">',
                "<title>Liberation User Manual</title>",
                "<script>",
                f"window.location.replace({json.dumps(default_root + '/')} + window.location.search + window.location.hash);",
                "</script>",
                "<noscript>",
                f'<meta http-equiv="refresh" content="0; url={default_root}/">',
                "</noscript>",
                "</head>",
                "<body>",
                "<p>Open the manual:</p>",
                "<ul>",
                links,
                "</ul>",
                "</body>",
                "</html>",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_legacy_english_redirects():
    english_root = OUTPUT / SOURCE_ROOT
    if not english_root.exists():
        return

    for source in english_root.rglob("*.html"):
        rel = source.relative_to(english_root)
        if rel == Path("index.html"):
            continue
        if rel.parts and rel.parts[0] == "gitbook":
            continue

        target = OUTPUT / rel
        href = posixpath.relpath(
            posixpath.join(SOURCE_ROOT, rel.as_posix()),
            start=target.parent.relative_to(OUTPUT).as_posix() if target.parent != OUTPUT else ".",
        )

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_redirect_page(href, "Liberation User Manual"), encoding="utf-8")


def main():
    language_entries = languages()

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    for index, (language_root, title) in enumerate(language_entries, start=1):
        print(f"[{index}/{len(language_entries)}] Building {title} ({language_root})")
        build_language(language_root)

    default_assets = OUTPUT / SOURCE_ROOT / ".gitbook"
    for language_root, _title in language_entries:
        if language_root != SOURCE_ROOT:
            copy_missing_directory(default_assets, OUTPUT / language_root / ".gitbook")

    write_root_language_index(language_entries)
    write_legacy_english_redirects()


if __name__ == "__main__":
    main()
