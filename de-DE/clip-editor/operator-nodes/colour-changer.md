---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Farbänderung

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Farbänderung

Beschreibung

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
* **blend** - wie stark die Farbänderung angewendet wird: 0% bedeutet gar nicht, 100% vollständig, und 50% ist eine Kombination aus der vorhandenen Farbe und den neuen Werten.
