---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Modificatori basati sulla posizione

Questa famiglia di nodi modifica il contenuto in base alla posizione. Per impostazione predefinita, l’effetto viene applicato lungo un asse orizzontale, da sinistra a destra, ma puoi ruotare questo asse a qualsiasi angolo. Ogni nodo include anche una modalità _radial_, in cui l’effetto è determinato dall’angolo di ciascun punto rispetto al centro.

* **Colour Changer by Position** – applica un gradiente lungo l’asse scelto o attorno all’angolo radiale.\
  \&#xNAN;_Esempio: crea un gradiente arcobaleno che attraversa una linea, oppure usa la modalità radial su un cerchio per ottenere un effetto ruota dei colori._
* **Wave Shift by Position** – applica una distorsione a onda sinusoidale, spostando il contenuto verticalmente, o in modo perpendicolare all’asse scelto.\
  \&#xNAN;_Esempio: fai increspare una linea come acqua, oppure usa la modalità radial per far pulsare un cerchio verso l’esterno dal centro._
* **Noise Shift by Position** – applica una distorsione con rumore simplex, spostando il contenuto verticalmente, o in modo perpendicolare all’asse scelto.\
  \&#xNAN;_Esempio: vedi l’esempio di Wave Shift, ma con un carattere più organico e casuale, perfetto per aggiungere variazioni naturali._

## &#x20;Cambio colore per posizione

Questo nodo applica variazioni di colore al contenuto in base alla posizione. Per impostazione predefinita, l’asse è orizzontale (0°), ma puoi ruotarlo o passare alla modalità radial.

* **wavelength** – imposta la dimensione del ciclo colore ripetuto.
  * _Modalità lineare:_ al 100%, un ciclo completo copre l’intera larghezza del contenuto.
  * _Modalità radial:_ al 100%, un ciclo completo copre l’intero cerchio (360°). I valori sono percentuali del cerchio: ad esempio 50% = mezzo cerchio (180°).
* **offset** – sposta il punto iniziale del ciclo colore, come percentuale della wavelength. Puoi modularlo, ad esempio con un oscillatore a dente di sega, per scorrere fluidamente tra i colori.
* **repeat** – quando è attivo, il ciclo si ripete sul contenuto. Se è disattivato, il gradiente viene applicato una sola volta: tutto ciò che si trova prima dell’inizio usa il colore iniziale, tutto ciò che si trova dopo la fine usa il colore finale.
* **pingpong** – quando è attivo, ogni ripetizione alterna la direzione, creando un effetto specchiato. Se _Repeat_ è disattivato, il gradiente va in avanti e poi torna indietro una sola volta. _Nota: in modalità Pingpong la wavelength comprende sia il passaggio in avanti sia quello di ritorno._
* **linear angle** – ruota l’asse dell’effetto. 0° = orizzontale.
* **radial** – passa alla modalità radial, applicando i colori in base all’angolo rispetto al centro.
* **radial smooth loop** – regola automaticamente la wavelength in modo che divida uniformemente il 100% del cerchio, evitando una giunzione visibile nel punto in cui il ciclo ricomincia.
* **legacy mode** – torna ai vecchi slider HSB di inizio/fine. Lascialo disattivato per usare il nuovo editor del gradiente.

**Modalità colore**

