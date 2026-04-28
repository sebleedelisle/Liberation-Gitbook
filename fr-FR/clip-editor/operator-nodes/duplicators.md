---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Crée une copie en miroir de tout le contenu. Par défaut, l’axe du miroir est une ligne verticale au centre.

* **angle** - angle de la ligne de l’axe du miroir.
* **offset position** - décale l’axe du miroir (déplacement perpendiculaire à l’axe).
* **delay** - retard temporel du contenu en miroir. Notez que cela n’aura d’effet que si le contenu comporte une forme d’animation.

#### Options 3D (disponibles lorsque 3D est sélectionné)

* **angle X / angle Y** - l’axe du miroir devient un plan, et vous pouvez utiliser ces réglages pour faire pivoter ce plan en 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplique le contenu selon un motif circulaire.

* **radius** - distance depuis le point central à laquelle le contenu est décalé avant la rotation.
* **count** - nombre de copies de l’objet à créer.
* **use each objects pivot point** - lorsque cette option est sélectionnée, chaque élément est décalé et pivoté autour de son propre point central. (N’a d’effet que lorsque plusieurs éléments sont dupliqués)
* **delay** - ajoute un retard temporel progressivement plus long à chaque élément dupliqué. Notez que le contenu doit comporter une forme d’animation pour que l’effet soit perceptible.
* **rotation** - rotation de décalage ajoutée aux éléments.

#### Options 3D (disponibles lorsque 3D est sélectionné)

* **rotation x / rotation y** - fait pivoter l’ensemble du motif circulaire autour des axes x et y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplique le contenu selon une grille de lignes et de colonnes.

* **spacing** - distance entre les éléments.
* **count X**- nombre de copies horizontalement (colonnes).
* **count Y**- nombre de copies verticalement (lignes).
* **horizontal alignment** - point de départ des colonnes, LEFT, CENTRE ou RIGHT.
* **vertical alignment** - point de départ des lignes, TOP, MIDDLE ou BOTTOM.
* **delay** - ajoute un retard temporel progressivement plus long à chaque élément dupliqué. Notez que le contenu doit comporter une forme d’animation pour que l’effet soit perceptible.
