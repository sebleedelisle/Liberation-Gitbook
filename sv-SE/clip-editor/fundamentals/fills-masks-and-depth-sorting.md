---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Fyllningar, masker och djupsortering

### Linjer, fyllningar och masker

Du kommer att märka att vissa Creator-noder har alternativet _Fill state_. Du kan rita dem med en linje (en kontur), som en mask (som täcker över sådant som ligger under), eller båda.

När du renderar en form som en mask är det som om den fylls med svart, och allt som ligger under den täcks över.

{% hint style="info" %}
Att rita en linje (eller _stroke_) med en laser är enkelt nog: du skannar lasern från linjens början till linjens slut. Där har du din linje!

Fyllda former är däremot svårare. Om du vill fylla en form med färg kan du manuellt korsskraffera genom att rita linjer och fylla ut, men Liberation kan inte göra det automatiskt (än). Och även om vi gjorde det skulle du fortfarande se andra linjer under den lysa igenom.

Det vi däremot kan göra är att fylla former med _svart_. Under huven gör Liberation alla beräkningar som behövs för att ta bort innehåll som ligger under den svartfyllda formen. Och tro mig, det är pilligt!

Men det fungerar riktigt bra och ger illusionen av en svart fylld form.
{% endhint %}

### Djupsortering

Eftersom vissa former kan _täcka_ andra former måste Liberation sortera dem efter djup. Som standard djupsorteras element efter sin z-position. Om de har samma z-position sorteras de efter sin lagerposition, som kan ändras med knapparna _MOVE TO FRONT_ och _MOVE TO BACK_ i varje Creator.
