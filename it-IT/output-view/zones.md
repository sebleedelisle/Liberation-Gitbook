---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zone

Il tipo principale di zona che userai nella maggior parte dei progetti è la _Beam zone_. È una zona pensata per effetti beam atmosferici attraverso l’aria. L’altro tipo di zona è una _Canvas zone_ (vedi [Grafica e sistema Canvas](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**ATTENZIONE - Usa la massima cautela quando sposti le zone mentre il laser è in funzione** e abbassa la luminosità al minimo possibile. Vedi [Panoramica del processo di configurazione dei laser](../setting-up/setting-up-lasers.md "mention") per una guida completa su come attivare e configurare le zone dei laser in sicurezza
{% endhint %}

Puoi fare clic sulle zone e trascinarle con il mouse. Attiva un pattern di test per vedere dove viene proiettata la zona.

{% hint style="info" %}
Usa i tasti freccia per **spostare leggermente** la zona/il punto attualmente selezionato. Premi il tasto `Shift` per spostarti con passi più grandi.
{% endhint %}

{% hint style="info" %}
Suggerimento: puoi copiare rapidamente le impostazioni delle zone su più laser! Vedi [Copiare le impostazioni tra laser](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Aggiungere una nuova beam zone

Fai clic sul pulsante _Add a new beam zone_ nella parte superiore della toolbar e apparirà una nuova zona. Nota che le beam zone vengono ordinate in base all’ordine in cui le aggiungi, ma puoi riordinarle. Vedi [Riordinare le zone beam](re-ordering-beam-zones.md "mention")

### Aggiungere una canvas zone esistente

Fai clic sul pulsante _Add existing canvas zone_ e vedrai un elenco delle canvas zone disponibili, che puoi attivare o disattivare per questo laser. Vedi [Grafica e sistema Canvas](../graphics-and-the-canvas-system/ "mention")

### Tipi di forma della zona

Ci sono 3 tipi di forma per le zone:

* **Quad** - la forma rettangolare predefinita della zona, che può essere uniforme (allineata agli assi) o distorta. Ideale per zone rettangolari più grandi o per canvas zone che richiedono correzione prospettica.
* **Line/Curve** - una zona definita da 2 o più punti e da uno spessore. Ideale per zone sottili o per terminare su balconate, ponti o altre forme curve.
* **Segmented** - una zona che può essere suddivisa in quad più piccoli. Ideale per il mapping architetturale.

Fai clic destro su qualsiasi zone per aprire le sue impostazioni. Da questo menu contestuale puoi:

* Rinominare la zona (può essere utile per identificarla nel Clip Deck, soprattutto se hai molte zone!)
* Abilitare/disabilitare la zona
* Bloccarne la posizione
* Cambiarne il tipo di forma
* Ripristinarla alla posizione predefinita
* Accedere alle impostazioni specifiche del tipo di forma
* Eliminarla
* Aggiungere una _Alt Zone_ (vedi [Sistema Alt zone](alt-zone-system.md "mention"))

{% hint style="danger" %}
**ATTENZIONE -** fai molta attenzione quando cambi il tipo di zona mentre il laser è attivo. La zona tornerà all’ultima posizione/dimensione usata per quella forma, quindi l’output potrebbe cambiare all’improvviso. È meglio spegnere il laser prima di cambiare il tipo di zona.
{% endhint %}

### Forma zona Quad

Puoi spostare ogni angolo del quad con il mouse. Fai `Alt / Option`-clic su un angolo per spostarlo indipendentemente dagli altri e distorcere il quad. Una volta distorto il quad, tutti gli angoli possono muoversi liberamente.

Puoi rimuovere la distorsione e riportarlo a un rettangolo allineato agli assi usando il pulsante _REMOVE DISTORTION_ nel menu contestuale.

#### Correzione prospettica

Questa opzione può essere impostata con il toggle button nel menu contestuale e determina il metodo di distorsione. Per i beam è meglio lasciarla disattivata, ma se questa zone proietta grafiche su un piano piatto, attivala e l’output verrà corretto prospetticamente.

{% hint style="info" %}
Se _Perspective correction_ è disattivata, il contenuto viene distorto usando _bi-linear interpolation_. In altre parole, il contenuto viene distribuito in modo uniforme sul quad. Ecco perché è la scelta migliore per i beam.

Con la correzione prospettica attivata, il contenuto viene distorto usando un warping prospettico che compensa lo scorcio. Quindi, se stai proiettando grafiche su una parete con un angolo obliquo, puoi usarla per raddrizzare l’output e correggere la distorsione della proiezione.
{% endhint %}

### Forma zona Line / Curve

La forma zona Line / Curve è diventata la mia opzione preferita negli show recenti, e si potrebbe anche sostenere che dovrebbe essere il valore predefinito per le beam zone.

Molto spesso le mie zone devono essere sottili per adattarsi a spazi stretti e scomodi nelle venue o tra le finestre degli edifici, e mi sono accorto che regolare i quattro angoli di un quad quando sono così vicini tra loro può essere davvero macchinoso. Così è nata la zona Line / Curve!

Per le linee dritte ti bastano due punti, poi regoli _Zone thickness_ nel menu contestuale. È il modo più veloce per creare zone semplici.

Fai `Alt / Option`-clic sulla linea per creare punti aggiuntivi. Questi punti vengono smussati automaticamente per creare una forma fluida, e puoi regolare _Smooth level_ per eliminare eventuali irregolarità.

Fai `Alt / Option`-clic su un punto per eliminarlo.

Oppure, se hai esperienza con app di grafica vettoriale (Inkscape, Illustrator ecc.), puoi usare l’opzione _Manually adjust bezier curves_ per ottenere una regolazione fine di tutti i punti di controllo.

### Forma zona Segmented

Questa zone suddivisa ti permette di apportare correzioni estremamente dettagliate ed è utile quando fai mapping su forme complesse. Puoi aggiungere o rimuovere suddivisioni usando i pulsanti + e - nel menu contestuale.

### Come modificare una zona completamente coperta da un’altra zona

Fai clic destro sulla zone in primo piano e fai clic sul pulsante con il lucchetto per bloccarla. A questo punto dovresti riuscire a modificare e regolare la zone sottostante.

<br>

{% hint style="info" %}
Una volta aggiunta una Beam zone al tuo output, sarà disponibile per essere aggiunta a una clip nel Clip Deck.
{% endhint %}
