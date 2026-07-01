---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Vanlige spørsmål

## Maskinvare

#### **Kjører Liberation på Windows?**

Ja – Liberation har full støtte for **Windows 10 og 11 (64-bit)**, med nøyaktig de samme funksjonene som Mac-versjonen. Alle utgivelser kommer samtidig for begge plattformer.

#### **Kjører Liberation på Mac**

Ja – Liberation har full støtte for **Mac (macOS 12 Monterey og nyere)**, med samme funksjonsnivå som Windows-versjonen. Alle oppdateringer utgis samtidig.

#### **Hva er minimumskravene til datamaskinen?**

Det avhenger av hvor mange lasere du vil styre. Hvis du bare kjører noen få lasere, klarer du deg fint med en maskin med lavere spesifikasjoner. Alle Mac-maskiner med Apple Silicon fungerer svært godt, og bør kunne styre opptil 100 lasere. Hvis du kjører komplekse show der mye står på spill, anbefaler vi den beste maskinen du har råd til.

#### **Hvor mange lasere kan jeg styre med Liberation?**

Liberation kan kjøre mange lasere fra én datamaskin. Det er testet med over 100 laserkontrollere, så svaret avhenger av:

* CPU-en i datamaskinen
* nettverkshastigheten
* lisensnivået ditt

#### **Hvilke MIDI-kontrollere kan jeg bruke?**

Liberation er utviklet og optimalisert rundt den populære APC40 Mk2 MIDI-kontrolleren. Det fungerer også med APC40 Mk1. Se [Live MIDI-kontrollere](midi-control/live-control-with-the-apc40.md "mention")

Liberation støtter også APC Mini og MIDI Fighter Twister. APC40 Mk2 er fortsatt den mest komplette referansekontrolleren.

