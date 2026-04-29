---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Einführung

Liberation enthält ein flexibles und leistungsstarkes DMX-System, mit dem du Lichteffekte erstellen und DMX-kompatible Laser über Art-Net steuern kannst. Es ist so ausgelegt, dass du deine Beleuchtung einfach mit deiner Lasershow synchron halten kannst – ganz ohne separates Lichtpult.

{% hint style="info" %}
**Was ist Art-Net, und wie hängt es mit DMX zusammen?**

**DMX** ist ein System, das seit Jahren zur Steuerung von Scheinwerfern, Lasern, Nebelmaschinen und anderen Bühneneffekten verwendet wird. Es sendet Steuersignale über spezielle Kabel, meist mit XLR-Steckern. Jedes Gerät hört auf einen bestimmten Kanalbereich, um zu wissen, was es tun soll.

**Art-Net** ist eine neuere Methode, dieselben DMX-Daten über ein normales Computernetzwerk zu übertragen. Statt spezieller Kabel wird alles über Ethernet gesendet, genau wie Internet- oder lokaler Netzwerkverkehr.

In Liberation wird die gesamte DMX-Ausgabe über Art-Net gesendet. Du kannst damit Art-Net-kompatible Geräte direkt steuern oder einen **Art-Net-Node** anschließen – eine kleine Box, die Art-Net wieder in standardmäßiges DMX umwandelt. So kannst du auch klassische DMX-Scheinwerfer und -Effekte weiterhin steuern, selbst wenn sie Art-Net nicht selbst unterstützen.
{% endhint %}

Du kannst damit außerdem viele verschiedene Arten von Bühnentechnik steuern, zum Beispiel Nebelmaschinen, Hazer, CO₂-Jets, Cold-Spark-Maschinen und mehr. Wenn ein Gerät DMX unterstützt, kannst du es als DMX-Zone einrichten und direkt aus Liberation triggern – direkt neben deinen Laser-Inhalten.

DMX-Geräte werden als **DMX zones** hinzugefügt. Sie erscheinen in der Zonenliste neben deinen Laserstrahl-Zonen und Canvas-Zielbereichen. Jede DMX-Zone verwendet ein **DMX preset**, das Liberation mitteilt, wie Eigenschaften aus deinen Laser-Clips – etwa Position, Farbe und Helligkeit – auf DMX-Kanalwerte abgebildet werden.

Wenn du einen Clip an eine DMX-Zone sendest, betrachtet Liberation das erste Element im Clip und wandelt dessen Eigenschaften entsprechend dem Preset um. So kannst du Scheinwerfer und DMX-Effekte direkt mit denselben Clips steuern, die du bereits für Laser verwendest.

#### Liberation in Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Der erste echte Test des Liberation DMX-Systems fand 2023 in Glastonbury statt. Dort installierte Reach Lasers insgesamt 90 Beam-Quellen als Teil der Arcadia-„Spider“-Bühne.

18 Laser wurden mit internen Ether Dreams gesteuert, weitere 12 Beam-Bars mit je 6 Köpfen über Art-Net und DMX.
