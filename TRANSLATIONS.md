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

Use `--model` to override the default model.

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
