---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Stilling fyrir biðtíma

Í _Settings_ panel (_Liberation->Settings_ eða CMD/CTRL ,) sérðu sleða merktan _Latency(ms)._ (Í eldri útgáfum af Liberation var þetta í Laser Overview panel)

{% hint style="info" %}
Sjálfgefna stillingin fyrir biðtíma, 150 ms, ætti að henta í flestum tilvikum, en ef þú lendir í vandamálum með netið getur verið gott að prófa að hækka gildið.
{% endhint %}

### Flóknari skýringin

Þessi stilling fyrir „frame latency“ er hámarkstíminn frá því að Liberation býr til ramma þar til laserinn byrjar að senda hann út. Ef þú hækkar þetta gildi gætirðu tekið eftir smávægilegri töf milli Liberation og úttaksins frá lasernum.

Kosturinn við lengri biðtíma ramma er að Liberation getur fyllt biðminni í laser controller með efni eins fljótt og hægt er. Ef umferðarteppa verður á netinu eru minni líkur á að controller verði uppiskroppa með points.

Þetta á yfirleitt aðeins við um DAC á neti og stilling upp á 100 ms ætti að gefa gott jafnvægi milli hraða og varnar gegn töfum á netinu. Ef þú ert með mjög öflugt net ættirðu að geta lækkað gildið í 50 ms.&#x20;
