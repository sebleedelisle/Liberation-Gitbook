# ✅ Lazer çıkışı ayarları paneli

Lazer çıkışı ayarları panelini _View -> Laser Output Settings_ menüsünden açın.

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Bu panelde, o anda seçili olan lazerin değiştirebileceğiniz ayarları gösterilir:

* _Laser Overview_ panelindeki numara düğmesiyle
* klavyenizdeki sayı tuşlarıyla; 1 ile 0 arasındaki tuşlar 1 - 10 numaralı lazerleri açar
* lazerler arasında geçiş yapmak için `Tab` tuşuyla (`Shift + Tab` geriye doğru gider).

Bu panelin üst kısmında şunları görürsünüz:

* bir numara düğmesi - bu lazere arm/disarm işlemi yapmak için tıklayın. Lazer armed durumdayken kırmızı görünür.
* yalnızca bu lazer için bir _Brightness_ kaydırıcısı. Bunun global brightness ile birlikte uygulandığını unutmayın.
* _Test Pattern_ aç/kapat düğmesi ve pattern seçici. Bu, yalnızca bu lazer için belirli bir test pattern seçmenizi sağlar. (Bu kontroller Output view araç çubuğunda da aynı şekilde bulunur.)

### Çıkış yönü / aynalama düzeltmesi

Sonraki öğeler, lazer kurulumunuzu Liberation içinde tutarlı davranacak şekilde düzeltmek içindir.

* **Flip horizontal / vertical** - bu seçenekler lazerinizin çıkışını düzeltmenizi sağlar

{% hint style="info" %}
Lazeriniz hatalı kablolanmadıysa veya arkasındaki X/Y flip düğmeleri doğru ayarlanmadıysa, horizontal / vertical flip ayarlarını değiştirmeniz gerekmez. Belirli bir Clip için çıkışın ters çevrilmesini istiyorsanız, bunu doğrudan Clip üzerinde yapabilirsiniz.
{% endhint %}

* **Orientation** - lazeriniz yan veya baş aşağı monte edildiyse, dönüşü bu ayarla düzeltebilirsiniz.
* **Fine position adjustments** - çok küçük kayma/dönüş düzeltmeleri için kullanılabilir. Bir lazer gece boyunca veya uzun süre açık kaldığında oluşabilecek sapma/yerleşme etkilerini düzeltmek için tasarlanmıştır.

{% hint style="info" %}
Orientation / mirroring düzeltmelerinin 3D Visualiser içinde hiçbir şeyi değiştirmediğini unutmayın. Bunlar, gerçek lazer çıkışını 3D Visualiser içinde gördüğünüzle eşleştirmek için kullanılmalıdır!
{% endhint %}

### Lazer ayarlarını kopyalama

Bkz. [Lazer ayarlarını kopyalama](./#copy-laser-settings "mention").

### Scanner ayarları

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed ayarı, scanner hareketlerinin ne kadar hızlı olacağını belirler.

{% hint style="danger" %}
Varsayılan ayarlar oldukça temkinli olsa da scanner ayarlarını çok hızlı sürerseniz yine de hasar verebilirsiniz. Özellikle hızı artırırken dikkatli olun.
{% endhint %}

{% hint style="info" %}
Bu Speed ayarı point rate değerini değiştirmez; bunun yerine noktaların ne kadar aralıklı yerleştirileceğini ayarlar. Daha fazla bilgi için bkz. [Liberation lazer içeriğini nasıl üretir](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Işın, scanner hareket ederken renk değiştirir ve açılıp kapanır; bu iki işlem genellikle birbiriyle tam olarak senkron değildir. Bu ayarı, ikisini tekrar hizalamak için kullanın.

{% hint style="info" %}
Bu ayar bazen _blank shift_ olarak bilinir, ancak ben kişisel olarak _scanner sync_ terimini tercih ediyorum. Çünkü tüm renk değişimlerinin zamanlamasını scanner hareketine göre ayarladığını daha doğru anlatır.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Lazer “kuyrukları” - Colour shift düzgün ayarlanmamış</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Lazer “kuyruğu” yok! Colour shift iyi!</p></figcaption></figure></div>

Lazer çıkışınızda küçük “kuyruklar” görüyorsanız, büyük olasılıkla scanner sync ayarının yapılması gerekir. Ne yaparsanız yapın kuyruklar görünmeye devam ediyorsa, muhtemelen scanner veya lazer sürücülerinizi kaldırabileceklerinden daha hızlı çalıştırıyorsunuzdur. Scanner hızını düşürmeyi deneyin.

#### Scanner presetleri

Önceden hazırlanmış bir scanner ayarı seçmek için bunu kullanın. Varsayılan seçenek genellikle uygundur; bu yüzden özellikle kötü (veya iyi) scanner donanımınız yoksa bu ayarı değiştirmeniz gerekmez. Daha ayrıntılı incelemek isterseniz bkz. [Scanner presetleri](../../advanced/scanner-presets.md "mention")

#### Renk kalibrasyonu

Bu sistemi, lazerinizin parlaklık eğrisini ve beyaz dengesini düzeltmek için kullanabilirsiniz. Bkz. [Renk kalibrasyonu](../../advanced/colour-calibration.md "mention")

#### Gelişmiş ayarlar

Bunlarla uğraşmanız gerekmez; ama merak ediyorsanız bkz. [Gelişmiş lazer ayarları](../../advanced/advanced-laser-settings.md "mention")
