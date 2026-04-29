---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Yfirlit yfir Canvas

Kerfið Canvas í Liberation er tiltölulega einfalt, en það getur verið ruglingslegt í fyrstu. Hér er hugmyndalegt yfirlit til að koma þér af stað.

{% hint style="info" %}
**Bíddu, þarf ég að nota Canvas?**

Kannski ekki! Ef þú ert bara að varpa einni grafík á einn leysi geturðu gert það auðveldlega með beam zone (þó að efni í beam zone sé sjálfgefið speglað lárétt, þannig að þú þarft að kveikja á X flip fyrir Clip).

En ef þú vilt dreifa grafísku efni á fleiri en einn leysi, eða skipta því í mismunandi hluta til að kortleggja á byggingarform, þá sér Canvas um það!
{% endhint %}

### Canvas

Fyrst er það sjálft Canvas. Þetta er það sem þú sérð í _CANVAS_ view og táknar stórt vinnusvæði — eiginlega striga — þar sem þú getur teiknað efni hvar sem er innan svæðisins.

### Marksvæði á Canvas

Þau birtast sem bláir útlínurétthyrningar í Canvas view og eru svæði sem þú getur sent efni á. Þú sendir efni úr Clip á marksvæði á Canvas á sama hátt og þú myndir senda Clip í beam zone. Þú sérð hnappana fyrir marksvæði á Canvas hægra megin við hnappana fyrir beam zone í Clip Deck.

{% hint style="info" %}
Ef þú sérð ekki hnappana fyrir Canvas í Clip Deck skaltu prófa að skruna hnappana fyrir beam zone með `Shift + Left / Right Arrow`. Þú ættir að sjá hnapp fyrir hvert marksvæði á Canvas, merkt _CANVAS 1, CANVAS 2_ o.s.frv.
{% endhint %}

### Canvas zones

Canvas zones eru svæði innan Canvas sem þú velur að senda á leysi. Þau birtast sem bleikir útlínurétthyrningar í Canvas view. Þú getur hægrismellt á hvert zone og valið leysana sem þú vilt úthluta því á. Ef þú skiptir nú yfir í _OUTPUT_ view fyrir þann leysi sérðu að nýtt zone hefur birst.

{% hint style="danger" %}
VIÐVÖRUN - ef leysirinn er armed gætirðu skyndilega byrjað að varpa efni í sjálfgefnu canvas zone. Best er að velja disarm fyrir leysinn áður en þú úthlutar canvas zones á hann.
{% endhint %}

{% hint style="info" %}
Þú getur líka úthlutað canvas zone á leysi með því að smella á _add canvas zone_ hnappinn í _OUTPUT_ view. Sjá [Zones](../output-view/zones.md).
{% endhint %}

### Leiðarmyndir

Þú getur bætt leiðarmynd inn í Canvas og notað hana sem sniðmát fyrir grafíkina þína. Það er ráðlegt að stilla litblæ leiðarmyndarinnar (í hægrismellivalmyndinni) og dekkja hana svo auðveldara sé að sjá efnið þitt ofan á henni.

{% hint style="info" %}
Við kortlagningu á byggingarform hefur mér reynst gagnlegt að búa til „útfletta“ mynd af byggingunni, þar sem allir fletir hennar eru sýndir sem flöt og óbjöguð mynd. Sjónarhornsleiðrétting fyrir mismunandi hluta er síðan hægt að gera með canvas zone í _OUTPUT_ view.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>„Flöt“ leiðarmynd fyrir Saltwell Hall í Gateshead í Bretlandi</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas zones í frumgerð af Liberation (um 2017!) Athugaðu að bleiku rétthyrningarnir velja hvaða hluti Canvas er sýndur, og Output views fyrir neðan sýna síðan á hvaða hluta hvers leysis þessi zones fara.</p></figcaption></figure>

### Canvas í 3D-sýnaranum

Það væri líklega ansi snúið, vægast sagt, að endurgera flókið vörpunarkerfi með mörgum leysum í 3D-sýnaranum! Þess í stað hefurðu möguleika á að staðsetja Canvas innan 3D-rýmisins. Kveiktu á _Show canvas_ gátreitnum í _3D visualiser settings_ panel. (Allar leiðarmyndir sem þú ert með í Canvas birtast líka í sýnaranum.)

{% hint style="info" %}
Athugaðu að sýnarinn mun samt sýna varpanir frá Canvas sem andrúmsloftsáhrif frá leysunum. Þú getur annaðhvort fært þær út úr sjónsviðinu eða, ef þú vilt vanda þig, látið þær passa við Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Það getur verið ótrúlega ánægjulegt þegar geislarnir frá leysinum passa við myndina á Canvas í 3D-sýnaranum!</p></figcaption></figure>
