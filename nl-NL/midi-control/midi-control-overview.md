---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Overzicht van MIDI-besturing

Liberation gebruikt MIDI op verschillende manieren:

* Als live controller. De APC40 Mk1/Mk2, APC Mini en MIDI Fighter Twister kunnen automatisch verbinding maken wanneer het bijbehorende apparaat beschikbaar is. Zie [Live MIDI-controllers](live-control-with-the-apc40.md "mention").
* Als bron voor clocksynchronisatie, met MIDI clock- en MIDI song position-berichten. Zie [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Als interactieve input op de MIDI notes-node om effecten in “laser harp”-stijl te maken. Zie [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Als algemener input-/outputsysteem met het MIDI Send/Receive-systeem. Zie [MIDI verzenden/ontvangen](midi-send-receive.md "mention")

Ondersteunde live controllers volgen de status die Liberation op het scherm toont: knoppen voor Clips lichten op in de kleuren van hun groep, zone-knoppen tonen de status van de zone, en toegewezen draaiknoppen of encoders volgen het huidige effect of de regelaars in het Parameters panel.
