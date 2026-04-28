---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Oscillateurs d’onde

## Sur cette page :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Onde en dents de scie](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Onde triangulaire](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Onde sinusoïdale](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Onde carrée](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Bruit](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Réglages des oscillateurs d’onde

Tous les oscillateurs d’onde disposent des réglages suivants :

* **range min / range max** - détermine la plage de valeurs de la propriété contrôlée par l’oscillateur. La propriété est définie sur _range min_ lorsque la forme d’onde est en bas, et sur _range max_ lorsqu’elle est en haut.

{% hint style="info" %}
Par exemple, si vous voulez qu’un point se déplace de gauche à droite entre -100 et 100, connectez l’oscillateur au _connecteur de propriété x_, réglez _min range_ sur -100 et _max range_ sur 100.
{% endhint %}

* **duration** - la durée nécessaire pour effectuer un cycle complet (ou _boucle_). Elle est relative au tempo, en mesures. Ainsi, ¼ correspond à un temps. 1 correspond à une mesure complète, etc.
* **duration multiplier** - multiplie la durée de base par un facteur choisi. Par exemple, si duration est réglé sur une noire et que le multiplicateur est 3, l’oscillateur durera trois noires (une blanche pointée). Les multiplicateurs fractionnaires sont également pris en charge : maintenez _SHIFT_ pendant que vous faites glisser le curseur pour définir des valeurs non entières, ce qui est utile pour les effets de phase ou pour créer de légers décalages temporels.
* **offset** - le décalage de départ de l’onde, exprimé en pourcentage de la durée. Si vous voulez que l’onde commence au quart de sa progression, réglez cette valeur sur 25 %.
* **repeat count** - le nombre de fois que la boucle s’exécute avant de s’arrêter. La valeur par défaut est _FOREVER_, mais vous pouvez la modifier si vous ne voulez pas que l’oscillateur tourne indéfiniment. Après l’arrêt, la propriété prend la valeur située à la fin de l’onde.
* **delay count** - le délai, en temps, avant le démarrage de l’oscillateur. Avant son démarrage, la propriété prend la valeur située au début de l’onde.

{% hint style="info" %}
En utilisant soigneusement _repeat count_ et _delay count_, vous pouvez créer des animations très complexes, presque comme avec une timeline dédiée !
{% endhint %}

## Réglages communs

* **steps** - divise le mouvement en un nombre de pas discrets. Pratique lorsque vous voulez que les propriétés « sautent » d’une valeur à l’autre plutôt que de se déplacer de manière fluide.

{% hint style="info" %}
Notez que les steps sont répartis dans le temps, et non selon la valeur. Ainsi, pour une onde divisée en 4 steps avec une duration de 1 mesure, la propriété changera instantanément à chaque temps.
{% endhint %}

* **clamp min / clamp max -** augmente l’échelle de l’onde au-delà de ses valeurs minimale ou maximale, puis limite le résultat.

{% hint style="info" %}
Le concept de _clamp_ est assez difficile à expliquer, mais imaginez la forme d’onde dépasser le haut ou le bas du graphique, puis être bloquée sur les bords. Je vous recommande d’expérimenter avec ces réglages ! Ils sont très utiles si vous voulez qu’une onde en dents de scie commence plus tard ou se termine plus tôt.
{% endhint %}

* **ease function** - les ondes Sawtooth et Triangle disposent aussi d’une fonction d’assouplissement qui modifie subtilement la courbe d’animation et peut rendre vos animations beaucoup plus expressives !
  * **LINEAR** - valeur par défaut, sans assouplissement : le mouvement est simplement linéaire entre les valeurs min et max.
  * **EASE OUT** - démarre rapidement, puis ralentit en approchant de la fin. Très utile pour simuler la physique, par exemple un ralentissement jusqu’à l’arrêt.
  * **EASE IN** - démarre lentement, puis accélère progressivement. Utile pour simuler une prise d’élan.
  * **EASE IN/OUT** - une combinaison des deux, pour un mouvement très organique.

{% hint style="warning" %}
**Easing -** évitez l’animation linéaire par défaut chaque fois que possible, sauf si vous recherchez précisément un rendu robotique. L’easing peut rendre vos animations beaucoup plus fluides et organiques !
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Onde en dents de scie

Aussi appelée parfois _forme d’onde en rampe_, car elle monte progressivement puis retombe brutalement à la fin de son cycle. C’est probablement l’oscillateur d’onde le plus courant, car il crée une boucle idéale pour faire varier des propriétés comme _hue_ ou _rotation_.

