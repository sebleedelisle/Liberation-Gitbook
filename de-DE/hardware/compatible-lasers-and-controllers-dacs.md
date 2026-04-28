---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatible Laser und Controller (DACs)

### Welche Laser sind mit Liberation kompatibel?

Wenn dein Laser einen standardmäßigen ILDA-Eingang hat, kannst du ihn mit Liberation verwenden, zusammen mit einem kompatiblen Laser-Controller wie dem Ether Dream oder Helios DAC – [die vollständige Liste findest du unten](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Der Helios DAC – die günstigste Option für den Heimgebrauch</p></figcaption></figure>

Du brauchst keinen externen Controller und keinen ILDA-Eingang, wenn:

* dein Laser Ether Dream intern eingebaut hat, oder;
* du einen LaserCube von Wicked Lasers hast, oder;
* du ein X-Laser-Gerät mit integriertem Mercury hast, oder;
* du einen Laser Animation Sollinger-Laser mit integriertem AVB-Controller hast (derzeit nur unter macOS im Test)

{% hint style="info" %}
**Was ist ein Laser-Controller?**

Ein Laser-Controller (oder DAC) ist ein Hardwaregerät, das die digitalen Daten von Liberation in analoge Signale umwandelt, die zur Steuerung der Scanner und der Ausgabe deines Lasers benötigt werden. Daher DAC: Digital to Analog Converter.

Der Controller wird per USB oder über ein normales Computernetzwerk mit deinem Computer verbunden. Er ist entweder ein externes Gerät oder im Laser eingebaut.

Wenn er extern ist, verbindest du ihn über den ILDA-Anschluss mit deinem Laser. ILDA ist ein Industriestandard, der einen klassischen 25-poligen „D“-Stecker verwendet. Besorge dir ein ILDA-Kabel, stecke ein Ende in den Controller und das andere in den Laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>Der ILDA-Ausgang an einem externen Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Die Rückseite eines Lasers mit den verschiedenen Anschlüssen, einschließlich ILDA-Eingang</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Ein standardmäßiges ILDA-Kabel</p></figcaption></figure>

### Welcher Controller ist am besten für mich?

Wenn du Heimanwender bist oder kleine Shows mit 4 oder weniger Lasern betreibst, die sich in der Nähe des Computers befinden, sind USB-Controller wie der **Helios DAC** die **günstigste** Option.

Netzwerk-DACs wie der **Ether Dream** sind die **beste Option für professionelle** Laseristen, die bereit sind, ein Netzwerk einzurichten, und viele Laser betreiben möchten. Alle großen Liberation-Shows wurden bisher mit Ether Dreams umgesetzt.

Wenn du einen **LaserCube** hast, brauchst du überhaupt keinen separaten Laser-Controller – Liberation ist mit allen LaserCubes kompatibel. Die älteren Modelle werden per USB-Kabel verbunden, die neueren Modelle über ein Netzwerk.

Wenn du als Profi die einfachste Option suchst, solltest du X-Laser-Geräte mit integriertem Mercury oder Laser Animation Sollinger-Laser mit AVB in Betracht ziehen.

### Kompatible Laser-Controller

#### Ether Dream (Netzwerk)

Den [Ether Dream](https://ether-dream.com) gibt es seit über zehn Jahren. Aktuell ist Version 4 erhältlich, wobei Liberation auch mit Ether Dream Version 1, 2 und 3 funktioniert. Die Geräte sind äußerst zuverlässig.

Du verbindest dich über ein normales Netzwerk mit ihnen. Sie sind als eigenständige Geräte erhältlich oder, noch besser, können direkt in Laser eingebaut werden.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) ist die beste Option für Einsteiger und günstiger als Ether Dreams. Da die Verbindung jedoch über USB läuft, ist Helios für lange Kabelwege nicht empfohlen. Außerdem können USB-Daten- und Treiberprobleme auftreten, sobald du mehr als 4 Geräte anschließt, besonders unter Windows.

Wenn du aber nur ein paar Laser zu Hause betreiben möchtest, ist es die günstigste und einfachste Option.

#### Mercury (in X-Laser-Geräte integriert)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) ist das leistungsstarke DMX-Lasersteuerungssystem von X-Laser, entwickelt für Lichtdesigner, die Laser direkt von einem klassischen Lichtpult aus betreiben möchten. Mit dem neuesten Firmware-Update enthält Mercury auch **Ether Dream emulation**. Das bedeutet, dass es jetzt nahtlos mit Liberation funktioniert – ebenso wie mit jeder anderen Software, die Ether Dream unterstützt.

#### AVB (in Laser Animation Sollinger-Geräte integriert)

**AVB** ist ein offenes, netzwerkbasiertes Protokoll für leistungsstarkes Audio- und Datenstreaming mit niedriger Latenz. Viele LaserAnimation Sollinger-Projektoren unterstützen AVB direkt in der Hardware, sodass Liberation sich über das Netzwerk mit ihnen verbinden kann, ohne externe DACs zu benötigen. AVB-Unterstützung in Liberation ist derzeit **nur unter macOS verfügbar und im Test** und erfordert **kompatible AVB-fähige Netzwerkgeräte**. Wenn es korrekt eingerichtet ist, bietet es einen einfacheren Workflow, weniger externe Geräte und hohe Zuverlässigkeit für professionelle Shows.

#### Controller, die in Zukunft unterstützt werden:

* [IDN](http://www.ilda-digital.com) (ein offenes Netzwerkprotokoll von ILDA, das von jedem Hersteller implementiert werden kann)

### Empfehlungen zur Verkabelung

Für optimale Leistung solltest du USB-DACs in der Nähe deines Computers platzieren und sie mit längeren ILDA-Kabeln mit den Lasern verbinden. Achte allerdings darauf: ILDA-Kabel können beim Abbau wie ein Enterhaken wirken!

Wenn du Ether Dreams verwendest, kannst du sie ebenfalls alle zusammen platzieren und die Laser über lange ILDA-Kabel verbinden. Alternativ kannst du sie nahe an den Lasern riggen und längere Netzwerkkabel verwenden.

Der ideale Aufbau ist, Ether Dreams oder andere Controller direkt in deine Laser einbauen zu lassen. In Großbritannien kann Rob von Stanwax Laser das für dich übernehmen.
