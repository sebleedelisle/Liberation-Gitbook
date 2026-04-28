---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Modificateurs basés sur la position

Cette famille de nodes modifie le contenu en fonction de la position. Par défaut, l’effet est appliqué le long d’un axe horizontal (de gauche à droite), mais vous pouvez faire pivoter cet axe à n’importe quel angle. Chaque node inclut aussi un mode _radial_, dans lequel l’effet est piloté par l’angle de chaque point par rapport au centre.

* **Colour Changer by Position** – décale les couleurs le long de l’axe choisi, ou autour de l’angle radial.\
  \&#xNAN;_Exemple : créez un dégradé arc-en-ciel qui traverse une ligne, ou utilisez le mode radial sur un cercle pour produire un effet de roue chromatique._
* **Wave Shift by Position** – applique une distorsion en onde sinusoïdale, en décalant le contenu verticalement (ou perpendiculairement à l’axe choisi).\
  \&#xNAN;_Exemple : faites onduler une ligne comme de l’eau, ou utilisez le mode radial pour faire pulser un cercle vers l’extérieur depuis le centre._
* **Noise Shift by Position** – applique une distorsion par bruit simplex, en décalant le contenu verticalement (ou perpendiculairement à l’axe choisi).\
  \&#xNAN;_Exemple : voir l’exemple de Wave Shift, mais avec un caractère plus organique et aléatoire, idéal pour ajouter une variation naturelle._

## &#x20;Changement de couleur par position

Ce node applique des changements de couleur à votre contenu en fonction de la position. Par défaut, l’axe est horizontal (0°), mais vous pouvez le faire pivoter ou passer en mode radial.

* **wavelength** – définit la taille du cycle de couleur répété.
  * _Mode linéaire :_ à 100 %, un cycle complet couvre toute la largeur du contenu.
  * _Mode radial :_ à 100 %, un cycle complet couvre tout le cercle (360°). Les valeurs sont des pourcentages du cercle : par exemple, 50 % = un demi-cercle (180°).
* **offset** – décale le point de départ du cycle de couleur, en pourcentage de la longueur d’onde. Vous pouvez le moduler (par exemple avec un oscillateur en dent de scie) pour faire défiler les couleurs de façon fluide.
* **repeat** – lorsque cette option est activée, le cycle se répète sur le contenu. Si elle est désactivée, le dégradé n’est appliqué qu’une seule fois : tout ce qui se trouve avant le début prend la couleur de début, et tout ce qui se trouve après la fin prend la couleur de fin.
* **pingpong** – lorsque cette option est activée, chaque répétition alterne de direction, ce qui crée un effet miroir. Si _Repeat_ est désactivé, le dégradé avance puis revient une seule fois. _Remarque : en mode Pingpong, la longueur d’onde couvre à la fois l’aller et le retour._
* **linear angle** – fait pivoter l’axe de l’effet. 0° = horizontal.
* **radial** – passe en mode radial, en appliquant les couleurs selon l’angle depuis le centre.
* **radial smooth loop** – ajuste automatiquement la longueur d’onde pour qu’elle se divise exactement dans 100 % du cercle, afin d’éviter une jointure visible à l’endroit où le cycle se referme.

**Modes de couleur**

