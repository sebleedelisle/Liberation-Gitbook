---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Обзор управления MIDI

Liberation использует MIDI несколькими способами:

* Как контроллер для живого управления. APC40 Mk1/Mk2, APC Mini и MIDI Fighter Twister могут подключаться автоматически, когда доступно соответствующее устройство. См. [Живое управление с MIDI-контроллерами](live-control-with-the-apc40.md "mention").
* Как источник синхронизации clock, используя сообщения MIDI clock и MIDI song position. См. [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Как интерактивный вход на node MIDI notes для создания эффектов в стиле «лазерной арфы». См. [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Как более универсальную систему ввода/вывода через MIDI Send/Receive. См. [MIDI Send/Receive](midi-send-receive.md "mention")

Поддерживаемые контроллеры для живого управления следуют состоянию, отображаемому на экране Liberation: кнопки Clip подсвечиваются цветами своих групп, кнопки zone показывают состояние zone, а назначенные ручки или энкодеры соответствуют текущему эффекту или элементам управления панели Parameters.
