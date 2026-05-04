---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ DMX-zónák létrehozása

1. Csatlakoztasd az Art-Net node eszközt, és állítsd be a [Csatlakozás Art-Net node-hoz](../connecting-to-an-artnet-node.md "mention") leírás szerint.
2. Nyisd meg a **DMX Zones** részt, majd kattints az **ADD DMX ZONE** gombra.
3. Állítsd be a zone **Node**, **Universe** és **Address** értékét úgy, hogy megfeleljen a lámpának.
4. Válassz egy **Preset** beállítást a lámpához. A preset határozza meg, hogy mely DMX-csatornák kapnak fix értékeket, tartalom be/ki értékeket, RGB-színt, X/Y pozíciót, fényerőt vagy explicit DMX Value bemeneteket.
5. Kattints az **Edit DMX profile/channel mapping** lehetőségre (csúszkák ikon) a csatornakiosztás szerkesztéséhez. Az alapértelmezett preset egy tartalom be/ki csatornával és RGB-színcsatornákkal indul.
6. A Clip elemeket ugyanúgy rendeld hozzá a DMX zone területhez, ahogy a beam zone vagy canvas zone területekhez szoktad.
7. Nyomd meg az **ARM** gombot, amikor készen állsz arra, hogy a zone DMX-jelet küldjön.

{% hint style="warning" %}
Csak az élesített DMX zone területek küldenek élő értékeket. A nem élesített DMX zone területek nullára állítják a hozzárendelt csatornáikat, ami biztonságosabb a lámpák beállításakor.
{% endhint %}

A DMX-kimenetet a licencszinted is korlátozza. Ha az **ARM** gomb le van tiltva, ellenőrizd, hogy a licencszinted tartalmazza-e a DMX-kimenetet, illetve hogy elérted-e már az élesíthető DMX zone területek maximális számát.
