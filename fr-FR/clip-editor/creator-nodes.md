---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Nœuds Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Crée un point / faisceau unique.

* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **Colour** - la couleur du point. Voir [Paramètres de couleur et HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Crée une ligne / nappe.

* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **Size** - la longueur de la ligne
* **Colour** - la couleur de la ligne. Voir [Paramètres de couleur et HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* **rotation** - l’angle de la ligne, en degrés
* **resolution** - voir [Résolution](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ définit le point de départ et le centre de rotation de la ligne
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Crée un cercle / cône.

* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **radius** - le rayon du cercle
* **Colour** - la couleur du cercle. Voir [Paramètres de couleur et HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* **resolution** - voir [Résolution](fundamentals/resolution.md "mention")
* **Fill state** - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Crée un polygone équilatéral : triangle, carré, pentagone, etc.

* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **size** - la distance entre le centre et chacun des sommets
* **Colour** - la couleur du polygone. Voir [Paramètres de couleur et HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* **rotation** - l’angle de rotation de la forme, en degrés
* **resolution** - voir [Résolution](fundamentals/resolution.md "mention")
* **Fill state** - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Charge un fichier SVG pour créer des formes personnalisées.

{% hint style="warning" %}
Liberation est compatible avec le format _SVGTiny_. InkScape est recommandé, mais la plupart des applications de dessin vectoriel peuvent exporter dans ce format. Veillez à convertir tout texte en formes avant l’exportation. Liberation affichera les contours et pourra aussi utiliser les remplissages comme masques. Assurez-vous que vos lignes ne sont pas noires, sinon elles ne s’afficheront pas sans modificateur de couleur !
{% endhint %}

* **Import SVG** - charge un fichier SVG depuis le disque.

{% hint style="info" %}
Une fois un SVG chargé, son contenu est converti et enregistré dans le clip. Vous n’avez donc pas besoin de conserver une référence au fichier, sauf si vous souhaitez modifier ultérieurement les paramètres de masque.
{% endhint %}

* **Use fills as masks** - traite toute forme remplie comme un masque, c.-à-d. comme si elle était remplie en noir. Cette option est activée automatiquement si votre SVG contient des formes remplies. S’il ne contient aucune forme remplie, elle est désactivée. Voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - si les formes de votre SVG n’ont pas de contour, Liberation ne peut pas les dessiner ! Cette option ajoute un contour (ou _stroke_) à toute forme remplie. Si votre SVG ne contient aucune forme avec contour, elle est activée automatiquement. S’il ne contient aucune forme remplie, elle est désactivée.
* **Invert black lines** - si toutes les lignes de votre SVG sont noires, vous ne pouvez pas les voir ! Cette option les rend blanches. Elle est activée automatiquement si votre SVG ne contient que des formes noires, mais elle est désactivée s’il n’en contient aucune.
* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **scale** - ajuste la taille du SVG. Cette valeur est calculée automatiquement au chargement du SVG pour s’assurer que l’image est visible, mais elle peut ensuite être modifiée manuellement.
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* **rotation** - l’angle de rotation de l’image, en degrés
* **resolution** - voir [Résolution](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Crée une animation à partir d’une séquence de fichiers SVG.

* **Import SVG Sequence** - choisissez le dossier contenant tous les fichiers SVG. Notez qu’ils sont chargés dans l’ordre alphanumérique.

{% hint style="info" %}
Une fois la séquence SVG chargée, son contenu est converti et enregistré dans le clip. Vous n’avez donc pas besoin de conserver une référence aux fichiers, sauf si vous souhaitez modifier ultérieurement les paramètres de masque.
{% endhint %}

* **Use fills as masks** - traite toute forme remplie comme un masque, c.-à-d. comme si elle était remplie en noir. Cette option est activée automatiquement si l’un de vos SVG contient des formes remplies. Si aucun n’en contient, elle est désactivée. Voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - si les formes de vos SVG n’ont pas de contour, Liberation ne peut pas les dessiner ! Cette option ajoute un contour (ou _stroke_) à toute forme remplie. Si vos SVG ne contiennent aucune forme avec contour, elle est activée automatiquement. Si aucun ne contient de forme remplie, elle est désactivée.
* **Invert black lines** - si toutes les lignes de vos SVG sont noires, vous ne pouvez pas les voir ! Cette option les rend blanches. Elle est activée automatiquement si vos SVG ne contiennent que des formes noires, mais elle est désactivée s’ils n’en contiennent aucune.
* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **scale** - ajuste la taille de l’image.
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* **rotation** - l’angle de rotation de l’image, en degrés
* **resolution** - voir [Résolution](fundamentals/resolution.md "mention")
* **speed** - la durée de l’animation complète, en mesures.
* **time per frame** - si cette option est activée, la durée s’applique à chaque image plutôt qu’à l’ensemble de l’animation. Ainsi, si _speed_ est réglé sur ¼, chaque image durera 1 temps.
* **animation direction** -
  * _FORWARDS_ - l’animation avance, puis revient au début en boucle
  * _BACKWARDS_ - l’animation recule, puis revient à la fin en boucle
  * _PINGPONG_ - l’animation avance puis recule en boucle
  * _MANUAL_ - l’image actuelle est définie avec le réglage _position manual_
* **position manual** - définit l’image actuelle : 0 % correspond à la première image, 100 % à la dernière. Cette valeur peut être réglée manuellement ou avec un oscillateur externe.
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Crée du texte avec une police TrueType ou OpenType.

* **Text** - saisissez ici le texte souhaité
* **Font** - choisissez la police souhaitée

{% hint style="info" %}
Pour ajouter d’autres polices à Liberation, copiez les fichiers .ttf ou .otf dans le dossier `data/fonts` du dossier de travail de Liberation, puis redémarrez Liberation.
{% endhint %}

* **Render profile** - voir [Render Profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - choisissez _LEFT_, _CENTRE_ ou _RIGHT_ pour sélectionner l’alignement du texte.
* **Fill state** - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - la taille du texte
* **monospace** - affiche chaque caractère avec la même largeur. C’est utile pour les minuteurs et les compteurs, car le texte ne se décale pas latéralement lorsque les chiffres changent.
* **character spacing** - ajuste l’espacement entre les caractères. Augmentez-le pour un interlettrage plus large, ou réduisez-le pour resserrer le texte.
* **colour -** voir [Paramètres de couleur et HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** and **y** position - voir [Système de coordonnées](fundamentals/co-ordinate-system.md "mention")
* **rotation** - l’angle de rotation de l’image, en degrés
* **resolution** - voir [Résolution](fundamentals/resolution.md "mention")
* **reveal** - utilisez ce réglage pour révéler progressivement le texte, un caractère à la fois. Entre 0 et 50 %, le texte apparaît progressivement de gauche à droite. Entre 50 % et 100 %, il disparaît de gauche à droite. Vous pouvez connecter un oscillateur à cette entrée pour créer des animations.
* **reveal by word** - lorsque cette option est activée, _reveal_ fonctionne mot par mot plutôt que caractère par caractère.
* **countdown** - remplace le texte saisi par un compte à rebours. Lorsque le compte à rebours atteint zéro, la valeur **Text** normale s’affiche.
* **use seconds** - compte en secondes réelles. Lorsque cette option est désactivée, le compte à rebours est basé sur le tempo : deux pulsations comptent comme une seconde, de sorte que 120 bpm correspond aux secondes réelles.
* **show minutes/seconds** - affiche le temps restant en minutes et secondes. S’il dépasse une heure, les heures sont également incluses.
* **countdown to date/time** - compte à rebours jusqu’à une date et une heure UTC précises, au lieu de compter à rebours à partir d’un nombre.
* **countdown datetime** - définit la date et l’heure UTC cibles lorsque **countdown to date/time** est activé.
* **start number** - nombre de départ lorsque **countdown to date/time** est désactivé.
* _MOVE TO FRONT / MOVE TO BACK_ - voir [Remplissages, masques et tri en profondeur](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Si le menu déroulant des polices est ouvert, les touches fléchées haut et bas permettent de parcourir les polices disponibles.
{% endhint %}
