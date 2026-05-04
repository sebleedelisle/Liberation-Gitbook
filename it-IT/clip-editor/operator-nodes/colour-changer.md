---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Cambio colore

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Cambio colore

Modifica i colori di tutto il contenuto in ingresso. Puoi impostare valori HSB fissi oppure passare al sistema a gradiente e campionare i colori da un gradiente personalizzato.

* **hue, saturation, brightness** - i valori del colore, vedi [Impostazioni colore e HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - la tonalità non viene modificata
  * FIXED - la tonalità degli elementi viene impostata sul valore di hue
  * SHIFT - la tonalità degli elementi viene spostata del valore indicato, quindi elementi di colori diversi resteranno diversi, ma verranno semplicemente spostati lungo il valore di tonalità.
* **saturation mode** -
  * OFF - la saturazione non viene modificata
  * FIXED - la saturazione viene fissata al valore specificato.
* **brightness mode** -
  * OFF - la luminosità non viene modificata
  * FIXED - la luminosità degli elementi viene impostata sul valore di brightness
  * MULTIPLY - la luminosità degli elementi viene combinata con il valore di brightness, quindi se stanno lampeggiando continueranno a lampeggiare, ma solo fino alla luminosità specificata qui.
* **gradient mode** - passa dagli slider HSB fissi all’editor del gradiente. Il node campiona un colore dal gradiente e poi lo applica usando le modalità di tonalità, saturazione e luminosità indicate sopra.
* **gradient position** - sceglie quale punto del gradiente viene campionato. Anima questo valore da 0% a 100% con un Sawtooth Oscillator per scorrere il gradiente nel tempo.
* **blend** - quanto viene applicato il modificatore di colore: 0% significa per niente, 100% completamente, e 50% è una combinazione tra il colore esistente e i nuovi valori.

{% hint style="info" %}
Il node Colour Change campiona un solo colore dal gradiente per tutto l’input. Se vuoi che il gradiente si distribuisca sulla forma in base alla posizione, usa invece [modificatori basati sulla posizione](position-based-changers.md "mention").
{% endhint %}

### Editor del gradiente

Quando **gradient mode** è attivo, l’editor del gradiente appare sotto i controlli principali.

* Fai clic sulla barra del gradiente per aggiungere uno stop di colore.
* Fai clic con il tasto sinistro su uno stop per selezionarlo, poi trascinalo lateralmente per spostarlo.
* Trascina uno stop selezionato verso il basso, lontano dalla barra, oppure premi Delete/Backspace, per rimuoverlo. Un gradiente mantiene sempre almeno due stop.
* Fai clic con il tasto destro su uno stop per modificarlo con il selettore colore.
* Usa **Position**, **Hue**, **Saturation** e **Brightness** per modificare con precisione lo stop selezionato.
* **interpolation** sceglie come vengono miscelati i colori tra gli stop:
* **HSB** - miscela tonalità, saturazione e luminosità. È l’opzione migliore per movimenti fluidi in stile arcobaleno intorno alla ruota dei colori.
* **RGB** - miscela direttamente i valori di rosso, verde e blu. Spesso dà una sensazione più simile a una dissolvenza colore su uno schermo o su una console luci.
* **NONE** - passa da uno stop al successivo senza miscelazione.
* **hue direction** è disponibile nell’interpolazione HSB:
* **AUTO** - segue il percorso più breve intorno alla ruota delle tonalità.
* **FORWARDS** - avanza sempre attraverso i valori di tonalità.
* **BACKWARDS** - arretra sempre attraverso i valori di tonalità.
