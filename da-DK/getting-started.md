---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Hurtig startguide

## Introduktion

Velkommen til **Liberation** - næste generation af lasershow-software.

Liberation er moderne software, der både er kraftfuld og kompleks. Den er bygget på grundprincipper om brugervenlighed og driftssikkerhed, så du får frihed til at udtrykke din kreativitet. Den er hurtig, effektiv og enkel at arbejde med; følg denne _hurtige startguide_, så er du i gang på ingen tid!

### Håndtering af lasere

Liberation er fleksibel nok til, at du kan sætte lasere op og visualisere dem helt uden at have fysiske lasere tilsluttet. Når du så er klar, kan du nemt tildele hver output til en lasercontroller.

{% hint style="info" %}
Du kan sætte og visualisere så mange lasere op, som du vil, i Liberation. Licensniveauerne (Hobbyist, Pro osv.) begrænser kun antallet af lasere, du kan _arme._ Det betyder, at du kan designe lasershows med 100 lasere selv med en gratis licens. Du behøver først at opgradere, når du faktisk skal køre showet på rigtige lasere.
{% endhint %}

Som standard er der 8 lasere placeret vandret, men du kan tilpasse det til lige præcis det, du vil. Det er nok bedst at beholde standardopsætningen, mens du lærer softwaren at kende. Senere kan du justere den, så den matcher din hardwareopsætning. (Se [Opsætning af dit projekt](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Vigtigt: Før du armer nogen lasere, skal du sikre dig, at du forstår de involverede risici, og gennemgå kapitlet [Oversigt over opsætning af lasere](setting-up/setting-up-lasers.md "mention") grundigt.
{% endhint %}

## Overblik over softwaren

### Sikkerhedsafbrydelse

Når du kører lasere, skal du altid have en **fysisk nødstopknap** ved hånden (se [Nødstop / interlocks](hardware/emergency-stop-interlocks.md "mention")). Hvis du vil disarme alt uden samme hast, kan du bruge knappen _**DISARM ALL**_ eller `Escape`-tasten (eller _**SESSION**_-tasten på APC40). Du kan også reducere den globale lysstyrke med skyderen på skærmen eller med hovedfaderen på APC40.

### Skyder-elementer

Rundt omkring i Liberation findes der forskellige skydere og kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klik på en skyder for at indtaste en ny værdi, hvis du har brug for mere præcis kontrol, end skyderen giver dig.
{% endhint %}

### Tastaturgenveje

Du kan finde en komplet liste over tastaturgenveje her: [Tastaturgenveje](reference/keyboard-shortcuts.md "mention")

### Skærmlayout

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Er du i tvivl om, hvad en bestemt knap gør? Hold musen over den for at få en beskrivelse!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menuen er stedet, hvor du finder alle muligheder for filimport/-eksport og kan åbne paneler. Her finder du også muligheden for at autorisere computeren med dit abonnement (under _Liberation -> Authorise/Deauthorise this computer_).

#### Ikonlinje

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Her finder du almindelige opgaver, f.eks. at arme/disarme alle lasere, global lysstyrke, testmønster og skift mellem visningerne 3D, Canvas og Output.

### Visninger

Det store område øverst til venstre på skærmen kan vise en af 3 hovedvisninger: **3D**, **CANVAS** og **OUTPUT.** Skift mellem dem med knapperne på ikonlinjen (eller brug `Tab`-tasten til at skifte mellem 3D- og OUTPUT-visningerne, og fortsæt derefter med at tabbe gennem hver laseroutput én ad gangen).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-visningen viser, hvordan dine lasere kommer til at se ud, og kan konfigureres, så den matcher din egen laseropsætning. Klik og træk for at rotere kameraet, og brug musehjulet til at bevæge dig frem og tilbage. Du kan finde mange flere muligheder i panelet _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3D Visualiser](setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-visningen bruges til at konfigurere zoner og masker for hver laser. (Bemærk det meget store tal i øverste venstre hjørne, så du nemt kan se, hvilken laser du arbejder med!)

Denne visning er en repræsentation af hele outputtet fra denne laser, og hvor hver zone ligger i det. Som standard er der kun én zone pr. laser, men du kan tilføje så mange zoner, som det er praktisk muligt, og du vil kunne se dem alle i denne visning.

{% hint style="info" %}
**Hvad er en zone?**

En zone er et område i en lasers output, som du kan sende laserindhold ind i. Du kan have mere end én zone pr. laser. Den enkleste zonetype er en _beam_-zone, men der findes også _canvas_-zoner og _DMX_-zoner. I denne guide fokuserer vi primært på beam-zoner, som normalt bruges til at skabe atmosfæriske beam-effekter gennem luften.
{% endhint %}

Du kan vælge den laser, du vil redigere, på en af disse måder:

* de nummererede knapper i linjen øverst
* tryk på taltasten for den laser, du vil vælge _(tasterne 1-9)_
* `Tab`-tasten for at skifte fra den ene til den næste

Tilføj en ny laser til opsætningen ved at trykke på _+_-knappen. (Der findes også en _ADD LASER_-knap i panelet _Laser Overview_)

Slet en laser fra opsætningen ved at trykke på den røde ⊖-knap i panelet _Laser Overview_.

Du kan zoome ind og ud med musehjulet og klikke og trække et sted, hvor der ikke er en zone, for at flytte visningen.

Klik på en zone for at vælge den, og juster derefter dens hjørnepunkter med musen. Brug `Alt / Option`-tasten, mens du trækker i et hjørne, for at gøre justeringen uensartet. Højreklik på zonen for at se flere muligheder, herunder ændring af zonetype.

Langs venstre side er der en linje med en række ikonknapper. Hold musen over en knap for at få en beskrivelse af, hvad den gør. Knapperne her lader dig tilføje beam-zoner, canvas-zoner og masker. Der findes også muligheder for at indstille et testmønster kun for denne laser samt indstillinger for grid og snapping.

Se flere detaljer i [Output-visning](output-view/ "mention").

#### Canvas

Canvas-systemet bruges primært til grafik og architectural mapping. Du kan fordele komplekse billeder på tværs af flere lasere og perspektivkorrigere hver sektion. Se [Grafik og Canvas-systemet](graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Selvom det er muligt at styre Liberation med mus og tastatur, er det langt bedre at bruge en APC40 MIDI-control interface (Mark 2 er bedst, men Mark 1 virker også).

Se også: [APC40-reference](reference/apc40-reference.md "mention")

Vi har nu også implementeret understøttelse af APC Mini Mark 2 og MIDI Fighter Twister, og flere er under udvikling. Men APC40 Mark 2 er den bedste løsning i de fleste tilfælde.

### Clips og effekter

{% hint style="info" %}
**Hvad er et clip?**

Et clip er en beholder til laserindhold i Liberation. Clips kan indeholde beams eller grafiske animationer, og de er normalt et loop. De kan sendes til enhver zone (eller _Canvas target area_) og trigges med clip-knapperne i clip deck.
{% endhint %}

#### Overblik over clip deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dette grid kaldes _clip deck_, og det er her, alle laser-clips gemmes. Det er designet til at mappe direkte til 8 x 5-knapgitteret på din APC40.

**Navigation i clip deck.**

Du kan scrolle clip deck til venstre og højre på disse måder:

* Venstre og højre piletast. Tilføj `Cmd / Ctrl` for at scrolle en hel side ad gangen.
* Trackpad: Swipe
* Mus: Hvis din mus har sidelæns scroll, kan du bruge det, mens markøren er over clip deck
* APC40 scroll-knap
* APC40 _<- DEVICE ->_-knapper

For at hjælpe dig med at orientere dig er der en mini-visualisering af clip deck langs toppen. Se også [Clips & Clip deck](clips/ "mention")

#### Start og stop af clips

Tryk på en clip-knap (enten med musen eller med APC40) for at starte et clip. Tryk igen for at stoppe det. Når du starter et clip, stopper alle andre clips med samme farve automatisk, medmindre du holder _shift_ nede.

Nogle clips vil være i _Flash mode_ (som standard de røde). I så fald stopper de, så snart du slipper clip-knappen.

Knappen _STOP_ stopper alle clips, der kører i øjeblikket.

#### Indstilling af outputzoner for clippet

Under clip-knapperne kan du se zoneknapperne, som standard beam-zoner 1 til 8 (_BEAM 1_, _BEAM 2_ osv.). Zoneknapperne lyser for at vise, hvilke zoner der er tildelt det aktuelt valgte clip.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

To rækker under zoneknapperne kan du se X/Y flip-knapperne. Slå dem til eller fra for at vende clippet vandret og lodret.

{% hint style="info" %}
Bemærk, at disse zonetildelinger og X/Y flip-indstillinger er knyttet til selve clippet; de bevares, næste gang du kører det clip. De er ikke en global indstilling.
{% endhint %}

Højreklik på et clip for at redigere flere indstillinger for clippet. Se også [Clip-indstillinger](clips/clip-settings.md "mention")

### Groups

Du vil bemærke, at hvert clip har en farvet kontur, og denne farve viser, hvilken _group_ det er i. APC40 clip-knapperne lyser også i denne farve.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Rød</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Grøn</td></tr></tbody></table>

Group-systemet er meget fleksibelt, og det lader dig:

* Lade clips i én group fortsætte, mens du toggler groups i en anden
* Hurtigt tildele zoner og X/Y flips til alle clips i en group
* Indstille _Flash mode_ for et clip (Group 3 er som standard sat til _Flash mode_)

Groups har også indstillinger for transition in/out, som kan nedarves af dens clips eller tilsidesættes.

Du kan tildele clippets group med knapperne i højreklik-menuen. Med APC40 kan du også trykke på group-knappen og, _mens den stadig holdes nede,_ trykke på clip-knapperne.

Ændr zoneindstillinger for alle clips i en group

Med APC40 skal du trykke på group-knappen og derefter, _mens den stadig holdes nede,_ bruge zone- og X/Y-knapperne til at toggle zoneindstillinger for alle clips i den group.

Se også [Clip-grupper](clips/groups.md "mention")

### Effects

Effects-systemet i Liberation er en kraftfuld og alsidig måde at ændre clip-output i realtid på. Standard effect-knapperne 1-8 ligger under zoneknapperne.

#### Anvendelse af en effect

Tryk på en effect-knap for at slå effekten til eller fra - eller endnu bedre: brug APC40-skyderne 1-8 til at fade effects ind og ud.

#### Effect-parametre

Brug drejekontrollerne 1-8\* til at justere _parameter_ for hver effect. (Eller du kan højreklikke med musen for at justere level og parameter). Parameterændringen gør forskellige ting afhængigt af, hvordan effekten er sat op. Se listen nedenfor for standard effects.

{% hint style="info" %}
De små tal, du ser på effect-knapperne, henviser til effektens _level_ og _parameter_. _Level_ styres af faderen på APC40, eller du kan klik-trække på knappen. Parameteren justeres med drejekontrollerne på APC40, eller du kan højreklikke for at justere med musen.
{% endhint %}

_\*Drejekontroller 1-8 sidder langs toppen af en APC40 Mk2 og øverst til højre på Mk1. Se også:_ [APC40-reference](reference/apc40-reference.md "mention")

#### Standard effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Anvender en kaotisk bevægelse på clip-outputtet. Parameteren justerer mængden/hastigheden af kaos.
2. **Sine wave** :\
   Forvrænger alt indhold hen over en bevægende sinuskurve. Parameteren justerer bølgelængden.
3. **Rotation** :\
   Roterer det hele rundt. Parameteren justerer rotationshastigheden.
4. **Horizontal flip** :\
   Presser og strækker det hele vandret. Parameteren justerer hastigheden.
5. **Scale** :\
   Skalerer gentagne gange det hele fra fuld størrelse til nul. Parameteren justerer hastigheden.
6. **Hue** :\
   Ændrer hue for det hele, men ændrer ikke saturation (dvs. alt, der er hvidt, forbliver hvidt). Parameteren justerer hue.
7. **Saturation and hue** :\
   Ændrer hue for det hele og saturerer også farven fuldt ud (dvs. alt, der er hvidt, skifter til farven). Parameteren justerer hue.
8. **Flash** :\
   Blinker gentagne gange lysstyrken for det hele fra fuld til nul. Parameteren justerer blinkhastigheden.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Der er yderligere 16 colour effects langs nederste række, som anvender forudindstillede hue- og saturation-værdier.

Bemærk, at dette er standard effects, men de kan redigeres til at gøre næsten hvad som helst!

#### Hvad er det _"aktuelt valgte clip"_?

Når du starter et clip, lyser det for at vise, at det er aktivt. Det har også en hvid kontur omkring sig, som viser, at dette er det aktuelt _valgte_ clip. Når du toggler zoneknapper eller justerer clip-indstillingerne, anvendes disse på det _aktuelt valgte clip._

{% hint style="info" %}
Hvis du vil vælge et clip uden at trigge det, skal du trykke på `Alt / Option`-tasten, før du trykker på clip-knappen. Det er en god måde at justere zoner og andre indstillinger på uden at køre det.
{% endhint %}

### Clip Settings-panel

Brug panelet _Clip Settings_ til at redigere skalering, X/Y-position og få adgang til det kraftfulde zone delay-system.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-panel

Find panelet _Global Settings_ for at justere globale outputindstillinger, der påvirker alt output på tværs af alle zoner.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå AUTO RESET til for automatisk at nulstille alle _Global settings_, når ingen clips afspilles.

### Timing

Næsten alle lasershows har en eller anden form for musikalsk soundtrack, så timing-systemet i Liberation er baseret på et tempo i beats per minute. I _Tempo Panel_ kan du se en visuel repræsentation af tiden; hver firkant repræsenterer et beat, og du kan se dem blinke i takt.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Der findes flere synkroniseringsmuligheder, herunder MIDI clock og Ableton Link. Hvis du kender musikkens tempo, kan du justere det manuelt med skyderen på skærmen eller APC40 Tempo-knappen, men du kan også holde takten med musikken ved hjælp af _Tap Tempo_-systemet\_.\_

#### Tap Tempo

_Tap Tempo_ er et udtryk, der ofte bruges i musikapps, og det lader dig tappe i takt med beatet for at indstille tempoet, mens musikken spiller. Du kan bruge knappen på skærmen, men det anbefales at bruge _T_-tasten eller _Tap Tempo_-knappen på APC40 (eller endda en fodkontakt, hvis du foretrækker det).

Tryk på _R_-tasten eller _Metronome_-knappen (APC40) for at nulstille tempoet til starten af takten.

Tryk på _Y_-tasten, eller drej _Tempo_-knappen (APC40), for at runde tempoet til et helt tal. Det kan være nyttigt til elektronisk musik, som ofte ligger på et helt antal beats per minute.

### Organisering af dit clip deck

Hvis du vil flytte et clip på dit clip deck, skal du klikke og trække det til en ny placering. Mens du trækker, kan du bruge piletasterne (eller scrollhjulet/-knapperne på din APC40) til at scrolle til venstre og højre.

Tryk på `Alt / Option`-tasten, mens du trækker, for at lave en kopi.

`Alt / Option`-klik på et clip for at vælge det uden at starte det.

`Alt / Option + Shift`-klik på et clip for at multivælge, eller klik og træk uden for et clip for at vælge med "lasso".

Klik og træk vil trække ALLE valgte clips.

Hvis du vil slette et eller flere clips, kan du enten trække dem væk fra clip deck (der vises et skraldespandsikon) eller bruge DELETE-knappen fra clippets højreklik-menu.

### Laser Overview-panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelet _Laser Overview_ giver dig et hurtigt overblik over status for de lasere, der kører i øjeblikket. Den grønne firkant til højre viser, at lasercontrolleren er tilfreds. Hvis den bliver orange, har du lejlighedsvise drop-outs, og hvis den er rød, er den blevet afbrudt. Hvis den er grå, er den slet ikke tilsluttet en controller.

Grafen i midten viser en historik over frame-længder, og tallet til højre er den aktuelle frame rate. Jo mere kompliceret indholdet er, desto lavere bliver frame raten (dvs. mere flimren). Alt under cirka 25 fps vil begynde at se en smule flimrende ud.

### Tilslutning til lasere - Controller Assignment-panel

Klik på knappen _Assign Laser Controllers_ for at åbne panelet _Controller Assignment_. (Dette panel kan også åbnes via _View -> Controller Assignment_ i menulinjen).

Her kan du vælge, hvilke laseroutputs der skal gå til hvilke lasercontrollere. Træk og slip controllere fra listen til højre ind i pladserne til venstre. Du kan omdøbe dine controllere, så de matcher den laser, de er parret med (brug knappen med penneikonet).

Læs kapitlet [Tildeling af controllere](setting-up/controller-assignment.md "mention") for flere detaljer.

{% hint style="danger" %}
Før du armer nogen lasere, skal du sørge for at gennemgå kapitlet [Oversigt over opsætning af lasere](setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser Output-panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dette panel viser indstillingerne for den _aktuelt valgte laser_ (repræsenteret af tallet øverst). Skift den aktuelt valgte laser med _tab_-tasten, ved at trykke på en taltast, ved at klikke på et lasernummer i panelet _Laser Overview_ eller i _output view._

* **Number button** armer og disarmer laseren. Hvis den er rød, er laseren armed.
* **Brightness** justerer laserens lysstyrke uafhængigt af de andre lasere (og den kombineres med indstillingen _global brightness_ - dvs. hvis begge står på 50 %, vil din laser være på 25 %).
* **Test Pattern** slår et testmønster til kun for denne laser (tilsidesætter den globale test pattern-indstilling)
* **Orientation** korrigerer for lasere, der er rigget sidelæns eller på hovedet.
* **Flip Horizontal and Flip Vertical** vender laserens output. Nyttigt til outputkorrektion på lasere med inkonsistent ledningsføring.
* **Copy Laser Settings** åbner et panel, hvor du kan kopiere forskellige indstillinger fra denne laser til andre.

### Scannerindstillinger

Displaylasere fungerer ved at flytte en enkelt laserstråle ekstremt hurtigt og tænde og slukke den for at tegne former i luften. Det, du ser som linjer, former og billeder, er i virkeligheden strålen, der følger baner hurtigere, end dine øjne kan opfatte.

En point stream er de data, der fortæller laseren, hvor den skal bevæge sig hen næste gang, og hvornår strålen skal være tændt eller slukket. I Liberation konverteres clips til denne point stream i realtid, efterhånden som de sendes til laserne.

Liberation giver dig detaljeret kontrol over, hvordan denne point stream genereres, så du kan balancere smoothness, brightness og performance for hver laser.

{% hint style="info" %}
Hvis du er vant til ældre lasersoftware, der er afhængig af forudberegnede point streams, kan denne tilgang føles anderledes i starten. Men realtidsgenerering af punkter gør det muligt at optimere det samme indhold forskelligt for hver laser. Det gør det nemmere at arbejde med flere lasere, der har forskellige scannerhastigheder eller forskellig kvalitet, uden at duplikere eller genopbygge indhold. Det holder også clip-filer meget små, hvilket er grunden til, at hele Liberation-standardens clip deck kun fylder få megabyte i stedet for gigabyte.
{% endhint %}

De grundlæggende scannerindstillinger er:

* **Speed** er scannerhastigheden, dvs. hvor hurtigt laseren bevæger sig rundt for at tegne former. Det svarer til at justere point rate i traditionel lasersoftware, men i Liberation kan du ændre, hvor hurtigt laseren bevæger sig, _uafhængigt af point rate._ Du bør ikke have behov for at justere dette.
* **Scanner sync** (nogle gange kaldet _blank shift, tidligere Colour Shift_) Scannerne bevæger laseren rundt meget hurtigt, men normalt er ændringen i lysstyrke og farve ikke synkron med bevægelsen. Det viser sig som små flimrende "haler" af lys på kanten af beams og linjer. Brug denne justering til at få bevægelse og farve synkroniseret med hinanden. Se [Panelet Laser output settings](setting-up/laser-settings.md "mention")

De øvrige avancerede scannerindstillinger beskrives i kapitlet [Avanceret](advanced/ "mention").

### Zoning

Se en komplet guide til opsætning og zoning af lasere her: [Oversigt over opsætning af lasere](setting-up/setting-up-lasers.md "mention")
