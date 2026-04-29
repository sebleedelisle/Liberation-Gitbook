---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Обзор управления MIDI

Liberation использует MIDI несколькими способами:

* Как контроллер для живого управления, с APC40. См. [Управление в реальном времени с APC40](live-control-with-the-apc40.md).
* Как источник синхронизации clock, используя сообщения MIDI clock и MIDI song position. См. [MIDI clock](../tempo-synchronisation.md#midi-clock)
* Как интерактивный вход на node MIDI notes для создания эффектов в стиле «лазерной арфы». См. [MIDI notes](../clip-editor/operator-nodes/midi-notes.md)
* Как более универсальную систему ввода/вывода через MIDI Send/Receive. См. [MIDI Send/Receive](midi-send-receive.md)
