#!/usr/bin/env python3
"""Translate Markdown docs with OpenAI or Anthropic while preserving structure."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


SOURCE_ROOT = Path("en-GB")
TRANSLATION_STATUS_PATH = Path(".translation-status.json")
LANGUAGE_NAMES = {
    "de-DE": "German",
    "nl-NL": "Dutch",
    "fr-FR": "French",
    "es-ES": "Spanish",
    "da-DK": "Danish",
    "nb-NO": "Norwegian Bokmål",
    "sv-SE": "Swedish",
    "ja-JP": "Japanese",
    "is-IS": "Icelandic",
    "fi-FI": "Finnish",
    "hu-HU": "Hungarian",
    "it-IT": "Italian",
    "pl-PL": "Polish",
    "pt-BR": "Brazilian Portuguese",
    "ko-KR": "Korean",
    "zh-HK": "Traditional Chinese (Hong Kong)",
    "zh-CN": "Simplified Chinese",
    "vi-VN": "Vietnamese",
    "tr-TR": "Turkish",
    "cs-CZ": "Czech",
    "hr-HR": "Croatian",
    "ru-RU": "Russian",
    "ar": "Arabic",
    "zh-TW": "Traditional Chinese (Taiwan)",
}
LANGS_LABELS = {
    "de-DE": "Deutsch",
    "nl-NL": "Nederlands",
    "fr-FR": "Français",
    "es-ES": "Español",
    "da-DK": "Dansk",
    "nb-NO": "Norsk Bokmål",
    "sv-SE": "Svenska",
    "ja-JP": "日本語",
    "is-IS": "Íslenska",
    "fi-FI": "Suomi",
    "hu-HU": "Magyar",
    "it-IT": "Italiano",
    "pl-PL": "Polski",
    "pt-BR": "Português do Brasil",
    "ko-KR": "한국어",
    "zh-HK": "繁體中文（香港）",
    "vi-VN": "Tiếng Việt",
    "tr-TR": "Türkçe",
    "cs-CZ": "Čeština",
    "hr-HR": "Hrvatski",
    "ru-RU": "Русский",
    "ar": "العربية",
    "zh-TW": "繁體中文（台灣）",
}
BOOK_TITLES = {
    "de-DE": "Liberation Benutzerhandbuch",
    "nl-NL": "Liberation gebruikershandleiding",
    "fr-FR": "Manuel utilisateur de Liberation",
    "es-ES": "Manual de usuario de Liberation",
    "da-DK": "Liberation brugervejledning",
    "nb-NO": "Liberation brukerhåndbok",
    "sv-SE": "Liberation användarhandbok",
    "ja-JP": "Liberation ユーザーマニュアル",
    "is-IS": "Liberation notendahandbók",
    "fi-FI": "Liberation käyttöopas",
    "hu-HU": "Liberation felhasználói kézikönyv",
    "it-IT": "Manuale utente di Liberation",
    "pl-PL": "Podręcznik użytkownika Liberation",
    "pt-BR": "Manual do usuário do Liberation",
    "ko-KR": "Liberation 사용자 설명서",
    "zh-HK": "Liberation 使用手冊",
    "vi-VN": "Sổ tay người dùng Liberation",
    "tr-TR": "Liberation kullanıcı kılavuzu",
    "cs-CZ": "Uživatelská příručka Liberation",
    "hr-HR": "Korisnički priručnik za Liberation",
    "ru-RU": "Руководство пользователя Liberation",
    "ar": "دليل مستخدم Liberation",
    "zh-TW": "Liberation 使用手冊",
}
LANGUAGE_STYLE_GUIDANCE = {
    "de-DE": (
        "For German, use informal 'du' consistently when addressing the reader. "
        "Do not use formal 'Sie'. Use natural German technical-manual prose. "
        "For prose actions like arm/disarm, prefer German verbs such as aktivieren/deaktivieren "
        "unless referring to exact on-screen UI labels."
    ),
    "nl-NL": (
        "For Dutch, use informal 'je/jij' consistently when addressing the reader. "
        "Use natural Dutch technical-manual prose and avoid overly literal English sentence structure. "
        "Translate normal headings into Dutch, for example use Licenties rather than Licences unless "
        "referring to an exact UI label. Keep exact UI labels in English, but translate explanatory prose "
        "around them. Avoid awkward English/Dutch hybrids such as arm-en; for prose actions and states "
        "like arm/disarm/armed/disarmed, use natural Dutch wording such as activeren, deactiveren, "
        "inschakelen voor output, or voor output activeren depending on context. Do not leave explanatory "
        "phrases such as currently selected clip in English in running Dutch prose; use natural Dutch such "
        "as momenteel geselecteerde clip."
    ),
    "fr-FR": (
        "For French, use 'vous' consistently when addressing the reader. "
        "Use natural French technical-manual prose and avoid word-for-word English phrasing."
    ),
    "es-ES": (
        "For Spanish, use European Spanish and informal 'tu' consistently when addressing the reader. "
        "Use natural Spanish technical-manual prose and avoid overly literal English sentence structure."
    ),
    "da-DK": (
        "For Danish, use informal 'du' consistently when addressing the reader. "
        "Use natural Danish technical-manual prose and avoid overly literal English sentence structure."
    ),
    "nb-NO": (
        "For Norwegian, use Bokmål and informal 'du' consistently when addressing the reader. "
        "Use natural Norwegian technical-manual prose and avoid overly literal English sentence structure."
    ),
    "sv-SE": (
        "For Swedish, use informal 'du' consistently when addressing the reader. "
        "Use natural Swedish technical-manual prose and avoid overly literal English sentence structure."
    ),
    "ja-JP": (
        "For Japanese, use clear, concise, polite technical-manual prose. "
        "Do not over-translate established technical terms where a katakana loanword or English UI label is more natural. "
        "Avoid marketing-like phrasing."
    ),
    "is-IS": (
        "For Icelandic, use informal 'þú' consistently when addressing the reader. "
        "Use natural Icelandic technical-manual prose and avoid overly literal English sentence structure. "
        "Avoid clunky gender-parenthetical forms such as tilbúin(n); rephrase neutrally where possible."
    ),
    "fi-FI": (
        "For Finnish, use natural direct technical-manual prose. "
        "Prefer concise imperatives where appropriate and avoid overly literal English sentence structure."
    ),
    "hu-HU": (
        "For Hungarian, use natural direct technical-manual prose. "
        "Use informal tegezés consistently, not formal magázás. "
        "Prefer concise instructions and avoid overly literal English sentence structure."
    ),
    "it-IT": (
        "For Italian, use informal 'tu' consistently when addressing the reader. "
        "Use natural Italian technical-manual prose and avoid overly literal English sentence structure."
    ),
    "pl-PL": (
        "For Polish, use natural Polish technical-manual prose. "
        "Prefer concise direct instructions and avoid awkward literal translations from English."
    ),
    "pt-BR": (
        "For Brazilian Portuguese, use informal 'você' consistently when addressing the reader. "
        "Use natural Brazilian Portuguese technical-manual prose and avoid overly literal English sentence structure."
    ),
    "ko-KR": (
        "For Korean, use clear, concise, polite technical-manual prose. "
        "Do not over-translate established technical terms where an English UI label or common loanword is more natural. "
        "Avoid marketing-like phrasing."
    ),
    "zh-HK": (
        "For Traditional Chinese (Hong Kong), use Traditional Chinese characters and natural Hong Kong technical-manual wording. "
        "Avoid Simplified Chinese characters and Mainland-only terminology where a Hong Kong phrasing is more natural. "
        "Use clear, concise, practical prose and avoid marketing-like phrasing. "
        "Keep established English software/UI terms in English when that is the natural Hong Kong usage."
    ),
    "vi-VN": (
        "For Vietnamese, use clear, natural Vietnamese technical-manual prose. "
        "Use a direct, polite instructional tone and avoid overly literal English sentence structure. "
        "Keep established English software/UI terms in English where Vietnamese technical users would naturally expect them."
    ),
    "tr-TR": (
        "For Turkish, use natural Turkish technical-manual prose with an informal direct instructional tone. "
        "Avoid overly literal English sentence structure and keep sentences concise."
    ),
    "cs-CZ": (
        "For Czech, use natural Czech technical-manual prose. "
        "Use direct instructions, avoid awkward literal phrasing, and keep established technical loanwords where they are normal Czech usage."
    ),
    "hr-HR": (
        "For Croatian, use natural Croatian technical-manual prose. "
        "Use direct instructions, avoid Serbian-only wording, and avoid overly literal English sentence structure."
    ),
    "ru-RU": (
        "For Russian, use natural Russian technical-manual prose. "
        "Use clear direct instructions, avoid marketing-like phrasing, and keep established English software/UI terms in English when they refer to exact UI labels."
    ),
    "ar": (
        "For Arabic, use Modern Standard Arabic in clear technical-manual prose. "
        "Use a direct, practical instructional tone. Keep left-to-right product names, acronyms, file paths, UI labels, and code unchanged. "
        "Avoid regional colloquialisms."
    ),
    "zh-TW": (
        "For Traditional Chinese (Taiwan), use Traditional Chinese characters and natural Taiwan technical-manual wording. "
        "Avoid Simplified Chinese characters and Mainland-only terminology where Taiwan phrasing is more natural. "
        "Use clear, concise, practical prose and avoid marketing-like phrasing. "
        "Keep established English software/UI terms in English when that is the natural Taiwan usage."
    ),
}
DEFAULT_OPENAI_MODEL = "gpt-5.5"
DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-6"
RETRYABLE_HTTP_STATUS_CODES = {408, 409, 425, 429, 500, 502, 503, 504}
REQUEST_TIMEOUT_SECONDS = int(os.environ.get("TRANSLATE_REQUEST_TIMEOUT", "600"))
CURRENT_APP_TERMS = [
    "Liberation",
    "Clip",
    "Clips",
    "Clip Deck",
    "Clip Editor",
    "Creator",
    "Creators",
    "node",
    "nodes",
    "zone",
    "zones",
    "beam zone",
    "canvas zone",
    "DMX zone",
    "mask",
    "masks",
    "Canvas",
    "Output",
    "3D",
    "Output view",
    "Canvas view",
    "3D view",
    "Controller Assignment",
    "Laser Overview",
    "Laser Settings",
    "Global Brightness",
    "Test Pattern",
    "DISARM ALL",
    "APC40",
    "LaserCube",
    "DMX",
    "MIDI",
    "OSC",
    "ILDA",
    "DAC",
    "Art-Net",
]


MARKDOWN_TARGET_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)\s]+(?:\s+\"[^\"]*\")?)\)")
HTML_SRC_PATTERN = re.compile(r"\bsrc=[\"']([^\"']+)[\"']")
FENCE_PATTERN = re.compile(r"^```", re.MULTILINE)
DIRECTIVE_PATTERN = re.compile(r"^\s*{%\s*[^%]+%}\s*$", re.MULTILINE)


class TranslationValidationError(RuntimeError):
    pass


class TranslationPatchError(RuntimeError):
    pass


def git(*args, check=True):
    import subprocess

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
    import subprocess

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
    import subprocess

    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}:{path}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def content_at(commit, path):
    return git_bytes("show", f"{commit}:{path}")


def source_diff(previous_source_text, current_source_text, relative_path):
    return "\n".join(
        difflib.unified_diff(
            previous_source_text.splitlines(),
            current_source_text.splitlines(),
            fromfile=f"previous en-GB/{relative_path}",
            tofile=f"current en-GB/{relative_path}",
            lineterm="",
        )
    )


def https_context():
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def post_json(url, headers, payload, attempts=6):
    data = json.dumps(payload).encode("utf-8")

    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(
            url,
            data=data,
            headers={**headers, "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, context=https_context(), timeout=REQUEST_TIMEOUT_SECONDS) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", "replace")
            if error.code not in RETRYABLE_HTTP_STATUS_CODES or attempt == attempts:
                raise RuntimeError(f"{error.code} {error.reason}: {body}") from error
        except (TimeoutError, urllib.error.URLError) as error:
            if attempt == attempts:
                raise RuntimeError(f"Request failed after {attempts} attempts: {error}") from error

        time.sleep(min(2 ** attempt, 30))

    raise RuntimeError("Request failed without a response.")


def require_provider_key(provider):
    key_name = "OPENAI_API_KEY" if provider == "openai" else "ANTHROPIC_API_KEY"
    if not os.environ.get(key_name):
        raise SystemExit(f"{key_name} is not set.")


def openai_translate(system_prompt, user_prompt, model, max_output_tokens, reasoning_effort):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set.")

    payload = {
        "model": model,
        "instructions": system_prompt,
        "input": user_prompt,
        "max_output_tokens": max_output_tokens,
    }
    if reasoning_effort:
        payload["reasoning"] = {"effort": reasoning_effort}

    response = post_json(
        "https://api.openai.com/v1/responses",
        {"Authorization": f"Bearer {api_key}"},
        payload,
    )

    if response.get("output_text"):
        return response["output_text"]

    parts = []
    for item in response.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"}:
                parts.append(content.get("text", ""))
    if parts:
        return "".join(parts)

    raise RuntimeError(f"Could not find text output in OpenAI response: {response}")


def anthropic_translate(system_prompt, user_prompt, model, max_output_tokens, _reasoning_effort=None):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ANTHROPIC_API_KEY is not set.")

    response = post_json(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        {
            "model": model,
            "max_tokens": max_output_tokens,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        },
    )

    parts = [
        content.get("text", "")
        for content in response.get("content", [])
        if content.get("type") == "text"
    ]
    if parts:
        return "".join(parts)

    raise RuntimeError(f"Could not find text output in Anthropic response: {response}")


def markdown_targets(text):
    targets = []
    for match in MARKDOWN_TARGET_PATTERN.finditer(text):
        targets.append(match.group(1).strip())
    return targets


def html_sources(text):
    return HTML_SRC_PATTERN.findall(text)


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text

    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[: index + 1]), "".join(lines[index + 1 :])

    return None, text


def restore_preserved_targets(source, translated):
    source_frontmatter, _ = split_frontmatter(source)
    translated_frontmatter, translated_body = split_frontmatter(translated)
    if source_frontmatter:
        translated = source_frontmatter + (translated_body if translated_frontmatter else translated)
    elif translated_frontmatter:
        translated = translated_body

    source_markdown_targets = markdown_targets(source)
    translated_markdown_targets = markdown_targets(translated)
    if source_markdown_targets and len(source_markdown_targets) == len(translated_markdown_targets):
        target_iter = iter(source_markdown_targets)

        def replace_markdown_target(match):
            target = next(target_iter)
            relative_start = match.start(1) - match.start(0)
            relative_end = match.end(1) - match.start(0)
            return match.group(0)[:relative_start] + target + match.group(0)[relative_end:]

        translated = MARKDOWN_TARGET_PATTERN.sub(replace_markdown_target, translated)

    source_html_sources = html_sources(source)
    translated_html_sources = html_sources(translated)
    if source_html_sources and len(source_html_sources) == len(translated_html_sources):
        source_iter = iter(source_html_sources)

        def replace_html_source(match):
            source_path = next(source_iter)
            relative_start = match.start(1) - match.start(0)
            relative_end = match.end(1) - match.start(0)
            return match.group(0)[:relative_start] + source_path + match.group(0)[relative_end:]

        translated = HTML_SRC_PATTERN.sub(replace_html_source, translated)

    source_directives = DIRECTIVE_PATTERN.findall(source)
    translated_directives = DIRECTIVE_PATTERN.findall(translated)
    if source_directives and len(source_directives) == len(translated_directives):
        directive_iter = iter(source_directives)

        def replace_directive(_match):
            return next(directive_iter)

        translated = DIRECTIVE_PATTERN.sub(replace_directive, translated)

    return translated


def validation_errors(source, translated):
    errors = []
    if source.startswith("---") != translated.startswith("---"):
        errors.append("frontmatter boundary changed")
    if FENCE_PATTERN.findall(source) != FENCE_PATTERN.findall(translated):
        errors.append("code fence count changed")
    if markdown_targets(source) != markdown_targets(translated):
        errors.append("Markdown link targets changed")
    if html_sources(source) != html_sources(translated):
        errors.append("HTML image/source paths changed")
    if DIRECTIVE_PATTERN.findall(source) != DIRECTIVE_PATTERN.findall(translated):
        errors.append("GitBook directive lines changed")
    return errors


def strip_wrapper(text):
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines[0].startswith("```") and lines[-1].startswith("```"):
            return "\n".join(lines[1:-1]).strip() + "\n"
    return stripped + "\n"


def normalize_final_markdown(text):
    return text.rstrip() + "\n"


def source_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_translation_status():
    if not TRANSLATION_STATUS_PATH.exists():
        return {"source_root": str(SOURCE_ROOT), "entries": {}}
    return json.loads(TRANSLATION_STATUS_PATH.read_text(encoding="utf-8"))


def mark_translation_current(status, source, target):
    status.setdefault("source_root", str(SOURCE_ROOT))
    status.setdefault("entries", {})[str(target)] = {
        "source": str(source),
        "source_sha256": source_sha256(source),
    }


def write_translation_status(status):
    TRANSLATION_STATUS_PATH.write_text(
        json.dumps(status, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def system_prompt(target_language, language_name, output_kind="markdown"):
    style_guidance = LANGUAGE_STYLE_GUIDANCE.get(target_language, "")
    app_terms = ", ".join(CURRENT_APP_TERMS)
    output_instruction = (
        "Return only valid JSON matching the requested schema."
        if output_kind == "json"
        else "Return only the translated Markdown document."
    )
    return " ".join(
        part
        for part in [
            "You are translating a technical user manual for laser show software.",
            f"Translate natural-language text into {language_name}.",
            "Use a clear, professional, friendly technical-manual tone.",
            "Keep the writing direct and practical, not marketing-like.",
            "Prefer natural native phrasing over literal word-for-word translation.",
            "Preserve the author's concise, lightly conversational clarity where it fits the target language.",
            "Use consistent technical terminology throughout the manual.",
            "Keep exact on-screen UI labels in English when the text refers to labels, buttons, menu items, panels, or settings.",
            "Translate visible Markdown link text when it is natural-language text, while preserving each link target exactly.",
            "In SUMMARY.md files, preserve leading status emoji prefixes such as ✅, 🟩, 🟧, and ◼️ exactly.",
            "When a Markdown link points to another manual page or section, make the visible link text match",
            "the translated title or heading for that destination instead of leaving the English source title.",
            "For GitBook mention links, do not leave visible labels as filenames, paths, slugs, or English titles",
            "such as setting-up-lasers.md, output-view, or Quick start guide; use the translated destination heading.",
            "Current app terminology: because the app UI is currently in English, keep these app concepts and UI terms",
            f"in English when they refer to Liberation features: {app_terms}.",
            "When keeping an English app term, do not leave awkward English plural forms or source-language grammar in running prose;",
            "rewrite the surrounding sentence so it reads naturally in the target language.",
            "For arm/disarm/armed/disarmed, preserve exact UI labels such as DISARM ALL, but translate or explain prose actions",
            "and states naturally when that is clearer in the target language.",
            "This glossary applies to Liberation UI and app concepts, not to generic hardware, safety, network, or operating-system terms.",
            "Translate generic terms such as laser, laser output, emergency stop button, interlock, key switch, aperture cover,",
            "router, wired network, wireless network, network protocol, laser controller, controller, test pattern, output level,",
            "hardware, software, desktop, and file explorer naturally",
            "unless they are exact on-screen labels. Do not blindly leave whole English source phrases untranslated; use the target",
            "language's accepted technical term, loanword, or localized explanation, whichever is most natural for that language and",
            "industry context. For phrases such as E-stop, keyswitches, LaserCube network protocol, ILDA input, or 25-pin D connector,",
            "make a terminology decision rather than applying a blanket rule. In mixed technical descriptions, keep identifiers such as",
            "ILDA, 25-pin, D, and RJ45 stable while translating or localizing the descriptive words where appropriate.",
            "Keep established protocol, connector, product, and acronym names unchanged, including ILDA, DMX, MIDI, OSC, DAC, USB,",
            "RJ45, XLR, TRRS, IP, DHCP, Ethernet, Art-Net, Ether Dream, LaserCube, LaserOS, APC40, Windows, and macOS.",
            "Use Art-Net as the visible spelling everywhere; do not use ArtNet, Artnet, or Art net.",
            "Translate the surrounding sentence naturally and use local articles, descriptors, or short explanations when needed",
            "to make the English app term fit the target-language grammar.",
            "Do not create awkward hybrid forms by adding target-language verb or case endings directly to English app terms;",
            "rewrite the sentence around the English term instead.",
            "If the app UI is localized in the future, this glossary should be updated to the localized UI terms.",
            style_guidance,
            output_instruction,
            "Preserve Markdown structure, heading levels, tables, frontmatter keys, YAML indentation,",
            "GitBook directives, HTML tags, image paths, Markdown link targets, anchors, file paths,",
            "code fences, inline code, keyboard shortcuts, UI labels, and product names.",
        ]
        if part
    )


def user_prompt(relative_path, source_text, retry_errors=None):
    prompt = [
        f"Translate this Markdown file: {relative_path}",
        "",
        "Important:",
        "- Do not add commentary.",
        "- Do not wrap the result in a Markdown code fence.",
        "- Preserve every Markdown link target exactly, but translate visible Markdown link text.",
        "- In SUMMARY.md files, preserve leading status emoji prefixes such as ✅, 🟩, 🟧, and ◼️ exactly.",
        "- If a link points to another manual page or section, use visible link text that matches the translated title or heading for that destination.",
        "- Do not leave GitBook mention link labels as filenames, paths, slugs, or English titles.",
        "- Preserve every image src/path exactly.",
        "- Preserve code fences and inline code exactly.",
    ]
    if retry_errors:
        prompt.extend(["", "The previous attempt failed validation:", *[f"- {error}" for error in retry_errors]])
    prompt.extend(["", source_text])
    return "\n".join(prompt)


def stale_update_prompt(relative_path, previous_source_text, current_source_text, existing_translation_text, retry_errors=None):
    prompt = [
        f"Update this Markdown translation: {relative_path}",
        "",
        "The existing translated Markdown was created from an earlier English version.",
        "Use the English source diff to identify exactly what changed.",
        "Update only the translated passages affected by that English diff.",
        "Preserve unchanged translated text exactly unless a small grammar adjustment is required around a changed passage.",
        "",
        "Important:",
        "- Return the complete updated translated Markdown document, not a diff.",
        "- Do not add commentary.",
        "- Do not wrap the result in a Markdown code fence.",
        "- Preserve every Markdown link target exactly, but translate visible Markdown link text.",
        "- In SUMMARY.md files, preserve leading status emoji prefixes such as ✅, 🟩, 🟧, and ◼️ exactly.",
        "- If a link points to another manual page or section, use visible link text that matches the translated title or heading for that destination.",
        "- Do not leave GitBook mention link labels as filenames, paths, slugs, or English titles.",
        "- Preserve every image src/path exactly.",
        "- Preserve code fences and inline code exactly.",
    ]
    if retry_errors:
        prompt.extend(["", "The previous attempt failed validation:", *[f"- {error}" for error in retry_errors]])
    prompt.extend(
        [
            "",
            "<english_source_diff>",
            source_diff(previous_source_text, current_source_text, relative_path),
            "</english_source_diff>",
            "",
            "<existing_translated_markdown>",
            existing_translation_text,
            "</existing_translated_markdown>",
        ]
    )
    return "\n".join(prompt)


def split_markdown_blocks(text):
    def flush_current():
        nonlocal current
        if current:
            blocks.append("".join(current))
            current = []

    def line_block_boundary(line):
        stripped = line.lstrip()
        return bool(
            re.match(r"#{1,6}\s", stripped)
            or re.match(r"[*+-]\s", stripped)
            or re.match(r"\d+\.\s", stripped)
            or stripped.startswith("|")
            or DIRECTIVE_PATTERN.fullmatch(line.rstrip("\n"))
        )

    blocks = []
    current = []
    lines = text.splitlines(keepends=True)
    index = 0

    if lines and lines[0].strip() == "---":
        current.append(lines[0])
        index = 1
        while index < len(lines):
            current.append(lines[index])
            if lines[index].strip() == "---":
                index += 1
                break
            index += 1
        flush_current()

    while index < len(lines):
        line = lines[index]

        if line.startswith("```"):
            flush_current()
            current.append(line)
            index += 1
            while index < len(lines):
                current.append(lines[index])
                if lines[index].startswith("```"):
                    index += 1
                    break
                index += 1
            flush_current()
            continue

        if line.lstrip().startswith("<figure"):
            flush_current()
            current.append(line)
            index += 1
            while index < len(lines) and "</figure>" not in current[-1]:
                current.append(lines[index])
                index += 1
            flush_current()
            continue

        if line_block_boundary(line):
            flush_current()
            blocks.append(line)
            index += 1
            continue

        current.append(line)
        if not line.strip():
            flush_current()
        index += 1
    flush_current()
    return blocks


def trailing_blank_suffix(block):
    match = re.search(r"((?:[ \t]*\n)+)\Z", block)
    return match.group(1) if match else ""


def normalize_existing_block_spacing(translated, source_block):
    suffix = trailing_blank_suffix(source_block)
    if not suffix:
        return translated
    return translated.rstrip() + suffix


def normalize_translated_block(translated, source_block):
    suffix = trailing_blank_suffix(source_block)
    body = strip_wrapper(translated).rstrip()
    return body + suffix


def protected_block(block):
    stripped = block.strip()
    if not stripped:
        return True
    if stripped.startswith("---"):
        return True
    if stripped.startswith("```"):
        return True
    if stripped.startswith("<figure") and stripped.endswith("</figure>"):
        return True
    lines = [line for line in stripped.splitlines() if line.strip()]
    if lines and all(DIRECTIVE_PATTERN.fullmatch(line) for line in lines):
        return True
    return not re.search(r"[A-Za-z]", stripped)


def align_translated_blocks(previous_blocks, translated_blocks):
    if len(previous_blocks) == len(translated_blocks):
        return translated_blocks

    previous_nonblank = sum(1 for block in previous_blocks if block.strip())
    translated_nonblank = sum(1 for block in translated_blocks if block.strip())
    if previous_nonblank != translated_nonblank:
        raise TranslationPatchError(
            "cannot safely patch by block because previous English and existing translation "
            f"have different nonblank block counts ({previous_nonblank} vs {translated_nonblank})"
        )

    aligned = []
    translated_index = 0
    for previous_block in previous_blocks:
        if not previous_block.strip():
            if translated_index < len(translated_blocks) and not translated_blocks[translated_index].strip():
                aligned.append(translated_blocks[translated_index])
                translated_index += 1
            else:
                aligned.append(previous_block)
            continue

        while translated_index < len(translated_blocks) and not translated_blocks[translated_index].strip():
            translated_index += 1
        if translated_index >= len(translated_blocks):
            raise TranslationPatchError("cannot safely patch by block because translation alignment ended early")
        aligned.append(translated_blocks[translated_index])
        translated_index += 1

    remaining = translated_blocks[translated_index:]
    if any(block.strip() for block in remaining):
        raise TranslationPatchError("cannot safely patch by block because translation alignment has extra content")
    return aligned


def make_block_patch_plan(previous_source_text, current_source_text, existing_translation_text):
    previous_blocks = split_markdown_blocks(previous_source_text)
    current_blocks = split_markdown_blocks(current_source_text)
    translated_blocks = align_translated_blocks(previous_blocks, split_markdown_blocks(existing_translation_text))

    result = []
    items = []
    matcher = difflib.SequenceMatcher(a=previous_blocks, b=current_blocks, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for offset, block in enumerate(translated_blocks[i1:i2]):
                result.append(("text", normalize_existing_block_spacing(block, current_blocks[j1 + offset])))
            continue
        if tag == "delete":
            continue

        for offset, current_block in enumerate(current_blocks[j1:j2]):
            previous_index = i1 + offset
            previous_block = previous_blocks[previous_index] if tag == "replace" and previous_index < i2 else ""
            existing_block = translated_blocks[previous_index] if tag == "replace" and previous_index < i2 else ""
            if protected_block(current_block):
                result.append(("text", current_block))
                continue

            item_id = f"b{len(items) + 1}"
            items.append(
                {
                    "id": item_id,
                    "previous_english": previous_block,
                    "current_english": current_block,
                    "existing_translation": existing_block,
                }
            )
            result.append(("item", item_id, current_block))

    return result, items


def block_update_prompt(relative_path, items, retry_errors=None):
    prompt = [
        f"Update changed Markdown translation blocks for: {relative_path}",
        "",
        "Each item contains one changed English Markdown block.",
        "Use previous_english and existing_translation as context.",
        "Translate current_english into the target language for each item.",
        "Preserve unchanged translated wording from existing_translation where it is still valid.",
        "",
        "Important:",
        "- Return only valid JSON.",
        "- Use exactly this schema: {\"translations\":[{\"id\":\"b1\",\"translation\":\"...\"}]}",
        "- Return one translation object for every input id, using the same id values.",
        "- Do not add commentary.",
        "- Preserve Markdown syntax, heading levels, list markers, table columns, HTML tags, GitBook directives, links, image paths, inline code, keyboard shortcuts, UI labels, and product names.",
        "- Preserve every Markdown link target exactly, but translate visible Markdown link text.",
        "- Preserve every image src/path exactly.",
        "- Preserve code fences and inline code exactly.",
    ]
    if retry_errors:
        prompt.extend(["", "The previous attempt failed validation:", *[f"- {error}" for error in retry_errors]])
    prompt.extend(
        [
            "",
            "<changed_blocks_json>",
            json.dumps({"items": items}, ensure_ascii=False, indent=2),
            "</changed_blocks_json>",
        ]
    )
    return "\n".join(prompt)


def parse_block_translations(text, expected_ids):
    raw = strip_wrapper(text).strip()
    if not raw.startswith("{"):
        start = raw.find("{")
        end = raw.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise TranslationValidationError("block update did not return JSON")
        raw = raw[start : end + 1]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        raise TranslationValidationError(f"block update returned invalid JSON: {error}") from error

    translations = data.get("translations")
    if not isinstance(translations, list):
        raise TranslationValidationError("block update JSON missing translations list")

    by_id = {}
    for item in translations:
        if not isinstance(item, dict):
            raise TranslationValidationError("block update JSON contains a non-object translation item")
        item_id = item.get("id")
        translation = item.get("translation")
        if not isinstance(item_id, str) or not isinstance(translation, str):
            raise TranslationValidationError("block update JSON items must contain string id and translation")
        by_id[item_id] = translation

    missing = [item_id for item_id in expected_ids if item_id not in by_id]
    extra = [item_id for item_id in by_id if item_id not in expected_ids]
    if missing or extra:
        details = []
        if missing:
            details.append(f"missing ids: {', '.join(missing)}")
        if extra:
            details.append(f"unexpected ids: {', '.join(extra)}")
        raise TranslationValidationError("; ".join(details))

    return by_id


def apply_block_translations(result_plan, translations):
    blocks = []
    for entry in result_plan:
        if entry[0] == "text":
            blocks.append(entry[1])
            continue
        _, item_id, source_block = entry
        blocks.append(normalize_translated_block(translations[item_id], source_block))
    return "".join(blocks)


def estimate_block_plan(previous_source_text, current_source_text, existing_translation_text):
    result_plan, items = make_block_patch_plan(previous_source_text, current_source_text, existing_translation_text)
    prompt_chars = len(json.dumps({"items": items}, ensure_ascii=False))
    output_chars = sum(len(item["current_english"]) for item in items)
    return {
        "items": items,
        "result_plan": result_plan,
        "input_chars": prompt_chars,
        "output_chars": output_chars,
    }


def translate_stale_blocks(
    provider,
    model,
    reasoning_effort,
    target_language,
    language_name,
    relative_path,
    current_source_text,
    previous_source_text,
    existing_translation_text,
    retries,
    max_output_tokens,
):
    plan = estimate_block_plan(previous_source_text, current_source_text, existing_translation_text)
    items = plan["items"]
    if not items:
        result = apply_block_translations(plan["result_plan"], {})
        result = restore_preserved_targets(current_source_text, result)
        errors = validation_errors(current_source_text, result)
        if errors:
            raise TranslationValidationError(f"{relative_path} failed validation: {', '.join(errors)}")
        return result

    translate = openai_translate if provider == "openai" else anthropic_translate
    system = system_prompt(target_language, language_name, output_kind="json")
    expected_ids = [item["id"] for item in items]
    errors = None
    for attempt in range(1, retries + 2):
        try:
            translations = parse_block_translations(
                translate(
                    system,
                    block_update_prompt(relative_path, items, errors),
                    model,
                    max_output_tokens,
                    reasoning_effort,
                ),
                expected_ids,
            )
            result = apply_block_translations(plan["result_plan"], translations)
            result = restore_preserved_targets(current_source_text, result)
            errors = validation_errors(current_source_text, result)
        except TranslationValidationError as error:
            errors = [str(error)]
        if not errors:
            return result
        if attempt <= retries:
            time.sleep(1)

    raise TranslationValidationError(f"{relative_path} failed validation: {', '.join(errors or [])}")


def translate_with_prompt(
    provider,
    model,
    reasoning_effort,
    system,
    prompt,
    relative_path,
    source_text,
    retries,
    max_output_tokens,
):
    translate = openai_translate if provider == "openai" else anthropic_translate
    errors = None
    for attempt in range(1, retries + 2):
        result = strip_wrapper(
            translate(
                system,
                prompt(errors),
                model,
                max_output_tokens,
                reasoning_effort,
            )
        )
        result = restore_preserved_targets(source_text, result)
        errors = validation_errors(source_text, result)
        if not errors:
            return result
        if attempt <= retries:
            time.sleep(1)

    raise TranslationValidationError(f"{relative_path} failed validation: {', '.join(errors or [])}")


def translate_text(
    provider,
    model,
    reasoning_effort,
    target_language,
    language_name,
    relative_path,
    source_text,
    retries,
    max_output_tokens,
    previous_source_text=None,
    existing_translation_text=None,
    stale_strategy="blocks",
    allow_full_fallback=False,
):
    system = system_prompt(target_language, language_name)

    if previous_source_text and existing_translation_text and previous_source_text != source_text:
        if stale_strategy == "blocks":
            try:
                return translate_stale_blocks(
                    provider,
                    model,
                    reasoning_effort,
                    target_language,
                    language_name,
                    relative_path,
                    source_text,
                    previous_source_text,
                    existing_translation_text,
                    retries,
                    max_output_tokens,
                )
            except (TranslationPatchError, TranslationValidationError) as error:
                if not allow_full_fallback:
                    raise
                print(
                    f"Warning: block update failed for {relative_path}: {error}. Falling back to full translation.",
                    file=sys.stderr,
                )

        elif stale_strategy == "diff":
            try:
                return translate_with_prompt(
                    provider,
                    model,
                    reasoning_effort,
                    system,
                    lambda errors: stale_update_prompt(
                        relative_path,
                        previous_source_text,
                        source_text,
                        existing_translation_text,
                        errors,
                    ),
                    relative_path,
                    source_text,
                    retries,
                    max_output_tokens,
                )
            except TranslationValidationError as error:
                if not allow_full_fallback:
                    raise
                print(
                    f"Warning: diff-based update failed for {relative_path}: {error}. Falling back to full translation.",
                    file=sys.stderr,
                )

        elif stale_strategy != "full":
            raise RuntimeError(f"Unknown stale strategy: {stale_strategy}")

    if (
        previous_source_text
        and existing_translation_text
        and previous_source_text != source_text
        and not allow_full_fallback
        and stale_strategy != "full"
    ):
        raise TranslationValidationError(
            f"{relative_path} needs full-file translation; rerun with --allow-full-fallback or --stale-strategy full"
        )

    return translate_with_prompt(
        provider,
        model,
        reasoning_effort,
        system,
        lambda errors: user_prompt(relative_path, source_text, errors),
        relative_path,
        source_text,
        retries,
        max_output_tokens,
    )


def git_changed_paths(source_root, spec, since=False):
    if since:
        output = git("diff", "--name-only", f"{spec}..HEAD", "--", str(source_root))
    elif ".." in spec:
        output = git("diff", "--name-only", spec, "--", str(source_root))
    else:
        output = git("show", "--name-only", "--format=", spec, "--", str(source_root))

    paths = []
    for line in output.splitlines():
        path = Path(line.strip())
        if not line.strip() or path.suffix != ".md":
            continue
        try:
            paths.append(path.relative_to(source_root))
        except ValueError:
            continue
    return paths


def source_files(source_root, paths, since=None, paths_from_git=None):
    selected = [Path(path) for path in paths]
    if since:
        selected.extend(git_changed_paths(source_root, since, since=True))
    if paths_from_git:
        selected.extend(git_changed_paths(source_root, paths_from_git))
    if selected:
        seen = set()
        files = []
        for path in selected:
            if path in seen:
                continue
            seen.add(path)
            files.append(source_root / path)
        return files
    return sorted(source_root.rglob("*.md"))


def should_translate(source, target, mode, force):
    if force:
        return True
    if not target.exists():
        return True
    if mode == "missing":
        return False
    if mode == "all":
        return True

    commit = last_commit(target)
    if not commit:
        return False
    if not path_exists_at(commit, source):
        return True
    return content_at(commit, source) != source.read_bytes()


def write_book_json(target_root, target_language):
    path = target_root / "book.json"
    if path.exists():
        return
    title = BOOK_TITLES.get(target_language, "Liberation User Manual")
    path.write_text(
        json.dumps({"title": title, "language": target_language}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def update_langs(target_language):
    label = LANGS_LABELS.get(target_language, LANGUAGE_NAMES.get(target_language, target_language))
    langs = Path("LANGS.md")
    line = f"* [{label}]({target_language})"
    if not langs.exists():
        langs.write_text(f"# Languages\n\n* [English](en-GB)\n{line}\n", encoding="utf-8")
        return

    content = langs.read_text(encoding="utf-8")
    if f"]({target_language})" in content:
        return
    if not content.endswith("\n"):
        content += "\n"
    langs.write_text(content + line + "\n", encoding="utf-8")


def stale_context(source, target, mode, stale_strategy, force):
    if mode != "stale" or stale_strategy == "full" or force or not target.exists():
        return None, None
    commit = last_commit(target)
    if not commit or not path_exists_at(commit, source):
        return None, None
    source_text = source.read_text(encoding="utf-8")
    return (
        content_at(commit, source).decode("utf-8", "replace"),
        restore_preserved_targets(source_text, target.read_text(encoding="utf-8")),
    )


def dry_run_details(source, target, rel, args):
    source_text = source.read_text(encoding="utf-8")
    previous_source_text, existing_translation_text = stale_context(
        source,
        target,
        args.mode,
        args.stale_strategy,
        args.force,
    )

    if (
        args.mode == "stale"
        and args.stale_strategy == "blocks"
        and previous_source_text
        and existing_translation_text
        and previous_source_text != source_text
    ):
        try:
            plan = estimate_block_plan(previous_source_text, source_text, existing_translation_text)
        except TranslationPatchError as error:
            return f"- {rel} (needs full-file fallback: {error})"
        return (
            f"- {rel} "
            f"(changed blocks: {len(plan['items'])}; "
            f"approx input chars: {plan['input_chars']}; "
            f"approx output chars: {plan['output_chars']})"
        )

    if (
        args.mode == "stale"
        and args.stale_strategy == "diff"
        and previous_source_text
        and existing_translation_text
        and previous_source_text != source_text
    ):
        diff_chars = len(source_diff(previous_source_text, source_text, rel))
        input_chars = diff_chars + len(existing_translation_text)
        return (
            f"- {rel} "
            f"(page-diff update; approx input chars: {input_chars}; "
            f"approx output chars: {len(source_text)})"
        )

    return f"- {rel} (full-file translation; approx input chars: {len(source_text)}; approx output chars: {len(source_text)})"


def parse_args():
    parser = argparse.ArgumentParser(description="Translate docs with OpenAI or Anthropic APIs.")
    parser.add_argument("target_language", help="Target locale folder, for example de-DE.")
    parser.add_argument("--language-name", help="Human-readable target language name.")
    parser.add_argument(
        "--provider",
        choices=["openai", "anthropic"],
        default=os.environ.get("TRANSLATE_PROVIDER", "openai"),
    )
    parser.add_argument("--model", help="Provider model. Defaults to a sensible model for the provider.")
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh"],
        default=os.environ.get("TRANSLATE_REASONING_EFFORT", "low"),
        help="OpenAI reasoning effort for translation calls. Defaults to low. Ignored by Anthropic.",
    )
    parser.add_argument("--source-root", type=Path, default=SOURCE_ROOT)
    parser.add_argument("--mode", choices=["missing", "stale", "all"], default="missing")
    parser.add_argument(
        "--stale-strategy",
        choices=["blocks", "diff", "full"],
        default=os.environ.get("TRANSLATE_STALE_STRATEGY", "blocks"),
        help="For stale files, update changed Markdown blocks, update from the English diff, or retranslate the full file.",
    )
    parser.add_argument("--path", action="append", default=[], help="Relative Markdown path to translate.")
    parser.add_argument("--since", help="Only translate source Markdown changed between this git ref and HEAD.")
    parser.add_argument(
        "--paths-from-git",
        help="Only translate source Markdown changed in this git commit or range, for example bccdd22 or main~3..main.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing target files.")
    parser.add_argument(
        "--allow-full-fallback",
        action="store_true",
        help="Allow stale block/diff updates to fall back to full-file translation if patch validation fails.",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, help="Translate at most this many files.")
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--max-output-tokens", type=int, default=12000)
    parser.add_argument("--update-langs", action="store_true", help="Add the target language to LANGS.md.")
    return parser.parse_args()


def main():
    args = parse_args()
    target_root = Path(args.target_language)
    language_name = args.language_name or LANGUAGE_NAMES.get(args.target_language)
    if not language_name:
        raise SystemExit("--language-name is required for unknown target locales.")

    model = args.model
    if not model:
        model = DEFAULT_OPENAI_MODEL if args.provider == "openai" else DEFAULT_ANTHROPIC_MODEL
    reasoning_effort = args.reasoning_effort if args.provider == "openai" else None

    files = []
    for source in source_files(args.source_root, args.path, args.since, args.paths_from_git):
        if not source.exists():
            raise SystemExit(f"Source path does not exist: {source}")
        rel = source.relative_to(args.source_root)
        target = target_root / rel
        if should_translate(source, target, args.mode, args.force):
            files.append((source, target, rel))

    if args.limit:
        files = files[: args.limit]

    print(f"Provider: {args.provider}")
    print(f"Model:    {model}")
    if args.provider == "openai":
        print(f"Reasoning effort: {reasoning_effort}")
    print(f"Target:   {args.target_language} ({language_name})")
    print(f"Files:    {len(files)}")
    if args.mode == "stale":
        print(f"Strategy: {args.stale_strategy}")

    if args.dry_run:
        total_input_chars = 0
        total_output_chars = 0
        for source, target, rel in files:
            details = dry_run_details(source, target, rel, args)
            print(details)
            for label, value in re.findall(r"approx (input|output) chars: (\d+)", details):
                if label == "input":
                    total_input_chars += int(value)
                else:
                    total_output_chars += int(value)
        if files:
            print(f"Approx total input chars:  {total_input_chars}")
            print(f"Approx total output chars: {total_output_chars}")
        return

    require_provider_key(args.provider)
    target_root.mkdir(parents=True, exist_ok=True)
    write_book_json(target_root, args.target_language)
    translation_status = load_translation_status()

    for index, (source, target, rel) in enumerate(files, start=1):
        print(f"[{index}/{len(files)}] {rel}", flush=True)
        source_text = source.read_text(encoding="utf-8")
        previous_source_text, existing_translation_text = stale_context(
            source,
            target,
            args.mode,
            args.stale_strategy,
            args.force,
        )

        translated = translate_text(
            args.provider,
            model,
            reasoning_effort,
            args.target_language,
            language_name,
            rel,
            source_text,
            args.retries,
            args.max_output_tokens,
            previous_source_text,
            existing_translation_text,
            args.stale_strategy,
            args.allow_full_fallback,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(normalize_final_markdown(translated), encoding="utf-8")
        mark_translation_current(translation_status, source, target)

    if files:
        write_translation_status(translation_status)

    if args.update_langs:
        update_langs(args.target_language)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
