# 🟦 Effects

The effects system in Liberation is a fun and versatile way of changing the clip output in real-time. Effects are completely flexible and can be used to make everything flash on and off, spin around,  change colours, or even fly around randomly!&#x20;

Anything that you can do in the clip editor can be used as an effect. In fact, effects are edited with the exact same node editor as clips! See [#editing-effects](effects.md#editing-effects "mention"). The creative possibilities are virtually infinite.&#x20;

The default effects buttons 1-8 are under the zone buttons, and effects 9-24 are the small buttons at the bottom.&#x20;

#### Applying an effect

Press an effect button to toggle the effect, or even better, using the APC40 sliders 1-8 to fade effects in and out. To fade in an effect without an APC40, click and drag up and down on the button. Or right click on the effect button and adjust the level slider.&#x20;

{% hint style="warning" %}
Pressing the effect button will immediately activate that effect. However, note that if the level parameter is set to zero, nothing with happen! Click/drag the button to change the level, or right click and use the _level_ slider, or use the APC40 faders.
{% endhint %}

#### Effects and the clip's zone delay

Effects pick up the zone delay setting for each currently running clip. So if your clip has a delay that moves from left to right, and you add the flashing effect, the flash also is delayed from left to right.&#x20;

{% hint style="info" %}
How the clip's zone delay is inherited by effects is one of those things that is extremely hard to describe but obvious when you try it!

I would argue that it is one of the most fun and creative tools built in to Liberation. Give it a try and you'll see what I mean!&#x20;
{% endhint %}

#### Effect parameters

Add a parameter to your effect with a _Parameter node._ The Parameter system is a way to adjust multiple settings inside your effect from the outside. See [parameter-node.md](clip-editor/parameter-node.md "mention") for more information.&#x20;

Use the rotary controllers 1-8 to adjust the _parameter_ for each effect. Or right-click the effect button and adjust the parameter slider(s). The parameter change does different things dependent on how the effect is set up. See the list below for the default effects and what their parameters do.

{% hint style="info" %}
Rotary controllers 1-8 are along the top of an APC40 Mk2 and on the top right on the Mk1. See also: [apc40-reference.md](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
The small numbers you see on the effect buttons refer to the _level_ and _parameter_ of the effect.  The _level_ is controlled by the fader on the APC40 or you can click-drag on the button. The parameter is adjusted by the rotaries on the APC40 or you can right-click to adjust with the mouse.&#x20;
{% endhint %}



#### The default effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applies a chaotic movement to the clip output. The parameter adjusts the amount/speed of chaos.
2. **Sine wave** :\
   Warps all the content across a moving sine wave. The parameter adjusts the wavelength.
3. **Rotation** :\
   Spins everything around. The parameter adjusts the spin speed.
4. **Horizontal flip** :\
   Squishes and stretches everything horizontally. The parameter adjusts the speed.
5. **Scale** :\
   Repeatedly scales everything from full to zero. The parameter adjusts the speed.
6. **Hue** :\
   Changes the hue of everything, but doesn't change the saturation (ie anything white stays white). The parameter adjusts the hue.
7. **Saturation and hue** :\
   Changes the hue of everything and also fully saturates the colour (ie anything white changes to the colour). The parameter adjusts the hue.
8. **Flash** :\
   Repeatedly flashes the brightness of everything from full to zero. The parameter adjusts the flash speed.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

There are a further 16 colour effects along the bottom row to apply pre-set hue and saturation values.

Note that these are the default effects but they can be edited to do almost whatever you want!

### Apply to groups

You can choose which groups are affected by the effect. Right click and toggle the group check boxes labelled _Apply to groups._&#x20;

I primarily use this setup when working with canvas graphics and laser beams separately. I assign all canvas clips to group 5 and then exclude this group from effects that I don't want to affect these graphical clips.&#x20;

You could also use it to live apply 2 different colour changes to 2 groups of lasers at once. Create two colour change effects and select which clip groups each one is applied ot.&#x20;

### MX group

Short for _Mutually Exclusive_ this is a way to group effects together in such a way that only one effect in the group can be active at the same time. Notice how only one of the default colour changing effects can be active at once. This is because they are all in MX Group 1.&#x20;

This functionality is disabled if the _MX Group_ setting is 0.

### Editing effects

Right click on any effect, and click the _EDIT EFFECT_ button to open the effect editor. Notice that this editor is identical the clip editor!&#x20;

Edit your effect in the same way that you would edit any clip. See [clip-editor](clip-editor/ "mention").

You need to have at least one creator node; this can be anything (line, circle, shape, even text!), but you should probably choose something that makes the most sense in the effect button preview.&#x20;

When effects are applied, all creator nodes in the effect are substituted with the output of the currently running clips.&#x20;

{% hint style="warning" %}
For extremely tedious technical reasons, the "trails" nodes are not enabled when inside a effect. The same applies for the "delay" setting inside pattern nodes (they use the same system). This will be fixed in future revisions.&#x20;
{% endhint %}

###
