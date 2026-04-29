---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Tüm içeriğin aynalanmış bir kopyasını oluşturur. Varsayılan olarak ayna ekseni ortadaki dikey bir çizgidir.

* **angle** - ayna ekseni çizgisinin açısı.
* **offset position** - ayna eksenini kaydırır (eksene dik yönde hareket ettirir)
* **delay** - aynalanmış içeriğin zaman gecikmesi. Bunun yalnızca içerikte bir tür animasyon varsa etkili olacağını unutmayın.

#### 3D seçenekleri (3D seçili olduğunda kullanılabilir)

* **angle X / angle Y** - ayna ekseni bir düzleme dönüşür ve bu ayarlarla düzlemi 3D içinde döndürebilirsiniz.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

İçeriği dairesel bir düzen içinde çoğaltır.

* **radius** - içeriğin döndürülmeden önce merkez noktasından ne kadar uzağa kaydırılacağı.
* **count** - nesneden oluşturulacak kopya sayısı.
* **use each objects pivot point** - seçildiğinde her öğe kendi merkez noktası etrafında kaydırılır ve döndürülür. (Yalnızca birden fazla öğe çoğaltılırken etkili olur)
* **delay** - çoğaltılan her öğeye kademeli olarak artan bir zaman gecikmesi ekler. Bunun fark edilir bir etki yaratması için içerikte bir tür animasyon olması gerekir.
* **rotation** - öğelere eklenen ofset dönüş.

#### 3D seçenekleri (3D seçili olduğunda kullanılabilir)

* **rotation x / rotation y** - tüm dairesel düzeni x ve y eksenleri etrafında döndürür.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

İçeriği satır ve sütunlardan oluşan bir ızgara düzeninde çoğaltır.

* **spacing** - öğeler arasındaki mesafe
* **count X**- yatay kopya sayısı (sütunlar)
* **count Y**- dikey kopya sayısı (satırlar)
* **horizontal alignment** - sütunların başlangıç noktası: LEFT, CENTRE veya RIGHT
* **vertical alignment** - satırların başlangıç noktası: TOP, MIDDLE veya BOTTOM
* **delay** - çoğaltılan her öğeye kademeli olarak artan bir zaman gecikmesi ekler. Bunun fark edilir bir etki yaratması için içerikte bir tür animasyon olması gerekir.
