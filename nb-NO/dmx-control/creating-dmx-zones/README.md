---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Opprette DMX-soner

1. Koble til Art-Net-noden din og sett den opp i [Koble til en Art-Net-node](../connecting-to-an-artnet-node.md "mention").
2. Åpne **DMX Zones** og klikk på **ADD DMX ZONE**.
3. Sett **Node**, **Universe** og **Address** for zone slik at de samsvarer med fixturen.
4. Velg en **Preset** for fixturen. Preset bestemmer hvilke DMX-kanaler som mottar faste verdier, content av/på-verdier, RGB-farge, X/Y-posisjon, lysstyrke eller eksplisitte DMX Value-innganger.
5. Klikk på **Edit DMX profile/channel mapping** (skyvebryterikonet) for å redigere kanaltilordningen. Standard preset starter med en content av/på-kanal og RGB-fargekanaler.
6. Tilordne Clips til DMX zone på samme måte som du tilordner dem til beam zones eller canvas zones.
7. Trykk på **ARM** når du er klar til at zone skal sende ut DMX.

{% hint style="warning" %}
Bare aktiverte DMX zones sender live-verdier. DMX zones som ikke er aktivert, nullstiller de tilordnede kanalene sine, noe som er tryggere når du setter opp fixturer.
{% endhint %}

DMX-utgang er også begrenset av lisensnivået ditt. Hvis **ARM**-knappen er deaktivert, bør du kontrollere om nivået ditt inkluderer DMX-utgang, eller om maksimalt antall aktiverte DMX zones allerede er nådd.
