---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ DMX-zones maken

1. Sluit je Art-Net-node aan en stel deze in via [Verbinding maken met een Art-Net-node](../connecting-to-an-artnet-node.md "mention").
2. Open **DMX Zones** en klik op **ADD DMX ZONE**.
3. Stel **Node**, **Universe** en **Address** van de zone zo in dat ze overeenkomen met het fixture.
4. Kies een **Preset** voor het fixture. De preset bepaalt welke DMX-kanalen vaste waarden, waarden voor content aan/uit, RGB-kleur, X/Y-positie, helderheid of expliciete DMX Value-invoer ontvangen.
5. Klik op **Edit DMX profile/channel mapping** (schuifregelaarpictogram) om de kanaaltoewijzing te bewerken. De standaardpreset begint met een kanaal voor content aan/uit en RGB-kleurkanalen.
6. Wijs Clips toe aan de DMX zone op dezelfde manier als je ze aan beam zone of canvas zone toewijst.
7. Druk op **ARM** wanneer je klaar bent om de zone DMX te laten uitsturen.

{% hint style="warning" %}
Alleen zones van het type DMX die voor output zijn geactiveerd, sturen livewaarden. Zones van het type DMX die niet zijn geactiveerd, zetten hun toegewezen kanalen terug naar nul. Dat is veiliger tijdens het instellen van fixtures.
{% endhint %}

DMX-output wordt ook beperkt door je licentieniveau. Als de knop **ARM** is uitgeschakeld, controleer dan of je niveau DMX-output omvat of dat het maximale aantal geactiveerde DMX zones al is bereikt.
