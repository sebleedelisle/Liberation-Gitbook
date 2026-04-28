---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Latensinnstilling

I _Settings_-panelet (_Liberation->Settings_ eller CMD/CTRL ,) ser du en glidebryter merket _Latency(ms)._ (I eldre versjoner av Liberation lå dette i Laser Overview-panelet)

{% hint style="info" %}
Standardinnstillingen for latens på 150 ms bør fungere fint i de fleste tilfeller, men hvis du har nettverksproblemer, kan det være lurt å prøve å øke den.
{% endhint %}

### Den kompliserte forklaringen

Denne innstillingen for «frame latency» er den maksimale tiden mellom at Liberation oppretter en frame, og at laseren begynner å sende den ut. Hvis du øker denne verdien, kan du merke en liten forsinkelse mellom Liberation og laserutgangen.

Fordelen med høyere frame latency er at Liberation kan fylle bufferne i laserkontrollerne med innhold så raskt som mulig. Hvis det er trafikkproblemer på nettverket, er det mindre sannsynlig at kontrolleren går tom for punkter.

Dette gjelder vanligvis bare nettverks-DAC-er, og en innstilling på 100 ms bør gi en god balanse mellom hastighet og beskyttelse mot nettverksforsinkelser. Hvis du har et svært stabilt nettverk, bør du kunne redusere den til 50 ms.&#x20;
