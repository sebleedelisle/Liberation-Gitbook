# ✅ Guide de démarrage rapide

## Introduction

Bienvenue dans **Liberation** - la nouvelle génération de logiciel pour spectacles laser.

Liberation est un logiciel moderne puissant et complexe ; il repose sur des principes d’ergonomie et de fiabilité pour vous donner la liberté d’exprimer votre créativité. Il est rapide, efficace et fluide ; suivez ce _guide de démarrage rapide_ pour être opérationnel en un rien de temps !

### Gestion des lasers

Liberation est suffisamment flexible pour vous permettre de configurer des lasers et de les visualiser sans qu’aucun laser réel ne soit connecté. Puis, lorsque vous êtes prêt, vous pouvez assigner facilement chaque sortie à un contrôleur laser.

{% hint style="info" %}
Vous pouvez configurer et visualiser autant de lasers que vous le souhaitez dans Liberation ; les niveaux de licence (Hobbyist, Pro, etc.) limitent uniquement le nombre de lasers que vous pouvez _armer_. Cela signifie que vous pouvez concevoir des spectacles laser avec 100 lasers, même avec une licence gratuite. Vous n’avez besoin de passer à une licence supérieure qu’au moment de les utiliser réellement avec de vrais lasers.
{% endhint %}

Par défaut, 8 lasers sont répartis horizontalement, mais vous pouvez personnaliser cette configuration comme vous le souhaitez. Il est sans doute préférable de conserver ce réglage par défaut pendant que vous découvrez le logiciel, puis de l’ajuster plus tard pour qu’il corresponde à votre configuration matérielle. (Voir [Configurer votre projet](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Important : avant d’armer des lasers, assurez-vous de bien comprendre les risques impliqués et parcourez attentivement le chapitre [Présentation du processus de configuration des lasers](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Présentation du logiciel

### Coupure de sécurité

Lorsque vous utilisez des lasers, vous devez toujours avoir un **bouton d’arrêt d’urgence matériel** à portée de main (voir [Arrêt d’urgence / interverrouillages](../hardware/emergency-stop-interlocks.md "mention")). Toutefois, si vous souhaitez tout désarmer de manière moins urgente, vous pouvez utiliser le bouton _**DISARM ALL**_, ou la touche `Escape` (ou la touche _**SESSION**_ sur l’APC40). Vous pouvez aussi réduire la luminosité globale avec le curseur à l’écran ou le fader principal de l’APC40.

### Éléments de type curseur

Dans Liberation, vous trouverez différents curseurs et contrôles.

{% hint style="info" %}
Cliquez sur un curseur avec `Cmd / Ctrl` enfoncé pour saisir une nouvelle valeur si vous avez besoin d’un contrôle plus précis que celui offert par le curseur.
{% endhint %}

### Raccourcis clavier

La liste complète des raccourcis clavier est disponible ici : [Raccourcis clavier](../reference/keyboard-shortcuts.md "mention")

### Disposition de l’écran

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Vous ne savez pas à quoi sert un bouton ? Survolez-le avec la souris pour afficher une description !
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Le menu contient toutes les options d’import/export de fichiers, ainsi que l’accès aux panneaux. Vous y trouverez également l’option permettant d’autoriser l’ordinateur avec votre abonnement (dans _Liberation -> Authorise/Deauthorise this computer_).

#### Barre d’icônes

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Les tâches courantes se trouvent ici, comme armer/désarmer tous les lasers, régler la luminosité globale, activer le motif de test et basculer entre les vues 3D, Canvas et Output.

### Vues

La grande zone située en haut à gauche de l’écran peut afficher l’une des 3 vues principales : **3D**, **CANVAS** et **OUTPUT.** Basculez entre elles à l’aide des boutons de la barre d’icônes (ou utilisez la touche `Tab` pour basculer entre les vues 3D et OUTPUT, puis continuer à parcourir chaque sortie laser l’une après l’autre).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Vue 3D

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

La vue 3D vous montre à quoi ressembleront vos lasers et peut être configurée pour correspondre à votre propre installation laser. Cliquez et faites glisser pour faire pivoter la caméra ; utilisez la molette de la souris pour avancer et reculer. De nombreuses autres options sont disponibles dans le panneau _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Voir [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Vue Output

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

La vue Output sert à configurer les zones et les masques de chaque laser. (Remarquez le très grand numéro dans le coin supérieur gauche, qui permet de voir facilement sur quel laser vous travaillez !)

Cette vue représente l’ensemble de la sortie de ce laser, ainsi que l’emplacement de chaque zone à l’intérieur de celle-ci. Par défaut, il n’y a qu’une seule zone par laser, mais vous pouvez ajouter autant de zones que raisonnablement nécessaire, et elles apparaîtront toutes dans cette vue.

{% hint style="info" %}
**Qu’est-ce qu’une zone ?**

Une zone est un espace dans la sortie d’un laser vers lequel vous pouvez envoyer du contenu laser. Vous pouvez avoir plusieurs zones par laser. Le type de zone le plus simple est une zone _beam_, mais il existe aussi des zones _canvas_ et des zones _DMX_. Dans ce guide, nous nous concentrerons surtout sur les zones beam, généralement utilisées pour créer des effets de faisceaux atmosphériques dans l’air.
{% endhint %}

Vous pouvez sélectionner le laser à modifier avec :

* les boutons numérotés dans la barre en haut
* la touche numérique correspondant au laser souhaité _(touches 1-9_)\_
* la touche `Tab` pour passer de l’un au suivant

Ajoutez un nouveau laser à la configuration en appuyant sur le bouton _+_. (Un bouton _ADD LASER_ est également disponible dans le panneau _Laser Overview_)

Supprimez un laser de la configuration en appuyant sur le bouton rouge ⊖ dans le panneau _Laser Overview_.

Vous pouvez zoomer et dézoomer avec la molette de la souris, puis cliquer et faire glisser à n’importe quel endroit où il n’y a pas de zone pour déplacer la vue.

Cliquez sur une zone pour la sélectionner, puis ajustez ses points d’angle avec la souris. Maintenez la touche `Alt / Option` pendant que vous faites glisser un angle pour rendre la transformation non uniforme. Faites un clic droit sur la zone pour afficher davantage d’options, notamment le changement de type de zone.

Sur la gauche se trouve une barre contenant une série de boutons d’icônes ; survolez n’importe quel bouton pour afficher une description de sa fonction. Ces boutons permettent d’ajouter des zones beam, des zones canvas et des masques. Des options permettent également de définir un motif de test pour ce laser uniquement, ainsi que des réglages de grille et d’alignement.

Pour plus de détails, voir [Vue Output](../output-view/ "mention").

#### Canvas

Le système Canvas est principalement utilisé pour les graphiques et le mapping architectural. Vous pouvez répartir des images complexes sur plusieurs lasers et corriger la perspective de chaque section. Voir [Graphiques et système Canvas](../graphics-and-the-canvas-system/ "mention").

### Contrôleur MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Même s’il est possible de contrôler Liberation avec la souris et le clavier, il est nettement préférable d’utiliser une interface de contrôle MIDI APC40 (la Mark 2 est idéale, mais la Mark 1 fonctionne aussi).

Voir aussi : [Référence APC40](../reference/apc40-reference.md "mention")

Nous avons désormais également ajouté la prise en charge de l’APC Mini Mark 2 et du MIDI Fighter Twister, et d’autres contrôleurs sont en développement. Mais l’APC40 Mark 2 reste la meilleure option dans la plupart des cas.&#x20;

### Clips et effets

{% hint style="info" %}
**Qu’est-ce qu’un clip ?**

Un clip est un conteneur pour tout contenu laser dans Liberation. Les clips peuvent contenir des faisceaux ou des animations graphiques, et fonctionnent généralement en boucle. Ils peuvent être envoyés vers n’importe quelle zone (ou _Canvas target area_) et sont déclenchés avec les boutons de clip dans le Clip Deck.
{% endhint %}

#### Présentation du Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Cette grille est appelée _clip deck_ et c’est là que tous les clips laser sont stockés. Elle est conçue pour correspondre directement à la grille de boutons 8 x 5 de votre APC40.

**Navigation dans le clip deck.**

Vous pouvez faire défiler le clip deck vers la gauche et la droite avec :

* les touches fléchées gauche et droite. Ajoutez `Cmd / Ctrl` pour faire défiler une page entière à la fois.
* Trackpad : balayage
* Souris : si votre souris dispose d’un défilement horizontal, vous pouvez l’utiliser lorsque le pointeur survole le clip deck
* Molette de défilement APC40
* Boutons APC40 _<- DEVICE ->_

Pour vous aider à vous repérer, un mini visualiseur du clip deck est affiché en haut. Voir aussi [Clips et Clip Deck](../clips/ "mention")

#### Démarrage et arrêt des clips

Appuyez sur un bouton de clip (avec la souris ou avec l’APC40) pour démarrer un clip. Appuyez de nouveau pour l’arrêter. Lorsque vous démarrez un clip, tous les autres clips de la même couleur s’arrêtent automatiquement, sauf si vous maintenez _shift_.

Certains clips sont en _Flash mode_ (par défaut, les clips rouges). Dans ce cas, ils s’arrêtent dès que vous relâchez le bouton de clip.

Le bouton _STOP_ arrête tous les clips en cours de lecture.

#### Définir les zones de sortie du clip

Sous les boutons de clip, vous verrez les boutons de zone : les zones beam 1 à 8 par défaut (_BEAM 1_, _BEAM 2_, etc.). Les boutons de zone s’allument pour indiquer quelles zones sont assignées au clip actuellement sélectionné.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Deux rangées sous les boutons de zone, vous trouverez les boutons d’inversion X/Y ; activez-les pour inverser le clip horizontalement et verticalement.

{% hint style="info" %}
Notez que ces affectations de zones et ces réglages d’inversion X/Y sont liés au clip lui-même ; ils seront conservés la prochaine fois que vous lancerez ce clip. Ce ne sont pas des réglages globaux.
{% endhint %}

Faites un clic droit sur un clip pour modifier davantage de réglages du clip. Voir aussi [Paramètres de Clip](../clips/clip-settings.md "mention")

### Groupes

Vous remarquerez que chaque clip possède un contour coloré ; cette couleur indique le _groupe_ auquel il appartient. Les boutons de clip de l’APC40 s’allument également dans cette couleur.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyan</td></tr><tr><td>Group 2</td><td>Orange</td></tr><tr><td>Group 3</td><td>Rouge</td></tr><tr><td>Group 4</td><td>Indigo</td></tr><tr><td>Group 5</td><td>Vert</td></tr></tbody></table>

Le système de groupes est très flexible et vous permet de :

* Laisser les clips d’un groupe actifs pendant que vous activez/désactivez des groupes dans un autre
* Assigner rapidement des zones et des inversions X/Y à tous les clips d’un groupe
* Définir le _Flash mode_ pour un clip (Group 3 est réglé sur _Flash mode_ par défaut)

Les groupes disposent également de réglages de transition d’entrée/sortie qui peuvent être hérités par leurs clips, ou remplacés.

Vous pouvez assigner le groupe du clip avec les boutons du menu contextuel, ou avec l’APC40 : appuyez sur le bouton de groupe puis, _tout en le maintenant enfoncé_, appuyez sur les boutons de clip.

Modifier les réglages de zone pour tous les clips d’un groupe

Avec l’APC40, appuyez sur le bouton de groupe, puis _tout en le maintenant enfoncé_, utilisez les boutons de zone et X/Y pour basculer les réglages de zone de tous les clips de ce groupe.

Voir aussi [Groupes de Clips](../clips/groups.md "mention")

### Effets

Le système d’effets de Liberation est un moyen puissant et polyvalent de modifier la sortie des clips en temps réel. Les boutons d’effets par défaut 1 à 8 se trouvent sous les boutons de zone.

#### Appliquer un effet

Appuyez sur un bouton d’effet pour activer ou désactiver l’effet, ou mieux encore, utilisez les curseurs APC40 1 à 8 pour faire apparaître et disparaître progressivement les effets.

#### Paramètres d’effet

Utilisez les contrôleurs rotatifs 1-8\* pour ajuster le _paramètre_ de chaque effet. (Vous pouvez aussi faire un clic droit avec la souris pour ajuster le niveau et le paramètre.) La modification du paramètre produit des résultats différents selon la configuration de l’effet. Voir la liste ci-dessous pour les effets par défaut.

{% hint style="info" %}
Les petits nombres affichés sur les boutons d’effet correspondent au _level_ et au _parameter_ de l’effet. Le _level_ est contrôlé par le fader de l’APC40, ou vous pouvez cliquer-glisser sur le bouton. Le paramètre est ajusté avec les rotatifs de l’APC40, ou vous pouvez faire un clic droit pour l’ajuster avec la souris.
{% endhint %}

_\*Les contrôleurs rotatifs 1-8 se trouvent en haut de l’APC40 Mk2 et en haut à droite sur la Mk1. Voir aussi :_ [Référence APC40](../reference/apc40-reference.md "mention")

#### Les effets par défaut

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applique un mouvement chaotique à la sortie du clip. Le paramètre ajuste la quantité/la vitesse du chaos.
2. **Sine wave** :\
   Déforme tout le contenu selon une onde sinusoïdale en mouvement. Le paramètre ajuste la longueur d’onde.
3. **Rotation** :\
   Fait tourner l’ensemble. Le paramètre ajuste la vitesse de rotation.
4. **Horizontal flip** :\
   Compresse et étire l’ensemble horizontalement. Le paramètre ajuste la vitesse.
5. **Scale** :\
   Met l’ensemble à l’échelle de façon répétée, de la taille complète à zéro. Le paramètre ajuste la vitesse.
6. **Hue** :\
   Modifie la teinte de l’ensemble, sans modifier la saturation (c’est-à-dire que tout ce qui est blanc reste blanc). Le paramètre ajuste la teinte.
7. **Saturation and hue** :\
   Modifie la teinte de l’ensemble et sature aussi complètement la couleur (c’est-à-dire que tout ce qui est blanc prend la couleur). Le paramètre ajuste la teinte.
8. **Flash** :\
   Fait clignoter de façon répétée la luminosité de l’ensemble, de la luminosité complète à zéro. Le paramètre ajuste la vitesse de clignotement.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

16 effets de couleur supplémentaires se trouvent sur la rangée inférieure pour appliquer des valeurs prédéfinies de teinte et de saturation.

Notez qu’il s’agit des effets par défaut, mais ils peuvent être modifiés pour faire presque tout ce que vous voulez !

#### Qu’est-ce que le _« clip actuellement sélectionné »_ ?

Lorsque vous lancez un clip, il s’allume pour indiquer qu’il est actif. Il possède également un contour blanc indiquant qu’il s’agit du clip actuellement _sélectionné_. Chaque fois que vous activez/désactivez des boutons de zone ou ajustez les réglages du clip, ces actions s’appliquent au _clip actuellement sélectionné_.

{% hint style="info" %}
Pour sélectionner un clip sans le déclencher, appuyez sur la touche `Alt / Option` avant d’appuyer sur le bouton de clip. C’est un bon moyen d’ajuster ses zones et d’autres réglages sans le lancer.
{% endhint %}

### Panneau Clip Settings

Utilisez le panneau _Clip Settings_ pour modifier l’échelle, la position X/Y et accéder au puissant système de délai par zone.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panneau Global Settings

Utilisez le panneau _Global Settings_ pour ajuster les réglages globaux de sortie qui affectent toutes les sorties sur toutes les zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Activez AUTO RESET pour réinitialiser automatiquement tous les _Global settings_ lorsqu’aucun clip n’est en lecture.&#x20;

### Timing

Presque tous les spectacles laser utilisent une bande-son musicale ; le système de timing de Liberation repose donc sur un tempo en battements par minute. Dans le _Tempo Panel_, vous pouvez voir une représentation du temps ; chaque carré représente un temps et clignote en rythme.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Plusieurs options de synchronisation sont disponibles, notamment MIDI clock et Ableton Link. Si vous connaissez le tempo de la musique, vous pouvez l’ajuster manuellement avec le curseur à l’écran ou le bouton Tempo de l’APC40, mais vous pouvez aussi rester synchronisé avec la musique grâce au système _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ est un terme couramment utilisé dans les applications musicales ; il vous permet de taper en rythme avec le beat pour définir le tempo pendant que la musique joue. Vous pouvez utiliser le bouton à l’écran, même s’il est recommandé d’utiliser la touche _T_ ou le bouton _Tap Tempo_ de l’APC40 (ou même une pédale si vous préférez).

Appuyez sur la touche _R_ ou sur le bouton _Metronome_ (APC40) pour réinitialiser le tempo au début de la mesure.

Appuyez sur la touche _Y_ ou tournez le bouton _Tempo_ (APC40) pour arrondir le tempo à un nombre entier. Cela peut être utile pour la musique électronique, qui utilise souvent un nombre entier de battements par minute.

### Organiser votre clip deck

Pour déplacer un clip dans votre clip deck, cliquez dessus et faites-le glisser vers une nouvelle position. Pendant le glisser-déposer, vous pouvez utiliser les touches fléchées (ou la molette/les boutons de défilement de votre APC40) pour faire défiler vers la gauche et la droite.

Appuyez sur la touche `Alt / Option` pendant que vous faites glisser pour créer une copie.

Cliquez sur un clip avec `Alt / Option` enfoncé pour le sélectionner sans le lancer.

Cliquez sur un clip avec `Alt / Option + Shift` enfoncé pour effectuer une sélection multiple, ou cliquez et faites glisser en dehors d’un clip pour sélectionner au « lasso ».&#x20;

Un clic-glisser déplacera TOUS les clips sélectionnés.

Pour supprimer un ou plusieurs clips, faites-les glisser hors du clip deck (une icône de corbeille apparaîtra) ou utilisez le bouton DELETE dans le menu contextuel du clip.

### Panneau Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Le panneau _Laser overview panel_ vous donne un aperçu rapide de l’état de vos lasers actuellement en fonctionnement. Le carré vert à droite indique que le contrôleur laser fonctionne correctement. S’il devient orange, vous avez des pertes occasionnelles ; s’il devient rouge, il est déconnecté. S’il est gris, il n’est connecté à aucun contrôleur.&#x20;

Le graphique au centre affiche l’historique des durées de trame, et le nombre à droite indique la fréquence de trame actuelle. Plus le contenu est complexe, plus la fréquence de trame sera faible (donc plus l’affichage scintillera). En dessous d’environ 25 fps, l’affichage commencera à paraître un peu scintillant.&#x20;

### Connexion aux lasers - panneau Controller Assignment

Cliquez sur le bouton _Assign Laser Controllers_ pour ouvrir le panneau _Controller Assignment_. (Ce panneau est également accessible via _View -> Controller Assignment_ dans la barre de menu.)

Vous pouvez choisir ici quelles sorties laser sont envoyées vers quels contrôleurs laser. Faites glisser les contrôleurs depuis la liste de droite vers les emplacements à gauche. Vous pouvez renommer vos contrôleurs pour les faire correspondre au laser auquel ils sont associés (utilisez le bouton avec l’icône de stylo).

Lisez le chapitre [Attribution des contrôleurs](../setting-up/controller-assignment.md "mention") pour plus de détails.

{% hint style="danger" %}
Avant d’armer des lasers, assurez-vous de parcourir le chapitre [Présentation du processus de configuration des lasers](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panneau Laser Output

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ce panneau affiche les réglages du _laser actuellement sélectionné_ (représenté par le numéro en haut). Changez de laser actuellement sélectionné avec la touche _tab_, en appuyant sur une touche numérique, en cliquant sur un numéro de laser dans le panneau _Laser Overview_ ou dans la _vue Output_.

* **Number button** arme et désarme le laser ; s’il est rouge, le laser est armé.
* **Brightness** ajuste la luminosité du laser indépendamment des autres lasers (et se combine avec le réglage _global brightness_ ; par exemple, si les deux sont à 50 %, votre laser sera à 25 %).
* **Test Pattern** active un motif de test pour ce laser uniquement (remplace le réglage global de motif de test)
* **Orientation** corrige les lasers installés sur le côté ou à l’envers.
* **Flip Horizontal and Flip Vertical** inverse la sortie du laser. Utile pour corriger la sortie de lasers câblés de manière incohérente.
* **Copy Laser Settings** ouvre un panneau permettant de copier différents réglages de ce laser vers d’autres.

### Réglages des scanners

Les lasers de projection fonctionnent en déplaçant un seul faisceau laser extrêmement rapidement et en l’allumant ou l’éteignant pour dessiner des formes dans l’air. Ce que vous voyez comme des lignes, des formes et des images correspond en réalité au faisceau qui trace des trajectoires plus vite que vos yeux ne peuvent les suivre.

Un flux de points est la donnée qui indique au laser où se déplacer ensuite et à quel moment le faisceau doit être allumé ou éteint. Dans Liberation, les clips sont convertis en ce flux de points en temps réel lorsqu’ils sont envoyés aux lasers.

Liberation vous donne un contrôle détaillé sur la manière dont ce flux de points est généré, afin d’équilibrer fluidité, luminosité et performances pour chaque laser.

{% hint style="info" %}
Si vous êtes habitué à d’anciens logiciels laser reposant sur des flux de points précalculés, cette approche peut sembler différente au départ. Cependant, la génération de points en temps réel permet d’optimiser différemment le même contenu pour chaque laser. Il devient ainsi plus facile de travailler avec plusieurs lasers ayant des vitesses ou des qualités de scanners différentes, sans dupliquer ni reconstruire le contenu. Cela permet aussi de garder des fichiers de clips très légers, ce qui explique pourquoi l’intégralité du clip deck par défaut de Liberation ne représente que quelques mégaoctets, et non des gigaoctets.
{% endhint %}

Les réglages de base des scanners sont :

* **Speed** correspond à la vitesse des scanners, c’est-à-dire la rapidité avec laquelle le laser se déplace pour dessiner les formes. Cela équivaut à ajuster le débit de points dans un logiciel laser traditionnel, mais dans Liberation, vous pouvez modifier la vitesse de déplacement du laser _indépendamment du débit de points_. Vous ne devriez pas avoir besoin d’ajuster ce réglage.
* **Scanner sync** (parfois appelé _blank shift, précédemment Colour Shift_) Les scanners déplacent le laser très rapidement, mais le changement de luminosité et de couleur est souvent désynchronisé par rapport au mouvement. Cela se manifeste par de petites « traînées » lumineuses scintillantes au bord des faisceaux et des lignes. Utilisez ce réglage pour synchroniser le mouvement et la couleur. Voir [Panneau des paramètres de sortie laser](../setting-up/laser-settings/ "mention")

Les autres réglages avancés des scanners sont décrits dans le chapitre [Avancé](../advanced/ "mention").

### Zoning

Pour un guide complet sur la configuration et le zoning des lasers, voir : [Présentation du processus de configuration des lasers](../setting-up/setting-up-lasers.md "mention")
