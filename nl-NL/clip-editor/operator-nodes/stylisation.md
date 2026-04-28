---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stiliseringsnodes

## &#x20;Randomise

Maakt verspreide kopieën van de inkomende elementen met behulp van een coherent noise field. Met andere woorden: deze node kopieert je vormen en punten en verplaatst ze op een gecontroleerde, “ruisachtige” manier. In plaats van dat alles netjes op één plek blijft, krijg je meerdere versies die verschuiven en uitwaaieren, zoals deeltjes die in een stroming bewegen.

* **count** – aantal kopieën per inkomend element (1–20). Bij 1 krijg je één licht verschoven versie van elk element. Hogere waarden maken meerdere verspreide kopieën.
* **noise offset** – loopt door het noise field (0–100%). Dit loopt naadloos door, dus als je dit animeert met een Oscillator Node krijg je een vloeiende, continue beweging van alle kopieën samen.
* **noise jitter** – bepaalt de textuurschaal van de ruis. Lagere waarden geven brede, vloeiende variatie. Hogere waarden geven compactere, grilligere plaatsing. Dit verandert het patroon, niet de sterkte.
* **change between points** – bepaalt hoe sterk elke kopie verschilt van de vorige. Lage waarden houden kopieën dicht bij elkaar en vergelijkbaar. Hoge waarden verspreiden ze verder met meer variatie.
* **face direction** – roteert elke kopie zodat deze in de bewegingsrichting van het noise field wijst, waardoor pijlen/deeltjes ontstaan die met de flow meelopen.
* **amount** – algemene sterkte van het effect (0–100%). Schaalt zowel de verplaatsing als de rotatie van Face direction.

{% hint style="info" %}
De Randomise-node vormt de kern van het Randomise-effect!
{% endhint %}

## &#x20;Trails

Maakt echo’s van je content, waarbij vervagende of schalende kopieën achter het origineel blijven terwijl het beweegt.

* **change render profile for trail** – indien ingeschakeld gebruiken alle trail-kopieën het geselecteerde **render profile**. _Zie_ [render-profile.md](../fundamentals/render-profile.md "mention").
* **render profile** – het profiel dat wordt gebruikt voor trail-kopieën wanneer de schakelaar hierboven aan staat. Dit wordt vaak gebruikt wanneer de hoofdcontent op **DETAIL** staat, maar de echo’s als **FAST** worden gerenderd. Zo behoud je duidelijke details in de hoofdvormen terwijl de trails efficiënter worden gerenderd.
* **delay** – bepaalt de afstand tussen trail-kopieën in muzikale tijd, gemeten in **1/64-nootstappen**.\
  Ter referentie:
  * 16 = 1/16 maat (zestiende noot)
  * 32 = 1/8 maat (achtste noot)
  * 64 = 1/4 maat (kwartnoot)
  * 128 = 1/2 maat (halve noot)
  * 256 = 1 maat
* **trail size** – hoeveel trail-kopieën achter de live content worden getekend.
* **freeze trails** – verandert vloeiend doorlopende trails in een reeks bevroren snapshots. Handig voor staccato, beat-gesynchroniseerde trail-effecten.
* **brightness start / brightness end** – past de helderheid over de trail toe, van de nieuwste kopie (**start**) tot de oudste kopie (**end**). Meestal stel je **brightness start** in op 100% en **brightness end** op 0%, zodat de echo’s uitfaden.
* **scale start / scale end** – past schaalverandering over de trail toe, van de nieuwste kopie (start) tot de oudste kopie (end). Voor trails die tot niets krimpen stel je **scale start** in op 100% en **scale end** op 0%.

## &#x20;Shimmer

Voegt een fonkelende helderheidsvariatie toe aan je content, van subtiele sparkle tot intens strobing.

* **speed** – hoe snel de shimmer in de tijd verandert. Hogere waarden flikkeren sneller; 0 pauzeert het effect.
* **separation** – hoe sterk aangrenzende punten/elementen van elkaar verschillen.
  * 0: alles shimmert samen.
  * \>0: nabije punten krijgen geleidelijk andere fases, zodat de shimmer over de vorm varieert.
  * <0: hetzelfde als hierboven, maar de fase-opbouw loopt de andere kant op.
* **threshold** – in plaats van vloeiend te vervagen, flitsen punten nu volledig aan of uit op basis van hun helderheid. Helderdere elementen lichten vaker op, maar let op: elementen met 100% helderheid staan altijd aan, terwijl elementen met 0% helderheid altijd uit staan. Handig voor scherpe glitter- of sterrenlichteffecten.

{% hint style="info" %}
**threshold** inschakelen is zo’n sterke verborgen functie die je particles of content echt tot leven kan brengen. In plaats van te vervagen, worden punten snel aan en uit geschakeld op basis van hun helderheid. Omdat er op elk moment minder punten worden getekend, levert dit een helderdere output en vloeiendere animatie op.

