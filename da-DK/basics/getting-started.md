# ✅ Hurtig start-guide

## Introduktion

Velkommen til **Liberation** – næste generation af lasershowsoftware.

Liberation er moderne software, der både er kraftfuld og kompleks. Det er bygget på grundlæggende principper om brugervenlighed og driftssikkerhed, så du får frihed til at udtrykke din kreativitet. Det er hurtigt, effektivt og gnidningsløst; følg denne _Hurtig start-guide_, så er du i gang på ingen tid!

### Håndtering af lasere

Liberation er fleksibelt nok til, at du kan sætte lasere op og visualisere dem helt uden at have rigtige lasere tilsluttet. Når du så er klar, kan du problemfrit tildele hvert output til en laser controller.

{% hint style="info" %}
Du kan sætte og visualisere så mange lasere op, du vil, i Liberation. Licenstrinnene (Hobbyist, Pro osv.) begrænser kun antallet af lasere, du kan sætte i _armed_-tilstand. Det betyder, at du kan designe lasershows med 100 lasere, selv med en gratis licens. Du behøver kun at opgradere, når du rent faktisk skal køre showet på rigtige lasere.
{% endhint %}

Som standard er der 8 lasere fordelt vandret, men du kan tilpasse det præcis, som du vil. Det er nok bedst at beholde denne standard, mens du lærer softwaren at kende, og så senere justere den, så den passer til dit hardware-setup. (Se [Opsætning af dit projekt](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Vigtigt: Før du sætter nogen lasere i _armed_-tilstand, skal du sikre dig, at du forstår de involverede risici, og gå omhyggeligt igennem kapitlet [Opsætning af lasere](../setting-up/setting-up-lasers.md).
{% endhint %}

## Overblik over softwaren

### Sikkerhedsafbrydelse

Når du kører lasere, skal du altid have en **fysisk nødstopknap** ved hånden (se [Nødstop og interlocks](../hardware/emergency-stop-interlocks.md)). Hvis du vil sætte alt i _disarmed_-tilstand uden samme hast, kan du bruge knappen _**DISARM ALL**_, `Escape`-tasten eller _**SESSION**_-tasten på APC40. Du kan også reducere Global Brightness med skyderen på skærmen eller hovedfaderen på APC40.

### Skyder-elementer

Rundt omkring i Liberation finder du forskellige skydere og kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klik på en skyder for at skrive en ny værdi, hvis du har brug for mere præcis kontrol, end skyderen giver.
{% endhint %}

### Tastaturgenveje

En komplet liste over tastaturgenveje findes her: [Tastaturgenveje](../reference/keyboard-shortcuts.md)

### Skærmlayout

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Er du i tvivl om, hvad en bestemt knap gør? Hold musen over den for at få en beskrivelse!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menuen er stedet, hvor du finder alle muligheder for filimport og -eksport samt åbner paneler. Her finder du også muligheden for at godkende computeren med dit abonnement under _Liberation -> Authorise/Deauthorise this computer_.

#### Ikonlinje

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Her finder du almindelige opgaver, f.eks. at skifte alle lasere mellem _armed_ og _disarmed_, Global Brightness, test pattern og skift mellem 3D view, Canvas view og Output view.

### Views

Det store område øverst til venstre på skærmen kan vise en af 3 hovedvisninger: **3D**, **CANVAS** og **OUTPUT.** Skift mellem dem med knapperne på ikonlinjen, eller brug `Tab`-tasten til at skifte mellem 3D view og Output view og derefter fortsætte gennem hvert laseroutput ét ad gangen.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view viser, hvordan dine lasere kommer til at se ud, og kan konfigureres, så det matcher dit eget laser-setup. Klik og træk for at rotere kameraet, og brug musehjulet til at bevæge dig frem og tilbage. Du finder mange andre muligheder i panelet _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3D Visualiser](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view bruges til at konfigurere zones og masks for hver laser. Bemærk det meget store tal i øverste venstre hjørne, så du nemt kan se, hvilken laser du arbejder med.

Denne view er en repræsentation af hele outputtet fra denne laser, og hvor hver zone ligger i det. Som standard er der kun én zone pr. laser, men du kan tilføje så mange zones, som det er praktisk rimeligt, og du vil se dem alle i denne view.

{% hint style="info" %}
**Hvad er en zone?**

En zone er et område inden for en lasere output, som du kan sende laserindhold ind i. Du kan have mere end én zone pr. laser. Den enkleste type zone er en _beam_ zone, men der findes også _canvas_ zones og _DMX_ zones. I denne guide fokuserer vi primært på beam zones, som normalt bruges til at skabe atmosfæriske beam-effekter gennem luften.
{% endhint %}

Du kan vælge den laser, du vil redigere, på en af disse måder:

* de nummererede knapper i linjen øverst
* tryk på taltasten for den ønskede laser (_1-9_-tasterne)
* brug `Tab`-tasten til at gå videre fra den ene til den næste

Tilføj en ny laser til setuppet ved at trykke på _+_-knappen. Der er også en _ADD LASER_-knap i panelet _Laser Overview_.

Slet en laser fra setuppet ved at trykke på den røde ⊖-knap i panelet _Laser Overview_.

Du kan zoome ind og ud med musens scrollhjul og klikke og trække alle steder, hvor der ikke er en zone, for at flytte visningen.

Klik på en zone for at vælge den, og juster derefter dens hjørnepunkter med musen. Hold `Alt / Option`-tasten nede, mens du trækker i et hjørne, for at gøre justeringen ikke-ensartet. Højreklik på zonen for at se flere muligheder, herunder ændring af zone-typen.

Langs venstre side er der en linje med en række ikonknapper. Hold musen over en knap for at få en beskrivelse af, hvad den gør. Knapperne her lader dig tilføje beam zones, canvas zones og masks. Der er også muligheder for kun at sætte en test pattern for denne laser samt indstillinger for grid og snapping.

Se flere detaljer under [Output-visning](../output-view/).

#### Canvas

Canvas-systemet bruges mest til grafik og arkitektonisk mapping. Du kan fordele komplekse billeder på tværs af flere lasere og perspektivkorrigere hver sektion. Se [Grafik og Canvas-systemet](../graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Selvom det er muligt at styre Liberation med mus og tastatur, er det langt bedre at bruge et APC40 MIDI control interface. Mark 2 er bedst, men Mark 1 virker også.

Se også: [APC40-reference](../reference/apc40-reference.md)

Vi har nu også implementeret understøttelse af APC Mini Mark 2 og MIDI Fighter Twister, og flere er under udvikling. APC40 Mark 2 er dog den bedste løsning i de fleste tilfælde.&#x20;

### Clips og effekter

{% hint style="info" %}
**Hvad er en clip?**

En clip er en beholder til enhver form for laserindhold i Liberation. Clips kan indeholde beams eller grafiske animationer, og de er normalt en loopende cyklus. De kan sendes ind i enhver zone eller _Canvas target area_ og udløses med clip-knapperne i Clip Deck.
{% endhint %}

#### Overblik over Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dette gitter kaldes _Clip Deck_, og det er her, alle laser clips gemmes. Det er designet til at matche direkte med 8 x 5-gitteret af knapper på din APC40.

**Navigering i Clip Deck.**

Du kan rulle Clip Deck mod venstre og højre med:

* Venstre og højre piletast. Tilføj `Cmd / Ctrl` for at rulle én hel side ad gangen.
* Trackpad: Swipe
* Mus: Hvis din mus har vandret scroll, kan du bruge det, mens markøren er over Clip Deck
* APC40 scroll knob
* APC40 _<- DEVICE ->_-knapper

For at hjælpe dig med at holde overblikket er der en mini-visualisering af Clip Deck langs toppen. Se også [Clips & Clip deck](../clips/)

#### Starte og stoppe clips

Tryk på en clip-knap, enten med musen eller APC40, for at starte en clip. Tryk igen for at stoppe den. Når du starter en clip, stopper alle andre clips med samme farve automatisk, medmindre du holder _shift_ nede.

Nogle clips er i _Flash mode_ (som standard de røde). I så fald stopper de, så snart du slipper clip-knappen.

Knappen _STOP_ stopper alle clips, der kører aktuelt.

#### Indstilling af output zones for clip

Under clip-knapperne ser du zone-knapperne, som standard beam zones 1 til 8 (_BEAM 1_, _BEAM 2_ osv.). Zone-knapperne lyser for at vise, hvilke zones der er tildelt den aktuelt valgte clip.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

To rækker under zone-knapperne ser du X/Y flip-knapperne. Slå dem til eller fra for at spejle clip vandret og lodret.

{% hint style="info" %}
Bemærk, at disse zone-tildelinger og X/Y flip-indstillinger er knyttet til selve clip. De bevares, næste gang du kører den clip. De er ikke en global indstilling.
{% endhint %}

Højreklik på en clip for at redigere flere indstillinger for clip. Se også [Clip-indstillinger](../clips/clip-settings.md)

### Grupper

Du vil se, at hver clip har en farvet kant, og denne farve viser, hvilken _gruppe_ den ligger i. APC40 clip-knapperne lyser også i denne farve.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Gruppe 1</td><td>Cyan</td></tr><tr><td>Gruppe 2</td><td>Orange</td></tr><tr><td>Gruppe 3</td><td>Rød</td></tr><tr><td>Gruppe 4</td><td>Indigo</td></tr><tr><td>Gruppe 5</td><td>Grøn</td></tr></tbody></table>

Gruppesystemet er meget fleksibelt og giver dig mulighed for at:

* Lade clips i én gruppe fortsætte, mens du slår grupper til og fra i en anden
* Hurtigt tildele zones og X/Y flips til alle clips i en gruppe
* Sætte _Flash mode_ for en clip. Gruppe 3 er som standard sat til _Flash mode_

Grupper har også indstillinger for overgang ind/ud, som kan nedarves af deres clips eller tilsidesættes.

Du kan tildele en clips gruppe med knapperne i højrekliksmenuen. Med APC40 kan du trykke på gruppeknappen og, _mens den stadig holdes nede_, trykke på clip-knapperne.

Skift zone-indstillinger for alle clips i en gruppe

Med APC40 skal du trykke på gruppeknappen og derefter, _mens den stadig holdes nede_, bruge zone- og X/Y-knapperne til at slå zone-indstillinger til eller fra for alle clips i den gruppe.

Se også [Clip-grupper](../clips/groups.md)

### Effekter

Effektsystemet i Liberation er en kraftfuld og alsidig måde at ændre clip-output i realtid. Standard-effektknapperne 1-8 ligger under zone-knapperne.

#### Anvend en effekt

Tryk på en effektknap for at slå effekten til eller fra. Endnu bedre er det at bruge APC40-skydere 1-8 til at fade effekter ind og ud.

#### Effektparametre

Brug rotary controllers 1-8\* til at justere _parameteren_ for hver effekt. Du kan også højreklikke med musen for at justere niveau og parameter. Parameterændringen gør forskellige ting, afhængigt af hvordan effekten er sat op. Se listen nedenfor for standardeffekterne.

{% hint style="info" %}
De små tal, du ser på effektknapperne, henviser til effektens _level_ og _parameter_. _Level_ styres med faderen på APC40, eller du kan klikke og trække på knappen. Parameteren justeres med rotary controls på APC40, eller du kan højreklikke for at justere med musen.
{% endhint %}

_\*Rotary controllers 1-8 sidder langs toppen af en APC40 Mk2 og øverst til højre på Mk1. Se også:_ [APC40-reference](../reference/apc40-reference.md)

#### Standardeffekterne

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Tilføjer en kaotisk bevægelse til clip-outputtet. Parameteren justerer mængden/hastigheden af kaos.
2. **Sine wave** :\
   Forvrænger alt indhold hen over en bevægende sinusbølge. Parameteren justerer bølgelængden.
3. **Rotation** :\
   Roterer det hele rundt. Parameteren justerer rotationshastigheden.
4. **Horizontal flip** :\
   Klemmer og strækker det hele vandret. Parameteren justerer hastigheden.
5. **Scale** :\
   Skalerer gentagne gange det hele fra fuld størrelse til nul. Parameteren justerer hastigheden.
6. **Hue** :\
   Ændrer farvetonen for det hele, men ændrer ikke mætningen, dvs. alt hvidt forbliver hvidt. Parameteren justerer farvetonen.
7. **Saturation and hue** :\
   Ændrer farvetonen for det hele og mætter også farven fuldt ud, dvs. alt hvidt ændres til farven. Parameteren justerer farvetonen.
8. **Flash** :\
   Blinker gentagne gange lysstyrken for det hele fra fuld til nul. Parameteren justerer blinkhastigheden.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Der er yderligere 16 farveeffekter langs nederste række til at anvende forudindstillede værdier for farvetone og mætning.

Bemærk, at dette er standardeffekterne, men de kan redigeres til at gøre næsten hvad som helst!

#### Hvad er den _"aktuelt valgte clip"_?

Når du starter en clip, lyser den op for at vise, at den er aktiv. Den har også en hvid kant omkring sig, som viser, at dette er den aktuelt _valgte_ clip. Når du slår zone-knapper til eller fra eller justerer clip-indstillinger, anvendes de på den _aktuelt valgte clip._

{% hint style="info" %}
Hvis du vil vælge en clip uden at udløse den, skal du trykke på `Alt / Option`-tasten, før du trykker på clip-knappen. Det er en god måde at justere dens zones og andre indstillinger uden at køre den.
{% endhint %}

### Clip Settings-panel

Brug panelet _Clip Settings_ til at redigere skalering, X/Y-position og få adgang til det kraftfulde zone delay-system.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-panel

Find panelet _Global Settings_ for at justere globale outputindstillinger, der påvirker alt output på tværs af alle zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå AUTO RESET til for automatisk at nulstille alle _Global settings_, når der ikke afspilles nogen clips.&#x20;

### Timing

Næsten alle lasershows har en form for musikalsk lydspor, så timing-systemet i Liberation er baseret på et tempo i slag pr. minut. I _Tempo Panel_ kan du se en repræsentation af tiden. Hver firkant repræsenterer et beat, og du kan se dem blinke i takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Der er flere synkroniseringsmuligheder, herunder MIDI clock og Ableton Link. Hvis du kender musikkens tempo, kan du justere det manuelt med skyderen på skærmen eller APC40 Tempo-knappen, men du kan også holde takt med musikken ved hjælp af _Tap Tempo_-systemet\_.\_

#### Tap Tempo

_Tap Tempo_ er et begreb, der ofte bruges i musikapps, og det lader dig tappe i takt med beatet for at sætte tempoet, mens musikken spiller. Du kan bruge knappen på skærmen, men det anbefales at bruge _T_-tasten eller _Tap Tempo_-knappen på APC40, eller endda en fodkontakt, hvis du foretrækker det.

Tryk på _R_-tasten eller _Metronome_-knappen (APC40) for at nulstille tempoet til taktens begyndelse.

Tryk på _Y_-tasten, eller drej _Tempo_-knappen (APC40), for at runde tempoet af til et helt tal. Det kan være nyttigt til elektronisk musik, som ofte har et rundt antal slag pr. minut.

### Organisering af dit Clip Deck

Hvis du vil flytte en clip i dit Clip Deck, skal du klikke og trække den til en ny position. Mens du trækker, kan du bruge piletasterne eller scrollhjul/knapper på din APC40 til at rulle mod venstre og højre.

Hold `Alt / Option`-tasten nede, mens du trækker, for at lave en kopi.

`Alt / Option`-klik på en clip for at vælge den uden at starte den.

`Alt / Option + Shift`-klik på en clip for at vælge flere, eller klik og træk uden for en clip for at vælge med "lasso".&#x20;

Klik og træk vil trække ALLE valgte clips.

Hvis du vil slette en eller flere clips, kan du enten trække dem væk fra Clip Deck, så der vises et skraldespandsikon, eller bruge DELETE-knappen i clips højrekliksmenu.

### Laser Overview-panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelet _Laser Overview_ giver dig et hurtigt overblik over status for de lasere, der kører aktuelt. Den grønne firkant til højre viser, at laser controller fungerer, som den skal. Hvis den bliver orange, har du lejlighedsvise dropouts, og hvis den bliver rød, er forbindelsen afbrudt. Hvis den er grå, er den slet ikke tilsluttet en controller.&#x20;

Grafen i midten viser historikken for frame-længder, og tallet til højre er den aktuelle frame rate. Jo mere komplekst indholdet er, desto lavere bliver frame rate, dvs. mere flimren. Alt under ca. 25 fps vil begynde at se lidt flimrende ud.&#x20;

### Tilslutning til lasere – Controller Assignment-panel

Klik på knappen _Assign Laser Controllers_ for at åbne panelet _Controller Assignment_. Dette panel kan også åbnes via _View -> Controller Assignment_ i menulinjen.

Her kan du vælge, hvilke laserudgange der skal gå til hvilke laser controllers. Træk og slip controllers fra listen til højre ind i pladserne til venstre. Du kan omdøbe dine controllers, så de matcher den laser, de er parret med. Brug knappen med pen-ikonet.

Læs kapitlet [Tildeling af controllere](../setting-up/controller-assignment.md) for flere detaljer.

{% hint style="danger" %}
Før du sætter nogen lasere i _armed_-tilstand, skal du sørge for at gennemgå kapitlet [Opsætning af lasere](../setting-up/setting-up-lasers.md).
{% endhint %}

### Laser output-panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dette panel viser indstillingerne for den _aktuelt valgte laser_, repræsenteret ved tallet øverst. Skift den aktuelt valgte laser med _tab_-tasten, ved at trykke på en taltast, ved at klikke på et lasernummer i panelet _Laser Overview_ eller i _Output view._

* **Number button** skifter laseren mellem _armed_ og _disarmed_. Hvis den er rød, er laseren _armed_.
* **Brightness** justerer laserens lysstyrke uafhængigt af de andre lasere. Den kombineres med indstillingen _Global Brightness_, dvs. hvis begge står på 50 %, vil din laser være på 25 %.
* **Test Pattern** slår en test pattern til kun for denne laser og tilsidesætter den globale test pattern-indstilling.
* **Orientation** korrigerer for lasere, der er rigget sidelæns eller på hovedet.
* **Flip Horizontal and Flip Vertical** vender laserens output. Nyttigt til outputkorrektion på lasere med inkonsekvent kabling.
* **Copy Laser Settings** åbner et panel, der lader dig kopiere forskellige indstillinger fra denne laser til andre.

### Scanner-indstillinger

Displaylasere fungerer ved at bevæge en enkelt laserstråle ekstremt hurtigt og tænde og slukke den for at tegne former i luften. Det, du ser som linjer, former og billeder, er i virkeligheden strålen, der følger baner hurtigere, end dine øjne kan følge med.

En point stream er de data, der fortæller laseren, hvor den skal bevæge sig hen næste gang, og hvornår strålen skal være tændt eller slukket. I Liberation konverteres clips til denne point stream i realtid, mens de sendes til lasere.

Liberation giver dig detaljeret kontrol over, hvordan denne point stream genereres, så du kan afveje glathed, lysstyrke og ydeevne for hver laser.

{% hint style="info" %}
Hvis du er vant til ældre lasersoftware, der bygger på forudberegnede point streams, kan denne tilgang føles anderledes i starten. Realtidsgenerering af punkter gør det dog muligt at optimere det samme indhold forskelligt for hver laser. Det gør det nemmere at arbejde med flere lasere, der har forskellige scannerhastigheder eller forskellig kvalitet, uden at du skal duplikere eller genopbygge indhold. Det holder også clip-filer meget små, hvilket er grunden til, at hele Liberation-standard-Clip Deck kun fylder nogle få megabyte i stedet for gigabyte.
{% endhint %}

De grundlæggende scanner-indstillinger er:

* **Speed** er scannerhastigheden, dvs. hvor hurtigt laseren bevæger sig rundt for at tegne former. Det svarer til at justere point rate i traditionel lasersoftware, men i Liberation kan du ændre, hvor hurtigt laseren bevæger sig, _uafhængigt af point rate._ Du bør ikke have brug for at justere dette.
* **Scanner sync** (nogle gange kendt som _blank shift_, tidligere Colour Shift) Scannerne bevæger laseren rundt meget hurtigt, men ændringen i lysstyrke og farve er normalt ikke synkron med bevægelsen. Det viser sig som små flimrende "haler" af lys i kanten af beams og linjer. Brug denne justering til at få bevægelse og farve synkroniseret med hinanden. Se [Laser Settings](../setting-up/laser-settings/)

De øvrige avancerede scanner-indstillinger gennemgås i kapitlet [Avanceret](../advanced/).

### Zoning

Se en komplet guide til opsætning og zoning af lasere her: [Opsætning af lasere](../setting-up/setting-up-lasers.md)
