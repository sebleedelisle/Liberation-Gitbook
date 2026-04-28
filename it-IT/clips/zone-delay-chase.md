---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Siamo tutti d’accordo: più laser significa più divertimento. Ma se fanno tutti esattamente la stessa cosa, ti stai perdendo molte possibilità creative.

Il sistema di zone delay è un metodo semplice ma efficace per introdurre varietà tra le zone e sfruttare davvero al meglio una configurazione multi-laser. Può anche essere usato per creare un effetto chase più tradizionale.

#### Come funziona

_Zone delay_ aggiunge un ritardo al timing della clip su ogni zona, creando una sorta di movimento a onda tra le zone.

È molto efficace applicare lo zone delay a una clip già in esecuzione: usa il controllo corrispondente sull’APC40 per regolare quantità e pattern. Vedi [apc40-reference.md](../reference/apc40-reference.md). In alternativa, puoi usare il pannello _Clip Settings_.

Impostazioni di zone delay:

* **Zone delay** - controlla la quantità di ritardo applicata a ogni zona, misurata in sessantaquattresimi.
* **Pattern** - scegli l’ordine delle zone
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Il pattern funziona in base ai numeri delle zone e presuppone che le zone siano ordinate da sinistra a destra. Per il calcolo dei pattern, Zone delay tratta le zone canvas e le zone DMX come gruppi separati.
{% endhint %}

* **Delay mode**
  1. No delay - usalo in modalità chase
  2. Delay - la modalità predefinita, ritarda il timing di ogni zona
  3. Delay with re-trigger - riporta la clip all’inizio ogni volta lungo il pattern. Funziona bene con _Chase mode_.
* **Chase mode** - con chase mode attivo, ogni zona viene accesa e spenta come in un effetto chase tradizionale. Regola l’aspetto del chase con le impostazioni _Fade in, Hold,_ e _Fade out_. Queste impostazioni sono definite come proporzione del valore di zone delay: quindi un valore di 1 corrisponde allo stesso tempo specificato in _Zone delay_. È un po’ difficile da spiegare, quindi il mio consiglio è di provarlo direttamente.

{% hint style="info" %}
Zone delay viene applicato anche a tutti gli effetti attivi. Per esempio, un effetto lampeggiante verrà ritardato tra le zone, così come l’animazione all’interno della clip stessa.
{% endhint %}

Quando una clip ha qualsiasi tipo di _Zone delay_, vedrai un’icona con tre puntini nell’angolo in alto a destra della clip. Questi puntini sono animati per mostrarti lo stile di _Zone delay_ usato da quella clip. Vedi [what-are-the-small-icons-on-the-clip-buttons.md](what-are-the-small-icons-on-the-clip-buttons.md) per maggiori dettagli.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Il simbolo con tre puntini che indica che una clip ha uno zone delay e ne mostra la modalità</p></figcaption></figure>

{% hint style="info" %}
Zone delay è un’impostazione specifica di ogni clip, non globale; fa parte della progettazione creativa della clip.
{% endhint %}
