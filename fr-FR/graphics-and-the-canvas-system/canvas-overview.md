---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Vue d’ensemble du Canvas

Le système Canvas de Liberation est relativement simple, mais il peut sembler déroutant au début. Voici une vue d’ensemble conceptuelle pour vous aider à démarrer.

{% hint style="info" %}
**Attendez, ai-je besoin du système Canvas ?**

Peut-être pas ! Si vous projetez simplement un seul graphique sur un seul laser, vous pouvez facilement le faire avec une zone de faisceau (même si, par défaut, le contenu d’une zone de faisceau est inversé horizontalement : vous devrez donc appliquer un X flip au Clip).

Mais si vous voulez répartir du contenu graphique sur plusieurs lasers, ou le diviser en différentes sections pour l’adapter à une architecture, le système Canvas est fait pour ça !
{% endhint %}

### Canvas

Tout d’abord, il y a le Canvas lui-même. C’est ce que vous voyez dans la vue _CANVAS_ : il représente une grande surface, un « canvas », dans laquelle vous pouvez dessiner du contenu à n’importe quel endroit.

### Zones cibles du Canvas

Elles apparaissent sous forme de rectangles à contour bleu dans la vue Canvas. Ce sont des zones auxquelles vous pouvez envoyer du contenu. Vous envoyez le contenu d’un Clip vers une zone cible du Canvas de la même manière que vous enverriez un Clip vers une zone de faisceau. Les boutons des zones cibles du Canvas se trouvent à droite des boutons des zones de faisceau dans le Clip Deck.

{% hint style="info" %}
Si vous ne voyez pas les boutons du Canvas dans le Clip Deck, essayez de faire défiler les boutons des zones de faisceau avec `Shift + Left / Right Arrow`. Vous devriez voir un bouton pour chaque zone cible du Canvas, libellé _CANVAS 1, CANVAS 2_, etc.
{% endhint %}

### Zones du Canvas

Les zones du Canvas sont des zones à l’intérieur du Canvas que vous choisissez d’envoyer vers un laser. Elles sont représentées par des rectangles à contour rose dans la vue Canvas. Vous pouvez faire un clic droit sur chaque zone et sélectionner les lasers auxquels vous voulez l’assigner. Si vous passez ensuite à la vue _OUTPUT_ pour ce laser, vous verrez qu’une nouvelle zone est apparue.

{% hint style="danger" %}
ATTENTION : si le laser est armé, vous pourriez commencer soudainement à projeter du contenu dans une zone Canvas par défaut. Il est préférable de désarmer le laser avant de lui assigner des zones du Canvas.
{% endhint %}

{% hint style="info" %}
Vous pouvez aussi assigner une zone du Canvas à un laser en cliquant sur le bouton _add canvas zone_ dans la vue _OUTPUT_. Voir [Zones](../output-view/zones.md "mention").
{% endhint %}

### Images guides

Vous pouvez ajouter une image guide dans le Canvas et l’utiliser comme modèle pour vos graphiques. Il est conseillé d’ajuster la teinte de couleur de l’image guide (menu clic droit) et de l’assombrir afin de voir plus facilement votre contenu par-dessus.

{% hint style="info" %}
Pour le mapping architectural, j’ai trouvé utile de produire un visuel « déplié » du bâtiment, représentant toutes ses surfaces sous forme d’image plate non déformée. La correction de perspective des différentes sections peut ensuite être effectuée avec la zone du Canvas dans la vue _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Une image guide « aplatie » de Saltwell Hall à Gateshead, au Royaume-Uni</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Les zones du Canvas dans une version embryonnaire de Liberation (vers 2017 !) Notez que les rectangles roses choisissent quelle partie du Canvas afficher, puis les vues Output ci-dessous montrent vers quelle partie de chaque laser ces zones sont envoyées.</p></figcaption></figure>

### Canvas dans le 3D visualiser

Recréer votre système de projection complexe à plusieurs lasers dans le 3D visualiser serait probablement assez fastidieux (c’est le moins qu’on puisse dire) ! À la place, vous pouvez placer votre Canvas dans l’espace 3D. Activez la case _Show canvas_ dans le panneau _3D visualiser settings_. (Toutes les images guides présentes dans le Canvas apparaîtront également dans le visualiser.)

{% hint style="info" %}
Notez que le visualiser affichera toujours les projections du Canvas comme des effets atmosphériques provenant des lasers. Vous pouvez simplement les déplacer hors du champ, ou, si vous voulez peaufiner le résultat, les aligner avec le Canvas !
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Il peut être extrêmement satisfaisant d’aligner les faisceaux du laser avec l’image du Canvas dans le 3D visualiser !</p></figcaption></figure>
