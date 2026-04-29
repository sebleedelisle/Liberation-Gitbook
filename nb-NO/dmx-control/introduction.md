---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introduksjon

Liberation har et fleksibelt og kraftig DMX-system som lar deg lage lyseffekter og styre DMX-kompatible lasere via Art-Net. Det er laget for å gjøre det enkelt å holde lysriggen synkronisert med lasershowet ditt – uten behov for en separat lysmikser.

{% hint style="info" %}
**Hva er Art-Net, og hvordan henger det sammen med DMX?**

**DMX** er et system som i mange år har vært brukt til å styre lys, lasere, røykmaskiner og andre sceneeffekter. Det sender styresignaler over spesialkabler, vanligvis med XLR-kontakter, og hver fixture lytter til et bestemt sett med kanaler for å vite hva den skal gjøre.

**Art-Net** er en nyere måte å sende de samme DMX-dataene over et vanlig datanettverk. I stedet for å bruke spesialkabler sendes alt over Ethernet, akkurat som internett- eller lokalnettverkstrafikk.

I Liberation sendes all DMX-output med Art-Net. Du kan bruke det til å styre Art-Net-kompatible enheter direkte, eller du kan koble til en **Art-Net-node** – en liten boks som konverterer Art-Net tilbake til standard DMX. Det betyr at du fortsatt kan styre tradisjonelle DMX-lys og effekter, selv om de ikke støtter Art-Net selv.
{% endhint %}

Du kan også bruke det til å styre mange typer sceneutstyr, som røykmaskiner, hazere, CO₂-kanoner, cold spark-maskiner og mer. Hvis utstyret støtter DMX, kan du sette det opp som en DMX-zone og trigge det direkte fra Liberation, side om side med laserinnholdet ditt.

DMX-fixtures legges til som **DMX zones**, som vises i zonelisten sammen med laser beam zones og canvas target areas. Hver DMX-zone bruker en **DMX preset**, som forteller Liberation hvordan egenskaper fra laserklippene dine – som posisjon, farge og lysstyrke – skal mappes til DMX-kanalverdier.

Når du sender et klipp til en DMX-zone, ser Liberation på det første elementet i klippet og konverterer egenskapene basert på presettet. Dette gjør det enkelt å styre lys og DMX-effekter direkte fra de samme klippene du allerede bruker til lasere.

#### Liberation på Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Den første virkelige testen av Liberation DMX-systemet var på Glastonbury 2023, der Reach Lasers installerte totalt 90 beam-kilder som en del av Arcadia "spider"-scenen.

18 lasere ble styrt med interne Ether Dreams, og ytterligere 12 6-head beam bars ble styrt via Art-Net og DMX.
