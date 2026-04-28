# ✅ Kom godt i gang

## Introduktion

Velkommen til **Liberation** - næste generation af software til lasershows.

Liberation er moderne software, der både er kraftfuld og avanceret. Det er bygget på grundlæggende principper om brugervenlighed og driftssikkerhed, så du får frihed til at udtrykke din kreativitet. Det er hurtigt, effektivt og smidigt. Følg denne _Quick start guide_, så er du hurtigt i gang!

### Håndtering af lasere

Liberation er fleksibelt nok til, at du kan opsætte lasere og visualisere dem helt uden at have fysiske lasere tilsluttet. Når du er klar, kan du derefter nemt tildele hvert output til en laserkontroller.

{% hint style="info" %}
Du kan opsætte og visualisere så mange lasere, du vil, i Liberation. Licenstyperne (Hobbyist, Pro osv.) begrænser kun, hvor mange lasere du kan _arm._ Det betyder, at du kan designe lasershows med 100 lasere, selv med en gratis licens. Du behøver først at opgradere, når du faktisk skal køre showet på rigtige lasere.
{% endhint %}

Som standard er der 8 lasere fordelt vandret, men du kan tilpasse dette, som du vil. Det er sandsynligvis bedst at beholde standardopsætningen, mens du lærer softwaren at kende. Senere kan du justere den, så den passer til din hardwareopsætning. Se [setting-up-your-project.md](../setting-up/setting-up-your-project.md "mention")&#x20;

{% hint style="warning" %}
Vigtigt: Før du armer nogen lasere, skal du sikre dig, at du forstår de involverede risici, og gennemgå kapitlet [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention") grundigt.
{% endhint %}

## Oversigt over softwaren

### Sikkerhedsafbrydelse

Når du arbejder med lasere, skal du altid have en **hardware emergency stop button** ved hånden (se [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md "mention")). Hvis du vil disarme alt uden samme hast, kan du bruge knappen _**DISARM ALL**_ eller tasten `Escape` eller tasten _**SESSION**_ på APC40. Du kan også reducere den globale lysstyrke med skyderen på skærmen eller hovedfaderen på APC40.

### Skyder-elementer

I Liberation findes der forskellige skydere og kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klik på en skyder for at indtaste en ny værdi, hvis du har brug for mere præcis kontrol, end skyderen giver.
{% endhint %}

### Tastaturgenveje

Du kan finde en komplet liste over tastaturgenveje her: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md "mention")

### Skærmlayout

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Er du i tvivl om, hvad en bestemt knap gør? Hold musen over den for at få en beskrivelse!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menuen er der, hvor du finder alle muligheder for filimport og -eksport samt åbning af paneler. Her finder du også muligheden for at godkende computeren med dit abonnement under _Liberation -> Authorise/Deauthorise this computer_.

#### Ikonlinje

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Her finder du almindelige opgaver, f.eks. at arme/disarme alle lasere, global lysstyrke, test pattern og skift mellem visningerne 3D, Canvas og Output.

### Visninger

