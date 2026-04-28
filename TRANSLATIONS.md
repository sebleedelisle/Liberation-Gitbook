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
* Finnish, Hungarian, and Polish: natural direct technical-manual prose.
* Japanese and Korean: concise polite technical-manual prose.
* Traditional Chinese (Hong Kong): Traditional Chinese characters with natural Hong Kong technical-manual wording; avoid Simplified Chinese characters and Mainland-only terminology.

Exact on-screen UI labels should stay in English when the text refers to labels, buttons, menu items, panels, or settings.

Visible Markdown link text should be translated when it is natural-language text. For links to other pages or sections in the manual, the visible text should match the translated title or heading for that destination, while the link target itself must stay exactly the same.

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
