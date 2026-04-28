---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Latenssiasetus

_Settings_-paneelissa (_Liberation->Settings_ tai CMD/CTRL ,) näet liukusäätimen, jonka nimi on _Latency(ms)._ (Liberationin vanhemmissa versioissa tämä oli Laser Overview -paneelissa)

{% hint style="info" %}
Oletusarvoinen 150 ms:n latenssiasetus sopii useimpiin tilanteisiin, mutta jos verkossa on ongelmia, asetusta kannattaa kokeilla suurentaa.
{% endhint %}

### Monimutkaisempi selitys

Tämä "frame latency" -asetus määrittää enimmäisajan siitä, kun Liberation luo framen, siihen, kun laser alkaa lähettää sitä. Jos suurennat arvoa, saatat huomata pienen viiveen Liberationin ja laserulostulon välillä.

Pidemmän frame latency -arvon etuna on, että Liberation voi täyttää laserohjainten puskurit sisällöllä mahdollisimman nopeasti. Jos verkossa on ruuhkaa, ohjaimelta loppuvat pisteet epätodennäköisemmin kesken.

Tämä koskee yleensä vain verkon kautta toimivia DAC-laitteita, ja 100 ms:n asetus on yleensä hyvä tasapaino nopeuden ja verkkoviiveiltä suojautumisen välillä. Jos verkkosi on todella hyvä, voit todennäköisesti pienentää arvon 50 ms:iin.&#x20;
