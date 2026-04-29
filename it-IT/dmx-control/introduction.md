---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introduzione

Liberation include un sistema DMX flessibile e potente che ti permette di creare effetti di illuminazione e controllare laser compatibili con DMX tramite Art-Net. È progettato per aiutarti a mantenere facilmente l’illuminazione sincronizzata con il tuo laser show, senza bisogno di una console luci separata.

{% hint style="info" %}
**Che cos’è Art-Net e che rapporto ha con DMX?**

**DMX** è un sistema usato da anni per controllare luci, laser, macchine del fumo e altri effetti scenici. Invia segnali di controllo su cavi dedicati, di solito con connettori XLR, e ogni fixture ascolta un insieme specifico di canali per sapere cosa deve fare.

**Art-Net** è un modo più recente per inviare gli stessi dati DMX su una normale rete informatica. Invece di usare cavi dedicati, invia tutto tramite Ethernet, proprio come il traffico internet o di rete locale.

In Liberation, tutto l’output DMX viene inviato usando Art-Net. Puoi usarlo per controllare direttamente dispositivi compatibili con Art-Net, oppure puoi collegare un **nodo Art-Net**: una piccola interfaccia che converte Art-Net di nuovo in DMX standard. Questo significa che puoi continuare a controllare luci ed effetti DMX tradizionali, anche se non supportano Art-Net direttamente.
{% endhint %}

Puoi usarlo anche per controllare molti altri tipi di attrezzatura scenica, come macchine del fumo, hazer, getti di CO₂, macchine per scintille fredde e altro ancora. Se supporta DMX, puoi configurarla come zona DMX e attivarla direttamente da Liberation, insieme ai tuoi contenuti laser.

Le fixture DMX vengono aggiunte come **zone DMX**, che compaiono nell’elenco delle zone insieme alle zone dei fasci laser e alle aree target del canvas. Ogni zona DMX usa un **preset DMX**, che indica a Liberation come mappare le proprietà dei tuoi clip laser, come posizione, colore e luminosità, sui valori dei canali DMX.

Quando invii un clip a una zona DMX, Liberation prende il primo elemento nel clip e ne converte le proprietà in base al preset. In questo modo puoi controllare luci ed effetti DMX direttamente dagli stessi clip che usi già per i laser.

#### Liberation a Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Il primo vero test del sistema DMX di Liberation è stato a Glastonbury 2023, dove Reach Lasers ha installato un totale di 90 sorgenti di fasci come parte del palco “spider” di Arcadia.

18 laser erano controllati con Ether Dreams interni, mentre altre 12 barre beam a 6 teste erano controllate tramite Art-Net e DMX.
