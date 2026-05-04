---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Assegnazione dei controller

Dopo aver configurato i laser in Liberation, puoi assegnare ciascuno di essi a un controller laser nel mondo reale. Consulta [Laser e controller compatibili (DAC)](../hardware/compatible-lasers-and-controllers-dacs.md "mention") per verificare quale hardware puoi usare. I controller saranno collegati tramite USB oppure tramite rete.

* Apri il pannello _Controller Assignment_ dal menu _View -> Controller Assignment_. In alternativa puoi usare il pulsante _ASSIGN LASER CONTROLLERS_ nel pannello _Laser Overview_.

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Pannello Controller Assignment"><figcaption></figcaption></figure>

* Il pannello è diviso in due: a sinistra trovi l’elenco dei laser, a destra l’elenco dei controller disponibili. Se non vedi il tuo controller laser nell’elenco, premi il pulsante _REFRESH_. Se continui ad avere problemi, consulta [Risoluzione dei problemi](../troubleshooting/ "mention").
* Per assegnare un controller a un laser, fai clic e trascinalo da destra su uno slot laser libero a sinistra. In questo modo indichi a Liberation quale controller deve usare per quale laser. Se cambi idea, puoi trascinare liberamente i controller su e giù da un laser all’altro.

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Elenco dei controller" width="375"><figcaption></figcaption></figure>

* Se vedi un quadrato verde accanto al controller, significa che Liberation si è collegato correttamente.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Un Ether Dream e un Helios DAC assegnati rispettivamente ai laser 2 e 3</p></figcaption></figure>

{% hint style="info" %}
Tieni presente che ogni volta che ti colleghi a un controller, il laser verrà automaticamente disarmato.
{% endhint %}

* Un quadrato arancione 🟧 indica che il controller ha problemi di connessione intermittenti. Di solito dipende da un problema di rete; consulta [Risoluzione dei problemi](../troubleshooting/ "mention").
* Un quadrato rosso 🟥 indica che il controller non è raggiungibile; consulta [Risoluzione dei problemi](../troubleshooting/ "mention").
* Il _pulsante di disconnessione_ (X) disconnette il controller, ma non lo rimuove dall’assegnazione al laser. Puoi quindi usare il _pulsante di riconnessione_ (icona con freccia di aggiornamento) per ricollegarlo, oppure fare di nuovo clic sul _pulsante di disconnessione_ per cancellare l’assegnazione.
* _Funzione avanzata:_ apri il pannello di analisi del controller facendo clic sul pulsante con l’icona simile a un grafico. Questa è una funzione avanzata che fornisce informazioni dettagliate sul flusso di dati e può aiutarti a diagnosticare i problemi. Questa opzione potrebbe non essere disponibile per alcuni tipi di controller.
* Puoi usare il _pulsante di rinomina_ (matita) per rinominare questo controller come preferisci. È utile scegliere un nome che renda facile associarlo a un hardware specifico. Se è integrato in un laser, puoi chiamarlo di conseguenza, ad esempio _LaserCube Ultra #1_ o _Triton T5 #3._ Questi nomi verranno salvati nella tua installazione di Liberation e compariranno d’ora in poi; possono essere molto utili per identificare rapidamente i tuoi laser.

{% hint style="info" %}
Suggerimento - fai **doppio clic** su un controller a destra per assegnarlo automaticamente al primo laser disponibile a sinistra. Può farti risparmiare davvero tempo se hai molti laser da assegnare!
{% endhint %}

Puoi usare i pulsanti _DISCONNECT ALL_ e _RECONNECT ALL_ per reimpostare rapidamente tutte le connessioni. È utile se stai avendo problemi di rete.
