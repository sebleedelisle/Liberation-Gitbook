---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Zones cibles du Canvas

Nous savons comment envoyer des parties du Canvas vers des zones dans chaque laser, mais pour placer du contenu dans le Canvas au départ, vous aurez besoin des _Canvas target areas_ — un nom un peu déroutant, mais exact.

Les _Canvas target areas_ sont des sections du Canvas dans lesquelles vous pouvez envoyer des clips. Dans la vue _CANVAS_, elles sont représentées par des rectangles à contour bleu.

La plupart du temps, une seule Canvas target area peut suffire, que vous diviserez ensuite en plusieurs zones envoyées à différents lasers.

Dans certains cas, vous pouvez aussi vouloir plusieurs Canvas target areas pour différentes parties d’un bâtiment, ou pour tirer parti du délai de zone entre elles. (Oui ! Le délai de zone fonctionne aussi entre les Canvas target areas !)

### Envoyer des clips vers les Canvas target areas

Si vous regardez dans le Clip Deck, à côté des boutons de zones de faisceaux, vous verrez les boutons des Canvas target areas. Vous devrez peut-être faire défiler les boutons de sortie pour les voir : utilisez `Shift + Left / Right Arrow`, les boutons ZONE PAGE à l’écran, ou les boutons de l’APC40 (voir [apc40-reference.md](../reference/apc40-reference.md "mention")).

Assignez des clips aux Canvas target areas en activant ces boutons exactement comme vous le feriez avec les boutons de zones de faisceaux.

### Ajouter / modifier des Canvas target areas

Dans la barre de menu supérieure, sélectionnez _View -> Canvas Target Areas_ : vous verrez tous les réglages de chaque Canvas target area présente dans votre projet.

En haut se trouve le bouton _ADD CANVAS TARGET AREA_.

Supprimez une Canvas target area à l’aide du bouton rouge avec un signe moins.

Ajustez la taille et la position avec les curseurs. Double-cliquez sur un curseur pour saisir une valeur.

### Mode de mise à l’échelle

* **FIT TO AREA** - réduit le contenu pour qu’il tienne entièrement dans la Canvas target area, tout en conservant le rapport d’aspect. (C’est le réglage par défaut)
* **FILL AREA** - agrandit le contenu pour remplir la Canvas target area, tout en conservant le rapport d’aspect. Le contenu peut être coupé sur les bords.
* **STRETCH TO FIT** - étire le contenu pour remplir toute la Canvas target area, sans tenir compte du rapport d’aspect.
