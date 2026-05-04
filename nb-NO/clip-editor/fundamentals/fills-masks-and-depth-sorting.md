---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Fyll, masker og dybdesortering

### Streker, fyll og masker

Du vil se at noen Creator-noder har et _Fill state_-valg; du kan tegne dem med en strek (et omriss), som en maske (som dekker over innhold under), eller begge deler.

Når du gjengir en form som en maske, er det som om den er fylt med svart, og alt som ligger under den, blir dekket.

{% hint style="info" %}
Å tegne en linje (eller _stroke_) med en laser er enkelt nok; du skanner laseren fra starten av linjen til slutten av linjen. Der har du linjen din!

Fylte former er derimot vanskeligere. Hvis du vil ha en form fylt med farge, kan du manuelt krysskravere ved å tegne linjer og fylle inn, men Liberation kan ikke gjøre dette automatisk (ennå). Og selv om vi gjorde det, ville du fortsatt se andre linjer under skinne gjennom.

Det vi derimot kan gjøre, er å fylle former med _svart_. Under panseret gjør Liberation alle beregningene som trengs for å fjerne innhold som ligger under den svartfylte formen. Og tro meg, det er pirkete!

Men det fungerer veldig bra og gir illusjonen av en svartfylt form.
{% endhint %}

### Dybdesortering

Siden noen former kan _dekke_ andre former, må Liberation sortere dem etter dybde. Som standard dybdesorteres elementer etter z-posisjonen sin. Hvis de har samme z-posisjon, sorteres de etter lagposisjonen, som kan endres med knappene _MOVE TO FRONT_ og _MOVE TO BACK_ inne i hver Creator.
