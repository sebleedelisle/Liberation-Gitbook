---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Description

* **hue, saturation, brightness** - les valeurs de couleur, voir [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - la teinte n’est pas modifiée
  * FIXED - la teinte des éléments est définie sur la valeur de teinte
  * SHIFT - la teinte des éléments est décalée selon la valeur indiquée. Ainsi, les éléments de couleurs différentes restent différents, mais sont simplement décalés le long de la teinte.
* **saturation mode** -
  * OFF - la saturation n’est pas modifiée
  * FIXED - la saturation est fixée à la valeur spécifiée.
* **brightness mode** -
  * OFF - la luminosité n’est pas modifiée
  * FIXED - la luminosité des éléments est définie sur la valeur de luminosité
  * MULTIPLY - la luminosité des éléments est combinée avec la valeur de luminosité. Ainsi, s’ils clignotent, ils continuent de clignoter, mais seulement jusqu’à la luminosité indiquée ici.
* **blend** - définit l’intensité d’application du changement de couleur : 0 % signifie aucun effet, 100 % l’effet complet, et 50 % une combinaison entre la couleur existante et les nouvelles valeurs.
