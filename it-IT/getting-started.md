---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Guida rapida

## Introduzione

Benvenuto in **Liberation**, la nuova generazione di software per laser show.

Liberation è un software moderno potente e complesso; è costruito su principi di usabilità e affidabilità per darti la libertà di esprimere la tua creatività. È veloce, efficiente e fluido: segui questa _Guida rapida_ per iniziare subito!

### Gestione dei laser

Liberation è abbastanza flessibile da permetterti di configurare e visualizzare i laser anche senza avere laser reali collegati. Poi, quando sei pronto, puoi assegnare in modo immediato ogni output a un controller laser.

{% hint style="info" %}
Puoi configurare e visualizzare tutti i laser che vuoi in Liberation; i livelli di licenza (Hobbyist, Pro, ecc.) limitano solo il numero di laser che puoi _armare_. Questo significa che puoi progettare laser show con 100 laser anche con una licenza gratuita. Devi fare l’upgrade solo quando arriva il momento di eseguirlo su laser reali.
{% endhint %}

La configurazione predefinita contiene 8 laser distribuiti orizzontalmente, ma puoi personalizzarla come preferisci. Probabilmente è meglio mantenere questa impostazione mentre impari a conoscere il software; più avanti potrai modificarla per adattarla al tuo setup hardware. Vedi [setting-up-your-project.md](setting-up/setting-up-your-project.md)

{% hint style="warning" %}
Importante: prima di armare qualsiasi laser, assicurati di comprendere i rischi coinvolti e leggi con attenzione il capitolo [setting-up-lasers.md](setting-up/setting-up-lasers.md).
{% endhint %}

## Panoramica del software

### Arresto di sicurezza

Ogni volta che usi dei laser devi avere a portata di mano un **pulsante di arresto di emergenza hardware** (vedi [emergency-stop-interlocks.md](hardware/emergency-stop-interlocks.md)); se invece vuoi disarmare tutto in modo meno urgente, puoi usare il pulsante _**DISARM ALL**_ oppure il tasto `Escape` (o il tasto _**SESSION**_ sull’APC40). Puoi anche ridurre la luminosità globale usando lo slider a schermo o il fader principale sull’APC40.

### Elementi slider

In Liberation sono presenti diversi slider e controlli.

{% hint style="info" %}
Fai `Cmd / Ctrl`-clic su uno slider per digitare un nuovo valore se ti serve un controllo più preciso di quello offerto dallo slider.
{% endhint %}

### Scorciatoie da tastiera

L’elenco completo delle scorciatoie da tastiera si trova qui: [keyboard-shortcuts.md](reference/keyboard-shortcuts.md)

### Layout dello schermo

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Non sai a cosa serve un pulsante? Passaci sopra con il mouse per visualizzarne la descrizione!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Nel menu trovi tutte le opzioni di importazione/esportazione dei file e l’apertura dei pannelli. Qui trovi anche l’opzione per autorizzare il computer con il tuo abbonamento, in _Liberation -> Authorise/Deauthorise this computer_.

#### Barra delle icone

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Qui trovi le attività più comuni, come armare/disarmare tutti i laser, la luminosità globale, il test pattern e il passaggio tra le viste 3D, Canvas e Output.

### Viste

L’area grande in alto a sinistra dello schermo può mostrare una delle 3 viste principali: **3D**, **CANVAS** e **OUTPUT.** Puoi passare da una all’altra usando i pulsanti della barra delle icone (oppure usare il tasto `Tab` per alternare le viste 3D e OUTPUT, e poi continuare a premere Tab per scorrere uno alla volta gli output dei laser).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

La 3D View mostra come appariranno i tuoi laser e può essere configurata per corrispondere al tuo setup laser. Fai clic e trascina per ruotare la camera, usa la rotellina del mouse per muoverti avanti e indietro. Trovi molte altre opzioni nel pannello _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Vedi [3d-visualiser.md](setting-up/3d-visualiser.md).

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

La Output View serve a configurare zone e maschere per ogni laser. Nota il grande numero nell’angolo in alto a sinistra: ti permette di vedere facilmente su quale laser ti trovi.

Questa vista rappresenta l’intero output di questo laser e mostra dove si trova ogni zona al suo interno. Per impostazione predefinita c’è una sola zona per laser, ma puoi aggiungere tutte le zone ragionevolmente gestibili, e le vedrai tutte in questa vista.

{% hint style="info" %}
**Che cos’è una zona?**

