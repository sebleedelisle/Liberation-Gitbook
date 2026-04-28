---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Specifiche degli scanner e Liberation

### La realtà complicata delle specifiche degli scanner

Le frequenze dei punti e le specifiche degli scanner possono creare un po’ di confusione. Spesso vedrai specifiche come 30kpps @ 8º o 50kpps @ 4º, ma non è sempre chiaro cosa rappresentino davvero quei numeri.

{% hint style="info" %}
Nota - Non sono uno specialista hardware di scanner, ma ho anni di esperienza pratica nel far rendere bene scanner di qualità molto diverse usando software e generazione del flusso di punti, invece della taratura hardware. Quanto segue si basa su quell’esperienza.
{% endhint %}

#### **Da dove arrivano questi numeri**

Termini come “30K” e “50K” sono abbreviazioni basate sul modo in cui gli scanner vengono valutati usando l’ILDA test pattern a quelle frequenze di punti, in condizioni specifiche.

Quando uno scanner viene indicato come qualcosa tipo: _30Kpps @ 8°_ in realtà significa:

> “Questo scanner può riprodurre l’ILDA test pattern a 30.000 punti/sec con un angolo di scansione di 8°, se tarato correttamente.”

Non è una misura completa o pienamente standardizzata delle prestazioni nel mondo reale. In realtà, in origine non era stato pensato come benchmark: veniva usato per una **procedura di taratura**. Esegui un pattern noto a una frequenza di punti fissa (ad es. 30.000 punti/sec) e regoli damping e gain finché l’immagine non appare corretta.

Resta comunque il riferimento più usato che abbiamo, e può darti una buona idea della qualità degli scanner, almeno con produttori affidabili. Con quelli _meno affidabili_, però...

#### Se vuoi testare gli scanner secondo le specifiche dichiarate

{% hint style="danger" %}
**Questa è una tecnica avanzata e puoi danneggiare gli scanner se non fai attenzione. Non è consigliata a meno che tu sappia cosa stai facendo.**
{% endhint %}

Dovrai trovare un software in grado di generare l’[ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) - credo che LaserShowGen possa farlo - e regolare la dimensione dell’output in modo che corrisponda all’angolo di scansione specificato (ad es. 8°). Consulta la documentazione ILDA per indicazioni su come analizzare l’output.

#### Perché potrebbe non essere un buon benchmark

Prima di tutto, il tuo test pattern potrebbe apparire in modo errato anche se gli scanner sono buoni, semplicemente perché non sono tarati in modo ottimizzato per quel test.

Può essere una guida generale utile per distinguere scanner “buoni” da scanner “cattivi”, ma a volte i produttori trattano queste specifiche in modo piuttosto libero.

#### Quindi come scelgo un buon scanner?

Direi innanzitutto di assicurarti che siano prodotti da un’azienda affidabile. I produttori di scanner costosi di fascia alta come Cambridge Technology (CT), Eye Magic (EMS) e ScannerMAX (una controllata di Pangolin) sono sempre validi, e con loro vai sul sicuro. Però quando una coppia di scanner costa intorno ai 1000 $, per molti di noi agli inizi è più dei nostri laser!

Quindi per lo più ho usato produttori cinesi. Gli scanner Dragon Tiger (DT) sono discreti e accessibili, e credo che LightSpace li utilizzi. Anche molti altri produttori (inclusi OPT e Able in alcuni modelli) usano sistemi basati su DT.

Phenix Technology (PT) in genere è una fascia più bassa, ma onestamente probabilmente va bene per la maggior parte degli utilizzi.

**Se i tuoi scanner non hanno marchio, è probabilmente il caso in cui dovresti preoccuparti della qualità!**

#### Come aiuta Liberation

Prima di tutto, per la maggior parte delle cose non ti servono scanner davvero costosi! Scanner DT da 30kpps, o persino PT, andranno bene. Le impostazioni predefinite degli scanner sono volutamente conservative e, nella maggior parte dei casi, _non dovresti aver bisogno di modificarle_ (a parte _Scanner sync_).

