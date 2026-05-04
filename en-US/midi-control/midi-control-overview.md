---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI control overview

There are several ways that Liberation uses MIDI:

* As a live controller. The APC40 Mk1/Mk2, APC Mini and MIDI Fighter Twister can connect automatically when the matching device is available. See [Live MIDI Controllers](live-control-with-the-apc40.md "mention").
* As a clock sync source, using MIDI clock and MIDI song position messages. See [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* As an interactive input on the MIDI notes node to create "laser harp" style effects. See [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* As a more general input/output system using the MIDI Send/Receive system. See [MIDI Send/Receive](midi-send-receive.md "mention")

Supported live controllers follow Liberation's on-screen state: clip buttons light up with their group colors, zone buttons show zone state, and mapped knobs or encoders follow the current effect or Parameters panel controls.
