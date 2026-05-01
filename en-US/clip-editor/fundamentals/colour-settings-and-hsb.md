---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Color settings and HSB

Color within Liberation is defined as HSB rather than RGB. This may be unfamiliar to you but I find it to be a much more intuitive system once you get used to it.

{% hint style="info" %}
If you prefer using RGB you can click on the color square in any color setting. This opens the color editor panel which gives you options for RGB and HSB.
{% endhint %}

### HSB - Hue, Saturation and Brightness

#### Hue

The color hue ranges between 0 and 255. 0 is red, and as you increase the value you'll pass through every hue in the rainbow, orange, yellow, green, cyan, blue, purple, magenta and then back to red at 255.

As this is a loop you can use a triangle wave to cycle through every color.

#### Saturation

This setting adjusts the saturation or vividness of your color. In other words, how _colorful_ it is and ranges from 0 to 255. Set your saturation to 0 for grays, and 255 for full rainbow colors. Somewhere in the middle will give you pastel washed-out colors.

{% hint style="info" %}
This US English version uses American spelling, but Liberation is made in England, so some screenshots, UI labels, file names, and older references may still use British English.
{% endhint %}

#### Brightness

Probably the simplest to understand, 0 is completely black, 255 is full brightness.

### Example usage

#### Rainbow cycle :

Set _Brightness_ and _Saturation_ to 255. Connect a _Sawtooth_ oscillator to your _Hue_ socket, and adjust its range from 0 to 255.

#### Pulsing brightness :

Connect a _Sawtooth_ oscillator to your _Brightness_ socket, and adjust its range from 255 to 0. You can further adjust the clamp min and max to check the duration of the change. And then use the easing functions to further refine the animation.

#### Hard flash / strobe :

Select a color using the _Hue_ and _Saturation_ or by clicking on the color picker. Connect a _Square Wave_ oscillator your _Brightness_ socket, adjust its range from 255 to 0.

#### Cycle across custom range of hues :

Set _Brightness_ and _Saturation_ to 255. Connect a _Triangle Wave_ oscillator to your _Hue_ socket, and adjust its range :

* for blue to cyan use a range of 70 to 128
* for red to yellow use a range of 0 to 40
* for red to magenta use a range of 255 to 220
