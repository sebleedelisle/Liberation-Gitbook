---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardware

#### **Kører Liberation på Windows?**

Ja - Liberation understøtter fuldt ud **Windows 10 og 11 (64-bit)** med præcis de samme funktioner som Mac-versionen. Hver udgivelse kommer samtidig til begge platforme.

#### **Kører Liberation på Mac**

Ja - Liberation understøtter fuldt ud **Mac (macOS 12 Monterey og nyere)** med samme funktionsniveau som Windows-versionen. Alle opdateringer udgives samtidig.

#### **Hvad er minimumskravene til computeren?**

Det afhænger af, hvor mange lasere du vil styre. Hvis du kun bruger nogle få lasere, kan du sagtens klare dig med en computer med lavere specifikationer. Alle Apple Silicon Macs kører rigtig godt og bør kunne styre op til 100 lasere. Hvis du kører komplekse shows, hvor meget afhænger af resultatet, anbefaler vi den bedste computer, du har råd til.

#### **Hvor mange lasere kan jeg styre med Liberation?**

Liberation kan køre mange lasere på én computer. Det er testet med over 100 lasercontrollere, så svaret afhænger af:

* computerens CPU
* netværkshastighed
* dit licensniveau

#### **Hvilke MIDI-controllere kan jeg bruge?**

Liberation er designet og optimeret omkring den populære APC40 Mk2 MIDI-controller. Det fungerer også med APC40 Mk1. Se [Live MIDI-controllere](midi-control/live-control-with-the-apc40.md "mention")

Liberation understøtter også APC Mini og MIDI Fighter Twister. APC40 Mk2 er stadig den mest komplette referencecontroller.

