---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Paramètres de couleur et HSB

Dans Liberation, la couleur est définie en HSB plutôt qu’en RGB. Cela peut vous sembler inhabituel, mais je trouve ce système beaucoup plus intuitif une fois qu’on s’y est habitué.

{% hint style="info" %}
Si vous préférez utiliser RGB, vous pouvez cliquer sur le carré de couleur dans n’importe quel paramètre de couleur. Cela ouvre le panneau d’édition de couleur, qui propose des options RGB et HSB.
{% endhint %}

### HSB - Hue, Saturation et Brightness

#### Hue

La teinte de la couleur va de 0 à 255. 0 correspond au rouge, puis, en augmentant la valeur, vous parcourez toutes les teintes de l’arc-en-ciel : orange, jaune, vert, cyan, bleu, violet, magenta, puis retour au rouge à 255.

Comme il s’agit d’une boucle, vous pouvez utiliser une onde triangulaire pour parcourir toutes les couleurs.

#### Saturation

Ce paramètre ajuste la saturation, ou la vivacité, de votre couleur. Autrement dit, à quel point elle est _colorée_. La valeur va de 0 à 255. Réglez la saturation sur 0 pour obtenir des gris, et sur 255 pour des couleurs d’arc-en-ciel pleinement saturées. Une valeur intermédiaire donne des couleurs pastel plus délavées.

{% hint style="info" %}
Désolé pour mes amis américains concernant la voyelle supplémentaire dans le mot colour. Liberation est développé en Angleterre, donc l’anglais britannique est la langue par défaut. À l’avenir, j’espère proposer des traductions en français, espagnol, allemand, italien, chinois simplifié et, oui, même en anglais américain. :innocent:
{% endhint %}

#### Brightness

C’est probablement le plus simple à comprendre : 0 correspond au noir complet, 255 à la luminosité maximale.

### Exemple d’utilisation

#### Cycle arc-en-ciel :

Réglez _Brightness_ et _Saturation_ sur 255. Connectez un oscillateur _Sawtooth_ à votre socket _Hue_, puis ajustez sa plage de 0 à 255.

#### Luminosité pulsée :

Connectez un oscillateur _Sawtooth_ à votre socket _Brightness_, puis ajustez sa plage de 255 à 0. Vous pouvez ensuite ajuster les valeurs clamp min et max pour contrôler la durée du changement. Utilisez ensuite les fonctions d’easing pour affiner davantage l’animation.

#### Flash dur / stroboscope :

Sélectionnez une couleur avec _Hue_ et _Saturation_, ou en cliquant sur le sélecteur de couleur. Connectez un oscillateur _Square Wave_ à votre socket _Brightness_, puis ajustez sa plage de 255 à 0.

#### Cycle sur une plage de teintes personnalisée :

Réglez _Brightness_ et _Saturation_ sur 255. Connectez un oscillateur _Triangle Wave_ à votre socket _Hue_, puis ajustez sa plage :

* pour passer du bleu au cyan, utilisez une plage de 70 à 128
* pour passer du rouge au jaune, utilisez une plage de 0 à 40
* pour passer du rouge au magenta, utilisez une plage de 255 à 220
