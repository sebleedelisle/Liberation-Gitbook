---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Übersicht zur MIDI-Steuerung

Liberation nutzt MIDI auf verschiedene Arten:

* Als Live-Controller. APC40 Mk1/Mk2, APC Mini und MIDI Fighter Twister können sich automatisch verbinden, wenn das passende Gerät verfügbar ist. Siehe [Live-MIDI-Controller](live-control-with-the-apc40.md "mention").
* Als Quelle für die Clock-Synchronisation, mit MIDI-Clock- und MIDI-Song-Position-Meldungen. Siehe [MIDI-Clock](../tempo-synchronisation.md#midi-clock "mention")
* Als interaktive Eingabe über den MIDI notes-node, um Effekte im Stil einer „Laserharfe“ zu erzeugen. Siehe [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Als allgemeineres Ein-/Ausgabesystem über das MIDI Send/Receive-System. Siehe [MIDI Send/Receive](midi-send-receive.md "mention")

Unterstützte Live-Controller folgen dem Bildschirmstatus von Liberation: Clip-Buttons leuchten in ihren Gruppenfarben, Buttons für zones zeigen den Status der jeweiligen zone an, und zugewiesene Regler oder Encoder folgen dem aktuellen Effekt oder den Bedienelementen im Parameters-Panel.