Una zona è uno spazio all’interno dell’output di un laser in cui puoi indirizzare contenuti laser. Puoi avere più di una zona per ogni laser. Il tipo di zona più semplice è una zona _beam_, ma esistono anche zone _canvas_ e zone _DMX_. In questa guida ci concentreremo soprattutto sulle zone beam, che di solito vengono usate per creare effetti beam atmosferici nell’aria.
{% endhint %}

Puoi selezionare il laser da modificare in uno di questi modi:

* con i pulsanti numerati nella barra in alto
* premendo il tasto numerico del laser desiderato _(tasti 1-9_ keys\_)\_
* con il tasto `Tab`, per passare da un laser al successivo

Aggiungi un nuovo laser al setup premendo il pulsante _+_. Nel pannello _Laser Overview_ è disponibile anche un pulsante _ADD LASER_.

Elimina un laser dal setup premendo il pulsante rosso ⊖ nel pannello _Laser Overview_.

Puoi ingrandire e ridurre la vista con la rotellina del mouse, e fare clic e trascinare in qualsiasi punto in cui non ci sia una zona per spostare la vista.

Fai clic su una zona per selezionarla, poi regola i suoi punti angolari con il mouse. Tieni premuto `Alt / Option` mentre trascini un angolo per renderla non uniforme. Fai clic destro sulla zona per vedere altre opzioni, inclusa la modifica del tipo di zona.

A sinistra c’è una barra con una serie di pulsanti a icona: passa sopra a qualsiasi pulsante per visualizzare la descrizione della sua funzione. I pulsanti qui permettono di aggiungere zone beam, zone canvas e maschere. Sono presenti anche opzioni per impostare un test pattern solo per questo laser, oltre alle impostazioni di griglia e snapping.

Per maggiori dettagli vedi [output-view](output-view/).

#### Canvas

Il sistema Canvas viene usato soprattutto per grafica e mapping architetturale. Puoi distribuire immagini complesse su più laser e correggere la prospettiva di ogni sezione. Vedi [graphics-and-the-canvas-system](graphics-and-the-canvas-system/).

### Controller MIDI APC40

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Anche se è possibile controllare Liberation con mouse e tastiera, è molto meglio usare un’interfaccia di controllo MIDI APC40 (la Mark 2 è la scelta migliore, ma funziona anche la Mark 1).

Vedi anche: [apc40-reference.md](reference/apc40-reference.md)

Abbiamo inoltre implementato il supporto per APC Mini Mark 2 e MIDI Fighter Twister, e altri controller sono in sviluppo. Tuttavia, nella maggior parte dei casi APC40 Mark 2 resta l’opzione migliore.

### Clip ed effetti

{% hint style="info" %}
**Che cos’è una clip?**

Una clip è un contenitore per qualsiasi contenuto laser all’interno di Liberation. Le clip possono contenere beam o animazioni grafiche e di solito funzionano in loop. Possono essere indirizzate a qualsiasi zona (o _Canvas target area_) e vengono attivate usando i pulsanti clip all’interno del clip deck.
{% endhint %}

#### Panoramica del Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Questa griglia si chiama _clip deck_ ed è il punto in cui vengono memorizzate tutte le clip laser. È progettata per corrispondere direttamente alla griglia di pulsanti 8 x 5 del tuo APC40.

**Navigare nel clip deck.**

Puoi scorrere il clip deck a sinistra e a destra usando:

* Tasti freccia sinistra e destra. Aggiungi `Cmd / Ctrl` per scorrere una pagina intera alla volta.
* Trackpad: scorri con uno swipe
* Mouse: se il tuo mouse ha lo scorrimento laterale, puoi usarlo mentre il puntatore si trova sopra il clip deck
* Manopola di scorrimento APC40
* Pulsanti APC40 _<- DEVICE ->_

Per aiutarti a orientarti, in alto c’è un mini visualizzatore del clip deck. Vedi anche [clips](clips/)

#### Avviare e fermare le clip

Premi un pulsante clip, con il mouse o con l’APC40, per avviare una clip. Premilo di nuovo per fermarla. Quando avvii una clip, tutte le altre clip dello stesso colore si fermeranno automaticamente, a meno che tu non tenga premuto _shift_.

Alcune clip saranno in _Flash mode_ (per impostazione predefinita, quelle rosse); in questo caso si fermeranno appena rilasci il pulsante clip.

Il pulsante _STOP_ ferma tutte le clip attualmente in esecuzione.

