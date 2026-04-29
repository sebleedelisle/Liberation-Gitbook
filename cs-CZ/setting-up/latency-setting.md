---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Nastavení latence

V panelu _Settings_ (_Liberation->Settings_ nebo CMD/CTRL ,) najdete posuvník označený _Latency(ms)._ (Ve starších verzích Liberation byl v panelu Laser Overview.)

{% hint style="info" %}
Výchozí nastavení latence 150 ms by mělo vyhovovat ve většině případů. Pokud ale máte problémy se sítí, můžete ho zkusit zvýšit.
{% endhint %}

### Složitější vysvětlení

Toto nastavení „latence snímků“ určuje maximální dobu mezi okamžikem, kdy Liberation vytvoří snímek, a okamžikem, kdy ho laser začne vysílat. Pokud tuto hodnotu zvýšíte, můžete si všimnout mírného zpoždění mezi Liberation a laserovým výstupem.

Výhodou delší latence snímků je, že Liberation může co nejdříve naplnit buffery laser controllers obsahem. Pokud dojde k zahlcení sítě, je méně pravděpodobné, že controlleru dojdou body.

To se obvykle týká jen síťových DAC a nastavení 100 ms by mělo být dobrým kompromisem mezi rychlostí a ochranou proti zpožděním v síti. Pokud máte opravdu kvalitní síť, měli byste být schopni hodnotu snížit na 50 ms.&#x20;
