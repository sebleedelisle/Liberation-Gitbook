---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Yfirlit yfir Canvas

Liberation Canvas-kerfið er tiltölulega einfalt, en það getur verið ruglingslegt í fyrstu. Hér er huglægt yfirlit sem kemur þér af stað.

{% hint style="info" %}
**Bíddu, þarf ég Canvas-kerfið?**

Kannski ekki! Ef þú ert bara að varpa einni grafík á einn laser geturðu auðveldlega gert það með beam zone (þó að efni í beam zone sé sjálfgefið speglað lárétt, þannig að þú þarft að nota X flip á Clip).

En ef þú vilt dreifa grafísku efni yfir fleiri en einn laser, eða skipta því upp í mismunandi hluta til að kortleggja á byggingar, þá sér Canvas-kerfið um það!
{% endhint %}

### Canvas

Fyrst er það Canvas sjálft. Þetta er það sem þú sérð í _CANVAS_ view og táknar stóran, ja, Canvas-flöt þar sem þú getur teiknað efni hvar sem er innan þessa svæðis.

### Canvas target areas

Þessi svæði birtast sem bláir útlínurétthyrningar í Canvas view og eru svæði sem þú getur sent efni á. Þú sendir efni úr Clip á Canvas target area, á sama hátt og þú myndir senda Clip á beam zone. Þú sérð Canvas target area-hnappana hægra megin við beam zone-hnappana í Clip Deck.

{% hint style="info" %}
Ef þú sérð ekki Canvas-hnappana í Clip Deck skaltu prófa að fletta beam zone-hnöppunum með `Shift + Left / Right Arrow`. Þú ættir að sjá hnapp fyrir hvert Canvas target area merkt _CANVAS 1, CANVAS 2_ o.s.frv.
{% endhint %}

### Canvas zones

Canvas zones eru svæði innan Canvas sem þú velur að senda á laser. Þau eru sýnd sem bleikir útlínurétthyrningar í Canvas view. Þú getur hægrismellt á hvert svæði og valið laserana sem þú vilt úthluta því til. Ef þú skiptir nú yfir í _OUTPUT_ view fyrir þann laser sérðu að nýtt svæði hefur birst.

{% hint style="danger" %}
VIÐVÖRUN - ef laserinn er armed gætirðu skyndilega byrjað að varpa efni á sjálfgefnu Canvas zone. Best er að disarm laserinn áður en þú úthlutar Canvas zones til hans.
{% endhint %}

{% hint style="info" %}
Þú getur einnig úthlutað Canvas zone til lasers með því að smella á _add canvas zone_ hnappinn í _OUTPUT_ view. Sjá [zones.md](../output-view/zones.md).
{% endhint %}

### Guide images

Þú getur bætt guide image inn í Canvas og notað hana sem sniðmát fyrir grafíkina þína. Mælt er með að stilla colour tint á guide image (hægrismellsvalmynd) og dekkja hana svo auðveldara sé að sjá efnið þitt ofan á henni.

{% hint style="info" %}
Við architectural mapping hefur mér reynst gagnlegt að búa til „útflett“ myndrænt yfirlit af byggingunni sem sýnir alla fleti hennar sem flata, óbjagaða mynd. Sjónarhornsleiðréttingu fyrir mismunandi hluta er hægt að gera með Canvas zone í _OUTPUT_ view.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>„Útflött“ guide image fyrir Saltwell Hall í Gateshead í Bretlandi</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas zones í frumgerð af Liberation (um 2017!) Taktu eftir að bleiku rétthyrningarnir velja hvaða hluta af Canvas á að sýna, og Output views fyrir neðan sýna síðan á hvaða hluta hvers lasers þessi svæði fara.</p></figcaption></figure>

### Canvas í 3D visualiser

Það væri líklega ansi snúið (vægast sagt) að endurskapa flókið fjöllaser-varpskerfi í 3D visualiser! Þess í stað geturðu sett Canvas inn í 3D-rýmið. Virkjaðu _Show canvas_ gátreitinn í _3D visualiser settings_ panel. (Allar guide images sem þú ert með í Canvas birtast líka í visualiser.)

{% hint style="info" %}
Athugaðu að visualiser sýnir samt Canvas-vörpunina sem lofthjúpsáhrif frá laserunum. Þú getur annaðhvort einfaldlega fært þau út úr sýninni eða, ef þú vilt gera þetta flott, stillt þau saman við Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Það getur verið einstaklega ánægjulegt þegar geislarnir frá lasernum eru stilltir saman við Canvas-myndina í 3D visualiser!</p></figcaption></figure>
