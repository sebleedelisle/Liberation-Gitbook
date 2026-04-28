---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Het belangrijkste type zone dat je voor de meeste projecten gebruikt, is de _Beam zone_. Dit is een zone die is bedoeld voor atmosferische beam-effecten door de lucht. Het andere type zone is een _Canvas zone_ (zie [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**WAARSCHUWING - Wees uiterst voorzichtig wanneer je zones verplaatst terwijl de laser actief is** en zet de helderheid zo laag mogelijk. Zie [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention") voor een uitgebreide gids om lasers veilig te activeren en zones in te stellen.
{% endhint %}

Je kunt zones met de muis aanklikken en verslepen. Zet een testpatroon aan om te zien waar die zone terechtkomt.

{% hint style="info" %}
Gebruik de pijltoetsen om de momenteel geselecteerde zone/het geselecteerde punt met kleine stapjes te **verplaatsen**. Houd `Shift` ingedrukt om grotere stappen te gebruiken.
{% endhint %}

{% hint style="info" %}
Top tip: je kunt zone-instellingen snel naar meerdere lasers kopiëren! Zie [copy-laser-settings.md](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Een nieuwe beam-zone toevoegen

Klik op de knop _Add a new beam zone_ bovenaan de toolbar en er verschijnt een nieuwe zone. Let op: beam-zones worden gesorteerd in de volgorde waarin je ze toevoegt, maar je kunt die volgorde aanpassen. Zie [re-ordering-beam-zones.md](re-ordering-beam-zones.md "mention")

### Een bestaande canvas-zone toevoegen

Klik op de knop _Add existing canvas zone_. Je ziet dan een lijst met beschikbare canvas-zones, die je voor deze laser aan en uit kunt zetten. Zie [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention")

### Zonevormtypen

Er zijn 3 zonevormtypen:

* **Quad** - de standaard rechthoekige zonevorm, die uniform (as-uitgelijnd) of vervormd kan zijn. Het meest geschikt voor grotere rechthoekige zones of canvas-zones waarvoor perspectiefcorrectie nodig is.
* **Line/Curve** - een zone die wordt gedefinieerd door 2 of meer punten en een dikte. Ideaal voor smalle zones of voor het afkappen op balkons, bruggen of andere gebogen vormen.
* **Segmented** - een zone die kan worden onderverdeeld in kleinere quads. Ideaal voor architecturale mapping.

Klik met de rechtermuisknop op een zone om de instellingen te openen. Vanuit dit rechtermuisknopmenu kun je:

* De zone hernoemen (dit kan handig zijn om de zone te herkennen in de clip deck, vooral als je veel zones hebt!)
* De zone in-/uitschakelen
* De positie vergrendelen
* Het vormtype wijzigen
* De zone terugzetten naar de standaardpositie
* Instellingen openen die specifiek zijn voor het vormtype
* De zone verwijderen
* Een _Alt Zone_ toevoegen (zie [alt-zone-system.md](alt-zone-system.md "mention"))

{% hint style="danger" %}
**WAARSCHUWING -** wees zeer voorzichtig wanneer je het zonetype wijzigt terwijl de laser actief is. De zone keert terug naar de laatste positie/grootte voor die vorm, waardoor de output plotseling kan veranderen. Je kunt de laser het beste uitschakelen voordat je het zonetype wijzigt.
{% endhint %}

### Quad-zonevorm

Je kunt elke hoek van de quad met de muis verplaatsen. `Alt / Option`-klik op een hoek om die onafhankelijk van de andere hoeken te verplaatsen en de quad te vervormen. Zodra de quad is vervormd, kunnen alle hoeken vrij worden verplaatst.

Je kunt de vervorming verwijderen en de quad terugzetten naar een as-uitgelijnde rechthoek met de knop _REMOVE DISTORTION_ in het rechtermuisknopmenu.

#### Perspectiefcorrectie

Deze optie kun je instellen met de toggle-knop in het rechtermuisknopmenu. De optie bepaalt de vervormingsmethode. Voor beams kun je dit het beste uit laten staan, maar als deze zone graphics op een plat vlak projecteert, zet je dit aan zodat de output met perspectiefcorrectie wordt weergegeven.

{% hint style="info" %}
Als _Perspective correction_ is uitgeschakeld, wordt content vervormd met _bi-linear interpolation_. Met andere woorden: content wordt gelijkmatig over de quad verdeeld. Daarom is dit het meest geschikt voor beams.

Als perspectiefcorrectie is ingeschakeld, wordt content vervormd met perspective warping, waarbij verkorting door perspectief wordt gecorrigeerd. Dus als je graphics onder een schuine hoek op een muur projecteert, kun je dit gebruiken om de output recht te trekken en de projectievervorming te corrigeren.
{% endhint %}

### Line / Curve-zonevorm

De Line / Curve-zonevorm is bij recente shows mijn standaardkeuze geworden, en je zou kunnen zeggen dat dit eigenlijk de standaard voor beam-zones zou moeten zijn.

Vaak moeten mijn zones smal zijn om in lastige smalle ruimtes op locaties te passen, of tussen ramen op gebouwen. Ik merkte dat het erg priegelig kan zijn om vier hoeken van een quad aan te passen wanneer ze zo dicht bij elkaar liggen. Zo is de Line / Curve-zone ontstaan!

Voor rechte lijnen heb je alleen twee punten nodig. Daarna pas je de _Zone thickness_ aan in het rechtermuisknopmenu. Dit is de snelste manier om eenvoudige zones te maken.

`Alt / Option`-klik op de lijn om extra punten te maken. Deze punten worden automatisch vloeiend gemaakt om een doorlopende vorm te creëren, en je kunt de _Smooth level_ aanpassen om eventuele knikken weg te werken.

`Alt / Option`-klik op een punt om het te verwijderen.

Als je ervaring hebt met vectorgraphics-apps (Inkscape, Illustrator enz.), kun je ook de optie _Manually adjust bezier curves_ gebruiken voor fijne aanpassing van alle controlepunten.

### Segmented-zonevorm

Met deze onderverdeelde zone kun je zeer gedetailleerde correcties maken. Dit is handig wanneer je op complexe vormen aan het mappen bent. Je kunt onderverdelingen toevoegen of verwijderen met de knoppen + en - in het rechtermuisknopmenu.

### Een zone bewerken die volledig wordt bedekt door een andere zone

Klik met de rechtermuisknop op de bovenliggende zone en klik op de hangslotknop om deze te vergrendelen. Je kunt nu de onderliggende zone bewerken en aanpassen.

<br>

{% hint style="info" %}
Zodra je een Beam zone aan je output toevoegt, is deze beschikbaar om toe te voegen aan een clip in de clip deck.
{% endhint %}
