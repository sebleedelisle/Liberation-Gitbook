---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Kuvaus

* **hue, saturation, brightness** - väriarvot, katso [Väriasetukset ja HSB](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - sävyä ei muuteta
  * FIXED - elementtien sävy asetetaan hue-arvoon
  * SHIFT - elementtien sävyä siirretään annetulla arvolla, joten eriväriset elementit pysyvät edelleen erivärisinä, mutta niiden sävy siirtyy hue-arvon mukaisesti.
* **saturation mode** -
  * OFF - kylläisyyttä ei muuteta
  * FIXED - kylläisyys lukitaan määritettyyn arvoon.
* **brightness mode** -
  * OFF - kirkkautta ei muuteta
  * FIXED - elementtien kirkkaus asetetaan brightness-arvoon
  * MULTIPLY - elementtien kirkkaus yhdistetään brightness-arvoon, joten jos ne vilkkuvat, ne vilkkuvat edelleen, mutta enintään tässä määritettyyn kirkkauteen asti.
* **blend** - kuinka voimakkaasti Colour change otetaan käyttöön. 0 % ei vaikuta lainkaan, 100 % käyttää vaikutusta kokonaan, ja 50 % on yhdistelmä nykyistä väriä ja uusia arvoja.