Det finnes også et MIDI Send/Receive-system som gir ekstra MIDI-kontroll. Se [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Se [MIDI-kontroll](midi-control/ "mention") for mer informasjon.

#### **Kan jeg bruke det med hvilken som helst MIDI-kontroller?**

For andre kontrollere kan du bruke MIDI Send/Receive-systemet eller en MIDI-oversetter som kan sende Liberations standard MIDI-meldinger. Søk i [forumet](https://forum.liberationlaser.com) etter råd om dette oppsettet, men i praksis er APC40 Mk2 fortsatt det beste alternativet for de fleste live-show.

## Laserkontrollere

#### **Hvilke laserkontrollere er kompatible med Liberation?**

* [Ether Dream (anbefalt)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury fra X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (du må kanskje oppdatere fastvaren)
* LaserCube USB (og LaserDock)
* LaserCube-nettverksprotokoll (med kablet tilkobling)
* AVB slik det brukes av [LASollinger-lasere](https://laseranimation.com/en/) (for øyeblikket kun macOS under testing)

Se [Kompatible lasere og kontrollere (DAC-er)](hardware/compatible-lasers-and-controllers-dacs.md "mention") for mer informasjon

#### **Hvorfor støtter dere ikke laserkontrollere fra \[annet merke]?**

For å bidra til bedre samspill mellom programvare og maskinvare støtter Liberation bare DAC-er som har en publisert kommunikasjonsprotokoll. Jeg mener dette er den beste veien videre for laserbransjen.

#### **Hvordan vet jeg om laseren min kan brukes med Liberation?**

Hvis laseren din har én av følgende, kan du bruke den med Liberation:

* En ekstern **ILDA-inngang** – en 25-pinners D-kontakt, brukt sammen med en kompatibel ekstern kontroller.
* En internt installert **Ether Dream**.
* En hvilken som helst **LaserCube** (fungerer med både USB- og Wi-Fi-LaserCube).
* En **X-Laser-enhet med innebygd Mercury-system** (i Ether Dream-modus).
* En **LaserAnimation Sollinger-projektor med innebygd AVB** (kun macOS, krever AVB-kompatible nettverksenheter, for øyeblikket under testing).

Se [Kompatible lasere og kontrollere (DAC-er)](hardware/compatible-lasers-and-controllers-dacs.md "mention") for mer informasjon

#### **Kan jeg bruke Liberation med LaserCube-en min?**

Ja, Liberation fungerer direkte med alle LaserCube. Se [LaserCube](hardware/lasercube.md "mention")

## Lisenser

#### **Hva koster en lisens?**

Se [butikksiden](https://liberationlaser.com/shop) for gjeldende priser.

#### **Hva er begrensningene mellom lisensnivåene?**

Se [butikksiden](https://liberationlaser.com/shop) for gjeldende lisensalternativer.

Merk at du kan sette opp, forhåndsvise og designe show med så mange lasere du vil på **alle** nivåer, også gratisnivået. Det finnes ingen andre begrensninger enn antallet lasere du kan _aktivere for output_. Alle andre Liberation-funksjoner er tilgjengelige for alle.

#### **Kan jeg oppgradere til et nytt nivå?**

Du kan oppgradere til et høyere nivå når som helst. Du får en delvis refusjon for gjenværende tid i den nåværende betalte perioden, og det nye lisensnivået starter umiddelbart. Se [Oppgradere / nedgradere lisensen](installation/upgrade-downgrade-your-license.md "mention")

#### **Kan jeg nedgradere lisensen min?**

Du kan nedgradere når som helst, men endringen trer i kraft ved slutten av den nåværende betalte perioden. Se [Oppgradere / nedgradere lisensen](installation/upgrade-downgrade-your-license.md "mention")

#### **Kan jeg sette lisensbetalingene på pause?**

Ja. Lisensen kan settes på pause fra neste abonnementsdato og startes igjen når som helst. Dette er nyttig hvis du bruker programvaren periodevis, og du trenger ikke å legge inn kortopplysningene på nytt. Se [Sette betalinger på pause eller avslutte abonnementet](installation/cancel-your-subscription.md "mention")

#### **Hvordan avslutter jeg lisensen min permanent?**

Du kan avslutte den gjentakende lisensen når som helst, og den deaktiveres automatisk ved slutten av den nåværende betalte perioden. Se [Sette betalinger på pause eller avslutte abonnementet](installation/cancel-your-subscription.md "mention")

#### **Hvordan autoriserer jeg datamaskinen med lisensen min?**

Når du har kjøpt en lisens, kan du autorisere datamaskinen i selve Liberation-programvaren. Du ser en _Authorise_-knapp på _About_-skjermen som ber deg logge inn på nettstedet. Følg instruksjonene på skjermen for å fullføre autoriseringen. Se [Autorisering og avautorisering](installation/authorising-and-de-authorising.md "mention")

#### **Hvor ofte må jeg koble datamaskinen til internett?**

Hver gang en gjentakende betalt lisens fornyes, må du koble Liberation til internett for å oppdatere den interne lisensen. For en lisens med månedlig automatisk fornyelse må du altså koble til hver måned.

#### **Hva skjer hvis jeg ikke kan koble datamaskinen til internett etter neste betaling?**

For gjentakende betalte måneds lisenser gir Liberation vanligvis en frist på 7 dager etter at den betalte lisensen er fornyet, slik at du kan koble til internett og oppdatere den interne lisensen. Etter denne perioden går Liberation tilbake til _Free_-modus.

#### **Hva skjer hvis kredittkortet mitt utløper?**

Du får en e-post fra betalingsleverandøren vår, og du må oppdatere kortopplysningene dine. Logg inn på nettstedet og bruk _UPDATE CARD DETAILS_ på lisenssiden, eller _Update_ under _Billing and payments_. Du må gjøre dette innen fristen for å unngå å miste tilgang til betalte funksjoner.

#### **Hvor mange datamaskiner kan jeg installere Liberation på?**

Du kan installere Liberation på så mange datamaskiner du vil. Lisensautorisering kreves bare for å aktivere laser-/DMX-output, og lisensnivået ditt bestemmer hvor mange datamaskiner som kan være autorisert for output samtidig. Se [Slik fungerer lisensiering](installation/how-licensing-works.md "mention")

#### **Hvordan flytter jeg lisensen min fra én datamaskin til en annen?**

* Åpne Liberation på datamaskinen du ikke vil bruke lenger
* Sørg for at du er koblet til internett, og klikk på _De-authorise this computer_-knappen på _About_-skjermen
* Åpne deretter Liberation på den nye datamaskinen
* Klikk på _Authorise this computer_-knappen på _About_-skjermen.
* Nettstedet åpnes. Logg inn og følg instruksjonene på skjermen for å fullføre autoriseringen

Du kan også avautorisere en datamaskin du ikke lenger har tilgang til, eksternt (med noen begrensninger). Se [Autorisering og avautorisering](installation/authorising-and-de-authorising.md "mention")

#### **Kan jeg avautorisere Liberation på en datamaskin som er mistet eller stjålet?**

Du kan avautorisere datamaskinen via nettstedet. Hvis Liberation-installasjonen ikke har vært på nett siden siste lisensoppdatering, kan dette gjøres umiddelbart.

Hvis ikke trer avautoriseringen i kraft når lisensen oppdateres neste gang, eller når datamaskinen kobler til internett – avhengig av hva som skjer først. Hvis du raskt trenger å autorisere en ny datamaskin, kontakter du kundestøtte.

### Bruke Liberation

#### Standardoppsettet har 8 lasere – hvordan endrer jeg dette?

Se [Sette opp prosjektet ditt](setting-up/setting-up-your-project.md "mention") og [Legge til / fjerne lasere](setting-up/adding-removing-lasers.md "mention")

#### Kan jeg kopiere zone-innstillinger fra én laser til de andre?

Ja! Se [Kopiere zones mellom lasere](output-view/copy-zones-between-lasers.md "mention")

#### Kan jeg skrive inn et tall i stedet for å bruke en skyveknapp?

Ja. `Cmd / Ctrl`-klikk på skyveknappen, så kan du skrive inn verdien med tastaturet.

#### **Hvordan synkroniserer jeg Liberation til musikk?**

Programmet har et intelligent «tap tempo»-system som fungerer slik du forventer, men du kan også bruke en ekstern MIDI-klokke eller Ableton Link. Se [Tempo / synkronisering](tempo-synchronisation.md "mention"). Tidslinjen kan synkroniseres til innkommende LTC/SMPTE-tidskode via et hvilket som helst lydgrensesnitt. Se [Timecode](timecode.md "mention").

#### Hvilke innstillinger må jeg justere for å få best mulig output fra laseren?

Hovedinnstillingen er _Scanner Sync_, som kompenserer for den lille forsinkelsen mellom speilbevegelsen og endringer i laserens lysstyrke. Hvis laserpunktene/-strålene har små «haler», må du justere dette. (Se bildene på siden [Innstillingspanelet Laser output](setting-up/laser-settings.md "mention") for et eksempel på «haler».)

Du kan også prøve å endre skannerhastigheten – lavere hvis skannerne dine er enkle, eller høyere hvis de er gode. Men **vær forsiktig, for du kan skade skannerne hvis du presser dem for hardt.**

Det finnes også noen forhåndsinnstilte skannerinnstillinger. Standardvalget er konservativt og fungerer fint for de fleste behov med laserstråler. Men det finnes andre forhåndsinnstillinger hvis du har bedre skannere, og det finnes innstillinger som er tilpasset grafikk.

For mer informasjon, se [Innstillingspanelet Laser output](setting-up/laser-settings.md "mention"). For informasjon om hvordan du lager egne forhåndsinnstillinger, se [◼️ Skannerforhåndsinnstillinger og render-profiler](advanced/scanner-presets.md "mention") (avansert, under arbeid)

Du kan også korrigere fargebalansen med _Colour calibration_-innstillingene. Se [Fargekalibrering](advanced/colour-calibration.md "mention") (avansert teknikk)

#### Hva gjør _Latency(ms)_-innstillingen?

Dette er bilde-latensen, eller den maksimale tiden mellom at et bilde genereres og deretter sendes til en laser. Du skal normalt ikke trenge å justere den, men hvis du har nettverksproblemer, kan du prøve å øke den. Se [Latensinnstilling](setting-up/latency-setting.md "mention") for mer informasjon.

### Clips

#### Hvordan justerer jeg zones og innstillinger for et Clip uten å kjøre det?

`Alt / Option`-klikk for å gjøre det til _currently selected clip_ uten å aktivere det. Se også [Starte / stoppe Clips](clips/starting-stopping-clips.md "mention")

#### Hvordan kopierer jeg Clips?

Klikk og dra mens du holder inne `Alt / Option`-tasten. Se også [Organisere Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Hvordan sletter jeg Clips?

Klikk og dra dem ut av Clip Deck. Se også [Organisere Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Hvordan gjør jeg flervalg, sletter, kombinerer Clip Decks osv.?

Se [Organisere Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Hva betyr det lille mikrofonsymbolet og de andre ikonene på Clip-knappen?

De viser at et Clip tar imot lyd- eller MIDI-input, og de tre prikkene viser at det finnes en zone-forsinkelse. Se [Hva betyr de små ikonene på Clip-knappene?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
