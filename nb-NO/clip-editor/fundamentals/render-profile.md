---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

Det finnes en _Render Profile_-innstilling i hver _Creator_-node, og den bestemmer hvordan figurene tegnes (eller _renderes_) med laserne.

**For de fleste bruksområder er&#x20;**_**DEFAULT**_**&#x20;-innstillingen helt fin**. Men hvis du jobber med grafikk eller komplekst innhold, kan det hende du vil ha mer kontroll over hvordan hver figur renderes.

{% hint style="info" %}
I motsetning til de fleste lasersystemer genererer Liberation en punktstrøm i sanntid, rett før den sendes til laserkontrollerne. Dette sparer deg for mye diskplass: Clip-er er bare noen få kB, i stedet for MB med forhåndsrenderte punktstrømmer.

Det betyr også at du kan tilpasse det samme innholdet for ulike scannertyper, laser for laser, uten å måtte endre selve Clip-ene.

For mer informasjon, se [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Det finnes tre forhåndsdefinerte _Render Profiles_: _DEFAULT_, _FAST_ og _DETAIL_.

_**DEFAULT**_ – en god generell profil, best for det meste

_**FAST** -_ hvis Clip-en din har mye innhold og noe av det bare er helt enkle punkter og rette linjer, kan du få mindre flimring ved å velge dette alternativet.

_**DETAIL**_ – hvis du tegner noe som trenger skarpe hjørner, bruker du dette alternativet. Men husk at scannerne da beveger seg saktere, noe som kan gjøre Output mer flimrete.

{% hint style="info" %}
I Clip editor kan du tilordne creators til ulike render profiles, men hver laser behandler disse profilene avhengig av scannerinnstillingene sine. Se [scanner-presets.md](../../advanced/scanner-presets.md "mention")
{% endhint %}
