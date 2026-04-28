---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Farbeinstellungen und HSB

Farben werden in Liberation als HSB definiert, nicht als RGB. Das ist dir vielleicht ungewohnt, aber ich finde, dass es ein deutlich intuitiveres System ist, sobald man sich daran gewöhnt hat.

{% hint style="info" %}
Wenn du lieber RGB verwendest, kannst du in jeder Farbeinstellung auf das Farbfeld klicken. Dadurch öffnet sich das Farbeditor-Panel, in dem du Optionen für RGB und HSB findest.
{% endhint %}

### HSB – Hue, Saturation und Brightness

#### Hue

Der Farbton reicht von 0 bis 255. 0 ist Rot. Wenn du den Wert erhöhst, durchläufst du alle Farbtöne des Regenbogens: Orange, Gelb, Grün, Cyan, Blau, Violett, Magenta und bei 255 wieder zurück zu Rot.

Da es sich um eine Schleife handelt, kannst du mit einer Dreieckwelle durch alle Farben wechseln.

#### Saturation

Diese Einstellung steuert die Sättigung oder Leuchtkraft deiner Farbe. Anders gesagt: wie _farbig_ sie ist. Der Bereich reicht von 0 bis 255. Setze die Sättigung auf 0 für Grautöne und auf 255 für volle Regenbogenfarben. Werte dazwischen ergeben pastellige, ausgewaschene Farben.

{% hint style="info" %}
Entschuldigung an meine US-Freunde für den zusätzlichen Vokal im Wort colour. Liberation wird in England entwickelt, daher ist britisches Englisch die Standardeinstellung. In Zukunft möchte ich Übersetzungen für Französisch, Spanisch, Deutsch, Italienisch, vereinfachtes Chinesisch und ja, sogar US-Englisch anbieten. :innocent:
{% endhint %}

#### Brightness

Wahrscheinlich am einfachsten zu verstehen: 0 ist komplett schwarz, 255 ist volle Helligkeit.

### Beispielanwendungen

#### Regenbogenzyklus:

Setze _Brightness_ und _Saturation_ auf 255. Verbinde einen _Sawtooth_-Oszillator mit deinem _Hue_-Socket und stelle seinen Bereich von 0 bis 255 ein.

#### Pulsierende Helligkeit:

Verbinde einen _Sawtooth_-Oszillator mit deinem _Brightness_-Socket und stelle seinen Bereich von 255 bis 0 ein. Du kannst außerdem Clamp-Minimum und -Maximum anpassen, um die Dauer der Änderung zu steuern. Verwende anschließend die Easing-Funktionen, um die Animation weiter zu verfeinern.

#### Harter Flash / Strobe:

Wähle eine Farbe über _Hue_ und _Saturation_ oder indem du auf den Colour Picker klickst. Verbinde einen _Square Wave_-Oszillator mit deinem _Brightness_-Socket und stelle seinen Bereich von 255 bis 0 ein.

#### Durch einen eigenen Farbtonbereich wechseln:

Setze _Brightness_ und _Saturation_ auf 255. Verbinde einen _Triangle Wave_-Oszillator mit deinem _Hue_-Socket und stelle seinen Bereich ein:

* Für Blau bis Cyan verwende einen Bereich von 70 bis 128.
* Für Rot bis Gelb verwende einen Bereich von 0 bis 40.
* Für Rot bis Magenta verwende einen Bereich von 255 bis 220.
