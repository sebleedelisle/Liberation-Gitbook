---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Color change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Color change

Description

* **hue, saturation, brightness** - the color values, see [Color settings and HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - the hue isn't changed
  * FIXED - the hue of elements is set to the hue value
  * SHIFT - the hue of elements is offset by the value, so different colored elements will remain different, but just be shifted along the hue value.
* **saturation mode** -
  * OFF - saturation isn't changed
  * FIXED - saturation is fixed at the specified value.
* **brightness mode** -
  * OFF - brightness isn't changed
  * FIXED - brightness of elements is set to the brightness value
  * MULTIPLY - brightness of elements is combined with the brightness value, so if they're flashing they'll still flash, but only up to the brightness specified here.
* **blend** - how strongly the color changer is applied, 0% is not at all, 100% is full, and 50% is a combination of the existing color and the new values.
