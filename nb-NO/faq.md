---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Maskinvare

#### **Kjører Liberation på Windows?**

Ja – Liberation støtter **Windows 10 og 11 (64-bit)** fullt ut, med nøyaktig de samme funksjonene som Mac-versjonen. Hver utgivelse lanseres samtidig for begge plattformer.

#### **Kjører Liberation på Mac**

Ja – Liberation støtter **Mac (macOS 12 Monterey og nyere)** fullt ut, med full funksjonslikhet med Windows-versjonen. Alle oppdateringer slippes samtidig.

#### **Hva er minimumskravene til maskinen?**

Det avhenger av hvor mange lasere du vil styre. Hvis du bare kjører noen få lasere, klarer du deg fint med en maskin med lavere spesifikasjoner. Alle Apple Silicon-Mac-er kjører svært godt, og bør kunne styre opptil 100 lasere. Hvis du kjører komplekse show der mye står på spill, anbefaler vi den beste maskinen du har råd til.

#### **Hvor mange lasere kan jeg styre med Liberation?**

Liberation kan kjøre mange lasere på én datamaskin. Det er testet med over 100 laserkontrollere, så svaret avhenger av:

* CPU-en i datamaskinen din
* nettverkshastighet
* abonnementstypen din

#### **Hvilke MIDI-kontrollere kan jeg bruke?**

Liberation er utviklet og optimalisert rundt den populære APC40 Mk2 MIDI-kontrolleren. Det fungerer også med APC40 Mk1. Se [Live-styring med APC40](midi-control/live-control-with-the-apc40.md "mention")

Vi legger gradvis til flere MIDI-kontrollere underveis, og støtter for øyeblikket også APC Mini Mk2 og MIDI Fighter Twister.

