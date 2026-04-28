---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Beskrivelse

* **hue, saturation, brightness** – fargeverdiene, se [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** –
  * OFF – hue endres ikke
  * FIXED – hue for elementer settes til hue-verdien
  * SHIFT – hue for elementer forskyves med verdien, slik at elementer med ulike farger fortsatt er ulike, men bare forskyves langs hue-verdien.
* **saturation mode** –
  * OFF – saturation endres ikke
  * FIXED – saturation låses til den angitte verdien.
* **brightness mode** –
  * OFF – brightness endres ikke
  * FIXED – brightness for elementer settes til brightness-verdien
  * MULTIPLY – brightness for elementer kombineres med brightness-verdien, slik at hvis de blinker, vil de fortsatt blinke, men bare opp til brightness som er angitt her.
* **blend** – hvor sterkt colour changer brukes. 0 % er ikke i det hele tatt, 100 % er fullt, og 50 % er en kombinasjon av den eksisterende fargen og de nye verdiene.
