---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Modifie les couleurs de tout le contenu entrant. Vous pouvez définir des valeurs HSB fixes, ou passer au système de dégradé et échantillonner des couleurs depuis un dégradé personnalisé.

* **hue, saturation, brightness** - les valeurs de couleur, voir [Paramètres de couleur et HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - la teinte n’est pas modifiée
  * FIXED - la teinte des éléments est définie sur la valeur de teinte
  * SHIFT - la teinte des éléments est décalée selon la valeur indiquée. Ainsi, les éléments de couleurs différentes restent différents, mais sont simplement décalés le long de la teinte.
* **saturation mode** -
  * OFF - la saturation n’est pas modifiée
  * FIXED - la saturation est fixée à la valeur spécifiée.
* **brightness mode** -
  * OFF - la luminosité n’est pas modifiée
  * FIXED - la luminosité des éléments est définie sur la valeur de luminosité
  * MULTIPLY - la luminosité des éléments est combinée avec la valeur de luminosité. Ainsi, s’ils clignotent, ils continuent de clignoter, mais seulement jusqu’à la luminosité indiquée ici.
* **gradient mode** - passe des curseurs HSB fixes à l’éditeur de dégradé. Le node échantillonne une couleur du dégradé, puis l’applique en utilisant les modes de teinte, de saturation et de luminosité ci-dessus.
* **gradient position** - choisit le point du dégradé à échantillonner. Animez ce paramètre de 0 % à 100 % avec un Sawtooth Oscillator pour parcourir le dégradé au fil du temps.
* **blend** - définit l’intensité d’application du changement de couleur : 0 % signifie aucun effet, 100 % l’effet complet, et 50 % une combinaison entre la couleur existante et les nouvelles valeurs.

{% hint style="info" %}
Le node Colour Change échantillonne une seule couleur du dégradé pour toute l’entrée. Si vous voulez que le dégradé s’applique sur la forme selon la position, utilisez plutôt [modificateurs basés sur la position](position-based-changers.md "mention").
{% endhint %}

### Éditeur de dégradé

Lorsque **gradient mode** est activé, l’éditeur de dégradé apparaît sous les contrôles principaux.

* Cliquez sur la barre de dégradé pour ajouter un point de couleur.
* Faites un clic gauche sur un point pour le sélectionner, puis faites-le glisser horizontalement pour le déplacer.
* Faites glisser un point sélectionné vers le bas, à l’écart de la barre, ou appuyez sur Delete/Backspace pour le supprimer. Un dégradé conserve toujours au moins deux points.
* Faites un clic droit sur un point pour le modifier avec le sélecteur de couleur.
* Utilisez **Position**, **Hue**, **Saturation** et **Brightness** pour modifier précisément le point sélectionné.
* **interpolation** choisit la façon dont les couleurs sont mélangées entre les points :
* **HSB** - mélange la teinte, la saturation et la luminosité. C’est l’option la plus adaptée pour des mouvements fluides de type arc-en-ciel autour de la roue chromatique.
* **RGB** - mélange directement les valeurs rouge, vert et bleu. Le résultat ressemble souvent davantage à un fondu de couleur sur un écran ou une console lumière.
* **NONE** - passe d’un point au suivant sans mélange.
* **hue direction** est disponible avec l’interpolation HSB :
* **AUTO** - emprunte le chemin le plus court autour de la roue des teintes.
* **FORWARDS** - parcourt toujours les valeurs de teinte vers l’avant.
* **BACKWARDS** - parcourt toujours les valeurs de teinte vers l’arrière.
