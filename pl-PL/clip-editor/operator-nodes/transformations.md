---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

Przesuwa całą zawartość wzdłuż osi x, y i/lub z. Pamiętaj, że układ współrzędnych jest wyśrodkowany i obejmuje zakres od +/-200 na osiach x i y. Zobacz [Układ współrzędnych](../fundamentals/co-ordinate-system.md "mention").

* **x** - odległość przesunięcia wzdłuż osi x (lewo - prawo).
* **y** - odległość przesunięcia wzdłuż osi y (góra - dół).

#### Opcje 3D (dostępne po wybraniu 3D)

* **z** - odległość przesunięcia wzdłuż osi z (w głąb ekranu i na zewnątrz).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Obraca całą zawartość. Wartości są podawane w stopniach. Zobacz [Układ współrzędnych](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - wartość obrotu zawartości zgodnie z ruchem wskazówek zegara, w stopniach. Wszystko jest obracane wokół początku układu (0,0), czyli środka.
* **pivot point x / pivot point y** - użyj tych wartości, aby przesunąć punkt początkowy obrotu.

#### Opcje 3D (dostępne po wybraniu 3D)

* **rotation x** - obrót wokół osi x (pitch).
* **rotation y** - obrót wokół osi y (yaw).
* **pivot point z** - przesunięcie pozycji obrotu na osi z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Skaluje całą zawartość.

* **scale** - procent skalowania.
* **scale x / scale y** - jeśli chcesz skalować poziomo i/lub pionowo, użyj tych opcji.

{% hint style="warning" %}
Gdy coś zostanie przeskalowane do 0% na dowolnej osi, znika!
{% endhint %}
