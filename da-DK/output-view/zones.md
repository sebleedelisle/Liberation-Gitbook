---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zoner

Den zonetype, du kommer til at bruge i de fleste af dine projekter, er _Beam zone_. Det er en zone, der er beregnet til atmosfæriske beam-effekter gennem luften. Den anden zonetype er en _Canvas zone_ (se [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**ADVARSEL - Vær ekstremt forsigtig, når du flytter zoner, mens laseren kører**, og skru lysstyrken så langt ned som muligt. Se [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention") for en komplet vejledning i sikker aktivering og zoneinddeling af lasere
{% endhint %}

Du kan klikke og trække zonerne rundt med musen. Slå et testmønster til for at se, hvor zonen rammer.

{% hint style="info" %}
Brug piletasterne til at **nudge** den valgte zone/det valgte punkt. Hold `Shift` nede for at flytte i større trin.
{% endhint %}

{% hint style="info" %}
Tip: Du kan hurtigt kopiere zoneindstillinger på tværs af flere lasere! Se [copy-laser-settings.md](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Tilføjelse af en ny beam-zone

Klik på knappen _Add a new beam zone_ øverst på værktøjslinjen, så vises en ny zone. Bemærk, at beam-zoner sorteres i den rækkefølge, du tilføjer dem, men du kan ændre rækkefølgen. Se [re-ordering-beam-zones.md](re-ordering-beam-zones.md "mention")

### Tilføjelse af en eksisterende canvas-zone

Klik på knappen _Add existing canvas zone_, så ser du en liste over tilgængelige canvas-zoner, som du kan slå til og fra for denne laser. Se [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention")

### Zoneformtyper

Der er 3 zoneformtyper:

* **Quad** - standardformen for rektangulære zoner, som kan være ensartet (aksejusteret) eller forvrænget. Bedst til større rektangulære zoner eller canvas-zoner, der kræver perspektivkorrektion.
* **Line/Curve** - en zone defineret af 2 eller flere punkter og en tykkelse. Ideel til smalle zoner eller til at afgrænse på balkoner, broer eller andre buede former.
* **Segmented** - en zone, der kan opdeles i mindre quads. Ideel til arkitektonisk mapping.

Højreklik på en zone for at åbne dens indstillinger. Fra denne højrekliksmenu kan du:

* Omdøbe zonen (det kan være en hjælp til at identificere den i clip deck, især hvis du har mange zoner!)
* Aktivere/deaktivere zonen
* Låse dens position
* Ændre dens formtype
* Nulstille den til standardpositionen
* Få adgang til indstillinger, der er specifikke for formtypen
* Slette den
* Tilføje en _Alt Zone_ (se [alt-zone-system.md](alt-zone-system.md "mention"))

{% hint style="danger" %}
**ADVARSEL -** vær meget forsigtig, når du ændrer zonetypen, mens laseren er aktiv. Zonen vender tilbage til den seneste position/størrelse for den form, så outputtet kan ændre sig pludseligt. Det er bedst at slukke laseren, før du ændrer zonetypen.
{% endhint %}

### Quad-zoneform

Du kan flytte hvert hjørne af quad’en med musen. `Alt / Option`-klik på et hjørne for at flytte det uafhængigt af de andre og forvrænge quad’en. Når quad’en er forvrænget, kan alle hjørner flyttes frit.

Du kan fjerne forvrængningen og vende tilbage til et aksejusteret rektangel med knappen _REMOVE DISTORTION_ i højrekliksmenuen.

#### Perspektivkorrektion

Denne indstilling kan sættes med toggle-knappen i højrekliksmenuen, og den bestemmer forvrængningsmetoden. Det er bedst at lade den være slået fra til beams, men hvis denne zone projicerer grafik på en flad overflade, skal du slå den til, så outputtet perspektivkorrigeres.

{% hint style="info" %}
Hvis _Perspective correction_ er slået fra, forvrænges indholdet med _bi-linear interpolation_. Med andre ord fordeles indholdet jævnt over quad’en. Derfor er det bedst til beams.

Når perspektivkorrektion er slået til, forvrænges indholdet med perspective warping, som kompenserer for forkortning i perspektivet. Så hvis du projicerer grafik på en væg i en skrå vinkel, kan du bruge dette til at rette outputtet op og korrigere projektionsforvrængningen.
{% endhint %}

### Line / Curve-zoneform

Line / Curve-zoneformen er blevet mit foretrukne valg i de seneste shows, og man kan argumentere for, at den burde være standard for beam-zoner.

Ofte skal mine zoner være smalle for at passe ind i besværlige, smalle områder på venues eller mellem vinduer på bygninger, og jeg oplevede, at det kunne være virkelig besværligt at justere fire hjørner på en quad, når de ligger så tæt på hinanden. Derfor blev Line / Curve-zonen til!

Til lige linjer skal du kun bruge to punkter og derefter justere _Zone thickness_ i højrekliksmenuen. Det er den hurtigste måde at oprette enkle zoner på.

`Alt / Option`-klik på linjen for at oprette ekstra punkter. Disse punkter udglattes automatisk, så der dannes en flydende form, og du kan justere _Smooth level_ for at rette eventuelle knæk ud.

`Alt / Option`-klik på et punkt for at slette det.

Eller hvis du har erfaring med vektorgrafikprogrammer (Inkscape, Illustrator osv.), kan du bruge indstillingen _Manually adjust bezier curves_ til at finjustere alle kontrolpunkterne.

### Segmented-zoneform

Denne opdelte zone giver dig mulighed for at lave meget detaljerede korrektioner og er nyttig, når du mapper på komplekse former. Du kan tilføje eller fjerne opdelinger med knapperne + og - i højrekliksmenuen.

### Sådan redigerer du en zone, der er helt dækket af en anden zone

Højreklik på zonen øverst, og klik på hængelåsknappen for at låse den. Du bør nu kunne redigere og justere zonen nedenunder.

<br>

{% hint style="info" %}
Når du har tilføjet en Beam zone til dit output, kan den føjes til et clip i clip deck.
{% endhint %}
