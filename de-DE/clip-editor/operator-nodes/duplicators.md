---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Erstellt eine gespiegelte Kopie des gesamten Inhalts. Standardmäßig ist die Spiegelachse eine vertikale Linie in der Mitte.

* **angle** - der Winkel der Spiegelachsenlinie.
* **offset position** - verschiebt die Spiegelachse (senkrecht zur Achse)
* **delay** - Zeitverzögerung des gespiegelten Inhalts. Beachte, dass dies nur eine Wirkung hat, wenn der Inhalt irgendeine Art von Animation enthält.

#### 3D-Optionen (verfügbar, wenn 3D ausgewählt ist)

* **angle X / angle Y** - die Spiegelachse wird zu einer Ebene, und du kannst diese Einstellungen verwenden, um die Ebene in 3D zu drehen.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Dupliziert Inhalte in einem kreisförmigen Muster.

* **radius** - der Abstand vom Mittelpunkt, um den der Inhalt vor dem Drehen verschoben wird.
* **count** - die Anzahl der Kopien, die vom Objekt erstellt werden.
* **use each objects pivot point** - wenn ausgewählt, wird jedes Element um seinen eigenen Mittelpunkt verschoben und gedreht. (Wirkt sich nur aus, wenn mehrere Elemente dupliziert werden)
* **delay** - fügt jedem duplizierten Element eine zunehmend längere Zeitverzögerung hinzu. Beachte, dass der Inhalt irgendeine Art von Animation enthalten muss, damit dies sichtbar wirkt.
* **rotation** - eine zusätzliche Rotation, die auf die Elemente angewendet wird.

#### 3D-Optionen (verfügbar, wenn 3D ausgewählt ist)

* **rotation x / rotation y** - dreht das gesamte kreisförmige Muster um die X- und Y-Achse.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Dupliziert Inhalte in einem Rastermuster aus Zeilen und Spalten.

* **spacing** - der Abstand zwischen den Elementen
* **count X**- die Anzahl der Kopien horizontal (Spalten)
* **count Y**- die Anzahl der Kopien vertikal (Zeilen)
* **horizontal alignment** - der Startpunkt der Spalten, LEFT, CENTRE oder RIGHT
* **vertical alignment** - der Startpunkt der Zeilen, TOP, MIDDLE oder BOTTOM
* **delay** - fügt jedem duplizierten Element eine zunehmend längere Zeitverzögerung hinzu. Beachte, dass der Inhalt irgendeine Art von Animation enthalten muss, damit dies sichtbar wirkt.
