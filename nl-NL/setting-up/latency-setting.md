---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Latency-instelling

In het _Settings_-paneel (_Liberation->Settings_ of CMD/CTRL ,) zie je een slider met het label _Latency(ms)._ (In oudere versies van Liberation stond deze in het Laser Overview-paneel)

{% hint style="info" %}
De standaard latency-instelling van 150 ms is in de meeste gevallen prima, maar als je netwerkproblemen hebt, kun je proberen deze waarde te verhogen.
{% endhint %}

### De ingewikkelde uitleg

Deze instelling voor "frame latency" is de maximale tijd tussen het moment waarop Liberation een frame aanmaakt en het moment waarop de laser het begint uit te sturen. Als je deze waarde verhoogt, kun je een kleine vertraging merken tussen Liberation en je laser-output.

Het voordeel van een langere frame latency is dat Liberation de buffers van de lasercontrollers zo snel mogelijk met content kan vullen; als er congestie op het netwerk is, is de kans kleiner dat de controller zonder punten komt te zitten.

Dit geldt meestal alleen voor netwerk-DAC's, en een instelling van 100 ms is doorgaans een goede balans tussen snelheid en bescherming tegen netwerkvertragingen. Als je een echt sterk netwerk hebt, zou je dit moeten kunnen verlagen naar 50 ms.&#x20;
