# ✅ Guida rapida

## Introduzione

Benvenuto in **Liberation**, la nuova generazione di software per laser show.

Liberation è un software moderno, potente e complesso; è costruito su basi di usabilità e affidabilità per darti la libertà di esprimere la tua creatività. È veloce, efficiente e fluido: segui questa _Guida rapida_ per iniziare subito!

### Gestire i laser

Liberation è abbastanza flessibile da permetterti di configurare i laser e visualizzarli anche senza collegare alcun laser reale. Quando sei pronto, puoi assegnare facilmente ogni Output a un laser controller.

{% hint style="info" %}
Puoi configurare e visualizzare tutti i laser che vuoi in Liberation; i livelli di licenza (Hobbyist, Pro, ecc.) limitano solo il numero di laser che puoi portare in stato _armed_. Questo significa che puoi progettare laser show con 100 laser anche con una licenza gratuita. Devi fare l’upgrade solo quando devi eseguirli davvero su laser reali.
{% endhint %}

La configurazione predefinita include 8 laser distribuiti orizzontalmente, ma puoi personalizzarla come preferisci. Probabilmente ti conviene mantenere questa impostazione mentre prendi confidenza con il software; più avanti potrai adattarla alla tua configurazione hardware. (Vedi [Configurare il progetto](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Importante: prima di portare qualsiasi laser in stato armed, assicurati di comprendere i rischi e leggi con attenzione il capitolo [Configurare i laser](../setting-up/setting-up-lasers.md).
{% endhint %}

## Panoramica del software

### Arresto di sicurezza

Ogni volta che usi i laser devi avere a portata di mano un **pulsante di arresto di emergenza hardware** (vedi [Arresto di emergenza / interblocchi](../hardware/emergency-stop-interlocks.md)); se invece vuoi portare tutto in stato disarmed senza urgenza, puoi usare il pulsante _**DISARM ALL**_, il tasto `Escape` oppure il tasto _**SESSION**_ sull’APC40. Puoi anche ridurre la Global Brightness usando lo slider sullo schermo o il fader principale dell’APC40.

### Slider e controlli

In Liberation sono presenti vari slider e controlli.

{% hint style="info" %}
Fai `Cmd / Ctrl`-click su uno slider per digitare un nuovo valore, se ti serve un controllo più preciso di quello offerto dallo slider.
{% endhint %}

### Scorciatoie da tastiera

Trovi l’elenco completo delle scorciatoie da tastiera qui: [Scorciatoie da tastiera](../reference/keyboard-shortcuts.md)

### Layout dello schermo

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Non sai a cosa serve un pulsante? Passaci sopra con il mouse per vedere una descrizione!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Nel menu trovi tutte le opzioni di importazione/esportazione dei file e i comandi per aprire i pannelli. Qui trovi anche l’opzione per autorizzare il computer con il tuo abbonamento, in _Liberation -> Authorise/Deauthorise this computer_.

#### Barra delle icone

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Qui trovi le operazioni più comuni, come portare tutti i laser in stato armed/disarmed, la Global Brightness, il test pattern e il passaggio tra 3D view, Canvas view e Output view.

### Views

La grande area in alto a sinistra dello schermo può mostrare una delle 3 views principali: **3D**, **CANVAS** e **OUTPUT**. Puoi passare da una all’altra usando i pulsanti nella barra delle icone, oppure usare il tasto `Tab` per alternare 3D view e OUTPUT view e poi continuare a scorrere uno alla volta gli Output di ogni laser.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

La 3D view mostra l’aspetto dei tuoi laser e può essere configurata in base al tuo setup. Fai click e trascina per ruotare la camera; usa la rotella del mouse per avanzare e arretrare. Trovi molte altre opzioni nel pannello _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Vedi [Visualizzatore 3D](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

La Output view serve a configurare zone e masks per ogni laser. Nota il numero molto grande nell’angolo in alto a sinistra: ti permette di capire subito su quale laser ti trovi.

Questa view rappresenta l’intero Output di questo laser e mostra dove si trova ogni zone al suo interno. Per impostazione predefinita c’è una sola zone per laser, ma puoi aggiungerne quante sono ragionevolmente pratiche; le vedrai tutte in questa view.

{% hint style="info" %}
**Che cos’è una zone?**

Una zone è uno spazio all’interno dell’Output di un laser verso cui puoi indirizzare contenuti laser. Puoi avere più di una zone per ogni laser. Il tipo più semplice di zone è una _beam_ zone, ma esistono anche _canvas_ zones e _DMX_ zones. In questa guida ci concentreremo soprattutto sulle beam zones, che di solito vengono usate per creare effetti beam atmosferici nell’aria.
{% endhint %}

Puoi selezionare il laser da modificare in uno di questi modi:

* i pulsanti numerati nella barra in alto
* premendo il tasto numerico del laser che vuoi _(tasti 1-9_ \_)\_
* il tasto `Tab`, per passare da un laser al successivo

Aggiungi un nuovo laser al setup premendo il pulsante _+_. C’è anche un pulsante _ADD LASER_ nel pannello _Laser Overview_.

Elimina un laser dal setup premendo il pulsante rosso ⊖ nel pannello _Laser Overview_.

Puoi fare zoom in avanti e indietro con la rotella del mouse; fai click e trascina in qualsiasi punto in cui non ci sia una zone per spostare la view.

Fai click su una zone per selezionarla, poi regola i suoi punti d’angolo con il mouse. Tieni premuto `Alt / Option` mentre trascini un angolo per renderlo non uniforme. Fai click destro sulla zone per vedere altre opzioni, incluso il cambio del tipo di zone.

A sinistra c’è una barra con una serie di pulsanti a icona: passa sopra un pulsante per vedere la descrizione di ciò che fa. I pulsanti qui permettono di aggiungere beam zones, canvas zones e masks. Sono disponibili anche opzioni per impostare un test pattern solo per questo laser, oltre alle impostazioni di griglia e snapping.

Per maggiori dettagli vedi [Vista Output](../output-view/).

#### Canvas

Il sistema Canvas viene usato principalmente per grafica e mapping architettonico. Puoi distribuire immagini complesse su più laser e correggere la prospettiva di ogni sezione. Vedi [Grafica e sistema Canvas](../graphics-and-the-canvas-system/).

### Controller MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Anche se è possibile controllare Liberation con mouse e tastiera, è molto meglio usare un’interfaccia di controllo MIDI APC40. Il Mark 2 è l’opzione migliore, ma funziona anche il Mark 1.

Vedi anche: [Riferimento APC40](../reference/apc40-reference.md)

Ora abbiamo implementato anche il supporto per APC Mini Mark 2 e MIDI Fighter Twister, e altri controller sono in sviluppo. Tuttavia, l’APC40 Mark 2 è la scelta migliore nella maggior parte dei casi.&#x20;

### Clips ed effetti

{% hint style="info" %}
**Che cos’è un Clip?**

Un Clip è un contenitore per qualsiasi contenuto laser in Liberation. I Clips possono contenere beams o animazioni grafiche e di solito funzionano in loop. Possono essere indirizzati a qualsiasi zone o _Canvas target area_ e vengono attivati con i pulsanti Clip dentro il Clip Deck.
{% endhint %}

#### Panoramica del Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Questa griglia è il _Clip Deck_ ed è il punto in cui vengono salvati tutti i laser Clips. È progettata per corrispondere direttamente alla griglia 8 x 5 di pulsanti del tuo APC40.

**Navigare nel Clip Deck.**

Puoi scorrere il Clip Deck a sinistra e a destra usando:

* Frecce sinistra e destra. Aggiungi `Cmd / Ctrl` per scorrere una pagina intera alla volta.
* Trackpad: swipe
* Mouse: se il tuo mouse supporta lo scroll laterale, puoi usarlo mentre il puntatore si trova sopra il Clip Deck
* Manopola di scroll dell’APC40
* Pulsanti APC40 _<- DEVICE ->_

Per aiutarti a orientarti, in alto c’è un mini visualiser del Clip Deck. Vedi anche [Clip e Clip deck](../clips/)

#### Avviare e fermare i Clips

Premi un pulsante Clip, con il mouse o con l’APC40, per avviare un Clip. Premilo di nuovo per fermarlo. Quando avvii un Clip, tutti gli altri Clips dello stesso colore si fermeranno automaticamente, a meno che tu non tenga premuto _shift_.

Alcuni Clips sono in _Flash mode_ (per impostazione predefinita, quelli rossi); in questo caso si fermano appena rilasci il pulsante Clip.

Il pulsante _STOP_ ferma tutti i Clips attualmente in esecuzione.

#### Impostare le zone di Output per il Clip

Sotto i pulsanti Clip vedrai i pulsanti zone: per impostazione predefinita, beam zones da 1 a 8 (_BEAM 1_, _BEAM 2_, ecc.). I pulsanti zone si illuminano per indicare quali zone sono assegnate al Clip attualmente selezionato.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Due righe sotto i pulsanti zone vedrai i pulsanti di flip X/Y: attivali per ribaltare il Clip in orizzontale e in verticale.

{% hint style="info" %}
Nota che queste assegnazioni delle zone e le impostazioni di flip X/Y sono collegate al Clip stesso: vengono mantenute la prossima volta che esegui quel Clip. Non sono un’impostazione globale.
{% endhint %}

Fai click destro su un Clip per modificare altre impostazioni del Clip. Vedi anche [Impostazioni Clip](../clips/clip-settings.md)

### Gruppi

Noterai che ogni Clip ha un bordo colorato: questo colore rappresenta il _gruppo_ a cui appartiene. Anche i pulsanti Clip dell’APC40 si illuminano con questo colore.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Ciano</td></tr><tr><td>Group 2</td><td>Arancione</td></tr><tr><td>Group 3</td><td>Rosso</td></tr><tr><td>Group 4</td><td>Indaco</td></tr><tr><td>Group 5</td><td>Verde</td></tr></tbody></table>

Il sistema dei gruppi è molto flessibile e ti permette di:

* mantenere attivi i Clips di un gruppo mentre attivi o disattivi i gruppi in un altro
* assegnare rapidamente zone e flip X/Y a tutti i Clips di un gruppo
* impostare il _Flash mode_ per un Clip; il Group 3 è impostato su _Flash mode_ per impostazione predefinita

I gruppi hanno anche impostazioni di transizione in/out che possono essere ereditate dai rispettivi Clips o sovrascritte.

Puoi assegnare il gruppo del Clip usando i pulsanti nel menu del click destro; oppure, con l’APC40, puoi premere il pulsante del gruppo e, _mentre lo tieni premuto_, premere i pulsanti Clip.

Modificare le impostazioni delle zone per tutti i Clips di un gruppo

Con l’APC40, premi il pulsante del gruppo, poi _mentre lo tieni ancora premuto_ usa i pulsanti zone e X/Y per attivare o disattivare le impostazioni delle zone per tutti i Clips di quel gruppo.

Vedi anche [Gruppi di Clip](../clips/groups.md)

### Effetti

Il sistema degli effetti in Liberation è un modo potente e versatile per modificare in tempo reale l’Output del Clip. I pulsanti degli effetti predefiniti 1-8 si trovano sotto i pulsanti zone.

#### Applicare un effetto

Premi un pulsante effetto per attivare o disattivare l’effetto; ancora meglio, usa gli slider 1-8 dell’APC40 per fare fade in e fade out degli effetti.

#### Parametri degli effetti

Usa i controller rotativi 1-8\* per regolare il _parametro_ di ogni effetto. In alternativa, puoi fare click destro con il mouse per regolare livello e parametro. La modifica del parametro produce risultati diversi a seconda di come è configurato l’effetto. Vedi l’elenco qui sotto per gli effetti predefiniti.

{% hint style="info" %}
I numeri piccoli che vedi sui pulsanti degli effetti si riferiscono al _livello_ e al _parametro_ dell’effetto. Il _livello_ è controllato dal fader sull’APC40, oppure puoi fare click e trascinare sul pulsante. Il parametro viene regolato con i rotativi sull’APC40, oppure puoi fare click destro per regolarlo con il mouse.
{% endhint %}

_\*I controller rotativi 1-8 si trovano lungo la parte superiore di un APC40 Mk2 e in alto a destra su un Mk1. Vedi anche:_ [Riferimento APC40](../reference/apc40-reference.md)

#### Effetti predefiniti

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**:\
   Applica un movimento caotico all’Output del Clip. Il parametro regola quantità/velocità del caos.
2. **Sine wave**:\
   Deforma tutto il contenuto lungo un’onda sinusoidale in movimento. Il parametro regola la lunghezza d’onda.
3. **Rotation**:\
   Fa ruotare tutto. Il parametro regola la velocità di rotazione.
4. **Horizontal flip**:\
   Schiaccia e allunga tutto in orizzontale. Il parametro regola la velocità.
5. **Scale**:\
   Scala ripetutamente tutto da pieno a zero. Il parametro regola la velocità.
6. **Hue**:\
   Cambia la tonalità di tutto, ma non modifica la saturazione; cioè tutto ciò che è bianco resta bianco. Il parametro regola la tonalità.
7. **Saturation and hue**:\
   Cambia la tonalità di tutto e satura completamente il colore; cioè tutto ciò che è bianco diventa del colore selezionato. Il parametro regola la tonalità.
8. **Flash**:\
   Fa lampeggiare ripetutamente la luminosità di tutto, da piena a zero. Il parametro regola la velocità del flash.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Nella riga inferiore ci sono altri 16 effetti colore, da usare per applicare valori preimpostati di tonalità e saturazione.

Nota che questi sono gli effetti predefiniti, ma possono essere modificati per fare quasi tutto ciò che vuoi.

#### Che cos’è il _“Clip attualmente selezionato”_?

Quando avvii un Clip, questo si illumina per mostrare che è attivo. Ha anche un bordo bianco che indica che è il Clip attualmente _selezionato_. Ogni volta che attivi o disattivi i pulsanti zone o regoli le impostazioni del Clip, le modifiche vengono applicate al _Clip attualmente selezionato_.

{% hint style="info" %}
Per selezionare un Clip senza attivarlo, premi il tasto `Alt / Option` prima di premere il pulsante Clip. È un buon modo per regolare le sue zone e altre impostazioni senza eseguirlo.
{% endhint %}

### Pannello Clip Settings

Usa il pannello _Clip Settings_ per modificare scala, posizione X/Y e accedere al potente sistema di ritardo delle zone.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Pannello Global Settings

Apri il pannello _Global Settings_ per regolare le impostazioni globali di Output che influenzano tutto l’Output su tutte le zone.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Attiva AUTO RESET per reimpostare automaticamente tutte le _Global settings_ ogni volta che non ci sono Clips in riproduzione.&#x20;

### Timing

Quasi tutti i laser show hanno una qualche colonna sonora musicale, quindi il sistema di timing in Liberation si basa su un tempo in battiti al minuto. Nel _Tempo Panel_ puoi vedere una rappresentazione del tempo: ogni quadrato rappresenta un beat e puoi vederli lampeggiare a tempo.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Sono disponibili diverse opzioni di sincronizzazione, incluse MIDI clock e Ableton Link. Se conosci il tempo della musica, puoi regolarlo manualmente usando lo slider sullo schermo o la manopola Tempo dell’APC40; puoi però anche restare a tempo con la musica usando il sistema _Tap Tempo_\_._\_

#### Tap Tempo

_Tap Tempo_ è un termine usato comunemente nelle app musicali e ti permette di battere il tempo seguendo il beat per impostare il tempo mentre la musica è in riproduzione. Puoi usare il pulsante sullo schermo, anche se è consigliato usare il tasto _T_ o il pulsante _Tap Tempo_ sull’APC40, o anche un foot switch se preferisci.

Premi il tasto _R_ o il pulsante _Metronome_ sull’APC40 per reimpostare il tempo all’inizio della battuta.

Premi il tasto _Y_ o ruota la manopola _Tempo_ sull’APC40 per arrotondare il tempo a un numero intero. Può essere utile per la musica elettronica, che tende ad avere un numero intero di battiti al minuto.

### Organizzare il tuo Clip Deck

Per spostare un Clip nel tuo Clip Deck, fai click e trascinalo in una nuova posizione. Mentre trascini, puoi usare i tasti freccia o la rotella/i pulsanti di scroll sull’APC40 per scorrere a sinistra e a destra.

Tieni premuto `Alt / Option` mentre trascini per creare una copia.

Fai `Alt / Option`-click su un Clip per selezionarlo senza avviarlo.

Fai `Alt / Option + Shift`-click su un Clip per fare una selezione multipla, oppure fai click e trascina fuori da un Clip per selezionare “a lazo”.&#x20;

Click e trascinamento sposteranno TUTTI i Clips selezionati.

Per eliminare uno o più Clips, trascinali fuori dal Clip Deck; comparirà un’icona del cestino. In alternativa, usa il pulsante DELETE dal menu del click destro del Clip.

### Pannello Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Il pannello _Laser Overview_ ti dà una rapida panoramica dello stato dei laser attualmente in esecuzione. Il quadrato verde a destra indica che il laser controller funziona correttamente. Se diventa arancione, ci sono drop-out occasionali; se diventa rosso, si è disconnesso. Se è grigio, non è collegato ad alcun controller.&#x20;

Il grafico al centro mostra la cronologia della durata dei frame, mentre il numero a destra è il frame rate corrente. Più il contenuto è complesso, più il frame rate sarà basso, quindi l’immagine tenderà a sfarfallare di più. Qualsiasi valore sotto circa 25 fps inizierà a sembrare un po’ tremolante.&#x20;

### Collegare i laser: pannello Controller Assignment

Fai click sul pulsante _Assign Laser Controllers_ per aprire il pannello _Controller Assignment_. Puoi accedere a questo pannello anche dalla barra dei menu, in _View -> Controller Assignment_.

Qui puoi scegliere quali Output dei laser vanno a quali laser controllers. Trascina i controllers dall’elenco a destra agli slot a sinistra. Puoi rinominare i controllers in modo che corrispondano al laser a cui sono associati, usando il pulsante con l’icona della penna.

Leggi il capitolo [Assegnazione controller](../setting-up/controller-assignment.md) per maggiori dettagli.

{% hint style="danger" %}
Prima di portare qualsiasi laser in stato armed, assicurati di leggere il capitolo [Configurare i laser](../setting-up/setting-up-lasers.md).
{% endhint %}

### Pannello Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Questo pannello mostra le impostazioni del _laser attualmente selezionato_, rappresentato dal numero in alto. Cambia il laser attualmente selezionato usando il tasto _tab_, premendo un tasto numerico, facendo click su un numero laser nel pannello _Laser Overview_ o nella _Output view_.

* **Number button** porta il laser in stato armed o disarmed; se è rosso, il laser è armed.
* **Brightness** regola la luminosità del laser indipendentemente dagli altri laser. Viene combinata con l’impostazione _Global Brightness_: se sono entrambe al 50%, il laser sarà al 25%.
* **Test Pattern** attiva un test pattern solo per questo laser, sovrascrivendo l’impostazione globale del test pattern.
* **Orientation** corregge i laser montati lateralmente o capovolti.
* **Flip Horizontal and Flip Vertical** invertono l’Output del laser. Utile per correggere l’Output su laser cablati in modo non uniforme.
* **Copy Laser Settings** apre un pannello che ti permette di copiare varie impostazioni da questo laser ad altri.

### Impostazioni scanner

I laser da spettacolo funzionano muovendo un singolo raggio laser a velocità estremamente elevata e accendendolo e spegnendolo per disegnare forme nell’aria. Quelle che vedi come linee, forme e immagini sono in realtà il raggio che traccia percorsi più velocemente di quanto i tuoi occhi possano seguire.

Un point stream è il dato che indica al laser dove muoversi dopo e quando il raggio deve essere acceso o spento. In Liberation, i Clips vengono convertiti in questo point stream in tempo reale mentre vengono inviati ai laser.

Liberation ti offre un controllo dettagliato su come viene generato questo point stream, permettendoti di bilanciare fluidità, luminosità e prestazioni per ogni laser.

{% hint style="info" %}
Se sei abituato a software laser più datati che si basano su point stream precalcolati, questo approccio potrebbe sembrarti diverso all’inizio. Tuttavia, la generazione dei punti in tempo reale permette di ottimizzare lo stesso contenuto in modo diverso per ogni laser. Questo semplifica il lavoro con più laser che hanno scanner con velocità o qualità diverse, senza duplicare o ricostruire i contenuti. Inoltre mantiene i file dei Clip molto piccoli: per questo l’intero Clip Deck predefinito di Liberation occupa solo pochi megabyte invece di gigabyte.
{% endhint %}

Le impostazioni scanner di base sono:

* **Speed** è la velocità dello scanner, cioè quanto rapidamente il laser si muove per disegnare le forme. Equivale alla regolazione del point rate nei software laser tradizionali, ma in Liberation puoi modificare la velocità con cui si muove il laser _indipendentemente dal point rate_. Non dovresti avere bisogno di regolarla.
* **Scanner sync** (a volte chiamato _blank shift_, in precedenza Colour Shift) Gli scanner muovono il laser molto rapidamente, ma di solito la variazione di luminosità e colore non è sincronizzata con il movimento. Questo si manifesta come piccole “code” di luce tremolanti ai bordi di beams e linee. Usa questa regolazione per sincronizzare movimento e colore. Vedi [Laser Settings](../setting-up/laser-settings/)

Le altre impostazioni scanner avanzate sono trattate nel capitolo [Avanzate](../advanced/).

### Zoning

Per una guida completa alla configurazione e allo zoning dei laser, vedi: [Configurare i laser](../setting-up/setting-up-lasers.md)
