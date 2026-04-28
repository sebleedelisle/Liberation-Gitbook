---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Laser e controller compatibili (DAC)

### Quali laser sono compatibili con Liberation?

Se il tuo laser ha un ingresso ILDA standard, puoi usarlo con Liberation insieme a un controller laser compatibile, come Ether Dream o Helios DAC - [vedi l’elenco completo qui sotto](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - l’opzione più economica per l’uso domestico</p></figcaption></figure>

Non ti serve un controller esterno o un ingresso ILDA se:

* Il tuo laser ha Ether Dream installato internamente, oppure;
* Hai un LaserCube di Wicked Lasers, oppure;
* Hai un’unità X-Laser con Mercury integrato, oppure;
* Hai un laser Laser Animation Sollinger con controller AVB integrato (attualmente in test solo su macOS)

{% hint style="info" %}
**Che cos’è un controller laser?**

Un controller laser, o DAC, è un dispositivo hardware che prende i dati digitali da Liberation e li converte nei segnali analogici necessari per controllare gli scanner e l’output del tuo laser. Da qui DAC: Digital to Analog Converter.

Il controller si collega al computer tramite USB o tramite una rete informatica standard; può essere un dispositivo esterno oppure essere installato all’interno del laser.

Se è esterno, lo colleghi al laser tramite la connessione ILDA. ILDA è uno standard di settore che usa un vecchio connettore “D” a 25 pin. Procurati un cavo ILDA, collega un’estremità al controller e l’altra al laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>L’output ILDA su un Ether Dream esterno</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Il pannello posteriore di un laser con le varie connessioni, incluso l’ingresso ILDA</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Un cavo ILDA standard</p></figcaption></figure>

### Quale controller è più adatto a me?

Se sei un utente domestico, oppure gestisci piccoli show con 4 laser o meno vicini al computer, i controller USB come **Helios DAC** sono l’opzione **più conveniente**.

I DAC di rete come **Ether Dream** sono la **scelta migliore per i professionisti** laser che non hanno problemi a configurare una rete e vogliono gestire un numero elevato di laser; finora tutti i grandi show con Liberation sono stati eseguiti con Ether Dream.

Se hai un **LaserCube**, non ti serve alcun controller laser separato: Liberation è compatibile con tutti i LaserCube. I modelli precedenti si collegano con un cavo USB, mentre i modelli più recenti si collegano tramite rete.

Se sei un professionista e cerchi l’opzione più semplice, valuta le unità X-Laser con Mercury integrato o i laser Laser Animation Sollinger che usano AVB.

### Controller laser compatibili

#### Ether Dream (rete)

[Ether Dream](https://ether-dream.com) è disponibile da oltre dieci anni ed è attualmente alla versione 4, anche se Liberation funziona anche con Ether Dream versione 1, 2 e 3. È estremamente affidabile.

Ti colleghi tramite una rete standard. Può essere acquistato come unità standalone oppure, soluzione ancora migliore, può essere installato direttamente all’interno dei laser.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) è la scelta migliore per chi inizia ed è più economico di Ether Dream; tuttavia, poiché si collega via USB, non è consigliato per tratte di cavo lunghe. Inoltre, potresti incontrare problemi di dati USB e driver quando colleghi più di 4 unità, soprattutto su Windows.

Ma se vuoi semplicemente gestire un paio di laser a casa, è l’opzione più economica e più semplice.

#### Mercury (integrato nelle unità X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) è il potente sistema di controllo laser DMX di X-Laser, progettato per lighting designer che vogliono gestire i laser direttamente da una console luci tradizionale. Con l’ultimo aggiornamento firmware, Mercury include anche l’**emulazione Ether Dream**, il che significa che ora funziona perfettamente con Liberation, oltre che con qualsiasi altro software che supporti Ether Dream.

#### AVB (integrato nelle unità Laser Animation Sollinger)

**AVB** è un protocollo aperto basato su rete per streaming audio e dati ad alte prestazioni e bassa latenza. Molti proiettori LaserAnimation Sollinger includono il supporto AVB direttamente nell’hardware, consentendo a Liberation di collegarsi tramite rete senza bisogno di DAC esterni. Il supporto AVB in Liberation è attualmente **solo per macOS e in fase di test**, e richiede **dispositivi di rete compatibili con AVB**. Se configurato correttamente, offre un flusso di lavoro più semplice, meno dispositivi esterni e un’affidabilità solida per gli show professionali.

#### Controller che saranno supportati in futuro:

* [IDN](http://www.ilda-digital.com) (un protocollo di rete aperto di ILDA, implementabile da qualsiasi produttore)

### Suggerimenti per il cablaggio

Per prestazioni ottimali, tieni i DAC USB vicino al computer e collegali ai laser usando cavi ILDA più lunghi. Fai però attenzione: durante lo smontaggio i cavi ILDA possono comportarsi come un uncino!

Se usi Ether Dream, puoi comunque tenerli tutti insieme e collegarli ai laser con cavi ILDA lunghi, oppure montarli vicino ai laser e usare cavi di rete più lunghi.

La configurazione ideale è avere Ether Dream, o altri controller, installati direttamente all’interno dei tuoi laser. Rob di Stanwax Laser può farlo per te nel Regno Unito.
