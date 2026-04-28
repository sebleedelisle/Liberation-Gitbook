---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Compatibele lasers en controllers (DACs)

### Welke lasers zijn compatibel met Liberation?

Als je laser een standaard ILDA-ingang heeft, kun je hem gebruiken met Liberation (samen met een compatibele lasercontroller zoals de Ether Dream of Helios DAC - [zie de volledige lijst hieronder](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>De Helios DAC - de goedkoopste optie voor thuisgebruik</p></figcaption></figure>

Je hebt geen externe controller of ILDA-ingang nodig als:

* Je laser een ingebouwde Ether Dream heeft, of;
* Je een LaserCube van Wicked Lasers hebt, of;
* Je een X-Laser-fixture met ingebouwde Mercury hebt, of;
* Je een Laser Animation Sollinger-laser met ingebouwde AVB-controller hebt (momenteel alleen in test op macOS)

{% hint style="info" %}
**Wat is een lasercontroller?**

Een lasercontroller (of DAC) is een hardwareapparaat dat de digitale data van Liberation kan omzetten naar de analoge signalen die nodig zijn om de scanners en output van je laser aan te sturen. (Vandaar DAC: Digital to Analog Converter.)

De controller wordt via USB of via een standaard computernetwerk met je computer verbonden; het is een extern apparaat of zit ingebouwd in de laser.

Als hij extern is, verbind je hem met je laser via de ILDA-aansluiting. ILDA is een industriestandaard die een ouderwetse 25-pins ‘D’-connector gebruikt. Neem een ILDA-kabel, steek het ene uiteinde in de controller en het andere in de laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>De ILDA-output op een externe Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Het achterpaneel van een laser met de verschillende aansluitingen, waaronder de ILDA-ingang</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Een standaard ILDA-kabel</p></figcaption></figure>

### Welke controller is het beste voor mij?

Als je thuisgebruiker bent, of kleine shows draait met 4 of minder lasers die dicht bij de computer staan, dan zijn USB-controllers zoals de **Helios DAC** de **meest betaalbare** optie.

Netwerk-DACs zoals de **Ether Dream** zijn de **beste optie voor professionele** laserists die graag een netwerk opzetten en een groot aantal lasers willen aansturen; alle grote Liberation-shows tot nu toe zijn op Ether Dreams gedraaid.

Als je een **LaserCube** hebt, heb je helemaal geen aparte lasercontroller nodig - Liberation is compatibel met alle LaserCubes. De oudere modellen maken verbinding met een USB-kabel en de nieuwere modellen maken verbinding via een netwerk.

Als je een professional bent en de eenvoudigste optie zoekt, overweeg dan X-Laser-units met ingebouwde Mercury of Laser Animation Sollinger-lasers die AVB gebruiken.

### Compatibele lasercontrollers

#### Ether Dream (Network)

De [Ether Dream](https://ether-dream.com) bestaat al meer dan tien jaar en zit momenteel op versie 4 (hoewel Liberation ook werkt met Ether Dream versie 1, 2 en 3). Ze zijn extreem betrouwbaar.

Je maakt verbinding via een standaard netwerk. Ze zijn verkrijgbaar als losse units, of nog beter: ze kunnen in lasers worden ingebouwd.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) is de beste optie voor beginners en goedkoper dan Ether Dreams, maar omdat ze via USB verbinden, wordt dit niet aanbevolen voor lange kabeltrajecten. Ook kun je USB-data- en driverproblemen krijgen zodra je meer dan 4 controllers aansluit (vooral op Windows).

Maar als je gewoon een paar lasers thuis wilt aansturen, is dit de goedkoopste en eenvoudigste optie.

#### Mercury (Built-in to X-Laser units)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) is het krachtige DMX-laserbesturingssysteem van X-Laser, ontworpen voor lichtontwerpers die lasers rechtstreeks vanaf een traditionele lichtconsole willen aansturen. Met de nieuwste firmware-update bevat Mercury ook **Ether Dream-emulatie**, wat betekent dat het nu naadloos werkt met Liberation - en met alle andere software die Ether Dream ondersteunt.

#### AVB (Built into Laser Animation Sollinger units)

**AVB** is een open netwerkprotocol voor hoogwaardige audio- en datastreaming met lage latency. Veel LaserAnimation Sollinger-projectoren hebben AVB-ondersteuning direct in de hardware ingebouwd, waardoor Liberation via het netwerk verbinding met ze kan maken zonder externe DACs. AVB-ondersteuning in Liberation is momenteel **alleen voor macOS en in test**, en vereist **compatibele netwerkapparaten met AVB-ondersteuning**. Als het correct is ingesteld, biedt het een eenvoudigere workflow, minder externe apparaten en robuuste betrouwbaarheid voor professionele shows. I

#### Controllers die in de toekomst worden ondersteund:

* [IDN](http://www.ilda-digital.com) (een open netwerkprotocol van ILDA, dat door elke fabrikant kan worden geïmplementeerd)

### Bekabelingssuggesties

Voor optimale prestaties houd je USB-DACs dicht bij je computer en verbind je ze met de lasers via langere ILDA-kabels. (Let wel op: ILDA-kabels kunnen tijdens de afbouw als een enterhaak werken!)

Als je Ether Dreams gebruikt, kun je ze nog steeds allemaal bij elkaar houden en met lange ILDA-kabels met de lasers verbinden, of je kunt ze dicht bij de lasers ophangen en langere netwerkkabels gebruiken.

De ideale opstelling is om Ether Dreams (of andere controllers) direct in je lasers te laten inbouwen (Rob van Stanwax Laser kan dit voor je doen in het VK)
