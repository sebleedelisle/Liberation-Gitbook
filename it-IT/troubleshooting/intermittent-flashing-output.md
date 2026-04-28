---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Output intermittente / lampeggiante

Apri il pannello _Laser Overview_ e controlla la spia di connessione accanto al laser con cui hai problemi.

**Se la spia di connessione NON è costantemente verde:**\
allora probabilmente hai un problema di rete o di prestazioni della CPU:

**Prestazioni di rete -**

* Assicurati di non essere connesso a una rete Wi-Fi. Dovresti sempre usare una connessione cablata. Assicurati che il sistema operativo dia priorità alla rete cablata rispetto al Wi-Fi oppure disattiva il Wi-Fi se non ne sei sicuro.
* Controlla l’adattatore di rete e prova un adattatore USB-C diverso.
* Utenti Windows: controlla / aggiorna i driver di rete ed esegui gli strumenti di test di rete appropriati.
* Controlla tutti i cavi, switch e router. Sostituisci e testa ogni cavo in modo metodico.
* Riavvia tutta l’attrezzatura di rete, inclusi switch, router e ogni Ether Dream.

**Prestazioni CPU**

Se hai un computer vecchio o con specifiche basse, potrebbe essere troppo lento per eseguire Liberation. Controlla l’indicatore del frame rate sul lato destro della barra delle icone.

Lì ci sono due numeri: il frame rate effettivo e il frame rate target. Se il frame rate effettivo scende sotto 30, potresti avere problemi.

Le seguenti azioni possono aiutare:

* Rimuovi i laser inutilizzati, ad esempio se hai un solo laser collegato, elimina gli altri.
* Passa alla vista output o canvas.
* Chiudi tutti gli altri programmi, controlla le impostazioni del firewall di rete, chiudi antivirus, Dropbox, ecc.
* Riduci la risoluzione dello schermo e rimpicciolisci la finestra di Liberation.

Se nulla di tutto questo funziona, valuta l’upgrade del computer.

***

**Se la spia di connessione È costantemente verde:**

allora è probabile che si tratti di un problema hardware. Questo argomento non rientra nello scopo di questo manuale, ma puoi provare le seguenti azioni:

* Disattiva il sistema SFS (Scan Fail Safety). Alcuni laser hanno una funzione che disattiva l’output se gli scanner smettono di muoversi, ad esempio producendo un fascio statico intenso. A volte possono essere un po’ troppo prudenti / inaffidabili.

{% hint style="danger" %}
Usa la massima cautela quando disattivi il sistema scan fail safety. I fasci statici intensi possono causare bruciature! Assicurati di avere a portata di mano un pulsante di arresto e un estintore.
{% endhint %}

* Controlla i cavi e i sistemi di interlock.
* Controlla tutti i cablaggi tra il controller e il laser.

Un [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) può essere uno strumento prezioso per diagnosticare problemi con i laser.
