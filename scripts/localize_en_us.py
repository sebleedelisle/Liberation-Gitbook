#!/usr/bin/env python3
"""Generate the US English manual from the British English source."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import check_link_texts


SOURCE_ROOT = Path("en-GB")
TARGET_ROOT = Path("en-US")

MARKDOWN_LINK_PATTERN = re.compile(r"(!?)\[([^\]]*)\]\(([^)]*)\)")
INLINE_CODE_PATTERN = re.compile(r"(`+[^`\n]*`+)")
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")
URL_PATTERN = re.compile(r"\b(?:https?|mailto|tel):[^\s<>)\"]+")
HTML_PATH_ATTR_PATTERN = re.compile(r"\b(?:src|href)=(\"[^\"]*\"|'[^']*')", re.IGNORECASE)

SPECIAL_REPLACEMENTS = {
    (
        "Apologies to my US friends for the additional vowel in the word colour. "
        "Liberation is made in England so British English is the default. In the future "
        "I hope to provide translations to French, Spanish, German, Italian, Simplified "
        "Chinese, and yes, even US English. :innocent:"
    ): (
        "This US English version uses American spelling, but Liberation is made in England, "
        "so some screenshots, UI labels, file names, and older references may still use "
        "British English."
    ),
    "Windows will probably pop up a bunch of requesters.": (
        "Windows will probably show a few permission prompts."
    ),
}

TERM_REPLACEMENTS = {
    "art-net set up": "Art-Net setup",
    "the the": "the",
    "you're laser": "your laser",
    "apc 40": "APC40",
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
    "an horizontal": "a horizontal",
    "anti-clockwise": "counterclockwise",
    "anti clockwise": "counterclockwise",
    "co-ordinates": "coordinates",
    "co-ordinate": "coordinate",
    "re-ordering": "reordering",
    "re-ordered": "reordered",
    "re-order": "reorder",
    "synchronisation": "synchronization",
    "synchronising": "synchronizing",
    "synchronised": "synchronized",
    "synchronise": "synchronize",
    "visualisations": "visualizations",
    "visualisation": "visualization",
    "visualisers": "visualizers",
    "visualiser": "visualizer",
    "visualising": "visualizing",
    "visualised": "visualized",
    "visualise": "visualize",
    "de-authorising": "de-authorizing",
    "de-authorised": "de-authorized",
    "de-authorisation": "de-authorization",
    "de-authorise": "de-authorize",
    "deauthorisations": "deauthorizations",
    "deauthorisation": "deauthorization",
    "deauthorising": "deauthorizing",
    "deauthorised": "deauthorized",
    "deauthorise": "deauthorize",
    "authorisations": "authorizations",
    "authorisation": "authorization",
    "authorising": "authorizing",
    "authorised": "authorized",
    "authorise": "authorize",
    "licences": "licenses",
    "licence": "license",
    "coloured": "colored",
    "colourful": "colorful",
    "colours": "colors",
    "colour": "color",
    "centred": "centered",
    "centres": "centers",
    "centre": "center",
    "organiser": "organizer",
    "organising": "organizing",
    "organised": "organized",
    "organise": "organize",
    "reorganising": "reorganizing",
    "reorganised": "reorganized",
    "reorganise": "reorganize",
    "customising": "customizing",
    "customisable": "customizable",
    "customisation": "customization",
    "customised": "customized",
    "customise": "customize",
    "optimisation": "optimization",
    "optimising": "optimizing",
    "optimised": "optimized",
    "optimise": "optimize",
    "stylisation": "stylization",
    "stylised": "stylized",
    "stylise": "stylize",
    "stabilising": "stabilizing",
    "stabilised": "stabilized",
    "stabilise": "stabilize",
    "right clicking": "right-clicking",
    "right click": "right-click",
    "left clicking": "left-clicking",
    "left click": "left-click",
    "double clicking": "double-clicking",
    "double click": "double-click",
    "on screen": "on-screen",
    "cursor keys": "arrow keys",
    "click / drag": "click and drag",
    "drop down": "drop-down",
    "pop up": "pop-up",
    "check boxes": "checkboxes",
    "check box": "checkbox",
    "64 bit": "64-bit",
    "32 bit": "32-bit",
    "high spec": "high-spec",
    "pre-set": "preset",
    "cover over": "cover",
    "multi laser": "multi-laser",
    "along side": "alongside",
    "built in to": "built into",
    "downloads folder": "Downloads folder",
    "clipdeck": "clip deck",
    "playing any more": "playing anymore",
    "use any more": "use anymore",
    "work out if": "figure out if",
    "midi": "MIDI",
    "reset behaviours": "reset behavior",
    "behaviours": "behaviors",
    "behaviour": "behavior",
    "travelling": "traveling",
    "labelled": "labeled",
    "labelling": "labeling",
    "modelling": "modeling",
    "catalogue": "catalog",
    "dialogue": "dialog",
    "analogue": "analog",
    "artefact": "artifact",
    "programmes": "programs",
    "programme": "program",
    "favourite": "favorite",
    "neighbouring": "neighboring",
    "neighbours": "neighbors",
    "neighbour": "neighbor",
    "defence": "defense",
    "offence": "offense",
    "whilst": "while",
    "learnt": "learned",
    "requesters": "prompts",
    "requester": "prompt",
    "fiddly": "tricky",
    "greyscale": "grayscale",
    "greys": "grays",
    "grey": "gray",
    "synch": "sync",
    "fastforward": "fast-forward",
    "half decent": "half-decent",
    "ie": "i.e.",
}

TERM_PATTERN = re.compile(
    r"(?<![A-Za-z])("
    + "|".join(re.escape(term) for term in sorted(TERM_REPLACEMENTS, key=len, reverse=True))
    + r")(?![A-Za-z])",
    re.IGNORECASE,
)


def match_case(source: str, replacement: str) -> str:
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def apply_terms(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        source = match.group(1)
        replacement = TERM_REPLACEMENTS[source.lower()]
        return match_case(source, replacement)

    return TERM_PATTERN.sub(replace, text)


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
    transformed = apply_terms(protected)
    return restore_paths(transformed, placeholders)


def transform_non_code_segment(segment: str) -> str:
    result: list[str] = []
    position = 0

    for match in MARKDOWN_LINK_PATTERN.finditer(segment):
        result.append(transform_plain_segment(segment[position : match.start()]))
        marker, label, target = match.groups()
        result.append(f"{marker}[{transform_plain_segment(label)}]({target})")
        position = match.end()

    result.append(transform_plain_segment(segment[position:]))
    return "".join(result)


def transform_markdown_line(line: str) -> str:
    parts = INLINE_CODE_PATTERN.split(line)
    return "".join(
        part if index % 2 else transform_non_code_segment(part)
        for index, part in enumerate(parts)
    )


def transform_markdown(text: str) -> str:
    for source, replacement in SPECIAL_REPLACEMENTS.items():
        text = text.replace(source, replacement)

    output: list[str] = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        if FENCE_PATTERN.match(line):
            output.append(line)
            in_fence = not in_fence
            continue
        output.append(line if in_fence else transform_markdown_line(line))
    return "".join(output)


def transform_target_files() -> None:
    for path in TARGET_ROOT.rglob("*.md"):
        path.write_text(transform_markdown(path.read_text(encoding="utf-8")), encoding="utf-8")

    book_json = TARGET_ROOT / "book.json"
    data = json.loads(book_json.read_text(encoding="utf-8"))
    data["language"] = "en-US"
    book_json.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fix_link_labels() -> None:
    root = Path.cwd()
    issues = [
        issue
        for issue in check_link_texts.find_issues(root)
        if issue.locale == TARGET_ROOT.name
    ]
    if not issues:
        return

    fixed = check_link_texts.fix_issues(root, issues)
    remaining = [
        issue
        for issue in check_link_texts.find_issues(root)
        if issue.locale == TARGET_ROOT.name
    ]
    if remaining:
        raise SystemExit(f"Could not fix {len(remaining)} {TARGET_ROOT} link labels.")
    print(f"Fixed {fixed} {TARGET_ROOT} link labels.")


def main() -> None:
    if not SOURCE_ROOT.exists():
        raise SystemExit(f"Missing source folder: {SOURCE_ROOT}")

    if TARGET_ROOT.exists():
        shutil.rmtree(TARGET_ROOT)
    shutil.copytree(SOURCE_ROOT, TARGET_ROOT)
    transform_target_files()
    fix_link_labels()
    print(f"Generated {TARGET_ROOT} from {SOURCE_ROOT}")


if __name__ == "__main__":
    main()
