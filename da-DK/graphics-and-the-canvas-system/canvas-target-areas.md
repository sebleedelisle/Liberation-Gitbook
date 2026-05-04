---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas target areas

Vi ved nu, hvordan du får dele af canvas ind i zoner i hver laser, men for overhovedet at få indhold ind i canvas skal du bruge de lidt forvirrende, men præcist navngivne _Canvas target areas_.

_Canvas target areas_ er sektioner af canvas, som du kan tegne clips ind i, og de vises i _CANVAS_-visningen som rektangler med blå kontur.

Ofte har du måske kun brug for én canvas target area, som du derefter opdeler i flere zoner, der sendes til forskellige lasere.

Andre gange vil du måske bruge flere canvas target areas til forskellige dele af en bygning eller for at udnytte zone delay mellem dem. (Ja! Zone delay virker stadig på tværs af canvas target areas!).

### Sådan sender du clips til canvas target areas

Hvis du kigger i Clip Deck, ved siden af knapperne til beam zone, kan du se knapperne til canvas target areas. Du skal muligvis rulle output-knapperne for at se dem. Brug `Shift + Left / Right Arrow`, ZONE PAGE-knapperne på skærmen eller APC40-knapperne (se [APC40-reference](../reference/apc40-reference.md "mention"))

Tildel clips til canvas target areas ved at slå disse knapper til eller fra på præcis samme måde som med beam zone-knapperne.

### Tilføjelse / redigering af canvas target areas

Vælg _View -> Canvas Target Areas_ i den øverste menulinje. Her ser du alle indstillingerne for hver canvas target area i dit projekt.

Øverst finder du knappen _ADD CANVAS TARGET AREA_.

Slet en canvas target area med den røde knap med minustegnet.

Juster størrelse og position med skyderne. Dobbeltklik på en skyder for at indtaste en værdi.

### Scale mode

* **FIT TO AREA** - formindsker indholdet, så det passer helt ind i canvas target area, samtidig med at billedformatet bevares. (Dette er standardindstillingen)
* **FILL AREA** - strækker indholdet, så det fylder canvas target area, samtidig med at billedformatet bevares. Indhold kan blive skåret af ved kanterne.
* **STRETCH TO FIT** - strækker indholdet, så det fylder hele canvas target area, uden at tage hensyn til billedformatet.