#### Impostare le zone di output per la clip

Sotto i pulsanti clip vedrai i pulsanti zona: per impostazione predefinita, le zone beam da 1 a 8 (_BEAM 1_, _BEAM 2_, ecc.). I pulsanti zona si illuminano per indicare quali zone sono assegnate alla clip attualmente selezionata.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Due righe sotto i pulsanti zona vedrai i pulsanti X/Y flip: attivali o disattivali per capovolgere la clip orizzontalmente e verticalmente.

{% hint style="info" %}
Nota che queste assegnazioni delle zone e le impostazioni X/Y flip sono collegate alla clip stessa: vengono mantenute la prossima volta che esegui quella clip. Non sono impostazioni globali.
{% endhint %}

Fai clic destro su una clip per modificarne altre impostazioni. Vedi anche [clip-settings.md](clips/clip-settings.md)

### Gruppi

Noterai che ogni clip ha un contorno colorato: questo colore rappresenta il _gruppo_ a cui appartiene. Anche i pulsanti clip dell’APC40 si illuminano con questo colore.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Gruppo 1</td><td>Ciano</td></tr><tr><td>Gruppo 2</td><td>Arancione</td></tr><tr><td>Gruppo 3</td><td>Rosso</td></tr><tr><td>Gruppo 4</td><td>Indaco</td></tr><tr><td>Gruppo 5</td><td>Verde</td></tr></tbody></table>

Il sistema dei gruppi è molto flessibile e ti permette di:

* Mantenere in esecuzione le clip di un gruppo mentre attivi o disattivi gruppi in un altro
* Assegnare rapidamente zone e X/Y flip a tutte le clip di un gruppo
* Impostare il _Flash mode_ per una clip (il Gruppo 3 è impostato su _Flash mode_ per impostazione predefinita)

I gruppi hanno anche impostazioni di transizione in/out che possono essere ereditate dalle clip oppure sovrascritte.

Puoi assegnare il gruppo della clip usando i pulsanti nel menu del clic destro, oppure con l’APC40: premi il pulsante del gruppo e, _mentre lo tieni ancora premuto,_ premi i pulsanti clip.

Modificare le impostazioni di zona per tutte le clip di un gruppo

Con l’APC40, premi il pulsante del gruppo, poi _mentre lo tieni ancora premuto,_ usa i pulsanti zona e X/Y per attivare o disattivare le impostazioni di zona per tutte le clip di quel gruppo.

Vedi anche [groups.md](clips/groups.md)

### Effetti

Il sistema di effetti di Liberation è un modo potente e versatile per modificare l’output delle clip in tempo reale. I pulsanti degli effetti predefiniti 1-8 si trovano sotto i pulsanti zona.

#### Applicare un effetto

Premi un pulsante effetto per attivare o disattivare l’effetto oppure, ancora meglio, usa gli slider 1-8 dell’APC40 per sfumare gli effetti in entrata e in uscita.

#### Parametri degli effetti

Usa i controller rotativi 1-8\* per regolare il _parametro_ di ogni effetto. In alternativa, puoi fare clic destro con il mouse per regolare livello e parametro. La modifica del parametro produce risultati diversi a seconda di come è configurato l’effetto. Vedi l’elenco seguente per gli effetti predefiniti.

{% hint style="info" %}
I piccoli numeri che vedi sui pulsanti effetto si riferiscono al _level_ e al _parameter_ dell’effetto. Il _level_ è controllato dal fader sull’APC40, oppure puoi fare clic e trascinare sul pulsante. Il parametro viene regolato dai rotativi sull’APC40, oppure puoi fare clic destro per regolarlo con il mouse.
{% endhint %}

_\*I controller rotativi 1-8 si trovano lungo la parte superiore di un APC40 Mk2 e in alto a destra su un Mk1. Vedi anche:_ [apc40-reference.md](reference/apc40-reference.md)

#### Gli effetti predefiniti

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applica un movimento caotico all’output della clip. Il parametro regola quantità/velocità del caos.
2. **Sine wave** :\
   Deforma tutto il contenuto lungo un’onda sinusoidale in movimento. Il parametro regola la lunghezza d’onda.
3. **Rotation** :\
   Fa ruotare tutto. Il parametro regola la velocità di rotazione.
4. **Horizontal flip** :\
   Comprime e allunga tutto in orizzontale. Il parametro regola la velocità.
5. **Scale** :\
   Scala ripetutamente tutto da pieno a zero. Il parametro regola la velocità.