Det store område øverst til venstre på skærmen kan vise en af 3 hovedvisninger: **3D**, **CANVAS** og **OUTPUT.** Skift mellem dem med knapperne på ikonlinjen, eller brug tasten `Tab` til at skifte mellem 3D- og OUTPUT-visningen og derefter fortsætte gennem hvert laseroutput ét ad gangen.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-visningen viser, hvordan dine lasere kommer til at se ud, og den kan konfigureres, så den matcher din egen laseropsætning. Klik og træk for at rotere kameraet, og brug musehjulet til at bevæge dig frem og tilbage. Du finder mange flere muligheder i panelet _3D Visualiser settings_ under _View -> 3D Visualiser Settings_. Se [3d-visualiser.md](../setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-visningen bruges til at konfigurere zoner og masker for hver laser. Bemærk det meget store tal i øverste venstre hjørne, så du nemt kan se, hvilken laser du arbejder med.

Denne visning repræsenterer hele outputtet fra denne laser, og hvor hver zone er placeret i det. Som standard er der kun én zone pr. laser, men du kan tilføje så mange zoner, som det er praktisk muligt, og du vil se dem alle i denne visning.

{% hint style="info" %}
**Hvad er en zone?**

En zone er et område i en lasers output, som du kan sende laserindhold ind i. Du kan have mere end én zone pr. laser. Den enkleste zonetype er en _beam_-zone, men der findes også _canvas_-zoner og _DMX_-zoner. I denne guide fokuserer vi mest på beam-zoner, som normalt bruges til at lave atmosfæriske beam-effekter gennem luften.
{% endhint %}

Du kan vælge den laser, du vil redigere, på en af disse måder:

* de nummererede knapper i linjen øverst
* ved at trykke på taltasten for den laser, du vil vælge _(tasterne 1-9_)\_
* tasten `Tab` for at gå videre fra den ene til den næste

Tilføj en ny laser til opsætningen ved at trykke på knappen _+_. Der findes også en knap med _ADD LASER_ i panelet _Laser Overview_.

Slet en laser fra opsætningen ved at trykke på den røde ⊖-knap i panelet _Laser Overview_.

Du kan zoome ind og ud med musehjulet og klikke og trække et sted, hvor der ikke er en zone, for at flytte visningen.

Klik på en zone for at vælge den, og juster derefter dens hjørnepunkter med musen. Brug tasten `Alt / Option`, mens du trækker i et hjørne, for at gøre justeringen ikke-uniform. Højreklik på zonen for at se flere muligheder, herunder ændring af zonetypen.

Til venstre er der en linje med en række ikonknapper. Hold musen over en knap for at få en beskrivelse af, hvad den gør. Knapperne her lader dig tilføje beam-zoner, canvas-zoner og masker. Der er også muligheder for at indstille et test pattern kun for denne laser samt indstillinger for grid og snapping.

Se flere detaljer under [output-view](../output-view/ "mention").

#### Canvas

Canvas-systemet bruges hovedsageligt til grafik og architectural mapping. Du kan fordele komplekse billeder på tværs af flere lasere og perspektivkorrigere hver sektion. Se [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Selvom det er muligt at styre Liberation med mus og tastatur, er det meget bedre at bruge et APC40 MIDI-controllerinterface. Mark 2 er bedst, men Mark 1 virker også.

Se også: [apc40-reference.md](../reference/apc40-reference.md "mention")

Vi har nu også implementeret understøttelse af APC Mini Mark 2 og MIDI Fighter Twister, og flere er under udvikling. Men APC40 Mark 2 er den bedste løsning i de fleste tilfælde.&#x20;

### Clips og effekter

{% hint style="info" %}
**Hvad er et clip?**

Et clip er en beholder til laserindhold i Liberation. Clips kan indeholde beams eller grafiske animationer, og de er normalt en loopende cyklus. De kan sendes ind i en hvilken som helst zone eller _Canvas target area_ og udløses med clip-knapperne i Clip Deck.
{% endhint %}

#### Oversigt over Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dette grid kaldes _Clip Deck_, og det er her, alle laser-clips gemmes. Det er designet til at mappe direkte til 8 x 5-gridet af knapper på din APC40.

**Navigering i Clip Deck.**

Du kan scrolle Clip Deck mod venstre og højre med:

* Venstre og højre piletast. Tilføj `Cmd / Ctrl` for at scrolle en hel side ad gangen.
* Trackpad: Swipe
* Mus: Hvis din mus har sidelæns scroll, kan du bruge det, mens markøren er over Clip Deck.
* APC40 scroll knob
* APC40 _<- DEVICE ->_-knapperne

For at hjælpe dig med at orientere dig er der en mini-visualisering af Clip Deck langs toppen. Se også [clips](../clips/ "mention")

#### Starte og stoppe clips

Tryk på en clip-knap, enten med musen eller med APC40, for at starte et clip. Tryk på den igen for at stoppe det. Når du starter et clip, stopper alle andre clips med samme farve automatisk, medmindre du holder _shift_ nede.

Nogle clips er i _Flash mode_ som standard de røde. I så fald stopper de, så snart du slipper clip-knappen.

Knappen _STOP_ stopper alle clips, der kører i øjeblikket.

#### Indstilling af outputzoner for clippet

Under clip-knapperne ser du zoneknapperne, som som standard er beam-zoner 1 til 8: _BEAM 1_, _BEAM 2_ osv. Zoneknapperne lyser for at vise, hvilke zoner der er tildelt det aktuelt valgte clip.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

To rækker under zoneknapperne ser du X/Y flip-knapperne. Slå dem til og fra for at vende clippet vandret og lodret.

{% hint style="info" %}
Bemærk, at disse zonetildelinger og X/Y flip-indstillinger er knyttet til selve clippet. De bevares, næste gang du kører det clip. De er ikke en global indstilling.
{% endhint %}

Højreklik på et clip for at redigere flere indstillinger for clippet. Se også [clip-settings.md](../clips/clip-settings.md "mention")

### Grupper

Du vil bemærke, at hvert clip har en farvet kant, og denne farve viser, hvilken _gruppe_ det er i. APC40 clip-knapperne lyser også i denne farve.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Gruppe 1</td><td>Cyan</td></tr><tr><td>Gruppe 2</td><td>Orange</td></tr><tr><td>Gruppe 3</td><td>Rød</td></tr><tr><td>Gruppe 4</td><td>Indigo</td></tr><tr><td>Gruppe 5</td><td>Grøn</td></tr></tbody></table>

Gruppesystemet er meget fleksibelt, og det lader dig:

* Holde clips i én gruppe kørende, mens du toggler grupper i en anden
* Hurtigt tildele zoner og X/Y flips til alle clips i en gruppe
* Indstille _Flash mode_ for et clip. Gruppe 3 er som standard sat til _Flash mode_.

Grupper har også indstillinger for transition in/out, som kan nedarves af gruppens clips eller tilsidesættes.

Du kan tildele clippets gruppe med knapperne i højreklikmenuen. Med APC40 kan du også trykke på gruppeknappen og, _mens den stadig holdes nede_, trykke på clip-knapperne.

Skift zoneindstillinger for alle clips i en gruppe

Med APC40 skal du trykke på gruppeknappen og derefter, _mens den stadig holdes nede_, bruge zone- og X/Y-knapperne til at toggle zoneindstillinger for alle clips i den gruppe.

Se også [groups.md](../clips/groups.md "mention")

### Effekter

Effektsystemet i Liberation er en kraftfuld og alsidig måde at ændre clip-outputtet i realtid. Standardeffektknapperne 1-8 ligger under zoneknapperne.

#### Anvend en effekt

Tryk på en effektknap for at toggle effekten, eller endnu bedre: Brug APC40-skyderne 1-8 til at fade effekter ind og ud.

#### Effektparametre

Brug drejeknapperne 1-8\* til at justere _parameteren_ for hver effekt. Du kan også højreklikke med musen for at justere level og parameter. Parameterændringen gør forskellige ting afhængigt af, hvordan effekten er sat op. Se listen nedenfor for standardeffekterne.

{% hint style="info" %}
De små tal, du ser på effektknapperne, henviser til effektens _level_ og _parameter_. _Level_ styres med faderen på APC40, eller du kan klikke og trække på knappen. Parameteren justeres med drejeknapperne på APC40, eller du kan højreklikke og justere med musen.
{% endhint %}

_\*Drejeknapperne 1-8 sidder langs toppen af en APC40 Mk2 og øverst til højre på Mk1. Se også:_ [apc40-reference.md](../reference/apc40-reference.md "mention")

#### Standardeffekterne

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Tilføjer en kaotisk bevægelse til clip-outputtet. Parameteren justerer mængden/hastigheden af kaos.
2. **Sine wave** :\
   Forvrænger alt indhold hen over en bevægende sinusbølge. Parameteren justerer bølgelængden.
3. **Rotation** :\
   Drejer alt rundt. Parameteren justerer rotationshastigheden.
4. **Horizontal flip** :\
   Presser og strækker alt vandret. Parameteren justerer hastigheden.
5. **Scale** :\
   Skalerer gentagne gange alt fra fuld størrelse til nul. Parameteren justerer hastigheden.
6. **Hue** :\
   Ændrer farvetonen for alt, men ændrer ikke mætningen, dvs. alt hvidt forbliver hvidt. Parameteren justerer farvetonen.
7. **Saturation and hue** :\
   Ændrer farvetonen for alt og mætter også farven fuldt ud, dvs. alt hvidt skifter til farven. Parameteren justerer farvetonen.
8. **Flash** :\
   Blinker gentagne gange lysstyrken for alt fra fuld til nul. Parameteren justerer blinkhastigheden.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Der er yderligere 16 farveeffekter langs nederste række til at anvende forudindstillede værdier for farvetone og mætning.

Bemærk, at disse er standardeffekterne, men de kan redigeres til at gøre næsten hvad som helst!

#### Hvad er det _"currently selected clip"_?

Når du starter et clip, lyser det for at vise, at det er aktivt. Det har også en hvid kant omkring sig, som viser, at dette er det aktuelt _valgte_ clip. Når du toggler zoneknapper eller justerer clip-indstillinger, anvendes ændringerne på det _currently selected clip._

{% hint style="info" %}
For at vælge et clip uden at udløse det skal du trykke på tasten `Alt / Option`, før du trykker på clip-knappen. Det er en god måde at justere zoner og andre indstillinger uden at køre clippet.
{% endhint %}

### Clip Settings-panel

Brug panelet _Clip Settings_ til at redigere skalering, X/Y-position og få adgang til det kraftfulde zone delay-system.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-panel

Find panelet _Global Settings_ for at justere globale outputindstillinger, der påvirker alt output på tværs af alle zoner.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå AUTO RESET til for automatisk at nulstille alle _Global settings_, når der ikke afspilles nogen clips.&#x20;

### Timing

Næsten alle lasershows har en form for musikalsk lydspor, så timingsystemet i Liberation er baseret på et tempo i beats per minute. I _Tempo Panel_ kan du se en visuel repræsentation af tiden. Hver firkant repræsenterer et beat, og du kan se dem blinke i takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Der er flere synkroniseringsmuligheder, herunder MIDI clock og Ableton Link. Hvis du kender musikkens tempo, kan du justere det manuelt med skyderen på skærmen eller APC40 Tempo-knappen, men du kan også holde takt med musikken med _Tap Tempo_-systemet\_.\_

#### Tap Tempo

_Tap Tempo_ er et begreb, der ofte bruges i musikapps. Det lader dig tappe i takt med beatet for at indstille tempoet, mens musikken spiller. Du kan bruge knappen på skærmen, men det anbefales at bruge tasten _T_ eller knappen _Tap Tempo_ på APC40 eller endda en fodkontakt, hvis du foretrækker det.

Tryk på tasten _R_ eller knappen _Metronome_ på APC40 for at nulstille tempoet til begyndelsen af takten.

Tryk på tasten _Y_, eller drej på _Tempo_-knappen på APC40 for at runde tempoet af til et helt tal. Det kan være nyttigt til elektronisk musik, som ofte har et rundt antal beats per minute.

### Organisering af dit Clip Deck

For at flytte et clip på dit Clip Deck skal du klikke og trække det til en ny position. Mens du trækker, kan du bruge piletasterne eller scrollhjulet/knapperne på din APC40 til at scrolle mod venstre og højre.

Tryk på tasten `Alt / Option`, mens du trækker, for at lave en kopi.

`Alt / Option`-klik på et clip for at vælge det uden at starte det.

`Alt / Option + Shift`-klik på et clip for at vælge flere, eller klik og træk uden for et clip for at vælge med "lasso".&#x20;

Klik og træk flytter ALLE valgte clips.

For at slette et eller flere clips kan du enten trække dem væk fra Clip Deck, hvor der vises et skraldespandsikon, eller bruge knappen DELETE i clip-højreklikmenuen.

### Laser Overview-panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelet _Laser Overview_ giver dig et hurtigt overblik over status for de lasere, der kører i øjeblikket. Den grønne firkant til højre viser, at laserkontrolleren er tilfreds. Hvis den bliver orange, er der lejlighedsvise drop-outs, og hvis den er rød, er forbindelsen afbrudt. Hvis den er grå, er den slet ikke forbundet til en kontroller.&#x20;

Grafen i midten viser historik over frame-længder, og tallet til højre er den aktuelle frame rate. Jo mere komplekst indholdet er, desto langsommere bliver frame raten, dvs. mere flimrende. Alt under ca. 25 fps begynder at se lidt flimrende ud.&#x20;

### Tilslutning til lasere - Controller Assignment-panel

Klik på knappen _Assign Laser Controllers_ for at åbne panelet _Controller Assignment_. Dette panel kan også åbnes via _View -> Controller Assignment_ i menulinjen.

Her kan du vælge, hvilke laseroutputs der sendes til hvilke laserkontrollere. Træk og slip controllere fra listen til højre ind i pladserne til venstre. Du kan omdøbe dine controllere, så de matcher den laser, de er parret med, ved hjælp af knappen med penneikonet.

Læs kapitlet [controller-assignment.md](../setting-up/controller-assignment.md "mention") for flere detaljer.

{% hint style="danger" %}
Før du armer nogen lasere, skal du sørge for at gennemgå kapitlet [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser output-panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dette panel viser indstillingerne for den _currently selected laser_, som vises med tallet øverst. Skift den aktuelt valgte laser med tasten _tab_, ved at trykke på en taltast, ved at klikke på et lasernummer i panelet _Laser Overview_ eller i _output view._

* **Number button** armer og disarmer laseren. Hvis den er rød, er laseren armet.
* **Brightness** justerer laserens lysstyrke uafhængigt af de andre lasere. Den kombineres med indstillingen _global brightness_, dvs. hvis begge er på 50 %, vil din laser være på 25 %.
* **Test Pattern** slår et testmønster til kun for denne laser og tilsidesætter den globale test pattern-indstilling.
* **Orientation** korrigerer for lasere, der er rigget sidelæns eller på hovedet.
* **Flip Horizontal and Flip Vertical** vender laserens output. Nyttigt til outputkorrektion på lasere med inkonsekvent kabling.
* **Copy Laser Settings** åbner et panel, hvor du kan kopiere forskellige indstillinger fra denne laser til andre.

### Scannerindstillinger

Displaylasere fungerer ved at flytte en enkelt laserstråle ekstremt hurtigt og tænde og slukke den for at tegne former i luften. Det, du ser som linjer, former og billeder, er i virkeligheden strålen, der tegner baner hurtigere, end dine øjne kan følge med.

En point stream er de data, der fortæller laseren, hvor den skal bevæge sig hen næste gang, og hvornår strålen skal være tændt eller slukket. I Liberation konverteres clips til denne point stream i realtid, mens de sendes til laserne.

Liberation giver dig detaljeret kontrol over, hvordan denne point stream genereres, så du kan afbalancere jævnhed, lysstyrke og ydeevne for hver laser.

{% hint style="info" %}
Hvis du er vant til ældre lasersoftware, der er baseret på forudberegnede point streams, kan denne tilgang virke anderledes i starten. Pointgenerering i realtid gør det dog muligt at optimere det samme indhold forskelligt for hver laser. Det gør det nemmere at arbejde med flere lasere, der har forskellige scannerhastigheder eller forskellig kvalitet, uden at duplikere eller genopbygge indhold. Det holder også clip-filer meget små, hvilket er grunden til, at hele Liberation-standard-Clip Deck kun fylder nogle få megabyte i stedet for gigabyte.
{% endhint %}

De grundlæggende scannerindstillinger er:

* **Speed** er scannerhastigheden, dvs. hvor hurtigt laseren bevæger sig rundt for at tegne former. Det svarer til at justere point rate i traditionel lasersoftware, men i Liberation kan du ændre, hvor hurtigt laseren bevæger sig, _uafhængigt af point rate._ Du bør ikke have behov for at justere dette.
* **Scanner sync** kaldes nogle gange _blank shift, tidligere Colour Shift_. Scannerne bevæger laseren meget hurtigt rundt, men normalt er ændringen i lysstyrke og farve ude af sync med bevægelsen. Det viser sig som små flimrende "haler" af lys på kanten af beams og linjer. Brug denne justering til at få bevægelse og farve i sync med hinanden. Se [laser-settings](../setting-up/laser-settings/ "mention")

De øvrige avancerede scannerindstillinger gennemgås i kapitlet [advanced](../advanced/ "mention").

### Zoning

Se en komplet guide til opsætning og zoning af lasere her: [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention")
