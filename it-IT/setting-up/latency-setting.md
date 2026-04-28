---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Impostazione della latenza

Nel pannello _Settings_ (_Liberation->Settings_ oppure CMD/CTRL ,) vedrai uno slider chiamato _Latency(ms)._ (Nelle versioni precedenti di Liberation si trovava nel pannello Laser Overview)

{% hint style="info" %}
L’impostazione predefinita della latenza a 150 ms va bene nella maggior parte dei casi, ma se hai problemi di rete puoi provare ad aumentarla.
{% endhint %}

### La spiegazione più complessa

Questa impostazione di “frame latency” indica il tempo massimo tra il momento in cui Liberation crea un frame e il momento in cui il laser inizia a riprodurlo. Se aumenti questo valore, potresti notare un leggero ritardo tra Liberation e l’output del laser.

Il vantaggio di una frame latency più lunga è che Liberation può riempire il prima possibile i buffer dei controller laser con i contenuti; se la rete è congestionata, è meno probabile che il controller rimanga senza punti.

Di solito questo riguarda solo i DAC di rete, e un’impostazione di 100 ms dovrebbe essere un buon equilibrio tra velocità e protezione dai ritardi di rete. Se hai una rete davvero solida, dovresti riuscire a ridurla a 50 ms.&#x20;
