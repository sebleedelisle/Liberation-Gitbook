---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas hedef alanları

Canvas’ın bazı bölümlerini her lazerdeki zones içine nasıl aktaracağımızı biliyoruz. Ancak içeriği en başta Canvas’a yerleştirmek için, adı biraz kafa karıştırıcı ama doğru olan _Canvas hedef alanlarına_ ihtiyacınız var.

_Canvas hedef alanları_, Clips çizebileceğiniz Canvas bölümleridir ve _CANVAS_ görünümünde mavi çerçeveli dikdörtgenlerle gösterilir.

Çoğu zaman yalnızca bir Canvas hedef alanı yeterli olur; ardından bunu farklı lazerlere gönderilen birden fazla zone olarak bölebilirsiniz.

Bazen de bir binanın farklı bölümleri için birden fazla Canvas hedef alanı kullanmak veya bunlar arasında zone delay özelliğinden yararlanmak isteyebilirsiniz. (Evet! Zone delay, Canvas hedef alanları arasında da çalışır!).

### Clips’i Canvas hedef alanlarına gönderme

Clip Deck’e bakarsanız, beam zone düğmelerinin yanında Canvas hedef alanı düğmelerini görürsünüz. Bunları görmek için Output düğmelerini kaydırmanız gerekebilir; `Shift + Left / Right Arrow` kullanabilir, ekrandaki ZONE PAGE düğmelerini veya APC40 düğmelerini kullanabilirsiniz (bkz. [APC40 referansı](../reference/apc40-reference.md "mention"))

Clips’i Canvas hedef alanlarına atamak için bu düğmeleri, beam zone düğmelerinde yaptığınızla tamamen aynı şekilde açıp kapatın.

### Canvas hedef alanları ekleme / düzenleme

Üst menü çubuğunda _View -> Canvas Target Areas_ öğesini seçin. Projenizdeki her Canvas hedef alanına ait tüm ayarları görürsünüz.

Üstte _ADD CANVAS TARGET AREA_ düğmesi bulunur.

Canvas hedef alanını silmek için eksi işaretli kırmızı düğmeyi kullanın.

Boyutu ve konumu slider’larla ayarlayın. Değer yazmak için bir slider’a çift tıklayın.

### Scale mode

* **FIT TO AREA** - En-boy oranını koruyarak içeriği Canvas hedef alanının içine tamamen sığacak şekilde küçültür. (Varsayılan ayar budur)
* **FILL AREA** - En-boy oranını koruyarak içeriği Canvas hedef alanını dolduracak şekilde ölçekler. İçeriğin kenarlardan taşan bölümleri kesilebilir.
* **STRETCH TO FIT** - En-boy oranını dikkate almadan içeriği tüm Canvas hedef alanını dolduracak şekilde esnetir.
