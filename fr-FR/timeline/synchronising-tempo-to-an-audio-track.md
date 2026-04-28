---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Synchroniser le tempo avec une piste audio

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchroniser le tempo avec une piste audio" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

La timeline de Liberation est conçue pour fonctionner avec des tempos fixes ou variables, mais une synchronisation fiable commence toujours par l’identification du tempo et l’alignement correct de l’audio. Cette section décrit le flux de travail recommandé.

#### 1. Aligner le premier temps fort

Ajoutez votre piste audio à la timeline et assurez-vous qu’elle est aimantée sur un temps, de sorte que le **premier temps fort musical** de la piste soit parfaitement aligné avec le début d’une mesure.

Cette étape est essentielle.

Si l’audio ne commence pas naturellement sur un temps fort, vous avez deux options :

* **Ajuster le retard du clip**\
  Faites un clic droit sur le clip audio et ajustez la valeur Delay jusqu’à ce que le premier temps fort soit aligné avec un repère de temps ou de mesure.
* **Découper l’audio dans un outil externe**\
  Modifiez le fichier audio dans un éditeur externe comme Audacity, afin que le fichier commence exactement sur le premier temps fort, puis réimportez-le.

{% hint style="info" %}
**Important :**\
Si le début de l’audio n’est pas aligné sur un temps ou une mesure, la position de départ perçue de la musique se décalera vers l’arrière et vers l’avant lorsque vous modifierez le tempo. Cela rend la correspondance précise du tempo extrêmement difficile.
{% endhint %}

#### 2. Définir un tempo initial

Si vous avez une idée approximative du BPM, saisissez-la dans le contrôle de tempo de la timeline et lancez la lecture depuis le début.

Observez attentivement les repères de temps et de mesures pendant la lecture de la piste.

* Si les repères prennent de l’avance sur la musique, réduisez légèrement le tempo.
* S’ils prennent du retard, augmentez légèrement le tempo.
* Arrêtez la lecture, ajustez le tempo, puis réessayez.

Pour la plupart des musiques modernes, le tempo est un BPM entier et fixe. Une fois que vous avez trouvé la bonne valeur, il devrait rester calé sur toute la durée de la piste.

#### 3. Utiliser la forme d’onde comme repère visuel

La forme d’onde audio est une référence utile pour ajuster le tempo.

* Les transitoires et les pics doivent s’aligner avec les repères verticaux de mesures.
* Zoomez fortement pour vérifier l’alignement sur plusieurs mesures.

**Astuce :**\
Utilisez la molette de la souris ou le geste du trackpad pour zoomer dans la timeline. Utilisez la molette horizontale ou le geste horizontal pour vous déplacer vers la gauche et la droite. Travailler avec un fort niveau de zoom rend les petits ajustements beaucoup plus faciles.

#### 4. Pistes avec un BPM non entier

Si la piste n’utilise pas un BPM entier, le décalage sera plus progressif.

* Zoomez davantage.
* Utilisez des ajustements de tempo plus fins.
* Vérifiez l’alignement sur des sections plus longues de la piste, plutôt que seulement sur les premières mesures.

#### 5. Musique avec changements de tempo

Si la musique accélère ou ralentit, utilisez le Tempo Map :

* Lancez la piste et observez les repères de temps.
* Lorsque le décalage devient visible, ajoutez un changement de tempo à cet endroit.
* Ajustez le tempo de la nouvelle section jusqu’à ce qu’elle soit à nouveau calée.

Répétez ce processus pour chaque changement de tempo dans la musique.

#### 6. Analyse externe du tempo (facultatif)

En dernier recours, vous pouvez analyser la piste dans une DAW comme Logic Pro et générer automatiquement une tempo map. Gardez à l’esprit que cela produit souvent un grand nombre de changements de tempo, parfois un par mesure, ce qui peut être plus détaillé que nécessaire pour la plupart des shows.
