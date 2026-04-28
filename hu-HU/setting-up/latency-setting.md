---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Késleltetés beállítása

A _Settings_ panelen (_Liberation->Settings_ vagy CMD/CTRL ,) egy _Latency(ms)_ feliratú csúszkát látsz. (A Liberation régebbi verzióiban ez a Laser Overview panelen volt.)

{% hint style="info" %}
Az alapértelmezett 150 ms-os késleltetési beállítás a legtöbb esetben megfelelő, de ha hálózati problémákat tapasztalsz, érdemes lehet növelni.
{% endhint %}

### A részletes magyarázat

Ez a „frame latency” beállítás azt a maximális időt adja meg, amely a között telik el, hogy a Liberation létrehoz egy frame-et, és a lézer elkezdi azt kiadni. Ha növeled ezt az értéket, enyhe késést észlelhetsz a Liberation és a lézerkimenet között.

A hosszabb frame latency előnye, hogy a Liberation a lehető leghamarabb fel tudja tölteni tartalommal a lézervezérlők pufferét; ha a hálózaton torlódás van, kisebb az esélye, hogy a vezérlő kifogy a pontokból.

Ez általában csak hálózati DAC-okra vonatkozik, és a 100 ms-os beállítás jó egyensúlyt ad a sebesség és a hálózati késések elleni védelem között. Ha igazán stabil hálózatod van, valószínűleg 50 ms-ra is csökkentheted.&#x20;
