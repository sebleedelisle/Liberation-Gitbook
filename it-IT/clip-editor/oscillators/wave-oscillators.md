---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Oscillatori a onda

## In questa pagina :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Onda sawtooth](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Onda triangle](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Onda sine](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Onda square](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Impostazioni degli oscillatori a onda

Tutti gli oscillatori a onda hanno le seguenti impostazioni :

* **range min / range max** - determina l’intervallo di valori per la proprietà controllata dall’oscillatore. La proprietà viene impostata su _range min_ quando la forma d’onda è al minimo, e su _range max_ quando la forma d’onda è al massimo.

{% hint style="info" %}
Ad esempio, se vuoi far muovere un punto a sinistra e a destra tra -100 e 100, devi collegare l’oscillatore alla _x property socket_, impostare _min range_ su -100 e _max range_ su 100.
{% endhint %}

* **duration** - il tempo necessario per completare un ciclo completo, o _loop_. È relativo al tempo musicale in battute. Quindi ¼ corrisponde a un singolo beat. 1 corrisponde a una battuta completa, e così via.
* **duration multiplier** - moltiplica la durata di base per un fattore scelto. Ad esempio, se duration è impostato su una semiminima e il moltiplicatore è 3, l’oscillatore durerà tre semiminime, cioè una minima puntata. Sono supportati anche moltiplicatori frazionari: tieni premuto _SHIFT_ mentre trascini lo slider per impostare numeri non interi, utile per effetti di phasing o per creare leggere variazioni di timing.
* **offset** - lo scostamento iniziale dell’onda, espresso come percentuale della durata. Se vuoi che l’onda inizi a un quarto del percorso, impostalo su 25%.
* **repeat count** - il numero di volte in cui il loop viene eseguito prima di fermarsi. Il valore predefinito è _FOREVER_, ma puoi cambiarlo se non vuoi che l’oscillatore continui all’infinito. Dopo l’arresto, la proprietà verrà impostata sul valore alla fine dell’onda.
* **delay count** - il ritardo in beat prima che l’oscillatore inizi a funzionare. Prima dell’avvio, la proprietà verrà impostata sul valore all’inizio dell’onda.

{% hint style="info" %}
Usando con attenzione _repeat count_ e _delay count_ puoi creare animazioni molto complesse, quasi come se fosse una timeline dedicata!
{% endhint %}

## Impostazioni comuni

* **steps** - divide il movimento in un numero di passaggi discreti. Utile quando vuoi che le proprietà “saltino” da un valore all’altro invece di muoversi in modo fluido.

{% hint style="info" %}
Tieni presente che gli step sono divisi in base al tempo, non al valore. Quindi, per un’onda divisa in 4 step con una durata di 1 battuta, la proprietà cambierà istantaneamente a ogni beat.
{% endhint %}

* **clamp min / clamp max -** aumenta la scala dell’onda oltre i suoi valori minimi o massimi e limita il risultato.

{% hint style="info" %}
Il concetto di _clamp_ è abbastanza difficile da spiegare, ma immagina la forma d’onda che supera il bordo superiore o inferiore del grafico e poi viene bloccata sui margini. Ti consiglio di sperimentare con questi valori! Sono però molto utili se vuoi che una sawtooth inizi in ritardo o finisca in anticipo.
{% endhint %}

* **ease function** - anche le onde Sawtooth e Triangle hanno una ease function, che modifica leggermente la curva dell’animazione e può rendere le tue animazioni molto più espressive!
  * **LINEAR** - il valore predefinito, senza easing: si muove semplicemente in modo lineare tra i valori minimo e massimo.
* **EASE OUT** - parte velocemente e poi rallenta avvicinandosi alla fine. Molto utile per simulare la fisica, ad esempio un rallentamento fino all’arresto.
  * **EASE IN** - parte lentamente e accelera gradualmente. Utile per simulare un accumulo di slancio.
  * **EASE IN/OUT** - una combinazione delle due precedenti, con un movimento molto organico.

{% hint style="warning" %}
**Easing -** ti consiglio di evitare l’animazione lineare predefinita ogni volta che puoi, a meno che tu non voglia ottenere un effetto volutamente robotico. L’easing può rendere le animazioni molto più fluide e naturali!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Onda sawtooth

