---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introduktion

Liberation innehåller ett flexibelt och kraftfullt DMX-system som låter dig skapa ljuseffekter och styra DMX-kompatibla lasrar via Art-Net. Det är utformat för att göra det enkelt att hålla ljuset synkat med din lasershow – utan att du behöver ett separat ljusbord.

{% hint style="info" %}
**Vad är Art-Net, och hur hänger det ihop med DMX?**

**DMX** är ett system som i många år har använts för att styra lampor, lasrar, rökmaskiner och andra sceneffekter. Det skickar styrsignaler via särskilda kablar (oftast med XLR-kontakter), och varje armatur lyssnar på en specifik uppsättning kanaler för att veta vad den ska göra.

**Art-Net** är ett nyare sätt att skicka samma DMX-data via ett vanligt datornätverk. I stället för att använda särskilda kablar skickas allt via Ethernet, precis som internet- eller lokal nätverkstrafik.

I Liberation skickas all DMX-output med Art-Net. Du kan använda det för att styra Art-Net-kompatibla enheter direkt, eller ansluta en **Art-Net node** – en liten box som omvandlar Art-Net tillbaka till vanlig DMX. Det betyder att du fortfarande kan styra traditionella DMX-lampor och effekter, även om de inte själva har stöd för Art-Net.
{% endhint %}

Du kan också använda det för att styra många olika typer av scenutrustning, som rökmaskiner, hazers, CO₂-jets, cold spark-maskiner med mera. Om utrustningen har stöd för DMX kan du konfigurera den som en DMX-zon och trigga den direkt från Liberation, sida vid sida med ditt laserinnehåll.

DMX-armaturer läggs till som **DMX-zoner**, som visas i zonlistan tillsammans med dina laserstrålezoner och canvas-målområden. Varje DMX-zon använder en **DMX preset**, som talar om för Liberation hur egenskaper från dina laserklipp – som position, färg och ljusstyrka – ska mappas till DMX-kanalvärden.

När du skickar ett klipp till en DMX-zon tittar Liberation på det första elementet i klippet och omvandlar dess egenskaper baserat på preseten. Det gör det enkelt att styra lampor och DMX-effekter direkt från samma klipp som du redan använder för lasrar.

#### Liberation på Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Det första riktiga testet av Liberations DMX-system var på Glastonbury 2023, där Reach Lasers installerade totalt 90 strålkällor som en del av Arcadia-scenen ”spider”.

18 lasrar styrdes med interna Ether Dreams, och ytterligare 12 beam bars med 6 huvuden styrdes via Art-Net och DMX.
