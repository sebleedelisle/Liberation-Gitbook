---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Spécifications des scanners et Liberation

### La réalité parfois confuse des spécifications de scanners

Les cadences de points et les spécifications des scanners peuvent prêter à confusion. Vous verrez souvent des indications comme 30 kpps @ 8º ou 50 kpps @ 4º, mais ce que ces chiffres représentent réellement n’est pas toujours évident.

{% hint style="info" %}
Avertissement : je ne suis pas spécialiste du matériel de scanner, mais j’ai des années d’expérience pratique pour obtenir un bon rendu avec des scanners de qualités très différentes, grâce au logiciel et à la génération du flux de points plutôt qu’au réglage matériel. Ce qui suit se base sur cette expérience.
{% endhint %}

#### **D’où viennent ces chiffres**

Les termes comme « 30K » et « 50K » sont des raccourcis basés sur la manière dont les scanners sont évalués avec le motif de test ILDA à ces cadences de points, dans des conditions spécifiques.

Quand un scanner est annoncé avec une valeur du type : _30Kpps @ 8°_, cela signifie en réalité :

> « Ce scanner peut reproduire le motif de test ILDA à 30 000 points/seconde avec un angle de balayage de 8°, lorsqu’il est correctement réglé. »

Ce n’est pas une mesure complète ni entièrement standardisée des performances en conditions réelles. En fait, ce test n’a pas été conçu à l’origine comme un benchmark : il servait à une **procédure de réglage**. Vous lancez un motif connu à une cadence de points fixe (par exemple 30 000 points/seconde), puis vous ajustez l’amortissement et le gain jusqu’à obtenir un affichage correct.

Mais cela reste la référence la plus utilisée, et elle peut donner une bonne idée de la qualité des scanners, au moins chez les fabricants sérieux. Avec les fabricants _moins sérieux_, en revanche...

#### Si vous voulez tester les scanners selon leur valeur annoncée

{% hint style="danger" %}
**Il s’agit d’une technique avancée et vous pouvez endommager vos scanners si vous ne faites pas attention. Déconseillé sauf si vous savez ce que vous faites.**
{% endhint %}

Vous devrez trouver un logiciel capable de sortir le [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) — je pense que LaserShowGen peut peut-être le faire — puis ajuster la taille de sortie pour correspondre à l’angle de balayage spécifié (par exemple 8°). Consultez la documentation ILDA pour savoir comment analyser la sortie.

#### Pourquoi ce n’est pas forcément un bon benchmark

Tout d’abord, votre motif de test peut s’afficher incorrectement même si vos scanners sont bons, simplement parce qu’ils ne sont pas réglés de manière optimisée pour ce test.

Cela peut servir de guide général utile pour distinguer de « bons » et de « mauvais » scanners, mais les fabricants peuvent parfois prendre beaucoup de libertés avec ces spécifications.

#### Alors, comment choisir un bon scanner ?

Je pense qu’il faut surtout s’assurer qu’ils sont fabriqués par un fabricant reconnu. Les fabricants de scanners haut de gamme coûteux comme Cambridge Technology (CT), Eye Magic (EMS) et ScannerMAX (une filiale de Pangolin) sont toujours de bons choix, sans mauvaise surprise. Mais quand une paire de scanners coûte environ 1 000 $, pour beaucoup d’entre nous au début, c’est plus cher que nos lasers !

J’ai donc surtout utilisé des fabricants chinois. Les scanners Dragon Tiger (DT) sont corrects et abordables, et je crois que LightSpace les utilise. De nombreux autres fabricants (dont OPT et Able sur certains modèles) utilisent également des systèmes basés sur DT.

Phenix Technology (PT) se situe généralement dans une gamme inférieure, mais honnêtement, ils conviendront probablement pour la plupart des usages.

**Si vos scanners ne portent aucune marque, c’est probablement là qu’il faut commencer à se soucier de la qualité !**

#### Comment Liberation vous aide

Tout d’abord, pour la plupart des usages, vous n’avez pas besoin de scanners vraiment coûteux ! Des DT 30 kpps abordables, voire des PT, feront très bien l’affaire. Les réglages de scanner par défaut sont volontairement prudents et, dans la plupart des cas, _vous ne devriez pas avoir besoin de les modifier_ (à part _Scanner sync_).

