---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

In ogni nodo _Creator_ è presente un’impostazione _Render Profile_, che determina come le forme vengono disegnate (o _rendered)_ con i laser.

**Per la maggior parte degli utilizzi, l’impostazione&#x20;**_**DEFAULT**_**&#x20;va benissimo**. Ma se lavori con elementi grafici o contenuti complessi, potresti volere un controllo maggiore su come viene renderizzata ogni forma.

{% hint style="info" %}
A differenza della maggior parte dei software laser, Liberation genera uno stream di punti in tempo reale, appena prima di inviarlo ai controller laser. Questo ti fa risparmiare molto spazio su disco: le clip occupano solo pochi kB, invece dei MB richiesti dagli stream di punti pre-renderizzati.

Significa anche che puoi ottimizzare lo stesso contenuto per diversi tipi di scanner, laser per laser, senza dover modificare le clip.

Per maggiori dettagli, vedi [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Sono disponibili tre _Render Profiles_ preimpostati: _DEFAULT_, _FAST_ e _DETAIL._

_**DEFAULT**_ - un buon profilo generico, ideale per la maggior parte dei casi

_**FAST** -_ se la tua clip contiene molti elementi e alcuni sono semplicemente punti o linee dritte, potresti ottenere meno flicker scegliendo questa opzione.

_**DETAIL**_ - se stai disegnando qualcosa che richiede angoli netti, usa questa opzione. Tieni però presente che gli scanner si muoveranno più lentamente, rendendo l’output più soggetto a flicker.

{% hint style="info" %}
Nel clip editor puoi assegnare i creator a diversi render profile, ma ogni laser elaborerà questi profili in base alle proprie impostazioni dello scanner. Vedi [scanner-presets.md](../../advanced/scanner-presets.md)
{% endhint %}
