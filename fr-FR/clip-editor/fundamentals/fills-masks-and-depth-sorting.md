---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Remplissages, masques et tri en profondeur

### Contours, remplissages et masques

Vous remarquerez que certains nœuds Creator disposent d’une option _Fill state_ ; vous pouvez les dessiner avec un contour (_stroke_), comme un masque (qui recouvre les éléments en dessous), ou les deux.

Lorsque vous rendez une forme comme un masque, c’est comme si elle était remplie en noir : tout ce qui se trouve en dessous est masqué.

{% hint style="info" %}
Dessiner une ligne (ou _stroke_) avec un laser est assez simple : vous scannez le laser du début de la ligne jusqu’à sa fin. Et voilà votre ligne !

Les formes remplies sont plus difficiles ; si vous voulez remplir une forme avec de la couleur, vous pourriez hachurer manuellement en traçant des lignes pour la remplir, mais Liberation ne peut pas encore le faire automatiquement. Et même si c’était le cas, vous verriez toujours les autres lignes situées en dessous apparaître à travers.

En revanche, ce que nous pouvons faire, c’est remplir les formes en _noir_. En arrière-plan, Liberation effectue tous les calculs nécessaires pour supprimer le contenu situé sous la forme remplie de noir. Et croyez-moi, c’est délicat !

Mais cela fonctionne très bien et donne l’illusion d’une forme remplie de noir.
{% endhint %}

### Tri en profondeur

Comme certaines formes peuvent _recouvrir_ d’autres formes, Liberation doit les trier selon leur profondeur. Par défaut, les éléments sont triés en profondeur selon leur position z. S’ils se trouvent à la même position z, ils sont triés selon leur position de calque, que vous pouvez modifier avec les boutons _MOVE TO FRONT_ et _MOVE TO BACK_ dans chaque creator.
