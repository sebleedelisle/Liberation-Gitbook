# ✅ Snelstartgids

## Introductie

Welkom bij **Liberation** - de volgende generatie lasershowsoftware.

Liberation is krachtige en complexe moderne software. Het is gebouwd op basisprincipes van gebruiksgemak en betrouwbaarheid, zodat je de vrijheid hebt om je creativiteit te uiten. Het is snel, efficiënt en naadloos in gebruik; volg deze _Snelstartgids_ om in korte tijd aan de slag te gaan!

### Lasers beheren

Liberation is flexibel genoeg om lasers in te stellen en te visualiseren zonder dat er echte lasers zijn aangesloten. Zodra je klaar bent om te starten, kun je elke output naadloos toewijzen aan een lasercontroller.

{% hint style="info" %}
Je kunt binnen Liberation zoveel lasers instellen en visualiseren als je wilt. De licentieniveaus (Hobbyist, Pro, enz.) beperken alleen het aantal lasers dat je kunt _armen._ Dit betekent dat je zelfs met een gratis licentie lasershows met 100 lasers kunt ontwerpen. Je hoeft pas te upgraden wanneer je de show daadwerkelijk op echte lasers wilt draaien.
{% endhint %}

Standaard staan er 8 lasers horizontaal naast elkaar, maar je kunt dit volledig aanpassen zoals je wilt. Het is waarschijnlijk het beste om deze standaardinstelling te behouden terwijl je de software leert kennen. Later kun je dit aanpassen aan je hardware-opstelling. (Zie [Je project instellen](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Belangrijk: voordat je lasers armt, moet je zorgen dat je de risico’s begrijpt en het hoofdstuk [Overzicht van het instelproces voor lasers](../setting-up/setting-up-lasers.md "mention") zorgvuldig doornemen.
{% endhint %}

## Overzicht van de software

### Veiligheidsuitschakeling

Wanneer je lasers gebruikt, moet je altijd een **hardware-noodstopknop** bij de hand hebben (zie [Noodstop / veiligheidsinterlocks](../hardware/emergency-stop-interlocks.md "mention")). Als je alles minder dringend wilt disarmen, kun je de knop _**DISARM ALL**_ gebruiken, of de `Escape`-toets (of de _**SESSION**_-toets op de APC40). Je kunt ook de globale helderheid verlagen met de slider op het scherm of met de main fader op de APC40.

### Slider-elementen

In Liberation vind je verschillende sliders en controls.

{% hint style="info" %}
`Cmd / Ctrl`-klik op een slider om een nieuwe waarde te typen als je meer controle nodig hebt dan de slider biedt.
{% endhint %}

### Sneltoetsen

Een volledige lijst met sneltoetsen vind je hier: [Sneltoetsen](../reference/keyboard-shortcuts.md "mention")

### Schermindeling

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Weet je niet zeker wat een bepaalde knop doet? Beweeg er met je muis overheen om een beschrijving te zien!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

In het menu vind je alle opties voor file import / export en kun je panels openen. Je vindt hier ook de optie om de computer met je abonnement te autoriseren (via _Liberation -> Authorise/Deauthorise this computer_).

#### Icon bar

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Hier vind je veelgebruikte taken, zoals alle lasers armen/disarmen, de globale helderheid, test pattern, en schakelen tussen de 3D-, Canvas- en Output-weergaven.

### Views

Het grote gebied linksboven in het scherm kan een van de 3 hoofdweergaven zijn: **3D**, **CANVAS** en **OUTPUT.** Je schakelt ertussen met de knoppen in de icon bar (of gebruik de `Tab`-toets om te wisselen tussen de 3D- en OUTPUT-weergaven, en blijf daarna tabben om één voor één door elke laser output te gaan).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

De 3D-weergave laat zien hoe je lasers eruit zullen zien en kan worden ingesteld zodat deze overeenkomt met je eigen laseropstelling. Klik en sleep om de camera te draaien, en gebruik het muiswiel om naar voren en achteren te bewegen. Je vindt veel andere opties in het panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Zie [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

De output-weergave wordt gebruikt om zones en masks voor elke laser te configureren. (Let op het grote nummer linksboven, zodat je gemakkelijk ziet op welke laser je zit!)

Deze weergave is een representatie van de volledige output van deze laser, en van waar elke zone daarin ligt. Standaard is er maar één zone per laser, maar je kunt zoveel zones toevoegen als praktisch haalbaar is. Je ziet ze allemaal in deze weergave.

{% hint style="info" %}
**Wat is een zone?**

Een zone is een ruimte binnen de output van een laser waar je lasercontent naartoe kunt sturen. Je kunt meer dan één zone per laser hebben. Het eenvoudigste type zone is een _beam_-zone, maar er zijn ook _canvas_-zones en _DMX_-zones. In deze gids richten we ons vooral op beam-zones, die meestal worden gebruikt om atmosferische beam-effecten door de lucht te maken.
{% endhint %}

Je kunt de laser die je wilt bewerken selecteren met:

* de genummerde knoppen in de balk bovenaan
* de cijfertoets voor de gewenste laser _(1-9_-toetsen\_)\_
* de `Tab`-toets om van de ene naar de volgende te gaan

Voeg een nieuwe laser toe aan de set-up door op de _+_-knop te drukken. (Er is ook een knop _ADD LASER_ in het panel _Laser Overview_)

Verwijder een laser uit de set-up door op de rode ⊖-knop in het panel _Laser Overview_ te drukken.

Je kunt in- en uitzoomen met het scrollwiel van de muis, en klikken en slepen op elke plek waar geen zone staat om de weergave te verplaatsen.

Klik op een zone om deze te selecteren en pas daarna de hoekpunten aan met de muis. Houd de `Alt / Option`-toets ingedrukt terwijl je een hoek sleept om deze niet-uniform te maken. Rechtsklik op de zone om meer opties te zien, waaronder het wijzigen van het type zone.

Links staat een balk met een reeks pictogramknoppen. Beweeg over een knop om een beschrijving te zien van wat deze doet. Met de knoppen hier kun je beam-zones, canvas-zones en masks toevoegen. Er zijn ook opties om alleen voor deze laser een test pattern in te stellen, plus grid- en snapping-instellingen.

Zie [Output-weergave](../output-view/ "mention") voor meer details.

#### Canvas

Het Canvas-systeem wordt vooral gebruikt voor graphics en architectural mapping. Je kunt complexe afbeeldingen over meerdere lasers verdelen en elk deel corrigeren voor perspectief. Zie [Graphics en het Canvas-systeem](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Hoewel het mogelijk is om Liberation met muis en toetsenbord te bedienen, werkt het veel beter met een APC40 MIDI control interface (Mark 2 is het beste, maar Mark 1 werkt ook).

Zie ook: [APC40-referentie](../reference/apc40-reference.md "mention")

We hebben inmiddels ook ondersteuning geïmplementeerd voor APC Mini Mark 2 en de MIDI Fighter Twister, en er zijn meer controllers in ontwikkeling. Maar de APC40 Mark 2 is in de meeste gevallen de beste optie.&#x20;

### Clips en effecten

{% hint style="info" %}
**Wat is een clip?**

Een clip is een container voor lasercontent binnen Liberation. Clips kunnen beams of grafische animaties bevatten en zijn meestal een herhalende cyclus. Ze kunnen naar elke zone (of _Canvas target area_) worden gestuurd en worden getriggerd met de clip buttons in het Clip Deck.
{% endhint %}

#### Overzicht van het Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dit raster staat bekend als het _Clip Deck_ en is de plek waar alle laserclips worden opgeslagen. Het is ontworpen om direct overeen te komen met het 8 x 5-raster van knoppen op je APC40.

**Navigeren door het Clip Deck.**

Je kunt het Clip Deck naar links en rechts scrollen met:

* Pijltjestoetsen links en rechts. Voeg `Cmd / Ctrl` toe om telkens één volledige pagina te scrollen.
* Trackpad: swipe
* Muis: als je muis zijwaarts scrollen ondersteunt, kun je dat gebruiken terwijl je boven het Clip Deck hangt
* APC40 scroll knob
* APC40 _<- DEVICE ->_-knoppen

Om je te helpen je weg te vinden, staat er bovenaan een mini-visualiser van het Clip Deck. Zie ook [Clips & Clip Deck](../clips/ "mention")

#### Clips starten en stoppen

Druk op een clip button (met de muis of met de APC40) om een clip te starten. Druk er nogmaals op om deze te stoppen. Wanneer je een clip start, stoppen alle andere clips met dezelfde kleur automatisch, tenzij je _shift_ ingedrukt houdt.

Sommige clips staan in _Flash mode_ (standaard de rode clips). In dat geval stoppen ze zodra je de clip button loslaat.

De knop _STOP_ stopt alle clips die op dat moment draaien.

#### Output-zones instellen voor de clip

Onder de clip buttons zie je de zone buttons, standaard beam-zones 1 tot 8 (_BEAM 1_, _BEAM 2_, enz.). De zone buttons lichten op om aan te geven welke zones aan de momenteel geselecteerde clip zijn toegewezen.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Twee rijen onder de zone buttons zie je de X/Y flip buttons. Zet deze aan of uit om de clip horizontaal en verticaal te spiegelen.

{% hint style="info" %}
Let op: deze zone-toewijzingen en X/Y flip-instellingen zijn gekoppeld aan de clip zelf; ze worden bewaard voor de volgende keer dat je die clip draait. Het is geen globale instelling.
{% endhint %}

Rechtsklik op een clip om meer instellingen voor de clip te bewerken. Zie ook [Clip settings](../clips/clip-settings.md "mention")

### Groepen

Je zult zien dat elke clip een gekleurde rand heeft. Deze kleur geeft aan in welke _groep_ de clip zit. De APC40 clip buttons lichten ook op in deze kleur.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Groep 1</td><td>Cyaan</td></tr><tr><td>Groep 2</td><td>Oranje</td></tr><tr><td>Groep 3</td><td>Rood</td></tr><tr><td>Groep 4</td><td>Indigo</td></tr><tr><td>Groep 5</td><td>Groen</td></tr></tbody></table>

Het groepssysteem is erg flexibel en maakt het mogelijk om:

* clips in één groep te laten doorlopen terwijl je clips in een andere groep aan- en uitzet
* snel zones en X/Y flips toe te wijzen aan alle clips binnen een groep
* _Flash mode_ voor een clip in te stellen (Group 3 staat standaard op _Flash mode_)

Groepen hebben ook instellingen voor transition in/out die door de clips kunnen worden overgenomen, of overschreven.

Je kunt de groep van de clip toewijzen met de knoppen in het rechtsklikmenu, of met de APC40: druk op de group button en druk _terwijl je deze ingedrukt houdt_ op de clip buttons.

Zone-instellingen wijzigen voor alle clips binnen een groep

Druk op de APC40 op de group button en gebruik daarna _terwijl je deze ingedrukt houdt_ de zone- en X/Y-buttons om zone-instellingen voor alle clips binnen die groep te togglen.

Zie ook [Clipgroepen](../clips/groups.md "mention")

### Effecten

Het effects-systeem in Liberation is een krachtige en veelzijdige manier om de clip output in realtime te veranderen. De standaard effects buttons 1-8 staan onder de zone buttons.

#### Een effect toepassen

Druk op een effect button om het effect aan of uit te zetten, of nog beter: gebruik de APC40 sliders 1-8 om effecten in en uit te faden.

#### Effectparameters

Gebruik de rotary controllers 1-8\* om de _parameter_ voor elk effect aan te passen. (Of je kunt rechtsklikken met de muis om het level en de parameter aan te passen). De parameterwijziging doet verschillende dingen, afhankelijk van hoe het effect is ingesteld. Zie de lijst hieronder voor de standaardeffecten.

{% hint style="info" %}
De kleine cijfers die je op de effect buttons ziet, verwijzen naar het _level_ en de _parameter_ van het effect. Het _level_ wordt geregeld door de fader op de APC40, of je kunt op de knop klikken en slepen. De parameter wordt aangepast met de rotaries op de APC40, of je kunt rechtsklikken om deze met de muis aan te passen.
{% endhint %}

_\*Rotary controllers 1-8 zitten bovenaan op een APC40 Mk2 en rechtsboven op de Mk1. Zie ook:_ [APC40-referentie](../reference/apc40-reference.md "mention")

#### De standaardeffecten

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Past een chaotische beweging toe op de clip output. De parameter past de hoeveelheid/snelheid van de chaos aan.
2. **Sine wave** :\
   Vervormt alle content over een bewegende sinusgolf. De parameter past de golflengte aan.
3. **Rotation** :\
   Laat alles ronddraaien. De parameter past de draaisnelheid aan.
4. **Horizontal flip** :\
   Drukt alles horizontaal samen en rekt het uit. De parameter past de snelheid aan.
5. **Scale** :\
   Schaalt alles herhaaldelijk van volledig naar nul. De parameter past de snelheid aan.
6. **Hue** :\
   Verandert de tint van alles, maar verandert de verzadiging niet (dus alles wat wit is blijft wit). De parameter past de tint aan.
7. **Saturation and hue** :\
   Verandert de tint van alles en verzadigt de kleur ook volledig (dus alles wat wit is verandert naar de kleur). De parameter past de tint aan.
8. **Flash** :\
   Laat de helderheid van alles herhaaldelijk flitsen van volledig naar nul. De parameter past de flitssnelheid aan.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Er staan nog 16 extra kleureffecten op de onderste rij om vooraf ingestelde hue- en saturation-waarden toe te passen.

Let op: dit zijn de standaardeffecten, maar ze kunnen worden bewerkt om bijna alles te doen wat je wilt!

#### Wat is de _"currently selected clip"_?

Wanneer je een clip start, licht deze op om aan te geven dat hij actief is. Er staat ook een witte rand omheen, die aangeeft dat dit de momenteel _geselecteerde_ clip is. Wanneer je zone buttons togglet of clip-instellingen aanpast, worden deze toegepast op de _currently selected clip._

{% hint style="info" %}
Als je een clip wilt selecteren zonder deze te triggeren, druk je op de `Alt / Option`-toets voordat je op de clip button drukt. Dit is een handige manier om zones en andere instellingen aan te passen zonder de clip te draaien.
{% endhint %}

### Clip settings panel

Gebruik het panel _Clip Settings_ om scaling, X/Y position en het krachtige zone delay-systeem te bewerken.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global settings panel

Open het panel _Global Settings_ om globale output-instellingen aan te passen die van invloed zijn op alle output in alle zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Schakel AUTO RESET in om alle _Global settings_ automatisch te resetten wanneer er geen clips spelen.&#x20;

### Timing

Bijna alle lasershows hebben een muzikale soundtrack, dus het timingsysteem in Liberation is gebaseerd op een tempo in beats per minute. In het _Tempo Panel_ zie je een weergave van de tijd; elk vierkant staat voor een beat en je ziet ze op de maat knipperen.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Er zijn meerdere synchronisatieopties, waaronder MIDI clock en Ableton Link. Als je het tempo van de muziek weet, kun je het handmatig aanpassen met de slider op het scherm of de APC40 Tempo knob, maar je kunt ook in de maat blijven met de muziek via het _Tap Tempo_-systeem\_.\_

#### Tap Tempo

_Tap Tempo_ is een term die vaak in muziekapps wordt gebruikt. Hiermee kun je op de maat van de beat tikken om het tempo in te stellen terwijl de muziek speelt. Je kunt de knop op het scherm gebruiken, maar het is aan te raden om de _T_-toets of de _Tap Tempo_-knop op de APC40 te gebruiken (of zelfs een foot switch als je dat prettiger vindt).

Druk op de _R_-toets of de _Metronome_-knop (APC40) om het tempo te resetten naar het begin van de maat.

Druk op de _Y_-toets of draai aan de _Tempo_-knop (APC40) om het tempo af te ronden naar een heel getal. Dit kan handig zijn voor elektronische muziek, die meestal een rond aantal beats per minute heeft.

### Je Clip Deck organiseren

Om een clip op je Clip Deck te verplaatsen, klik en sleep je deze naar een nieuwe positie. Tijdens het slepen kun je de cursortoetsen gebruiken (of het scrollwiel/de knoppen op je APC40) om naar links en rechts te scrollen.

Houd de `Alt / Option`-toets ingedrukt terwijl je sleept om een kopie te maken.

`Alt / Option`-klik op een clip om deze te selecteren zonder hem te starten.

`Alt / Option + Shift`-klik op een clip om meerdere clips te selecteren, of klik en sleep buiten een clip om met een “lasso” te selecteren.&#x20;

Klikken en slepen verplaatst ALLE geselecteerde clips.

Om één of meer clips te verwijderen, sleep je ze van het Clip Deck af (er verschijnt een prullenbakpictogram) of gebruik je de DELETE-knop in het rechtsklikmenu van de clip.

### Laser overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Het panel _Laser Overview_ geeft je snel inzicht in de status van de lasers die momenteel draaien. Het groene vierkant rechts geeft aan dat de lasercontroller goed werkt. Als het oranje wordt, heb je af en toe drop-outs, en als het rood wordt is de verbinding verbroken. Als het grijs is, is er helemaal geen controller verbonden.&#x20;

De grafiek in het midden toont de historie van frame lengths, en het getal rechts is de huidige frame rate. Hoe complexer de content, hoe lager de frame rate zal zijn (dus hoe meer flicker). Alles onder ongeveer 25fps begint wat flickery te ogen.&#x20;

### Verbinden met lasers - Controller Assignment panel

Klik op de knop _Assign Laser Controllers_ om het panel _Controller Assignment_ te openen. (Dit panel is ook bereikbaar via _View -> Controller Assignment_ in de menubalk).

Hier kun je kiezen welke laser outputs naar welke lasercontrollers gaan. Sleep controllers uit de lijst rechts naar slots links. Je kunt je controllers hernoemen zodat ze overeenkomen met de laser waaraan ze gekoppeld zijn (gebruik de knop met het penpictogram).

Lees het hoofdstuk [Controllertoewijzing](../setting-up/controller-assignment.md "mention") voor meer details.

{% hint style="danger" %}
Voordat je lasers armt, moet je het hoofdstuk [Overzicht van het instelproces voor lasers](../setting-up/setting-up-lasers.md "mention") doornemen.
{% endhint %}

### Laser output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dit panel toont de instellingen voor de _currently selected laser_ (aangegeven door het nummer bovenaan). Wijzig welke laser momenteel geselecteerd is met de _tab_-toets, door op een cijfertoets te drukken, door op een lasernummer in het panel _Laser Overview_ te klikken of in de _output view._

* **Number button** armt en disarmt de laser; als deze rood is, is de laser armed.
* **Brightness** past de laserhelderheid aan, onafhankelijk van de andere lasers (en wordt gecombineerd met de instelling _global brightness_ - dus als beide op 50% staan, staat je laser op 25%).
* **Test Pattern** schakelt alleen voor deze laser een test pattern in (overschrijft de globale test pattern-instelling)
* **Orientation** corrigeert lasers die zijwaarts of ondersteboven zijn opgehangen.
* **Flip Horizontal and Flip Vertical** keert de output van de laser om. Handig voor output-correctie bij lasers die inconsistent bedraad zijn.
* **Copy Laser Settings** opent een panel waarmee je verschillende instellingen van deze laser naar andere lasers kunt kopiëren.

### Scanner-instellingen

Displaylasers werken door één enkele laserstraal extreem snel te bewegen en deze aan en uit te zetten om vormen in de lucht te tekenen. Wat je ziet als lijnen, vormen en afbeeldingen is in werkelijkheid de straal die paden volgt, sneller dan je ogen kunnen volgen.

Een point stream is de data die de laser vertelt waar hij naartoe moet bewegen en wanneer de straal aan of uit moet staan. In Liberation worden clips in realtime omgezet naar deze point stream terwijl ze naar de lasers worden gestuurd.

Liberation geeft je gedetailleerde controle over hoe deze point stream wordt gegenereerd, zodat je voor elke laser een balans kunt vinden tussen vloeiendheid, helderheid en performance.

{% hint style="info" %}
Als je gewend bent aan oudere lasersoftware die afhankelijk is van vooraf berekende point streams, kan deze aanpak in het begin anders aanvoelen. Realtime point generation maakt het echter mogelijk om dezelfde content per laser anders te optimaliseren. Daardoor werk je makkelijker met meerdere lasers die verschillende scanner speeds of kwaliteit hebben, zonder content te dupliceren of opnieuw op te bouwen. Het houdt clipbestanden ook erg klein; daarom is het volledige standaard Clip Deck van Liberation maar een paar megabytes groot in plaats van gigabytes.
{% endhint %}

De basisinstellingen voor scanners zijn:

* **Speed** is de scanner speed, dus hoe snel de laser beweegt om vormen te tekenen. Dit komt overeen met het aanpassen van de point rate in traditionele lasersoftware, maar in Liberation kun je wijzigen hoe snel de laser beweegt _onafhankelijk van de point rate._ Je zou dit niet hoeven aan te passen.
* **Scanner sync** (soms bekend als _blank shift, previously Colour Shift_) De scanners bewegen de laser heel snel rond, maar meestal loopt de verandering in helderheid en kleur niet synchroon met de beweging. Dit zie je als kleine flikkerende “staarten” van licht aan de rand van beams en lijnen. Gebruik deze instelling om beweging en kleur met elkaar te synchroniseren. Zie [Paneel Laser output settings](../setting-up/laser-settings/ "mention")

De andere geavanceerde scanner-instellingen worden behandeld in het hoofdstuk [Geavanceerd](../advanced/ "mention").

### Zoning

Voor een volledige gids over het instellen en zonen van lasers, zie: [Overzicht van het instelproces voor lasers](../setting-up/setting-up-lasers.md "mention")
