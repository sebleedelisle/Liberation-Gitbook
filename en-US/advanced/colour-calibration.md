---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Color calibration

Color calibration ensures your projector’s red, green and blue lasers output light in a smooth and predictable way at all brightness levels. Different projectors can have non-linear brightness curves, meaning that 50% red may look far brighter or dimmer than half the intensity of 100% red. Calibration corrects this so colors mix cleanly, gradients look smooth, and whites are balanced.

#### Warming up your projector

Laser diodes change behavior as they warm up. Always let your projector stabilize before calibration:

* Project a bright frame such as the **White rectangle test pattern (11)** for at least **15–20 minutes**.
* This ensures the color balance you set will stay consistent during a show.

#### How the calibration test works

Use the test patterns for calibration (see [Test patterns](../output-view/test-patterns.md "mention"))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Each of these shows four moving lines:

* **Top line** – 100% brightness at full speed
* **Second line** – 75% brightness at 75% speed
* **Third line** – 50% brightness at 50% speed
* **Fourth line** – 25% brightness at 25% speed

Because both brightness _and speed_ are scaled together, the lines should all look the same brightness. If one looks lighter or darker, adjust the corresponding slider until they match.

Each test pattern also has a fifth line at **0% brightness** which shouldn't be visible. This is used to correct for lasers that don’t output any light at very low levels. If your laser remains invisible at low brightness, gradually increase the **0% setting** until the line is just visible, then back it off slightly until it disappears again. The goal is to find the threshold where the laser starts to light, then stay just below it - so your fades start naturally without cutting off the bottom range.

#### Using the Color Calibration panel

The panel gives you independent controls for each channel (red, green, blue) at 100, 75, 50, 25, and 0% levels.

1. **Select a test pattern** (start with red).
2. **Adjust the sliders** so the 100, 75, 50 and 25% lines look the same brightness.
3. **Tweak the 0% slider** if the “off” line is still faintly visible.
4. **Repeat for green and blue.**
5. Switch to the **White test pattern (8)**. All four lines should look equal, and the white should appear neutral (not tinted).

#### Adjusting the white balance

You can also use this system to adjust **white balance**. After calibrating each channel individually, switch to the **White test pattern (8)**. If the output looks tinted (for example too green or too blue), adjust the relative levels of the red, green and blue channels until the lines appear neutral white. Even if your lasers are quite mismatched in power, calibration will still help bring them closer together and produce a cleaner, more balanced mix of colors.

#### Saving your calibration

* Use **Store** to overwrite the current preset.
* Use **Store As** to create a new preset (useful if you work with multiple lasers).
