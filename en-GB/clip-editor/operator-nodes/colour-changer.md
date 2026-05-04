---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Changes the colours of all incoming content. You can either set fixed HSB values, or switch to the gradient system and sample colours from a custom gradient.

* **hue, saturation, brightness** - the colour values, see [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - the hue isn't changed
  * FIXED - the hue of elements is set to the hue value
  * SHIFT - the hue of elements is offset by the value, so different coloured elements will remain different, but just be shifted along the hue value.
* **saturation mode** -
  * OFF - saturation isn't changed
  * FIXED - saturation is fixed at the specified value.
* **brightness mode** -
  * OFF - brightness isn't changed
  * FIXED - brightness of elements is set to the brightness value
  * MULTIPLY - brightness of elements is combined with the brightness value, so if they're flashing they'll still flash, but only up to the brightness specified here.
* **gradient mode** - switches from the fixed HSB sliders to the gradient editor. The node samples one colour from the gradient and then applies it using the hue, saturation and brightness modes above.
* **gradient position** - chooses which point in the gradient is sampled. Animate this from 0% to 100% with a Sawtooth Oscillator to cycle through the gradient over time.
* **blend** - how strongly the colour changer is applied, 0% is not at all, 100% is full, and 50% is a combination of the existing colour and the new values.

{% hint style="info" %}
The Colour Change node samples one colour from the gradient for the whole input. If you want the gradient to run across the shape by position, use [position-based-changers.md](position-based-changers.md "mention") instead.
{% endhint %}

### Gradient editor

When **gradient mode** is on, the gradient editor appears below the main controls.

* Click the gradient bar to add a colour stop.
* Left-click a stop to select it, then drag it sideways to move it.
* Drag a selected stop down away from the bar, or press Delete/Backspace, to remove it. A gradient always keeps at least two stops.
* Right-click a stop to edit it with the colour picker.
* Use **Position**, **Hue**, **Saturation** and **Brightness** to edit the selected stop precisely.
* **interpolation** chooses how colours are blended between stops:
  * **HSB** - blends hue, saturation and brightness. This is best for smooth rainbow-style movement around the colour wheel.
  * **RGB** - blends red, green and blue values directly. This often feels more like a screen or lighting console colour fade.
  * **NONE** - jumps from one stop to the next with no blend.
* **hue direction** is available in HSB interpolation:
  * **AUTO** - takes the shortest route around the hue wheel.
  * **FORWARDS** - always travels forwards through hue values.
  * **BACKWARDS** - always travels backwards through hue values.