Voir les sections ci-dessus pour :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Spécifique à l’onde Sawtooth :

* **cycle range compensation** - disponible lorsque **steps** est défini, et utile pour faire tourner des valeurs en boucle, par exemple une rotation de 0 à 360. Lorsque ce réglage n’est pas activé, les valeurs de début et de fin sont identiques, ce qui peut provoquer un blocage au point de départ (car 0 et 360 correspondent au même angle). Activez-le pour réduire la plage maximale et corriger la position des steps.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Onde triangulaire

Contrairement à l’_onde en dents de scie_, qui revient brusquement au début à chaque cycle, l’_onde triangulaire_ avance de façon linéaire, puis revient en arrière.

Voir les sections ci-dessus pour :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Onde sinusoïdale

La forme d’onde la plus douce ! Elle oscille délicatement entre deux valeurs, comme un pendule.

Voir les sections ci-dessus pour :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Onde carrée

La forme d’onde la plus simple : elle bascule simplement entre deux valeurs, dans un sens puis dans l’autre !

Voir les sections ci-dessus pour :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Spécifique à l’onde Square :

* **pulse width** - la durée pendant laquelle l’onde reste à sa valeur maximale, par rapport à la durée totale. 50 % est la valeur par défaut, ce qui correspond exactement à moitié-moitié. Si vous voulez qu’elle ne soit « active » qu’un quart du temps, réglez cette valeur sur 25 %. Vous pouvez ajuster le moment où cette impulsion se produit avec la valeur _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Bruit

L’un des points forts de Liberation est sa capacité à générer des effets aléatoires, mais reproductibles. L’oscillateur _noise_ peut être utilisé pour créer un mouvement aléatoire organique en boucle, avec autant de détail ou de jitter que vous le souhaitez.

Voir les sections ci-dessus pour :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Spécifique à Noise :

* **noise type** - l’algorithme utilisé pour générer le bruit.
  * **SIMPLEX** - valeur par défaut, une valeur ondulante qui monte et descend, et se répète en boucle.
  * **RANDOM** - utilise un algorithme de nombres aléatoires plus traditionnel, totalement bruité et chaotique.

{% hint style="info" %}
Le **bruit Simplex** a été conçu par Ken Perlin en 2001 comme une amélioration de son algorithme de « bruit de Perlin », qu’il avait développé en 1983 dans le cadre de son travail sur le film _Tron_ (pour lequel il a remporté un Oscar !)

Ce bruit dit « de gradient » est né de sa frustration face à des images générées par ordinateur auparavant trop « mécaniques ». Dans le monde de la CGI, il est particulièrement efficace pour rendre des nuages, des surfaces d’eau ou même des height-maps pour des terrains réalistes.

Mais dans Liberation, il est surtout utile pour créer des mouvements qui semblent imprévisibles tout en restant fluides et organiques.
{% endhint %}

* **seed** - la valeur utilisée pour créer le bruit. Si l’apparence de l’onde de bruit ne vous convient pas, essayez de modifier cette valeur.

{% hint style="info" %}
Petit fait amusant pour les geeks ! Pour obtenir un bruit Simplex parfaitement bouclé, je parcours un cercle sur un plan de bruit 2D. Et modifier la valeur seed déplace ce plan dans une 3e dimension !
{% endhint %}

* **simplex detail** - modifie le niveau de détail ou de jitter du bruit. Si vous voulez que le motif répété soit moins évident, augmentez la duration et cette valeur.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Crée des formes d’onde entièrement personnalisées. C’est très utile pour créer des animations complexes.

Voir les sections ci-dessus pour :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

En dessous se trouve une liste de positions et de valeurs. La duration est divisée en 64 steps, et vous pouvez placer une valeur à n’importe lequel de ces points.

Chaque step dispose des réglages suivants :

* **Step** - le pas temporel dans la duration. 0 correspond au début et 64 à la fin.
* **Level** - le niveau de l’onde à ce pas temporel. Le niveau est compris entre 0 et 1.
* **Animation type** - le menu déroulant vous permet de choisir comment atteindre ce niveau depuis le step précédent.
  * **None** - aucune transition : saut direct à ce niveau au moment indiqué.
  * **Linear** - un mouvement entièrement linéaire du niveau précédent vers celui-ci.
  * **Ease in / Ease out / Ease in/out** - applique un assouplissement entre le niveau précédent et celui-ci. Voir _ease function_ ci-dessus pour une description des types d’animation.

***
