---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Global transformations

In addition to clip transformations (shift x/y, scale x/y) there are Global Transformations that apply to every clip that you run. Open the _Global Transformations_ panel to see them. (This panel is usually in a tab alongside _Clip Settings_).

By default, all of these settings will be reset as soon as there are no clips playing anymore. This reset behavior can be disabled with the _AUTO RESET_ button at the bottom of the _Global Transformations_ panel.

{% hint style="info" %}
Note that Global Transformations do not affect anything in the canvas, only Beam and DMX zones
{% endhint %}

### Scale X/Y

Horizontal and vertical scale, these values are locked together unless you press `Shift`. By default these are also mapped onto APC40 Device Control knobs 4 and 8, and appear in the contextual Parameters panel to the right of the clip deck.

### Shift X/Y

Horizontal and vertical shift. Translates everything horizontally / vertically.

### Spin

Spins all content around the center. A positive value spins in the clockwise direction, a negative value spins counterclockwise. You'll see that this setting affects the _Rotation_ transformation. By default this is mapped to APC40 Device Control knob 3, and appears in the contextual Parameters panel to the right of the clip deck.

### Spin 3D

Spins all content around the Y axis (which is a vertical line in the center). You'll see that this setting affects the _Rotation3D_ transformation. By default this is mapped to APC40 Device Control knob 7, and appears in the contextual Parameters panel to the right of the clip deck.

### Rotation

A rotation around the center, value in degrees.

### Rotation 3D

A rotation around the Y axis (which is a vertical line in the center), value in degrees.

### Auto reset

When turned on, this will reset all of the Global Transformations as soon as all the currently running clips are deactivated. So you can be sure that you won't get any surprises next time you run a clip!
