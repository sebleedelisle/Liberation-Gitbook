---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Vullingen, maskers en dieptesortering

### Lijnen, vullingen en maskers

Je zult merken dat sommige Creator-nodes een optie _Fill state_ hebben; je kunt ze tekenen met een lijn (een contour), als masker (dat onderliggende inhoud afdekt), of allebei.

Wanneer je een vorm als masker rendert, is het alsof die met zwart is gevuld en alles eronder wordt afgedekt.

{% hint style="info" %}
Een lijn (of _stroke_) tekenen met een laser is vrij eenvoudig; je scant de laser van het begin van de lijn naar het einde van de lijn. Daar is je lijn!

Gevulde vormen zijn lastiger. Als je een vorm met kleur wilt vullen, kun je handmatig arceren door lijnen te tekenen en zo op te vullen, maar Liberation kan dat (nog) niet automatisch. En zelfs als we dat wel zouden doen, zou je nog steeds andere lijnen eronder zien doorschijnen.

Wat we wel kunnen doen, is vormen met _zwart_ vullen. Onder de motorkap voert Liberation alle berekeningen uit om inhoud te verwijderen die onder de zwart gevulde vorm ligt. En geloof me: dat is priegelwerk!

Maar het werkt heel goed en geeft de illusie van een zwart gevulde vorm.
{% endhint %}

### Dieptesortering

Omdat sommige vormen andere vormen kunnen _afdekken_, moet Liberation ze sorteren op diepte. Standaard worden elementen op diepte gesorteerd op basis van hun z-positie. Als ze dezelfde z-positie hebben, worden ze gesorteerd op hun laagpositie. Die kun je wijzigen met de knoppen _MOVE TO FRONT_ en _MOVE TO BACK_ in elke creator.
