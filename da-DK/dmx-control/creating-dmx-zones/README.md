---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Oprettelse af DMX-zoner

1. Tilslut din Art-Net node, og sæt den op i [Opret forbindelse til en Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Åbn **DMX Zones**, og klik på **ADD DMX ZONE**.
3. Indstil zonens **Node**, **Universe** og **Address**, så de passer til armaturet.
4. Vælg en **Preset** til armaturet. Preset definerer, hvilke DMX-kanaler der modtager faste værdier, indhold til/fra-værdier, RGB-farve, X/Y-position, lysstyrke eller eksplicitte DMX Value-inputs.
5. Klik på **Edit DMX profile/channel mapping** (skyderikonet) for at redigere kanaltilknytningen. Standard-preset starter med en kanal til indhold til/fra og RGB-farvekanaler.
6. Tildel Clips til DMX zone på samme måde, som du tildeler dem til beam zone eller canvas zone.
7. Tryk på **ARM**, når du er klar til, at zonen sender DMX.

{% hint style="warning" %}
Kun DMX zones, der er aktiveret, sender live-værdier. DMX zones, der ikke er aktiveret, nulstiller deres tilknyttede kanaler, hvilket er mere sikkert, når du sætter armaturer op.
{% endhint %}

DMX-output er også begrænset af dit licensniveau. Hvis knappen **ARM** er deaktiveret, skal du kontrollere, om dit niveau inkluderer DMX-output, eller om det maksimale antal aktiverede DMX zones allerede er nået.