Det finnes også et MIDI Send/Receive-system som gir ekstra MIDI-kontroll. Se [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Se [MIDI-kontroll](midi-control/ "mention")for mer informasjon.

#### **Kan jeg bruke det med hvilken som helst MIDI-kontroller?**

Vi jobber for øyeblikket med et konfigurerbart MIDI-system som vil gjøre dette mulig i fremtiden. I mellomtiden har noen brukere hatt hell med å bruke en MIDI-fortolker som kan konvertere MIDI-meldinger for MIDI Send/Receive-systemet, men dette er en pirkete og avansert prosess. Søk i [forumet](https://forum.liberationlaser.com) etter råd om dette oppsettet, men realistisk sett er APC40 det beste alternativet.

## Laserkontrollere

#### **Hvilke laserkontrollere er kompatible med Liberation?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (du må kanskje oppdatere firmware)
* LaserCube USB (og LaserDock)
* LaserCube network protocol (med kablet tilkobling)
* AVB slik det brukes av [LASollinger lasers](https://laseranimation.com/en/) (for øyeblikket bare macOS, under testing)

Se [Kompatible lasere og kontrollere (DAC-er)](hardware/compatible-lasers-and-controllers-dacs.md "mention") for mer informasjon

#### **Hvorfor støtter dere ikke \[annet merke av] laserkontroller?**

For å oppmuntre til bedre samspill mellom programvare og maskinvare vil Liberation bare støtte DAC-er som har en publisert kommunikasjonsprotokoll. Jeg mener dette er den beste veien videre for laserbransjen.

#### **Hvordan vet jeg om laseren min kan brukes med Liberation?**

Hvis laseren din har ett av følgende, kan du bruke den med Liberation:

* En ekstern **ILDA input** – en 25-pinners D-kontakt, brukt med en kompatibel ekstern kontroller.
* En internt installert **Ether Dream**.
* En hvilken som helst **LaserCube** (fungerer med både USB- og Wi-Fi-LaserCube).
* En **X-Laser unit with a built-in Mercury system** (i Ether Dream-modus).
* En **LaserAnimation Sollinger projector with AVB built in** (bare macOS, krever AVB-kompatible nettverksenheter, for øyeblikket under testing).

Se [Kompatible lasere og kontrollere (DAC-er)](hardware/compatible-lasers-and-controllers-dacs.md "mention") for mer informasjon

#### **Kan jeg bruke Liberation med min LaserCube?**

Ja, Liberation fungerer direkte med alle LaserCube. Se [LaserCube](hardware/lasercube.md "mention")

## Lisenser

#### **Hva koster en lisens?**

Se [shop](https://liberationlaser.com/shop)-siden for gjeldende priser.

#### **Hva er begrensningene mellom lisensnivåene?**

Se [shop](https://liberationlaser.com/shop)-siden for gjeldende lisensalternativer.

Merk at du kan sette opp, forhåndsvise og designe show med så mange lasere du vil på **alle** nivåer, også gratisnivået. Det finnes ingen andre begrensninger i det hele tatt bortsett fra antallet lasere du kan _arm_. Alle andre Liberation-funksjoner er tilgjengelige for alle.

#### **Kan jeg oppgradere til et nytt nivå?**

Du kan når som helst oppgradere til et høyere nivå. Du får en delvis refusjon for gjenstående tid på den nåværende lisensen, og den nye planen starter umiddelbart. Se [Oppgrader / nedgrader lisensen din](installation/upgrade-downgrade-your-license.md "mention")

#### **Kan jeg nedgradere lisensen min?**

Du kan nedgradere når som helst, men endringen trer i kraft ved slutten av den nåværende lisensperioden. Se [Oppgrader / nedgrader lisensen din](installation/upgrade-downgrade-your-license.md "mention")

#### **Hvordan autoriserer jeg datamaskinen med lisensen min?**

Når du har kjøpt en lisens, kan du autorisere datamaskinen i selve Liberation-programvaren. Du vil se en _Authorise_-knapp på _About_-skjermen som ber deg logge inn på nettstedet. Følg instruksjonene på skjermen for å fullføre autoriseringsprosessen. Se [Autorisere og deautorisere](installation/authorising-and-de-authorising.md "mention")

#### **Hvor ofte må jeg koble datamaskinen til internett?**

Hver gang lisensen fornyes, må du koble Liberation til internett for å oppdatere den interne lisensen. Ved månedlig gjentakende betaling må du koble til hver måned.

#### **Hva skjer hvis jeg ikke kan koble datamaskinen til internett etter fornyelse?**

Liberation gir deg en frist på 7 dager etter at lisensen fornyes til å koble til internett og oppdatere den interne lisensen. Etter denne perioden går Liberation tilbake til _Free_-modus.

#### **Hva skjer hvis kredittkortet mitt utløper?**

Du får et e-postvarsel fra betalingsleverandøren vår, og du må oppdatere betalingssystemet ditt. Logg inn på nettstedet og bruk lenken _Update payment details_ på abonnementssiden.

#### **Hvordan avslutter jeg den gjentakende lisensen min?**

Logg inn på nettstedet, åpne siden _Your subscriptions_, velg abonnementet du vil avslutte, og klikk deretter på lenken _Cancel Subscription_. Du kan fortsette å bruke Liberation resten av lisensperioden.

#### **Hvor mange datamaskiner kan jeg installere Liberation på?**

Du kan installere Liberation på så mange datamaskiner du vil. Lisensautorisasjoner kreves bare for å aktivere laser-/DMX-utgang, og lisensnivået ditt bestemmer hvor mange datamaskiner som kan autoriseres for utgang samtidig. Se [Slik fungerer lisensiering](installation/how-licensing-works.md "mention")

#### **Hvordan flytter jeg lisensen min fra én datamaskin til en annen?**

* Åpne Liberation på datamaskinen du ikke lenger vil bruke
* Sørg for at du er koblet til internett, og klikk på knappen _De-authorise this computer_ på _About_-skjermen
* Åpne nå Liberation på den nye datamaskinen
* Klikk på knappen _Authorise this computer_ på _About_-skjermen.
* Nettstedet åpnes. Logg inn og følg instruksjonene på skjermen for å fullføre autoriseringen

Du kan også deautorisere en datamaskin du ikke lenger har tilgang til, eksternt (med noen begrensninger). Se [Autorisere og deautorisere](installation/authorising-and-de-authorising.md "mention")

#### **Kan jeg deautorisere Liberation på en datamaskin som er mistet eller stjålet?**

Du kan deautorisere datamaskinen via nettstedet. Hvis Liberation-installasjonen ikke har vært på nett siden siste fornyelse, kan dette gjøres umiddelbart.

Hvis ikke, trer deautoriseringen i kraft når abonnementet fornyes eller når datamaskinen kobler til internett, avhengig av hva som skjer først. Hvis du raskt må reautorisere en ny datamaskin, tar du kontakt med support.

### Bruke Liberation

#### Standardoppsettet har 8 lasere – hvordan endrer jeg dette?

Se [Sette opp prosjektet ditt](setting-up/setting-up-your-project.md "mention") og [Legge til / fjerne lasere](setting-up/adding-removing-lasers.md "mention")

#### Kan jeg kopiere soneinnstillinger fra én laser til de andre?

Ja! Se [Kopier soner mellom lasere](output-view/copy-zones-between-lasers.md "mention")

#### Kan jeg skrive inn et tall i stedet for å bruke en slider?

Ja. `Cmd / Ctrl`-klikk på slideren, så kan du angi verdien med tastaturet.

#### **Hvordan synkroniserer jeg Liberation til musikk?**

Det har et intelligent "tap tempo"-system som fungerer slik du forventer, men du kan også bruke en ekstern MIDI-klokke eller Ableton Link. Se [Tempo / synkronisering](tempo-synchronisation.md "mention"). Tidslinjen kan synkroniseres til innkommende LTC/SMPTE-timecode via et hvilket som helst lydgrensesnitt. Se [Timecode](timecode.md "mention").

#### Hvilke innstillinger må jeg justere for å få best mulig utgang fra laseren?

Hovedinnstillingen er _Colour Shift,_ som kompenserer for den lille forsinkelsen mellom at speilene beveger seg og at laserne endrer lysstyrke. Hvis laserpunktene/-strålene dine har små "haler", må du justere dette. (Se bildene på siden [Innstillingspanelet Laser output](setting-up/laser-settings.md "mention") for et eksempel på "haler")

Du kan også prøve å endre scannerhastigheten – lavere hvis scannerne dine er enkle, eller høyere hvis de er gode. Men **vær forsiktig, siden du kan skade scannerne hvis du driver dem for hardt.**

Det finnes også noen forhåndsinnstilte scannerinnstillinger. Standardalternativet er konservativt og fungerer fint for de fleste krav til laserstråler. Men det finnes andre forhåndsinnstillinger hvis du har bedre scannere, og det finnes forhåndsinnstillinger som er tilpasset grafikk.

For mer informasjon, se [Innstillingspanelet Laser output](setting-up/laser-settings.md "mention"), og for informasjon om hvordan du lager dine egne forhåndsinnstillinger, se [◼️ Scanner-forhåndsinnstillinger og renderprofiler](advanced/scanner-presets.md "mention") (avansert, under arbeid)

Du kan også korrigere fargebalansen med innstillingene _Colour calibration_. Se [Fargekalibrering](advanced/colour-calibration.md "mention")(avansert teknikk)

#### Hva gjør innstillingen _Latency(ms)_?

Dette er frame-latensen, eller maksimal tid mellom at en frame genereres og deretter sendes til en laser. Du skal vanligvis ikke trenge å justere den, men hvis du har nettverksproblemer, kan du prøve å øke den. Se [Latensinnstilling](setting-up/latency-setting.md "mention") for mer informasjon.

### Clips

#### Hvordan justerer jeg soner og innstillinger for en clip uten å kjøre den?

`Alt / Option`-klikk for å gjøre den til _Clip som er valgt for øyeblikket_ uten å aktivere den. Se også [Starte / stoppe clips](clips/starting-stopping-clips.md "mention")

#### Hvordan kopierer jeg clips?

Klikk og dra mens du holder inne `Alt / Option`-tasten. Se også [Organisere Clip Deck-et ditt](clips/organising-your-clip-deck.md "mention")

#### Hvordan sletter jeg clips?

Klikk og dra dem ut av Clip Deck. Se også [Organisere Clip Deck-et ditt](clips/organising-your-clip-deck.md "mention")

#### Hvordan multivelger, sletter og kombinerer jeg Clip Decks osv.?

Se [Organisere Clip Deck-et ditt](clips/organising-your-clip-deck.md "mention")

#### Hva betyr det lille mikrofonsymbolet og de andre ikonene på clipen?

De viser deg at en clip tar imot lyd- eller MIDI-inndata, og de 3 prikkene viser at det finnes en soneforsinkelse. Se [Hva er de små ikonene på clip-knappene?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
