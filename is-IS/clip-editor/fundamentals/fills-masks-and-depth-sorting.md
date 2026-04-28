---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Fyllingar, grímur og dýptarröðun

### Útlínur, fyllingar og grímur

Þú tekur eftir því að sumir Creator-hnútar eru með valkostinn _Fill state_; þú getur teiknað þá með útlínu (outline), sem grímu (sem hylur það sem er undir) eða hvort tveggja.

Þegar þú birtir form sem grímu er það eins og það sé fyllt með svörtu og allt sem er undir því er hulið.

{% hint style="info" %}
Það er nógu einfalt að teikna línu (eða _stroke_) með leysi; þú skannar leysinn frá byrjun línunnar að enda hennar. Þar er línan komin!

Fyllt form eru hins vegar erfiðari; ef þú vilt fylla form með lit gætirðu handvirkt krossstrikað með því að teikna línur og fylla þannig inn, en Liberation getur ekki gert það sjálfvirkt (enn). Og jafnvel þótt við gerðum það, sæirðu samt aðrar línur undir því skína í gegn.

Það sem við getum hins vegar gert er að fylla form með _svörtu_. Undir húddinu framkvæmir Liberation alla útreikninga til að fjarlægja efni sem er undir svartfyllta forminu. Og trúðu mér, það er ansi vandasamt!

En þetta virkar mjög vel og gefur þá sjónhverfingu að formið sé fyllt með svörtu.
{% endhint %}

### Dýptarröðun

Þar sem sum form geta _hulið_ önnur form þarf Liberation að raða þeim eftir dýpt. Sjálfgefið er að einingar séu dýptarraðaðar eftir z-stöðu sinni. Ef þær eru í sömu z-stöðu eru þær raðaðar eftir stöðu sinni í lagi, sem hægt er að breyta með hnöppunum _MOVE TO FRONT_ og _MOVE TO BACK_ inni í hverjum creator.
