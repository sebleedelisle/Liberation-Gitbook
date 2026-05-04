---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Dolgular, mask ve derinlik sıralaması

### Stroke, dolgu ve mask

Bazı Creator node öğelerinde _Fill state_ seçeneği olduğunu fark edeceksiniz; bunları stroke (dış çizgi) ile, mask olarak (altındaki öğeleri kapatarak) veya ikisi birlikte olacak şekilde çizebilirsiniz.

Bir şekli mask olarak render ettiğinizde, siyahla doldurulmuş gibi davranır ve altındaki her şeyi kapatır.

{% hint style="info" %}
Lazerle bir çizgi (veya _stroke_) çizmek oldukça kolaydır; lazeri çizginin başından sonuna kadar tararsınız. İşte çizginiz!

Dolu şekiller ise daha zordur. Bir şeklin renkle doldurulmasını istiyorsanız, elle çizgiler çizip içini çapraz tarama ile doldurabilirsiniz; ancak Liberation bunu otomatik olarak yapamaz (henüz). Bunu yapabilsek bile, altındaki diğer çizgilerin görünmeye devam ettiğini görürdünüz.

Ama yapabildiğimiz şey, şekilleri _siyah_ ile doldurmaktır. Arka planda Liberation, siyah dolgulu şeklin altında kalan içeriği kaldırmak için tüm hesaplamaları yapar. Ve inanın, bu oldukça hassas bir iştir!

Yine de çok iyi çalışır ve siyah dolgulu bir şekil yanılsaması verir.
{% endhint %}

### Derinlik sıralaması

Bazı şekiller diğer şekilleri _kapatabildiği_ için Liberation bunları derinliklerine göre sıralamak zorundadır. Varsayılan olarak öğeler, z konumlarına göre derinlik sıralamasına alınır. Aynı z konumundalarsa, layer konumlarına göre sıralanırlar; bu konum her Creator içindeki _MOVE TO FRONT_ ve _MOVE TO BACK_ düğmeleriyle değiştirilebilir.
