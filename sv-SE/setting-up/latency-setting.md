---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Latensinställning

I panelen _Settings_ (_Liberation->Settings_ eller CMD/CTRL ,) ser du ett skjutreglage med etiketten _Latency(ms)._ (I äldre versioner av Liberation fanns detta i panelen Laser Overview)

{% hint style="info" %}
Standardinställningen för latens på 150 ms fungerar bra i de flesta fall, men om du har nätverksproblem kan du prova att öka den.
{% endhint %}

### Den komplicerade förklaringen

Den här inställningen för "frame latency" är den längsta tiden mellan att Liberation skapar en frame och att lasern börjar mata ut den. Om du ökar värdet kan du märka en liten fördröjning mellan Liberation och din laseroutput.

Fördelen med högre frame latency är att Liberation kan fylla lasercontrollerarnas buffertar med innehåll så snabbt som möjligt. Om nätverket är belastat är det då mindre sannolikt att controllern får slut på punkter.

Detta gäller oftast bara nätverks-DAC:ar, och en inställning på 100 ms bör vara en bra balans mellan snabbhet och skydd mot nätverksfördröjningar. Om du har ett riktigt stabilt nätverk bör du kunna sänka den till 50 ms.&#x20;
