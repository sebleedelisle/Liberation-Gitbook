---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Beskrivelse

* **hue, saturation, brightness** - farveværdierne, se [Farveindstillinger og HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - farvetonen ændres ikke
  * FIXED - elementernes farvetone sættes til værdien for hue
  * SHIFT - elementernes farvetone forskydes med værdien, så elementer med forskellige farver fortsat er forskellige, men blot forskydes langs farvetonen.
* **saturation mode** -
  * OFF - mætningen ændres ikke
  * FIXED - mætningen fastsættes til den angivne værdi.
* **brightness mode** -
  * OFF - lysstyrken ændres ikke
  * FIXED - elementernes lysstyrke sættes til værdien for brightness
  * MULTIPLY - elementernes lysstyrke kombineres med værdien for brightness, så hvis de blinker, bliver de ved med at blinke, men kun op til den lysstyrke, der er angivet her.
* **blend** - hvor kraftigt Colour change anvendes. 0% er slet ikke, 100% er fuldt, og 50% er en kombination af den eksisterende farve og de nye værdier.
