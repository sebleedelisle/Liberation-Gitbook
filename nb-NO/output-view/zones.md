---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Soner

Hovedtypen sone du vil bruke i de fleste prosjektene dine, er _Beam zone_. Dette er en sone laget for atmosfæriske beam-effekter gjennom luften. Den andre sonetypen er en _Canvas zone_ (se [Grafikk og Canvas-systemet](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**ADVARSEL – Vær ekstremt forsiktig når du flytter soner mens laseren kjører**, og sett lysstyrken så lavt som mulig. Se [Oversikt over prosessen for laseroppsett](../setting-up/setting-up-lasers.md "mention") for en komplett veiledning i hvordan du aktiverer og soner lasere på en trygg måte.
{% endhint %}

Du kan klikke og dra sonene rundt med musen. Slå på et testmønster for å se hvor sonen havner.

{% hint style="info" %}
Bruk piltastene til å **finjustere** den valgte sonen/det valgte punktet. Hold inne `Shift` for å flytte i større trinn.
{% endhint %}

{% hint style="info" %}
Tips: Du kan raskt kopiere soneinnstillinger på tvers av flere lasere! Se [Kopier innstillinger mellom lasere](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Legge til en ny Beam zone

Klikk på knappen _Add a new beam zone_ øverst på verktøylinjen, så vises en ny sone. Merk at Beam zones sorteres i rekkefølgen du legger dem til, men du kan endre rekkefølgen. Se [Endre rekkefølgen på beam-soner](re-ordering-beam-zones.md "mention")

### Legge til en eksisterende Canvas zone

Klikk på knappen _Add existing canvas zone_, så får du se en liste over tilgjengelige Canvas zones, og du kan slå dem av og på for denne laseren. Se [Grafikk og Canvas-systemet](../graphics-and-the-canvas-system/ "mention")

### Typer soneform

Det finnes 3 typer soneform:

* **Quad** – standard rektangulær soneform, som kan være jevn (aksejustert) eller forvrengt. Best for større rektangulære soner eller Canvas zones som krever perspektivkorrigering.
* **Line/Curve** – en sone definert av 2 eller flere punkter og en tykkelse. Ideell for smale soner eller for avgrensing mot balkonger, broer eller andre buede former.
* **Segmented** – en sone som kan deles opp i mindre quads. Ideell for arkitektonisk mapping.

Høyreklikk på en hvilken som helst sone for å åpne innstillingene. Fra denne høyreklikkmenyen kan du:

* Gi sonen nytt navn (dette kan være nyttig for å identifisere den i Clip Deck, spesielt hvis du har mange soner!)
* Aktivere/deaktivere sonen
* Låse posisjonen
* Endre formtype
* Tilbakestille den til standardposisjon
* Få tilgang til innstillinger som er spesifikke for formtypen
* Slette den
* Legge til en _Alt Zone_ (se [Alt zone-systemet](alt-zone-system.md "mention"))

{% hint style="danger" %}
**ADVARSEL –** vær svært forsiktig når du endrer sonetype mens laseren er aktiv. Sonen går tilbake til siste posisjon/størrelse for den formen, så output kan endre seg brått. Det er best å slå av laseren før du endrer sonetype.
{% endhint %}

### Quad-soneform

Du kan flytte hvert hjørne i quad-en med musen. `Alt / Option`-klikk på et hjørne for å flytte det uavhengig av de andre og forvrenge quad-en. Når quad-en først er forvrengt, kan alle hjørnene flyttes fritt.

Du kan fjerne forvrengningen og sette den tilbake til et aksejustert rektangel med knappen _REMOVE DISTORTION_ i høyreklikkmenyen.

#### Perspective correction

Dette alternativet kan settes med veksleknappen i høyreklikkmenyen, og det bestemmer forvrengningsmetoden. Det er best å ha dette avslått for beams, men hvis denne sonen projiserer grafikk på en flat flate, slår du det på, så blir output perspektivkorrigert.

{% hint style="info" %}
Hvis _Perspective correction_ er slått av, forvrenges innholdet med _bi-lineær interpolasjon_. Med andre ord fordeles innholdet jevnt over quad-en. Derfor egner det seg best for beams.

Når perspektivkorrigering er slått på, forvrenges innholdet med perspektiv-warping, som kompenserer for forkorting. Hvis du for eksempel projiserer grafikk på en vegg i skrå vinkel, kan du bruke dette til å rette opp output og korrigere projeksjonsforvrengningen.
{% endhint %}

### Line / Curve-soneform

Line / Curve-soneformen har blitt mitt førstevalg i nyere show, og det kan argumenteres for at dette burde være standardvalget for Beam zones.

Ofte må sonene mine være smale for å få plass i vanskelige, smale områder på spillesteder eller mellom vinduer på bygninger, og jeg oppdaget at det kunne være veldig plundrete å justere fire hjørner på en quad når de ligger så tett. Slik ble Line / Curve-soneformen til!

For rette linjer trenger du bare to punkter, og deretter justerer du _Zone thickness_ i høyreklikkmenyen. Det er den raskeste måten å lage enkle soner på.

`Alt / Option`-klikk på linjen for å opprette flere punkter. Disse punktene glattes automatisk for å lage en flytende form, og du kan justere _Smooth level_ for å jevne ut eventuelle knekk.

`Alt / Option`-klikk på et punkt for å slette det.

Hvis du har erfaring med vektorgrafikkprogrammer (Inkscape, Illustrator osv.), kan du også bruke alternativet _Manually adjust bezier curves_ for å få finjustering av alle kontrollpunktene.

### Segmented-soneform

Denne oppdelte sonen lar deg gjøre svært detaljerte korrigeringer og er nyttig når du mapper på komplekse former. Du kan legge til eller fjerne inndelinger med + og - knappene i høyreklikkmenyen.

### Slik redigerer du en sone som er helt dekket av en annen sone

Høyreklikk på sonen som ligger øverst, og klikk på hengelåsknappen for å låse den. Nå skal du kunne redigere og justere sonen under.

<br>

{% hint style="info" %}
Når du har lagt til en Beam zone i outputen din, blir den tilgjengelig for å legges til i en Clip i Clip Deck.
{% endhint %}
