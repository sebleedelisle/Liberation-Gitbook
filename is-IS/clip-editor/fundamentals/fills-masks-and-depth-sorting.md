---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Fyllingar, masks og dýptarröðun

### Útlínur, fyllingar og masks

Þú tekur eftir því að sumir Creator nodes eru með valkostinn _Fill state_; þú getur teiknað þá með útlínu, sem mask sem hylur það sem er undir, eða hvort tveggja.

Þegar þú renderar form sem mask er það eins og það sé fyllt með svörtu og allt sem er undir því hverfur.

{% hint style="info" %}
Það er nógu einfalt að teikna línu, eða _stroke_, með laser; þú skannar laserinn frá byrjun línunnar til enda hennar. Þar er línan komin!

Fyllt form eru hins vegar erfiðari. Ef þú vilt fylla form með lit gætirðu handvirkt teiknað þverstrikun með línum og fyllt þannig inn, en Liberation getur ekki gert það sjálfkrafa, að minnsta kosti ekki enn. Og jafnvel þótt við gætum gert það myndirðu samt sjá aðrar línur undir skína í gegn.

Það sem við getum hins vegar gert er að fylla form með _svörtu_. Undir húddinu sér Liberation um alla útreikninga sem þarf til að fjarlægja efni sem liggur undir svarta fyllta forminu. Og trúðu mér, það er talsvert vandasamt!

En þetta virkar mjög vel og skapar þá blekkingu að formið sé fyllt með svörtu.
{% endhint %}

### Dýptarröðun

Þar sem sum form geta _hulið_ önnur form þarf Liberation að raða þeim eftir dýpt. Sjálfgefið eru element dýptarröðuð eftir z-staðsetningu. Ef þau eru á sömu z-staðsetningu er þeim raðað eftir stöðu þeirra í lagi, sem hægt er að breyta með hnöppunum _MOVE TO FRONT_ og _MOVE TO BACK_ inni í hverjum Creator.
