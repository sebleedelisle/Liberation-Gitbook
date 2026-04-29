---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas-målområder

Vi vet hvordan vi får deler av Canvas inn i soner i hver laser, men for å få innhold inn i Canvas i utgangspunktet trenger du de forvirrende, men presist navngitte, _Canvas-målområdene_.

_Canvas-målområder_ er deler av Canvas som du kan tegne Clip-er inn i, og de vises i _CANVAS_-visningen som blå rektangler med kontur.

Ofte trenger du kanskje bare ett Canvas-målområde, og deretter kan du dele det opp i flere soner som sendes til ulike lasere.

Noen ganger vil du kanskje ha flere Canvas-målområder for ulike deler av en bygning, eller for å utnytte soneforsinkelsen mellom dem. (Ja! Soneforsinkelse fungerer fortsatt på tvers av Canvas-målområder!).

### Sende Clip-er til Canvas-målområder

Hvis du ser i Clip Deck, ved siden av knappene for strålesoner, ser du knappene for Canvas-målområder. Det kan hende du må bla gjennom Output-knappene for å se dem. Bruk `Shift + Left / Right Arrow`, eller ZONE PAGE-knappene på skjermen, eller APC40-knappene (se [APC40-referanse](../reference/apc40-reference.md "mention"))

Tildel Clip-er til Canvas-målområder ved å slå disse knappene av og på på nøyaktig samme måte som du gjør med knappene for strålesoner.

### Legge til / redigere Canvas-målområder

Velg _View -> Canvas Target Areas_ i den øverste menylinjen – da ser du alle innstillingene for hvert Canvas-målområde du har i prosjektet.

Øverst finner du knappen _ADD CANVAS TARGET AREA_.

Slett et Canvas-målområde med den røde knappen med minustegn.

Juster størrelse og posisjon med glidebryterne. Dobbeltklikk på en glidebryter for å skrive inn en verdi.

### Skaleringsmodus

* **FIT TO AREA** – skalerer innhold ned slik at det passer helt innenfor Canvas-målområdet, samtidig som størrelsesforholdet bevares. (Dette er standardinnstillingen)
* **FILL AREA** – strekker innhold slik at det fyller Canvas-målområdet, samtidig som størrelsesforholdet bevares. Innhold kan bli kuttet i kantene.
* **STRETCH TO FIT** – strekker innhold slik at det fyller hele Canvas-målområdet, uten å ta hensyn til størrelsesforholdet.
