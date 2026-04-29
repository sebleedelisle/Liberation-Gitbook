---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Modificateurs de tracé

## &#x20;Dotter

Ce nœud remplace le contenu des lignes et des formes par des points régulièrement espacés (les points existants ne sont pas modifiés).

* **Colour** – la couleur des points. Ignorée si _Inherit Colour_ est activé, voir ci-dessous. _Voir aussi_ [Paramètres de couleur et HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – la distance entre les points, mesurée en pixels. Valeurs plus faibles = plus de points, valeurs plus élevées = moins de points.
* **Offset** – décale la position de départ des points, en pourcentage de l’espacement. Peut être animé (par exemple avec un nœud Oscillator en dent de scie) pour créer des effets de points « en déplacement ».
* **Keep Original** – si cette option est activée, les lignes/formes d’origine sont conservées et les points sont dessinés par-dessus.
* **Render Profile** – choisit la qualité de rendu. _Voir_ [Render Profile](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – ajuste automatiquement l’espacement afin que la longueur du tracé soit divisible de façon régulière.
* **Fade Out Ends** – réduit progressivement la luminosité des points vers le début et la fin du tracé. Utile lorsque vous animez **Offset** avec un nœud Oscillator en dent de scie, afin que les points apparaissent et disparaissent en douceur lorsqu’ils atteignent l’extrémité de la forme.

## &#x20;Trimmer

Ce nœud réduit la longueur visible des lignes et des formes, ce qui vous permet de les révéler, de les masquer ou de les animer dans le temps.

* **Offset** – contrôle l’endroit où commence la partie visible de la forme. Même avec _Trim Size_ à 0 %, animer Offset de 0 % → 100 % fait se dessiner la forme, la rend entièrement visible à 50 %, puis la fait disparaître de nouveau.
* **Trim Size** – définit la proportion de la forme conservée, en pourcentage de sa longueur totale.
* **Loop** – traite la forme comme une boucle continue : la fin se reconnecte au début au lieu de disparaître.
* **All Shapes** – combine toutes les formes en entrée et les découpe comme s’il s’agissait d’un seul tracé. Si l’option est désactivée, chaque forme est découpée individuellement.
* **Add Dot at Start / Add Dot at End** – ajoute un point de la couleur choisie aux points de découpe. (Si aucune découpe n’est appliquée, aucun point n’est ajouté.)
* **Colour** – la couleur des points de découpe. _Voir aussi_ [Paramètres de couleur et HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – choisit le profil de rendu pour les points. _Voir_ [Render Profile](../fundamentals/render-profile.md "mention")
