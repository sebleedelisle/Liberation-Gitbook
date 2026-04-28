---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube-Werbebild mit freundlicher Genehmigung von Wicked Lasers</p></figcaption></figure>

Der [LaserCube](https://www.laseros.com/lasercube/) von Wicked Lasers ist eine extrem kompakte, akkubetriebene Lasereinheit, die in verschiedenen Leistungskonfigurationen erhältlich ist. Er ist bei Hobby-Anwendern beliebt, weil die Smartphone-App sehr einfach zu bedienen ist. Neuere Modelle sind aber leistungsfähig genug, um auch bei professionellen Shows eingesetzt zu werden.

Die Smartphone-App (sie heißt LaserOS und ist auch für Desktop verfügbar) kann kostenlos heruntergeladen werden, macht viel Spaß und ist für die meisten Anwender völlig ausreichend. Wenn du aber größere Shows mit mehreren Lasern fährst, brauchst du etwas Spezialisierteres und Leistungsfähigeres – und genau hier kommt Liberation ins Spiel.

### Mit einem LaserCube verbinden

Frühe LaserCubes werden über USB gesteuert, die aktuellen Modelle haben jedoch alle einen integrierten Netzwerk-Controller. Diese netzwerkgesteuerten Cubes werden als „LaserCube Wifi“ bezeichnet. Liberation unterstützt beide LaserCube-Typen\*, egal ob sie per USB oder über ein Netzwerk verbunden sind.

\*(Unterstützung für das LaserCube-Netzwerkprotokoll wurde in Version 0.7.3 eingeführt)

### USB LaserCube

Verbinde deinen LaserCube mit einem Micro-USB-Kabel mit deinem Computer und suche ihn anschließend im _Controller Assignment_-Panel (siehe [controller-assignment.md](../setting-up/controller-assignment.md "mention")). Wenn er nicht automatisch erscheint, klicke auf den _REFRESH_-Button.

### Network LaserCube „Wifi“

{% hint style="danger" %}
Auch wenn die „Wifi“-Cubes dafür ausgelegt sind, über ein drahtloses Netzwerk betrieben zu werden, wird das nicht empfohlen. Du wirst dabei sehr wahrscheinlich Aussetzer und Störungen bekommen. Verwende stattdessen die RJ45-Buchse, um deinen LaserCube mit einem kabelgebundenen Netzwerk zu verbinden – genau wie bei Ether Dreams.
{% endhint %}

Verbinde deinen LaserCube mit deinem kabelgebundenen Netzwerk.

Schalte deinen LaserCube in den „LAN Client“-Modus und stelle sicher, dass sich ein Router in deinem Netzwerk befindet. Der LaserCube erhält dann eine IP-Adresse von deinem Router und sollte anschließend im _Controller Assignment_-Panel erscheinen. (Siehe [controller-assignment.md](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Es ist möglich, ein Netzwerk ohne Router einzurichten und allen Geräten feste IP-Adressen zu geben. Das ist in der Veranstaltungsbranche sehr verbreitet. Ich persönlich bevorzuge es, einen Router ins Netzwerk einzubinden, und empfehle diese Variante allen, die weniger Erfahrung mit Netzwerken haben.

Der Router weist allen Geräten dynamisch eine IP-Adresse zu. Meiner Erfahrung nach ist das einfacher und weniger fehleranfällig.
{% endhint %}

{% hint style="danger" %}
Anders als Ether Dream _**UNTERDRÜCKEN LaserCubes DEN LASERSTRAHL NICHT**_, wenn ein Buffer-Underrun, ein verlorenes Paket oder andere beschädigte / falsche Daten auftreten.

Stattdessen machen sie einfach an der Stelle weiter, an der sie aufgehört haben. In manchen Fällen kann dadurch ein aktiver Strahl Bereiche durchqueren, die nicht innerhalb von Zonen liegen, und noch schlimmer: Er kann Software-Masken durchschneiden.

Ich spreche mit den Designern/Entwicklern von LaserCube und hoffe, dass sie dieses Verhalten in Zukunft mit einem Firmware-Update beheben. Bis dahin musst du jedoch sicherstellen, dass alle Bereiche, in die der Laser nicht gelangen darf, physisch maskiert sind.

Fairerweise solltest du das vermutlich ohnehin tun. Ich selbst verwende allerdings Software-Masken, um Kameras und Projektoren zu schützen. Sei dir also bewusst, dass dies mit dem LaserCube-Netzwerkprotokoll gefährlicher ist als mit Ether Dream (das sofort in einen Sicherheitsstopp-Modus geht, sobald ein Fehler oder fehlende Daten auftreten).

Außerdem habe ich es bereits gesagt, aber: **Verwende eine kabelgebundene Verbindung zu deinem LaserCube**. Wifi reicht dafür nicht aus und macht dieses Problem sogar noch schlimmer.
{% endhint %}
