---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zonen

Der wichtigste Zonentyp, den du in den meisten Projekten verwenden wirst, ist die _Beam zone_. Diese Zone ist für atmosphärische Beam-Effekte in der Luft gedacht. Der andere Zonentyp ist eine _Canvas zone_ (siehe [Grafiken und das Canvas-System](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**WARNUNG: Sei extrem vorsichtig, wenn du Zonen verschiebst, während der Laser läuft**, und drehe die Helligkeit so weit wie möglich herunter. In [Überblick über den Laser-Einrichtungsprozess](../setting-up/setting-up-lasers.md "mention") findest du eine ausführliche Anleitung, wie du Laser sicher aktivierst und Zonen einrichtest.
{% endhint %}

Du kannst die Zonen mit der Maus anklicken und ziehen. Aktiviere ein Testmuster, um zu sehen, wohin diese Zone ausgegeben wird.

{% hint style="info" %}
Verwende die Pfeiltasten, um die aktuell ausgewählte Zone bzw. den aktuell ausgewählten Punkt fein zu **verschieben**. Halte die Taste `Shift` gedrückt, um in größeren Schritten zu verschieben.
{% endhint %}

{% hint style="info" %}
Tipp: Du kannst Zoneneinstellungen schnell auf mehrere Laser kopieren! Siehe [Einstellungen zwischen Lasern kopieren](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Neue Beam-Zone hinzufügen

Klicke oben in der Toolbar auf die Schaltfläche _Add a new beam zone_. Daraufhin erscheint eine neue Zone. Beachte, dass Beam-Zonen in der Reihenfolge sortiert werden, in der du sie hinzufügst. Du kannst sie aber neu anordnen. Siehe [Beam-Zonen neu anordnen](re-ordering-beam-zones.md "mention")

### Vorhandene Canvas-Zone hinzufügen

Klicke auf die Schaltfläche _Add existing canvas zone_. Du siehst dann eine Liste der verfügbaren Canvas-Zonen und kannst sie für diesen Laser ein- oder ausschalten. Siehe [Grafiken und das Canvas-System](../graphics-and-the-canvas-system/ "mention")

### Zonenformen

Es gibt 3 Zonenformen:

* **Quad** – die standardmäßige rechteckige Zonenform, die einheitlich (achsenausgerichtet) oder verzerrt sein kann. Am besten geeignet für größere rechteckige Zonen oder Canvas-Zonen, die eine perspektivische Korrektur benötigen.
* **Line/Curve** – eine Zone, die durch 2 oder mehr Punkte und eine Stärke definiert wird. Ideal für schmale Zonen oder zum Begrenzen auf Balkonen, Brücken oder anderen gekrümmten Formen.
* **Segmented** – eine Zone, die in kleinere Quads unterteilt werden kann. Ideal für Architektur-Mapping.

Klicke mit der rechten Maustaste auf eine beliebige Zone, um ihre Einstellungen zu öffnen. In diesem Rechtsklick-Menü kannst du:

* Die Zone umbenennen. Das kann hilfreich sein, um sie im Clip Deck zu identifizieren, besonders wenn du viele Zonen hast.
* Die Zone aktivieren/deaktivieren
* Die Position sperren
* Den Formtyp ändern
* Auf die Standardposition zurücksetzen
* Auf formtypspezifische Einstellungen zugreifen
* Die Zone löschen
* Eine _Alt Zone_ hinzufügen (siehe [Alt-Zonen-System](alt-zone-system.md "mention"))

{% hint style="danger" %}
**WARNUNG:** Sei sehr vorsichtig, wenn du den Zonentyp änderst, während der Laser aktiv ist. Die Zone kehrt zur letzten Position bzw. Größe für diese Form zurück, sodass sich die Ausgabe plötzlich ändern kann. Am besten schaltest du den Laser aus, bevor du den Zonentyp änderst.
{% endhint %}

### Quad-Zonenform

Du kannst jede Ecke des Quads mit der Maus verschieben. Klicke mit `Alt / Option` auf eine Ecke, um sie unabhängig von den anderen zu verschieben und das Quad zu verzerren. Sobald das Quad verzerrt ist, können alle Ecken frei verschoben werden.

Du kannst die Verzerrung entfernen und die Zone mit der Schaltfläche _REMOVE DISTORTION_ im Rechtsklick-Menü wieder in ein achsenausgerichtetes Rechteck zurücksetzen.

#### Perspektivische Korrektur

Diese Option kann über den Umschalter im Rechtsklick-Menü eingestellt werden und legt die Verzerrungsmethode fest. Für Beams lässt du sie am besten ausgeschaltet. Wenn diese Zone jedoch Grafiken auf eine flache Ebene projiziert, schalte sie ein, damit die Ausgabe perspektivisch korrigiert wird.

{% hint style="info" %}
Wenn _Perspective correction_ ausgeschaltet ist, wird Inhalt mit _bi-linear interpolation_ verzerrt. Anders gesagt: Der Inhalt wird gleichmäßig über das Quad verteilt. Deshalb eignet sich diese Methode am besten für Beams.

Wenn die perspektivische Korrektur eingeschaltet ist, wird Inhalt mit perspektivischem Warping verzerrt, das die perspektivische Verkürzung ausgleicht. Wenn du also Grafiken in einem schrägen Winkel auf eine Wand projizierst, kannst du damit die Ausgabe entzerren und die Projektionsverzerrung korrigieren.
{% endhint %}

### Line / Curve-Zonenform

Die Line / Curve-Zonenform ist in meinen letzten Shows zu meiner bevorzugten Option geworden, und man könnte durchaus sagen, dass sie eigentlich der Standard für Beam-Zonen sein sollte.

Meine Zonen müssen oft sehr schmal sein, damit sie in schwierige, enge Bereiche in Veranstaltungsorten oder zwischen Fenster an Gebäuden passen. Dabei habe ich festgestellt, dass es extrem fummelig sein kann, die vier Ecken eines Quads anzupassen, wenn sie so nah beieinander liegen. So ist die Line / Curve-Zone entstanden!

Für gerade Linien brauchst du nur zwei Punkte und passt dann im Rechtsklick-Menü die _Zone thickness_ an. Das ist die schnellste Möglichkeit, einfache Zonen zu erstellen.

Klicke mit `Alt / Option` auf die Linie, um zusätzliche Punkte zu erstellen. Diese Punkte werden automatisch geglättet, damit eine fließende Form entsteht. Mit _Smooth level_ kannst du Knicke ausgleichen.

Klicke mit `Alt / Option` auf einen Punkt, um ihn zu löschen.

Wenn du Erfahrung mit Vektorgrafik-Programmen hast (Inkscape, Illustrator usw.), kannst du alternativ die Option _Manually adjust bezier curves_ verwenden, um alle Kontrollpunkte präzise selbst anzupassen.

### Segmented-Zonenform

Mit dieser unterteilten Zone kannst du äußerst detaillierte Korrekturen vornehmen. Sie ist nützlich, wenn du auf komplexe Formen mappst. Über die Schaltflächen + und - im Rechtsklick-Menü kannst du Unterteilungen hinzufügen oder entfernen.

### Eine Zone bearbeiten, die vollständig von einer anderen Zone verdeckt wird

Klicke mit der rechten Maustaste auf die obere Zone und klicke auf die Schaltfläche mit dem Vorhängeschloss, um sie zu sperren. Danach solltest du die darunterliegende Zone bearbeiten und anpassen können.

<br>

{% hint style="info" %}
Sobald du deinem Output eine Beam-Zone hinzufügst, kannst du sie einem Clip im Clip Deck hinzufügen.
{% endhint %}
