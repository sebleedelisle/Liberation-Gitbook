---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Nodi di stilizzazione

## &#x20;Randomise

Crea copie sparse degli elementi in ingresso usando un campo di rumore coerente. In altre parole, copia e sposta le tue forme e i tuoi punti in modo controllato e “rumoroso”. Invece di avere tutto ordinatamente fermo in un unico punto, ottieni più versioni che si spostano e si distribuiscono, come particelle che si muovono in un flusso.

* **count** – numero di copie per ogni elemento in ingresso (1–20). Con 1, ottieni una singola versione leggermente spostata di ogni elemento. Valori più alti creano più copie sparse.
* **noise offset** – scorre attraverso il campo di rumore (0–100%). Il ciclo è continuo, quindi animarlo con un Oscillator Node produce un movimento fluido e continuo di tutte le copie insieme.
* **noise jitter** – controlla la scala della texture del rumore. Valori più bassi producono variazioni ampie e morbide. Valori più alti producono posizionamenti più stretti e irregolari. Questo cambia il pattern, non l’intensità.
* **change between points** – controlla quanto ogni copia differisce dalla precedente. Valori bassi mantengono le copie raggruppate e simili. Valori alti le distribuiscono con una variazione maggiore.
* **face direction** – ruota ogni copia in modo che sia orientata nella direzione di movimento nel campo di rumore, producendo frecce/particelle allineate al flusso.
* **amount** – intensità complessiva dell’effetto (0–100%). Scala sia lo spostamento sia la rotazione generata da Face direction.

{% hint style="info" %}
Il nodo Randomise è alla base dell’effetto Randomise!
{% endhint %}

## &#x20;Trails

Crea echi del tuo contenuto, lasciando dietro all’originale copie che sfumano o cambiano scala mentre si muove.

* **change render profile for trail** – se attivo, tutte le copie della scia usano il **render profile** selezionato. _Vedi_ [Render profile](../fundamentals/render-profile.md "mention").
* **render profile** – il profilo da usare per le copie della scia quando l’interruttore sopra è attivo. Si usa spesso quando il contenuto principale è impostato su **DETAIL**, ma gli echi vengono renderizzati come **FAST**: in questo modo mantieni dettagli chiari sulle forme principali e renderizzi le scie in modo più efficiente.
* **delay** – imposta la distanza tra le copie della scia in tempo musicale, misurata in **passi da 1/64 di nota**.\
  Per riferimento:
  * 16 = 1/16 di battuta (semicroma)
  * 32 = 1/8 di battuta (croma)
  * 64 = 1/4 di battuta (semiminima)
  * 128 = 1/2 battuta (minima)
  * 256 = 1 battuta
* **trail size** – quante copie della scia disegnare dietro al contenuto live.
* **prefill trails** – riempie subito la cronologia delle scie quando il Clip inizia, invece di attendere che gli echi si accumulino durante i primi beat.
* **freeze trails** – trasforma scie fluide in una sequenza di istantanee congelate. Utile per creare effetti scia staccati e sincronizzati al beat.
* **brightness start / brightness end** – applica la luminosità lungo la scia, dalla copia più recente (**start**) a quella più vecchia (**end**). In genere, imposta **brightness start** a 100% e **brightness end** a 0% per far svanire gli echi.
* **scale start / scale end** – applica la scala lungo la scia, dalla copia più recente (start) a quella più vecchia (end). Per scie che si riducono fino a sparire, imposta **scale start** a 100% e **scale end** a 0%.

## &#x20;Shimmer

Aggiunge al tuo contenuto una variazione di luminosità scintillante, da un luccichio leggero fino a uno strobing intenso.

* **speed** – quanto rapidamente cambia lo shimmer nel tempo. Valori più alti producono uno sfarfallio più veloce; 0 mette in pausa l’effetto.
* **separation** – quanto i punti/elementi vicini differiscono tra loro.
  * 0: tutto scintilla insieme.
  * \>0: i punti vicini ricevono fasi progressivamente diverse, quindi lo shimmer varia lungo la forma.
  * <0: come sopra, ma la progressione di fase procede nel verso opposto.
* **threshold** – invece di sfumare in modo morbido, i punti ora lampeggiano completamente accesi o spenti in base alla loro luminosità. Gli elementi più luminosi si accendono più spesso, ma tieni presente che gli elementi al 100% di luminosità sono sempre accesi, mentre quelli allo 0% sono sempre spenti. Utile per effetti glitter o luce stellare più netti.

{% hint style="info" %}
Attivare **threshold** è una di quelle ottime funzioni nascoste che possono davvero dare vita alle particelle o al contenuto. Invece di sfumare, i punti vengono accesi e spenti rapidamente in base alla loro luminosità. Poiché in ogni momento vengono disegnati meno punti, il risultato è un output più luminoso e un’animazione più fluida.

