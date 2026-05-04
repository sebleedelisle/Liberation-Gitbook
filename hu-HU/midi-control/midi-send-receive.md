---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

A MIDI Send/Receive rendszer elkülönül az APC40 vezérlőktől, és arra szolgál, hogy MIDI-adatokat küldj be a Liberationbe, illetve küldj ki belőle. Az olyan funkciókhoz, mint a klipek indítása és leállítása, a globális beállítások módosítása, az effektek és a klipparaméterek vezérlése, mind tartozik egy MIDI-parancs.

{% hint style="info" %}
A MIDI Send/Receive rendszer eredetileg még azelőtt készült, hogy a Liberation rendelkezett volna Timeline funkcióval; kerülőmegoldásként szolgált arra, hogy egy show-t felvehess és visszajátszhass zenei szoftverekben, például Logic Próban vagy Cubase-ben.

Közvetlen vezérlést ad a klipek, effektek és beállítások felett, függetlenül a megjelenítéstől és a Clip Deck görgetési pozíciójától. Az olyan átfogóbb élő vezérlési lehetőségek, mint a tap tempo, a zónák hozzárendelése, valamint az élesítés/hatástalanítás, nincsenek megvalósítva.
{% endhint %}

### MIDI Send/Receive beállítások

Nyisd meg a _MIDI Send/Receive_ panelt (a _View -> MIDI Send/Receive_ menüből). Láthatod, hogy választhatsz a _SEND, RECEIVE,_ vagy _BOTH_ küldési és fogadási módok közül, valamint kiválaszthatod, mely MIDI-interfészeket szeretnéd használni.

{% hint style="danger" %}
A _BOTH_ beállítást körültekintően használd. A MIDI-eszközök és szoftverek beállíthatók úgy, hogy visszaküldjék a beérkező adatokat; ez MIDI-adat visszacsatolási hurkot okozhat, ami nem kívánatos.
{% endhint %}

### MIDI-kiosztás

Lásd: [MIDI küldés/fogadás alapértelmezett leképezése](../reference/midi-send-receive-default-mapping.md "mention")

A jövőben sokkal jobban testreszabható MIDI-kiosztást tervezek hozzáadni, de addig is használhatsz olyan alkalmazásokat, mint a [BOME](https://www.bome.com/products/miditranslator) és a [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en), hogy fordítsanak a Liberation és az egyedi hardvered között.