Ces modes déterminent quels aspects des ajustements de couleur sont appliqués au contenu. Voir aussi : [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – la teinte reste inchangée.
  * _FIXED_ – la teinte est forcée à une valeur fixe.
  * _SHIFTED_ – la teinte est décalée de la valeur indiquée (les éléments de couleurs différentes restent distincts, mais sont décalés ensemble autour de la roue chromatique).
* **saturation mode**
  * _OFF_ – la saturation reste inchangée.
  * _FIXED_ – la saturation est définie sur la valeur indiquée.
* **brightness mode**
  * _OFF_ – la luminosité reste inchangée.
  * _FIXED_ – la luminosité est définie sur la valeur indiquée.
  * _MULTIPLY_ – la luminosité est multipliée par la valeur indiquée. Cela préserve les dynamiques (par exemple, les éléments qui clignotent continuent de clignoter, mais dans la plage de luminosité limitée).

**Valeurs de début / fin**

Ces sliders définissent la plage de couleur appliquée le long de l’axe choisi (ou du balayage radial).

* **start hue** – la teinte au début du dégradé.
* **end hue** – la teinte à la fin du dégradé.
* **start saturation** – la saturation au début.
* **end saturation** – la saturation à la fin.
* **start brightness** – la luminosité au début.
* **end brightness** – la luminosité à la fin.
* **blend** – mélange le changement de couleur avec les couleurs d’origine. À 100 %, l’effet remplace entièrement les couleurs d’origine.

**Exemple 1 : dégradé arc-en-ciel glissant**

En partant des réglages par défaut :

1. Laissez le node en mode **Linear** (angle de 0° = horizontal).
2. Laissez **wavelength** à 100 % (couvre toute la largeur, ce qui devrait être le réglage par défaut).
3. Laissez les valeurs de début et de fin par défaut.
4. Activez **repeat**.
5. Ajoutez un **Sawtooth Oscillator** au réglage **offset**, allant de 0 % à 100 %.

***

**Exemple 2 : dégradé noir–blanc–noir (Pingpong)**

En partant des réglages par défaut :

1. Laissez le node en mode **Linear** (angle de 0° = horizontal).
2. Laissez **wavelength** à 100 % (couvre toute la largeur, ce qui devrait être le réglage par défaut).
3. Désactivez **repeat**.
4. Réglez **start brightness** sur 0 (noir).
5. Réglez **end brightness** sur 100 (blanc).
6. Réglez **start saturation** et **end saturation** sur 0 (convertit en niveaux de gris).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Activez **pingpong**.

_Résultat : le dégradé passe du noir au blanc, puis revient au noir sur toute la largeur._\
Notez que si vous voulez que le contenu conserve sa teinte et sa saturation, désactivez Saturation mode (OFF). \\

***

**Exemple 3 : roue arc-en-ciel en rotation (Radial)**

1. Activez le mode **radial**.
2. Réglez **wavelength** sur 100 % (un balayage complet de 360°).
3. Activez **repeat**.
4. Ajoutez un **Sawtooth Oscillator** au réglage **offset**, allant de 0 % à 100 %.

_Résultat : une roue chromatique sans jointure qui tourne en continu autour du cercle._

## &#x20;Décalage par onde selon la position

Ce node applique une distorsion en onde à votre contenu, en décalant les points perpendiculairement à l’axe choisi (ou radialement depuis le centre).

* **Wavelength** – définit la longueur du cycle de l’onde.
  * _Mode linéaire :_ à 100 %, un cycle complet couvre toute la largeur du contenu.
  * _Mode radial :_ à 100 %, un cycle complet couvre les 360° entiers. (Les valeurs sont des pourcentages du cercle : 50 % = un demi-tour, 25 % = un quart de tour, etc.)
* **Size** – contrôle l’amplitude de l’onde (la distance de déplacement du contenu).
* **Offset** – décale l’onde le long de l’axe (ou autour du cercle en mode radial). Il s’agit d’un pourcentage de la longueur d’onde, ce qui vous permet de l’animer avec un **Oscillator Node** pour faire voyager l’onde.
* **Radial** – passe du mode linéaire au mode radial, afin que le déplacement soit basé sur l’angle depuis le centre.
* **Radial Smooth Loop** – ajuste la longueur d’onde pour qu’elle se divise exactement dans 100 % du cercle, afin d’éviter les jointures visibles au point de bouclage.
* **Triangle** – change la forme d’onde de sinusoïdale à triangulaire.
* **Absolute** – prend la valeur absolue de l’onde, ce qui crée uniquement des déplacements vers le haut (en repliant la partie négative sur la partie positive).
* **Angle** – fait pivoter l’axe de l’onde. 0° = horizontal.

## &#x20;Décalage par bruit selon la position

Ce node déforme le contenu à l’aide d’un champ de bruit (comme une turbulence), en décalant les points perpendiculairement à l’axe choisi (ou radialement depuis le centre). Par rapport à _Wave Shift_, le résultat est plus organique et aléatoire.

* **Detail** – contrôle la finesse du bruit. Des valeurs élevées produisent des variations plus nettes et plus détaillées. Des valeurs faibles produisent des variations plus douces.
* **Wavelength** – définit l’échelle du motif de bruit.
  * _Mode linéaire :_ à 100 %, un cycle complet de bruit couvre la largeur du contenu.
  * _Mode radial :_ à 100 %, un cycle complet couvre les 360° entiers.
* **Size** – contrôle l’amplitude du déplacement (amplitude de la distorsion par bruit).
* **Offset** – décale le motif de bruit le long de l’axe (ou autour du cercle). Il s’agit d’un pourcentage de la longueur d’onde, ce qui vous permet de l’animer avec un **Oscillator Node** pour faire « s’écouler » le bruit.
* **Depth Offset** – se déplace dans le champ de bruit 3D, en créant une variation dans le temps. C’est particulièrement efficace lorsqu’il est animé avec un Oscillator Node.
* **Depth Detail** – contrôle le niveau de détail de la variation dans la dimension de profondeur.
* **Absolute** – prend la valeur absolue du bruit, en repliant les valeurs négatives vers les positives (ce qui produit uniquement un déplacement d’un seul côté).
* **Radial** – passe du mode linéaire au mode radial, afin que le déplacement soit basé sur l’angle depuis le centre.
* **Radial Smooth Loop** – ajuste la longueur d’onde pour qu’elle se divise exactement dans 100 % du cercle, afin d’éviter les jointures visibles en mode radial.
