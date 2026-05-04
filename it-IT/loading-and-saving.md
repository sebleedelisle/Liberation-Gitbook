---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Caricamento e salvataggio

Liberation salva costantemente il proprio stato su disco, così puoi essere sicuro che, in caso di blackout o problema di sistema, si riavvierà esattamente dal punto in cui era rimasto. Non dovresti mai perdere le tue zone, la timeline o altri contenuti.

Puoi comunque esportare la tua configurazione per crearne un backup o trasferirla su un altro computer.

### Importazione/esportazione del progetto

Il file di progetto salva quasi tutto ciò che è presente nella configurazione corrente, tra cui:

* Tutto ciò che è descritto in [Caricamento e salvataggio](loading-and-saving.md#laser-settings-import-export "mention") più sotto
* Clip, effetti e impostazioni dei gruppi
* Tutte le tue timeline (esclusi i media audio e video)
* Configurazione Art-Net
* Impostazioni di invio/ricezione MIDI
* Impostazioni di tempo/sincronizzazione

Al momento non salva e carica:

* Impostazioni di ingresso audio e MIDI usate nel node MIDI notes e nel Sound Input Oscillator (_salva_ invece le impostazioni di invio/ricezione MIDI e l’ingresso audio per il timecode)
* Ridimensionamento dell’interfaccia
* Media per le immagini guida di Canvas
* Media audio e video per le timeline
* Font usati nel nodo Text

{% hint style="danger" %}
I file audio e video nella timeline non vengono salvati con i file di progetto, quindi assicurati di salvarli separatamente se vuoi trasferirli su un altro computer. Vedi [Caricamento e salvataggio](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Importazione/esportazione delle impostazioni laser

* Impostazioni laser per ogni laser
* Zone del fascio
* Aree target di Canvas
* Zone DMX
* Assegnazione dei controller laser (e alias per eventuali controller che hai rinominato)
* Impostazioni e preset di calibrazione scanner e colore del laser
* Impostazioni e preset del 3D Visualiser

### Importazione/esportazione del Clip Deck

* Tutte le Clip e le relative assegnazioni di zona, impostazioni e parametri
* Tutte le impostazioni dei gruppi, flash mode, tempi di fade in/out ecc.

Al momento non salva e carica:

* Tutti gli effetti con i relativi parametri e impostazioni

{% hint style="info" %}
**Caricare le Clip da un file di progetto senza caricare l’intero progetto**

Per importare solo le Clip da un progetto, seleziona _**Clips->Import Clip Deck**_ e, invece di scegliere un file Clip Deck (.cpdk), scegli un file di progetto.
{% endhint %}

### Append Clip Deck

Puoi aggiungere Clip da un file Clip Deck esportato al progetto corrente usando _Append Clip Deck_. Le Clip vengono aggiunte alla fine del Clip Deck corrente, ma gli effetti e le impostazioni dei gruppi presenti nel file non vengono importati.

### Export Selected Clips

Tutte le Clip attualmente selezionate verranno esportate in un file. Le impostazioni dei gruppi e gli effetti non verranno salvati, ma solo le Clip. Nota che le Clip attive in esecuzione non vengono esportate, a meno che non siano anche selezionate.

{% hint style="info" %}
Fai Option/Alt - shift - clic sulle Clip per selezionarle (oppure usa il lazo). Puoi riconoscere le Clip selezionate dal bordo bianco spesso intorno a esse. Vedi [Avviare / fermare le clip](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Importazione/esportazione degli effetti

Carica e salva tutti gli effetti insieme alle relative impostazioni di gruppo e ai parametri.

{% hint style="info" %}
**Caricare gli effetti da un file di progetto senza caricare l’intero progetto**

Per importare solo gli effetti da un progetto, seleziona _**Effects->Import Effects**_ e, invece di scegliere un file effetti (.efts), scegli un file di progetto.
{% endhint %}

### Esportazione della timeline

Esporta un file timeline con una o più timeline. Nota che il Clip Deck è sempre incluso nei file timeline esportati (anche se puoi scegliere in modo selettivo quali Clip reimportare; vedi [Caricamento e salvataggio](loading-and-saving.md#timeline-import "mention") più sotto).

Se nel file di progetto è presente più di una timeline, si aprirà un pannello che ti permette di selezionare quali timeline vuoi esportare.

{% hint style="danger" %}
I file audio e video nella timeline non vengono salvati con i file timeline, quindi assicurati di salvarli separatamente se vuoi trasferire i contenuti su un altro computer. Vedi [Caricamento e salvataggio](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Importazione della timeline

Importa una o più timeline da un singolo file timeline. Dopo aver selezionato il file timeline, si aprirà un pannello con diverse opzioni di importazione.

Se il file timeline contiene più di una timeline, verranno elencate tutte. Seleziona quelle che vuoi includere.

* Replace existing timelines\
  Elimina tutte le timeline correnti e le sostituisce con quelle importate
* Import used clips only\
  Importa solo le Clip utilizzate e le dispone in gruppi, uno per ogni timeline. Se questa opzione non è selezionata, l’intero Clip Deck del file timeline verrà aggiunto alle Clip esistenti.
* Replace existing clip deck\
  Sostituisce il Clip Deck corrente con le Clip presenti nel file timeline. Disponibile solo se _Replace existing timelines_ è selezionato.

{% hint style="info" %}
**Caricare timeline da un file di progetto senza caricare l’intero progetto**

Per importare solo le timeline da un progetto, seleziona _**Timeline->Import Timeline(s)**_ e, invece di scegliere un file timeline (.ltml), scegli un file di progetto.
{% endhint %}

### Importazione/esportazione DMX / Art-Net

Salva e carica i nodi Art-Net insieme ai relativi indirizzi IP. Include anche le zone DMX e tutti i tuoi preset DMX.

### Nota importante sui file media della timeline

I file audio e video **non vengono** attualmente esportati con il file timeline, quindi, se devi spostare i contenuti su un altro computer, assicurati di includerli.

{% hint style="info" %}
**Come una timeline cerca i file media**

Quando la timeline viene caricata, cerca nella stessa cartella del file timeline (o del progetto) e anche all’interno di eventuali sottocartelle. Quindi, finché i file si trovano nella stessa cartella o in una sottocartella (ad esempio _/videos_ o _/sound_), verranno trovati durante il caricamento.
{% endhint %}
