---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Questo nodo sostituisce il contenuto di linee e forme con punti distribuiti a intervalli regolari (i punti già esistenti non vengono modificati).

* **Colour** – il colore dei punti. Viene ignorato se _Inherit Colour_ è abilitato, vedi sotto. _Vedi anche_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – la distanza tra i punti, misurata in pixel. Valori più piccoli = più punti, valori più grandi = meno punti.
* **Offset** – sposta la posizione iniziale dei punti come percentuale dello spacing. Può essere animato (ad esempio con un Oscillator Node a dente di sega) per creare effetti di punti "in movimento".
* **Keep Original** – se abilitato, le linee/forme originali vengono mantenute e i punti vengono disegnati sopra.
* **Render Profile** – sceglie la qualità di rendering. _Vedi_ [render-profile.md](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – regola automaticamente lo spacing in modo che la lunghezza del percorso sia divisibile in parti uguali.
* **Fade Out Ends** – riduce gradualmente la luminosità dei punti verso l’inizio e la fine del percorso. Utile quando animi **Offset** con un Oscillator Node a dente di sega, così i punti sfumano in entrata/uscita in modo fluido mentre si spostano verso la fine della forma.

## &#x20;Trimmer

Questo nodo ritaglia la lunghezza visibile di linee e forme, permettendoti di rivelarle, nasconderle o animarle nel tempo.

* **Offset** – controlla dove inizia la parte visibile della forma. Anche con _Trim Size_ allo 0%, animando Offset da 0% → 100% la forma viene disegnata, diventa completamente visibile al 50%, poi scompare di nuovo.
* **Trim Size** – imposta quanta parte della forma viene mantenuta, come percentuale della sua lunghezza totale.
* **Loop** – tratta la forma come un loop continuo, quindi la fine si collega di nuovo all’inizio invece di scomparire.
* **All Shapes** – combina tutte le forme in ingresso e le ritaglia come se fossero un unico percorso. Se disattivato, ogni forma viene ritagliata singolarmente.
* **Add Dot at Start / Add Dot at End** – aggiunge un punto del colore scelto nei punti di ritaglio. (Se non viene applicato alcun ritaglio, non viene aggiunto alcun punto.)
* **Colour** – il colore dei punti di ritaglio. _Vedi anche_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – sceglie il render profile per i punti. _Vedi_ [render-profile.md](../fundamentals/render-profile.md)
