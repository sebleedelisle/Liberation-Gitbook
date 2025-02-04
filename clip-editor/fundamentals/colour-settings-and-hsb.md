# 🟦 Colour settings and HSB

Colour within Liberation is defined as HSB rather than RGB. This may be unfamiliar to you but I find it to be a much more intuitive system once you get used to it.&#x20;

{% hint style="info" %}
If you prefer using RGB you can click on the colour square in any colour setting. This opens the colour editor window which gives you options for RGB and HSB.&#x20;
{% endhint %}

### HSB - Hue, Saturation and Brightness

#### Hue &#x20;

The colour hue ranges between 0 and 255. 0 is red, and as you increase the value you'll pass through every hue in the rainbow, orange, yellow, green, cyan, blue, purple, magenta and then back to red at 255.&#x20;

As this is a loop you can use a triangle wave to cycle through every colour.&#x20;

#### Saturation

This setting adjusts the saturation or vividness of your colour. In other words, how _colourful_ it is and ranges from 0 to 255. Set your saturation to 0 for greys, and 255 for full rainbow colours. Somewhere in the middle will give you pastel washed-out colours.&#x20;

{% hint style="info" %}
Apologies to my US friends for the additional vowel in the word colour. Liberation is made in England so British English is the default. In the future I hope to provide translations to French, Spanish, German, Italian, Simplified Chinese, and yes, even US English. :innocent:
{% endhint %}

#### Brightness

Probably the simplest to understand, 0 is completely black, 255 is full brightness.&#x20;

### Example usage

#### Rainbow cycle :&#x20;

Set _Brightness_ and _Saturation_ to 255. Connect a _Sawtooth_ oscillator to your _Hue_ socket, and adjust its range from 0 to 255.&#x20;

#### Pulsing brightness :&#x20;

Connect a _Sawtooth_ oscillator to your _Brightness_ socket, and adjust its range from 255 to 0. You can further adjust the clamp min and max to check the duration of the change. And then use the easing functions to further refine the animation.&#x20;

#### Hard flash / strobe :&#x20;

Select a colour using the _Hue_ and _Saturation_ or by clicking on the colour picker. Connect a _Square Wave_ oscillator your _Brightness_ socket, adjust its range from 255 to 0.&#x20;

#### Cycle across custom range of hues :&#x20;

Set _Brightness_ and _Saturation_ to 255. Connect a _Triangle Wave_ oscillator to your _Hue_ socket, and adjust its range :&#x20;

* for blue to cyan use a range of 70 to 128
* for red to yellow use a range of 0 to 40
* for red to magenta use a range of 255 to 220



