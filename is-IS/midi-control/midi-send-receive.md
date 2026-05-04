---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive-kerfið er aðskilið frá APC40-stýringunum og er leið til að flytja MIDI-gögn inn í og út úr Liberation. Aðgerðir eins og að ræsa og stöðva Clips, breyta almennum stillingum, effects og Clip-breytum hafa allar tengda MIDI-skipun.

{% hint style="info" %}
MIDI Send/Receive-kerfið var upphaflega smíðað áður en Liberation var með Timeline-virkni; það var bráðabirgðalausn sem þú gast notað til að taka upp og spila sýningu í tónlistarforritum eins og Logic Pro eða Cubase.

Það veitir þér beina stjórn á Clips, effects og stillingum, óháð skjá og flettistöðu í Clip Deck. Kerfisbundnari möguleikar fyrir lifandi stjórn, eins og tap tempo, úthlutun á zones og að nota arm/disarm, eru ekki útfærðir.
{% endhint %}

### Stillingar fyrir MIDI Send/Receive

Opnaðu _MIDI Send/Receive_ panel (með valmyndinni _View -> MIDI Send/Receive_). Þú sérð að þú getur valið _SEND, RECEIVE,_ eða _BOTH_ fyrir sendingu og móttöku, auk þess að velja hvaða MIDI-tengi þú vilt nota.

{% hint style="danger" %}
Farðu varlega með stillinguna _BOTH_. MIDI-tæki og hugbúnaður geta verið stillt til að senda til baka gögn sem þau fá inn. Þetta getur valdið endurgjöfarlykkju af MIDI-gögnum, og það er ekki gott!
{% endhint %}

### MIDI-vörpun

Sjá [Sjálfgefin MIDI-vörpun fyrir sendingu/móttöku](../reference/midi-send-receive-default-mapping.md "mention")

Ég stefni á að bæta við mun sérsniðnari MIDI-vörpun í framtíðinni, en þangað til geturðu notað forrit eins og [BOME](https://www.bome.com/products/miditranslator) og [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) til að þýða milli Liberation og sérsniðna vélbúnaðarins þíns.