6. **Hue** :\
   Cambia la tonalità di tutto, ma non cambia la saturazione (cioè tutto ciò che è bianco resta bianco). Il parametro regola la tonalità.
7. **Saturation and hue** :\
   Cambia la tonalità di tutto e satura completamente il colore (cioè tutto ciò che è bianco diventa del colore selezionato). Il parametro regola la tonalità.
8. **Flash** :\
   Fa lampeggiare ripetutamente la luminosità di tutto da piena a zero. Il parametro regola la velocità del flash.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Nella riga in basso sono presenti altri 16 effetti colore per applicare valori preimpostati di tonalità e saturazione.

Nota che questi sono gli effetti predefiniti, ma possono essere modificati per fare quasi tutto ciò che vuoi.

#### Che cos’è la _"clip attualmente selezionata"_?

Quando avvii una clip, questa si illumina per indicare che è attiva. Ha anche un contorno bianco che indica che quella è la clip attualmente _selezionata_. Ogni volta che attivi/disattivi i pulsanti zona o modifichi le impostazioni della clip, le modifiche vengono applicate alla _clip attualmente selezionata._

{% hint style="info" %}
Per selezionare una clip senza attivarla, premi il tasto `Alt / Option` prima di premere il pulsante clip. È un buon modo per regolare le sue zone e altre impostazioni senza eseguirla.
{% endhint %}

### Pannello Clip Settings

Usa il pannello _Clip Settings_ per modificare scala, posizione X/Y e accedere al potente sistema di zone delay.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Pannello Global Settings

Apri il pannello _Global Settings_ per regolare le impostazioni globali dell’output che influenzano tutti gli output in tutte le zone.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Attiva AUTO RESET per ripristinare automaticamente tutte le _Global settings_ ogni volta che non ci sono clip in riproduzione.

### Timing

Quasi tutti gli spettacoli laser hanno una colonna sonora musicale, quindi il sistema di timing di Liberation è basato su un tempo in battiti al minuto. Nel _Tempo Panel_ puoi vedere una rappresentazione del tempo: ogni quadrato rappresenta un battito e li vedrai lampeggiare a tempo.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Sono disponibili più opzioni di sincronizzazione, tra cui MIDI clock e Ableton Link. Se conosci il tempo della musica puoi regolarlo manualmente usando lo slider a schermo o la manopola Tempo dell’APC40, ma puoi anche restare a tempo con la musica usando il sistema _Tap Tempo_\_ .\_

#### Tap Tempo

_Tap Tempo_ è un termine comunemente usato nelle app musicali e ti permette di battere il tempo seguendo il beat per impostare il tempo mentre la musica è in riproduzione. Puoi usare il pulsante a schermo, anche se è consigliato usare il tasto _T_ o il pulsante _Tap Tempo_ sull’APC40 (o anche un foot switch, se preferisci).

Premi il tasto _R_ o il pulsante _Metronome_ (APC40) per reimpostare il tempo all’inizio della battuta.

Premi il tasto _Y_ o ruota la manopola _Tempo_ (APC40) per arrotondare il tempo a un numero intero. Può essere utile per la musica elettronica, che tende ad avere un numero intero di battiti al minuto.

### Organizzare il clip deck

Per spostare una clip nel clip deck, fai clic e trascinala in una nuova posizione. Durante il trascinamento puoi usare i tasti cursore (o la rotellina/i pulsanti di scorrimento sull’APC40) per scorrere a sinistra e a destra.

Tieni premuto il tasto `Alt / Option` mentre trascini per creare una copia.

Fai `Alt / Option`-clic su una clip per selezionarla senza avviarla.

Fai `Alt / Option + Shift`-clic su una clip per selezionare più elementi, oppure fai clic e trascina fuori da una clip per selezionare con il “lazo”.

Facendo clic e trascinando, sposterai TUTTE le clip selezionate.

Per eliminare una o più clip, trascinale fuori dal clip deck (apparirà un’icona del cestino) oppure usa il pulsante DELETE dal menu del clic destro della clip.

### Pannello Laser Overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Il pannello _Laser Overview_ ti offre una rapida panoramica dello stato dei laser attualmente in esecuzione. Il quadrato verde a destra indica che il controller laser funziona correttamente. Se diventa arancione, ci sono drop-out occasionali; se diventa rosso, si è disconnesso. Se è grigio, non è collegato a nessun controller.