Même si vous avez de meilleurs scanners, il est inutile de les pousser plus fort que nécessaire. Cela prolongera considérablement leur durée de vie.

#### Qu’est-ce qu’un « flux de points » ?

Vous avez probablement déjà entendu ce terme : c’est la manière dont nous contrôlons le trajet des scanners.

Un flux de points est une liste de positions X/Y, chacune avec une couleur. Pour dessiner quelque chose comme une ligne blanche, vous envoyez une séquence de points le long de cette ligne, tous définis en blanc. Les scanners se déplacent ensuite de point en point à une cadence fixe — la cadence en points par seconde (PPS) — et le faisceau trace la forme.

#### Comment cela fonctionne dans les logiciels laser traditionnels

Les logiciels laser traditionnels stockent un flux de points pour chaque cue. Pour les cues animés, cela signifie généralement un flux de points distinct pour chaque image. Le point essentiel est que tout est entièrement prédéterminé. Par conséquent, augmenter la cadence de points fait se déplacer les scanners plus rapidement dans les mêmes données prédéfinies.

{% hint style="info" %}
Pour les anciens logiciels, cette approche était nécessaire : les ordinateurs n’étaient tout simplement pas assez rapides pour générer des flux de points en temps réel. C’est pourquoi il existe généralement un éditeur de cue séparé, utilisé pour pré-générer les données de chaque image d’animation.

Cela explique aussi pourquoi le contenu peut occuper des gigaoctets d’espace. En pratique, vous stockez de grandes formes d’onde non compressées à des fréquences d’échantillonnage assez élevées.
{% endhint %}

#### Pourquoi la « cadence de points » a moins de sens dans Liberation

Liberation génère le flux de points en temps réel, ce qui nous donne énormément de flexibilité. Remarquez le réglage "Scanner speed" dans le panneau Laser Settings. Il permet d’accélérer et de ralentir les scanners, mais surtout, il **ne modifie pas** la cadence de points sous-jacente (PPS).

#### Attendez, quoi ? Comment ?

Je sais, cela paraît étrange au début.

Comme Liberation génère le flux de points en temps réel, il peut ajuster ce flux de points. Plus les points sont espacés, plus les scanners se déplacent rapidement. Plus ils sont rapprochés, plus les scanners se déplacent lentement.

{% hint style="info" %}
Dans les versions récentes de Liberation, le _point rate_ réel (dans les réglages avancés) n’affecte plus du tout la vitesse des scanners. À la place, le moteur de rendu ajuste la répartition des points pour correspondre à la cadence de points sélectionnée, tout en conservant inchangé le mouvement des scanners.

Cela a bien un effet sur la « résolution » du trajet des points, mais cela fait surtout une différence pour les graphismes (et peut aider à affiner le réglage _scanner sync_).
{% endhint %}

#### Très bien ! Alors qu’est-ce que tout cela signifie concrètement ?

Bonne question. Voici mes conseils :

* Évitez les scanners sans marque. Si vous pouvez obtenir des scanners plus rapides, faites-le — minimum 30 KPPS.
* Dans la plupart des cas, les scanners DT30 conviennent, et les scanners PT30 sont probablement acceptables dans les lasers moins chers.
* Si vous faites des graphismes, dans la plupart des cas, avoir plus de lasers sera préférable à des scanners plus rapides.
* Lorsque vous passez à des configurations haut de gamme, n’importe laquelle des marques haut de gamme établies conviendra.
* Si vous ne pouvez obtenir que les scanners sans marque les moins chers, les réglages par défaut de Liberation sont assez prudents et vous obtiendrez probablement des résultats corrects pour du travail de faisceaux basique. Si les scanners peinent, réduisez le réglage **Speed** (mais ne modifiez pas la cadence de points !).

#### Et le ILDA Test Pattern ?

…reste très utile comme outil de calibration et de référence, mais il n’a jamais été conçu comme un benchmark complet et peut être utilisé à mauvais escient ou interprété de manière approximative par les fabricants.
