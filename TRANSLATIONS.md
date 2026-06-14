# Translation workflow

English in `en-GB` is the source of truth. Other language folders mirror the same Markdown paths.

Keep the English source consistent with [STYLE_GUIDE.md](STYLE_GUIDE.md). Before translating English edits, run:

```sh
npm run check:english-style
```

`en-US` is a generated English variant rather than an AI translation. Regenerate it from `en-GB` after English edits:

```sh
npm run localize:en-us
```

The generator applies conservative UK-to-US spelling and terminology substitutions while preserving Markdown link targets, image paths, URLs, code, keyboard shortcuts, and the underlying file structure.

## Operating model

Production docs are built with HonKit and deployed to GitHub Pages by `.github/workflows/honkit-pages.yml`. The live site is:

```text
https://docs.liberationlaser.com/
```

GitHub Pages deploys production from `main`. It does not currently create a separate public Pages URL for each pull request. Preview translation PRs locally from the PR branch before merging.

The intended workflow is:

1. Edit `en-GB` only.
2. Run `npm run manual:uk:check`.
3. Commit and push `main`.
4. Let GitHub Pages deploy the English/source update.
5. Let `Translation Updates` open/update translation PRs on the weekly or monthly cadence.
6. Preview and merge translation PRs when they look good.

Do not update every translated locale for every English edit. The cadence exists to keep English changes fast and to avoid unnecessary translation API usage.

For terminology changes, do not run bulk search/replace across translated locale folders. That touches translation git history and can make freshness checks treat manually edited translations as current. Make the change in `en-GB`, regenerate `en-US`, and leave AI-translated locales to the weekly or monthly translation PRs. If an asset filename contains old terminology, keep the filename stable during a normal English edit unless generated-image checks prove all locale references have been updated through the translation workflow.

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

OpenAI translation calls default to `--reasoning-effort low`, which is usually enough for structured translation and keeps cost and latency down. Use `--reasoning-effort medium` for difficult pages or retries. The value can also be set with `TRANSLATE_REASONING_EFFORT`.

## Tone and terminology

The translation prompt asks for a clear, friendly, practical technical-manual tone rather than marketing copy. It also asks the model to use native phrasing instead of literal word-for-word translation, while preserving Markdown structure, links, image paths, code, keyboard shortcuts, UI labels, and product names.

Language-specific reader address:

* German: informal `du`, not formal `Sie`.
* Dutch: informal `je/jij`; use natural Dutch technical-manual prose. Translate normal headings such as `Licences` to `Licenties` unless they are exact UI labels. Keep exact UI labels in English, but translate explanatory prose around them. Avoid awkward English/Dutch hybrids such as `arm-en`; for prose actions and states like `arm`, `disarm`, `armed`, and `disarmed`, use natural Dutch wording such as `activeren`, `deactiveren`, `inschakelen voor output`, or `voor output activeren` depending on context. Do not leave explanatory phrases such as `currently selected clip` in English in running Dutch prose; use natural Dutch such as `momenteel geselecteerde clip`.
* French: `vous`.
* Spanish: European Spanish with informal `tu`.
* Danish, Norwegian Bokmål, Swedish, Icelandic, Italian, and Brazilian Portuguese: informal direct address.
* Finnish and Polish: natural direct technical-manual prose.
* Hungarian: informal `te` / tegezés, not formal magázás.
* Japanese and Korean: concise polite technical-manual prose.
* Traditional Chinese (Hong Kong): Traditional Chinese characters with natural Hong Kong technical-manual wording; avoid Simplified Chinese characters and Mainland-only terminology.
* Vietnamese, Turkish, Czech, Croatian, and Russian: natural direct technical-manual prose with concise instructions and no literal English sentence structure.
* Arabic: Modern Standard Arabic, direct practical technical-manual prose, with left-to-right product names, acronyms, file paths, UI labels, and code unchanged.
* Traditional Chinese (Taiwan): Traditional Chinese characters with natural Taiwan technical-manual wording; avoid Simplified Chinese characters and Mainland-only terminology.

Exact on-screen UI labels should stay in English when the text refers to labels, buttons, menu items, panels, or settings.

Current app terminology should also stay in English when it refers to Liberation concepts, because the app UI is currently in English. This includes terms such as `Clip`, `Clip Deck`, `Clip Editor`, `Creator`, `node`, `zone`, `beam zone`, `canvas zone`, `DMX zone`, `mask`, `Canvas`, `Output`, `Output view`, `Controller Assignment`, `Laser Overview`, `Laser Settings`, `Global Brightness`, `Test Pattern`, `DISARM ALL`, `APC40`, `LaserCube`, `DMX`, `MIDI`, `OSC`, `ILDA`, `DAC`, and `Art-Net`. Translate the surrounding sentence naturally, but keep these terms aligned with the app. Use local articles, descriptors, or short explanations when needed to make the English term fit the target-language grammar. Avoid awkward English plural forms and awkward hybrid forms where English app terms get target-language endings bolted onto them; rewrite around the term instead. For `arm`, `disarm`, `armed`, and `disarmed`, keep exact UI labels such as `DISARM ALL`, but translate or explain prose actions and states naturally when that is clearer in the target language. If the app UI is localized later, update this glossary to the localized UI terms.

