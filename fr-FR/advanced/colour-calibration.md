---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Étalonnage des couleurs

L’étalonnage des couleurs garantit que les lasers rouge, vert et bleu de votre projecteur produisent une lumière fluide et prévisible à tous les niveaux de luminosité. Certains projecteurs ont des courbes de luminosité non linéaires : par exemple, 50 % de rouge peut paraître beaucoup plus lumineux ou plus sombre que la moitié de l’intensité de 100 % de rouge. L’étalonnage corrige cela afin que les couleurs se mélangent proprement, que les dégradés soient réguliers et que les blancs soient équilibrés.

#### Faire chauffer votre projecteur

Le comportement des diodes laser change lorsqu’elles montent en température. Laissez toujours votre projecteur se stabiliser avant l’étalonnage :

* Projetez une image lumineuse, par exemple le **White rectangle test pattern (11)**, pendant au moins **15 à 20 minutes**.
* Cela garantit que l’équilibre des couleurs que vous définissez restera constant pendant un show.

#### Fonctionnement du test d’étalonnage

Utilisez les motifs de test pour l’étalonnage (voir [Mires de test](../output-view/test-patterns.md "mention"))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Chacun affiche quatre lignes en mouvement :

* **Ligne du haut** – luminosité à 100 % à vitesse maximale
* **Deuxième ligne** – luminosité à 75 % à 75 % de la vitesse
* **Troisième ligne** – luminosité à 50 % à 50 % de la vitesse
* **Quatrième ligne** – luminosité à 25 % à 25 % de la vitesse

Comme la luminosité _et la vitesse_ sont réduites ensemble, toutes les lignes devraient sembler avoir la même luminosité. Si l’une d’elles paraît plus claire ou plus sombre, ajustez le curseur correspondant jusqu’à ce qu’elles correspondent.

Chaque motif de test comporte également une cinquième ligne à **0 % de luminosité**, qui ne devrait pas être visible. Elle sert à corriger les lasers qui n’émettent aucune lumière à très bas niveau. Si votre laser reste invisible à faible luminosité, augmentez progressivement le **réglage 0 %** jusqu’à ce que la ligne devienne tout juste visible, puis réduisez-le légèrement jusqu’à ce qu’elle disparaisse à nouveau. L’objectif est de trouver le seuil auquel le laser commence à s’allumer, puis de rester juste en dessous, afin que vos fondus commencent naturellement sans couper le bas de la plage.

#### Utiliser le panneau Colour Calibration

Le panneau vous donne des contrôles indépendants pour chaque canal (rouge, vert, bleu) aux niveaux 100, 75, 50, 25 et 0 %.

1. **Sélectionnez un motif de test** (commencez par le rouge).
2. **Ajustez les curseurs** afin que les lignes à 100, 75, 50 et 25 % semblent avoir la même luminosité.
3. **Ajustez finement le curseur 0 %** si la ligne « éteinte » reste légèrement visible.
4. **Répétez l’opération pour le vert et le bleu.**
5. Passez au **White test pattern (8)**. Les quatre lignes devraient paraître identiques, et le blanc devrait sembler neutre (sans teinte).

#### Ajuster la balance des blancs

Vous pouvez également utiliser ce système pour ajuster la **balance des blancs**. Après avoir étalonné chaque canal individuellement, passez au **White test pattern (8)**. Si la sortie semble teintée (par exemple trop verte ou trop bleue), ajustez les niveaux relatifs des canaux rouge, vert et bleu jusqu’à ce que les lignes apparaissent en blanc neutre. Même si vos lasers ont des puissances très différentes, l’étalonnage aidera à les rapprocher et à produire un mélange de couleurs plus propre et mieux équilibré.

#### Enregistrer votre étalonnage

* Utilisez **Store** pour écraser le préréglage actuel.
* Utilisez **Store As** pour créer un nouveau préréglage (utile si vous travaillez avec plusieurs lasers).
