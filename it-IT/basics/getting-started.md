# ✅ Guida rapida

## Introduzione

Benvenuto in **Liberation**: la nuova generazione di software per laser show.

Liberation è un software moderno, potente e complesso; è costruito su principi di usabilità e affidabilità per darti la libertà di esprimere la tua creatività. È veloce, efficiente e fluido; segui questa _guida rapida_ per iniziare subito!

### Gestire i laser

Liberation è abbastanza flessibile da permetterti di configurare e visualizzare i laser anche senza avere alcun laser fisicamente collegato. Quando poi sei pronto, puoi assegnare facilmente ogni output a un controller laser.

{% hint style="info" %}
Puoi configurare e visualizzare tutti i laser che vuoi in Liberation; i livelli di licenza (Hobbyist, Pro, ecc.) limitano solo il numero di laser che puoi _armare._ Questo significa che puoi progettare laser show con 100 laser anche con una licenza gratuita. Devi fare l’upgrade solo quando devi effettivamente eseguirli su laser reali.
{% endhint %}

La configurazione predefinita ha 8 laser distribuiti orizzontalmente, ma puoi personalizzarla come preferisci. Probabilmente è meglio mantenere questa impostazione mentre prendi confidenza con il software, e modificarla più avanti per adattarla al tuo setup hardware. (Vedi [setting-up-your-project.md](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Importante: prima di armare qualsiasi laser, assicurati di comprendere i rischi coinvolti e leggi con attenzione il capitolo [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

## Panoramica del software

### Arresto di sicurezza

Ogni volta che usi i laser devi avere a portata di mano un **pulsante di emergenza hardware** (vedi [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md)); se invece vuoi disarmare tutto in modo meno urgente puoi usare il pulsante _**DISARM ALL**_, oppure il tasto `Escape` (o il tasto _**SESSION**_ sull’APC40). Puoi anche ridurre la luminosità globale usando lo slider sullo schermo o il fader principale sull’APC40.

### Slider e controlli

In Liberation sono presenti vari slider e controlli.

{% hint style="info" %}
Fai `Cmd / Ctrl`-clic su uno slider per digitare un nuovo valore se hai bisogno di un controllo più preciso di quello offerto dallo slider.
{% endhint %}

### Scorciatoie da tastiera

L’elenco completo delle scorciatoie da tastiera è disponibile qui: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md)

### Layout dello schermo

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Non sei sicuro di cosa faccia un pulsante? Passaci sopra con il mouse per visualizzare una descrizione!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Nel menu trovi tutte le opzioni di importazione/esportazione dei file e l’apertura dei pannelli. Qui trovi anche l’opzione per autorizzare il computer con il tuo abbonamento (in _Liberation -> Authorise/Deauthorise this computer_).

#### Barra delle icone

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Qui trovi le operazioni più comuni, come armare/disarmare tutti i laser, la luminosità globale, il test pattern e il passaggio tra le viste 3D, Canvas e Output.

### Viste

La grande area in alto a sinistra dello schermo può mostrare una delle 3 viste principali: **3D**, **CANVAS** e **OUTPUT.** Passa da una all’altra usando i pulsanti della barra delle icone (oppure usa il tasto `Tab` per alternare tra le viste 3D e OUTPUT, e poi continuare a scorrere in sequenza ogni output laser).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Vista 3D

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

La vista 3D mostra come appariranno i tuoi laser e può essere configurata per corrispondere al tuo setup laser. Fai clic e trascina per ruotare la camera, usa la rotellina del mouse per avanzare e arretrare. Puoi trovare molte altre opzioni nel pannello _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Vedi [3d-visualiser.md](../setting-up/3d-visualiser.md).

#### Vista Output

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

La vista Output serve a configurare zone e mask per ogni laser. Nota il numero molto grande nell’angolo in alto a sinistra, così puoi vedere subito su quale laser ti trovi.

Questa vista rappresenta l’intero output di questo laser e mostra dove si trova ogni zone al suo interno. Per impostazione predefinita c’è una sola zone per laser, ma puoi aggiungerne quante ne sono ragionevolmente pratiche, e le vedrai tutte in questa vista.

{% hint style="info" %}
**Che cos’è una zone?**

Una zone è uno spazio all’interno dell’output di un laser in cui puoi indirizzare contenuti laser. Puoi avere più di una zone per ogni laser. Il tipo più semplice di zone è una zone _beam_, ma esistono anche zone _canvas_ e zone _DMX_. In questa guida ci concentreremo soprattutto sulle beam zone, usate di solito per creare effetti beam atmosferici nell’aria.
{% endhint %}

Puoi selezionare il laser da modificare usando:

* i pulsanti numerati nella barra in alto
* il tasto numerico del laser desiderato _(tasti 1-9_)\_
* il tasto `Tab` per passare da uno al successivo

Aggiungi un nuovo laser al setup premendo il pulsante _+_. (C’è anche un pulsante _ADD LASER_ nel pannello _Laser Overview_)

Elimina un laser dal setup premendo il pulsante rosso ⊖ nel pannello _Laser Overview_.

Puoi fare zoom avanti e indietro con la rotellina del mouse, e fare clic e trascinare in qualsiasi punto in cui non ci sia una zone per spostare la vista.

Fai clic su una zone per selezionarla e poi regola i suoi punti d’angolo con il mouse. Usa il tasto `Alt / Option` mentre trascini un angolo per renderla non uniforme. Fai clic destro sulla zone per vedere altre opzioni, inclusa la modifica del tipo di zone.

A sinistra trovi una barra con una serie di pulsanti a icona: passa sopra qualsiasi pulsante per visualizzare una descrizione della sua funzione. I pulsanti qui permettono di aggiungere beam zone, canvas zone e mask. Ci sono anche opzioni per impostare un test pattern solo per questo laser, oltre a impostazioni di griglia e snapping.

Per maggiori dettagli vedi [output-view](../output-view/).

#### Canvas

Il sistema Canvas viene usato soprattutto per grafica e mapping architettonico. Puoi distribuire immagini complesse su più laser e correggere la prospettiva di ogni sezione. Vedi [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/).

### Controller MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Anche se è possibile controllare Liberation con mouse e tastiera, è molto meglio usare un’interfaccia di controllo MIDI APC40 (Mark 2 è la scelta migliore, ma funziona anche Mark 1).

Vedi anche: [apc40-reference.md](../reference/apc40-reference.md)

Ora abbiamo implementato anche il supporto per APC Mini Mark 2 e MIDI Fighter Twister, e altri controller sono in sviluppo. Tuttavia, APC40 Mark 2 è l’opzione migliore nella maggior parte dei casi.&#x20;

### Clip ed effetti

{% hint style="info" %}
**Che cos’è un clip?**

Un clip è un contenitore per qualsiasi contenuto laser all’interno di Liberation. I clip possono contenere beam o animazioni grafiche e di solito sono cicli in loop. Possono essere indirizzati a qualsiasi zone (o _Canvas target area_) e vengono attivati usando i pulsanti clip all’interno del clip deck.
{% endhint %}

#### Panoramica del clip deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Questa griglia è chiamata _clip deck_ ed è il punto in cui sono salvati tutti i clip laser. È progettata per corrispondere direttamente alla griglia 8 x 5 di pulsanti del tuo APC40.

**Navigare nel clip deck.**

Puoi scorrere il clip deck a sinistra e a destra usando:

* Frecce sinistra e destra. Aggiungi `Cmd / Ctrl` per scorrere di una pagina intera alla volta.
* Trackpad: swipe
* Mouse: se il mouse supporta lo scorrimento laterale, puoi usarlo mentre il puntatore è sopra il clip deck
* Manopola di scorrimento dell’APC40
* Pulsanti APC40 _<- DEVICE ->_

Per aiutarti a orientarti, in alto c’è un mini visualiser del clip deck. Vedi anche [clips](../clips/)

#### Avviare e fermare i clip

Premi un pulsante clip (con il mouse o con l’APC40) per avviare un clip. Premilo di nuovo per fermarlo. Quando avvii un clip, tutti gli altri clip dello stesso colore si fermeranno automaticamente, a meno che tu non tenga premuto _shift_.

Alcuni clip saranno in _Flash mode_ (per impostazione predefinita, quelli rossi); in questo caso si fermeranno appena rilasci il pulsante clip.

Il pulsante _STOP_ ferma tutti i clip attualmente in esecuzione.

#### Impostare le output zone per il clip

Sotto i pulsanti clip vedrai i pulsanti delle zone, per impostazione predefinita le beam zone da 1 a 8 (_BEAM 1_, _BEAM 2_, ecc.). I pulsanti zone si illuminano per indicare quali zone sono assegnate al clip attualmente selezionato.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Due righe sotto i pulsanti zone trovi i pulsanti di flip X/Y: attivali per ribaltare il clip in orizzontale e in verticale.

{% hint style="info" %}
Nota che queste assegnazioni delle zone e le impostazioni di flip X/Y sono collegate al clip stesso; verranno mantenute la prossima volta che esegui quel clip. Non sono impostazioni globali.
{% endhint %}

Fai clic destro su un clip per modificare altre impostazioni del clip. Vedi anche [clip-settings.md](../clips/clip-settings.md)

### Gruppi

Noterai che ogni clip ha un contorno colorato, e questo colore rappresenta il _gruppo_ a cui appartiene. Anche i pulsanti clip dell’APC40 si illuminano con questo colore.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Gruppo 1</td><td>Ciano</td></tr><tr><td>Gruppo 2</td><td>Arancione</td></tr><tr><td>Gruppo 3</td><td>Rosso</td></tr><tr><td>Gruppo 4</td><td>Indaco</td></tr><tr><td>Gruppo 5</td><td>Verde</td></tr></tbody></table>

Il sistema dei gruppi è molto flessibile e ti permette di:

* Mantenere in esecuzione i clip di un gruppo mentre attivi e disattivi i gruppi in un altro
* Assegnare rapidamente zone e flip X/Y a tutti i clip di un gruppo
* Impostare la _Flash mode_ per un clip (il Gruppo 3 è impostato su _Flash mode_ per impostazione predefinita)

I gruppi hanno anche impostazioni di transizione in/out che possono essere ereditate dai clip oppure sovrascritte.

Puoi assegnare il gruppo del clip usando i pulsanti nel menu del clic destro, oppure con l’APC40 puoi premere il pulsante del gruppo e, _mentre è ancora tenuto premuto,_ premere i pulsanti clip.

Modificare le impostazioni delle zone per tutti i clip di un gruppo

Usando l’APC40, premi il pulsante del gruppo, poi _mentre è ancora tenuto premuto,_ usa i pulsanti zone e X/Y per attivare o disattivare le impostazioni delle zone per tutti i clip di quel gruppo.

Vedi anche [groups.md](../clips/groups.md)

### Effetti

Il sistema degli effetti in Liberation è un modo potente e versatile per modificare l’output del clip in tempo reale. I pulsanti effetti predefiniti 1-8 si trovano sotto i pulsanti zone.

#### Applicare un effetto

Premi un pulsante effetto per attivare/disattivare l’effetto, o ancora meglio usa gli slider 1-8 dell’APC40 per sfumare gli effetti in entrata e in uscita.

#### Parametri degli effetti

Usa i controller rotativi 1-8\* per regolare il _parametro_ di ogni effetto. (Oppure puoi fare clic destro con il mouse per regolare livello e parametro). La variazione del parametro ha effetti diversi a seconda di come è configurato l’effetto. Vedi l’elenco seguente per gli effetti predefiniti.

{% hint style="info" %}
I piccoli numeri che vedi sui pulsanti degli effetti si riferiscono al _level_ e al _parameter_ dell’effetto. Il _level_ è controllato dal fader sull’APC40, oppure puoi fare clic e trascinare sul pulsante. Il parametro viene regolato dai rotativi sull’APC40, oppure puoi fare clic destro per regolarlo con il mouse.
{% endhint %}

_\*I controller rotativi 1-8 si trovano lungo la parte superiore di un APC40 Mk2 e in alto a destra sul Mk1. Vedi anche:_ [apc40-reference.md](../reference/apc40-reference.md)

#### Gli effetti predefiniti

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Applica un movimento caotico all’output del clip. Il parametro regola quantità/velocità del caos.
2. **Sine wave** :\
   Deforma tutto il contenuto lungo un’onda sinusoidale in movimento. Il parametro regola la lunghezza d’onda.
3. **Rotation** :\
   Fa ruotare tutto. Il parametro regola la velocità di rotazione.
4. **Horizontal flip** :\
   Schiaccia e allunga tutto orizzontalmente. Il parametro regola la velocità.
5. **Scale** :\
   Scala ripetutamente tutto da pieno a zero. Il parametro regola la velocità.
6. **Hue** :\
   Cambia la tonalità di tutto, ma non modifica la saturazione (cioè tutto ciò che è bianco resta bianco). Il parametro regola la tonalità.
7. **Saturation and hue** :\
   Cambia la tonalità di tutto e satura completamente il colore (cioè tutto ciò che è bianco cambia nel colore). Il parametro regola la tonalità.
8. **Flash** :\
   Fa lampeggiare ripetutamente la luminosità di tutto da piena a zero. Il parametro regola la velocità del flash.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Nella riga inferiore ci sono altri 16 effetti colore per applicare valori preimpostati di tonalità e saturazione.

Nota che questi sono gli effetti predefiniti, ma possono essere modificati per fare quasi tutto ciò che vuoi!

#### Che cos’è il _"currently selected clip"_?

Quando avvii un clip, questo si illumina per indicare che è attivo. Ha anche un contorno bianco, che indica che è il clip attualmente _selezionato_. Ogni volta che attivi/disattivi pulsanti zone o regoli le impostazioni del clip, le modifiche vengono applicate al _currently selected clip._

{% hint style="info" %}
Per selezionare un clip senza attivarlo, premi il tasto `Alt / Option` prima di premere il pulsante clip. È un buon modo per regolare zone e altre impostazioni senza eseguirlo.
{% endhint %}

### Pannello Clip Settings

Usa il pannello _Clip Settings_ per modificare scala, posizione X/Y e accedere al potente sistema di delay delle zone.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Pannello Global Settings

Trova il pannello _Global Settings_ per regolare le impostazioni globali di output che influenzano tutto l’output su tutte le zone.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Attiva AUTO RESET per reimpostare automaticamente tutti i _Global settings_ ogni volta che non ci sono clip in riproduzione.&#x20;

### Timing

Quasi tutti gli spettacoli laser hanno una qualche colonna sonora, quindi il sistema di timing in Liberation si basa su un tempo in battiti al minuto. Nel _Tempo Panel_ puoi vedere una rappresentazione del tempo: ogni quadrato rappresenta un battito e puoi vederli lampeggiare a tempo.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Sono disponibili diverse opzioni di sincronizzazione, inclusi MIDI clock e Ableton Link. Se conosci il tempo della musica puoi regolarlo manualmente usando lo slider sullo schermo o la manopola Tempo dell’APC40, ma puoi anche restare a tempo con la musica usando il sistema _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ è un termine usato comunemente nelle app musicali e ti permette di battere il tempo seguendo il beat per impostare il tempo mentre la musica è in riproduzione. Puoi usare il pulsante sullo schermo, anche se è consigliato usare il tasto _T_ o il pulsante _Tap Tempo_ sull’APC40 (o anche un foot switch, se preferisci).

Premi il tasto _R_ o il pulsante _Metronome_ (APC40) per riportare il tempo all’inizio della battuta.

Premi il tasto _Y_ o ruota la manopola _Tempo_ (APC40) per arrotondare il tempo a un numero intero. Può essere utile per la musica elettronica, che tende ad avere un numero intero di battiti al minuto.

### Organizzare il clip deck

Per spostare un clip nel clip deck, fai clic e trascinalo in una nuova posizione. Mentre trascini, puoi usare i tasti cursore (o la rotellina/i pulsanti di scorrimento sul tuo APC40) per scorrere a sinistra e a destra.

Premi il tasto `Alt / Option` mentre trascini per creare una copia.

Fai `Alt / Option`-clic su un clip per selezionarlo senza avviarlo.

Fai `Alt / Option + Shift`-clic su un clip per effettuare una selezione multipla, oppure fai clic e trascina fuori da un clip per selezionare con il “lazo”.&#x20;

Clic e trascinamento sposteranno TUTTI i clip selezionati.

Per eliminare uno o più clip, trascinali fuori dal clip deck (apparirà l’icona di un cestino) oppure usa il pulsante DELETE dal menu del clic destro del clip.

### Pannello Laser overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Il pannello _Laser overview panel_ ti offre una rapida panoramica dello stato dei laser attualmente in esecuzione. Il quadrato verde a destra indica che il controller laser funziona correttamente. Se diventa arancione, ci sono drop-out occasionali; se diventa rosso, si è disconnesso. Se è grigio, non è collegato ad alcun controller.&#x20;

Il grafico al centro mostra la cronologia delle durate dei frame, e il numero a destra è il frame rate corrente. Più il contenuto è complesso, più il frame rate sarà lento (cioè più sfarfallante). Qualsiasi valore sotto circa 25 fps inizierà ad apparire un po’ sfarfallante.&#x20;

### Collegarsi ai laser - pannello Controller Assignment

Fai clic sul pulsante _Assign Laser Controllers_ per aprire il pannello _Controller Assignment_. (Questo pannello è accessibile anche da _View -> Controller Assignment_ nella barra dei menu).

Qui puoi scegliere quali output laser inviare a quali controller laser. Trascina i controller dall’elenco a destra negli slot a sinistra. Puoi rinominare i controller in modo che corrispondano al laser a cui sono associati (usa il pulsante con l’icona della penna).

Leggi il capitolo [controller-assignment.md](../setting-up/controller-assignment.md) per maggiori dettagli.

{% hint style="danger" %}
Prima di armare qualsiasi laser, assicurati di leggere il capitolo [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

### Pannello Laser output

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Questo pannello mostra le impostazioni del _currently selected laser_ (rappresentato dal numero in alto). Cambia il laser attualmente selezionato usando il tasto _tab_, premendo un tasto numerico, facendo clic su un numero laser nel pannello _Laser Overview_ o nella _output view._

* **Number button** arma e disarma il laser; se è rosso, il laser è armato.
* **Brightness** regola la luminosità del laser indipendentemente dagli altri laser (e viene combinata con l’impostazione _global brightness_: ad esempio, se entrambe sono al 50%, il tuo laser sarà al 25%).
* **Test Pattern** attiva un test pattern solo per questo laser (sovrascrive l’impostazione globale del test pattern)
* **Orientation** corregge i laser montati lateralmente o capovolti.
* **Flip Horizontal and Flip Vertical** inverte l’output del laser. Utile per correggere l’output su laser cablati in modo non coerente.
* **Copy Laser Settings** apre un pannello che ti permette di copiare varie impostazioni da questo laser ad altri.

### Impostazioni scanner

I laser da spettacolo funzionano muovendo un singolo fascio laser in modo estremamente rapido e accendendolo e spegnendolo per disegnare forme nell’aria. Ciò che vedi come linee, forme e immagini è in realtà il fascio che traccia percorsi più velocemente di quanto i tuoi occhi possano seguire.

Un point stream è il dato che indica al laser dove muoversi successivamente e quando il fascio deve essere acceso o spento. In Liberation, i clip vengono convertiti in questo point stream in tempo reale mentre vengono inviati ai laser.

Liberation ti dà un controllo dettagliato su come viene generato questo point stream, permettendoti di bilanciare fluidità, luminosità e prestazioni per ogni laser.

{% hint style="info" %}
Se sei abituato a software laser più vecchi basati su point stream precalcolati, questo approccio può sembrarti diverso all’inizio. Tuttavia, la generazione dei punti in tempo reale permette di ottimizzare lo stesso contenuto in modo diverso per ogni laser. Questo rende più facile lavorare con più laser che hanno velocità o qualità degli scanner diverse, senza duplicare o ricostruire i contenuti. Inoltre mantiene i file clip molto piccoli: per questo l’intero clip deck predefinito di Liberation pesa solo pochi megabyte invece di gigabyte.
{% endhint %}

Le impostazioni scanner di base sono:

* **Speed** è la velocità dello scanner, cioè quanto rapidamente il laser si muove per disegnare le forme. Equivale alla regolazione del point rate nei software laser tradizionali, ma in Liberation puoi modificare la velocità di movimento del laser _indipendentemente dal point rate._ Non dovresti aver bisogno di regolarla.
* **Scanner sync** (a volte chiamato _blank shift, precedentemente Colour Shift_) Gli scanner muovono il laser molto velocemente, ma di solito il cambiamento di luminosità e colore non è sincronizzato con il movimento. Questo si manifesta come piccole “code” di luce tremolanti ai bordi di beam e linee. Usa questa regolazione per sincronizzare movimento e colore. Vedi [laser-settings](../setting-up/laser-settings/)

Le altre impostazioni scanner avanzate sono trattate nel capitolo [advanced](../advanced/).

### Zoning

Per una guida completa alla configurazione e allo zoning dei laser, vedi: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
