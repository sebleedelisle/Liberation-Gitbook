---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Oversigt over MIDI control

Der er flere måder, Liberation bruger MIDI på:

* Som live-controller. APC40 Mk1/Mk2, APC Mini og MIDI Fighter Twister kan oprette forbindelse automatisk, når den tilsvarende enhed er tilgængelig. Se [Live MIDI-controllere](live-control-with-the-apc40.md "mention").
* Som kilde til clock-synkronisering ved hjælp af MIDI clock- og MIDI song position-beskeder. Se [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Som interaktiv input på MIDI notes-noden til at lave effekter i “laserharpe”-stil. Se [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Som et mere generelt input/output-system ved hjælp af MIDI Send/Receive-systemet. Se [MIDI Send/Receive](midi-send-receive.md "mention")

Understøttede live-controllere følger Liberations tilstand på skærmen: Clip-knapper lyser med deres gruppefarver, zone-knapper viser zone-tilstand, og mappede knapper eller encodere følger den aktuelle effekt eller kontrollerne i Parameters-panelet.
