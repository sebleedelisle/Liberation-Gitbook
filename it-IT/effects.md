---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effetti

Il sistema di effetti di Liberation è un modo divertente e versatile per modificare l’output dei clip in tempo reale. Gli effetti sono completamente flessibili e possono essere usati per far lampeggiare tutto, far ruotare gli elementi, cambiare i colori o persino farli muovere in modo casuale!

Qualsiasi cosa tu possa fare nell’editor dei clip può essere usata come effetto. Infatti, gli effetti si modificano con lo stesso identico editor a nodi usato per i clip! Vedi [#editing-effects](effects.md#editing-effects). Le possibilità creative sono praticamente infinite.

I pulsanti degli effetti predefiniti 1-8 si trovano sotto i pulsanti delle zone, mentre gli effetti 9-24 sono i piccoli pulsanti in basso.

#### Applicare un effetto

Premi un pulsante effetto per attivare o disattivare l’effetto oppure, ancora meglio, usa gli slider 1-8 dell’APC40 per sfumare gli effetti in entrata e in uscita. Per sfumare un effetto senza APC40, clicca e trascina su e giù sul pulsante. In alternativa, fai clic destro sul pulsante dell’effetto e regola lo slider _level_.

{% hint style="warning" %}
Premere il pulsante dell’effetto attiverà immediatamente quell’effetto. Tuttavia, tieni presente che se il livello è impostato a zero non succederà nulla! Clicca e trascina sul pulsante per cambiare il livello, oppure fai clic destro e usa lo slider _level_, o ancora usa i fader dell’APC40.
{% endhint %}

#### Effetti e zone delay del clip

Gli effetti ereditano l’impostazione zone delay per ogni clip attualmente in esecuzione. Quindi, se il tuo clip ha un ritardo che si sposta da sinistra a destra e aggiungi l’effetto lampeggiante, anche il lampeggio verrà ritardato da sinistra a destra.

{% hint style="info" %}
Il modo in cui lo zone delay del clip viene ereditato dagli effetti è una di quelle cose estremamente difficili da descrivere, ma ovvie appena le provi!

Direi che è uno degli strumenti più divertenti e creativi integrati in Liberation. Provalo e capirai cosa intendo!
{% endhint %}

#### Parametri degli effetti

Aggiungi un parametro al tuo effetto con un _Parameter node._ Il sistema Parameter è un modo per regolare dall’esterno più impostazioni all’interno dell’effetto. Vedi [parameter-control.md](clip-editor/oscillators/parameter-control.md) per maggiori informazioni.

Usa i controller rotativi 1-8 per regolare il _parameter_ di ogni effetto. Oppure fai clic destro sul pulsante dell’effetto e regola gli slider dei parametri. La modifica del parametro produce risultati diversi a seconda di come è configurato l’effetto. Vedi l’elenco qui sotto per gli effetti predefiniti e per sapere cosa fanno i loro parametri.

{% hint style="info" %}
I controller rotativi 1-8 si trovano lungo la parte superiore di un APC40 Mk2 e in alto a destra su un Mk1. Vedi anche: [apc40-reference.md](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
I piccoli numeri che vedi sui pulsanti degli effetti indicano il _level_ e il _parameter_ dell’effetto. Il _level_ è controllato dal fader sull’APC40, oppure puoi cliccare e trascinare sul pulsante. Il parametro viene regolato con i rotativi sull’APC40, oppure puoi fare clic destro per regolarlo con il mouse.
{% endhint %}

#### Gli effetti predefiniti

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applica un movimento caotico all’output del clip. Il parametro regola la quantità/velocità del caos.
2. **Sine wave** :\
   Deforma tutto il contenuto lungo un’onda sinusoidale in movimento. Il parametro regola la lunghezza d’onda.
3. **Rotation** :\
   Fa ruotare tutto. Il parametro regola la velocità di rotazione.
4. **Horizontal flip** :\
   Schiaccia e allunga tutto in orizzontale. Il parametro regola la velocità.
5. **Scale** :\
   Ridimensiona ripetutamente tutto da pieno a zero. Il parametro regola la velocità.
6. **Hue** :\
   Cambia la tonalità di tutto, ma non cambia la saturazione (cioè tutto ciò che è bianco resta bianco). Il parametro regola la tonalità.
7. **Saturation and hue** :\
   Cambia la tonalità di tutto e satura completamente il colore (cioè tutto ciò che è bianco cambia in quel colore). Il parametro regola la tonalità.
8. **Flash** :\
   Fa lampeggiare ripetutamente la luminosità di tutto da piena a zero. Il parametro regola la velocità del lampeggio.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Nella riga inferiore ci sono altri 16 effetti colore per applicare valori preimpostati di tonalità e saturazione.

Tieni presente che questi sono gli effetti predefiniti, ma possono essere modificati per fare quasi tutto ciò che vuoi!

### Apply to groups

Puoi scegliere quali gruppi vengono influenzati dall’effetto. Fai clic destro e attiva o disattiva le caselle di controllo dei gruppi etichettate _Apply to groups._

Uso principalmente questa configurazione quando lavoro separatamente con grafiche Canvas e raggi laser. Assegno tutti i clip Canvas al gruppo 5 e poi escludo questo gruppo dagli effetti che non voglio applicare a questi clip grafici.

Puoi usarlo anche per applicare dal vivo 2 cambi colore diversi a 2 gruppi di laser contemporaneamente. Crea due effetti di cambio colore e seleziona a quali gruppi di clip applicare ciascuno.

### MX group

Abbreviazione di _Mutually Exclusive_, è un modo per raggruppare gli effetti in modo che solo un effetto del gruppo possa essere attivo nello stesso momento. Nota che solo uno degli effetti predefiniti di cambio colore può essere attivo alla volta. Questo perché sono tutti in MX Group 1.

Questa funzionalità è disattivata se l’impostazione _MX Group_ è 0.

### Modificare gli effetti

Fai clic destro su un effetto qualsiasi e clicca sul pulsante _EDIT EFFECT_ per aprire l’editor degli effetti. Nota che questo editor è identico all’editor dei clip!

Modifica il tuo effetto nello stesso modo in cui modificheresti qualsiasi clip. Vedi [clip-editor](clip-editor/).

Devi avere almeno un creator node; può essere qualsiasi cosa (linea, cerchio, forma, persino testo!), ma probabilmente conviene scegliere qualcosa che abbia più senso nell’anteprima del pulsante dell’effetto.

Quando gli effetti vengono applicati, tutti i creator node nell’effetto vengono sostituiti con l’output dei clip attualmente in esecuzione.

{% hint style="warning" %}
Per motivi tecnici estremamente noiosi, i nodi "trails" non sono abilitati all’interno di un effetto. Lo stesso vale per l’impostazione "delay" dentro i nodi pattern (usano lo stesso sistema). Questo verrà corretto nelle versioni future.
{% endhint %}