Anche se hai scanner migliori, non ha senso spingerli più del necessario. Questo ne allungherà significativamente la vita utile.

#### Cos’è un "point stream"?

Probabilmente hai già sentito questo termine: è il modo in cui controlliamo il percorso degli scanner.

Un point stream è un elenco di posizioni X/Y, ciascuna con un colore. Per disegnare qualcosa come una linea bianca, invii una sequenza di punti lungo quella linea, tutti impostati su bianco. Gli scanner poi si muovono da un punto all’altro a una frequenza fissa - la frequenza di punti al secondo (PPS) - e il raggio traccia la forma.

#### Come funziona nel software laser tradizionale

Il software laser tradizionale memorizza un point stream per ogni cue. Per le cue animate, di solito questo significa un point stream separato per ogni frame. Il punto importante è che tutto è completamente predeterminato. Di conseguenza, aumentare la frequenza dei punti fa muovere gli scanner più velocemente attraverso gli stessi dati predefiniti.

{% hint style="info" %}
Per i software più vecchi questo approccio era necessario: i computer semplicemente non erano abbastanza veloci da generare point stream in tempo reale. Per questo di solito esiste un editor di cue separato, usato per pre-generare i dati di ogni frame dell’animazione.

Questo spiega anche perché i contenuti possono occupare gigabyte di spazio. Di fatto stai memorizzando grandi forme d’onda non compresse a frequenze di campionamento piuttosto elevate.
{% endhint %}

#### Perché "point rate" ha meno significato in Liberation

Liberation genera il point stream in tempo reale, e questo ci dà un’enorme flessibilità. Nota l’impostazione "Scanner speed" nel pannello Laser Settings. Questa ci permette di accelerare e rallentare gli scanner, ma soprattutto **non** cambia la frequenza dei punti sottostante (PPS).

#### Aspetta, cosa? Come?

Lo so, all’inizio sembra strano.

Poiché Liberation genera il point stream in tempo reale, può modificarlo. Più i punti sono distanziati, più velocemente si muovono gli scanner. Più sono ravvicinati, più lentamente si muovono gli scanner.

{% hint style="info" %}
Nelle versioni recenti di Liberation, il _point rate_ effettivo (nelle impostazioni avanzate) non influisce affatto sulla velocità degli scanner. Il renderer invece regola la distribuzione dei punti per corrispondere al point rate selezionato, mantenendo invariato il movimento degli scanner.

Questo ha un effetto sulla "risoluzione" del percorso dei punti, ma fa differenza soprattutto per la grafica (e può aiutare con una regolazione più precisa dell’impostazione _scanner sync_).
{% endhint %}

#### Perfetto! Quindi cosa significa tutto questo, in pratica?

Ottima domanda. Ecco i miei consigli:

* Evita scanner senza marchio. Se puoi prendere scanner più veloci, fallo - minimo 30KPPS.
* Nella maggior parte dei casi, gli scanner DT30 vanno bene, e gli scanner PT30 sono probabilmente OK nei laser più economici.
* Se fai grafica, nella maggior parte dei casi più laser saranno meglio di scanner più veloci.
* Quando arrivi a setup di fascia più alta, qualunque marchio high-end affermato andrà bene.
* Se puoi prendere solo gli scanner senza marchio più economici, le impostazioni predefinite di Liberation sono abbastanza conservative e probabilmente otterrai risultati OK per beam work di base. Se fanno fatica, riduci l’impostazione **Speed** (ma non cambiare il point rate!).

#### E l’ILDA Test Pattern?

…è ancora molto utile come strumento di calibrazione e riferimento, ma non è mai stato progettato come benchmark completo e può essere usato in modo improprio o interpretato con una certa libertà dai produttori.
