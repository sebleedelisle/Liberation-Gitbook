# ✅ Hurtigstartveiledning

## Innledning

Velkommen til **Liberation** – neste generasjon programvare for lasershow.

Liberation er kraftig og kompleks moderne programvare. Den er bygget på grunnleggende prinsipper for brukervennlighet og driftssikkerhet, slik at du får frihet til å uttrykke kreativiteten din. Den er rask, effektiv og sømløs. Følg denne _Hurtigstartveiledningen_ for å komme raskt i gang!

### Administrere lasere

Liberation er fleksibelt nok til at du kan sette opp lasere og visualisere dem helt uten at noen faktiske lasere er koblet til. Når du er klar til å kjøre, kan du sømløst tilordne hver output til en laserkontroller.

{% hint style="info" %}
Du kan sette opp og visualisere så mange lasere du vil i Liberation. Lisensnivåene (Hobbyist, Pro osv.) begrenser bare hvor mange lasere du kan _armere_. Det betyr at du kan designe lasershow med 100 lasere selv med en gratis lisens. Du trenger bare å oppgradere når du faktisk skal kjøre showet på ekte lasere.
{% endhint %}

Standardoppsettet har 8 lasere fordelt horisontalt, men du kan tilpasse dette akkurat slik du vil. Det er sannsynligvis best å beholde standardoppsettet mens du blir kjent med programvaren. Senere kan du justere det slik at det passer til maskinvareoppsettet ditt. (Se [setting-up-your-project.md](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Viktig: Før du armerer noen lasere, må du sørge for at du forstår risikoene og gå nøye gjennom kapitlet [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Oversikt over programvaren

### Sikkerhetsavstenging

Når du kjører lasere, må du alltid ha en **fysisk nødstoppsknapp** tilgjengelig (se [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md "mention")). Hvis du vil deaktivere alt på en mindre akutt måte, kan du bruke knappen _**DISARM ALL**_, eller `Escape`-tasten (eller _**SESSION**_-tasten på APC40). Du kan også redusere global lysstyrke med skyveknappen på skjermen eller hovedfaderen på APC40.

### Skyveknapper og kontroller

I Liberation finnes det ulike skyveknapper og kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klikk på en skyveknapp for å skrive inn en ny verdi hvis du trenger mer presis kontroll enn skyveknappen gir.
{% endhint %}

### Tastatursnarveier

Du finner en fullstendig liste over tastatursnarveier her: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md "mention")

### Skjermoppsett

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Usikker på hva en bestemt knapp gjør? Hold musepekeren over den for å se en beskrivelse!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

I menyen finner du alle alternativer for filimport og -eksport, og for å åpne paneler. Her finner du også valget for å autorisere datamaskinen med abonnementet ditt (i _Liberation -> Authorise/Deauthorise this computer_).

#### Icon bar

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Her finner du vanlige oppgaver, som å armere/deaktivere alle laserne, global lysstyrke, testmønster og bytte mellom visningene 3D, Canvas og Output.

### Visninger

Det store området øverst til venstre på skjermen kan vise én av tre hovedvisninger: **3D**, **CANVAS** og **OUTPUT.** Bytt mellom dem med knappene på ikonlinjen (eller bruk `Tab`-tasten til å bytte mellom 3D- og OUTPUT-visningene, og fortsett deretter å tabbe gjennom hver laser-output etter tur).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D-visningen viser hvordan laserne dine vil se ut, og kan konfigureres slik at den samsvarer med ditt eget laseroppsett. Klikk og dra for å rotere kameraet, og bruk musehjulet til å bevege deg frem og tilbake. Du finner mange andre alternativer i panelet _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3d-visualiser.md](../setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-visningen brukes til å konfigurere soner og masker for hver laser. (Legg merke til det store tallet øverst til venstre, slik at du enkelt ser hvilken laser du arbeider med!)

Denne visningen er en representasjon av hele outputen fra denne laseren, og hvor hver sone ligger innenfor den. Som standard finnes det bare én sone per laser, men du kan legge til så mange soner som det er praktisk å bruke, og du vil se alle i denne visningen.

{% hint style="info" %}
**Hva er en sone?**

En sone er et område innenfor en lasers output som du kan sende laserinnhold til. Du kan ha mer enn én sone per laser. Den enkleste typen sone er en _beam_-sone, men det finnes også _canvas_-soner og _DMX_-soner. I denne veiledningen fokuserer vi mest på beam-soner, som vanligvis brukes til å lage atmosfæriske stråleeffekter gjennom luften.
{% endhint %}

Du kan velge laseren du vil redigere, på én av disse måtene:

* de nummererte knappene i linjen øverst
* trykk på talltasten for laseren du vil ha _(tastene 1–9)_
* bruk `Tab`-tasten for å gå fra én laser til den neste

Legg til en ny laser i oppsettet ved å trykke på _+_-knappen. (Det finnes også en _ADD LASER_-knapp i panelet _Laser Overview_)

Slett en laser fra oppsettet ved å trykke på den røde ⊖-knappen i panelet _Laser Overview_.

Du kan zoome inn og ut med musehjulet, og klikke og dra hvor som helst der det ikke finnes en sone for å flytte visningen.

Klikk på en sone for å velge den, og juster deretter hjørnepunktene med musen. Hold inne `Alt / Option`-tasten mens du drar et hjørne for å gjøre justeringen ikke-uniform. Høyreklikk på sonen for å se flere alternativer, blant annet for å endre sonetype.

Langs venstre side finnes en linje med en serie ikonknapper. Hold musepekeren over en knapp for å få en beskrivelse av hva den gjør. Knappene her lar deg legge til beam-soner, canvas-soner og masker. Det finnes også alternativer for å angi et testmønster bare for denne laseren, samt innstillinger for rutenett og snapping.

Se [output-view](../output-view/ "mention") for mer informasjon.

#### Canvas

Canvas-systemet brukes hovedsakelig til grafikk og arkitektonisk mapping. Du kan fordele komplekse bilder på flere lasere og perspektivkorrigere hver del. Se [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Selv om det er mulig å styre Liberation med mus og tastatur, er det mye bedre å bruke et APC40 MIDI-kontrollgrensesnitt (Mark 2 er best, men Mark 1 fungerer også).

Se også: [apc40-reference.md](../reference/apc40-reference.md "mention")

Vi har nå også implementert støtte for APC Mini Mark 2 og MIDI Fighter Twister, og flere er under utvikling. APC40 Mark 2 er likevel det beste valget i de fleste tilfeller.&#x20;

### Clips og effekter

{% hint style="info" %}
**Hva er en clip?**

En clip er en beholder for alt laserinnhold i Liberation. Clips kan inneholde beams eller grafiske animasjoner, og de er vanligvis en loopende syklus. De kan sendes til hvilken som helst sone (eller _Canvas target area_) og trigges med clip-knappene i clip deck.
{% endhint %}

#### Oversikt over Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dette rutenettet kalles _clip deck_, og det er der alle laser-clips lagres. Det er utformet for å mappes direkte til 8 x 5-knapperutenettet på APC40.

**Navigere i clip deck.**

Du kan bla clip deck til venstre og høyre med:

* venstre og høyre piltast. Legg til `Cmd / Ctrl` for å bla én hel side om gangen.
* styreflate: sveip
* mus: hvis musen har horisontal rulling, kan du bruke den mens pekeren er over clip deck
* rullehjulet på APC40
* APC40 _<- DEVICE ->_-knappene

For å hjelpe deg å orientere deg finnes det en mini-visualisering av clip deck øverst. Se også [clips](../clips/ "mention")

#### Starte og stoppe clips

Trykk på en clip-knapp (enten med musen eller med APC40) for å starte en clip. Trykk på den igjen for å stoppe den. Når du starter en clip, stopper alle andre clips med samme farge automatisk, med mindre du holder inne _shift_.

Noen clips er i _Flash mode_ (som standard de røde), og da stopper de så snart du slipper clip-knappen.

Knappen _STOP_ stopper alle clips som kjører nå.

#### Angi output-soner for clipen

Under clip-knappene ser du soneknappene, som standard beam-soner 1 til 8 (_BEAM 1_, _BEAM 2_ osv.). Soneknappene lyser for å vise hvilke soner som er tilordnet den valgte clipen.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

To rader under soneknappene ser du X/Y flip-knappene. Slå disse av eller på for å vende clipen horisontalt og vertikalt.

{% hint style="info" %}
Merk at disse sonetildelingene og X/Y flip-innstillingene er knyttet til selve clipen. De beholdes neste gang du kjører den clipen. De er ikke en global innstilling.
{% endhint %}

Høyreklikk på en clip for å redigere flere innstillinger for clipen. Se også [clip-settings.md](../clips/clip-settings.md "mention")

### Grupper

Du vil se at hver clip har en farget omrisslinje, og denne fargen viser hvilken _gruppe_ den tilhører. Clip-knappene på APC40 lyser også i denne fargen.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Gruppe 1</td><td>Cyan</td></tr><tr><td>Gruppe 2</td><td>Oransje</td></tr><tr><td>Gruppe 3</td><td>Rød</td></tr><tr><td>Gruppe 4</td><td>Indigo</td></tr><tr><td>Gruppe 5</td><td>Grønn</td></tr></tbody></table>

Gruppesystemet er svært fleksibelt, og lar deg:

* la clips i én gruppe fortsette å kjøre mens du slår grupper i en annen gruppe av og på
* raskt tilordne soner og X/Y flips til alle clips i en gruppe
* angi _Flash mode_ for en clip (Gruppe 3 er satt til _Flash mode_ som standard)

Grupper har også innstillinger for overgang inn/ut som kan arves av clips i gruppen, eller overstyres.

Du kan tilordne clipens gruppe med knappene i høyreklikkmenyen. Med APC40 kan du også trykke på gruppeknappen og, _mens den fortsatt holdes inne_, trykke på clip-knappene.

Endre soneinnstillinger for alle clips i en gruppe

Med APC40 trykker du på gruppeknappen, og _mens den fortsatt holdes inne_, bruker du sone- og X/Y-knappene til å slå soneinnstillinger av eller på for alle clips i den gruppen.

Se også [groups.md](../clips/groups.md "mention")

### Effekter

Effektsystemet i Liberation er en kraftig og fleksibel måte å endre clip-output i sanntid på. Standard effektknapper 1–8 ligger under soneknappene.

#### Bruke en effekt

Trykk på en effektknapp for å slå effekten av eller på. Enda bedre er det å bruke APC40-faderne 1–8 til å fade effekter inn og ut.

#### Effektparametere

Bruk rotary-kontrollerne 1–8\* til å justere _parameteren_ for hver effekt. (Du kan også høyreklikke med musen for å justere nivå og parameter.) Parameterendringen gjør ulike ting avhengig av hvordan effekten er satt opp. Se listen nedenfor for standardeffektene.

{% hint style="info" %}
De små tallene du ser på effektknappene, viser til _level_ og _parameter_ for effekten. _Level_ styres med faderen på APC40, eller du kan klikke og dra på knappen. Parameteren justeres med rotary-kontrollerne på APC40, eller du kan høyreklikke for å justere med musen.
{% endhint %}

_\*Rotary-kontrollerne 1–8 ligger langs toppen på en APC40 Mk2 og øverst til høyre på Mk1. Se også:_ [apc40-reference.md](../reference/apc40-reference.md "mention")

#### Standardeffektene

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Legger kaotisk bevegelse på clip-outputen. Parameteren justerer mengden/hastigheten på kaoset.
2. **Sine wave** :\
   Forvrenger alt innhold over en bevegelig sinusbølge. Parameteren justerer bølgelengden.
3. **Rotation** :\
   Roterer alt rundt. Parameteren justerer rotasjonshastigheten.
4. **Horizontal flip** :\
   Klemmer og strekker alt horisontalt. Parameteren justerer hastigheten.
5. **Scale** :\
   Skalerer alt gjentatte ganger fra full størrelse til null. Parameteren justerer hastigheten.
6. **Hue** :\
   Endrer fargetonen på alt, men endrer ikke metningen (dvs. alt som er hvitt forblir hvitt). Parameteren justerer fargetonen.
7. **Saturation and hue** :\
   Endrer fargetonen på alt og metter også fargen fullt ut (dvs. alt som er hvitt endres til fargen). Parameteren justerer fargetonen.
8. **Flash** :\
   Blinker gjentatte ganger lysstyrken på alt fra full til null. Parameteren justerer blinkehastigheten.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finnes ytterligere 16 fargeeffekter langs nederste rad for å bruke forhåndsinnstilte hue- og saturation-verdier.

Merk at dette er standardeffektene, men de kan redigeres til å gjøre nesten hva du vil!

#### Hva er _"currently selected clip"_?

Når du starter en clip, lyser den for å vise at den er aktiv. Den har også en hvit omrisslinje rundt seg, som viser at dette er clipen som er valgt nå. Når du slår soneknapper av eller på, eller justerer clip-innstillingene, brukes disse på _currently selected clip_.

{% hint style="info" %}
For å velge en clip uten å trigge den, trykker du på `Alt / Option`-tasten før du trykker på clip-knappen. Dette er en god måte å justere soner og andre innstillinger på uten å kjøre den.
{% endhint %}

### Clip Settings-panel

Bruk panelet _Clip Settings_ til å redigere skalering, X/Y-posisjon og få tilgang til det kraftige systemet for soneforsinkelse.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-panel

Finn panelet _Global Settings_ for å justere globale output-innstillinger som påvirker all output på tvers av alle soner.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå på AUTO RESET for automatisk å tilbakestille alle _Global settings_ når ingen clips spiller.&#x20;

### Timing

Nesten alle laseroppsetninger har en form for musikalsk lydspor, så timing-systemet i Liberation er basert på et tempo i slag per minutt. I _Tempo Panel_ kan du se en representasjon av tiden. Hver rute representerer ett slag, og du kan se at de blinker i takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Det finnes flere synkroniseringsalternativer, inkludert MIDI clock og Ableton Link. Hvis du kjenner tempoet i musikken, kan du justere det manuelt med skyveknappen på skjermen eller APC40 Tempo-knotten, men du kan også holde takten med musikken ved hjelp av _Tap Tempo_-systemet\_.\_

#### Tap Tempo

_Tap Tempo_ er et begrep som ofte brukes i musikkapper, og det lar deg tappe i takt med slaget for å angi tempoet mens musikken spiller. Du kan bruke knappen på skjermen, men det anbefales å bruke _T_-tasten eller _Tap Tempo_-knappen på APC40 (eller til og med en fotbryter hvis du foretrekker det).

Trykk på _R_-tasten eller _Metronome_-knappen (APC40) for å tilbakestille tempoet til starten av takten.

Trykk på _Y_-tasten eller vri på _Tempo_-knotten (APC40) for å runde av tempoet til et helt tall. Dette kan være nyttig for elektronisk musikk, som ofte har et rundt antall slag per minutt.

### Organisere clip deck

For å flytte en clip i clip deck klikker du og drar den til en ny posisjon. Mens du drar, kan du bruke piltastene (eller rullehjulet/knappene på APC40) til å bla til venstre og høyre.

Hold inne `Alt / Option`-tasten mens du drar for å lage en kopi.

`Alt / Option`-klikk på en clip for å velge den uten å starte den.

`Alt / Option + Shift`-klikk på en clip for å multivelge, eller klikk og dra utenfor en clip for å velge med "lasso".&#x20;

Klikk og dra vil dra ALLE valgte clips.

For å slette én eller flere clips kan du enten dra dem ut av clip deck (et søppelbøtteikon vises) eller bruke DELETE-knappen i høyreklikkmenyen for clipen.

### Laser Overview-panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelet _Laser overview panel_ gir deg en rask oversikt over statusen til laserne som kjører nå. Den grønne firkanten til høyre viser at laserkontrolleren er fornøyd. Hvis den blir oransje, har du sporadiske dropouts, og hvis den blir rød, er den koblet fra. Hvis den er grå, er den ikke koblet til noen kontroller i det hele tatt.&#x20;

Grafen i midten viser historikk for bildelengder, og tallet til høyre er gjeldende bildefrekvens. Jo mer komplisert innholdet er, desto lavere blir bildefrekvensen (dvs. mer flimring). Alt under omtrent 25 fps vil begynne å se litt flimrende ut.&#x20;

### Koble til lasere – Controller Assignment-panel

Klikk på knappen _Assign Laser Controllers_ for å åpne panelet _Controller Assignment_. (Dette panelet kan også åpnes via _View -> Controller Assignment_ i menylinjen).

Her kan du velge hvilke laser-outputer som går til hvilke laserkontrollere. Dra og slipp kontrollere fra listen til høyre inn i plassene til venstre. Du kan gi kontrollerne nye navn slik at de samsvarer med laseren de er koblet sammen med (bruk knappen med pennikonet).

Les kapitlet [controller-assignment.md](../setting-up/controller-assignment.md "mention") for mer informasjon.

{% hint style="danger" %}
Før du armerer noen lasere, må du gå gjennom kapitlet [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser Output-panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dette panelet viser innstillingene for _currently selected laser_ (vist med tallet øverst). Endre hvilken laser som er valgt nå ved å bruke _tab_-tasten, trykke på en talltast, klikke på et lasernummer i panelet _Laser Overview_ eller i _output view._

* **Number button** armerer og deaktiverer laseren. Hvis den er rød, er laseren armert.
* **Brightness** justerer laserens lysstyrke uavhengig av de andre laserne (og kombineres med innstillingen _global brightness_ – dvs. hvis begge er på 50 %, vil laseren være på 25 %).
* **Test Pattern** slår på et testmønster bare for denne laseren (overstyrer den globale testmønsterinnstillingen)
* **Orientation** korrigerer for lasere som er rigget sidelengs eller opp-ned.
* **Flip Horizontal and Flip Vertical** reverserer outputen fra laseren. Nyttig for output-korrigering på lasere med inkonsistent kabling.
* **Copy Laser Settings** åpner et panel som lar deg kopiere ulike innstillinger fra denne laseren til andre.

### Scanner-innstillinger

Displaylasere fungerer ved å flytte én enkelt laserstråle ekstremt raskt og slå den av og på for å tegne former i luften. Det du ser som linjer, former og bilder, er egentlig strålen som tegner baner raskere enn øynene dine kan følge.

En punktstrøm er dataene som forteller laseren hvor den skal flytte seg neste gang, og når strålen skal være på eller av. I Liberation konverteres clips til denne punktstrømmen i sanntid når de sendes til laserne.

Liberation gir deg detaljert kontroll over hvordan denne punktstrømmen genereres, slik at du kan balansere jevnhet, lysstyrke og ytelse for hver laser.

{% hint style="info" %}
Hvis du er vant til eldre laserprogramvare som baserer seg på forhåndsberegnede punktstrømmer, kan denne tilnærmingen føles annerledes i starten. Sanntidsgenerering av punkter gjør imidlertid at det samme innholdet kan optimaliseres ulikt for hver laser. Dette gjør det enklere å jobbe med flere lasere som har forskjellig scanner-hastighet eller kvalitet, uten å duplisere eller bygge om innhold. Det holder også clip-filer svært små, og det er derfor hele standard clip deck i Liberation bare er noen få megabyte i stedet for gigabyte.
{% endhint %}

De grunnleggende scanner-innstillingene er:

* **Speed** er scanner-hastigheten, dvs. hvor raskt laseren beveger seg for å tegne former. Dette tilsvarer å justere punktfrekvensen i tradisjonell laserprogramvare, men i Liberation kan du endre hvor raskt laseren beveger seg _uavhengig av punktfrekvensen_. Du skal normalt ikke trenge å justere dette.
* **Scanner sync** (noen ganger kalt _blank shift_, tidligere Colour Shift) Scannerne flytter laseren svært raskt, men vanligvis er endringen i lysstyrke og farge ute av synk med bevegelsen. Dette vises som små flimrende "haler" av lys i kanten av beams og linjer. Bruk denne justeringen for å få bevegelse og farge i synk med hverandre. Se [laser-settings](../setting-up/laser-settings/ "mention")

De andre avanserte scanner-innstillingene dekkes i kapitlet [advanced](../advanced/ "mention").

### Soner

For en fullstendig veiledning i å sette opp og soneinndele lasere, se: [setting-up-lasers.md](../setting-up/setting-up-lasers.md "mention")