Houd er wel rekening mee dat dit niets doet als je content al op 100% helderheid staat!
{% endhint %}

* **use whole shape** – past één shimmer-waarde gelijkmatig toe op de hele vorm. Wanneer dit uit staat, verdeelt de node vormen in kleinere delen zodat verschillende onderdelen onafhankelijk kunnen fonkelen voor een gespikkelde look.

## &#x20;Particles

Dit is een experimenteel effect dat particles maakt en animeert op basis van je content. Alle puntgebaseerde elementen die binnenkomen, worden behandeld als emitterposities. Omdat particle-paden vooraf worden berekend, moet je de particles mogelijk verversen/herberekenen als je invoercontent verandert (verander gewoon een van de instellingen).

**General**

* **keep original** – indien ingeschakeld blijft de originele content behouden en worden particles erbovenop toegevoegd. Handig wanneer je de emitterpunten zichtbaar wilt houden.
* **number of particles** – hoeveel particles per emissie worden gemaakt. Hogere waarden geven dichtere effecten, lagere waarden zijn minimalistischer.
* **emission period** – de lengte van de loop (in maten) waarover particles worden uitgestoten. Bij 100% worden ze gelijkmatig over de loop verdeeld; kleinere waarden bundelen ze voor bursts.
* **loop length** – hoe lang de particle-loop duurt, gemeten in muzikale maten.
* **loop count** – hoe vaak de loop wordt herhaald voordat deze reset. Als dit op 1 staat, volgen de particles elke keer exact dezelfde simulatie, waardoor het perfect herhaalbaar is. Hogere waarden zorgen voor meer variatie voordat de cyclus reset.
* **delay** – verschuift de starttijd van de emissie met een aantal 1/64-noten, voor timing-effecten.

**Motion**

* **speed** – hoe snel de particles van de emitter af bewegen.
* **speed variation** – voegt willekeur toe zodat particles niet allemaal met dezelfde snelheid bewegen. Dit geeft een natuurlijkere spreiding.
* **direction** – bepaalt de basisrichting waarin particles worden afgevuurd, gedefinieerd door **x, y, z angles**. Deze hoeken roteren de afvuurrichting in 3D-ruimte, zodat je particles recht omhoog, zijwaarts of in elke diagonale richting kunt richten. Combineer dit met **spread** voor bredere kegels of chaotischere bursts.

{% hint style="info" %}
**Euler angles**\
Liberation gebruikt **Euler angles** om oriëntatie in 3D-ruimte te beschrijven. Dit zijn simpelweg rotaties rond de drie hoofdassen:

* **X** – voorover/achterover kantelen (alsof je met je hoofd knikt)
* **Y** – links/rechts draaien (alsof je “nee” schudt)
* **Z** – met de klok mee/tegen de klok in rollen (alsof je je hoofd zijwaarts kantelt)

Door deze drie waarden aan te passen, kun je particles in elke richting richten.
{% endhint %}

* **direction variation** – voegt willekeurige spreiding rond die richting toe. Handig voor kegels, sprays of explosies.
* **drag** – vertraagt particles na verloop van tijd. Hogere waarden laten ze zwaarder en trager aanvoelen.
* **gravity** – trekt particles omlaag (positief) of duwt ze omhoog (negatief).
* **gravity variation** – voegt per particle variatie toe aan gravity, waardoor de beweging chaotischer wordt.

**Life**

* **life duration** – hoe lang particles bestaan (gemeten in 1/64-nooteenheden). Bij kortere waarden verdwijnen particles snel, terwijl ze bij langere waarden langer zichtbaar blijven.
* **life variation** – voegt willekeur toe aan de levensduur van particles zodat ze niet allemaal tegelijk verdwijnen.
* **start delay / start delay variation** – vertraagt wanneer elke particle zichtbaar wordt (in 1/64-nootstappen). De particle is tijdens deze periode al gemaakt en in beweging, maar de helderheid blijft op 0, zodat hij onzichtbaar blijft tot de vertraging voorbij is. Dit is handig als je vertraagde vuurwerk-“sparkles” wilt laten verschijnen.

**Colour & brightness**

* **hue start** – beginkleur van particles.
* **hue variation** – voegt willekeur toe zodat particles niet allemaal met dezelfde kleur beginnen.
* **hue change** – verschuift de hue gedurende de levensduur van de particle, waardoor kleurveranderende trails ontstaan.
* **brightness start / brightness end** – past helderheid toe over de levensduur van de particle. Meestal stel je brightness start hoog in en brightness end laag, zodat ze natuurlijk uitfaden.
* **brightness variation** – randomiseert de beginhelderheid voor een dynamischere look.
* **saturation start / saturation end** – bepaalt hoe verzadigd de kleur aan het begin en einde is.
* **saturation variation** – randomiseert de verzadiging voor variatie tussen particles.

**Simulation**

* **time adjustment** – versnelt of vertraagt de volledige particle-simulatie. Handig om te synchroniseren met verschillende tempo’s of om beweging te versterken.
