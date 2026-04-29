---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Positionsbasierte Changer

Diese Node-Familie verändert Inhalte abhängig von ihrer Position. Standardmäßig wird der Effekt entlang einer horizontalen Achse angewendet (von links nach rechts), du kannst diese Achse aber auf einen beliebigen Winkel drehen. Jeder Node enthält außerdem einen _radial_-Modus, bei dem der Effekt durch den Winkel jedes Punkts relativ zur Mitte gesteuert wird.

* **Colour Changer by Position** – verschiebt Farben entlang der gewählten Achse oder um den radialen Winkel.\
  \&#xNAN;_Beispiel: Erzeuge einen Regenbogenverlauf, der über eine Linie wandert, oder nutze den radialen Modus auf einem Kreis, um einen Farbrad-Effekt zu erzeugen._
* **Wave Shift by Position** – wendet eine Sinuswellen-Verzerrung an und verschiebt den Inhalt vertikal (oder senkrecht zur gewählten Achse).\
  \&#xNAN;_Beispiel: Lass eine Linie wie Wasser kräuseln, oder nutze den radialen Modus, um einen Kreis von der Mitte aus nach außen pulsieren zu lassen._
* **Noise Shift by Position** – wendet eine Simplex-Noise-Verzerrung an und verschiebt den Inhalt vertikal (oder senkrecht zur gewählten Achse).\
  \&#xNAN;_Beispiel: ähnlich wie beim Wave Shift-Beispiel, aber mit einem organischeren und zufälligeren Charakter – ideal, um natürliche Variation hinzuzufügen._

## &#x20;Farbänderung nach Position

Dieser Node wendet Farbänderungen positionsabhängig auf deinen Inhalt an. Standardmäßig ist die Achse horizontal (0°), du kannst sie aber drehen oder in den radialen Modus wechseln.

* **wavelength** – legt die Größe des sich wiederholenden Farbzyklus fest.
  * _Linear mode:_ Bei 100% erstreckt sich ein vollständiger Zyklus über die gesamte Breite des Inhalts.
  * _Radial mode:_ Bei 100% erstreckt sich ein vollständiger Zyklus über den ganzen Kreis (360°). Die Werte sind Prozentwerte des Kreises: z. B. 50% = ein halber Kreis (180°).
* **offset** – verschiebt den Startpunkt des Farbzyklus als Prozentsatz der Wellenlänge. Du kannst diesen Wert modulieren (z. B. mit einem Sägezahn-Oszillator), um Farben gleichmäßig durchlaufen zu lassen.
* **repeat** – wenn aktiviert, wiederholt sich der Zyklus über den Inhalt hinweg. Wenn deaktiviert, wird der Verlauf nur einmal angewendet: Alles vor dem Start erhält die Startfarbe, alles nach dem Ende erhält die Endfarbe.
* **pingpong** – wenn aktiviert, wechselt jede Wiederholung die Richtung und erzeugt dadurch einen gespiegelten Effekt. Wenn _Repeat_ deaktiviert ist, läuft der Verlauf einmal vorwärts und dann wieder zurück. _Hinweis: Im Pingpong-Modus umfasst die wavelength sowohl den Vorwärts- als auch den Rücklauf._
* **linear angle** – dreht die Achse des Effekts. 0° = horizontal.
* **radial** – schaltet in den radialen Modus und wendet Farben basierend auf dem Winkel von der Mitte an.
* **radial smooth loop** – passt die wavelength automatisch so an, dass sie gleichmäßig in 100% des Kreises passt. Dadurch wird eine sichtbare Naht an der Stelle verhindert, an der der Zyklus umspringt.

**Farbmodi**

