---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Nodi Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Crea un singolo punto / raggio.

* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **Colour** - il colore del punto. Vedi [Impostazioni colore e HSB](fundamentals/colour-settings-and-hsb.md)
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Crea una linea / lama.

* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **Size** - la lunghezza della linea
* **Colour** - il colore della linea. Vedi [Impostazioni colore e HSB](fundamentals/colour-settings-and-hsb.md)
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* **rotation** - l’angolo della linea, in gradi
* **resolution** - vedi [Resolution](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ determina il punto iniziale e il centro di rotazione della linea
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Crea un cerchio / cono.

* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **radius** - il raggio del cerchio
* **Colour** - il colore del cerchio. Vedi [Impostazioni colore e HSB](fundamentals/colour-settings-and-hsb.md)
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* **resolution** - vedi [Resolution](fundamentals/resolution.md)
* **Fill state** - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Crea un poligono equilatero: triangolo, quadrato, pentagono ecc.

* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **size** - la distanza dal centro a ciascun angolo
* **Colour** - il colore del poligono. Vedi [Impostazioni colore e HSB](fundamentals/colour-settings-and-hsb.md)
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* **rotation** - l’angolo di rotazione della forma, in gradi
* **resolution** - vedi [Resolution](fundamentals/resolution.md)
* **Fill state** - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Carica un file SVG per creare forme personalizzate.

{% hint style="warning" %}
Liberation è compatibile con il formato _SVGTiny_. InkScape è consigliato, ma la maggior parte delle app di grafica vettoriale può esportare in questo formato. Assicurati di convertire tutto il testo in forme prima dell’esportazione. Liberation esegue il rendering dei tratti e, opzionalmente, può usare i riempimenti come maschere. Assicurati che le linee non siano nere, altrimenti non saranno visibili senza un modificatore di colore.
{% endhint %}

* **Import SVG** - carica un file SVG dal disco.

{% hint style="info" %}
Una volta caricato l’SVG, il contenuto viene convertito e salvato all’interno del clip, quindi non devi mantenere un riferimento al file, a meno che in seguito tu non voglia modificare le impostazioni delle maschere.
{% endhint %}

* **Use fills as masks** - elabora qualsiasi forma riempita come maschera, cioè riempita di nero. Viene impostato automaticamente se il tuo SVG contiene forme riempite. Se non contiene forme riempite, viene disabilitato. Vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - se le forme nel tuo SVG non hanno un contorno, non possiamo disegnarle! Questa opzione aggiunge un contorno, o _stroke_, a qualsiasi forma riempita. Se il tuo SVG non contiene forme con tratto, viene impostata automaticamente. Se non contiene forme riempite, viene disabilitata.
* **Invert black lines** - se tutte le linee nel tuo SVG sono nere, non puoi vederle! Questa opzione le rende bianche. Viene impostata automaticamente se il tuo SVG contiene solo forme nere, ma viene disabilitata se non ne contiene.
* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **scale** - regola le dimensioni dell’SVG. Viene calcolato automaticamente quando l’SVG viene caricato, per assicurare che l’immagine sia visibile, ma può essere modificato manualmente in seguito.
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* **rotation** - l’angolo di rotazione dell’immagine, in gradi
* **resolution** - vedi [Resolution](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Crea un’animazione da una sequenza di file SVG.

* **Import SVG Sequence** - scegli la cartella che contiene tutti i file SVG. Nota che vengono caricati in ordine alfanumerico.

{% hint style="info" %}
Una volta caricata la sequenza SVG, il contenuto viene convertito e salvato all’interno del clip, quindi non devi mantenere un riferimento ai file, a meno che in seguito tu non voglia modificare le impostazioni delle maschere.
{% endhint %}

* **Use fills as masks** - elabora qualsiasi forma riempita come maschera, cioè riempita di nero. Viene impostato automaticamente se uno qualsiasi dei tuoi SVG contiene forme riempite. Se nessuno contiene forme riempite, viene disabilitato. Vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - se le forme nei tuoi SVG non hanno contorni, non possiamo disegnarle! Questa opzione aggiunge un contorno, o _stroke_, a qualsiasi forma riempita. Se i tuoi SVG non contengono forme con tratto, viene impostata automaticamente. Se nessuno contiene forme riempite, viene disabilitata.
* **Invert black lines** - se tutte le linee nei tuoi SVG sono nere, non puoi vederle! Questa opzione le rende bianche. Viene impostata automaticamente se i tuoi SVG contengono solo forme nere, ma viene disabilitata se non ne contengono.
* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **scale** - regola le dimensioni dell’immagine.
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* **rotation** - l’angolo di rotazione dell’immagine, in gradi
* **resolution** - vedi [Resolution](fundamentals/resolution.md)
* **speed** - la durata dell’intera animazione, in battute.
* **time per frame** - se è attivo, la durata si applica a ogni frame invece che all’intera animazione. Quindi, se _speed_ è impostato su ¼, ogni frame durerà 1 beat.
* **animation direction** -
  * _FORWARDS_ - l’animazione avanza e poi torna in loop all’inizio
  * _BACKWARDS_ - l’animazione procede all’indietro e poi torna in loop alla fine
  * _PINGPONG_ - l’animazione avanza e poi torna indietro in loop
  * _MANUAL_ - il frame corrente viene impostato con l’impostazione _position manual_
* **position manual** - imposta il frame corrente: 0% è il primo frame, 100% è l’ultimo frame. Può essere impostato manualmente o tramite un oscillatore esterno.
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Crea testo usando un font TrueType o OpenType.

* **Text** - digita qui il testo che vuoi usare
* **Font** - scegli il font che vuoi usare

{% hint style="info" %}
Per aggiungere altri font a Liberation, copia i file .ttf o .otf nella cartella data/resources/fonts.
{% endhint %}

* **Render profile** - vedi [Render profile](fundamentals/render-profile.md)
* **horizontal alignment** - scegli _LEFT_, _CENTRE_ o _RIGHT_ per selezionare l’allineamento del testo.
* **Fill state** - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - la dimensione del testo
* **colour -** vedi [Impostazioni colore e HSB](fundamentals/colour-settings-and-hsb.md)
* **x** e **y** position - vedi [Sistema di coordinate](fundamentals/co-ordinate-system.md)
* **rotation** - l’angolo di rotazione dell’immagine, in gradi
* **resolution** - vedi [Resolution](fundamentals/resolution.md)
* **reveal** - usalo per rivelare gradualmente il testo, un carattere alla volta. Quando è tra 0 e 50%, il testo appare gradualmente da sinistra a destra. Quando è tra 50% e 100%, il testo scompare da sinistra a destra. Puoi collegare un oscillatore a questo socket per creare animazioni.
* **reveal by word** - quando è attivo, _reveal_ funziona parola per parola invece che carattere per carattere.
* **countdown** - un sistema di conto alla rovescia implementato in fretta! Cambia ogni 2 beat, quindi se vuoi i secondi assicurati di essere a 120 bpm.
* **countdown start** - il numero da cui vuoi far partire il conto alla rovescia
* _MOVE TO FRONT / MOVE TO BACK_ - vedi [Riempimenti, maschere e ordinamento per profondità](fundamentals/fills-masks-and-depth-sorting.md)