Il grafico al centro mostra la cronologia della durata dei frame, mentre il numero a destra indica il frame rate attuale. Più il contenuto è complesso, più il frame rate sarà basso (cioè l’immagine sarà più soggetta a sfarfallio). Qualsiasi valore sotto circa 25 fps inizierà a sembrare un po’ tremolante.

### Collegamento ai laser: pannello Controller Assignment

Fai clic sul pulsante _Assign Laser Controllers_ per aprire il pannello _Controller Assignment_. Questo pannello è accessibile anche dalla barra dei menu tramite _View -> Controller Assignment_.

Qui puoi scegliere quali output laser inviare a quali controller laser. Trascina i controller dall’elenco a destra negli slot a sinistra. Puoi rinominare i controller per farli corrispondere al laser a cui sono associati (usa il pulsante con l’icona della penna).

Leggi il capitolo [controller-assignment.md](setting-up/controller-assignment.md) per maggiori dettagli.

{% hint style="danger" %}
Prima di armare qualsiasi laser, assicurati di leggere il capitolo [setting-up-lasers.md](setting-up/setting-up-lasers.md).
{% endhint %}

### Pannello Laser Output

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Questo pannello mostra le impostazioni del _laser attualmente selezionato_, rappresentato dal numero in alto. Cambia il laser attualmente selezionato usando il tasto _tab_, premendo un tasto numerico, facendo clic su un numero laser nel pannello _Laser Overview_ o nella _output view._

* **Number button** arma e disarma il laser; se è rosso, il laser è armato.
* **Brightness** regola la luminosità del laser indipendentemente dagli altri laser (e viene combinata con l’impostazione _global brightness_: per esempio, se entrambe sono al 50%, il laser sarà al 25%).
* **Test Pattern** attiva un test pattern solo per questo laser (sovrascrive l’impostazione globale del test pattern).
* **Orientation** corregge i laser montati di lato o capovolti.
* **Flip Horizontal and Flip Vertical** invertono l’output del laser. Utile per correggere l’output su laser cablati in modo non uniforme.
* **Copy Laser Settings** apre un pannello che permette di copiare varie impostazioni da questo laser ad altri.

### Impostazioni scanner

I laser da spettacolo funzionano muovendo un singolo raggio laser a velocità estremamente elevata e accendendolo e spegnendolo per disegnare forme nell’aria. Ciò che percepisci come linee, forme e immagini è in realtà il raggio che traccia percorsi più velocemente di quanto i tuoi occhi possano seguire.

Uno stream di punti è il dato che indica al laser dove muoversi e quando il raggio deve essere acceso o spento. In Liberation, le clip vengono convertite in questo stream di punti in tempo reale mentre vengono inviate ai laser.

Liberation ti offre un controllo dettagliato su come viene generato questo stream di punti, permettendoti di bilanciare fluidità, luminosità e prestazioni per ogni laser.

{% hint style="info" %}
Se sei abituato a software laser più datati che si basano su stream di punti precalcolati, questo approccio potrebbe sembrarti diverso all’inizio. Tuttavia, la generazione dei punti in tempo reale permette di ottimizzare lo stesso contenuto in modo diverso per ogni laser. Questo semplifica il lavoro con più laser che hanno scanner di velocità o qualità diverse, senza duplicare o ricostruire i contenuti. Inoltre mantiene molto piccoli i file delle clip: per questo l’intero clip deck predefinito di Liberation pesa solo pochi megabyte invece di gigabyte.
{% endhint %}

Le impostazioni scanner di base sono:

* **Speed** è la velocità dello scanner, cioè quanto rapidamente il laser si muove per disegnare le forme. È equivalente alla regolazione del point rate nei software laser tradizionali, ma in Liberation puoi modificare la velocità di movimento del laser _indipendentemente dal point rate._ Non dovresti avere bisogno di modificarla.
* **Scanner sync** (a volte chiamato _blank shift_, in precedenza Colour Shift) Gli scanner muovono il laser molto rapidamente, ma di solito la variazione di luminosità e colore non è sincronizzata con il movimento. Questo si manifesta come piccole “code” tremolanti di luce sui bordi di beam e linee. Usa questa regolazione per sincronizzare movimento e colore. Vedi [laser-settings.md](setting-up/laser-settings.md)

Le altre impostazioni scanner avanzate sono trattate nel capitolo [advanced](advanced/).

### Zoning

Per una guida completa alla configurazione e allo zoning dei laser, vedi: [setting-up-lasers.md](setting-up/setting-up-lasers.md)
