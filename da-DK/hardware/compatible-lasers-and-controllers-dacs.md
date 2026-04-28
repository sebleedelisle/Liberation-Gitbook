---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatible lasere og controllere (DACs)

### Hvilke lasere er kompatible med Liberation?

Hvis din laser har en standard ILDA-indgang, kan du bruge den med Liberation (sammen med en kompatibel lasercontroller som Ether Dream eller Helios DAC - [se hele listen nedenfor](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - den billigste løsning til hjemmebrug</p></figcaption></figure>

Du behøver ikke en ekstern controller eller en ILDA-indgang, hvis:

* Din laser har Ether Dream installeret internt, eller;
* Du har en LaserCube fra Wicked Lasers, eller;
* Du har en X-Laser-enhed med indbygget Mercury, eller;
* Du har en Laser Animation Sollinger-laser med indbygget AVB-controller (i øjeblikket kun under test på macOS)

{% hint style="info" %}
**Hvad er en lasercontroller?**

En lasercontroller (eller DAC) er en hardwareenhed, der kan tage de digitale data fra Liberation og konvertere dem til de analoge signaler, der kræves for at styre scannerne og outputtet fra din laser. (Deraf DAC: Digital to Analog Converter.)

Controlleren forbindes til din computer via USB eller over et almindeligt computernetværk. Den er enten en ekstern enhed eller installeret inde i laseren.

Hvis den er ekstern, forbinder du den til din laser via ILDA-forbindelsen. ILDA er en industristandard, der bruger et gammeldags 25-benet 'D'-stik. Skaf et ILDA-kabel, sæt den ene ende i controlleren og den anden i laseren.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>ILDA-outputtet på en ekstern Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Bagpanelet på en laser, der viser de forskellige forbindelser, herunder ILDA-indgangen</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Et standard ILDA-kabel</p></figcaption></figure>

### Hvilken controller er bedst for mig?

Hvis du er hjemmebruger eller afvikler små shows med 4 eller færre lasere, der står tæt på computeren, er USB-controllere som **Helios DAC** den **mest prisvenlige** løsning.

Netværks-DACs som **Ether Dream** er den **bedste løsning for professionelle** laserteknikere, der er trygge ved at sætte et netværk op og vil køre et stort antal lasere. Alle større Liberation-shows indtil videre er blevet afviklet med Ether Dreams.

Hvis du har en **LaserCube**, behøver du slet ikke en separat lasercontroller - Liberation er kompatibel med alle LaserCubes. De tidligere modeller tilsluttes med et USB-kabel, og de nyere modeller tilsluttes over et netværk.

Hvis du er professionel og leder efter den nemmeste løsning, bør du overveje X-Laser-enheder med indbygget Mercury eller Laser Animation Sollinger-lasere, der bruger AVB.

### Kompatible lasercontrollere

#### Ether Dream (netværk)

[Ether Dream](https://ether-dream.com) har eksisteret i over ti år og er i øjeblikket på version 4 (selvom Liberation også fungerer med Ether Dream version 1, 2 og 3). De er ekstremt driftssikre.

Du forbinder til dem over et almindeligt netværk. De kan købes som separate enheder eller, endnu bedre, monteres inde i lasere.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) er den bedste løsning for begyndere, og de er billigere end Ether Dreams, men da de forbindes via USB, anbefales de ikke til lange kabeltræk. Du kan også få problemer med USB-data og drivere, når du tilslutter mere end 4 (især på Windows).

Men hvis du bare vil køre et par lasere derhjemme, er det den billigste og enkleste løsning.

#### Mercury (indbygget i X-Laser-enheder)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) er X-Lasers kraftfulde DMX-laserstyringssystem, designet til lysdesignere, der vil køre lasere direkte fra en traditionel lyspult. Med den seneste firmwareopdatering indeholder Mercury også **Ether Dream-emulering**, hvilket betyder, at det nu fungerer problemfrit med Liberation - samt med al anden software, der understøtter Ether Dream.

#### AVB (indbygget i Laser Animation Sollinger-enheder)

**AVB** er en åben netværksbaseret protokol til højtydende lyd- og datastreaming med lav latenstid. Mange LaserAnimation Sollinger-projektorer har AVB-understøttelse direkte i hardwaren, hvilket gør det muligt for Liberation at oprette forbindelse til dem over netværket uden behov for eksterne DACs. AVB-understøttelse i Liberation er i øjeblikket **kun til macOS og under test**, og den kræver **kompatible AVB-aktiverede netværksenheder**. Når det er sat korrekt op, giver det en enklere arbejdsgang, færre eksterne enheder og solid driftssikkerhed til professionelle shows. I

#### Controllere, der vil blive understøttet i fremtiden:

* [IDN](http://www.ilda-digital.com) (en åben netværksprotokol fra ILDA, som kan implementeres af enhver producent)

### Kabelforslag

For optimal ydelse bør du placere USB-DACs tæt på din computer og forbinde dem til laserne med længere ILDA-kabler. (Men pas på - ILDA-kabler kan fungere som en gribekrog under nedrigning!)

Hvis du bruger Ether Dreams, kan du stadig holde dem samlet og forbinde dem til laserne med lange ILDA-kabler, eller du kan rigge dem tæt på laserne og bruge længere netværkskabler.

Den ideelle opsætning er at have Ether Dreams (eller andre controllere) installeret direkte inde i dine lasere (Rob hos Stanwax Laser kan gøre dette for dig i Storbritannien)
