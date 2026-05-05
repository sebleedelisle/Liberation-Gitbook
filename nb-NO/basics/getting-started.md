# ✅ Hurtigstartveiledning

## Introduksjon

Velkommen til **Liberation** – neste generasjon laserprogramvare.

Liberation er kraftig og avansert moderne programvare. Den er bygget på grunnprinsipper for brukervennlighet og driftssikkerhet, slik at du får frihet til å uttrykke kreativiteten din. Den er rask, effektiv og sømløs. Følg denne _hurtigstartveiledningen_ for å komme i gang på kort tid!

### Håndtere lasere

Liberation er fleksibelt nok til at du kan sette opp lasere og visualisere dem uten at noen faktiske lasere er koblet til. Når du er klar, kan du sømløst tilordne hver Output til en laser controller.

{% hint style="info" %}
Du kan sette opp og visualisere så mange lasere du vil i Liberation. Lisensnivåene (Hobbyist, Pro osv.) begrenser bare hvor mange lasere du kan sette i _armed_-tilstand. Det betyr at du kan designe lasershow med 100 lasere selv med en gratis lisens. Du trenger først å oppgradere når du faktisk skal kjøre showet på ekte lasere.
{% endhint %}

Som standard er det 8 lasere plassert horisontalt, men du kan tilpasse dette slik du vil. Det er sannsynligvis best å beholde denne standarden mens du blir kjent med programvaren. Senere kan du justere den slik at den passer til maskinvareoppsettet ditt. (Se [Sette opp prosjektet](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Viktig: Før du setter noen lasere i _armed_-tilstand, må du sørge for at du forstår risikoen og gå nøye gjennom kapittelet [Sette opp lasere](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Oversikt over programvaren

### Sikkerhetsstopp

Når du kjører lasere, må du alltid ha en **fysisk nødstoppknapp** tilgjengelig (se [Nødstopp / sikkerhetsinterlocks](../hardware/emergency-stop-interlocks.md "mention")). Hvis du vil sette alt til disarmed uten at det haster like mye, kan du bruke knappen _**DISARM ALL**_, `Escape`-tasten eller _**SESSION**_-tasten på APC40. Du kan også redusere Global Brightness med skjermskyveknappen eller hovedfaderen på APC40.

### Skyveknapper

I Liberation finnes det ulike skyveknapper og kontroller.

{% hint style="info" %}
`Cmd / Ctrl`-klikk på en skyveknapp for å skrive inn en ny verdi hvis du trenger mer presis kontroll enn skyveknappen gir.
{% endhint %}

### Tastatursnarveier

Du finner en komplett liste over tastatursnarveier her: [Tastatursnarveier](../reference/keyboard-shortcuts.md "mention")

### Skjermoppsett

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Usikker på hva en bestemt knapp gjør? Hold musepekeren over den for å se en beskrivelse!
{% endhint %}

#### Meny

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

I menyen finner du alle alternativer for filimport og -eksport, og du kan åpne paneler. Her finner du også valget for å autorisere datamaskinen med abonnementet ditt (i _Liberation -> Authorise/Deauthorise this computer_).

#### Ikonlinje

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Her finner du vanlige oppgaver, som å sette alle lasere til armed eller disarmed, Global Brightness, test pattern og bytte mellom 3D view, Canvas view og Output view.

### Views

Det store området øverst til venstre på skjermen kan vise én av tre hovedvisninger: **3D**, **CANVAS** og **OUTPUT.** Bytt mellom dem med knappene på ikonlinjen, eller bruk `Tab`-tasten for å bytte mellom 3D view og Output view, og deretter videre gjennom hver laser output etter tur.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view viser hvordan laserne dine vil se ut, og kan konfigureres slik at den samsvarer med ditt eget laseroppsett. Klikk og dra for å rotere kameraet, og bruk musehjulet til å bevege deg fremover og bakover. Du finner mange flere alternativer i panelet _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Se [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view brukes til å konfigurere zones og masks for hver laser. Legg merke til det store tallet øverst til venstre, slik at du enkelt ser hvilken laser du jobber med.

Denne visningen representerer hele Output for denne laseren, og hvor hver zone ligger innenfor den. Som standard finnes det bare én zone per laser, men du kan legge til så mange zones som er praktisk fornuftig, og du vil se dem alle i denne visningen.

{% hint style="info" %}
**Hva er en zone?**

En zone er et område innenfor en lasers Output som du kan sende laserinnhold til. Du kan ha mer enn én zone per laser. Den enkleste typen zone er en _beam_ zone, men det finnes også _canvas_ zones og _DMX_ zones. I denne veiledningen fokuserer vi hovedsakelig på beam zones, som vanligvis brukes til å lage atmosfæriske stråleeffekter gjennom luften.
{% endhint %}

Du kan velge laseren du vil redigere, på disse måtene:

* de nummererte knappene i linjen øverst
* trykke på talltasten for laseren du vil velge (_tastene 1-9_)
* `Tab`-tasten for å gå fra én laser til den neste

Legg til en ny laser i oppsettet ved å trykke på _+_-knappen. (Det finnes også en _ADD LASER_-knapp i panelet _Laser Overview_.)

Slett en laser fra oppsettet ved å trykke på den røde ⊖-knappen i panelet _Laser Overview_.

Du kan zoome inn og ut med musehjulet, og klikke og dra hvor som helst der det ikke finnes en zone for å flytte visningen.

Klikk på en zone for å velge den, og juster deretter hjørnepunktene med musen. Hold inne `Alt / Option` mens du drar et hjørne for å gjøre justeringen ikke-uniform. Høyreklikk på zone for å se flere alternativer, inkludert å endre typen zone.

Langs venstre side finnes det en linje med en serie ikonknapper. Hold musepekeren over en knapp for å få en beskrivelse av hva den gjør. Knappene her lar deg legge til beam zones, canvas zones og masks. Det finnes også alternativer for å angi et test pattern bare for denne laseren, sammen med innstillinger for rutenett og snapping.

For mer informasjon, se [Output-visning](../output-view/ "mention").

#### Canvas

Canvas-systemet brukes hovedsakelig til grafikk og arkitektonisk mapping. Du kan fordele komplekse bilder på tvers av flere lasere og perspektivkorrigere hver del. Se [Grafikk og Canvas-systemet](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Selv om det er mulig å styre Liberation med mus og tastatur, er det langt bedre å bruke en APC40 MIDI controller-grensesnitt. Mark 2 er best, men Mark 1 fungerer også.

Se også: [APC40-referanse](../reference/apc40-reference.md "mention")

Liberation støtter også APC Mini og MIDI Fighter Twister. APC40 Mark 2 er fortsatt det beste valget i de fleste tilfeller.&#x20;

### Clips og effekter

{% hint style="info" %}
**Hva er en Clip?**

En Clip er en beholder for laserinnhold i Liberation. Clips kan inneholde beams eller grafiske animasjoner, og de er vanligvis en loop. De kan sendes til hvilken som helst zone eller _Canvas target area_, og trigges med Clip-knappene i Clip Deck.
{% endhint %}

#### Oversikt over Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Dette rutenettet kalles _Clip Deck_, og det er her alle laser-Clips lagres. Det er laget for å mappe direkte til 8 x 5-rutenettet med knapper på APC40.

**Navigere i Clip Deck.**

Du kan rulle Clip Deck mot venstre og høyre med:

* venstre og høyre piltast. Legg til `Cmd / Ctrl` for å rulle én hel side om gangen.
* styreflate: sveip
* mus: hvis musen din har horisontal rulling, kan du bruke den mens musepekeren er over Clip Deck
* rulleknappen på APC40
* APC40 _<- DEVICE ->_-knappene

For å hjelpe deg med å orientere deg finnes det en liten visualisering av Clip Deck langs toppen. Se også [Clips og Clip Deck](../clips/ "mention")

#### Starte og stoppe Clips

Trykk på en Clip-knapp, enten med musen eller med APC40, for å starte en Clip. Trykk på den igjen for å stoppe den. Når du starter en Clip, stopper alle andre Clips med samme farge automatisk, med mindre du holder inne _shift_.

Noen Clips er i _Flash mode_ (som standard de røde), og da stopper de så snart du slipper Clip-knappen.

Knappen _STOP_ stopper alle Clips som kjører for øyeblikket.

#### Angi output zones for Clip

Under Clip-knappene ser du zone-knappene, beam zones 1 til 8 som standard (_BEAM 1_, _BEAM 2_ osv.). Zone-knappene lyser for å vise hvilke zones som er tilordnet Clip som er valgt for øyeblikket.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

To rader under zone-knappene ser du X/Y flip-knappene. Slå disse av eller på for å speilvende Clip horisontalt og vertikalt.

{% hint style="info" %}
Merk at disse zone-tilordningene og X/Y flip-innstillingene er knyttet til selve Clip. De beholdes neste gang du kjører den Clip. De er ikke en global innstilling.
{% endhint %}

Høyreklikk på en Clip for å redigere flere innstillinger for den. Se også [Clip settings](../clips/clip-settings.md "mention")

### Grupper

Du vil se at hver Clip har en farget kantlinje, og denne fargen viser hvilken _gruppe_ den tilhører. Clip-knappene på APC40 lyser også i denne fargen.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Oransje</td></tr><tr><td>Group 3</td><td>Rød</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Grønn</td></tr></tbody></table>

Gruppesystemet er svært fleksibelt, og lar deg:

* la Clips i én gruppe fortsette å kjøre mens du slår Clips i en annen gruppe av og på
* raskt tilordne zones og X/Y flip til alle Clips i en gruppe
* angi _Flash mode_ for en Clip (Group 3 er satt til _Flash mode_ som standard)

Grupper har også innstillinger for transition in/out som kan arves av Clips i gruppen, eller overstyres.

Du kan tilordne hvilken gruppe Clip tilhører med knappene i høyreklikkmenyen. Med APC40 kan du trykke på gruppeknappen og, _mens den fortsatt holdes nede,_ trykke på Clip-knappene.

Endre zone-innstillinger for alle Clips i en gruppe

Med APC40 trykker du på gruppeknappen, og _mens den fortsatt holdes nede,_ bruker du zone- og X/Y-knappene til å slå zone-innstillinger av og på for alle Clips i den gruppen.

Se også [Clip-grupper](../clips/groups.md "mention")

### Effekter

Effektsystemet i Liberation er en kraftig og allsidig måte å endre Clip output i sanntid på. Standard effektknapper 1–8 ligger under zone-knappene.

#### Bruke en effekt

Trykk på en effektknapp for å slå effekten av eller på. Enda bedre er det å bruke APC40-skyveknappene 1–8 til å fade effekter inn og ut.

#### Effektparametere

Bruk rotary controllers 1–8\* til å justere _parameter_ for hver effekt. (Du kan også høyreklikke med musen for å justere level og parameter.) Parameterendringen gjør ulike ting avhengig av hvordan effekten er satt opp. Se listen nedenfor for standardeffektene.

{% hint style="info" %}
De små tallene du ser på effektknappene, viser til _level_ og _parameter_ for effekten. _Level_ styres av faderen på APC40, eller du kan klikke og dra på knappen. Parameter justeres med rotary controls på APC40, eller du kan høyreklikke for å justere med musen.
{% endhint %}

_\*Rotary controllers 1–8 ligger langs toppen på en APC40 Mk2 og øverst til høyre på Mk1. Se også:_ [APC40-referanse](../reference/apc40-reference.md "mention")

#### Standardeffektene

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Legger en kaotisk bevegelse på Clip output. Parameteren justerer mengden/hastigheten på kaoset.
2. **Sine wave** :\
   Forvrenger alt innholdet over en bevegelig sinusbølge. Parameteren justerer bølgelengden.
3. **Rotation** :\
   Roterer alt. Parameteren justerer rotasjonshastigheten.
4. **Horizontal flip** :\
   Klemmer sammen og strekker alt horisontalt. Parameteren justerer hastigheten.
5. **Scale** :\
   Skalerer alt gjentatte ganger fra fullt til null. Parameteren justerer hastigheten.
6. **Hue** :\
Endrer hue for alt, men endrer ikke saturation (dvs. alt som er hvitt forblir hvitt). Parameteren justerer hue.
7. **Saturation and hue** :\
Endrer hue for alt og gjør også fargen fullstendig mettet (dvs. alt som er hvitt endres til fargen). Parameteren justerer hue.
8. **Flash** :\
   Blinker gjentatte ganger brightness for alt fra fullt til null. Parameteren justerer blinkehastigheten.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finnes ytterligere 16 fargeeffekter langs nederste rad for å bruke forhåndsinnstilte hue- og saturation-verdier.

Merk at dette er standardeffektene, men de kan redigeres til å gjøre nesten hva du vil!

#### Hva er _Clip som er valgt for øyeblikket_?

Når du starter en Clip, lyser den for å vise at den er aktiv. Den har også en hvit kantlinje rundt seg, som viser at dette er Clip som er valgt for øyeblikket. Når du slår zone-knapper av eller på, eller justerer Clip-innstillinger, brukes disse på _Clip som er valgt for øyeblikket_.

{% hint style="info" %}
Hvis du vil velge en Clip uten å trigge den, trykker du på `Alt / Option` før du trykker på Clip-knappen. Dette er en god måte å justere zones og andre innstillinger på uten å kjøre den.
{% endhint %}

### Panelet Clip Settings

Bruk panelet _Clip Settings_ til å redigere skalering, X/Y-posisjon og få tilgang til det kraftige systemet for zone delay.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panelet Global Settings

Finn panelet _Global Settings_ for å justere globale Output-innstillinger som påvirker all Output på tvers av alle zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Slå på AUTO RESET for automatisk å tilbakestille alle _Global settings_ når ingen Clips spiller.&#x20;

### Timing

Nesten alle laseroppsetninger har en form for musikalsk lydspor, så timing-systemet i Liberation er basert på tempo i slag per minutt. I _Tempo Panel_ ser du en representasjon av tiden. Hver firkant representerer et slag, og du kan se at de blinker i takt.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Det finnes flere synkroniseringsalternativer, inkludert MIDI clock og Ableton Link. Hvis du kjenner tempoet i musikken, kan du justere det manuelt med skjermskyveknappen eller _Tempo_-knappen på APC40. Du kan også holde takten med musikken ved hjelp av _Tap Tempo_-systemet.

#### Tap Tempo

_Tap Tempo_ er et begrep som ofte brukes i musikkapper, og lar deg tappe i takt med beatet for å angi tempoet mens musikken spiller. Du kan bruke knappen på skjermen, men det anbefales å bruke _T_-tasten eller _Tap Tempo_-knappen på APC40 (eller en fotbryter hvis du foretrekker det).

Trykk på _R_-tasten eller _Metronome_-knappen (APC40) for å tilbakestille tempoet til starten av takten.

Trykk på _Y_-tasten eller drei _Tempo_-knappen (APC40) for å runde tempoet av til et helt tall. Dette kan være nyttig for elektronisk musikk, som ofte har et rundt antall slag per minutt.

### Organisere Clip Deck

For å flytte en Clip i Clip Deck klikker du og drar den til en ny plassering. Mens du drar, kan du bruke piltastene eller rullehjulet/-knappene på APC40 til å rulle mot venstre og høyre.

Hold inne `Alt / Option` mens du drar for å lage en kopi.

`Alt / Option`-klikk på en Clip for å velge den uten å starte den.

`Alt / Option + Shift`-klikk på en Clip for å velge flere, eller klikk og dra utenfor en Clip for å «lasso»-velge.&#x20;

Klikk og dra vil dra ALLE valgte Clips.

For å slette én eller flere Clips kan du enten dra dem ut av Clip Deck (et søppelbøtteikon vises), eller bruke DELETE-knappen fra høyreklikkmenyen for Clip.

### Panelet Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panelet _Laser Overview_ gir deg en rask oversikt over statusen til laserne som kjører for øyeblikket. Den grønne firkanten til høyre viser at laser controller fungerer som den skal. Hvis den blir oransje, har du sporadiske drop-outs, og hvis den blir rød, er den frakoblet. Hvis den er grå, er den ikke koblet til noen controller i det hele tatt.&#x20;

Grafen i midten viser historikken for frame length, og tallet til høyre er gjeldende frame rate. Jo mer komplisert innholdet er, desto lavere blir frame rate (altså mer flimring). Alt under omtrent 25 fps vil begynne å se litt flimrete ut.&#x20;

### Koble til lasere – panelet Controller Assignment

Klikk på knappen _Assign Laser Controllers_ for å åpne panelet _Controller Assignment_. (Dette panelet kan også åpnes via _View -> Controller Assignment_ i menylinjen.)

Her kan du velge hvilke laser outputs som skal gå til hvilke laser controllers. Dra og slipp controllers fra listen til høyre inn i plassene til venstre. Du kan gi controllers nytt navn slik at de samsvarer med laseren de er paret med (bruk knappen med pennikonet).

Les kapittelet [Kontrollertildeling](../setting-up/controller-assignment.md "mention") for mer informasjon.

{% hint style="danger" %}
Før du setter noen lasere i _armed_-tilstand, må du gå gjennom kapittelet [Sette opp lasere](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panelet Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Dette panelet viser innstillingene for _currently selected laser_ (representert av tallet øverst). Endre hvilken laser som er valgt for øyeblikket med _tab_-tasten, ved å trykke på en talltast, ved å klikke på et lasernummer i panelet _Laser Overview_ eller i _Output view._

* **Number button** setter laseren til armed eller disarmed. Hvis den er rød, er laseren armed.
* **Brightness** justerer laserens brightness uavhengig av de andre laserne. Den kombineres med innstillingen _Global Brightness_ – dvs. hvis begge står på 50 %, blir laseren din på 25 %.
* **Test Pattern** slår på et test pattern bare for denne laseren (overstyrer den globale test pattern-innstillingen).
* **Orientation** korrigerer for lasere som er rigget sidelengs eller opp-ned.
* **Flip Horizontal and Flip Vertical** reverserer Output fra laseren. Nyttig for Output-korrigering på lasere med ulik kabling.
* **Copy Laser Settings** åpner et panel som lar deg kopiere ulike innstillinger fra denne laseren til andre.

### Scanner settings

Displaylasere fungerer ved å flytte én enkelt laserstråle ekstremt raskt og slå den av og på for å tegne former i luften. Det du ser som linjer, former og bilder, er egentlig strålen som tegner baner raskere enn øynene dine klarer å følge.

En point stream er dataene som forteller laseren hvor den skal flytte seg videre, og når strålen skal være på eller av. I Liberation konverteres Clips til denne point stream i sanntid når de sendes til laserne.

Liberation gir deg detaljert kontroll over hvordan denne point stream genereres, slik at du kan balansere jevnhet, brightness og ytelse for hver laser.

{% hint style="info" %}
Hvis du er vant til eldre laserprogramvare som baserer seg på forhåndsberegnede point streams, kan denne tilnærmingen føles annerledes i starten. Sanntidsgenerering av punkter gjør det imidlertid mulig å optimalisere det samme innholdet ulikt for hver laser. Dette gjør det enklere å arbeide med flere lasere som har ulik scanner-hastighet eller kvalitet, uten å duplisere eller bygge innhold på nytt. Det holder også Clip-filer svært små, og derfor er hele standard Clip Deck i Liberation bare noen få megabyte i stedet for gigabyte.
{% endhint %}

De grunnleggende scanner-innstillingene er:

* **Speed** er scanner-hastigheten, altså hvor raskt laseren beveger seg rundt for å tegne former. Dette tilsvarer å justere point rate i tradisjonell laserprogramvare, men i Liberation kan du endre hvor raskt laseren beveger seg _uavhengig av point rate._ Du skal normalt ikke trenge å justere dette.
* **Scanner sync** (noen ganger kalt _blank shift, tidligere Colour Shift_) Scannere beveger laseren svært raskt, men vanligvis er endringen i brightness og farge ute av synk med bevegelsen. Dette viser seg som små flimrende «haler» av lys i kanten av beams og linjer. Bruk denne justeringen for å få bevegelse og farge i synk med hverandre. Se [Laser Settings](../setting-up/laser-settings.md "mention")

De andre avanserte scanner-innstillingene dekkes i kapittelet [Avansert](../advanced/ "mention").

### Zoning

For en komplett veiledning til å sette opp og bruke zones for lasere, se: [Sette opp lasere](../setting-up/setting-up-lasers.md "mention")
