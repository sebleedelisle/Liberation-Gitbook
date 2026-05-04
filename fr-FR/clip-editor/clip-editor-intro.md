---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introduction au Clip Editor

Le Clip Editor est un outil polyvalent pour créer du contenu laser, et il est au cœur de Liberation. Il permet de réaliser facilement des éléments simples, tout en offrant assez de souplesse pour créer des effets très sophistiqués et complexes.

{% hint style="info" %}
L’éditeur basé sur des nœuds a été la toute première partie de Liberation à être créée ! Il est né d’une conversation avec Rob Stanley lors d’une rencontre laser au Royaume-Uni en 2018, autour de ce à quoi pourrait ressembler un concepteur de contenu laser « orienté objet ».

Même s’il paraît simple, c’est un système assez complexe à développer. Mais début 2019, j’avais une démo fonctionnelle qui validait le concept — et c’est ce qui a lancé toute cette aventure !
{% endhint %}

Il s’agit d’un éditeur visuel basé sur des nœuds, ou [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph), qui vous sera familier si vous avez déjà utilisé des produits comme TouchDesigner, MaxMSP ou VVVV. Le Clip Editor est toutefois un peu différent et plus simple, car il a été conçu spécifiquement pour les graphismes vectoriels.

Vous pouvez ouvrir le Clip Editor en faisant un clic droit sur le bouton du Clip, puis en sélectionnant _EDIT CLIP_. Vous pouvez aussi faire un clic droit sur un bouton de Clip vide et sélectionner _CREATE AND EDIT CLIP_.

### Vue d’ensemble

Voici ce que vous verrez dans le Clip Editor :

* Les boutons de nœuds **Creator** et **Operator** en haut
* Les boutons de nœuds **Oscillator** sur la gauche
* Un aperçu du contenu dans un panneau à droite ; si vous cliquez sur un nœud, un second aperçu s’affiche pour montrer le contenu au niveau de ce nœud.
* Tous les nœuds et connexions du clip que vous modifiez (si c’est un nouveau clip, cette zone sera vide)
* Le panneau Clip Editor avec différentes options

Pendant l’édition, vous verrez également l’apparence du clip dans le 3D Visualiser en arrière-plan.

{% hint style="info" %}
Si vous ne voyez aucune sortie dans le 3D Visualiser, vous devrez peut-être utiliser les boutons de zone pour activer les zones souhaitées. Vous devez aussi vérifier que _Preview to lasers_ est activé ; voir [Introduction au Clip Editor](clip-editor-intro.md#clip-editor-panel "mention") ci-dessous.
{% endhint %}

### Construire un clip

Vous commencez généralement avec un ou plusieurs [nœuds Creator](creator-nodes.md), puis vous connectez des [Nœuds Operator](operator-nodes/) de gauche à droite pour traiter le contenu. Lorsque vous rapprochez des Creators et/ou des Operators, vous remarquerez qu’ils se connectent automatiquement entre eux. Vous pouvez ensuite les éloigner pour les déconnecter.

### Ajouter des nœuds à votre clip

Cliquez et faites glisser l’un des boutons de nœud situés en haut ou à gauche vers un espace vide dans le Clip Editor.

### Ajuster les réglages d’un nœud

Cliquez sur le bouton avec l’icône d’engrenage, en haut à droite du nœud, pour ouvrir le panneau de propriétés de ce nœud.

### Activer et désactiver un nœud

Cliquez sur le bouton avec l’icône d’alimentation, en haut à gauche du nœud, pour activer ou désactiver le nœud. Le nœud s’assombrit pour indiquer qu’il n’est pas actif actuellement. Notez que le contenu continue de traverser un Operator même s’il est désactivé, mais le nœud n’affecte pas le contenu.

### Connecter des nœuds entre eux

Le contenu est créé avec un nœud Creator, puis transmis de nœud en nœud de gauche à droite ; chaque Operator modifie le contenu d’une manière ou d’une autre, puis le transmet à l’Operator suivant. Ce qui reste à la fin du chemin constitue le contenu du clip. Les Creators et Operators se connectent automatiquement entre eux lorsque vous les rapprochez. Pour les séparer, éloignez-les à nouveau.

{% hint style="info" %}
Vous pouvez connecter plusieurs nœuds à l’entrée du nœud suivant. C’est utile pour combiner plusieurs éléments de contenu.
{% endhint %}

### Propriétés et sockets des nœuds

Chaque nœud possède une rangée de sockets en bas, et chacun représente une propriété du nœud, comme la luminosité, la position, l’échelle, la rotation, etc.

Les [nœuds Oscillator](oscillators/) peuvent être connectés à ces sockets par le bas et utilisés pour animer ces réglages. Les nœuds Oscillator ont une sortie en haut : cliquez et faites glisser pour tirer la connexion, puis déposez-la sur l’un des sockets de propriété des autres nœuds.

### Nœuds Oscillator

Les nœuds Oscillator servent à modifier des propriétés au fil du temps. Ils représentent généralement des formes d’onde, comme une dent de scie ou une sinusoïde, mais certains nœuds Oscillator utilisent des entrées externes, comme le niveau d’entrée du microphone, comme source.

{% hint style="info" %}
Si vous avez déjà utilisé un synthétiseur analogique, le concept d’oscillateurs vous sera familier : ils sont couramment utilisés pour créer des formes d’onde ou modifier le son au fil du temps. Les oscillateurs dans Liberation jouent un rôle similaire.

**Fun fact :** le nom _Liberation_ est inspiré du Moog Liberation, un synthétiseur « keytar » sorti en 1980 et rendu célèbre par Herbie Hancock, Jean-Michel Jarre et même James Brown !
{% endhint %}

Les oscillateurs ont toujours des réglages de _range_, qui contrôlent la valeur minimale et maximale de la propriété à modifier. Les _Wave Oscillators_ ont toujours un réglage de _duration_, qui détermine la vitesse à laquelle l’oscillateur modifie la valeur. Voir [Oscillateurs d’onde](oscillators/wave-oscillators.md "mention") pour plus d’informations.

### Panneau Clip Editor

* Timer - en haut du panneau, vous voyez le temps actuel du clip pendant sa progression
* _RETRIGGER_ - redémarre le clip depuis le début ; particulièrement utile si votre clip ne boucle pas
* _Preview to lasers_ - lorsque cette option est cochée, le 3D Visualiser se met à jour pendant que vous modifiez ce clip. Si vous la désactivez, vous verrez les clips en cours de lecture en dehors de l’éditeur. Il s’agit d’un réglage global, pas d’un réglage propre à chaque clip.
* _UNDO/REDO_ - pour le Clip Editor lui-même. Également associé à `Cmd / Ctrl + Z` et `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - enregistre vos modifications, mais vous avertit en cas d’écrasement
* _SAVE AS A COPY_ - enregistre votre clip dans le prochain emplacement disponible du Clip Deck. Cet emplacement devient la nouvelle position de votre clip, et tous les enregistrements suivants se feront à cet endroit.
* _EXIT EDITOR_ - ferme le Clip Editor. Si vous avez des modifications non enregistrées, un panneau de confirmation s’affiche.
