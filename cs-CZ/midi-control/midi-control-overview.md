---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Přehled ovládání přes MIDI

Liberation využívá MIDI několika způsoby:

* Jako ovladač pro živé ovládání s APC40. Viz [Živé ovládání pomocí APC40](live-control-with-the-apc40.md).
* Jako zdroj synchronizace tempa pomocí MIDI clock a zpráv MIDI song position. Viz [MIDI clock](../tempo-synchronisation.md#midi-clock)
* Jako interaktivní vstup v node MIDI Notes pro vytváření efektů ve stylu „laserové harfy“. Viz [MIDI Notes](../clip-editor/operator-nodes/midi-notes.md)
* Jako obecnější vstupně-výstupní systém pomocí systému MIDI Send/Receive. Viz [MIDI Send/Receive](midi-send-receive.md)
