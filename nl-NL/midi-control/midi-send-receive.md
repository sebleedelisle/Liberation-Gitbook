---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI verzenden/ontvangen

Het MIDI Send/Receive-systeem staat los van de APC40-bediening en is een manier om MIDI-data in en uit Liberation te krijgen. Functies zoals clips starten en stoppen, globale instellingen aanpassen, effecten wijzigen en clipparameters bedienen hebben allemaal een bijbehorende MIDI-command.

{% hint style="info" %}
Het MIDI Send/Receive-systeem is oorspronkelijk gebouwd voordat Liberation Timeline-functionaliteit had. Het was een workaround waarmee je een show kon opnemen en afspelen in muzieksoftware zoals Logic Pro of Cubase.

Het geeft je directe controle over clips, effecten en instellingen, ongeacht de weergave en de scrollpositie van het clip deck. Meer systemische live-bedieningsmogelijkheden zoals tap tempo, zones toewijzen en arming/disarming zijn niet geïmplementeerd.
{% endhint %}

### MIDI Send/Receive-instellingen

Open het _MIDI Send/Receive_-paneel (via het menu _View -> MIDI Send/Receive_). Je ziet dat je kunt kiezen tussen _SEND, RECEIVE,_ of _BOTH_ voor verzenden en ontvangen, en dat je kunt selecteren welke MIDI-interfaces je wilt gebruiken.

{% hint style="danger" %}
Gebruik de instelling _BOTH_ met voorzichtigheid. MIDI-apparaten en software kunnen zo worden geconfigureerd dat ze ontvangen data weer terugsturen. Dit kan een feedbackloop van MIDI-data veroorzaken, en dat is niet goed!
{% endhint %}

### MIDI-mapping

Zie [Standaard MIDI-mapping voor verzenden/ontvangen](../reference/midi-send-receive-default-mapping.md "mention")

Ik ben van plan om in de toekomst veel meer aanpasbare MIDI-mapping toe te voegen, maar tot die tijd kun je apps zoals [BOME](https://www.bome.com/products/miditranslator) en [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) gebruiken om te vertalen tussen Liberation en je eigen hardware.
