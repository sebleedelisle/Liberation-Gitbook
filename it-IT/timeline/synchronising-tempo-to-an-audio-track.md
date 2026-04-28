---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Sincronizzare il tempo con una traccia audio

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchronising tempo to an audio track" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

La timeline di Liberation è progettata per lavorare con tempi fissi o variabili, ma una sincronizzazione affidabile parte sempre dall’individuare il tempo e allineare correttamente l’audio. Questa sezione descrive il flusso di lavoro consigliato.

#### 1. Allinea il primo downbeat

Aggiungi la tua traccia audio alla timeline e assicurati che sia agganciata a un beat, in modo che il **primo downbeat musicale** della traccia sia allineato esattamente con l’inizio di una battuta.

Questo passaggio è fondamentale.

Se l’audio non inizia naturalmente su un downbeat, hai due opzioni:

* **Regola il ritardo della clip**\
  Fai clic destro sulla clip audio e regola il valore Delay finché il primo downbeat non si allinea con un marker di beat o di battuta.
* **Taglia l’audio esternamente**\
  Modifica il file audio in un editor esterno, ad esempio Audacity, in modo che il file inizi esattamente sul primo downbeat, quindi importalo di nuovo.

{% hint style="info" %}
**Importante:**\
Se l’inizio dell’audio non è allineato a un beat o a una battuta, la posizione di inizio percepita della musica si sposterà avanti e indietro quando cambi il tempo. Questo rende molto difficile ottenere una corrispondenza precisa del tempo.
{% endhint %}

#### 2. Imposta un tempo iniziale

Se hai un’idea approssimativa dei BPM, inseriscila nel controllo del tempo della timeline e avvia la riproduzione dall’inizio.

Osserva con attenzione i marker di beat e di battuta mentre la traccia viene riprodotta.

* Se i marker vanno avanti rispetto alla musica, riduci leggermente il tempo.
* Se rimangono indietro, aumenta leggermente il tempo.
* Interrompi la riproduzione, regola il tempo e riprova.

Per la maggior parte della musica moderna, il tempo è un BPM intero e fisso. Una volta trovato il valore corretto, dovrebbe rimanere sincronizzato per l’intera traccia.

#### 3. Usa la forma d’onda come riferimento visivo

La forma d’onda audio è un riferimento utile quando devi far corrispondere il tempo.

* Transienti e picchi dovrebbero allinearsi con i marker verticali di battuta.
* Ingrandisci molto la vista per controllare l’allineamento su più battute.

**Suggerimento:**\
Usa la rotellina del mouse o il gesto sul trackpad per fare zoom sulla timeline. Usa la rotellina orizzontale o il gesto corrispondente per spostarti a sinistra e a destra. Lavorare con lo zoom ravvicinato rende molto più semplici le piccole regolazioni.

#### 4. Tracce con BPM non interi

Se la traccia non usa un BPM intero, lo slittamento sarà più graduale.

* Ingrandisci ulteriormente.
* Usa regolazioni del tempo più piccole.
* Controlla l’allineamento su sezioni più lunghe della traccia, non solo sulle prime battute.

#### 5. Musica con cambi di tempo

Se la musica accelera o rallenta, usa la Tempo Map:

* Riproduci la traccia e osserva i marker di beat.
* Quando lo slittamento diventa evidente, aggiungi un cambio di tempo in quel punto.
* Regola il tempo per la nuova sezione finché non si sincronizza di nuovo.

Ripeti questo processo per ogni cambio di tempo nella musica.

#### 6. Analisi esterna del tempo (opzionale)

Come ultima risorsa, puoi analizzare la traccia in una DAW come Logic Pro e generare automaticamente una mappa del tempo. Tieni presente che spesso questo produce un gran numero di cambi di tempo, a volte uno per battuta, che potrebbero essere più dettagliati del necessario per la maggior parte degli show.
