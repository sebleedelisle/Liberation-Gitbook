---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Vue d’ensemble du contrôle MIDI

Liberation utilise le MIDI de plusieurs façons :

* Comme contrôleur live. L’APC40 Mk1/Mk2, l’APC Mini et le MIDI Fighter Twister peuvent se connecter automatiquement lorsque l’appareil correspondant est disponible. Voir [Contrôleurs MIDI live](live-control-with-the-apc40.md "mention").
* Comme source de synchronisation d’horloge, à l’aide de l’horloge MIDI et des messages de position dans le morceau MIDI. Voir [Horloge MIDI](../tempo-synchronisation.md#midi-clock "mention")
* Comme entrée interactive sur le node MIDI notes, pour créer des effets de type « harpe laser ». Voir [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Comme système d’entrée/sortie plus général, avec le système MIDI Send/Receive. Voir [MIDI Send/Receive](midi-send-receive.md "mention")

Les contrôleurs live pris en charge suivent l’état affiché à l’écran dans Liberation : les boutons de Clip s’allument avec les couleurs de leur groupe, les boutons de zone indiquent l’état de la zone, et les potentiomètres ou encodeurs mappés suivent l’effet actuel ou les contrôles du panneau Parameters.
