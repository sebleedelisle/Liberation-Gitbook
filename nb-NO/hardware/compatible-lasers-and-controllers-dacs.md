---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatible lasere og kontrollere (DAC-er)

### Hvilke lasere er kompatible med Liberation?

Hvis laseren din har en standard ILDA-inngang, kan du bruke den med Liberation sammen med en kompatibel laserkontroller, for eksempel Ether Dream eller Helios DAC - [se full liste nedenfor](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - det rimeligste alternativet for hjemmebruk</p></figcaption></figure>

Du trenger ikke en ekstern kontroller eller en ILDA-inngang hvis:

* Laseren din har Ether Dream installert internt, eller;
* Du har en LaserCube fra Wicked Lasers, eller;
* Du har en X-Laser-armatur med innebygd Mercury, eller;
* Du har en Laser Animation Sollinger-laser med innebygd AVB-kontroller (for øyeblikket under testing kun på macOS)

{% hint style="info" %}
**Hva er en laserkontroller?**

En laserkontroller (eller DAC) er en maskinvareenhet som kan ta de digitale dataene fra Liberation og konvertere dem til de analoge signalene som trengs for å styre skannerne og utgangen på laseren din. (Derav DAC: Digital to Analog Converter.)

Kontrolleren kobles til datamaskinen via USB eller over et vanlig datanettverk. Den kan enten være en ekstern enhet eller være installert inne i laseren.

Hvis den er ekstern, kobler du den til laseren via ILDA-tilkoblingen. ILDA er en bransjestandard som bruker en gammeldags 25-pinners D-kontakt. Skaff deg en ILDA-kabel, koble den ene enden til kontrolleren og den andre til laseren.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>ILDA-utgangen på en ekstern Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Bakpanelet på en laser, med de ulike tilkoblingene, inkludert ILDA-inngangen</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>En standard ILDA-kabel</p></figcaption></figure>

### Hvilken kontroller passer best for meg?

Hvis du er hjemmebruker, eller kjører små show med 4 eller færre lasere som står nær datamaskinen, er USB-kontrollere som **Helios DAC** det **rimeligste** alternativet.

Nettverks-DAC-er som **Ether Dream** er det **beste alternativet for profesjonelle** laseroperatører som er komfortable med å sette opp et nettverk og ønsker å kjøre et stort antall lasere. Alle de store Liberation-showene så langt har blitt kjørt på Ether Dream.

Hvis du har en **LaserCube**, trenger du ikke en separat laserkontroller i det hele tatt - Liberation er kompatibel med alle LaserCube-modeller. De eldre modellene kobles til med USB-kabel, og de nyere modellene kobles til over nettverk.

Hvis du er profesjonell og vil ha den enkleste løsningen, bør du vurdere X-Laser-enheter med innebygd Mercury eller Laser Animation Sollinger-lasere som bruker AVB.

### Kompatible laserkontrollere

#### Ether Dream (nettverk)

[Ether Dream](https://ether-dream.com) har eksistert i over ti år og er for øyeblikket på versjon 4 (selv om Liberation også fungerer med Ether Dream versjon 1, 2 og 3). De er svært driftssikre.

Du kobler til dem over et vanlig nettverk. De kan kjøpes som frittstående enheter, eller enda bedre: de kan monteres inne i lasere.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) er det beste alternativet for nybegynnere, og de er billigere enn Ether Dream. Men siden de kobles til via USB, anbefales de ikke for lange kabelstrekk. Du kan også få problemer med USB-data og drivere når du kobler til mer enn 4 enheter (spesielt på Windows).

Men hvis du bare vil kjøre et par lasere hjemme, er dette det billigste og enkleste alternativet.

#### Mercury (innebygd i X-Laser-enheter)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) er X-Lasers kraftige DMX-baserte laserkontrollsystem, laget for lysdesignere som vil kjøre lasere direkte fra et tradisjonelt lysbord. Med den nyeste fastvareoppdateringen inkluderer Mercury også **Ether Dream-emulering**, som betyr at det nå fungerer sømløst med Liberation - samt all annen programvare som støtter Ether Dream.

#### AVB (innebygd i Laser Animation Sollinger-enheter)

**AVB** er en åpen, nettverksbasert protokoll for høyytelses lyd- og datastrømming med lav forsinkelse. Mange LaserAnimation Sollinger-projektorer har AVB-støtte direkte i maskinvaren, noe som gjør at Liberation kan koble til dem over nettverket uten behov for eksterne DAC-er. AVB-støtte i Liberation er for øyeblikket **kun for macOS og under testing**, og krever **kompatible nettverksenheter med AVB-støtte**. Når det er riktig satt opp, gir det en enklere arbeidsflyt, færre eksterne enheter og robust driftssikkerhet for profesjonelle show.

#### Kontrollere som vil bli støttet i fremtiden:

* [IDN](http://www.ilda-digital.com) (en åpen nettverksprotokoll fra ILDA, som kan implementeres av alle produsenter)

### Kabelforslag

For optimal ytelse bør du plassere USB-DAC-er nær datamaskinen og koble dem til laserne med lengre ILDA-kabler. (Men pass på: ILDA-kabler kan fungere som en gripekrok når du rigger ned!)

Hvis du bruker Ether Dream, kan du fortsatt ha dem samlet og koble til laserne med lange ILDA-kabler, eller du kan rigge dem nær laserne og bruke lengre nettverkskabler.

Det ideelle oppsettet er å ha Ether Dream (eller andre kontrollere) installert direkte inne i laserne dine (Rob hos Stanwax Laser kan gjøre dette for deg i Storbritannia)
