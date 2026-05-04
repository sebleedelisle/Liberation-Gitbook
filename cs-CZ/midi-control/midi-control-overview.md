---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Přehled ovládání přes MIDI

Liberation využívá MIDI několika způsoby:

* Jako ovladač pro živé ovládání. APC40 Mk1/Mk2, APC Mini a MIDI Fighter Twister se mohou připojit automaticky, pokud je dostupné odpovídající zařízení. Viz [Živé MIDI controllery](live-control-with-the-apc40.md "mention").
* Jako zdroj synchronizace tempa pomocí MIDI clock a zpráv MIDI song position. Viz [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Jako interaktivní vstup v node MIDI Notes pro vytváření efektů ve stylu „laserové harfy“. Viz [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Jako obecnější vstupně-výstupní systém pomocí systému MIDI Send/Receive. Viz [MIDI Send/Receive](midi-send-receive.md "mention")

Podporované controllery pro živé ovládání sledují stav zobrazený v Liberation na obrazovce: tlačítka Clip svítí barvami svých skupin, tlačítka zone zobrazují stav zone a namapované knoby nebo enkodéry sledují aktuální efekt nebo ovládací prvky v panelu Parameters.
