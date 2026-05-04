# Liberation Manual Style Guide

`en-GB` is the source text for the manual. Keep it in British English, but use modern technical-documentation conventions where they are clearer than traditional variants.

## British English

Use British spelling for normal prose:

| Use | Avoid | Notes |
| --- | --- | --- |
| `colour`, `coloured` | `color`, `colored` | US English is generated separately in `en-US`. |
| `centre`, `centred` | `center`, `centered` | Use `center` only if it is an exact UI label or code term. |
| `visualise`, `visualiser` | `visualize`, `visualizer` | Match the app wording where the UI uses `Visualiser`. |
| `authorise`, `deauthorise` | `authorize`, `deauthorize` | Use `authorisation` and `deauthorisation` in prose. Match the app wording where the UI uses `Visualiser`. |
| `optimise`, `customise` | `optimize`, `customize` | Keep `-ise` style in source English. |
| `licence` | `license` as a noun | `licence tier`, `licence period`, `your licence`. |
| `license`, `licensing` | `licence` as a verb | UK English uses `license` for the verb: `license the software`, `licensing system`. |

Do not rename existing files or URLs just to change spelling. Some slugs still contain historical spellings such as `license`, `colour`, or `co-ordinate`; link targets and asset paths must remain stable.

## Technical Terms

Use these visible spellings in the manual:

| Use | Avoid | Notes |
| --- | --- | --- |
| `setup` | `set-up` | Noun/adjective: `laser setup`, `hardware setup`, `setup guide`. |
| `set up` | `setup` as a verb | Verb: `set up your lasers`, `set up a network`. |
| `preset` | `pre-set` | One word in software docs. |
| `checkbox`, `checkboxes` | `check box`, `check boxes` | One word for UI controls. |
| `right-click`, `right-clicking` | `right click`, `right clicking` | Hyphenate click actions. |
| `double-click`, `double-clicking` | `double click`, `double clicking` | Hyphenate click actions. |
| `click and drag` | `click/drag`, `click / drag` | Spell it out in instructions. |
| `click and drag` | `click-drag` | Avoid compressed interaction shorthand in prose. |
| `drop-down` | `drop down`, `dropdown` | Noun/adjective: `drop-down menu`. |
| `pop-up` | `popup`, `pop up` as a noun/adjective | Keep `pop up` only as a verb. |
| `on-screen` | `on screen` before a noun | `on-screen slider`, but `shown on screen`. |
| `64-bit`, `32-bit` | `64 bit`, `32 bit` | Hyphenate bit-depth adjectives. |
| `high-spec` | `high spec` | Hyphenate before a noun. |
| `anti-clockwise` | `counter-clockwise`, `counterclockwise` | UK source uses `anti-clockwise`; US generation converts this. |
| `coordinate` | `co-ordinate` | Use the unhyphenated technical spelling in visible text. Existing paths may still use `co-ordinate`. |
| `MIDI`, `DMX`, `OSC`, `ILDA`, `DAC` | `midi`, `Midi` | Acronyms stay uppercase. |
| `Art-Net` | `ArtNet`, `Artnet`, `Art net` | Protocol name. |
| `APC40` | `APC 40` | Product shorthand. |
| `LaserCube` | `Laser Cube` | Product name. |
| `sync` | `synch` | Use the shorter technical spelling. |
| `i.e.` | `ie` | Prefer rewriting if it reads more naturally. |

Use `Clip`, `Clip Deck`, `Clip Editor`, `zone`, `mask`, `Output view`, `Laser Settings`, `APC40`, `LaserCube`, `Art-Net`, `ILDA`, `DMX`, `MIDI`, and similar product/UI terms consistently with the app. Exact UI labels may keep the app's spelling and capitalisation.

## UI Controls

Use action-first wording for icon-only buttons. Name the action first, then add the icon as a locator in parentheses:

| Use | Avoid |
| --- | --- |
| `Click **Edit DMX zone settings** (pencil icon).` | `Click the **Pencil** button.` |
| `Click **Edit DMX profile/channel mapping** (sliders icon).` | `Click **Sliders**.` |

This keeps instructions meaningful for screen readers, translations, and users who do not recognise the icon. Use the icon name by itself only when the app's visible UI label is actually the icon name.

## Checks

Run the style check before translating:

```sh
npm run check:english-style
```

For mechanical fixes:

```sh
npm run fix:english-style
```

The fixer only changes visible Markdown prose. It preserves Markdown link targets, image paths, raw URLs, inline code, fenced code, and frontmatter.
