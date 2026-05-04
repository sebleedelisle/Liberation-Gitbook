---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introduzione al Clip Editor

Il clip editor è uno strumento versatile per creare contenuti laser ed è al centro di Liberation. È facile creare elementi semplici, ma è anche abbastanza flessibile da realizzare effetti incredibilmente sofisticati e complessi.

{% hint style="info" %}
L’editor basato su nodi è stata la prima parte di Liberation a essere realizzata! È nato da una conversazione con Rob Stanley durante un raduno laser nel Regno Unito nel 2018, su come avrebbe potuto essere un designer di contenuti laser "object-oriented".

Anche se sembra semplice, è un sistema piuttosto complesso da costruire, ma all’inizio del 2019 avevo una demo funzionante che dimostrava il concetto, e da lì è iniziato tutto questo percorso!
{% endhint %}

È un editor visuale basato su nodi (o [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) che ti sarà familiare se hai usato prodotti come TouchDesigner, MaxMSP o VVVV. Il clip editor però è un po’ diverso e in parte più semplice, perché è stato progettato specificamente per la grafica vettoriale.

Puoi aprire il Clip Editor facendo clic destro sul pulsante del Clip e selezionando _EDIT CLIP_. Oppure fai clic destro su un pulsante Clip vuoto e seleziona _CREATE AND EDIT CLIP_.

### Panoramica

Nel clip editor vedrai:

* I pulsanti dei **nodi Creator** e **Operator** lungo la parte superiore
* I pulsanti dei **nodi Oscillator** lungo il lato sinistro
* Un’anteprima del contenuto in un pannello a destra; se fai clic su un nodo, vedrai una seconda anteprima che mostra il contenuto nel nodo stesso.
* Tutti i nodi e i collegamenti della clip che stai modificando (se è una nuova clip, l’area sarà vuota)
* Il pannello Clip Editor con varie opzioni

Mentre modifichi, vedrai anche l’aspetto della clip nel 3D Visualiser sullo sfondo.

{% hint style="info" %}
Se non vedi alcun output nel 3D Visualiser, potresti dover usare i pulsanti delle zone per attivare le zone desiderate. Devi anche assicurarti che _Preview to lasers_ sia abilitato; vedi [Introduzione al Clip Editor](clip-editor-intro.md#clip-editor-panel "mention") qui sotto.
{% endhint %}

### Creare una clip

Di solito inizi con uno o più [nodi Creator](creator-nodes.md) e colleghi gli [Nodi Operator](operator-nodes/) da sinistra a destra per elaborare il contenuto. Quando avvicini tra loro creator e/o operatori, noterai che si collegano automaticamente. Puoi trascinarli di nuovo lontano l’uno dall’altro per scollegarli.

### Aggiungere nodi alla clip

Fai clic e trascina da uno dei pulsanti dei nodi in alto o a sinistra verso uno spazio vuoto all’interno del clip editor.

### Regolare le impostazioni di un nodo

Fai clic sul pulsante con l’icona a ingranaggio (in alto a destra del nodo) per aprire il pannello delle proprietà di quel nodo.

### Abilitare e disabilitare un nodo

Fai clic sul pulsante con l’icona di accensione (in alto a sinistra del nodo) per abilitare o disabilitare il nodo. Il nodo si attenuerà per indicare che al momento non è attivo. Nota che il contenuto passa comunque attraverso un operatore anche se è disabilitato, ma il nodo non modifica il contenuto.

### Collegare i nodi tra loro

Il contenuto viene creato con un nodo Creator e passa da un nodo all’altro da sinistra a destra; ogni operatore modifica il contenuto in qualche modo e lo passa all’operatore successivo. Ciò che rimane alla fine del percorso è il contenuto della clip. Creator e Operator si collegano automaticamente tra loro quando li avvicini. Per separarli, trascinali di nuovo lontano l’uno dall’altro.

{% hint style="info" %}
Puoi collegare più di un nodo all’input del nodo successivo. È utile per combinare più elementi di contenuto.
{% endhint %}

### Proprietà e socket dei nodi

Ogni nodo ha una serie di socket lungo la parte inferiore e ognuno rappresenta una proprietà del nodo, come luminosità, posizione, scala, rotazione e così via.

I [nodi Oscillator](oscillators/) possono essere collegati a questi socket dal basso e usati per animare queste impostazioni. I nodi Oscillator hanno un output nella parte superiore: fai clic e trascina per estrarre il collegamento e rilascialo in uno dei socket proprietà degli altri nodi.

### Nodi Oscillator

I nodi Oscillator vengono usati per modificare le proprietà nel tempo. In genere rappresentano forme d’onda, come un’onda a dente di sega o sinusoidale, ma alcuni nodi Oscillator usano input esterni (come il livello di ingresso del microfono) come sorgente.

{% hint style="info" %}
Se hai mai usato un sintetizzatore analogico, conoscerai il concetto di oscillatori, comunemente usati per creare forme d’onda o modificare il suono nel tempo. Gli oscillatori in Liberation svolgono un ruolo simile.

**Curiosità:** il nome _Liberation_ è stato ispirato dal Moog Liberation, un sintetizzatore "keytar" uscito nel 1980 e reso famoso da Herbie Hancock, Jean-Michel Jarre e persino James Brown!
{% endhint %}

Gli oscillatori hanno sempre impostazioni di _range_ che controllano il valore minimo e massimo della proprietà da modificare. Inoltre, i _Wave Oscillators_ hanno sempre un’impostazione _duration_ che determina la velocità con cui l’oscillatore modifica il valore. Vedi [Oscillatori a onda](oscillators/wave-oscillators.md "mention") per maggiori informazioni.

### Pannello Clip Editor

* Timer - nella parte superiore del pannello vedrai il tempo corrente della clip mentre avanza
* _RETRIGGER_ - riavvia la clip dall’inizio; particolarmente utile se la clip non è in loop
* _Preview to lasers_ - quando questa opzione è selezionata, vedrai il 3D Visualiser aggiornarsi mentre modifichi questa clip. Se la disattivi, vedrai le clip in esecuzione al di fuori dell’editor. È un’impostazione globale, non specifica della singola clip.
* _UNDO/REDO_ - per il clip editor stesso. È anche associato a `Cmd / Ctrl + Z` e `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - salva le modifiche, ma ti avvisa prima di sovrascrivere
* _SAVE AS A COPY_ - salva la clip nel primo slot disponibile nel clip deck. Questo diventa la nuova posizione della clip e tutti i salvataggi successivi verranno effettuati in questa nuova posizione.
* _EXIT EDITOR_ - chiude il clip editor. Se hai modifiche non salvate, verrà mostrato un pannello di conferma.