Determinano quali aspetti delle regolazioni colore vengono applicati al contenuto. Vedi anche: [Impostazioni colore e HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – la hue non viene modificata.
  * _FIXED_ – la hue viene forzata a un valore fisso.
  * _SHIFTED_ – la hue viene spostata della quantità specificata: elementi con colori diversi restano distinti, ma vengono spostati insieme lungo la ruota dei colori.
* **saturation mode**
  * _OFF_ – la saturation non viene modificata.
  * _FIXED_ – la saturation viene impostata sul valore specificato.
* **brightness mode**
  * _OFF_ – la brightness non viene modificata.
  * _FIXED_ – la brightness viene impostata sul valore specificato.
  * _MULTIPLY_ – la brightness viene scalata in base al valore specificato. Questo conserva le dinamiche: ad esempio gli elementi lampeggianti continuano a lampeggiare, ma entro l’intervallo di brightness limitato.

**Editor del gradiente**

Usa lo stesso editor del gradiente di [Colour Changer](colour-changer.md "mention"), ma mappa il gradiente sul contenuto in base alla posizione.

* Fai clic sulla barra del gradiente per aggiungere uno stop di colore.
* Fai clic con il pulsante sinistro su uno stop per selezionarlo, quindi trascinalo lateralmente per spostarlo.
* Trascina uno stop selezionato verso il basso, lontano dalla barra, oppure premi Delete/Backspace, per rimuoverlo. Un gradiente mantiene sempre almeno due stop.
* Fai clic con il pulsante destro su uno stop per modificarlo con il selettore colore.
* Usa **Position**, **Hue**, **Saturation** e **Brightness** per modificare con precisione lo stop selezionato.
* **interpolation** sceglie come vengono miscelati i colori tra gli stop:
* **HSB** – miscela hue, saturation e brightness. È l’opzione migliore per movimenti fluidi in stile arcobaleno attorno alla ruota dei colori.
* **RGB** – miscela direttamente i valori di rosso, verde e blu. Spesso dà una sensazione più simile a una dissolvenza colore su uno schermo o su una console luci.
* **NONE** – passa da uno stop al successivo senza miscelazione.
* **hue direction** è disponibile con l’interpolazione HSB:
* **AUTO** – segue il percorso più breve attorno alla ruota delle hue.
* **FORWARDS** – procede sempre in avanti attraverso i valori di hue.
* **BACKWARDS** – procede sempre all’indietro attraverso i valori di hue.
* **blend** – miscela la variazione di colore con i colori originali. Al 100%, l’effetto sostituisce completamente i colori originali.

**Valori iniziali / finali legacy**

Se **legacy mode** è attivo, l’editor del gradiente viene sostituito dai controlli precedenti:

* **start hue / end hue** – hue all’inizio e alla fine dell’intervallo.
* **start saturation / end saturation** – saturation all’inizio e alla fine dell’intervallo.
* **start brightness / end brightness** – brightness all’inizio e alla fine dell’intervallo.

**Esempio 1: gradiente arcobaleno in scorrimento**

Partendo dalle impostazioni predefinite:

1. Lascia il nodo in modalità **Linear** (angolo 0° = orizzontale).
2. Lascia **wavelength** al 100%: copre l’intera larghezza e dovrebbe essere il valore predefinito.
3. Lascia il gradiente predefinito così com’è.
4. Attiva **repeat**.
5. Aggiungi un **Sawtooth Oscillator** all’impostazione **offset**, da 0% a 100%.

***

**Esempio 2: gradiente nero–bianco–nero (Pingpong)**

Partendo dalle impostazioni predefinite:

1. Lascia il nodo in modalità **Linear** (angolo 0° = orizzontale).
2. Lascia **wavelength** al 100%: copre l’intera larghezza e dovrebbe essere il valore predefinito.
3. Disattiva **repeat**.
4. Imposta il primo stop del gradiente su nero.
5. Imposta lo stop finale del gradiente su bianco.
6. Imposta **hue mode** su OFF.
7. Imposta **saturation mode** su FIXED se vuoi forzare il risultato in scala di grigi.
8. Imposta **brightness mode** su FIXED.
9. Attiva **pingpong**.

_Risultato: il gradiente sfuma da nero a bianco, poi di nuovo a nero lungo la larghezza._\
Nota che, se vuoi che il contenuto mantenga la propria hue e saturation, imposta Saturation mode su OFF. \\

***

**Esempio 3: ruota arcobaleno rotante (Radial)**

1. Attiva la modalità **radial**.
2. Imposta **wavelength** su 100%: una scansione completa di 360°.
3. Attiva **repeat**.
4. Aggiungi un **Sawtooth Oscillator** all’impostazione **offset**, da 0% a 100%.

_Risultato: una ruota dei colori continua, senza giunzioni, che ruota costantemente attorno al cerchio._

## &#x20;Spostamento a onda per posizione

Questo nodo applica al contenuto una distorsione a onda, spostando i punti in modo perpendicolare all’asse scelto, o radialmente dal centro.

* **Wavelength** – imposta la lunghezza del ciclo dell’onda.
  * _Modalità lineare:_ al 100%, un ciclo completo copre l’intera larghezza del contenuto.
  * _Modalità radial:_ al 100%, un ciclo completo copre tutti i 360°. I valori sono percentuali del cerchio: 50% = mezzo giro, 25% = un quarto di giro, ecc.
* **Size** – controlla l’ampiezza dell’onda, cioè quanto viene spostato il contenuto.
* **Offset** – sposta l’onda lungo l’asse, o attorno al cerchio in modalità radial. È una percentuale della wavelength, quindi puoi animarlo con un **Oscillator Node** per far viaggiare l’onda.
* **Radial** – passa dalla modalità lineare alla modalità radial, così lo spostamento viene calcolato in base all’angolo rispetto al centro.
* **Radial Smooth Loop** – regola la wavelength in modo che divida uniformemente il 100% del cerchio, evitando giunzioni visibili nel punto di ritorno.
* **Triangle** – cambia la forma d’onda da sinusoidale a triangolare.
* **Absolute** – usa il valore assoluto dell’onda, creando solo spostamenti verso l’alto, ripiegando il lato negativo su quello positivo.
* **Angle** – ruota l’asse dell’onda. 0° = orizzontale.

## &#x20;Spostamento con rumore per posizione

Questo nodo distorce il contenuto usando un campo di rumore, simile a una turbolenza, spostando i punti in modo perpendicolare all’asse scelto, o radialmente dal centro. Rispetto a _Wave Shift_, il risultato è più organico e casuale.

* **Detail** – controlla quanto è fine il rumore. Valori più alti producono variazioni più nette e dettagliate. Valori più bassi producono variazioni più morbide.
* **Wavelength** – imposta la scala del pattern di rumore.
  * _Modalità lineare:_ al 100%, un ciclo completo di rumore copre la larghezza del contenuto.
  * _Modalità radial:_ al 100%, un ciclo completo copre tutti i 360°.
* **Size** – controlla la quantità di spostamento, cioè l’ampiezza della distorsione del rumore.
* **Offset** – sposta il pattern di rumore lungo l’asse, o attorno al cerchio. È una percentuale della wavelength, quindi puoi animarlo con un **Oscillator Node** per far “fluire” il rumore.
* **Depth Offset** – si sposta attraverso il campo di rumore 3D, creando variazioni nel tempo. È particolarmente efficace se animato con un Oscillator Node.
* **Depth Detail** – controlla quanto è dettagliata la variazione lungo la dimensione di profondità.
* **Absolute** – usa il valore assoluto del rumore, ripiegando i valori negativi in positivi, e producendo quindi solo uno spostamento su un lato.
* **Angle** – ruota l’asse del rumore in modalità lineare. 0° = orizzontale.
* **Radial** – passa dalla modalità lineare alla modalità radial, così lo spostamento viene calcolato in base all’angolo rispetto al centro.
* **Radial Smooth Loop** – regola la wavelength in modo che divida uniformemente il 100% del cerchio, evitando giunzioni visibili in modalità radial.
