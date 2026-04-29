---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Systemet MIDI Send/Receive är separat från APC40-kontrollerna och är ett sätt att skicka MIDI-data in i och ut ur Liberation. Funktioner som att starta och stoppa clips, justera globala inställningar, effekter och clipparametrar har alla ett tillhörande MIDI-kommando.

{% hint style="info" %}
Systemet MIDI Send/Receive byggdes ursprungligen innan Liberation hade någon Timeline-funktionalitet. Det var en tillfällig lösning som du kunde använda för att spela in och spela upp en show i musikprogram som Logic Pro eller Cubase.

Det ger dig direkt kontroll över clips, effekter och inställningar, oberoende av visningen och Clip Decks rullningsläge. Mer övergripande funktioner för livekontroll, som tap tempo, tilldelning av zoner och aktivering/inaktivering, är inte implementerade.
{% endhint %}

### Inställningar för MIDI Send/Receive

Öppna panelen _MIDI Send/Receive_ (via menyn _View -> MIDI Send/Receive_). Du ser att du kan välja _SEND, RECEIVE,_ eller _BOTH_ för att skicka och ta emot, samt välja vilka MIDI-gränssnitt du vill använda.

{% hint style="danger" %}
Använd inställningen _BOTH_ med försiktighet. MIDI-enheter och programvara kan konfigureras för att skicka tillbaka data som de tar emot. Det kan orsaka en återkopplingsloop av MIDI-data, och det är inte bra!
{% endhint %}

### MIDI-mappning

Se [Standardmappning för MIDI-sändning/-mottagning](../reference/midi-send-receive-default-mapping.md "mention")

Jag planerar att lägga till betydligt mer anpassningsbar MIDI-mappning i framtiden, men tills vidare kan du använda appar som [BOME](https://www.bome.com/products/miditranslator) och [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) för att översätta mellan Liberation och din egen hårdvara.
