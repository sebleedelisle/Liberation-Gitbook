# ✅ Pannello delle impostazioni Laser output

Apri il pannello delle impostazioni _Laser output_ dal menu _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Vedrai le impostazioni del laser attualmente selezionato, che puoi cambiare:

* tramite il relativo pulsante numerico nel pannello _Laser overview_
* con un tasto numerico della tastiera: i tasti da 1 a 0 aprono i laser 1 - 10
* con il tasto `Tab` per scorrere tra i laser (`Shift + Tab` scorre all’indietro).

Nella parte superiore di questo pannello trovi:

* un pulsante numerico: cliccalo per armare/disarmare questo laser. È rosso quando il laser è armato.
* uno slider _Brightness_ solo per questo laser. Nota che questo valore viene combinato con la luminosità globale.
* toggle _Test Pattern_ e selettore del pattern. Ti permette di scegliere un test pattern specifico solo per questo laser. (Questi controlli sono replicati nella toolbar della vista Output).

### Correzione dell’orientamento / mirroring dell’output

Gli elementi successivi servono a correggere la configurazione del laser, in modo che si comporti in modo coerente in Liberation.

* **Flip horizontal / vertical** - queste opzioni ti permettono di correggere l’output del laser

{% hint style="info" %}
Non dovresti aver bisogno di modificare le impostazioni di flip horizontal / vertical, a meno che il laser non sia stato cablato in modo errato o abbia pulsanti X/Y flip sul retro non impostati correttamente. Se vuoi invertire l’output per una clip specifica, puoi farlo direttamente sulla clip.
{% endhint %}

* **Orientation** - se il laser è stato montato di lato o capovolto, puoi correggere la rotazione con questa impostazione.
* **Fine position adjustments** - può essere usato per correggere spostamenti/rotazioni molto lievi. È pensato per compensare deriva o assestamenti se un laser è rimasto acceso durante la notte o per lunghi periodi.

{% hint style="info" %}
Nota che le correzioni di orientamento / mirroring non modificano nulla nel 3D Visualiser: vanno usate per correggere l’output del laser reale in modo che corrisponda a ciò che vedi nel 3D Visualiser!
{% endhint %}

### Copy laser settings

Vedi [#copy-laser-settings](./#copy-laser-settings "mention").

### Impostazioni degli scanner

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

L’impostazione Speed determina la velocità con cui si muovono gli scanner.

{% hint style="danger" %}
Anche se le impostazioni predefinite sono piuttosto conservative, puoi comunque danneggiare gli scanner se li piloti troppo velocemente. Fai attenzione, soprattutto quando aumenti la velocità.
{% endhint %}

{% hint style="info" %}
Questa impostazione di velocità non modifica il point rate; regola invece quanto sono distanziati i punti tra loro. Per maggiori informazioni, vedi [◼️ Come Liberation genera contenuti laser](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Il fascio cambia colore e si accende e spegne mentre gli scanner lo spostano, e di solito queste due cose non sono perfettamente sincronizzate tra loro. Regola questa impostazione per riallinearle.

{% hint style="info" %}
Questa regolazione è a volte chiamata _blank shift_, ma personalmente preferisco il termine _scanner sync_: è un po’ più preciso, perché regola il timing di tutti i cambi di colore rispetto al movimento degli scanner.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>“Code” laser - Colour shift non impostato correttamente</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Niente “code” laser! Colour shift corretto!</p></figcaption></figure></div>

Se vedi piccole “code” nell’output del laser, è probabile che lo scanner sync debba essere regolato. Se le code compaiono comunque, è probabile che tu stia pilotando gli scanner/driver laser più velocemente di quanto possano gestire. Prova a ridurre la scanner speed.

#### Scanner presets

Usa questa impostazione per scegliere una configurazione scanner predefinita. L’opzione di default di solito va bene, quindi non dovresti aver bisogno di cambiarla, a meno che tu non abbia scanner particolarmente scadenti (o particolarmente buoni). Se vuoi approfondire, vedi [◼️ Preset scanner e profili di rendering](../../advanced/scanner-presets.md "mention")

#### Colour calibration

Puoi usare questo sistema per correggere la curva di luminosità e il bilanciamento del bianco del laser. Vedi [Calibrazione del colore](../../advanced/colour-calibration.md "mention")

#### Advanced settings

Non dovresti aver bisogno di modificare queste impostazioni, ma se sei curioso, vedi [◼️ Impostazioni laser avanzate](../../advanced/advanced-laser-settings.md "mention")