Der findes også MIDI Send/Receive-systemet, som giver ekstra MIDI-styring. Se [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Se [MIDI-kontrol](midi-control/ "mention") for mere information.

#### **Kan jeg bruge det med en hvilken som helst MIDI-controller?**

Til andre controllere kan du bruge MIDI Send/Receive-systemet eller en MIDI-translator, der kan sende Liberations standard-MIDI-beskeder. Søg på [forummet](https://forum.liberationlaser.com) efter råd om denne opsætning, men realistisk set er APC40 Mk2 stadig den bedste løsning til de fleste live-shows.

## Lasercontrollere

#### **Hvilke lasercontrollere er kompatible med Liberation?**

* [Ether Dream (anbefales)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury fra X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (du skal muligvis opdatere din firmware)
* LaserCube USB (og LaserDock)
* LaserCube-netværksprotokol (med kablet forbindelse)
* AVB som brugt af [LASollinger-lasere](https://laseranimation.com/en/) (i øjeblikket kun macOS under test)

Se [Kompatible lasere og controllere (DACs)](hardware/compatible-lasers-and-controllers-dacs.md "mention") for mere information

#### **Hvorfor understøtter I ikke \[et andet mærke] lasercontroller?**

For at fremme bedre interoperabilitet mellem software og hardware understøtter Liberation kun DACs, der har en offentliggjort kommunikationsprotokol. Jeg mener, at det er den bedste vej frem for laserbranchen.

#### **Hvordan kan jeg se, om min laser kan bruges med Liberation?**

Hvis din laser har en af følgende muligheder, kan du bruge den med Liberation:

* En ekstern **ILDA-indgang** – et 25-pin D-stik, der bruges med en kompatibel ekstern controller.
* En internt installeret **Ether Dream**.
* En hvilken som helst **LaserCube** (fungerer med både USB- og Wi-Fi-LaserCube).
* En **X-Laser-enhed med indbygget Mercury-system** (i Ether Dream-tilstand).
* En **LaserAnimation Sollinger-projektor med indbygget AVB** (kun macOS, kræver AVB-kompatible netværksenheder, i øjeblikket under test).

Se [Kompatible lasere og controllere (DACs)](hardware/compatible-lasers-and-controllers-dacs.md "mention") for mere information

#### **Kan jeg bruge Liberation med min LaserCube?**

Ja, Liberation fungerer direkte med alle LaserCube-enheder. Se [LaserCube](hardware/lasercube.md "mention")

## Licenser

#### **Hvad koster en licens?**

Se siden [shop](https://liberationlaser.com/shop) for de aktuelle priser.

#### **Hvad er begrænsningerne mellem licensniveauerne?**

Se siden [shop](https://liberationlaser.com/shop) for de aktuelle licensmuligheder.

Bemærk, at du kan opsætte, forhåndsvise og designe shows med så mange lasere, du vil, på **alle** niveauer – også det gratis – og der er ingen andre begrænsninger overhovedet ud over antallet af lasere, du kan aktivere til output. Alle andre Liberation-funktioner er tilgængelige for alle.

#### **Kan jeg opgradere til et nyt niveau?**

Du kan opgradere til et højere niveau når som helst. Du får en delvis refusion for den resterende tid i din nuværende betalte periode, og dit nye licensniveau starter med det samme. Se [Opgrader / nedgrader din licens](installation/upgrade-downgrade-your-license.md "mention")

#### **Kan jeg nedgradere min licens?**

Du kan nedgradere når som helst, men ændringen træder i kraft ved udgangen af din nuværende betalte periode. Se [Opgrader / nedgrader din licens](installation/upgrade-downgrade-your-license.md "mention")

#### **Kan jeg sætte betalinger for min licens på pause?**

Ja. Licensen kan sættes på pause fra næste abonnementsdato og genstartes når som helst. Det er nyttigt, hvis du bruger softwaren i perioder, og du behøver ikke indtaste dine kortoplysninger igen. Se [Sæt betalinger på pause eller annuller](installation/cancel-your-subscription.md "mention")

#### **Hvordan annullerer jeg min licens permanent?**

Du kan annullere din tilbagevendende licens når som helst, og den deaktiveres automatisk ved udgangen af den aktuelle betalte periode. Se [Sæt betalinger på pause eller annuller](installation/cancel-your-subscription.md "mention")

#### **Hvordan autoriserer jeg min computer med min licens?**

Når du har købt en licens, kan du autorisere computeren i selve Liberation-softwaren. Du vil se en _Authorise_-knap på _About_-skærmen, som beder dig om at logge ind på websitet. Følg instruktionerne på skærmen for at gennemføre autoriseringsprocessen. Se [Autorisation og fjernelse af autorisation](installation/authorising-and-de-authorising.md "mention")

#### **Hvor ofte skal jeg forbinde min computer til internettet?**

Hver gang en tilbagevendende betalt licens fornyes korrekt, skal du forbinde Liberation til internettet for at opdatere den interne licens. Så for en månedlig licens med automatisk fornyelse skal du forbinde hver måned.

#### **Hvad sker der, hvis jeg ikke kan forbinde min computer til internettet efter næste betaling?**

For månedlige tilbagevendende betalte licenser giver Liberation normalt en frist på 7 dage efter, at din betalte licens er fornyet, til at forbinde til internettet og opdatere den interne licens. Efter den periode går Liberation tilbage til _Free_-tilstand.

#### **Hvad sker der, hvis mit kreditkort udløber?**

Du får en e-mailbesked fra vores betalingsudbyder, og du skal opdatere dine kortoplysninger. Log ind på websitet, og brug _UPDATE CARD DETAILS_ på licenssiden eller _Update_ under _Billing and payments_. Du skal gøre dette inden for fristen for at undgå at miste adgang til betalte funktioner.

#### **Hvor mange computere kan jeg installere Liberation på?**

Du kan installere Liberation på så mange computere, du vil. Licensautorisationer kræves kun for at aktivere laser-/DMX-output, og dit licensniveau bestemmer, hvor mange computere der kan være autoriseret til output på samme tid. Se [Sådan fungerer licensering](installation/how-licensing-works.md "mention")

#### **Hvordan flytter jeg min licens fra én computer til en anden?**

* Åbn Liberation på den computer, du ikke længere vil bruge
* Sørg for, at du har forbindelse til internettet, og klik på knappen _De-authorise this computer_ på _About_-skærmen
* Åbn nu Liberation på den nye computer
* Klik på knappen _Authorise this computer_ på _About_-skærmen.
* Websitet åbnes. Log ind, og følg instruktionerne på skærmen for at gennemføre autoriseringen

Du kan også fjerne autorisationen eksternt fra en computer, du ikke længere har adgang til (med visse begrænsninger). Se [Autorisation og fjernelse af autorisation](installation/authorising-and-de-authorising.md "mention")

#### **Kan jeg fjerne autorisationen af Liberation på en computer, der er blevet væk eller stjålet?**

Du kan fjerne computerens autorisation via websitet. Hvis Liberation-installationen ikke har været online siden den seneste licensopdatering, kan det gøres med det samme.

Hvis ikke, træder fjernelsen af autorisationen i kraft, næste gang licensen opdateres, eller når computeren forbinder til internettet – alt efter hvad der sker først. Hvis du akut har brug for at genautorisere en ny computer, skal du kontakte support.

### Brug af Liberation

#### Standardopsætningen har 8 lasere - hvordan ændrer jeg det?

Se [Opsætning af dit projekt](setting-up/setting-up-your-project.md "mention") og [Tilføjelse / fjernelse af lasere](setting-up/adding-removing-lasers.md "mention")

#### Kan jeg kopiere zone-indstillinger fra én laser til de andre?

Ja! Se [Kopiér zones mellem lasere](output-view/copy-zones-between-lasers.md "mention")

#### Kan jeg skrive et tal i stedet for at bruge en slider?

Ja. `Cmd / Ctrl`-klik på slideren, så kan du indtaste værdien med tastaturet.

#### **Hvordan synkroniserer jeg Liberation til musik?**

Liberation har et intelligent "tap tempo"-system, der fungerer, som du forventer, men du kan også bruge et eksternt MIDI-clock eller Ableton Link. Se [Tempo / synkronisering](tempo-synchronisation.md "mention"). Tidslinjen kan synkroniseres til indgående LTC/SMPTE-timecode via enhver audiointerface. Se [Timecode](timecode.md "mention").

#### Hvilke indstillinger skal jeg justere for at få det bedste output fra laseren?

Den vigtigste indstilling er _Scanner Sync_, som kompenserer for den lille forsinkelse mellem spejlenes bevægelse og laserens ændring i lysstyrke. Hvis dine laserprikker/-stråler har små "haler", skal du justere denne indstilling. (Se billederne på siden [Panelet Laser output settings](setting-up/laser-settings.md "mention") for et eksempel på "haler")

Du kan også prøve at ændre scannerhastigheden – langsommere, hvis dine scannere er enkle, eller hurtigere, hvis de er gode. Men **brug det med forsigtighed, da du kan beskadige dine scannere, hvis du presser dem for hårdt.**

Der findes også nogle forudindstillede scannerindstillinger. Standardindstillingen er konservativ og fungerer fint til de fleste krav til laserstråler. Men der er andre presets, hvis du har bedre scannere, og der er presets, som er tunet til grafik.

For mere information, se [Panelet Laser output settings](setting-up/laser-settings.md "mention"), og for information om, hvordan du opretter dine egne presets, se [◼️ Scanner-presets og render-profiler](advanced/scanner-presets.md "mention") (avanceret, under udarbejdelse)

Du kan også korrigere farvebalancen med indstillingerne _Colour calibration_. Se [Farvekalibrering](advanced/colour-calibration.md "mention") (avanceret teknik)

#### Hvad gør indstillingen _Latency(ms)_?

Dette er frame-latency, eller den maksimale tid mellem, at en frame genereres, og at den efterfølgende sendes til en laser. Du bør ikke behøve at justere den, men hvis du har netværksproblemer, kan du prøve at øge den. Se [Latency-indstilling](setting-up/latency-setting.md "mention") for flere detaljer.

### Clips

#### Hvordan justerer jeg zones og indstillinger for et Clip uden at køre det?

`Alt / Option`-klik for at gøre det til det _aktuelt valgte Clip_, men uden at aktivere det. Se også [Start / stop Clips](clips/starting-stopping-clips.md "mention")

#### Hvordan kopierer jeg Clips?

Klik og træk, mens du holder `Alt / Option`-tasten nede. Se også [Organisering af dit Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Hvordan sletter jeg Clips?

Klik og træk dem væk fra Clip Deck. Se også [Organisering af dit Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Hvordan multivælger, sletter, kombinerer jeg Clip Decks osv.?

Se [Organisering af dit Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Hvad betyder det lille mikrofonsymbol og de andre ikoner på Clip?

De viser, at et Clip bruger lyd- eller MIDI-input, og de 3 prikker viser, at der er en zone-forsinkelse. Se [Hvad betyder de små ikoner på Clip-knapperne?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
