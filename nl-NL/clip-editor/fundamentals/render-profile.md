---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Elke _Creator_-node heeft een instelling _Render Profile_. Hiermee bepaal je hoe de vormen met de lasers worden getekend (of _gerenderd_).

**Voor de meeste toepassingen is de instelling&#x20;**_**DEFAULT**_**&#x20;helemaal prima**. Maar als je met graphics of complexe content werkt, wil je misschien meer controle over hoe elke vorm wordt gerenderd.

{% hint style="info" %}
Anders dan de meeste lasersoftware genereert Liberation in realtime een puntenstroom, vlak voordat die naar de lasercontrollers wordt gestuurd. Dit bespaart je veel schijfruimte: clips zijn maar een paar kB, in plaats van MB's aan vooraf gerenderde puntenstromen.

Dit betekent ook dat je dezelfde content per laser kunt afstemmen op verschillende scannertypen, zonder de clips zelf te hoeven aanpassen.

Zie voor meer informatie [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Er zijn drie vooraf ingestelde _Render Profiles_: _DEFAULT_, _FAST_ en _DETAIL._

_**DEFAULT**_ - een goed algemeen profiel, geschikt voor de meeste situaties

_**FAST** -_ als je clip veel content bevat en een deel daarvan uit heel eenvoudige punten en rechte lijnen bestaat, kun je met deze optie mogelijk minder flikkering krijgen.

_**DETAIL**_ - gebruik deze optie als je iets tekent dat scherpe hoeken nodig heeft. Houd er wel rekening mee dat je scanners langzamer bewegen, waardoor de output flikkeriger wordt.

{% hint style="info" %}
In de clip editor kun je creators aan verschillende render profiles toewijzen, maar elke laser verwerkt deze profielen afhankelijk van de scanner settings. Zie [scanner-presets.md](../../advanced/scanner-presets.md "mention")
{% endhint %}
