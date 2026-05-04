---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Hurtigstartveiledning

## Introduksjon

Velkommen til **Liberation** – neste generasjon programvare for lasershow.

Liberation er kraftig og avansert moderne programvare. Den er bygget på grunnleggende prinsipper for brukervennlighet og driftssikkerhet, slik at du får frihet til å uttrykke kreativiteten din. Den er rask, effektiv og sømløs. Følg denne _hurtigstartveiledningen_ for å komme i gang på kort tid!

### Administrere lasere

Liberation er fleksibelt nok til at du kan sette opp lasere og visualisere dem uten at noen fysiske lasere er koblet til. Når du er klar, kan du deretter sømløst tilordne hver utgang til en laserkontroller.

{% hint style="info" %}
Du kan sette opp og visualisere så mange lasere du vil i Liberation. Lisensnivåene (Hobbyist, Pro osv.) begrenser bare hvor mange lasere du kan _armere._ Det betyr at du kan designe lasershow med 100 lasere selv med en gratis lisens. Du trenger bare å oppgradere når du faktisk skal kjøre showet på ekte lasere.
{% endhint %}

Som standard er det 8 lasere fordelt horisontalt, men du kan tilpasse dette akkurat slik du vil. Det er sannsynligvis best å beholde standardoppsettet mens du blir kjent med programvaren, og så kan du senere justere det slik at det passer maskinvareoppsettet ditt. (Se [Sette opp prosjektet ditt](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Viktig: Før du armerer noen lasere, må du sørge for at du forstår risikoen og gå nøye gjennom kapittelet [Oversikt over prosessen for laseroppsett](setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Oversikt over programvaren

### Sikkerhetsavstenging

Når du bruker lasere, må du alltid ha en **fysisk nødstoppknapp** tilgjengelig (se [Nødstopp / sikkerhetsinterlocks](hardware/emergency-stop-interlocks.md "mention")). Hvis du vil deaktivere alt uten samme hastverk, kan du bruke knappen _**DISARM ALL**_ eller `Escape`-tasten (eller _**SESSION**_-tasten på APC40). Du kan også redusere den globale lysstyrken med skyvebryteren på skjermen eller hovedfaderen på APC40.

### Skyvebrytere

I Liberation finnes det ulike skyvebrytere og kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klikk på en skyvebryter for å skrive inn en ny verdi hvis du trenger mer presis kontroll enn skyvebryteren gir.
{% endhint %}

### Tastatursnarveier

Du finner en fullstendig liste over tastatursnarveier her: [Tastatursnarveier](reference/keyboard-shortcuts.md "mention")

### Skjermoppsett

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Usikker på hva en bestemt knapp gjør? Hold musepekeren over den for å få en beskrivelse!
{% endhint %}

#### Meny

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menyen er stedet der du finner alle alternativer for import/eksport av filer og åpner paneler. Her finner du også valget for å autorisere datamaskinen med abonnementet ditt (i _Liberation -> Authorise/Deauthorise this computer_).

#### Ikonlinje

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Her finner du vanlige oppgaver, som å armere/dearmere alle lasere, global lysstyrke, testmønster og bytte mellom visningene 3D, Canvas og Output.

### Visninger

Det store området øverst til venstre på skjermen kan være én av 3 hovedvisninger: **3D**, **CANVAS** og **OUTPUT.** Bytt mellom dem med knappene på ikonlinjen (eller bruk `Tab`-tasten for å bytte mellom 3D- og OUTPUT-visningene, og fortsett deretter å tabbe gjennom hver laserutgang etter tur).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D-visning

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view viser hvordan laserne dine vil se ut, og kan konfigureres slik at den samsvarer med ditt eget laseroppsett. Klikk og dra for å rotere kameraet, og bruk musehjulet for å bevege deg fremover og bakover. Du finner mange andre alternativer i panelet _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3D Visualiser](setting-up/3d-visualiser.md "mention").

#### Output-visning

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output-visningen brukes til å konfigurere soner og masker for hver laser. (Legg merke til det store tallet øverst til venstre, slik at du enkelt ser hvilken laser du er på!)

Denne visningen er en representasjon av hele utgangen til denne laseren, og hvor hver sone ligger innenfor den. Som standard finnes det bare én sone per laser, men du kan legge til så mange soner som det er praktisk fornuftig å bruke, og du vil se alle i denne visningen.

{% hint style="info" %}
**Hva er en sone?**

En sone er et område innenfor en lasers utgang som du kan sende laserinnhold til. Du kan ha mer enn én sone per laser. Den enkleste sonetypen er en _beam_-sone, men det finnes også _canvas_-soner og _DMX_-soner. I denne veiledningen fokuserer vi mest på beam-soner, som vanligvis brukes til å lage atmosfæriske stråleeffekter gjennom luften.
{% endhint %}

Du kan velge laseren du vil redigere, på en av disse måtene:

* de nummererte knappene i linjen øverst
* trykke på talltasten for laseren du vil bruke (_1-9 keys_)
* `Tab`-tasten for å gå videre fra én til den neste

Legg til en ny laser i oppsettet ved å trykke på _+_-knappen. (Det finnes også en _ADD LASER_-knapp i panelet _Laser Overview_)

Slett en laser fra oppsettet ved å trykke på den røde ⊖-knappen i panelet _Laser Overview_.

Du kan zoome inn og ut med rullehjulet på musen, og klikke og dra hvor som helst der det ikke finnes en sone for å flytte visningen.

Klikk på en sone for å velge den, og juster deretter hjørnepunktene med musen. Bruk `Alt / Option`-tasten mens du drar et hjørne for å gjøre det ikke-uniformt. Høyreklikk på sonen for å se flere alternativer, blant annet for å endre sonetype.

Langs venstre side finnes en linje med en serie ikonknapper. Hold musepekeren over en knapp for å få en beskrivelse av hva den gjør. Knappene her lar deg legge til beam-soner, canvas-soner og masker. Det finnes også alternativer for å angi et testmønster bare for denne laseren, sammen med innstillinger for rutenett og festing.

Du finner mer informasjon i [Output-visning](output-view/ "mention").

#### Canvas

Canvas-systemet brukes hovedsakelig til grafikk og arkitektonisk mapping. Du kan fordele komplekse bilder over flere lasere og perspektivkorrigere hver del. Se [Grafikk og Canvas-systemet](graphics-and-the-canvas-system/ "mention").

### APC40 MIDI-kontroller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Selv om det er mulig å styre Liberation med mus og tastatur, er det mye bedre å bruke et APC40 MIDI-kontrollgrensesnitt (Mark 2 er best, men Mark 1 fungerer også).

Se også: [APC40-referanse](reference/apc40-reference.md "mention")

Liberation støtter også APC Mini og MIDI Fighter Twister. APC40 Mark 2 er fortsatt det beste alternativet i de fleste tilfeller.

### Clips og effekter

{% hint style="info" %}
**Hva er en clip?**

En clip er en beholder for laserinnhold i Liberation. Clips kan inneholde beams eller grafiske animasjoner, og de er vanligvis en loop. De kan sendes til en hvilken som helst sone (eller et _Canvas target area_) og trigges med clip-knappene i Clip Deck.
{% endhint %}

#### Oversikt over Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dette rutenettet kalles _Clip Deck_, og det er her alle laser-clips lagres. Det er laget for å mappe direkte til rutenettet med 8 x 5 knapper på APC40.

**Navigere i Clip Deck.**

Du kan rulle Clip Deck mot venstre og høyre med:

* Venstre og høyre piltast. Legg til `Cmd / Ctrl` for å rulle én hel side om gangen.
* Styreflate: Sveip
* Mus: Hvis musen har siderulling, kan du bruke den mens musepekeren er over Clip Deck
* APC40-rulleknott
* APC40 _<- DEVICE ->_-knapper

For å gjøre det lettere å orientere seg finnes det en mini-visualisering av Clip Deck langs toppen. Se også [Clips og Clip Deck](clips/ "mention")

#### Starte og stoppe clips

Trykk på en clip-knapp (enten med musen eller med APC40) for å starte en clip. Trykk på den igjen for å stoppe den. Når du starter en clip, stopper alle andre clips med samme farge automatisk, med mindre du holder inne _shift_.

Noen clips er i _Flash mode_ (som standard de røde). Da stopper de så snart du slipper clip-knappen.

Knappen _STOP_ stopper alle clips som kjører.

#### Angi utgangssoner for clipen

Under clip-knappene ser du soneknappene, beam-soner 1 til 8 som standard (_BEAM 1_, _BEAM 2_ osv.). Soneknappene lyser for å vise hvilke soner som er tilordnet den valgte clipen.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

To rader under soneknappene ser du X/Y flip-knappene. Slå disse av eller på for å speilvende clipen horisontalt og vertikalt.

{% hint style="info" %}
Merk at disse sonetildelingene og X/Y flip-innstillingene er knyttet til selve clipen. De beholdes neste gang du kjører den clipen. De er ikke en global innstilling.
{% endhint %}

Høyreklikk på en Clip for å redigere flere innstillinger for den. Se også [Clip settings](clips/clip-settings.md "mention")

### Grupper

Du vil legge merke til at hver clip har en farget ramme, og denne fargen viser hvilken _gruppe_ den tilhører. Clip-knappene på APC40 lyser også i denne fargen.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Red</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Green</td></tr></tbody></table>

Gruppesystemet er svært fleksibelt og lar deg:

* Holde clips i én gruppe gående mens du slår grupper i en annen av og på
* Raskt tilordne soner og X/Y flips til alle clips i en gruppe
* Angi _Flash mode_ for en clip (Group 3 er satt til _Flash mode_ som standard)

Grupper har også innstillinger for inn-/utoverganger som kan arves av clipene, eller overstyres.

Du kan tilordne clipens gruppe med knappene i høyreklikkmenyen, eller med APC40 ved å trykke på gruppeknappen og, _mens den fortsatt holdes inne,_ trykke på clip-knappene.

Endre soneinnstillinger for alle clips i en gruppe

Med APC40 trykker du på gruppeknappen, og _mens den fortsatt holdes inne,_ bruker du sone- og X/Y-knappene til å slå soneinnstillinger av eller på for alle clips i den gruppen.

Se også [Clip-grupper](clips/groups.md "mention")

### Effekter

Effektsystemet i Liberation er en kraftig og allsidig måte å endre clip-utgangen på i sanntid. Standard effektknapper 1–8 ligger under soneknappene.

#### Bruke en effekt

Trykk på en effektknapp for å slå effekten av eller på, eller enda bedre: bruk APC40-skyvebryterne 1–8 for å fade effektene inn og ut.

#### Effektparametere

Bruk dreiekontrollene 1–8\* til å justere _parameteren_ for hver effekt. (Du kan også høyreklikke med musen for å justere nivå og parameter). Parameterendringen gjør ulike ting avhengig av hvordan effekten er satt opp. Se listen nedenfor for standardeffektene.

{% hint style="info" %}
De små tallene du ser på effektknappene, viser til _level_ og _parameter_ for effekten. _Level_ styres av faderen på APC40, eller du kan klikke og dra på knappen. Parameteren justeres med dreiekontrollene på APC40, eller du kan høyreklikke for å justere med musen.
{% endhint %}

_\*Dreiekontroller 1–8 ligger langs toppen av en APC40 Mk2 og øverst til høyre på Mk1. Se også:_ [APC40-referanse](reference/apc40-reference.md "mention")

#### Standardeffektene

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Legger en kaotisk bevegelse på clip-utgangen. Parameteren justerer mengden/hastigheten på kaoset.
2. **Sine wave** :\
   Forvrenger alt innhold over en bevegelig sinusbølge. Parameteren justerer bølgelengden.
3. **Rotation** :\
   Roterer alt rundt. Parameteren justerer rotasjonshastigheten.
4. **Horizontal flip** :\
   Klemmer og strekker alt horisontalt. Parameteren justerer hastigheten.
5. **Scale** :\
   Skalerer alt gjentatte ganger fra fullt til null. Parameteren justerer hastigheten.
6. **Hue** :\
Endrer nyansen på alt, men endrer ikke metningen (dvs. alt som er hvitt forblir hvitt). Parameteren justerer nyansen.
7. **Saturation and hue** :\
Endrer nyansen på alt og metter også fargen helt (dvs. alt som er hvitt endres til fargen). Parameteren justerer nyansen.
8. **Flash** :\
   Blinker lysstyrken på alt gjentatte ganger fra fullt til null. Parameteren justerer blinkehastigheten.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finnes ytterligere 16 fargeeffekter langs nederste rad for å bruke forhåndsdefinerte verdier for nyanse og metning.

Merk at dette er standardeffektene, men de kan redigeres til å gjøre nesten hva som helst!

#### Hva er den _«valgte clipen»_?

Når du starter en clip, lyser den for å vise at den er aktiv. Den har også en hvit ramme rundt seg, som viser at dette er den _valgte_ clipen. Når du slår soneknapper av eller på eller justerer clip-innstillingene, brukes disse på den _valgte clipen._

{% hint style="info" %}
For å velge en clip uten å trigge den, trykker du på `Alt / Option`-tasten før du trykker på clip-knappen. Dette er en god måte å justere soner og andre innstillinger på uten å kjøre den.
{% endhint %}

### Clip Settings-panel

Bruk panelet _Clip Settings_ til å redigere skalering, X/Y-posisjon og få tilgang til det kraftige sonedelay-systemet.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings-panel

Finn panelet _Global Settings_ for å justere globale utgangsinnstillinger som påvirker all utgang i alle soner.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå på AUTO RESET for automatisk å tilbakestille alle _Global settings_ når ingen clips spiller.

### Timing

Nesten alle laseroppsetninger har en form for musikalsk lydspor, så timingsystemet i Liberation er basert på et tempo i slag per minutt. I _Tempo Panel_ kan du se en representasjon av tiden. Hver rute representerer et slag, og du kan se at de blinker i takt.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Det finnes flere synkroniseringsalternativer, blant annet MIDI clock og Ableton Link. Hvis du kjenner tempoet på musikken, kan du justere det manuelt med skyvebryteren på skjermen eller APC40 Tempo-knotten, men du kan også holde takten med musikken ved å bruke _Tap Tempo_-systemet.

#### Tap Tempo

_Tap Tempo_ er et begrep som ofte brukes i musikkapper, og det lar deg tappe i takt med beatet for å angi tempoet mens musikken spiller. Du kan bruke knappen på skjermen, men det anbefales å bruke _T_-tasten eller _Tap Tempo_-knappen på APC40 (eller til og med en fotbryter hvis du foretrekker det).

Trykk på _R_-tasten eller _Metronome_-knappen (APC40) for å tilbakestille tempoet til begynnelsen av takten.

Trykk på _Y_-tasten eller vri på _Tempo_-knotten (APC40) for å runde tempoet av til et helt tall. Dette kan være nyttig for elektronisk musikk, som ofte har et rundt antall slag per minutt.

### Organisere Clip Deck

For å flytte en clip i Clip Deck klikker du og drar den til en ny posisjon. Mens du drar, kan du bruke piltastene (eller rullehjulet/knappene på APC40) til å rulle mot venstre og høyre.

Trykk på `Alt / Option`-tasten mens du drar for å lage en kopi.

`Alt / Option`-klikk på en clip for å velge den uten å starte den.

`Alt / Option + Shift`-klikk på en clip for å velge flere, eller klikk og dra utenfor en clip for å velge med «lasso».

Klikk og dra vil dra ALLE valgte clips.

For å slette én eller flere Clips kan du enten dra dem ut av Clip Deck (et søppelbøtteikon vises) eller bruke DELETE-knappen fra høyreklikkmenyen for Clip-en.

### Laser Overview-panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelet _Laser overview panel_ gir deg en rask oversikt over statusen til laserne som kjører. Den grønne firkanten til høyre viser at laserkontrolleren er fornøyd. Hvis den blir oransje, har du sporadiske utfall, og hvis den er rød, er den frakoblet. Hvis den er grå, er den ikke koblet til en kontroller i det hele tatt.

Grafen i midten viser historikk for rammelengder, og tallet til høyre er gjeldende bildefrekvens. Jo mer komplisert innholdet er, desto lavere blir bildefrekvensen (dvs. mer flimring). Alt under omtrent 25 fps begynner å se litt flimrete ut.

### Koble til lasere – Controller Assignment-panel

Klikk på knappen _Assign Laser Controllers_ for å åpne panelet _Controller Assignment_. (Dette panelet kan også åpnes via _View -> Controller Assignment_ i menylinjen).

Her kan du velge hvilke laserutganger som skal gå til hvilke laserkontrollere. Dra og slipp kontrollere fra listen til høyre inn i sporene til venstre. Du kan gi kontrollerne nye navn slik at de samsvarer med laseren de er paret med (bruk knappen med pennikonet).

Les kapittelet [Kontrollertildeling](setting-up/controller-assignment.md "mention") for mer informasjon.

{% hint style="danger" %}
Før du armerer noen lasere, må du sørge for å gå gjennom kapittelet [Oversikt over prosessen for laseroppsett](setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Laser Output-panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dette panelet viser innstillingene for den _valgte laseren_ (representert av tallet øverst). Endre hvilken laser som er valgt, med _tab_-tasten, ved å trykke på en talltast, klikke på et lasernummer i panelet _Laser Overview_ eller i _output view._

* **Number button** armerer og dearmerer laseren. Hvis den er rød, er laseren armert.
* **Brightness** justerer laserens lysstyrke uavhengig av de andre laserne (og den kombineres med innstillingen _global brightness_ – dvs. hvis begge står på 50 %, vil laseren din være på 25 %).
* **Test Pattern** slår på et testmønster bare for denne laseren (overstyrer den globale testmønsterinnstillingen)
* **Orientation** korrigerer for lasere som er rigget sidelengs eller opp-ned.
* **Flip Horizontal and Flip Vertical** reverserer laserens utgang. Nyttig for utgangskorrigering på lasere med inkonsekvent kabling.
* **Copy Laser Settings** åpner et panel som lar deg kopiere ulike innstillinger fra denne laseren til andre.

### Scanner-innstillinger

Displaylasere fungerer ved å flytte én enkelt laserstråle ekstremt raskt og slå den av og på for å tegne former i luften. Det du ser som linjer, former og bilder, er egentlig strålen som følger baner raskere enn øynene dine kan oppfatte.

En punktstrøm er dataene som forteller laseren hvor den skal flytte seg videre, og når strålen skal være på eller av. I Liberation konverteres clips til denne punktstrømmen i sanntid mens de sendes til laserne.

Liberation gir deg detaljert kontroll over hvordan denne punktstrømmen genereres, slik at du kan balansere jevnhet, lysstyrke og ytelse for hver laser.

{% hint style="info" %}
Hvis du er vant til eldre laserprogramvare som er avhengig av forhåndsberegnede punktstrømmer, kan denne tilnærmingen føles annerledes i starten. Sanntidsgenerering av punkter gjør imidlertid at det samme innholdet kan optimaliseres forskjellig for hver laser. Dette gjør det enklere å jobbe med flere lasere som har ulik scannerhastighet eller kvalitet, uten å duplisere eller bygge om innhold. Det holder også clip-filene svært små, og derfor er hele standard Clip Deck i Liberation bare noen få megabyte i stedet for gigabyte.
{% endhint %}

De grunnleggende scanner-innstillingene er:

* **Speed** er scannerhastigheten, dvs. hvor raskt laseren beveger seg rundt for å tegne former. Dette tilsvarer å justere punktraten i tradisjonell laserprogramvare, men i Liberation kan du endre hvor raskt laseren beveger seg _uavhengig av punktraten._ Du skal normalt ikke trenge å justere dette.
* **Scanner sync** (noen ganger kalt _blank shift, tidligere Colour Shift_) Scannerne beveger laseren svært raskt, men vanligvis er endringer i lysstyrke og farge ute av synk med bevegelsen. Dette viser seg som små flimrende «haler» av lys langs kanten av stråler og linjer. Bruk denne justeringen for å få bevegelse og farge i synk med hverandre. Se [Innstillingspanelet Laser output](setting-up/laser-settings.md "mention")

De andre avanserte scanner-innstillingene dekkes i kapittelet [Avansert](advanced/ "mention").

### Soning

Du finner en fullstendig veiledning for oppsett og soning av lasere her: [Oversikt over prosessen for laseroppsett](setting-up/setting-up-lasers.md "mention")
