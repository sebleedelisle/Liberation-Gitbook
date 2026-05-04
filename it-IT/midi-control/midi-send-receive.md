---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Il sistema MIDI Send/Receive è separato dai controlli APC40 ed è un modo per far entrare e uscire dati MIDI da Liberation. Funzioni come avviare e fermare clip, regolare impostazioni globali, effetti e parametri delle clip hanno tutte un comando MIDI associato.

{% hint style="info" %}
Il sistema MIDI Send/Receive è stato creato inizialmente prima che Liberation avesse qualsiasi funzionalità Timeline; era una soluzione alternativa che potevi usare per registrare e riprodurre uno show in software musicali come Logic Pro o Cubase.

Ti offre un controllo diretto su clip, effetti e impostazioni, indipendentemente dalla visualizzazione e dalla posizione di scorrimento del clip deck. Funzionalità più sistemiche per il controllo live, come tap tempo, assegnazione delle zone e arm/disarm, non sono implementate.
{% endhint %}

### Impostazioni MIDI Send/Receive

Apri il pannello _MIDI Send/Receive_ (dal menu _View -> MIDI Send/Receive_). Noterai che puoi scegliere tra _SEND, RECEIVE,_ o _BOTH_ per inviare e ricevere, oltre a selezionare quali interfacce MIDI vuoi usare.

{% hint style="danger" %}
Usa l’impostazione _BOTH_ con cautela. Dispositivi e software MIDI possono essere configurati per rimandare indietro i dati che ricevono; questo potrebbe causare un loop di feedback di dati MIDI, e non va bene!
{% endhint %}

### Mappatura MIDI

Vedi [Mappatura predefinita MIDI di invio/ricezione](../reference/midi-send-receive-default-mapping.md "mention")

In futuro ho in programma di aggiungere una mappatura MIDI molto più personalizzabile, ma nel frattempo puoi usare app come [BOME](https://www.bome.com/products/miditranslator) e [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) per tradurre i messaggi tra Liberation e il tuo hardware personalizzato.
