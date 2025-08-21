# 🟦 Position based changers

This family of nodes modifies content according to position. By default, the effect is applied along a horizontal axis (left to right), but you can rotate this axis to any angle. Each node also includes a _radial_ mode, where the effect is driven by the angle of each point relative to the centre.

* **Colour Changer by Position** – shifts colours across the chosen axis or around the radial angle.\
  &#xNAN;_&#x45;xample: Create a rainbow gradient sweeping across a line, or use radial mode on a circle to produce a colour wheel effect._
* **Wave Shift by Position** – applies a sine wave distortion, offsetting the content vertically (or perpendicular to the chosen axis).\
  &#xNAN;_&#x45;xample: Make a line ripple like water, or use radial mode to make a circle pulse outward from the centre._
* **Noise Shift by Position** – applies a simplex noise distortion, offsetting the content vertically (or perpendicular to the chosen axis).\
  &#xNAN;_&#x45;xample: see Wave Shift example, but with a more organic and random character, perfect for adding natural variation._

## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Colour change by position

This node applies colour changes across your content based on position. By default, the axis is horizontal (0°), but you can rotate it or switch into radial mode.

* **wavelength** – sets the size of the repeating colour cycle.
  * _Linear mode:_ at 100%, one full cycle spans the full width of the content.
  * _Radial mode:_ at 100%, one full cycle spans the full circle (360°). Values are percentages of the circle: e.g. 50% = half a circle (180°).
* **offset** – shifts the starting point of the colour cycle, as a percentage of the wavelength. You can modulate this (e.g. with a sawtooth oscillator) to cycle smoothly through colours.
* **repeat** – when enabled, the cycle repeats across the content. If disabled, the gradient is applied once only: everything before the start is the start colour, everything after the end is the end colour.
* **pingpong** – when enabled, each repeat alternates in direction, creating a mirrored effect. If _Repeat_ is disabled, the gradient goes forward then back once. _Note: in Pingpong mode the wavelength covers both the forward and return sweep._
* **linear angle** – rotates the axis of the effect. 0° = horizontal.
* **radial** – switches to radial mode, applying colours based on the angle from the centre.
* **radial smooth loop** – automatically adjusts the wavelength so it divides evenly into 100% of the circle, preventing a visible seam where the cycle wraps.

**Colour Modes**

These determine which aspects of the colour adjustments are applied to the content. See also: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – hue is unchanged.
  * _FIXED_ – hue is forced to a fixed value.
  * _SHIFTED_ – hue is offset by the specified amount (different coloured elements remain distinct, but are shifted around the colour wheel together).
* **saturation mode**
  * _OFF_ – saturation is unchanged.
  * _FIXED_ – saturation is set to the specified value.
* **brightness mode**
  * _OFF_ – brightness is unchanged.
  * _FIXED_ – brightness is set to the specified value.
  * _MULTIPLY_ – brightness is scaled by the specified value. This preserves dynamics (e.g. flashing elements still flash, but within the limited brightness range).

**Start / End Values**

These sliders define the colour range applied across the chosen axis (or radial sweep).

* **start hue** – the hue at the beginning of the gradient.
* **end hue** – the hue at the end of the gradient.
* **start saturation** – saturation at the beginning.
* **end saturation** – saturation at the end.
* **start brightness** – brightness at the beginning.
* **end brightness** – brightness at the end.



* **blend** – mixes the colour change with the original colours. At 100%, the effect fully replaces the original colours.

**Example 1: Sliding Rainbow Gradient**

Starting with default settings :&#x20;

1. Leave the node in **Linear** mode (0° angle = horizontal).
2. Leave **wavelength** at 100% (spans the full width, and should be the default).
3. Leave the start and end values as default.&#x20;
4. Enable **repeat**.
5. Add a **Sawtooth Oscillator** to the **offset** setting that goes from 0% to 100%.

***

**Example 2: Black–White–Black Gradient (Pingpong)**

Starting with default settings :&#x20;

1. Leave the node in **Linear** mode (0° angle = horizontal).
2. Leave **wavelength** at 100% (spans the full width, and should be the default).
3. Turn **repeat** off.
4. Set **start brightness** to 0 (black).
5. Set e**nd brightness** to 100 (white).
6. Set **start saturation** and **end saturation** to 0 (converts to greyscale).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Enable **pingpong**.

_Result: the gradient fades from black to white, then back to black across the width._\
Note that if you want the content to keep its hue and saturation, turn OFF Saturation mode. \


***

**Example 3: Rotating Rainbow Wheel (Radial)**

1. Enable **radial** mode.
2. Set **wavelength** to 100% (a full 360° sweep).
3. Turn **repeat** on.
4. Add a **Sawtooth Oscillator** to the **offset** setting that goes from 0% to 100%.

_Result: a seamless colour wheel that continuously rotates around the circle._



## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Wave shift by position

This node applies a wave distortion across your content, shifting points perpendicular to the chosen axis (or radially from the centre).

* **Wavelength** – sets the length of the wave cycle.
  * _Linear mode:_ at 100%, one full cycle spans the full width of the content.
  * _Radial mode:_ at 100%, one full cycle spans the full 360°. (Values are percentages of the circle: 50% = half a turn, 25% = quarter turn, etc.)
* **Size** – controls the amplitude of the wave (how far the content is displaced).
* **Offset** – shifts the wave along the axis (or around the circle in radial mode). This is a percentage of the wavelength, so you can animate it with an **Oscillator Node** to make the wave travel.
* **Radial** – switches from linear to radial mode, so displacement is based on the angle from the centre.
* **Radial Smooth Loop** – adjusts the wavelength so it divides evenly into 100% of the circle, preventing visible seams at the wrap.
* **Triangle** – changes the waveform shape from sine to triangle.
* **Absolute** – takes the absolute value of the wave, creating only upward displacements (folding the negative side over the positive).
* **Angle** – rotates the axis of the wave. 0° = horizontal.



## <img src="../../.gitbook/assets/image (2).png" alt="" data-size="line">  Noise shift by position

This node distorts content using a noise field (like turbulence), shifting points perpendicular to the chosen axis (or radially from the centre). Compared to _Wave Shift_, the result is more organic and random.

* **Detail** – controls how fine the noise is. Higher values = sharper, more detailed variation. Lower values = smoother variation.
* **Wavelength** – sets the scale of the noise pattern.
  * _Linear mode:_ at 100%, one full cycle of noise spans the width of the content.
  * _Radial mode:_ at 100%, one full cycle spans the full 360°.
* **Size** – controls the displacement amount (amplitude of the noise distortion).
* **Offset** – shifts the noise pattern along the axis (or around the circle). This is a percentage of the wavelength, so you can animate it with an **Oscillator Node** to make the noise “flow.”
* **Depth Offset** – moves through the 3D noise field, creating variation over time. This is especially effective when animated with an Oscillator Node.
* **Depth Detail** – controls how detailed the variation is across the depth dimension.
* **Absolute** – takes the absolute value of the noise, folding negative values into positives (producing only one-sided displacement).
* **Radial** – switches from linear to radial mode, so displacement is based on angle from the centre.
* **Radial Smooth Loop** – adjusts wavelength so it divides evenly into 100% of the circle, preventing visible seams in radial mode.

