---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synchronisation

La synchronisation musicale est un élément fondamental de Liberation : une fois que le tempo et les temps sont alignés sur la musique, vous pouvez être sûr que tout restera synchronisé. Si vous avez la chance de disposer d’une horloge MIDI (ou d’Ableton Link), vous n’avez pas du tout à vous soucier de la synchronisation manuelle. Sinon, pas d’inquiétude : vous pouvez vous caler manuellement grâce à la fonction de tempo _Live_.

Si vous avez déjà utilisé des logiciels de musique ou d’éclairage, ce processus vous sera familier. Sinon, il vaut la peine de prendre le temps de vous familiariser avec le système et de vous entraîner chez vous avant d’arriver sur un spectacle live.

## Panneau Tempo

Le panneau _Tempo_ reste toujours affiché à l’écran et contient tous les réglages de synchronisation. En haut, vous verrez le compteur mesure/temps actuel, ainsi qu’un transport avec les boutons lecture/pause et retour/avance rapide.

En dessous, vous verrez le marqueur de temps : quatre carrés qui « pulsent » sur le beat. Ce _beat marker_ est une visualisation extrêmement utile, que vous consulterez constamment lorsque vous utiliserez le système de tempo _Live_.

### Régler le tempo

Vous avez plusieurs options pour régler le tempo :

* Cliquez-glissez sur le curseur _Tempo_
* Maj-clic puis glissez sur le curseur _Tempo_ pour modifier le tempo par incréments de 0,1
* Double-cliquez sur le curseur _Tempo_ et saisissez le nombre manuellement
* Utilisez le potentiomètre _Tempo_ de l’APC40 (appuyez sur Shift pour des incréments de 0,1)
* Tap Tempo

{% hint style="info" %}
Le tempo est défini en « battements par minute » et la valeur par défaut traditionnelle est généralement 120.
{% endhint %}

## Tap Tempo

Réglez le tempo automatiquement en cliquant sur le bouton _TAP_ en rythme avec le beat. Définissez le début de la mesure avec le bouton _RESET_.

{% hint style="info" %}
Le système Tap Tempo est suffisamment intelligent pour savoir si vous avez arrêté de taper pendant un moment, ou si vous avez manqué quelques temps. Si vous commencez à taper en double tempo, il comprendra que vous voulez doubler le tempo ; il en va de même si vous tapez en mi-tempo.

Il est également capable de détecter si deux personnes tapent le tempo en même temps (par exemple une au clavier et une sur l’APC40). Liberation fera la moyenne des doubles frappes.
{% endhint %}

#### Commandes clavier :

T - tap tempo\
R - reset the bar\
Y - arrondir le tempo au battement par minute le plus proche.

{% hint style="info" %}
Comme la plupart des musiques actuelles sont créées numériquement, le tempo est généralement un nombre entier arrondi. Donc, si le tempo tapé semble proche, utilisez la touche Y (ou déplacez le potentiomètre de tempo de l’APC40 d’un « cran ») pour l’arrondir à un nombre entier.
{% endhint %}

#### Contrôles APC40 :

L’APC40 dispose d’un bouton dédié _TAP TEMPO_, mais vous pouvez aussi utiliser un footswitch connecté pour taper le tempo au pied !

Utilisez le potentiomètre _TEMPO_ pour ajuster. Appuyez sur _SHIFT_ pendant que vous utilisez le potentiomètre _TEMPO_ pour des réglages fins.

Utilisez le bouton _METRONOME_ pour **réinitialiser la mesure**. (Notez que le bouton _METRONOME_ s’allume également en rythme avec le beat)

Tournez le potentiomètre _TEMPO_ d’un « cran » vers la droite ou la gauche pour **arrondir le tempo** vers le haut ou vers le bas à un nombre entier de BPM.

Voir aussi [Référence APC40](reference/apc40-reference.md "mention")

### Nudge tempo

Si vous êtes sûr d’être assez proche du tempo réel, mais que vous constatez un décalage progressif, utilisez les boutons _NUDGE_ pour corriger.

Si le tempo de Liberation prend de l’avance sur la musique, maintenez _NUDGE -_ enfoncé pour ralentir temporairement jusqu’à ce qu’il se recale.

Si le tempo de Liberation prend du retard sur la musique, maintenez _NUDGE +_ enfoncé pour accélérer temporairement jusqu’à ce qu’il se recale.

{% hint style="info" %}
Vous pouvez utiliser soit les boutons NUDGE à l’écran, soit les boutons dédiés de l’APC40.
{% endhint %}

### Mi-tempo / double tempo

Utilisez les boutons _÷2_ et _x2_ pour diviser par deux ou doubler le tempo de façon permanente. Contrairement au multiplicateur de tempo, il s’agit d’un changement permanent du tempo actuel.

## Tempo Multiplier

Le système _Tempo Multiplier_ vous permet d’ajuster temporairement le tempo avant de revenir à sa valeur précédente.

Activez/désactivez le _Tempo Multiplier_ en appuyant sur le bouton _TEMPO MULTIPLIER_ ou sur le bouton _BANK_ de l’APC40. Ajustez-le avec le curseur à l’écran ou avec le curseur A-B de l’APC40. Vous pouvez aussi utiliser les boutons de préréglage _25%, 50%, 100% 200%_.

## Sources de tempo externes

### MIDI Clock

Pour vous synchroniser sur un signal d’horloge MIDI externe, sélectionnez le bouton radio _MIDI CLOCK_ et choisissez l’appareil MIDI dans le menu déroulant. Notez le voyant d’état coloré à côté des menus déroulants :

* Vert - réception d’un signal d’horloge MIDI
* Orange - connexion possible à l’appareil MIDI, mais aucun signal d’horloge n’est actuellement reçu
* Rouge - connexion impossible à l’appareil MIDI

{% hint style="info" %}
MIDI Clock diffuse une série de trames (24 par noire), mais les messages ne contiennent aucune donnée de position. Cela signifie que c’est utile pour rester en rythme, mais que vous devrez peut-être quand même réinitialiser la mesure.

La source de tempo MIDI Clock de Liberation répond également aux messages **MIDI Machine Control (MMC)** ; donc si votre source d’horloge les transmet, vous n’aurez pas besoin de réinitialiser la mesure manuellement.
{% endhint %}



### Timeline

Chaque timeline possède son propre tempo, qui peut être une valeur fixe ou une _Tempo Map_. La _Tempo Map_ vous permet d’ajuster le tempo à des moments précis dans la timeline.

Le tempo de la timeline sera utilisé lorsque _TIMELINE_ est sélectionné comme source de tempo.

{% hint style="info" %}
Vous pouvez lancer une timeline avec _n’importe quelle_ source de tempo ! Ainsi, si vous avez un groupe live qui ne joue pas au clic, vous pouvez démarrer la timeline manuellement et la garder synchronisée avec la source de tempo _LIVE_. Ou si vous avez un signal d’horloge MIDI, vous pouvez l’utiliser !
{% endhint %}
