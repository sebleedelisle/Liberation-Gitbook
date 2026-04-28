---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Le système MIDI Send/Receive est distinct des contrôles APC40. Il permet d’envoyer des données MIDI vers Liberation et d’en recevoir depuis Liberation. Les fonctions comme le démarrage et l’arrêt des clips, le réglage des paramètres globaux, des effets et des paramètres de clips disposent toutes d’une commande MIDI associée.

{% hint style="info" %}
Le système MIDI Send/Receive a été créé à l’origine avant que Liberation ne dispose de fonctionnalités de Timeline ; c’était une solution de contournement que vous pouviez utiliser pour enregistrer et relire un show dans un logiciel de musique comme Logic Pro ou Cubase.

Il vous donne un contrôle direct sur les clips, les effets et les réglages, indépendamment de l’affichage et de la position de défilement du Clip Deck. Des fonctions de contrôle live plus globales, comme le tap tempo, l’assignation de zones et l’armement/désarmement, ne sont pas implémentées.
{% endhint %}

### Réglages MIDI Send/Receive

Ouvrez le panneau _MIDI Send/Receive_ (avec le menu _View -> MIDI Send/Receive_). Vous verrez que vous pouvez choisir _SEND, RECEIVE,_ ou _BOTH_ pour l’envoi et la réception, ainsi que sélectionner les interfaces MIDI que vous souhaitez utiliser.

{% hint style="danger" %}
Utilisez le réglage _BOTH_ avec prudence. Les appareils et logiciels MIDI peuvent être configurés pour renvoyer les données qu’ils reçoivent ; cela peut provoquer une boucle de rétroaction de données MIDI, ce qui est à éviter.
{% endhint %}

### Mapping MIDI

Voir [midi-send-receive-default-mapping.md](../reference/midi-send-receive-default-mapping.md "mention")

Je prévois d’ajouter à l’avenir un mapping MIDI beaucoup plus personnalisable. En attendant, vous pouvez utiliser des applications comme [BOME](https://www.bome.com/products/miditranslator) et [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) pour faire la conversion entre Liberation et votre matériel personnalisé.
