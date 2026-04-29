---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive-systemet er separat fra APC40-kontrollene, og brukes til å få MIDI-data inn og ut av Liberation. Funksjoner som å starte og stoppe klipp, justere globale innstillinger, effekter og klipparametere har alle en tilknyttet MIDI-kommando.

{% hint style="info" %}
MIDI Send/Receive-systemet ble opprinnelig bygget før Liberation hadde Timeline-funksjonalitet. Det var en midlertidig løsning du kunne bruke til å ta opp og spille av et show i musikkprogramvare som Logic Pro eller Cubase.

Det gir deg direkte kontroll over klipp, effekter og innstillinger, uavhengig av visningen og rulleposisjonen i Clip Deck. Mer systemiske live-kontrollfunksjoner som tap tempo, tildeling av soner og arming/disarming er ikke implementert.
{% endhint %}

### MIDI Send/Receive-innstillinger

Åpne _MIDI Send/Receive_-panelet (med menyen _View -> MIDI Send/Receive_). Du vil se at du har valg for _SEND, RECEIVE,_ eller _BOTH_ for sending og mottak, samt mulighet til å velge hvilke MIDI-grensesnitt du vil bruke.

{% hint style="danger" %}
Bruk _BOTH_-innstillingen med forsiktighet. MIDI-enheter og programvare kan konfigureres til å sende tilbake data de mottar. Dette kan føre til en feedback loop med MIDI-data, og det er ikke bra!
{% endhint %}

### MIDI-mapping

Se [Standardtilordning for MIDI-sending/-mottak](../reference/midi-send-receive-default-mapping.md "mention")

Jeg planlegger å legge til mye mer tilpassbar MIDI-mapping i fremtiden, men i mellomtiden kan du bruke apper som [BOME](https://www.bome.com/products/miditranslator) og [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) til å oversette mellom Liberation og din egen tilpassede maskinvare.
