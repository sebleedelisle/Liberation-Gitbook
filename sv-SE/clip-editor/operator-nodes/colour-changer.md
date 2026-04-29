---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Beskrivning

* **hue, saturation, brightness** - färgvärdena, se [Färginställningar och HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - färgtonen ändras inte
  * FIXED - elementens färgton ställs in på värdet hue
  * SHIFT - elementens färgton förskjuts med värdet, så element med olika färger förblir olika, men flyttas längs färgtonsskalan.
* **saturation mode** -
  * OFF - mättnaden ändras inte
  * FIXED - mättnaden låses till det angivna värdet.
* **brightness mode** -
  * OFF - ljusstyrkan ändras inte
  * FIXED - elementens ljusstyrka ställs in på värdet brightness
  * MULTIPLY - elementens ljusstyrka kombineras med värdet brightness, så om de blinkar fortsätter de att blinka, men bara upp till den ljusstyrka som anges här.
* **blend** - hur starkt colour changer tillämpas. 0 % är inte alls, 100 % är fullt ut och 50 % är en kombination av den befintliga färgen och de nya värdena.
