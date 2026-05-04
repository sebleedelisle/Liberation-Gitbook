---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 DMX-alueiden luominen

1. Yhdistä Art-Net-node ja määritä se kohdan [Art-Net-nodeen yhdistäminen](../connecting-to-an-artnet-node.md "mention") ohjeiden mukaan.
2. Avaa **DMX Zones** ja napsauta **ADD DMX ZONE**.
3. Aseta zone-kohteen **Node**, **Universe** ja **Address** vastaamaan valaisinta.
4. Valitse valaisimelle **Preset**. Preset määrittää, mitkä DMX-kanavat vastaanottavat kiinteitä arvoja, sisällön päälle/pois-arvoja, RGB-värin, X/Y-sijainnin, kirkkauden tai erilliset DMX Value -syötteet.
5. Napsauta **Edit DMX profile/channel mapping** -painiketta (liukusäädinkuvake), jos haluat muokata kanavakartoitusta. Oletusarvoinen Preset alkaa sisällön päälle/pois-kanavalla ja RGB-värikanavilla.
6. Määritä Clips DMX zone -kohteelle samalla tavalla kuin määrität ne beam zone- tai canvas zone -kohteille.
7. Paina **ARM**, kun haluat, että zone alkaa lähettää DMX:ää.

{% hint style="warning" %}
Vain käyttöön viritetyt DMX zone -kohteet lähettävät reaaliaikaisia arvoja. Kun DMX zone ei ole viritetty käyttöön, sen kartoitetut kanavat tyhjennetään nollaan. Tämä on turvallisempaa valaisimia määritettäessä.
{% endhint %}

DMX-lähtöä rajoittaa myös lisenssitasosi. Jos **ARM**-painike on pois käytöstä, tarkista, sisältyykö DMX-lähtö lisenssitasoosi tai onko käyttöön viritettyjen DMX zone -kohteiden enimmäismäärä jo saavutettu.
