---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Latency-indstilling

I panelet _Settings_ (_Liberation->Settings_ eller CMD/CTRL ,) ser du en skyder med teksten _Latency(ms)._ (I ældre versioner af Liberation lå den i panelet Laser Overview)

{% hint style="info" %}
Standardindstillingen for latency på 150 ms bør fungere fint i de fleste tilfælde, men hvis du har netværksproblemer, kan du prøve at øge den.
{% endhint %}

### Den komplicerede forklaring

Denne indstilling for "frame latency" er den maksimale tid mellem, at Liberation opretter en frame, og at laseren begynder at outputte den. Hvis du øger værdien, kan du opleve en lille forsinkelse mellem Liberation og dit laser-output.

Fordelen ved en længere frame latency er, at Liberation kan fylde lasercontrollerens buffere med indhold så tidligt som muligt. Hvis der er belastning på netværket, er der mindre risiko for, at controlleren løber tør for punkter.

Dette gælder normalt kun for netværks-DAC'er, og en indstilling på 100 ms bør være en god balance mellem hastighed og beskyttelse mod netværksforsinkelser. Hvis du har et virkelig stabilt netværk, bør du kunne sænke den til 50 ms.&#x20;