A volte è chiamata anche _ramp waveform_, perché sale progressivamente e poi scende bruscamente alla fine del ciclo. Probabilmente è l’oscillatore a onda più comune, perché crea un loop adatto a proprietà cicliche come _hue_ o _rotation._

Vedi le sezioni precedenti per :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Specifico per Sawtooth :

* **cycle range compensation** - disponibile quando **steps** è impostato, ed è utile per valori ciclici, ad esempio una rotazione da 0 a 360. Quando non è attivo, il valore iniziale e quello finale saranno uguali, e questo può causare un blocco sul punto di partenza, perché 0 e 360 sono lo stesso angolo. Attivalo e l’intervallo massimo verrà ridotto per correggere le posizioni degli step.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Onda triangle

A differenza della _sawtooth wave_, che salta di nuovo all’inizio a ogni ciclo, la _triangle wave_ si muove linearmente in avanti e poi all’indietro.

Vedi le sezioni precedenti per :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Onda sine

La forma d’onda più fluida! Oscilla dolcemente tra due valori, come un pendolo.

Vedi le sezioni precedenti per :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Onda square

La forma d’onda più semplice: passa semplicemente da un valore all’altro, avanti e indietro!

Vedi le sezioni precedenti per :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Specifico per Square wave :

* **pulse width** - il tempo durante il quale l’onda resta al valore massimo, relativo alla durata complessiva. 50% è il valore predefinito, esattamente metà e metà. Se vuoi che resti “on” solo per un quarto del tempo, impostalo su 25%. Puoi regolare quando avviene questo impulso usando il valore _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Uno dei punti di forza di Liberation è la possibilità di generare effetti casuali ma ripetibili. L’oscillatore _noise_ può essere usato per creare un movimento casuale organico in loop, con tutto il dettaglio o jitter che desideri.

Vedi le sezioni precedenti per :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Specifico per Noise :

* **noise type** - l’algoritmo usato per generare il noise.
  * **SIMPLEX** - il valore predefinito: un valore ondulato che cresce e cala, e si ripete in loop.
  * **RANDOM** - usa un algoritmo di numeri casuali più tradizionale, completamente rumoroso e caotico.

{% hint style="info" %}
**Simplex noise** è stato progettato da Ken Perlin nel 2001 come miglioramento del suo algoritmo “Perlin noise”, sviluppato nel 1983 come parte del suo lavoro sul film _Tron_ (per il quale ha vinto un Oscar!)

Questo cosiddetto noise “a gradiente” è nato dalla sua frustrazione verso immagini generate al computer che in precedenza risultavano troppo “meccaniche”. Nel mondo della CGI è particolarmente adatto per renderizzare nuvole, superfici d’acqua o persino height-map per terreni realistici.

In Liberation, invece, è utile per ottenere movimenti apparentemente imprevedibili ma comunque fluidi e organici.
{% endhint %}

* **seed** - il valore usato per creare il noise. Se non ti piace l’aspetto dell’onda di noise che hai ottenuto, prova a cambiare questo valore.

{% hint style="info" %}
Curiosità da nerd! Per ottenere un simplex noise perfettamente in loop, sto iterando lungo un cerchio su un piano di noise 2D. Cambiare il valore seed sposta questo piano attraverso una terza dimensione!
{% endhint %}

* **simplex detail** - modifica quanto il noise è dettagliato o instabile. Se vuoi che il pattern ripetuto sia meno evidente, aumenta la durata e incrementa questo valore.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Crea forme d’onda completamente personalizzate. È molto utile per creare animazioni complesse.

Vedi le sezioni precedenti per :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Sotto sono presenti un elenco di posizioni e valori. La durata è divisa in 64 step e puoi inserire un valore in uno qualsiasi di questi punti.

Ogni step ha le seguenti impostazioni :

* **Step** - lo step temporale all’interno della durata. 0 è all’inizio e 64 è alla fine.
* **Level** - il livello dell’onda in quello step temporale. Il livello varia tra 0 e 1.
* **Animation type** - il menu a discesa ti permette di scegliere come vuoi arrivare a questo livello partendo dallo step precedente.
  * **None** - nessuna transizione: salta direttamente a questo livello nel momento specificato.
  * **Linear** - un movimento completamente lineare dal livello precedente a questo.
  * **Ease in / Ease out / Ease in/out** - applica easing tra il livello precedente e questo. Vedi _ease function_ sopra per una descrizione dei tipi di animazione.

***
