---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive-systemet er adskilt fra APC40-kontrollerne og er en måde at få MIDI-data ind og ud af Liberation på. Funktioner som at starte og stoppe clips, justere globale indstillinger, effekter og clip-parametre har alle en tilknyttet MIDI-kommando.

{% hint style="info" %}
MIDI Send/Receive-systemet blev oprindeligt bygget, før Liberation havde nogen Timeline-funktionalitet. Det var en workaround, som du kunne bruge til at optage og afspille et show i musiksoftware som Logic Pro eller Cubase.

Det giver dig direkte kontrol over clips, effekter og indstillinger, uafhængigt af visningen og Clip Deckets scroll-position. Mere systemiske live-control-funktioner som tap tempo, tildeling af zoner og arming/disarming er ikke implementeret.
{% endhint %}

### MIDI Send/Receive-indstillinger

Åbn panelet _MIDI Send/Receive_ (via menuen _View -> MIDI Send/Receive_). Du vil se, at du kan vælge _SEND, RECEIVE,_ eller _BOTH_ for afsendelse og modtagelse, samt vælge hvilke MIDI-interfaces du vil bruge.

{% hint style="danger" %}
Brug indstillingen _BOTH_ med forsigtighed. MIDI-enheder og software kan konfigureres til at sende data tilbage, som de modtager. Det kan skabe et feedback-loop af MIDI-data, og det er ikke godt!
{% endhint %}

### MIDI-mapping

Se [Standard-mapping for MIDI send/receive](../reference/midi-send-receive-default-mapping.md "mention")

Jeg planlægger at tilføje langt mere brugerdefinerbar MIDI-mapping i fremtiden, men indtil da kan du bruge apps som [BOME](https://www.bome.com/products/miditranslator) og [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) til at oversætte mellem Liberation og din egen hardware.
