# Translation workflow

English in `en-GB` is the source of truth. Other language folders mirror the same Markdown paths.

## API keys

For OpenAI:

```sh
export OPENAI_API_KEY="..."
```

For Claude:

```sh
export ANTHROPIC_API_KEY="..."
```

## Initial translation

German with OpenAI:

```sh
npm run translate:docs -- de-DE --language-name German --update-langs
```

German with Claude:

```sh
npm run translate:docs -- de-DE --language-name German --provider anthropic --update-langs
```

Use `--model` to override the default model. The default OpenAI model is `gpt-5.5` for high-quality documentation translation.

## Tone and terminology

The translation prompt asks for a clear, friendly, practical technical-manual tone rather than marketing copy. It also asks the model to use native phrasing instead of literal word-for-word translation, while preserving Markdown structure, links, image paths, code, keyboard shortcuts, UI labels, and product names.

Language-specific reader address:

* German: informal `du`, not formal `Sie`.
* Dutch: informal `je/jij`.
* French: `vous`.
* Spanish: European Spanish with informal `tu`.
* Danish, Norwegian Bokmål, Swedish, Icelandic, Italian, and Brazilian Portuguese: informal direct address.
* Finnish and Polish: natural direct technical-manual prose.
* Hungarian: informal `te` / tegezés, not formal magázás.
* Japanese and Korean: concise polite technical-manual prose.
* Traditional Chinese (Hong Kong): Traditional Chinese characters with natural Hong Kong technical-manual wording; avoid Simplified Chinese characters and Mainland-only terminology.

Exact on-screen UI labels should stay in English when the text refers to labels, buttons, menu items, panels, or settings.

Current app terminology should also stay in English when it refers to Liberation concepts, because the app UI is currently in English. This includes terms such as `Clip`, `Clip Deck`, `Clip Editor`, `Creator`, `node`, `zone`, `beam zone`, `canvas zone`, `DMX zone`, `mask`, `Canvas`, `Output`, `Output view`, `Laser Overview`, `Laser Settings`, `Global Brightness`, `test pattern`, `arm`, `disarm`, `controller`, `APC40`, `LaserCube`, `DMX`, `MIDI`, `OSC`, `ILDA`, `DAC`, and `Art-Net`. Translate the surrounding sentence naturally, but keep these terms aligned with the app. Use local articles, descriptors, or short explanations when needed to make the English term fit the target-language grammar. Avoid awkward hybrid forms where English app terms get target-language endings bolted onto them; rewrite around the term instead. If the app UI is localized later, update this glossary to the localized UI terms.

This glossary is not a reason to keep generic hardware, safety, network, or operating-system words in English. Translate terms such as laser, laser output, emergency stop button, interlock, key switch, aperture cover, router, wired network, wireless network, network protocol, hardware, software, desktop, and file explorer naturally unless they are exact on-screen labels. Do not blindly leave whole English source phrases untranslated; use the target language's accepted technical term, loanword, or localized explanation, whichever is most natural for that language and industry context. For phrases such as `E-stop`, `keyswitches`, `LaserCube network protocol`, `ILDA input`, or `25-pin D connector`, make a terminology decision rather than applying a blanket rule. In mixed technical descriptions, keep identifiers such as `ILDA`, `25-pin`, `D`, and `RJ45` stable while translating or localizing the descriptive words where appropriate.

Established protocol, connector, product, and acronym names should remain stable. Keep names such as `ILDA`, `DMX`, `MIDI`, `OSC`, `DAC`, `USB`, `RJ45`, `XLR`, `TRRS`, `IP`, `DHCP`, `Ethernet`, `Art-Net`, `Ether Dream`, `LaserCube`, `LaserOS`, `APC40`, `Windows`, and `macOS` unchanged, while translating the descriptive words around them. Use `Art-Net` as the visible spelling everywhere; do not use `ArtNet`, `Artnet`, or `Art net`.

Visible Markdown link text should be translated when it is natural-language text. For links to other pages or sections in the manual, the visible text should match the translated title or heading for that destination, while the link target itself must stay exactly the same.

GitBook mention links must not keep visible labels as filenames, paths, slugs, or English titles such as `setting-up-lasers.md`, `output-view`, or `Quick start guide`. Use the translated destination title or heading as the visible link text.

## Keeping translations current

Check translation freshness from git history:

```sh
npm run check:translations
```

Update only missing or stale German pages:

```sh
npm run translate:docs -- de-DE --language-name German --mode stale
```

Translate a single page:

```sh
npm run translate:docs -- de-DE --language-name German --path setting-up/laser-settings.md --force
```

Run the normal checks after translating:

```sh
npm run check:translations
npm run check:links
npm run build:site
```

`npm run check:links` also checks translated internal link labels so stale English page titles and filename-style mention labels cannot be reintroduced silently.
