---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

Déplace tout le contenu le long des axes x, y et/ou z. Notez que le système de coordonnées est centré et s’étend de +/-200 sur les axes x et y. Voir [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **x** - la distance à parcourir sur l’axe x (gauche - droite).
* **y** - la distance à parcourir sur l’axe y (haut - bas).

#### Options 3D (disponibles lorsque 3D est sélectionné)

* **z** - la distance à parcourir sur l’axe z (vers l’arrière et vers l’avant dans l’écran).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Fait pivoter tout le contenu. Les valeurs sont exprimées en degrés. Voir [co-ordinate-system.md](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - l’angle de rotation du contenu dans le sens horaire, en degrés. Tout pivote autour de l’origine (0,0), au centre.
* **pivot point x / pivot point y** - utilisez ces valeurs pour décaler l’origine de la rotation.

#### Options 3D (disponibles lorsque 3D est sélectionné)

* **rotation x** - rotation autour de l’axe x (pitch).
* **rotation y** - rotation autour de l’axe y (yaw).
* **pivot point z** - position de décalage de la rotation sur l’axe z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Met tout le contenu à l’échelle.

* **scale** - le pourcentage d’échelle.
* **scale x / scale y** - si vous voulez redimensionner horizontalement et/ou verticalement, utilisez ces options.

{% hint style="warning" %}
Chaque fois qu’un élément est mis à l’échelle à 0 % sur un axe, il disparaît !
{% endhint %}