This glossary is not a reason to keep generic hardware, safety, network, or operating-system words in English. Translate terms such as laser, laser output, emergency stop button, interlock, key switch, aperture cover, router, wired network, wireless network, network protocol, laser controller, controller, test pattern, output level, hardware, software, desktop, and file explorer naturally unless they are exact on-screen labels. Do not blindly leave whole English source phrases untranslated; use the target language's accepted technical term, loanword, or localized explanation, whichever is most natural for that language and industry context. For phrases such as `E-stop`, `keyswitches`, `LaserCube network protocol`, `ILDA input`, or `25-pin D connector`, make a terminology decision rather than applying a blanket rule. In mixed technical descriptions, keep identifiers such as `ILDA`, `25-pin`, `D`, and `RJ45` stable while translating or localizing the descriptive words where appropriate.

Established protocol, connector, product, and acronym names should remain stable. Keep names such as `ILDA`, `DMX`, `MIDI`, `OSC`, `DAC`, `USB`, `RJ45`, `XLR`, `TRRS`, `IP`, `DHCP`, `Ethernet`, `Art-Net`, `Ether Dream`, `LaserCube`, `LaserOS`, `APC40`, `Windows`, and `macOS` unchanged, while translating the descriptive words around them. Use `Art-Net` as the visible spelling everywhere; do not use `ArtNet`, `Artnet`, or `Art net`.

Visible Markdown link text should be translated when it is natural-language text. For links to other pages or sections in the manual, the visible text should match the translated title or heading for that destination, while the link target itself must stay exactly the same.

GitBook mention links must not keep visible labels as filenames, paths, slugs, or English titles such as `setting-up-lasers.md`, `output-view`, or `Quick start guide`. Use the translated destination title or heading as the visible link text.

In `SUMMARY.md`, preserve leading status emoji prefixes such as `✅`, `🟩`, `🟧`, and `◼️` exactly. Translate the page title after the emoji, but do not remove or change the emoji marker.

## Keeping translations current

The translation workflow is deliberately batched so English updates are not blocked by every locale.

For normal manual edits, update `en-GB` first and run the English/build checks:

```sh
npm run manual:uk:check
```

This does not update translations.

GitHub Pages will deploy the `en-GB` update from `main`. Translations should be handled by the scheduled GitHub workflow or by an intentional manual batch run.

Check translation freshness from git history:

```sh
npm run check:translations
```

Regenerate US English and update the weekly priority AI locales:

```sh
npm run translate:weekly
```

Preview the weekly update first:

```sh
npm run translate:weekly:dry-run
```

Regenerate US English and update every AI locale:

```sh
npm run translate:monthly
```

Preview the monthly update first:

```sh
npm run translate:monthly:dry-run
```

The weekly and monthly locale lists live in `translation-tiers.json`. The batch runner records successful runs in `.translation-cadence.json` and refuses to run the same tier too soon. Weekly batches are held for 7 days, and monthly batches are held for 28 days.

If a scheduled run is not due, the workflow exits cleanly without opening a PR. This prevents expected cadence skips from showing as failed GitHub Actions runs.

If an urgent translation fix is needed, either translate the specific page with `translate:docs` or pass `--force-cadence` to the batch command, for example:

```sh
npm run translate:weekly -- --force-cadence
```

By default, stale mode uses git history to compare the current English file with the English version from the last commit where the matching translated file was touched. Existing stale files use `--stale-strategy blocks`: the script splits the page into Markdown blocks, sends only changed translatable blocks to the translation API, and stitches the translated blocks back into the existing page locally. This keeps unchanged translated blocks out of the API request and avoids rewriting whole pages for small edits.

The dry run includes a rough character estimate for the changed blocks that would be sent and returned:

```sh
npm run translate:weekly:dry-run
npm run translate:monthly:dry-run
```

To update only files changed in a specific commit or range:

```sh
npm run translate:docs -- de-DE --mode stale --paths-from-git bccdd22
npm run translate:docs -- de-DE --mode stale --paths-from-git main~3..main
```

To update only files changed since a ref:

```sh
npm run translate:docs -- de-DE --mode stale --since origin/main
```

