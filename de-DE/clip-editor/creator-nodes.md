---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-Nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Erzeugt einen einzelnen Punkt / Beam.

* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **Colour** - die Farbe des Punkts. Siehe [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Erzeugt eine Linie / Fläche.

* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **Size** - die Länge der Linie
* **Colour** - die Farbe der Linie. Siehe [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - der Winkel der Linie in Grad
* **resolution** - siehe [resolution.md](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ legt den Startpunkt und den Drehpunkt der Linie fest
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Erzeugt einen Kreis / Kegel.

* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **radius** - der Radius des Kreises
* **Colour** - die Farbe des Kreises. Siehe [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **resolution** - siehe [resolution.md](fundamentals/resolution.md "mention")
* **Fill state** - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Erzeugt ein gleichseitiges Polygon, z. B. Dreieck, Quadrat, Fünfeck usw.

* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **size** - der Abstand vom Mittelpunkt zu jeder Ecke
* **Colour** - die Farbe des Polygons. Siehe [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - der Drehwinkel der Form in Grad
* **resolution** - siehe [resolution.md](fundamentals/resolution.md "mention")
* **Fill state** - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Lädt eine SVG-Datei für eigene Formen.

{% hint style="warning" %}
Liberation ist mit dem Format _SVGTiny_ kompatibel. InkScape wird empfohlen, aber die meisten Vektorgrafik-Apps können in dieses Format exportieren. Achte darauf, vor dem Exportieren jeden Text in Formen umzuwandeln. Liberation rendert Konturen und kann optional Füllungen als Masken verwenden. Achte darauf, dass deine Linien nicht schwarz sind, sonst werden sie ohne Farbmodifikator nicht angezeigt!
{% endhint %}

* **Import SVG** - lädt eine SVG-Datei vom Datenträger.

{% hint style="info" %}
Nachdem ein SVG geladen wurde, wird der Inhalt konvertiert und im Clip gespeichert. Du musst also keinen Verweis auf die Datei behalten, es sei denn, du möchtest später die Maskeneinstellungen ändern.
{% endhint %}

* **Use fills as masks** - verarbeitet jede gefüllte Form als Maske, d. h. sie wird mit Schwarz gefüllt. Dies wird automatisch aktiviert, wenn dein SVG gefüllte Formen enthält. Wenn es keine gefüllten Formen enthält, wird es deaktiviert. Siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - wenn die Formen in deinem SVG keine Kontur haben, können wir sie nicht zeichnen! Diese Option fügt jeder gefüllten Form eine Kontur (oder _stroke_) hinzu. Wenn dein SVG keine Formen mit Kontur enthält, wird sie automatisch aktiviert. Wenn es keine gefüllten Formen enthält, ist sie deaktiviert.
* **Invert black lines** - wenn alle Linien in deinem SVG schwarz sind, kannst du sie nicht sehen! Diese Option macht sie weiß. Sie wird automatisch aktiviert, wenn dein SVG nur schwarze Formen enthält, ist aber deaktiviert, wenn keine vorhanden sind.
* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **scale** - passt die Größe des SVG an. Dies wird automatisch berechnet, wenn das SVG geladen wird (damit das Bild sichtbar ist), kann danach aber manuell geändert werden.
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - der Drehwinkel des Bildes in Grad
* **resolution** - siehe [resolution.md](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Erzeugt eine Animation aus einer Sequenz von SVG-Dateien.

* **Import SVG Sequence** - wähle den Ordner aus, der alle SVG-Dateien enthält. Beachte, dass sie in alphanumerischer Reihenfolge geladen werden.

{% hint style="info" %}
Nachdem die SVG-Sequenz geladen wurde, wird der Inhalt konvertiert und im Clip gespeichert. Du musst also keinen Verweis auf die Dateien behalten, es sei denn, du möchtest später die Maskeneinstellungen ändern.
{% endhint %}

* **Use fills as masks** - verarbeitet jede gefüllte Form als Maske, d. h. sie wird mit Schwarz gefüllt. Dies wird automatisch aktiviert, wenn eines deiner SVGs gefüllte Formen enthält. Wenn keines gefüllte Formen enthält, wird es deaktiviert. Siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - wenn die Formen in deinen SVGs keine Konturen haben, können wir sie nicht zeichnen! Diese Option fügt jeder gefüllten Form eine Kontur (oder _stroke_) hinzu. Wenn deine SVGs keine Formen mit Kontur enthalten, wird sie automatisch aktiviert. Wenn keines gefüllte Formen enthält, ist sie deaktiviert.
* **Invert black lines** - wenn alle Linien in deinen SVGs schwarz sind, kannst du sie nicht sehen! Diese Option macht sie weiß. Sie wird automatisch aktiviert, wenn deine SVGs nur schwarze Formen enthalten, ist aber deaktiviert, wenn keine vorhanden sind.
* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **scale** - passt die Größe des Bildes an.
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - der Drehwinkel des Bildes in Grad
* **resolution** - siehe [resolution.md](fundamentals/resolution.md "mention")
* **speed** - die Dauer der gesamten Animation in Takten.
* **time per frame** - wenn dies aktiviert ist, gilt die Dauer pro Frame und nicht für die gesamte Länge der Animation. Wenn _speed_ also auf ¼ gesetzt ist, dauert jeder Frame 1 Schlag.
* **animation direction** -
  * _FORWARDS_ - die Animation läuft vorwärts und springt dann zum Anfang zurück
  * _BACKWARDS_ - die Animation läuft rückwärts und springt dann zum Ende zurück
  * _PINGPONG_ - die Animation läuft in einer Schleife vorwärts und dann rückwärts
  * _MANUAL_ - der aktuelle Frame wird über die Einstellung _position manual_ festgelegt
* **position manual** - legt den aktuellen Frame fest: 0 % ist der erste Frame, 100 % ist der letzte Frame. Dies kann manuell oder mit einem externen Oszillator eingestellt werden.
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Erzeugt Text mit einer TrueType- oder OpenType-Schriftart.

* **Text** - gib hier den gewünschten Text ein
* **Font** - wähle die gewünschte Schriftart aus

{% hint style="info" %}
Um Liberation weitere Schriftarten hinzuzufügen, kopiere die .ttf- oder .otf-Dateien in den Ordner data/resources/fonts.
{% endhint %}

* **Render profile** - siehe [render-profile.md](fundamentals/render-profile.md "mention")
* **horizontal alignment** - wähle _LEFT_, _CENTRE_ oder _RIGHT_, um die Textausrichtung festzulegen.
* **Fill state** - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - die Textgröße
* **colour -** siehe [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md "mention")
* **x**- und **y**-Position - siehe [co-ordinate-system.md](fundamentals/co-ordinate-system.md "mention")
* **rotation** - der Drehwinkel des Bildes in Grad
* **resolution** - siehe [resolution.md](fundamentals/resolution.md "mention")
* **reveal** - damit kannst du den Text schrittweise einblenden, jeweils ein Zeichen nach dem anderen. Wenn der Wert zwischen 0 und 50 % liegt, erscheint der Text schrittweise von links nach rechts. Zwischen 50 % und 100 % verschwindet der Text von links nach rechts. Du kannst einen Oszillator mit diesem Anschluss verbinden, um Animationen zu erstellen.
* **reveal by word** - wenn aktiviert, arbeitet _reveal_ wortweise statt zeichenweise.
* **countdown** - ein (schnell implementiertes!) Countdown-System. Es ändert sich alle 2 Schläge. Wenn du also Sekunden möchtest, stelle sicher, dass du bei 120 bpm bist.
* **countdown start** - die Zahl, bei der der Countdown starten soll
* _MOVE TO FRONT / MOVE TO BACK_ - siehe [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md "mention")
