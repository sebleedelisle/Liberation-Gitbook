---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Sustav MIDI Send/Receive odvojen je od kontrola APC40 i služi za slanje MIDI podataka u Liberation i primanje MIDI podataka iz njega. Funkcije kao što su pokretanje i zaustavljanje stavki Clip, podešavanje globalnih postavki, efekata i parametara Clip imaju pridruženu MIDI naredbu.

{% hint style="info" %}
Sustav MIDI Send/Receive izvorno je izrađen prije nego što je Liberation imao bilo kakvu funkcionalnost Timeline; bio je to zaobilazni način na koji ste mogli snimiti i reproducirati show u glazbenom softveru kao što su Logic Pro ili Cubase.

Omogućuje izravno upravljanje stavkama Clip, efektima i postavkama, neovisno o prikazu i položaju pomicanja u Clip Deck. Sustavnije mogućnosti upravljanja uživo, kao što su tap tempo, dodjela zones te arm/disarm, nisu implementirane.
{% endhint %}

### Postavke za MIDI Send/Receive

Otvorite panel _MIDI Send/Receive_ (preko izbornika _View -> MIDI Send/Receive_). Primijetit ćete da imate opcije za _SEND, RECEIVE,_ ili _BOTH_ slanje i primanje, kao i mogućnost odabira MIDI sučelja koja želite koristiti.

{% hint style="danger" %}
Opciju _BOTH_ koristite oprezno. MIDI uređaji i softver mogu se konfigurirati tako da šalju natrag podatke koje prime; to može uzrokovati povratnu petlju MIDI podataka, a to nije dobro!
{% endhint %}

### MIDI mapiranje

Pogledajte [Zadano mapiranje za MIDI slanje/primanje](../reference/midi-send-receive-default-mapping.md)

U budućnosti planiram dodati mnogo prilagodljivije MIDI mapiranje, ali u međuvremenu možete koristiti aplikacije kao što su [BOME](https://www.bome.com/products/miditranslator) i [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) za prevođenje između Liberation i vašeg prilagođenog hardvera.
