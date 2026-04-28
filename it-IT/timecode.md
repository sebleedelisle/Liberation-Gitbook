---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation supporta la sincronizzazione con un segnale timecode SMPTE/LTC esterno, comunemente usato negli spettacoli musicali dal vivo per mantenere sincronizzati luci, effetti pirotecnici, video e backing track.

{% hint style="info" %}
Che cos'è SMPTE/LTC?

SMPTE è uno standard per il timecode, mentre LTC è questo timecode convertito in un segnale audio. Se ascolti questo audio, sembra un terribile fischio acuto, ma per i computer è un'informazione di timing ad alta risoluzione.

**Curiosità da nerd!**

Storicamente SMPTE è stato usato per mantenere sincronizzati video e audio oppure, nel caso della sincronizzazione con nastro analogico, una traccia veniva registrata con l'audio del timecode, pratica a volte chiamata "striping" del nastro. Questa traccia di timecode poteva essere usata per mantenere sincronizzati più registratori a nastro tra loro, oppure per tenere un sequencer MIDI sincronizzato con il nastro. (Così non dovevi registrare gli strumenti MIDI su nastro: potevi semplicemente farli suonare dal sequencer in tempo reale mentre mixavi!)

SMPTE significa Society of Motion Picture and Television Engineers, l'organizzazione che ha definito lo standard. LTC significa _Linear TimeCode._
{% endhint %}

Puoi ricevere un segnale timecode LTC tramite qualsiasi interfaccia audio collegata al computer, ma è consigliato usare un'interfaccia professionale con almeno un ingresso XLR regolabile e funzionalità di monitoraggio.

Ho avuto una buona esperienza con la [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), perché ha il monitoraggio in cuffia, 2 ingressi XLR e non richiede driver speciali (almeno su macOS). Se pensi di usarla solo per il timecode, puoi scegliere la leggermente più economica [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (che ha un solo ingresso e non ha MIDI), ma in realtà qualsiasi interfaccia audio di qualità discreta dovrebbe funzionare.

{% hint style="info" %}
I segnali timecode LTC sono in genere distribuiti tramite cavi XLR bilanciati, perché sono abbastanza robusti da trasmettere segnali audio a basso livello su lunghe distanze. (XLR è il connettore cilindrico solitamente usato con i microfoni)
{% endhint %}

### Connessioni hardware

Collega il cavo XLR del segnale timecode alla tua interfaccia audio e assicurati di ricevere un buon segnale. Regola il livello sull'interfaccia audio finché il segnale è forte ma non va in clipping. Se la tua interfaccia audio ha un'uscita cuffie, puoi ascoltare il timecode e verificare che non abbia glitch e che non ci sia troppo rumore.

{% hint style="info" %}
In teoria è possibile ricevere il segnale tramite la presa jack del tuo MacBook, ma servirebbe un cavo personalizzato. Questi jack sono in genere mini jack TRRS a 4 poli e, sinceramente, non sono sicuro di quali contatti possano essere usati come ingresso audio, né di quale livello di tensione possano gestire (ho letto da qualche parte che fosse +/-1V, ma usalo a tuo rischio!)

Penso che sia meglio procurarti una semplice interfaccia audio USB economica piuttosto che tentare questa strada.
{% endhint %}

Se la tua interfaccia audio non ha alcun tipo di monitoraggio dell'ingresso, puoi controllare nelle impostazioni di sistema di macOS (sotto _Sound_) per assicurarti di ricevere un segnale. (Su Windows, usa il _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS mostra il livello di ingresso di qualsiasi interfaccia audio nel pannello delle impostazioni di sistema Sound</p></figcaption></figure>

### Configurazione in Liberation

1. Seleziona la tua interfaccia audio e il canale di ingresso corretto nella finestra delle impostazioni Timecode.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Nota che nel menu a discesa ci sono opzioni separate per ogni canale di ingresso della tua interfaccia audio

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Osserva il quadrato a sinistra: se stai ricevendo un segnale timecode valido, diventerà verde. In caso contrario sarà rosso.

2. Seleziona il framerate corretto per il timecode in ingresso. Chi ti fornisce il timecode dovrebbe saperti dire qual è il frame rate. (Se lo imposti in modo errato, la sincronizzazione funzionerà comunque, ma noterai un piccolo "salto" ogni secondo)
3. Apri le impostazioni timecode della Timeline usando la piccola icona a forma di orologio sulla barra della timeline e scegli l'opzione SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Regola lo start offset (in ore, minuti, secondi, frame) in modo che corrisponda all'inizio del brano. Se hai più timeline, dovrai impostare queste opzioni separatamente per ciascuna.

{% hint style="info" %}
Nel mondo dei tour è una convenzione comune far iniziare ogni brano a un'ora diversa, ad esempio 01:00:00:00 per il primo brano, 02:00:00:00 per il secondo e così via.

Liberation passerà automaticamente alla timeline in base al timecode, quindi durante uno show non dovrai mai cambiare timeline manualmente.
{% endhint %}

Nota che, a differenza di MIDI Clock e Ableton Link, SMPTE è un sistema di tempo _assoluto_, misurato in ore, minuti, secondi e frame. Il sistema di tempo principale di Liberation è basato su beat e battute, quindi quando ricevi il timecode userà il tempo impostato nella timeline. Dovrai assicurarti che questo tempo sia sincronizzato con la musica eventualmente sincronizzata allo stesso timecode.
