---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Crea effetti in stile “arpa laser”, in cui le note MIDI in ingresso attivano raggi o forme distribuiti su un intervallo. Il nodo usa qualunque contenuto gli passi come _sorgente_ per ogni nota: se gli invii un punto, otterrai una fila di punti. Se gli invii una forma come un cerchio, otterrai una fila di cerchi; anche le forme più complesse verranno replicate allo stesso modo.

Puoi scegliere l’interfaccia MIDI che Liberation deve ascoltare in **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – il canale MIDI da ascoltare (0 = tutti i canali, 1–16 = canale specifico)
* **width** – la larghezza totale su cui vengono distribuite le note.
* **MIDI note min / max** – i valori MIDI della nota più bassa e più alta dell’intervallo.
* **ignore out of range notes** – filtra tutte le note fuori dall’intervallo impostato. Se disattivato, le note fuori intervallo vengono "bloccate" sulla nota disponibile più vicina (le note alte attivano la parte superiore dell’intervallo, le note basse quella inferiore).
* **auto extend range** – amplia automaticamente l’intervallo se vengono suonate note al di fuori di esso.

{% hint style="info" %}
Non sai bene quale intervallo di note stai ricevendo? Attiva **auto extend range**, imposta **MIDI note min** molto alto e **MIDI note max** molto basso, poi suona tutte le note. Il sistema le rileverà tutte ed espanderà l’intervallo per te. Una volta acquisito tutto, disattiva **auto extend range** per bloccarlo.
{% endhint %}

* **leave all notes visible** – crea raggi o forme per tutte le note dell’intervallo, che stiano suonando o meno, ottenendo un effetto “arpa laser”.
* **hit colour** – il colore che appare quando una nota viene attivata.
* **hit colour hold time** – per quanto tempo il colore di hit resta alla massima luminosità prima di iniziare a sfumare. Il valore è in secondi (0–1). _100% = 1 secondo._
* **hit colour decay time** – quanto tempo impiega il colore di hit a sfumare dopo il tempo di hold. Il valore è in secondi (0–1). _100% = 1 secondo._

{% hint style="info" %}
Se il tuo contenuto è già bianco puro, impostare il colore di hit su bianco non farà alcuna differenza. Per ottenere i risultati migliori, usa un colore saturo per il contenuto e imposta il colore di hit su bianco: così ottieni un effetto flash molto piacevole quando le note vengono attivate.
{% endhint %}

* **note off fade out time** – quanto tempo impiega la nota a sfumare dopo essere stata rilasciata. Il valore è in secondi (0–1). _100% = 1 secondo._
* **hit scale factor** – di quanto la nota viene ingrandita quando viene attivata (ad es. 2 = dimensione doppia).
* **hit scale hold time** – per quanto tempo la nota resta ingrandita prima di tornare alle dimensioni originali. Il valore è in secondi (0–1). _100% = 1 secondo._
* **hit scale decay time** – quanto tempo impiega la nota a tornare alle dimensioni originali. Il valore è in secondi (0–1). _100% = 1 secondo._
* **note off shrink time** – quanto tempo impiega a ridursi alle dimensioni originali dopo che la nota è stata rilasciata. Il valore è in secondi (0–1). _100% = 1 secondo._ (Non ha effetto quando **leave all notes visible** è abilitato.)

{% hint style="info" %}
Ridimensionamento: tieni presente che, se il tuo contenuto è un singolo punto, il ridimensionamento non avrà alcun effetto.
{% endhint %}
