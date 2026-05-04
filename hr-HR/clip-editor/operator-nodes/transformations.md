---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformacije

## &#x20;Translate

Pomiče sav sadržaj duž osi x, y i/ili z. Imajte na umu da je koordinatni sustav centriran i proteže se od +/-200 po osima x i y. Pogledajte [Koordinatni sustav](../fundamentals/co-ordinate-system.md "mention").

* **x** - udaljenost pomaka duž osi x (lijevo - desno).
* **y** - udaljenost pomaka duž osi y (gore - dolje).

#### 3D opcije (dostupne kada je odabran 3D)

* **z** - udaljenost pomaka duž osi z (naprijed i natrag u dubinu zaslona).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Rotira sav sadržaj. Vrijednosti su u stupnjevima. Pogledajte [Koordinatni sustav](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - iznos za koji se sadržaj rotira u smjeru kazaljke na satu, u stupnjevima. Sve se rotira oko ishodišta (0,0), odnosno središta.
* **pivot point x / pivot point y** - upotrijebite ove vrijednosti za pomak ishodišta rotacije.

#### 3D opcije (dostupne kada je odabran 3D)

* **rotation x** - rotacija oko osi x (pitch).
* **rotation y** - rotacija oko osi y (yaw).
* **pivot point z** - položaj pomaka rotacije po osi z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skalira sav sadržaj.

* **scale** - postotak skaliranja.
* **scale x / scale y** - ako želite skalirati vodoravno i/ili okomito, upotrijebite ove opcije.

{% hint style="warning" %}
Kad god se nešto skalira na 0% po bilo kojoj osi, nestaje!
{% endhint %}
