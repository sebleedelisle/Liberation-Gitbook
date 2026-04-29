---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introductie

Liberation bevat een flexibel en krachtig DMX-systeem waarmee je lichteffecten kunt maken en DMX-compatibele lasers via Art-Net kunt aansturen. Het is ontworpen om je verlichting eenvoudig synchroon te houden met je lasershow, zonder dat je een aparte lichttafel nodig hebt.

{% hint style="info" %}
**Wat is Art-Net, en hoe verhoudt het zich tot DMX?**

**DMX** is een systeem dat al jaren wordt gebruikt om lampen, lasers, rookmachines en andere podiumeffecten aan te sturen. Het verstuurt stuursignalen via speciale kabels, meestal met XLR-connectoren. Elk armatuur luistert naar een specifieke set kanalen om te weten wat het moet doen.

**Art-Net** is een nieuwere manier om dezelfde DMX-data via een normaal computernetwerk te versturen. In plaats van speciale kabels te gebruiken, loopt alles via Ethernet, net zoals internet- of lokaal netwerkverkeer.

In Liberation wordt alle DMX-output via Art-Net verstuurd. Je kunt hiermee Art-Net-compatibele apparaten rechtstreeks aansturen, of je kunt een **Art-Net-node** aansluiten: een klein kastje dat Art-Net weer omzet naar standaard DMX. Zo kun je traditionele DMX-lampen en effecten blijven aansturen, ook als ze zelf geen Art-Net ondersteunen.
{% endhint %}

Je kunt het ook gebruiken om allerlei andere podiumapparatuur aan te sturen, zoals rookmachines, hazers, CO₂-jets, cold spark-machines en meer. Als het DMX ondersteunt, kun je het instellen als DMX zone en rechtstreeks vanuit Liberation triggeren, naast je lasercontent.

DMX-armaturen worden toegevoegd als **DMX zones**. Deze verschijnen in de zonelijst naast je laser beam zones en canvas target areas. Elke DMX zone gebruikt een **DMX preset**, die Liberation vertelt hoe eigenschappen van je laserclips, zoals positie, kleur en helderheid, naar DMX-kanaalwaarden worden vertaald.

Wanneer je een clip naar een DMX zone stuurt, kijkt Liberation naar het eerste element in de clip en zet het de eigenschappen daarvan om op basis van de preset. Zo kun je lampen en DMX-effecten eenvoudig rechtstreeks aansturen vanuit dezelfde clips die je al voor lasers gebruikt.

#### Liberation op Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

De eerste echte test van het DMX-systeem van Liberation was op Glastonbury 2023, waar Reach Lasers in totaal 90 beambronnen installeerde als onderdeel van de Arcadia "spider"-stage.

18 lasers werden aangestuurd met interne Ether Dreams, en nog eens 12 beam bars met 6 koppen werden aangestuurd via Art-Net en DMX.
