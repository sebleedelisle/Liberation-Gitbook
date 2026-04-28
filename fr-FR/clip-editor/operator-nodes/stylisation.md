---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Nœuds de stylisation

## &#x20;Randomise

Crée des copies dispersées des éléments entrants à l’aide d’un champ de bruit cohérent. Autrement dit, il copie et déplace vos formes et vos points de manière contrôlée, avec un rendu « bruité ». Au lieu que tout reste bien rangé au même endroit, vous obtenez plusieurs versions qui se déplacent et se répartissent, comme des particules entraînées dans un flux.

* **count** – nombre de copies par élément entrant (1–20). Avec 1, vous obtenez une seule version légèrement décalée de chaque élément. Des valeurs plus élevées créent plusieurs copies dispersées.
* **noise offset** – parcourt le champ de bruit (0–100%). La boucle est parfaitement continue : en l’animant avec un Oscillator Node, vous obtenez un mouvement fluide et continu de toutes les copies ensemble.
* **noise jitter** – contrôle l’échelle de texture du bruit. Des valeurs faibles produisent des variations larges et douces. Des valeurs élevées donnent un placement plus serré et plus irrégulier. Cela modifie le motif, pas l’intensité.
* **change between points** – contrôle à quel point chaque copie diffère de la précédente. Des valeurs faibles gardent les copies groupées et similaires. Des valeurs élevées les dispersent davantage, avec plus de variation.
* **face direction** – fait pivoter chaque copie pour qu’elle soit orientée dans la direction du déplacement dans le champ de bruit, ce qui produit des flèches/particules alignées avec le flux.
* **amount** – intensité globale de l’effet (0–100%). Met à l’échelle à la fois le déplacement et la rotation issus de face direction.

{% hint style="info" %}
Le nœud randomise est au cœur de l’effet Randomise !
{% endhint %}

## &#x20;Trails

Crée des échos de votre contenu, en laissant derrière l’original des copies qui s’estompent ou changent d’échelle pendant son déplacement.

* **change render profile for trail** – si activé, toutes les copies de traînée utilisent le **render profile** sélectionné. _Voir_ [render-profile.md](../fundamentals/render-profile.md "mention").
* **render profile** – profil à utiliser pour les copies de traînée lorsque l’option ci-dessus est activée. Il est souvent utilisé lorsque le contenu principal est réglé sur **DETAIL**, mais que les échos sont rendus en **FAST** : vous conservez ainsi des détails nets sur les formes principales tout en rendant les traînées plus efficacement.
* **delay** – définit l’espacement entre les copies de traînée en temps musical, mesuré par pas de **1/64 de note**.\
  À titre de repère :
  * 16 = 1/16 de mesure (double-croche)
  * 32 = 1/8 de mesure (croche)
  * 64 = 1/4 de mesure (noire)
  * 128 = 1/2 mesure (blanche)
  * 256 = 1 mesure
* **trail size** – nombre de copies de traînée à dessiner derrière le contenu en direct.
* **freeze trails** – transforme des traînées fluides en une séquence d’instantanés figés. Utile pour créer des effets de traînée saccadés et synchronisés au beat.
* **brightness start / brightness end** – applique la luminosité le long de la traînée, de la copie la plus récente (**start**) à la plus ancienne (**end**). En général, réglez **brightness start** sur 100% et **brightness end** sur 0% pour que les échos s’estompent.
* **scale start / scale end** – applique l’échelle le long de la traînée, de la copie la plus récente (start) à la plus ancienne (end). Pour des traînées qui rétrécissent jusqu’à disparaître, réglez **scale start** sur 100% et **scale end** sur 0%.

## &#x20;Shimmer

Ajoute à votre contenu une variation de luminosité scintillante, allant d’un léger éclat à un stroboscope intense.

* **speed** – vitesse à laquelle le scintillement évolue dans le temps. Des valeurs élevées produisent un clignotement plus rapide ; 0 met l’effet en pause.
* **separation** – à quel point les points/éléments voisins diffèrent les uns des autres.
  * 0 : tout scintille ensemble.
  * \>0 : les points proches reçoivent des phases progressivement différentes, ce qui fait varier le scintillement sur la forme.
  * <0 : identique au cas précédent, mais la progression de phase se fait dans le sens opposé.
* **threshold** – au lieu de s’estomper progressivement, les points s’allument ou s’éteignent complètement selon leur luminosité. Les éléments plus lumineux s’allument plus souvent, mais notez que les éléments à 100% de luminosité restent toujours allumés, tandis que ceux à 0% restent toujours éteints. Utile pour des effets de paillettes nettes ou de lumière d’étoiles.

{% hint style="info" %}
Activer **threshold** fait partie de ces excellentes fonctions cachées qui peuvent vraiment donner vie à vos particules ou à votre contenu. Au lieu de s’estomper, les points sont rapidement activés et désactivés en fonction de leur luminosité. Comme moins de points sont dessinés à un instant donné, le résultat est une sortie plus lumineuse et une animation plus fluide.

Gardez toutefois à l’esprit que si votre contenu est déjà à 100% de luminosité, cela n’aura aucun effet !
{% endhint %}

