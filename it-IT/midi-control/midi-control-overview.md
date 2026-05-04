---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Panoramica del controllo MIDI

Liberation usa MIDI in diversi modi:

* Come controller live. APC40 Mk1/Mk2, APC Mini e MIDI Fighter Twister possono connettersi automaticamente quando il dispositivo corrispondente è disponibile. Vedi [Controller MIDI live](live-control-with-the-apc40.md "mention").
* Come sorgente di sincronizzazione del clock, usando messaggi MIDI clock e MIDI song position. Vedi [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Come input interattivo nel node MIDI notes per creare effetti in stile "arpa laser". Vedi [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Come sistema di input/output più generale tramite il sistema MIDI Send/Receive. Vedi [MIDI Send/Receive](midi-send-receive.md "mention")

I controller live supportati seguono lo stato mostrato a schermo in Liberation: i pulsanti dei Clip si illuminano con i colori del rispettivo gruppo, i pulsanti delle zone mostrano lo stato della zone e le manopole o gli encoder mappati seguono l’effetto corrente o i controlli del pannello Parameters.
