---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Przegląd sterowania MIDI

Liberation korzysta z MIDI na kilka sposobów:

* Jako kontroler live. APC40 Mk1/Mk2, APC Mini i MIDI Fighter Twister mogą łączyć się automatycznie, gdy dostępne jest pasujące urządzenie. Zobacz [Kontrolery MIDI do pracy na żywo](live-control-with-the-apc40.md "mention").
* Jako źródło synchronizacji zegara, z użyciem komunikatów MIDI clock i MIDI song position. Zobacz [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Jako interaktywne wejście w node MIDI notes do tworzenia efektów w stylu „laser harp”. Zobacz [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Jako bardziej ogólny system wejścia/wyjścia z użyciem systemu MIDI Send/Receive. Zobacz [MIDI Send/Receive](midi-send-receive.md "mention")

Obsługiwane kontrolery live podążają za stanem widocznym na ekranie w Liberation: przyciski Clip świecą kolorami swoich grup, przyciski zone pokazują stan zone, a przypisane pokrętła lub enkodery podążają za bieżącym efektem albo kontrolkami w panelu Parameters.
