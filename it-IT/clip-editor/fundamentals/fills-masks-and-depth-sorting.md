---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Riempimenti, maschere e ordinamento per profondità

### Tratti, riempimenti e maschere

Noterai che alcuni nodi Creator hanno un’opzione _Fill state_; puoi disegnarli con un tratto (un contorno), come maschera (coprendo ciò che sta sotto) oppure in entrambi i modi.

Quando renderizzi una forma come maschera, è come se fosse riempita di nero e tutto ciò che si trova sotto venisse coperto.

{% hint style="info" %}
Disegnare una linea (o _stroke_) con un laser è abbastanza semplice: scansioni il laser dall’inizio della linea alla fine della linea. Ecco la tua linea!

Le forme riempite, però, sono più difficili. Se vuoi una forma riempita di colore, potresti creare manualmente un tratteggio incrociato disegnando linee e riempiendo l’area, ma Liberation non può farlo automaticamente (per ora). E anche se lo facessimo, vedresti comunque le altre linee sottostanti trasparire.

Quello che possiamo fare, però, è riempire le forme di _nero_. Sotto il cofano, Liberation esegue tutti i calcoli necessari per rimuovere il contenuto che si trova sotto la forma riempita di nero. E fidati: è una faccenda delicata!

Ma funziona molto bene e dà l’illusione di una forma riempita di nero.
{% endhint %}

### Ordinamento per profondità

Dato che alcune forme possono _coprire_ altre forme, Liberation deve ordinarle in base alla profondità. Per impostazione predefinita, gli elementi vengono ordinati per profondità in base alla loro posizione z. Se si trovano alla stessa posizione z, vengono ordinati in base alla posizione del layer, che può essere modificata usando i pulsanti _MOVE TO FRONT_ e _MOVE TO BACK_ all’interno di ciascun Creator.
