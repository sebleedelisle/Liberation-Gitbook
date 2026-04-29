---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / sincronizzazione

La sincronizzazione con la musica è un elemento fondamentale di Liberation: una volta allineati tempo e battiti alla musica, puoi essere sicuro che tutto resterà sincronizzato. Se hai la fortuna di ricevere un MIDI clock o Ableton Link, non devi preoccuparti affatto della sincronizzazione manuale. In caso contrario, nessun problema: puoi allinearti manualmente usando la funzione tempo _Live_.

Se hai esperienza con software musicali o per luci, questo processo ti sarà familiare. In caso contrario, vale la pena dedicare un po’ di tempo a prendere confidenza con il sistema e a fare pratica a casa prima di arrivare a uno show dal vivo.

## Pannello Tempo

Il pannello _Tempo_ è sempre visibile sullo schermo e contiene tutte le impostazioni di sincronizzazione. In alto trovi il contatore corrente di battuta/beat e un transport con i pulsanti play/pause e rewind/fastforward.

Sotto trovi il beat marker: quattro quadrati che “pulsano” a tempo. Questo _beat marker_ è una visualizzazione estremamente utile e lo consulterai continuamente quando usi il sistema di tempo _Live_.

### Impostare il tempo

Hai diverse opzioni per impostare il tempo:

* Clicca e trascina lo slider _Tempo_
* Shift-clicca e trascina lo slider _Tempo_ per modificare il tempo con incrementi di 0,1
* Fai doppio clic sullo slider _Tempo_ e digita manualmente il numero
* Usa la manopola _Tempo_ sull’APC40 (premi Shift per incrementi di 0,1)
* Tap Tempo

{% hint style="info" %}
Il tempo è definito in “beats per minute” e il valore predefinito tradizionale è di solito 120.
{% endhint %}

## Tap Tempo

Imposta automaticamente il tempo cliccando il pulsante _TAP_ a ritmo con il beat. Imposta l’inizio della battuta con il pulsante _RESET_.

{% hint style="info" %}
Il sistema Tap Tempo è abbastanza intelligente da capire se hai smesso di battere per un po’ o se hai saltato un paio di beat. Se inizi a battere in double time, capirà che vuoi raddoppiare il tempo; lo stesso vale se batti in half time.

È anche in grado di capire se ci sono due persone che stanno battendo il tempo contemporaneamente, ad esempio una sulla tastiera e una sull’APC40. Liberation calcolerà una media dei doppi tap.
{% endhint %}

#### Comandi da tastiera:

T - tap tempo\
R - resetta la battuta\
Y - arrotonda il tempo al beat per minute più vicino.

{% hint style="info" %}
Poiché oggi la maggior parte della musica viene creata digitalmente, è probabile che il tempo sia un numero intero arrotondato. Quindi, se il tempo battuto sembra vicino, usa il tasto Y oppure sposta la manopola tempo dell’APC40 di uno “scatto” per arrotondarlo a un numero intero.
{% endhint %}

#### Controlli APC40:

L’APC40 ha un pulsante _TAP TEMPO_ dedicato, oppure puoi usare anche un footswitch collegato per battere il tempo con il piede!

Usa la manopola _TEMPO_ per regolare. Premi _SHIFT_ mentre usi la manopola _TEMPO_ per regolazioni fini.

Usa il pulsante _METRONOME_ per **resettare la battuta**. Nota che anche il pulsante _METRONOME_ si illumina a tempo con il beat.

Ruota la manopola _TEMPO_ di uno “scatto” a destra o a sinistra per **arrotondare il tempo** verso l’alto o verso il basso a un valore intero di BPM.

Vedi anche [Riferimento APC40](reference/apc40-reference.md)

### Nudge tempo

Se sei sicuro di essere abbastanza vicino al tempo reale ma noti che stai andando fuori tempo, usa i pulsanti _NUDGE_ per correggere.

Se il tempo di Liberation sta andando avanti rispetto alla musica, tieni premuto _NUDGE -_ per rallentare temporaneamente finché non si riallinea.

Se il tempo di Liberation sta rimanendo indietro rispetto alla musica, tieni premuto _NUDGE +_ per accelerare temporaneamente finché non si riallinea.

{% hint style="info" %}
Puoi usare sia i pulsanti NUDGE sullo schermo sia i pulsanti dedicati sull’APC40.
{% endhint %}

### Half time / double time

Usa i pulsanti _÷2_ e _x2_ per dimezzare o raddoppiare il tempo in modo permanente. A differenza del tempo multiplier, questa è una modifica permanente del tempo corrente.

## Tempo Multiplier

Il sistema _Tempo Multiplier_ ti permette di modificare temporaneamente il tempo prima di tornare al valore precedente.

Attiva o disattiva _Tempo Multiplier_ premendo il pulsante _TEMPO MULTIPLIER_ o il pulsante _BANK_ sull’APC40. Regolalo usando lo slider sullo schermo oppure lo slider APC40 A-B. In alternativa, usa i pulsanti preset _25%, 50%, 100% 200%_.

## Sorgenti di tempo esterne

### MIDI Clock

Per sincronizzarti a un segnale MIDI clock esterno, seleziona il radio button _MIDI CLOCK_ e scegli il dispositivo MIDI dal menu a tendina. Nota la spia di stato colorata accanto ai menu a tendina:

* Verde - ricezione di un segnale MIDI clock
* Arancione - può connettersi al dispositivo MIDI, ma al momento non c’è alcun segnale di clock
* Rosso - impossibile connettersi al dispositivo MIDI

{% hint style="info" %}
MIDI Clock trasmette una serie di frame, 24 per quarto, ma nei messaggi non sono presenti dati di posizione. Questo significa che è utile per restare a tempo, ma potresti comunque dover resettare la battuta.

La sorgente tempo MIDI Clock di Liberation risponde anche ai messaggi **MIDI Machine Control (MMC)**, quindi se la tua sorgente clock li trasmette non dovrai resettare manualmente la battuta.
{% endhint %}



### Timeline

Ogni timeline ha il proprio tempo, che può essere un valore fisso oppure una _Tempo Map_. La _Tempo Map_ ti permette di modificare il tempo in momenti specifici all’interno della timeline.

Il tempo della timeline verrà usato quando _TIMELINE_ è selezionato come sorgente tempo.

{% hint style="info" %}
Puoi eseguire una timeline insieme a _qualsiasi_ sorgente tempo! Quindi, se hai una band dal vivo che non suona con un click, puoi avviare manualmente la timeline e mantenerla sincronizzata usando la sorgente tempo _LIVE_. Oppure, se hai un segnale MIDI clock, puoi usare quello!
{% endhint %}
