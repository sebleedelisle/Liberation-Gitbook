---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Live MIDI Controllers

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40-controller**

Dette er standard-hardwarecontrolleren til Liberation. Den anbefales varmt, og man kan roligt sige, at Liberation helt fra begyndelsen er designet omkring denne hardware. Så snart du tilslutter APC40, opretter Liberation automatisk forbindelse til den med det samme.

{% hint style="warning" %}
_Åh nej! Mit USB-stik blev trukket ud midt under et show!_

Gå ikke i panik – sæt det bare i igen. Liberation opretter automatisk forbindelse igen uden problemer.
{% endhint %}

### APC40 Mark 1 eller Mark 2?

Kort sagt anbefales Mark 2, fordi den har knapper i fuld farve, som matcher Liberation Clip Deck-brugerfladen bedre. Mark 1-versionen kan bruges, hvis det er nødvendigt, men den vil være lidt mere forvirrende, fordi layoutet afviger en smule fra det, du ser på skærmen, og knapperne kun kan lyse rødt, orange eller grønt, så de matcher ikke klippenes farver.

{% hint style="info" %}
Den originale APC40 Mark 1 udkom i 2009(!), og nogle foretrækker den stadig på grund af dens metalkabinet og robuste, konsolagtige formfaktor. Den opdaterede Mark 2 udkom i 2014, og selvom den blev udgået i 2024, sættes den i produktion igen i 2025 på grund af efterspørgsel fra visual artists (Resolume osv.) og laserfolk.
{% endhint %}

Se den fulde liste over kontroller, der er tilgængelige på APC40, her: [APC40-reference](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 indeholder også en APC Mini-profil. Den mapper 8x5 Clip-gitteret, zone-knapper, kontroller til X/Y-spejlvending af zone, gruppeknapper, stop af alle Clips, flytning mellem Clip-sider, flytning mellem zone-sider, tap tempo, takt-nulstilling og tempo nudge. Dens fadere styrer effektniveauer, og fadere med Shift styrer effektparametre. Den sidste fader styrer global lysstyrke.

### MIDI Fighter Twister

MIDI Fighter Twister-profilen er beregnet til encoder-baseret styring frem for start af Clips. Én række encodere styrer parameter 1 for effektplads 1-8, og en anden række følger de otte kontekstafhængige kontroller i Parameters-panelet, herunder Clip shift, zone delay, global spin/scale og gruppefades.