Diese bestimmen, welche Aspekte der Farbanpassungen auf den Inhalt angewendet werden. Siehe auch: [Farbeinstellungen und HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – der Farbton bleibt unverändert.
  * _FIXED_ – der Farbton wird auf einen festen Wert gesetzt.
  * _SHIFTED_ – der Farbton wird um den angegebenen Betrag verschoben (unterschiedlich gefärbte Elemente bleiben unterscheidbar, werden aber gemeinsam um das Farbrad verschoben).
* **saturation mode**
  * _OFF_ – die Sättigung bleibt unverändert.
  * _FIXED_ – die Sättigung wird auf den angegebenen Wert gesetzt.
* **brightness mode**
  * _OFF_ – die Helligkeit bleibt unverändert.
  * _FIXED_ – die Helligkeit wird auf den angegebenen Wert gesetzt.
  * _MULTIPLY_ – die Helligkeit wird mit dem angegebenen Wert skaliert. Dadurch bleiben Dynamiken erhalten (z. B. blinken blinkende Elemente weiterhin, aber innerhalb des begrenzten Helligkeitsbereichs).

**Start- / Endwerte**

Diese Slider definieren den Farbbereich, der entlang der gewählten Achse (oder des radialen Sweeps) angewendet wird.

* **start hue** – der Farbton am Anfang des Verlaufs.
* **end hue** – der Farbton am Ende des Verlaufs.
* **start saturation** – die Sättigung am Anfang.
* **end saturation** – die Sättigung am Ende.
* **start brightness** – die Helligkeit am Anfang.
* **end brightness** – die Helligkeit am Ende.
* **blend** – mischt die Farbänderung mit den Originalfarben. Bei 100% ersetzt der Effekt die Originalfarben vollständig.

**Beispiel 1: Gleitender Regenbogenverlauf**

Ausgehend von den Standardeinstellungen:

1. Lass den Node im **Linear**-Modus (0° Winkel = horizontal).
2. Lass **wavelength** auf 100% (erstreckt sich über die volle Breite und sollte der Standardwert sein).
3. Lass die Start- und Endwerte auf ihren Standardwerten.
4. Aktiviere **repeat**.
5. Füge der Einstellung **offset** einen **Sawtooth Oscillator** hinzu, der von 0% bis 100% läuft.

***

**Beispiel 2: Schwarz-Weiß-Schwarz-Verlauf (Pingpong)**

Ausgehend von den Standardeinstellungen:

1. Lass den Node im **Linear**-Modus (0° Winkel = horizontal).
2. Lass **wavelength** auf 100% (erstreckt sich über die volle Breite und sollte der Standardwert sein).
3. Schalte **repeat** aus.
4. Setze **start brightness** auf 0 (Schwarz).
5. Setze **end brightness** auf 100 (Weiß).
6. Setze **start saturation** und **end saturation** auf 0 (wandelt zu Graustufen um).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Aktiviere **pingpong**.

_Ergebnis: Der Verlauf blendet über die Breite von Schwarz zu Weiß und dann zurück zu Schwarz._\
Wenn der Inhalt seinen Farbton und seine Sättigung behalten soll, schalte Saturation mode auf OFF. \\

***

**Beispiel 3: Rotierendes Regenbogen-Farbrad (Radial)**

1. Aktiviere den **radial**-Modus.
2. Setze **wavelength** auf 100% (ein vollständiger 360°-Sweep).
3. Schalte **repeat** ein.
4. Füge der Einstellung **offset** einen **Sawtooth Oscillator** hinzu, der von 0% bis 100% läuft.

_Ergebnis: ein nahtloses Farbrad, das sich kontinuierlich um den Kreis dreht._

## &#x20;Wellenverschiebung nach Position

Dieser Node wendet eine Wellenverzerrung auf deinen Inhalt an und verschiebt Punkte senkrecht zur gewählten Achse (oder radial von der Mitte aus).

* **Wavelength** – legt die Länge des Wellenzyklus fest.
  * _Linear mode:_ Bei 100% erstreckt sich ein vollständiger Zyklus über die gesamte Breite des Inhalts.
  * _Radial mode:_ Bei 100% erstreckt sich ein vollständiger Zyklus über die vollen 360°. (Die Werte sind Prozentwerte des Kreises: 50% = eine halbe Umdrehung, 25% = eine Viertelumdrehung usw.)
* **Size** – steuert die Amplitude der Welle (wie weit der Inhalt verschoben wird).
* **Offset** – verschiebt die Welle entlang der Achse (oder im radialen Modus um den Kreis). Dies ist ein Prozentsatz der Wellenlänge, sodass du ihn mit einem **Oscillator Node** animieren kannst, damit die Welle wandert.
* **Radial** – wechselt vom linearen in den radialen Modus, sodass die Verschiebung auf dem Winkel von der Mitte basiert.
* **Radial Smooth Loop** – passt die Wellenlänge so an, dass sie gleichmäßig in 100% des Kreises passt. Dadurch werden sichtbare Nähte am Übergang verhindert.
* **Triangle** – ändert die Wellenform von Sinus zu Dreieck.
* **Absolute** – verwendet den Absolutwert der Welle und erzeugt dadurch nur Verschiebungen nach oben (die negative Seite wird auf die positive umgeklappt).
* **Angle** – dreht die Achse der Welle. 0° = horizontal.

## &#x20;Noise-Verschiebung nach Position

Dieser Node verzerrt Inhalte mit einem Noise-Feld (ähnlich wie Turbulenz) und verschiebt Punkte senkrecht zur gewählten Achse (oder radial von der Mitte aus). Im Vergleich zu _Wave Shift_ ist das Ergebnis organischer und zufälliger.

* **Detail** – steuert, wie fein der Noise ist. Höhere Werte = schärfere, detailliertere Variation. Niedrigere Werte = weichere Variation.
* **Wavelength** – legt die Skalierung des Noise-Musters fest.
  * _Linear mode:_ Bei 100% erstreckt sich ein vollständiger Noise-Zyklus über die Breite des Inhalts.
  * _Radial mode:_ Bei 100% erstreckt sich ein vollständiger Zyklus über die vollen 360°.
* **Size** – steuert die Stärke der Verschiebung (Amplitude der Noise-Verzerrung).
* **Offset** – verschiebt das Noise-Muster entlang der Achse (oder um den Kreis). Dies ist ein Prozentsatz der Wellenlänge, sodass du ihn mit einem **Oscillator Node** animieren kannst, damit der Noise „fließt“.
* **Depth Offset** – bewegt sich durch das 3D-Noise-Feld und erzeugt Variation über die Zeit. Das ist besonders effektiv, wenn es mit einem Oscillator Node animiert wird.
* **Depth Detail** – steuert, wie detailliert die Variation entlang der Tiefendimension ist.
* **Absolute** – verwendet den Absolutwert des Noise und klappt negative Werte in positive um (dadurch entsteht nur eine einseitige Verschiebung).
* **Radial** – wechselt vom linearen in den radialen Modus, sodass die Verschiebung auf dem Winkel von der Mitte basiert.
* **Radial Smooth Loop** – passt die Wellenlänge so an, dass sie gleichmäßig in 100% des Kreises passt. Dadurch werden sichtbare Nähte im radialen Modus verhindert.
