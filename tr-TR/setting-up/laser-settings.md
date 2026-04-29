---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Lazer çıkışı ayarları paneli

Lazer çıkışı ayarları panelini _View -> Laser Output Settings_ menüsünden açın.

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Bu panel, şu anda seçili lazerin değiştirebileceğiniz ayarlarını gösterir:

* _Laser Overview_ panelindeki numara düğmesiyle
* klavyenizdeki sayı tuşlarıyla; 1 ile 0 arasındaki tuşlar 1 - 10 numaralı lazerleri açar
* lazerler arasında geçiş yapmak için `Tab` tuşuyla (`Shift + Tab` geriye doğru gider).

Bu panelin üst kısmında şunları görürsünüz:

* numara düğmesi - bu lazere arm/disarm uygulamak için tıklayın. Lazer armed durumdayken kırmızıdır.
* yalnızca bu lazer için bir _Brightness_ kaydırıcısı. Bunun Global Brightness ile birlikte uygulandığını unutmayın.
* _Test Pattern_ açma/kapatma düğmesi ve pattern seçici. Bu, yalnızca bu lazer için belirli bir test pattern seçmenizi sağlar. (Bu kontroller Output view araç çubuğunda da aynen bulunur).

### Çıkış yönü / aynalama düzeltmesi

Sonraki öğeler, lazer kurulumunuzu Liberation içinde tutarlı davranacak şekilde düzeltmek içindir.

* **Flip horizontal / vertical** - bu seçenekler lazerinizin çıkışını düzeltmenizi sağlar

{% hint style="info" %}
Lazeriniz hatalı kablolanmadıysa veya arkasındaki X/Y flip düğmeleri doğru ayarlanmadıysa horizontal / vertical flip ayarlarını değiştirmeniz gerekmez. Belirli bir Clip için çıkışın çevrilmesini istiyorsanız bunu doğrudan Clip üzerinde yapabilirsiniz.
{% endhint %}

* **Orientation** - lazeriniz yan veya baş aşağı asıldıysa, dönüşü bu ayarla düzeltebilirsiniz.
* **Fine position adjustments** - çok küçük kaymaları/dönmeleri düzeltmek için kullanılabilir. Bir lazer gece boyunca veya uzun süre bırakıldığında oluşabilecek kayma/oturma etkisini düzeltmek için tasarlanmıştır.

{% hint style="info" %}
Orientation / mirroring düzeltmelerinin 3D Visualiser içinde hiçbir şeyi değiştirmediğini unutmayın; bunlar gerçek lazerin çıkışını 3D Visualiser içinde görünenle eşleştirmek için kullanılmalıdır!
{% endhint %}

### Lazer ayarlarını kopyalama

Bkz. [Lazer ayarlarını kopyalama](laser-settings.md#copy-laser-settings).

### Scanner ayarları

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed ayarı, scanner hareket hızını belirler.

{% hint style="danger" %}
Varsayılan ayarlar oldukça güvenli tarafta olsa da scanner’ları çok hızlı sürerseniz yine de zarar verebilirsiniz. Özellikle hızı artırırken dikkatli olun.
{% endhint %}

{% hint style="info" %}
Bu Speed ayarı point rate değerini değiştirmez; bunun yerine noktaların ne kadar aralıklı yerleştiğini ayarlar. Daha fazla bilgi için bkz. [Liberation lazer içeriğini nasıl oluşturur](../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Scanner ışını hareket ettirirken beam renk değiştirir ve açılıp kapanır; bu iki işlem genellikle birbiriyle tam senkron değildir. Bunları tekrar hizalamak için bu ayarı düzenleyin.

{% hint style="info" %}
Bu ayar bazen _blank shift_ olarak bilinir, ancak ben kişisel olarak _scanner sync_ terimini tercih ediyorum. Çünkü tüm renk değişimlerinin zamanlamasını scanner hareketine göre ayarladığı için biraz daha doğru bir isimdir.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Lazer “kuyrukları” - Colour shift doğru ayarlanmamış</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Lazer “kuyruğu” yok! Colour shift iyi!</p></figcaption></figure></div>

Lazer çıkışınızda küçük “kuyruklar” görüyorsanız büyük olasılıkla scanner sync ayarının düzenlenmesi gerekir. Ne yaparsanız yapın kuyruklar görünmeye devam ediyorsa muhtemelen scanner’ları/lazer sürücülerini kaldırabileceklerinden daha hızlı sürüyorsunuzdur. Scanner hızını düşürmeyi deneyin.

#### Scanner ön ayarları

Önceden hazırlanmış bir scanner ayarı seçmek için bunu kullanın. Varsayılan seçenek genellikle uygundur; bu yüzden scanner’larınız özellikle kötü (veya iyi) değilse bu ayarı değiştirmeniz gerekmez. Daha ayrıntılı incelemek isterseniz bkz. [Scanner ön ayarları](../advanced/scanner-presets.md)

#### Renk kalibrasyonu

Bu sistemi lazerinizin parlaklık eğrisini ve beyaz dengesini düzeltmek için kullanabilirsiniz. Bkz. [Renk kalibrasyonu](../advanced/colour-calibration.md)

#### Gelişmiş ayarlar

Bunlarla uğraşmanız gerekmez; ancak merak ediyorsanız bkz. [Gelişmiş lazer ayarları](../advanced/advanced-laser-settings.md)