* **use whole shape** – applique une seule valeur de scintillement uniformément à toute la forme. Lorsque cette option est désactivée, le nœud subdivise les formes pour que différentes parties puissent scintiller indépendamment, avec un aspect moucheté.

## &#x20;Particles

Il s’agit d’un effet expérimental qui génère et anime des particules à partir de votre contenu. Tout élément entrant basé sur des points est traité comme une position d’émetteur. Comme les trajectoires des particules sont précalculées, si votre contenu d’entrée change, vous devrez peut-être actualiser/recalculer pour mettre les particules à jour (il suffit de modifier n’importe quel réglage)

**General**

* **keep original** – si activé, le contenu original est conservé et les particules sont ajoutées par-dessus. Utile lorsque vous voulez que les points émetteurs restent visibles.
* **number of particles** – nombre de particules créées par émission. Des valeurs élevées produisent des effets plus denses ; des valeurs faibles donnent un rendu plus minimal.
* **emission period** – durée de la boucle (en mesures) sur laquelle les particules sont émises. À 100%, elles sont réparties uniformément sur la boucle ; des valeurs plus faibles les regroupent pour créer des rafales.
* **loop length** – durée de la boucle de particules, mesurée en mesures musicales.
* **loop count** – nombre de répétitions de la boucle avant réinitialisation. Avec la valeur 1, les particules suivent toujours exactement la même simulation à chaque fois, ce qui la rend parfaitement répétable. Des valeurs plus élevées introduisent davantage de variation avant la réinitialisation du cycle.
* **delay** – décale le début de l’émission d’un certain nombre de 1/64 de note, pour des effets de timing.

**Motion**

* **speed** – vitesse à laquelle les particules s’éloignent de l’émetteur.
* **speed variation** – ajoute de l’aléatoire afin que les particules ne se déplacent pas toutes à la même vitesse. Crée une dispersion plus naturelle.
* **direction** – définit la direction de base dans laquelle les particules sont projetées, au moyen des **angles x, y, z**. Ces angles font pivoter le vecteur de projection dans l’espace 3D : vous pouvez donc orienter les particules vers le haut, sur le côté ou dans n’importe quelle diagonale. Combinez avec **spread** pour obtenir des cônes plus larges ou des rafales plus chaotiques.

{% hint style="info" %}
**Angles d’Euler**\
Liberation utilise des **angles d’Euler** pour décrire l’orientation dans l’espace 3D. Il s’agit simplement de rotations autour des trois axes principaux :

* **X** – inclinaison vers l’avant/l’arrière (comme lorsque vous hochez la tête)
* **Y** – rotation vers la gauche/la droite (comme lorsque vous secouez la tête pour dire « non »)
* **Z** – roulis dans le sens horaire/antihoraire (comme lorsque vous penchez la tête sur le côté)

En ajustant ces trois valeurs, vous pouvez orienter les particules dans n’importe quelle direction.
{% endhint %}

* **direction variation** – ajoute une dispersion aléatoire autour de cette direction. Utile pour créer des cônes, des jets ou des explosions.
* **drag** – ralentit les particules au fil du temps. Des valeurs élevées leur donnent une sensation plus lourde et plus lente.
* **gravity** – attire les particules vers le bas (valeur positive) ou les pousse vers le haut (valeur négative).
* **gravity variation** – ajoute une variation de gravité par particule, ce qui rend le mouvement plus chaotique.

**Life**

* **life duration** – durée d’existence des particules (mesurée en unités de 1/64 de note). Avec des valeurs courtes, les particules disparaissent rapidement ; avec des valeurs plus longues, elles restent visibles plus longtemps.
* **life variation** – ajoute de l’aléatoire à la durée de vie des particules pour qu’elles ne disparaissent pas toutes en même temps.
* **start delay / start delay variation** – retarde le moment où chaque particule devient visible (par pas de 1/64 de note). La particule est déjà générée et en mouvement pendant cette période, mais sa luminosité reste à 0 : elle demeure donc invisible jusqu’à la fin du délai. C’est utile si vous voulez faire apparaître des « étincelles » de feu d’artifice en différé.

**Colour & brightness**

* **hue start** – couleur initiale des particules.
* **hue variation** – ajoute de l’aléatoire pour que les particules ne commencent pas toutes avec la même couleur.
* **hue change** – décale la teinte au cours de la durée de vie de la particule, créant des traînées qui changent de couleur.
* **brightness start / brightness end** – applique la luminosité sur la durée de vie de la particule. En général, réglez brightness start sur une valeur élevée et brightness end sur une valeur faible pour qu’elles s’estompent naturellement.
* **brightness variation** – randomise la luminosité de départ pour un rendu plus dynamique.
* **saturation start / saturation end** – définit l’intensité de la couleur au début et à la fin.
* **saturation variation** – randomise la saturation pour créer des variations entre les particules.

**Simulation**

* **time adjustment** – accélère ou ralentit toute la simulation de particules. Utile pour synchroniser avec différents tempos ou accentuer le mouvement.
