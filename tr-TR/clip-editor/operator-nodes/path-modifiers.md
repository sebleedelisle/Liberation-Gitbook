---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Yol Değiştiriciler

## &#x20;Dotter

Bu node, çizgi ve şekil içeriklerini eşit aralıklı noktalarla değiştirir (mevcut noktalar değişmeden kalır).

* **Colour** – noktaların rengi. _Inherit Colour_ etkinse yok sayılır; aşağıya bakın. _Ayrıca bkz._ [renk ayarları ve HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – noktalar arasındaki mesafe; piksel cinsinden ölçülür. Daha küçük değerler = daha fazla nokta, daha büyük değerler = daha az nokta.
* **Offset** – noktaların başlangıç konumunu, aralığın yüzdesi olarak kaydırır. "Hareket eden" nokta efektleri oluşturmak için animasyon uygulanabilir (ör. testere dişi Oscillator Node ile).
* **Keep Original** – etkinse orijinal çizgiler/şekiller korunur ve noktalar bunların üzerine çizilir.
* **Render Profile** – render kalitesini seçer. _Bkz._ [render profili](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – path uzunluğunun eşit bölünebilmesi için aralığı otomatik olarak ayarlar.
* **Fade Out Ends** – path başlangıcına ve sonuna doğru noktaların parlaklığını kademeli olarak azaltır. **Offset** bir testere dişi Oscillator Node ile animasyonlanırken kullanışlıdır; böylece noktalar şeklin sonuna doğru hareket ederken yumuşakça belirir/kaybolur.

## &#x20;Trimmer

Bu node, çizgi ve şekillerin görünür uzunluğunu kırpar; böylece bunları zaman içinde ortaya çıkarabilir, gizleyebilir veya animasyonlayabilirsiniz.

* **Offset** – şeklin görünür kısmının nereden başlayacağını kontrol eder. _Trim Size_ 0% olsa bile Offset değerini 0% → 100% arasında animasyonlamak, şeklin çizilmesini, 50%'de tamamen görünür olmasını ve ardından tekrar kaybolmasını sağlar.
* **Trim Size** – şeklin toplam uzunluğunun yüzdesi olarak ne kadarının korunacağını belirler.
* **Loop** – şekli sürekli bir döngü gibi ele alır; böylece son kısım kaybolmak yerine başa bağlanır.
* **All Shapes** – tüm giriş şekillerini birleştirir ve tek bir path gibi kırpar. Kapalıysa her şekil ayrı ayrı kırpılır.
* **Add Dot at Start / Add Dot at End** – kırpma noktalarına seçilen renkte bir nokta ekler. (Kırpma uygulanmazsa nokta eklenmez.)
* **Colour** – kırpma noktalarının rengi. _Ayrıca bkz._ [renk ayarları ve HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – noktalar için render profilini seçer. _Bkz._ [render profili](../fundamentals/render-profile.md)
