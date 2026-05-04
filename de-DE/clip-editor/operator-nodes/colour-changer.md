---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Farbänderung

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Farbänderung

Ändert die Farben aller eingehenden Inhalte. Du kannst entweder feste HSB-Werte festlegen oder zum Gradient-System wechseln und Farben aus einem benutzerdefinierten Farbverlauf abtasten.

* **hue, saturation, brightness** - die Farbwerte, siehe [Farbeinstellungen und HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - der Farbton wird nicht geändert
  * FIXED - der Farbton der Elemente wird auf den Wert von hue gesetzt
  * SHIFT - der Farbton der Elemente wird um den Wert verschoben. Unterschiedlich gefärbte Elemente bleiben dadurch unterschiedlich, werden aber entlang des Farbtonwerts verschoben.
* **saturation mode** -
  * OFF - die Sättigung wird nicht geändert
  * FIXED - die Sättigung wird auf den angegebenen Wert festgelegt.
* **brightness mode** -
  * OFF - die Helligkeit wird nicht geändert
  * FIXED - die Helligkeit der Elemente wird auf den Wert von brightness gesetzt
  * MULTIPLY - die Helligkeit der Elemente wird mit dem brightness-Wert kombiniert. Wenn sie blinken, blinken sie weiterhin, aber nur bis zur hier angegebenen Helligkeit.
* **gradient mode** - wechselt von den festen HSB-Schiebereglern zum Gradient-Editor. Der node tastet eine Farbe aus dem Farbverlauf ab und wendet sie dann mit den oben beschriebenen Modi für Farbton, Sättigung und Helligkeit an.
* **gradient position** - wählt aus, welcher Punkt im Farbverlauf abgetastet wird. Animiere diesen Wert mit einem Sawtooth Oscillator von 0 % bis 100 %, um den Farbverlauf über die Zeit zu durchlaufen.
* **blend** - wie stark die Farbänderung angewendet wird: 0% bedeutet gar nicht, 100% vollständig, und 50% ist eine Kombination aus der vorhandenen Farbe und den neuen Werten.

{% hint style="info" %}
Der Colour Change node tastet eine Farbe aus dem Farbverlauf für die gesamte Eingabe ab. Wenn der Farbverlauf positionsabhängig über die Form laufen soll, verwende stattdessen [positionsbasierte Changer](position-based-changers.md "mention").
{% endhint %}

### Gradient-Editor

Wenn **gradient mode** aktiviert ist, erscheint der Gradient-Editor unter den Hauptsteuerungen.

* Klicke auf die Farbverlaufsleiste, um einen Farbstopp hinzuzufügen.
* Klicke mit der linken Maustaste auf einen Stopp, um ihn auszuwählen, und ziehe ihn dann seitlich, um ihn zu verschieben.
* Ziehe einen ausgewählten Stopp nach unten von der Leiste weg oder drücke Delete/Backspace, um ihn zu entfernen. Ein Farbverlauf behält immer mindestens zwei Stopps.
* Klicke mit der rechten Maustaste auf einen Stopp, um ihn mit dem Color Picker zu bearbeiten.
* Verwende **Position**, **Hue**, **Saturation** und **Brightness**, um den ausgewählten Stopp präzise zu bearbeiten.
* **interpolation** legt fest, wie Farben zwischen Stopps gemischt werden:
* **HSB** - mischt Farbton, Sättigung und Helligkeit. Das eignet sich am besten für weiche Bewegungen im Regenbogenstil um den Farbkreis.
* **RGB** - mischt Rot-, Grün- und Blauwerte direkt. Das wirkt oft eher wie ein Farb-Fade auf einem Bildschirm oder einer Lichtkonsole.
* **NONE** - springt ohne Überblendung von einem Stopp zum nächsten.
* **hue direction** ist bei HSB-Interpolation verfügbar:
* **AUTO** - nimmt den kürzesten Weg um den Farbkreis.
* **FORWARDS** - läuft immer vorwärts durch die Farbtonwerte.
* **BACKWARDS** - läuft immer rückwärts durch die Farbtonwerte.