If a block-level patch cannot be safely applied, the command stops instead of silently retranslating the whole page. Add `--allow-full-fallback` if you want those failures to fall back to full-file translation. The GitHub Actions translation workflow uses this fallback so one mismatched translated page does not stop the whole scheduled batch. To force a fresh full-file translation for every selected stale page, use `--stale-strategy full`. The previous page-level diff behaviour is still available with `--stale-strategy diff`.

The translator also updates `.translation-status.json`. This records pages that have been processed against the current English source even when the translated Markdown does not need any byte-level content change, so the strict freshness check can distinguish handled no-op translations from genuinely stale pages.

Update only stale German pages:

```sh
npm run translate:docs -- de-DE --language-name German --mode stale
```

Translate a single page:

```sh
npm run translate:docs -- de-DE --language-name German --path setting-up/laser-settings.md --force
```

Run the normal checks after translating:

```sh
npm run check:english-style
npm run check:spelling
npm run check:translations:strict
python3 scripts/check_markdown_link_spacing.py --fix
python3 scripts/check_link_texts.py --fix
npm run check:links
npm run build:site
npm run check:generated-images
```

`npm run localize:en-us` is still available for a one-off US English regeneration, but the weekly and monthly batch commands run it automatically.

## GitHub automation

The `Translation Updates` GitHub Actions workflow runs the same batches automatically:

* Weekly: every Monday at 03:00 UTC.
* Monthly: on the 1st of each month at 04:00 UTC.

The workflow opens or updates a pull request from `translation/weekly` or `translation/monthly` instead of committing AI translations directly to `main`.

To enable it, add `OPENAI_API_KEY` as a repository secret in GitHub. If you want to use Anthropic instead, add `ANTHROPIC_API_KEY` as a secret and set the repository variable `TRANSLATE_PROVIDER` to `anthropic`.

You can also run it manually from the Actions tab with optional inputs for the batch tier, `--force-cadence`, dry-run mode, a per-locale file limit, or a space-separated locale override.

Use this manual GitHub Actions test sequence when changing the workflow itself:

1. Run `weekly` with `dry_run: true`.
2. Run a single locale, for example `weekly` with `locale: de-DE` and `force_cadence: true`.
3. If that passes, run the intended full `weekly` or `monthly` batch.

Do not use `limit` for a real PR-creating test unless you also adjust the checks. A limited run intentionally leaves selected locales stale, so strict freshness checks can fail.

For translation PR review:

1. Wait for the `Translation Updates` run to finish.
2. Preview the PR locally from the PR branch:

   ```sh
   git fetch origin translation/weekly
   git worktree add /tmp/liberation-gitbook-pr origin/translation/weekly
   cd /tmp/liberation-gitbook-pr
   npm ci
   npm run build:site
   python3 -m http.server 4001 --directory _book
   ```

3. Open `http://localhost:4001/en-GB/` and spot-check the changed areas plus several translated locales.
4. Merge the PR if it looks good.
5. Watch the post-merge `Checks` and `HonKit Pages` workflows on `main`.

`npm run check:links` also checks Markdown link spacing plus source and translated internal link labels so stale English page titles and filename-style mention labels cannot be reintroduced silently.
It also checks translated `SUMMARY.md` files against the English sidebar so missing or changed status emoji prefixes cannot be reintroduced silently.

## Automated checks

The `Checks` workflow runs on normal pushes and human pull requests. It runs:

```sh
npm run check:english-style
npm run build:site
npm run check:generated-images
npm run check:links
npm run check:spelling
```

Coverage:

* Broken internal links: yes, via `scripts/check_links.py`.
* Markdown link spacing: yes, via `scripts/check_markdown_link_spacing.py`.
* Source link labels: yes, via `scripts/check_source_link_texts.py`.
* Translated link labels: yes, via `scripts/check_link_texts.py`.
* Summary status emoji prefixes: yes, via `scripts/check_summary_icons.py`.
* Generated image references and shared locale asset folders: yes, via `scripts/check_generated_images.py`.
* Spelling: partly, via `codespell` for `en-GB`, `en-US`, scripts, workflows, plugin/config files, and selected root docs.
* Grammar: no full grammar checker. `check:english-style` is a mechanical style/terminology checker for common source-English issues.

Translation PR branches are pushed by GitHub Actions. GitHub may not trigger the separate `Checks` workflow for those bot-created pushes, so the `Translation Updates` workflow runs the important translation checks itself before it opens or updates the PR:

```sh
npm run check:english-style
python3 scripts/check_translation_batch.py <tier> --strict
python3 scripts/check_markdown_link_spacing.py --fix
python3 scripts/check_link_texts.py --fix
npm run check:links
npm run build:site
npm run check:generated-images
```
