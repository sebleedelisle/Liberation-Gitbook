---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Ön ayar sistemi

Ön ayar sistemi, Liberation içinde bir _ön ayar_ listesinden birden fazla seçilebilir ayarın saklanması gereken çeşitli yerlerde kullanılır.

Bu sistem şu anda şunlar için kullanılır:

* Scanner ayarları
* Renk kalibrasyonu ayarları
* 3D görselleştirici kamera ayarları
* 3D görselleştirici lazer ayarları
* DMX profilleri

Yani yeni ve güçlü CT6210 scanner’larınız için scanner ayarlarını ince ayar yaptıysanız, bunu bir ön ayar olarak kaydedip "CT6210" adını verebilirsiniz. Böylece gelecekte ihtiyaç duyduğunuzda ön ayar listesinde ve açılır menüde kullanılabilir olur.

Kullanıyor olsanız da olmasanız da tüm ön ayarlar projenizle (veya lazer ayarlarınızla) birlikte kaydedilir. Bu nedenle bu dosyalardan birini her yüklediğinizde, içindeki tüm ön ayarlar mevcut ön ayarlarınıza eklenir. Yüklenen ön ayarlardan biri mevcut ön ayarlarınızdan biriyle aynı ada sahipse, mevcut ön ayarın üzerine yazılır.

Ayrıca ön ayar açılır listesinin yanındaki load/save düğmesini (disket simgesi) kullanarak ön ayar dosyalarını içe ve dışa aktarabilirsiniz. Bu, içe/dışa aktarma düğmelerinin bulunduğu ve ayrıca bir veya daha fazla ön ayarınızı silme seçeneği sunan bir açılır pencere açar.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Load/save simgesine tıkladığınızda açılan açılır menü</p></figcaption></figure>

Bir ön ayarı düzenlerseniz, örneğin _Default_ adlı scanner ayarını değiştirirseniz, diğer lazerlerin otomatik olarak güncellenmeyeceğini unutmayın. Bunun yerine, her birinin scanner ayarı artık _Default(edited)_ olarak etiketlenir. Bunu yeni _Default_ ön ayarına güncellemek için açılır listeden yeniden seçin.

{% hint style="info" %}
Çok sayıda lazeriniz varsa ve hepsinin scanner ayarlarını güncellemek istiyorsanız _COPY LASER SETTINGS_ sistemini kullanın. Bkz. [Lazer ayarlarını kopyalama](../setting-up/copy-laser-settings.md)
{% endhint %}

Başka bir yerde kullanılan bir ön ayarı silerseniz ayarı kaybetmezsiniz; bunun yerine _(deleted)_ olarak etiketlendiğini görürsünüz.
