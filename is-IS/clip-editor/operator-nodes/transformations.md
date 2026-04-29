---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Umbreytingar

## &#x20;Translate

Færir allt efni eftir x-, y- og/eða z-ás. Athugaðu að hnitakerfið er miðjað og nær frá +/-200 á x- og y-ás. Sjá [Hnitakerfi](../fundamentals/co-ordinate-system.md).

* **x** - fjarlægðin sem á að færa eftir x-ás (vinstri - hægri).
* **y** - fjarlægðin sem á að færa eftir y-ás (efst - neðst).

#### 3D-valkostir (í boði þegar 3D er valið)

* **z** - fjarlægðin sem á að færa eftir z-ás (aftur og fram inn í skjáinn).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Snýr öllu efni. Gildi eru í gráðum. Sjá [Hnitakerfi](../fundamentals/co-ordinate-system.md).

* **rotation** - hversu mikið efninu er snúið réttsælis, í gráðum. Öllu er snúið um upphafspunktinn (0,0), miðjuna.
* **pivot point x / pivot point y** - notaðu þessi gildi til að hliðra upphafspunkti snúningsins.

#### 3D-valkostir (í boði þegar 3D er valið)

* **rotation x** - snúningur um x-ás (pitch).
* **rotation y** - snúningur um y-ás (yaw).
* **pivot point z** - hliðrun á stöðu snúnings í z-ás.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Kvarðar allt efni.

* **scale** - kvörðunarprósenta.
* **scale x / scale y** - notaðu þessa valkosti ef þú vilt kvarða lárétt og/eða lóðrétt.

{% hint style="warning" %}
Þegar eitthvað er kvarðað í 0% á einhverjum ás hverfur það!
{% endhint %}
