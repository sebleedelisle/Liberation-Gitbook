# Liberation Manual

This repository builds and publishes the Liberation user manual.

Production is built with HonKit and deployed by GitHub Actions to GitHub Pages:

https://docs.liberationlaser.com/

`en-GB` is the source of truth. `en-US` is generated from `en-GB`. All other locale folders are AI-assisted translations that should be updated on the translation cadence, not every time English changes.

## Day-to-day workflow

For normal manual edits:

1. Edit only `en-GB`.
2. Run the UK/manual checks:

   ```sh
   npm run manual:uk:check
   ```

3. Commit and push to `main`.
4. GitHub Pages deploys the live docs from `main`.
5. Let the translation workflow open/update translation PRs on schedule.

Do not manually edit translated locale folders unless you are fixing a specific translation issue.

Terminology changes follow the same rule: do not run bulk replacements across translated locale folders. Update `en-GB`, regenerate `en-US` with `npm run localize:en-us`, and let scheduled translation PRs update AI-translated locales. Keep shared asset filenames stable during normal English edits unless all locale references are updated through the translation workflow.

## Local preview

Build and serve the current checkout:

```sh
npm ci
npm run build:site
npm run preview
```

Open:

```text
http://localhost:4000/en-GB/
```

To preview a translation PR without touching the main checkout, use a separate worktree and another port:

```sh
git fetch origin translation/weekly
git worktree add /tmp/liberation-gitbook-pr origin/translation/weekly
cd /tmp/liberation-gitbook-pr
npm ci
npm run build:site
python3 -m http.server 4001 --directory _book
```

Open:

```text
http://localhost:4001/en-GB/
```

GitHub Pages currently deploys production only. There is no separate GitHub Pages URL for each PR.

## Automated checks

The `Checks` workflow runs on pushes and human pull requests:

```sh
npm run check:english-style
npm run build:site
npm run check:generated-images
npm run check:links
npm run check:spelling
```

These cover:

- English mechanical style rules for `en-GB`.
- Full HonKit build and Pagefind search index generation.
- Generated local image references and locale asset folders.
- Broken internal Markdown links, Markdown link spacing, source/translated link labels, and summary status icons.
- Codespell spelling checks for `en-GB`, `en-US`, scripts, workflow files, and plugin/config files.

They do not provide a full grammar or prose-quality review. `check:english-style` is a mechanical style checker, not a grammar checker.

## Translation cadence

The `Translation Updates` workflow creates translation PRs instead of committing translations directly to `main`.

- Weekly: Monday at 03:00 UTC.
- Monthly: the 1st of each month at 04:00 UTC.
- Weekly updates `en-US` plus the priority locales in `translation-tiers.json`.
- Monthly updates every configured AI translation locale.

The workflow records successful runs in `.translation-cadence.json` so reruns are skipped unless forced.

Manual dry run:

```sh
npm run translate:weekly:dry-run
npm run translate:monthly:dry-run
```

Manual real run:

```sh
npm run translate:weekly
npm run translate:monthly
```

Manual GitHub Actions runs should normally be dry-run first. Only use `force_cadence` when you intentionally want an urgent rerun.

## Translation PR review

For translation PRs:

1. Wait for the translation workflow to finish.
2. Preview locally from the PR branch.
3. Spot-check changed English/US pages and a few translated pages.
4. Merge the PR if it looks good.
5. Confirm the post-merge `Checks` and `HonKit Pages` workflows pass.

After merge, GitHub Pages publishes the live docs at `docs.liberationlaser.com`.

## Secrets and permissions

The translation workflow needs:

- Repository secret `OPENAI_API_KEY`.
- Repository Actions permission allowing GitHub Actions to create pull requests.

Optional:

- Repository secret `ANTHROPIC_API_KEY`.
- Repository variable `TRANSLATE_PROVIDER=anthropic`.

The default OpenAI translation model is `gpt-5.5`.

## Reference docs

- [TRANSLATIONS.md](TRANSLATIONS.md): detailed translation system, prompts, cadence, and troubleshooting.
- [STYLE_GUIDE.md](STYLE_GUIDE.md): source English style rules.
- [LANGS.md](LANGS.md): published language list.
- [translation-tiers.json](translation-tiers.json): weekly/monthly locale tiers.
