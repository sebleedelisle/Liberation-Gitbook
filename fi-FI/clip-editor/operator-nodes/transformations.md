---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

Siirtää kaiken sisällön x-, y- ja/tai z-akselia pitkin. Huomaa, että koordinaatisto on keskitetty ja ulottuu x- ja y-akseleilla arvoihin +/-200. Katso [co-ordinate-system.md](../fundamentals/co-ordinate-system.md).

* **x** - etäisyys, jonka sisältö siirtyy x-akselilla (vasen–oikea).
* **y** - etäisyys, jonka sisältö siirtyy y-akselilla (ylä–ala).

#### 3D-asetukset (käytettävissä, kun 3D on valittuna)

* **z** - etäisyys, jonka sisältö siirtyy z-akselilla (taakse- ja eteenpäin näytön suuntaisesti).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Kiertää kaiken sisällön. Arvot ovat asteina. Katso [co-ordinate-system.md](../fundamentals/co-ordinate-system.md).

* **rotation** - määrä asteina, jonka sisältöä kierretään myötäpäivään. Kaikki kierretään origon (0,0) eli keskikohdan ympäri.
* **pivot point x / pivot point y** - Näillä arvoilla voit siirtää kierron origopistettä.

#### 3D-asetukset (käytettävissä, kun 3D on valittuna)

* **rotation x** - kierto x-akselin ympäri (pitch).
* **rotation y** - kierto y-akselin ympäri (yaw).
* **pivot point z** - kierron siirtopiste z-akselilla.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skaalaa kaiken sisällön.

* **scale** - skaalausprosentti.
* **scale x / scale y** - käytä näitä asetuksia, jos haluat skaalata vaakasuunnassa ja/tai pystysuunnassa.

{% hint style="warning" %}
Kun jokin skaalataan 0%:iin millä tahansa akselilla, se katoaa!
{% endhint %}