Tieni però presente che, se il tuo contenuto è già al 100% di luminosità, non avrà alcun effetto!
{% endhint %}

* **use whole shape** – applica un unico valore di shimmer in modo uniforme all’intera forma. Quando è disattivato, il nodo suddivide le forme in modo che parti diverse possano scintillare indipendentemente, creando un aspetto puntinato.

## &#x20;Particles

È un effetto sperimentale che genera e anima particelle in base al tuo contenuto. Qualsiasi elemento basato su punti in ingresso viene trattato come posizione emettitore. Poiché i percorsi delle particelle sono pre-calcolati, se il contenuto in input cambia potresti dover aggiornare/ricalcolare le particelle per aggiornarle (basta cambiare una qualsiasi impostazione).

**General**

* **keep original** – se attivo, il contenuto originale viene mantenuto e le particelle vengono aggiunte sopra. Utile quando vuoi che i punti emettitori restino visibili.
* **number of particles** – quante particelle vengono create per ogni emissione. Valori più alti producono effetti più densi, valori più bassi effetti più minimali.
* **emission period** – l’intervallo del loop (in battute) durante il quale vengono emesse le particelle. Al 100% sono distribuite uniformemente lungo il loop; valori più piccoli le raggruppano in burst.
* **loop length** – quanto dura il loop delle particelle, misurato in battute musicali.
* **loop count** – quante volte il loop si ripete prima di resettarsi. Se impostato su 1, le particelle seguiranno sempre esattamente la stessa simulazione a ogni ciclo, rendendola perfettamente ripetibile. Valori più alti introducono più variazione prima che il ciclo si resetti.
* **delay** – sposta il tempo di inizio dell’emissione di un numero di note da 1/64, per effetti di timing.

**Motion**

* **speed** – quanto velocemente le particelle si allontanano dall’emettitore.
* **speed variation** – aggiunge casualità in modo che le particelle non si muovano tutte alla stessa velocità. Crea una distribuzione più naturale.
* **direction** – imposta la direzione di base in cui vengono lanciate le particelle, definita dagli **angoli x, y, z**. Questi angoli ruotano il vettore di emissione nello spazio 3D, quindi puoi puntare le particelle verso l’alto, di lato o in qualsiasi diagonale. Combinalo con **spread** per coni più ampi o burst più caotici.

{% hint style="info" %}
**Angoli di Eulero**\
Liberation usa gli **angoli di Eulero** per descrivere l’orientamento nello spazio 3D. Sono semplicemente rotazioni attorno ai tre assi principali:

* **X** – inclinazione avanti/indietro (come annuire con la testa)
* **Y** – rotazione sinistra/destra (come scuotere la testa per dire “no”)
* **Z** – rollio in senso orario/antiorario (come inclinare la testa di lato)

Regolando questi tre valori, puoi puntare le particelle in qualsiasi direzione.
{% endhint %}

* **direction variation** – aggiunge una dispersione casuale attorno a quella direzione. Utile per creare coni, spruzzi o esplosioni.
* **drag** – rallenta le particelle nel tempo. Valori più alti le fanno sembrare più pesanti e lente.
* **gravity** – tira le particelle verso il basso (positivo) o le spinge verso l’alto (negativo).
* **gravity variation** – aggiunge variazione alla gravità per ogni particella, rendendo il movimento più caotico.

**Life**

* **life duration** – quanto a lungo esistono le particelle (misurato in unità da 1/64 di nota). Con valori più brevi le particelle scompaiono rapidamente, mentre con valori più lunghi restano visibili più a lungo.
* **life variation** – aggiunge casualità alla durata delle particelle, così non scompaiono tutte insieme.
* **start delay / start delay variation** – ritarda il momento in cui ogni particella diventa visibile (in passi da 1/64 di nota). La particella è già generata e in movimento durante questo periodo, ma la sua luminosità resta a 0, quindi rimane invisibile finché il ritardo non termina. È utile se vuoi far apparire “scintille” di fuochi d’artificio in ritardo.

**Colour & brightness**

* **hue start** – colore iniziale delle particelle.
* **hue variation** – aggiunge casualità in modo che le particelle non partano tutte con lo stesso colore.
* **hue change** – sposta la tonalità lungo la vita della particella, creando scie che cambiano colore.
* **brightness start / brightness end** – applica la luminosità lungo la vita della particella. In genere, imposta brightness start alto e brightness end basso, così le particelle svaniscono in modo naturale.
* **brightness variation** – randomizza la luminosità iniziale per un aspetto più dinamico.
* **saturation start / saturation end** – imposta quanto è vivido il colore all’inizio e alla fine.
* **saturation variation** – randomizza la saturazione per creare variazione tra le particelle.

**Simulation**

* **time adjustment** – accelera o rallenta l’intera simulazione delle particelle. Utile per sincronizzarla a tempi diversi o per enfatizzare il movimento.
