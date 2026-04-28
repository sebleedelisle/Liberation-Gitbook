---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive kerfið er aðskilið frá APC40-stýringunum og er leið til að flytja MIDI-gögn inn í og út úr Liberation. Aðgerðir eins og að ræsa og stöðva Clip, breyta víðværum stillingum, áhrifum og færibreytum Clip-a hafa allar tengda MIDI-skipun.

{% hint style="info" %}
MIDI Send/Receive kerfið var upphaflega byggt áður en Liberation var með nokkra Timeline-virkni; þetta var hjáleið sem þú gast notað til að taka upp og spila aftur sýningu í tónlistarhugbúnaði eins og Logic Pro eða Cubase.

Það veitir þér beina stjórn á Clip-um, áhrifum og stillingum, óháð birtingu og skrunstöðu í Clip Deck. Almennari möguleikar fyrir lifandi stýringu, eins og tap tempo, úthlutun svæða og að virkja/afvirkja, eru ekki útfærðir.
{% endhint %}

### Stillingar fyrir MIDI Send/Receive

Opnaðu _MIDI Send/Receive_ spjaldið (með valmyndinni _View -> MIDI Send/Receive_). Þú sérð að þú getur valið að _SEND, RECEIVE,_ eða _BOTH_ senda og taka á móti, ásamt því að velja hvaða MIDI-tengi þú vilt nota.

{% hint style="danger" %}
Notaðu _BOTH_ stillinguna með varúð. Hægt er að stilla MIDI-tæki og hugbúnað þannig að þau sendi til baka gögn sem þau fá inn. Það getur valdið endurgjöfarlykkju af MIDI-gögnum, og það er ekki gott!
{% endhint %}

### MIDI-vörpun

Sjá [midi-send-receive-default-mapping.md](../reference/midi-send-receive-default-mapping.md)

Ég áætla að bæta við mun sveigjanlegri MIDI-vörpun í framtíðinni, en þangað til geturðu notað forrit eins og [BOME](https://www.bome.com/products/miditranslator) og [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) til að þýða á milli Liberation og sérsniðna vélbúnaðarins þíns.
