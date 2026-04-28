---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Impostazioni delle clip

### Pannello Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Il pannello Clip settings</p></figcaption></figure>

Modifica la dimensione di output della clip con _Scale X_ e _Scale Y_. Sono collegati tra loro, a meno che tu non tenga premuto il tasto _SHIFT_.

Modifica la posizione orizzontale e verticale della clip con _Shift X_ e _Shift Y_.

_Zone Delay/Chase_ è una funzione così divertente che ha una sezione tutta sua. [zone-delay-chase.md](zone-delay-chase.md)

### Bloccare le clip

Se una clip è bloccata, non può essere spostata o eliminata. Per bloccare una clip, usa la casella _Locked_ nel menu del clic destro. Nel pannello Clip settings trovi alcune opzioni aggiuntive.

* _UNLOCK ALL -_ sblocca tutte le clip nel Clip Deck.
* _AUTO-LOCK_ - quando _Auto-Lock_ è attivo, qualsiasi clip riprodotta automaticamente (tramite la timeline o il sistema di registrazione/riproduzione MIDI) verrà bloccata. È utile se hai programmato uno show in Logic Pro (o simili) e non vuoi modificare accidentalmente le clip usate nello show.
* _LOCKED CLIPS ZONES_ - se è attivo, non puoi modificare le zone di nessuna clip bloccata.
* _LOCKED CLIPS PARAMS_ - se è attivo, non puoi modificare i parametri (scale, shift ecc.) di nessuna clip bloccata.

### Menu del clic destro

Se fai clic destro su una clip, appare un menu con alcune opzioni relative a quella clip. Vedi [clip-editor-intro.md](../clip-editor/clip-editor-intro.md), [clip-settings.md](clip-settings.md) e [groups.md](groups.md) per maggiori informazioni sulle prime voci di questo menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Il menu del clic destro delle impostazioni clip</p></figcaption></figure>

### Retrigger

Per impostazione predefinita, le clip sono impostate su _retrigger_. Questo significa che, indipendentemente da quando la premi, la clip inizierà a essere riprodotta da quel momento. Quindi, se la avvii in ritardo, l’animazione della clip sarà leggermente in ritardo e fuori tempo.

{% hint style="info" %}
Se usi _Tap Tempo_ mentre una clip con retrigger è in esecuzione, il sistema “quantizzerà” la clip per metterla a tempo, anche se non l’hai avviata esattamente sul beat.
{% endhint %}

Se _Retrigger_ non è abilitato, la clip sarà sempre a tempo: è come se la clip fosse stata avviata proprio all’inizio del clock. È una buona scelta quando sei perfettamente sincronizzato con la musica tramite un segnale di clock esterno.

{% hint style="info" %}
Le clip sono spesso progettate per andare in loop all’infinito, ma puoi crearle in modo che vengano riprodotte una sola volta o solo per pochi cicli. Assicurati di lasciarle impostate su _retrigger_, altrimenti non ripartiranno!
{% endhint %}

### Tempo di transizione in/out (fade)

Le clip possono essere impostate per entrare e uscire con un fade, con una durata misurata in secondi. Per impostazione predefinita, il tempo di fade viene ereditato dalle impostazioni del gruppo (e può essere modificato facendo clic destro sul pulsante del gruppo).

Se vuoi una durata di fade diversa da quella del gruppo della clip, prima disattiva il pulsante _USE GROUP DEFAULT_, poi regola gli slider _In time_ e _Out time_ della clip.
