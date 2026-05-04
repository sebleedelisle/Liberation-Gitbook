---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Controller MIDI live

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **Controller APC40**

Questo è il controller hardware predefinito per Liberation; è fortemente consigliato e si può dire che Liberation sia stato progettato attorno a questo hardware fin dall’inizio. Non appena colleghi l’APC40, Liberation si connette automaticamente.

{% hint style="warning" %}
_Oh no! Mi si è scollegato il cavo USB a metà show!_

Niente panico: ricollegalo e Liberation si riconnetterà automaticamente, senza problemi.
{% endhint %}

### APC40 Mark 1 o Mark 2?

In breve, è consigliato il Mark 2 perché ha pulsanti a colori completi, che corrispondono meglio all’interfaccia Clip Deck di Liberation. La versione Mark 1 può andare bene in caso di necessità, ma risulterà un po’ più confusa: il layout è leggermente diverso da quello visualizzato a schermo e i pulsanti possono diventare solo rossi, arancioni o verdi, quindi non corrisponderanno ai colori delle Clip.

{% hint style="info" %}
L’APC40 Mark 1 originale è uscito nel 2009(!) e alcune persone lo preferiscono ancora per il corpo in metallo e per il formato robusto, simile a una console. Il Mark 2 aggiornato è uscito nel 2014 e, anche se è stato dismesso nel 2024, tornerà in produzione nel 2025 grazie alla richiesta di visual artist (Resolume ecc.) e laserist.
{% endhint %}

Per l’elenco completo dei controlli disponibili sull’APC40, vedi [Riferimento APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 include anche un profilo per APC Mini. Mappa la griglia Clips 8x5, i pulsanti delle zone, i controlli di inversione X/Y delle zone, i pulsanti dei gruppi, l’arresto di tutti i Clips, lo spostamento tra le pagine dei Clips, lo spostamento tra le pagine delle zone, tap tempo, reset della battuta e regolazione fine del tempo. I suoi fader controllano i livelli degli effetti, mentre i fader con shift controllano i parametri degli effetti. L’ultimo fader controlla la luminosità globale.

### MIDI Fighter Twister

Il profilo MIDI Fighter Twister è pensato per un controllo basato soprattutto sugli encoder, più che per l’avvio dei Clips. Una fila di encoder controlla il parametro 1 per gli slot effetti 1-8, mentre un’altra fila segue gli otto controlli contestuali del pannello Parameters, inclusi lo shift dei Clip, il ritardo delle zone, spin/scale globali e le dissolvenze dei gruppi.
