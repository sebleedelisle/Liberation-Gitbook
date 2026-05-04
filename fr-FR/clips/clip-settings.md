---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Paramètres de Clip

### Panneau des paramètres de Clip

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Le panneau des paramètres de Clip</p></figcaption></figure>

Modifiez la taille de sortie du Clip avec _Scale X_ et _Scale Y_. Ces deux paramètres sont liés, sauf si vous maintenez la touche _SHIFT_ enfoncée.

Modifiez la position horizontale et verticale du Clip avec _Shift X_ et _Shift Y_.

_Zone Delay/Chase_ est une fonctionnalité tellement intéressante qu’elle a droit à sa propre section. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Panneau Parameters

Le panneau situé à droite du Clip Deck affiche huit paramètres contextuels. Lorsqu’un Clip est sélectionné, les premières commandes sont _Shift X_, _Shift Y_ et _Zone Delay_ pour le Clip sélectionné, suivies des commandes globales _Spin_ et _Scale_.

Ces mêmes paramètres sont aussi repris sur les contrôleurs MIDI compatibles. Si aucun Clip n’est sélectionné, les emplacements propres au Clip restent vides. Si vous maintenez un bouton de groupe enfoncé, les deux premières commandes deviennent les durées de fondu en entrée et de fondu en sortie de ce groupe.

### Verrouiller des Clips

Si un Clip est verrouillé, il ne peut pas être déplacé ni supprimé. Pour verrouiller un Clip, utilisez la case _Locked_ dans le menu du clic droit. Dans le panneau des paramètres de Clip, vous disposez de quelques options supplémentaires.

* _UNLOCK ALL -_ déverrouille tous les Clips du Clip Deck.
* _AUTO-LOCK_ - lorsque _Auto-Lock_ est activé, tout Clip lancé automatiquement (soit avec la timeline, soit avec le système d’enregistrement/lecture MIDI) est verrouillé. C’est utile si vous avez programmé un show dans Logic Pro (ou un logiciel similaire) et que vous ne voulez pas modifier accidentellement les Clips utilisés dans le show.
* _LOCKED CLIPS ZONES_ - si cette option est activée, vous ne pouvez pas modifier les zones des Clips verrouillés.
* _LOCKED CLIPS PARAMS_ - si cette option est activée, vous ne pouvez pas modifier les paramètres (scale, shift, etc.) des Clips verrouillés.

### Menu du clic droit

Si vous faites un clic droit sur un Clip, un menu apparaît avec certaines options propres à ce Clip. Consultez [Introduction au Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Paramètres de Clip](clip-settings.md "mention") et [Groupes de Clips](groups.md "mention") pour en savoir plus sur les premiers éléments de ce menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Par défaut, les Clips sont configurés sur _retrigger_. Cela signifie que, quel que soit le moment où vous les lancez, ils démarrent à partir de cet instant. Donc si vous lancez un Clip en retard, son animation sera légèrement en retard et décalée par rapport au tempo.

{% hint style="info" %}
Si vous utilisez _Tap Tempo_ pendant qu’un Clip avec retrigger est en cours de lecture, le système va « quantifier » le Clip pour le recaler dans le tempo, même si vous ne l’avez pas lancé exactement sur le temps.
{% endhint %}

Si _Retrigger_ n’est pas activé, le Clip restera toujours dans le tempo : c’est comme si le Clip avait été lancé tout au début de l’horloge. C’est utile lorsque vous êtes parfaitement synchronisé avec la musique via un signal d’horloge externe.

{% hint style="info" %}
Les Clips sont souvent conçus pour boucler indéfiniment, mais vous pouvez aussi les créer de façon à ce qu’ils ne se jouent qu’une seule fois, ou seulement quelques fois. Veillez à laisser ceux-ci réglés sur _retrigger_, sinon ils ne redémarreront pas !
{% endhint %}

### Temps de transition entrée/sortie (fondu)

Les Clips peuvent être configurés pour faire un fondu en entrée et en sortie, avec une durée mesurée en secondes. Par défaut, le temps de fondu est hérité des paramètres de son groupe (et peut être modifié en faisant un clic droit sur le bouton du groupe).

Si vous voulez une durée de fondu différente de celle du groupe du Clip, désactivez d’abord le bouton _USE GROUP DEFAULT_, puis ajustez les curseurs _In time_ et _Out time_ du Clip.
