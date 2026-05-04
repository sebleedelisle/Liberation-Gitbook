---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effets

Le système d’effets de Liberation est une manière ludique et polyvalente de modifier la sortie des clips en temps réel. Les effets sont entièrement flexibles et peuvent servir à faire clignoter l’ensemble de la sortie, la faire tourner, changer les couleurs, ou même la déplacer de façon aléatoire !

Tout ce que vous pouvez faire dans l’éditeur de clip peut être utilisé comme effet. En fait, les effets se modifient avec exactement le même éditeur de nœuds que les clips ! Voir [Effets](effects.md#editing-effects "mention"). Les possibilités créatives sont quasiment infinies.

Les boutons d’effets par défaut 1 à 8 se trouvent sous les boutons de zone, et les effets 9 à 24 sont les petits boutons situés en bas.

#### Appliquer un effet

Appuyez sur un bouton d’effet pour activer ou désactiver l’effet, ou mieux encore, utilisez les faders 1 à 8 de l’APC40 pour faire entrer et sortir les effets progressivement. Pour faire apparaître progressivement un effet sans APC40, cliquez sur le bouton et faites glisser vers le haut ou vers le bas. Vous pouvez aussi faire un clic droit sur le bouton d’effet et ajuster le curseur de niveau.

{% hint style="warning" %}
Appuyer sur le bouton d’effet active immédiatement cet effet. Notez toutefois que si le niveau est réglé sur zéro, rien ne se passera ! Cliquez sur le bouton et faites glisser pour modifier le niveau, ou faites un clic droit et utilisez le curseur _level_, ou utilisez les faders de l’APC40.
{% endhint %}

#### Effets et délai de zone du clip

Les effets reprennent le réglage de délai de zone de chaque clip en cours de lecture. Ainsi, si votre clip possède un délai qui se déplace de gauche à droite et que vous ajoutez l’effet de clignotement, le clignotement sera lui aussi retardé de gauche à droite.

{% hint style="info" %}
La façon dont le délai de zone du clip est hérité par les effets fait partie de ces choses extrêmement difficiles à décrire, mais évidentes dès que vous les essayez !

Je dirais même que c’est l’un des outils les plus amusants et créatifs intégrés à Liberation. Essayez-le et vous verrez ce que je veux dire !
{% endhint %}

#### Paramètres d’effet

Ajoutez un paramètre à votre effet avec un _Parameter node_. Le système Parameter permet d’ajuster depuis l’extérieur plusieurs réglages à l’intérieur de votre effet. Voir [Parameter Control](clip-editor/oscillators/parameter-control.md "mention") pour plus d’informations.

Utilisez les contrôleurs rotatifs 1 à 8 pour ajuster le _parameter_ de chaque effet. Vous pouvez aussi faire un clic droit sur le bouton d’effet et ajuster le ou les curseurs de paramètre. Le changement de paramètre produit des résultats différents selon la configuration de l’effet. Consultez la liste ci-dessous pour connaître les effets par défaut et l’action de leurs paramètres.

{% hint style="info" %}
Les contrôleurs rotatifs 1 à 8 se trouvent en haut de l’APC40 Mk2 et en haut à droite sur le Mk1. Voir aussi : [Référence APC40](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
Les petits nombres affichés sur les boutons d’effet indiquent le _level_ et le _parameter_ de l’effet. Le _level_ est contrôlé par le fader de l’APC40, ou en cliquant sur le bouton et en faisant glisser. Le paramètre se règle avec les contrôleurs rotatifs de l’APC40, ou par clic droit pour l’ajuster à la souris.
{% endhint %}

#### Les effets par défaut

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applique un mouvement chaotique à la sortie du clip. Le paramètre ajuste l’intensité/la vitesse du chaos.
2. **Sine wave** :\
   Déforme tout le contenu selon une onde sinusoïdale en mouvement. Le paramètre ajuste la longueur d’onde.
3. **Rotation** :\
   Fait tourner l’ensemble de la sortie. Le paramètre ajuste la vitesse de rotation.
4. **Horizontal flip** :\
   Compresse et étire l’ensemble de la sortie horizontalement. Le paramètre ajuste la vitesse.
5. **Scale** :\
   Redimensionne l’ensemble de la sortie de manière répétée, de la taille complète à zéro. Le paramètre ajuste la vitesse.
6. **Hue** :\
Modifie la teinte de l’ensemble de la sortie, sans changer la saturation (c.-à-d. que tout ce qui est blanc reste blanc). Le paramètre ajuste la teinte.
7. **Saturation and hue** :\
Modifie la teinte de l’ensemble de la sortie et sature aussi entièrement la couleur (c.-à-d. que tout ce qui est blanc prend la couleur). Le paramètre ajuste la teinte.
8. **Flash** :\
   Fait clignoter de manière répétée la luminosité de l’ensemble de la sortie, du maximum à zéro. Le paramètre ajuste la vitesse de clignotement.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Il existe 16 effets de couleur supplémentaires sur la rangée du bas, qui appliquent des valeurs prédéfinies de teinte et de saturation.

Notez qu’il s’agit des effets par défaut, mais qu’ils peuvent être modifiés pour faire presque tout ce que vous voulez !

### Appliquer aux groupes

Vous pouvez choisir les groupes affectés par l’effet. Faites un clic droit et activez ou désactivez les cases de groupe intitulées _Apply to groups_.

J’utilise principalement cette configuration lorsque je travaille séparément avec des graphismes Canvas et des faisceaux laser. J’assigne tous les clips Canvas au groupe 5, puis j’exclus ce groupe des effets que je ne veux pas appliquer à ces clips graphiques.

Vous pouvez aussi l’utiliser en live pour appliquer deux changements de couleur différents à deux groupes de lasers en même temps. Créez deux effets de changement de couleur et sélectionnez les groupes de clips auxquels chacun doit s’appliquer.

### Groupe MX

Abréviation de _Mutually Exclusive_, c’est une manière de regrouper des effets de sorte qu’un seul effet du groupe puisse être actif à la fois. Remarquez qu’un seul des effets de changement de couleur par défaut peut être actif en même temps. C’est parce qu’ils sont tous dans MX Group 1.

Cette fonctionnalité est désactivée si le réglage _MX Group_ est défini sur 0.

### Modifier les effets

Faites un clic droit sur n’importe quel effet, puis cliquez sur le bouton _EDIT EFFECT_ pour ouvrir l’éditeur d’effet. Notez que cet éditeur est identique à l’éditeur de clip !

Modifiez votre effet de la même manière que vous modifieriez n’importe quel clip. Voir [Le Clip Editor](clip-editor/ "mention").

Vous devez avoir au moins un nœud de création ; cela peut être n’importe quoi (ligne, cercle, forme, même du texte !), mais il est préférable de choisir quelque chose qui a le plus de sens dans l’aperçu du bouton d’effet.

Lorsque des effets sont appliqués, tous les nœuds de création de l’effet sont remplacés par la sortie des clips actuellement en lecture.

{% hint style="warning" %}
Pour des raisons techniques extrêmement fastidieuses, les nodes "trails" ne sont pas activés à l’intérieur d’un effet. Il en va de même pour le réglage "delay" à l’intérieur des nodes pattern (ils utilisent le même système). Cela sera corrigé dans de futures versions.
{% endhint %}
