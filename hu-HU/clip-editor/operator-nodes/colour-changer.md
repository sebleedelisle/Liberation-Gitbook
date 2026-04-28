---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Leírás

* **hue, saturation, brightness** - a színértékek, lásd: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - a hue nem módosul
  * FIXED - az elemek hue értéke a megadott hue értékre áll
  * SHIFT - az elemek hue értéke a megadott értékkel eltolódik, így a különböző színű elemek továbbra is különbözőek maradnak, csak a hue érték mentén eltolva.
* **saturation mode** -
  * OFF - a saturation nem módosul
  * FIXED - a saturation a megadott értékre rögzül.
* **brightness mode** -
  * OFF - a brightness nem módosul
  * FIXED - az elemek brightness értéke a megadott brightness értékre áll
  * MULTIPLY - az elemek brightness értéke a brightness értékkel kombinálódik, így ha villognak, továbbra is villogni fognak, de legfeljebb az itt megadott brightness értékig.
* **blend** - meghatározza, milyen erősen érvényesül a színváltó: 0% esetén egyáltalán nem, 100% esetén teljes mértékben, 50% esetén pedig a meglévő szín és az új értékek keveréke.
