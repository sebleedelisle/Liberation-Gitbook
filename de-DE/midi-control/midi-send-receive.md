---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Das MIDI Send/Receive-System ist von den APC40-Steuerungen getrennt und dient dazu, MIDI-Daten in Liberation hinein- und wieder herauszubekommen. Funktionen wie das Starten und Stoppen von Clips sowie das Anpassen globaler Einstellungen, Effekte und Clip-Parameter haben jeweils einen zugehörigen MIDI-Befehl.

{% hint style="info" %}
Das MIDI Send/Receive-System wurde ursprünglich entwickelt, bevor Liberation irgendeine Timeline-Funktionalität hatte. Es war ein Workaround, mit dem du eine Show in Musiksoftware wie Logic Pro oder Cubase aufnehmen und wiedergeben konntest.

Es gibt dir direkten Zugriff auf Clips, Effekte und Einstellungen, unabhängig von der Anzeige und der Scrollposition im Clip Deck. Systemischere Live-Steuerungsfunktionen wie Tap Tempo, das Zuweisen von Zonen und das Aktivieren/Deaktivieren sind nicht implementiert.
{% endhint %}

### MIDI Send/Receive-Einstellungen

Öffne das _MIDI Send/Receive_-Panel über das Menü _View -> MIDI Send/Receive_. Du siehst dort die Optionen _SEND, RECEIVE_ und _BOTH_ zum Senden und Empfangen sowie die Möglichkeit, auszuwählen, welche MIDI-Interfaces du verwenden möchtest.

{% hint style="danger" %}
Verwende die Einstellung _BOTH_ mit Vorsicht. MIDI-Geräte und Software können so konfiguriert sein, dass sie empfangene Daten wieder zurücksenden. Dadurch kann eine Feedback-Schleife aus MIDI-Daten entstehen, und das ist nicht gut!
{% endhint %}

### MIDI-Mapping

Siehe [Standardzuordnung für MIDI-Senden/-Empfangen](../reference/midi-send-receive-default-mapping.md "mention")

Ich plane, in Zukunft deutlich flexibleres MIDI-Mapping hinzuzufügen. Bis dahin kannst du Apps wie [BOME](https://www.bome.com/products/miditranslator) und [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) verwenden, um zwischen Liberation und deiner eigenen Hardware zu übersetzen.
