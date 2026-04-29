---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Dönüşümler

## &#x20;Translate

Tüm içeriği x, y ve/veya z eksenleri boyunca taşır. Koordinat sisteminin merkezli olduğunu ve x ile y eksenlerinde +/-200 aralığına uzandığını unutmayın. Bkz. [koordinat sistemi](../fundamentals/co-ordinate-system.md).

* **x** - x ekseni boyunca taşınacak mesafe (sol - sağ).
* **y** - y ekseni boyunca taşınacak mesafe (üst - alt).

#### 3D seçenekleri (3D seçiliyken kullanılabilir)

* **z** - z ekseni boyunca taşınacak mesafe (ekranın içine ve dışına doğru).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Tüm içeriği döndürür. Değerler derece cinsindendir. Bkz. [koordinat sistemi](../fundamentals/co-ordinate-system.md).

* **rotation** - içeriğin saat yönünde kaç derece döndürüleceği. Her şey başlangıç noktası (0,0), yani merkez etrafında döner.
* **pivot point x / pivot point y** - Döndürme başlangıç noktasını kaydırmak için bu değerleri kullanın.

#### 3D seçenekleri (3D seçiliyken kullanılabilir)

* **rotation x** - x ekseni etrafında döndürme (pitch).
* **rotation y** - y ekseni etrafında döndürme (yaw).
* **pivot point z** - z eksenindeki döndürme kaydırma konumu.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Tüm içeriği ölçeklendirir.

* **scale** - ölçek yüzdesi.
* **scale x / scale y** - yatay ve/veya dikey olarak ölçeklendirmek istiyorsanız bu seçenekleri kullanın.

{% hint style="warning" %}
Herhangi bir eksende bir şey 0% değerine ölçeklendirilirse kaybolur!
{% endhint %}
