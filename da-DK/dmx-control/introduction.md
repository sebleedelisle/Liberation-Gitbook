---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introduktion

Liberation indeholder et fleksibelt og kraftfuldt DMX-system, der lader dig oprette lyseffekter og styre DMX-kompatible lasere via Art-Net. Det er designet til at gøre det nemt at holde lyset synkroniseret med dit lasershow – uden behov for en separat lyspult.

{% hint style="info" %}
**Hvad er Art-Net, og hvordan hænger det sammen med DMX?**

**DMX** er et system, der i mange år er blevet brugt til at styre lamper, lasere, røgmaskiner og andre sceneeffekter. Det sender styresignaler via særlige kabler, normalt med XLR-stik, og hver fixture lytter til et bestemt sæt kanaler for at vide, hvad den skal gøre.

**Art-Net** er en nyere måde at sende de samme DMX-data over et almindeligt computernetværk. I stedet for at bruge særlige kabler sender det alt via Ethernet, ligesom internet- eller lokal netværkstrafik.

I Liberation sendes alt DMX-output med Art-Net. Du kan bruge det til at styre Art-Net-kompatible enheder direkte, eller du kan tilslutte en **Art-Net-node** – en lille boks, der konverterer Art-Net tilbage til standard-DMX. Det betyder, at du stadig kan styre traditionelle DMX-lamper og effekter, selvom de ikke selv understøtter Art-Net.
{% endhint %}

Du kan også bruge det til at styre mange forskellige typer sceneudstyr, f.eks. røgmaskiner, hazere, CO₂-jets, cold spark-maskiner og mere. Hvis udstyret understøtter DMX, kan du sætte det op som en DMX-zone og trigge det direkte fra Liberation side om side med dit laserindhold.

DMX-fixtures tilføjes som **DMX zones**, som vises i zonelisten sammen med dine laser beam zones og canvas target areas. Hver DMX-zone bruger en **DMX preset**, som fortæller Liberation, hvordan egenskaber fra dine laserclips – f.eks. position, farve og lysstyrke – skal mappes til DMX-kanalværdier.

Når du sender en clip til en DMX-zone, kigger Liberation på det første element i clippet og konverterer dets egenskaber ud fra presettet. Det gør det enkelt at styre lamper og DMX-effekter direkte fra de samme clips, som du allerede bruger til lasere.

#### Liberation på Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Den første reelle test af Liberation DMX-systemet var på Glastonbury 2023, hvor Reach Lasers installerede i alt 90 beam-kilder som en del af Arcadia "spider"-scenen.

18 lasere blev styret med interne Ether Dreams, og yderligere 12 6-head beam bars blev styret via Art-Net og DMX.
