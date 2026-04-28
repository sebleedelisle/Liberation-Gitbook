---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Panoramica di Canvas

Il sistema Canvas di Liberation è relativamente semplice, ma all’inizio può creare un po’ di confusione. Ecco una panoramica concettuale per iniziare.

{% hint style="info" %}
**Aspetta, mi serve davvero il sistema Canvas?**

Forse no! Se devi solo proiettare una singola grafica su un singolo laser, puoi farlo facilmente con una beam zone (anche se, per impostazione predefinita, il contenuto della beam zone viene ribaltato orizzontalmente, quindi dovrai applicare X flip alla clip).

Ma se vuoi distribuire contenuti grafici su più di un laser, oppure dividerli in sezioni diverse da mappare su elementi architettonici, allora il sistema Canvas fa al caso tuo!
{% endhint %}

### Canvas

Prima di tutto, c’è il Canvas vero e proprio. È ciò che vedi nella vista _CANVAS_ e rappresenta un grande, beh, canvas, all’interno del quale puoi disegnare contenuti in qualsiasi punto.

### Aree target del Canvas

Sono mostrate come rettangoli con contorno blu nella vista Canvas e sono le aree a cui puoi inviare contenuti. Invii il contenuto di una clip a un’area target del Canvas nello stesso modo in cui invieresti una clip a una beam zone. Nel Clip Deck vedrai i pulsanti delle aree target del Canvas a destra dei pulsanti delle beam zone.

{% hint style="info" %}
Se non vedi i pulsanti Canvas nel Clip Deck, prova a scorrere i pulsanti delle beam zone con `Shift + Left / Right Arrow`. Dovresti vedere un pulsante per ogni area target del Canvas etichettato _CANVAS 1, CANVAS 2_ ecc.
{% endhint %}

### Zone Canvas

Le zone Canvas sono aree all’interno del Canvas che scegli di inviare a un laser. Sono rappresentate come rettangoli con contorno rosa nella vista Canvas. Puoi fare clic destro su ogni zona e selezionare i laser a cui vuoi assegnarla. Se ora passi alla vista _OUTPUT_ per quel laser, vedrai che è comparsa una nuova zona.

{% hint style="danger" %}
ATTENZIONE: se il laser è armato, potresti iniziare improvvisamente a proiettare contenuti in una zona Canvas predefinita. È meglio disarmare il laser prima di assegnargli zone Canvas.
{% endhint %}

{% hint style="info" %}
Puoi anche assegnare una zona Canvas a un laser facendo clic sul pulsante _add canvas zone_ nella vista _OUTPUT_. Vedi [zones.md](../output-view/zones.md).
{% endhint %}

### Immagini guida

Puoi aggiungere un’immagine guida nel Canvas e usarla come modello per le tue grafiche. È consigliabile regolare la tinta del colore sull’immagine guida (menu con clic destro) e scurirla, così da vedere più facilmente i contenuti sopra di essa.

{% hint style="info" %}
Per il mapping architettonico ho trovato utile produrre una visualizzazione “srotolata” dell’edificio, che rappresenti tutte le superfici dell’edificio come un’immagine piatta e non distorta. La correzione prospettica per le varie sezioni può essere fatta usando la zona Canvas nella vista _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Un’immagine guida “appiattita” per Saltwell Hall a Gateshead, Regno Unito</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Le zone Canvas in una versione embrionale di Liberation (circa 2017!) Nota che i rettangoli rosa scelgono quale parte del Canvas mostrare, mentre le viste di output sotto mostrano verso quale parte di ciascun laser vengono inviate quelle zone.</p></figcaption></figure>

### Canvas nel 3D visualiser

Ricreare nel 3D visualiser il tuo complesso sistema di proiezione multi-laser sarebbe probabilmente complicato, per non dire altro! Quindi, in alternativa, hai la possibilità di posizionare il tuo Canvas all’interno dello spazio 3D. Attiva la casella _Show canvas_ nel pannello _3D visualiser settings_. (Anche eventuali immagini guida presenti nel Canvas verranno mostrate nel visualiser.)

{% hint style="info" %}
Tieni presente che il visualiser continuerà a mostrare le proiezioni del Canvas come effetti atmosferici provenienti dai laser. Puoi semplicemente spostarle fuori dall’inquadratura oppure, se vuoi fare le cose per bene, puoi allinearle con il Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Può essere estremamente soddisfacente quando allinei i fasci del laser con l’immagine del Canvas nel 3D visualiser!</p></figcaption></figure>
