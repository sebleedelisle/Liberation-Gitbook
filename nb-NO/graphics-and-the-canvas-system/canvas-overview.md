---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas-oversikt

Liberation Canvas-systemet er relativt enkelt, men det kan være litt forvirrende i starten. Her er en konseptuell oversikt som hjelper deg i gang.

{% hint style="info" %}
**Vent, trenger jeg Canvas-systemet?**

Kanskje ikke! Hvis du bare projiserer én enkelt grafikk på én enkelt laser, kan du enkelt gjøre det med en beam zone (men som standard er innhold i beam zones speilvendt horisontalt, så du må bruke X flip på Clip-en).

Men hvis du vil fordele grafisk innhold over flere lasere, eller dele det opp i ulike seksjoner for å mappe det på arkitektur, er Canvas-systemet det du trenger.
{% endhint %}

### Canvas

Først har vi selve Canvas. Dette er det du ser i _CANVAS_-visningen, og det representerer et stort, ja, canvas, der du kan tegne innhold hvor som helst innenfor dette området.

### Canvas-målområder

Disse vises som blå konturrektangler i Canvas-visningen, og dette er områder du kan sende innhold til. Du sender innholdet fra en Clip til et Canvas-målområde på samme måte som du ville sendt en Clip til en beam zone. Du ser knappene for Canvas-målområder til høyre for beam zone-knappene i Clip Deck.

{% hint style="info" %}
Hvis du ikke ser Canvas-knappene i Clip Deck, kan du prøve å bla i beam zone-knappene med `Shift + Left / Right Arrow`. Du skal se én knapp for hvert Canvas-målområde, merket _CANVAS 1, CANVAS 2_ osv.
{% endhint %}

### Canvas-soner

Canvas-soner er områder inne i Canvas som du velger å sende til en laser. De vises som rosa konturrektangler i Canvas-visningen. Du kan høyreklikke på hver sone og velge laserne du vil tilordne den til. Hvis du nå bytter til _OUTPUT_-visningen for den laseren, ser du at en ny sone har dukket opp.

{% hint style="danger" %}
ADVARSEL – hvis laseren er armert, kan du plutselig begynne å projisere innhold i en standard Canvas-sone. Det er best å avarmere laseren før du tilordner Canvas-soner til den.
{% endhint %}

{% hint style="info" %}
Du kan også tilordne en Canvas-sone til en laser ved å klikke på _add canvas zone_-knappen i _OUTPUT_-visningen. Se [zones.md](../output-view/zones.md "mention").
{% endhint %}

### Guide images

Du kan legge til et guide image i Canvas og bruke det som mal for grafikken din. Det anbefales å justere fargetonen på guide image-et (høyreklikkmenyen) og mørkne det, slik at det blir enklere å se innholdet ditt oppå det.

{% hint style="info" %}
For arkitektonisk mapping har jeg erfart at det er nyttig å lage en «utbrettet» visualisering av bygningen, der alle flater på bygningen vises som et flatt bilde uten forvrengning. Perspektivkorrigeringen for de ulike seksjonene kan gjøres med Canvas-sonen i _OUTPUT_-visningen.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Et «utflatet» guide image for Saltwell Hall i Gateshead, UK</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas-sonene i en tidlig versjon av Liberation (ca. 2017!) Legg merke til at de rosa rektanglene velger hvilken del av Canvas som skal vises, og at output-visningene nedenfor viser hvilken del av hver laser disse sonene sendes til.</p></figcaption></figure>

### Canvas i 3D-visualisereren

Det ville sannsynligvis vært temmelig fiklete (for å si det mildt) å gjenskape et komplisert projeksjonssystem med flere lasere i 3D-visualisereren! I stedet har du derfor mulighet til å plassere Canvas inne i 3D-rommet. Aktiver avkrysningsboksen _Show canvas_ i panelet _3D visualiser settings_. (Eventuelle guide images du har i Canvas, vises også i visualisereren.)

{% hint style="info" %}
Merk at visualisereren fortsatt viser Canvas-projeksjonene som atmosfæriske effekter fra laserne. Du kan enten bare flytte dem ut av visningen, eller, hvis du vil være litt avansert, kan du justere dem slik at de treffer Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Det kan være ekstremt tilfredsstillende når du får strålene fra laseren til å treffe Canvas-bildet i 3D-visualisereren!</p></figcaption></figure>
