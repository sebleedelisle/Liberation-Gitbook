---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI-ohjauksen yleiskatsaus

Liberation käyttää MIDIä useilla tavoilla:

* Live-ohjaimena. APC40 Mk1/Mk2, APC Mini ja MIDI Fighter Twister voivat muodostaa yhteyden automaattisesti, kun vastaava laite on käytettävissä. Katso [Live MIDI Controllers](live-control-with-the-apc40.md "mention").
* Kellon synkronointilähteenä MIDI-kellon ja MIDI song position -viestien avulla. Katso [MIDI Clock](../tempo-synchronisation.md#midi-clock "mention")
* Interaktiivisena syötteenä MIDI notes -nodessa, jolla voi luoda “laser harp” -tyylisiä efektejä. Katso [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Yleisempänä syöttö- ja lähtöjärjestelmänä MIDI Send/Receive -järjestelmän avulla. Katso [MIDI Send/Receive](midi-send-receive.md "mention")

Tuetut live-ohjaimet seuraavat Liberationin näytöllä näkyvää tilaa: Clip-painikkeet syttyvät ryhmiensä väreissä, zone-painikkeet näyttävät zone-tilan, ja mäpätyt säätimet tai enkooderit seuraavat nykyisen efektin tai Parameters-paneelin säätimiä.
