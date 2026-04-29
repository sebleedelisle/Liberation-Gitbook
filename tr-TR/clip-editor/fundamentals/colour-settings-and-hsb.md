---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Renk ayarları ve HSB

Liberation içinde renk, RGB yerine HSB olarak tanımlanır. Bu size yabancı gelebilir, ancak alıştığınızda çok daha sezgisel bir sistem olduğunu düşünüyorum.

{% hint style="info" %}
RGB kullanmayı tercih ederseniz herhangi bir renk ayarında renk karesine tıklayabilirsiniz. Bu, RGB ve HSB seçenekleri sunan renk düzenleyici panelini açar.
{% endhint %}

### HSB - Hue, Saturation ve Brightness

#### Hue

Renk tonu 0 ile 255 arasında değişir. 0 kırmızıdır; değeri artırdıkça gökkuşağındaki tüm tonlardan geçersiniz: turuncu, sarı, yeşil, camgöbeği, mavi, mor, macenta ve 255’te tekrar kırmızı.

Bu bir döngü olduğu için tüm renkler arasında geçiş yapmak üzere bir triangle wave kullanabilirsiniz.

#### Saturation

Bu ayar renginizin doygunluğunu, yani canlılığını ayarlar. Başka bir deyişle rengin ne kadar _renkli_ olduğunu belirler ve 0 ile 255 arasında değişir. Gri tonlar için Saturation değerini 0’a, tam gökkuşağı renkleri için 255’e ayarlayın. Ortalarda bir değer, soluk pastel renkler verir.

{% hint style="info" %}
colour kelimesindeki fazladan sesli harf için ABD’li arkadaşlarımdan özür dilerim. Liberation İngiltere’de geliştirildiği için varsayılan dil British English. Gelecekte Fransızca, İspanyolca, Almanca, İtalyanca, Basitleştirilmiş Çince ve evet, hatta US English çevirileri de sunmayı umuyorum. :innocent:
{% endhint %}

#### Brightness

Muhtemelen anlaşılması en kolay olanı: 0 tamamen siyah, 255 tam parlaklıktır.

### Örnek kullanım

#### Gökkuşağı döngüsü:

_Brightness_ ve _Saturation_ değerlerini 255’e ayarlayın. Bir _Sawtooth_ osilatörünü _Hue_ socket’ine bağlayın ve aralığını 0’dan 255’e ayarlayın.

#### Nabız gibi değişen parlaklık:

Bir _Sawtooth_ osilatörünü _Brightness_ socket’ine bağlayın ve aralığını 255’ten 0’a ayarlayın. Değişimin süresini kontrol etmek için clamp min ve max değerlerini ayrıca ayarlayabilirsiniz. Ardından animasyonu daha da iyileştirmek için easing fonksiyonlarını kullanın.

#### Sert flash / strobe:

_Hue_ ve _Saturation_ kullanarak veya renk seçiciye tıklayarak bir renk seçin. Bir _Square Wave_ osilatörünü _Brightness_ socket’ine bağlayın ve aralığını 255’ten 0’a ayarlayın.

#### Özel bir renk tonu aralığında döngü:

_Brightness_ ve _Saturation_ değerlerini 255’e ayarlayın. Bir _Triangle Wave_ osilatörünü _Hue_ socket’ine bağlayın ve aralığını ayarlayın:

* maviden camgöbeğine geçiş için 70 ile 128 aralığını kullanın
* kırmızıdan sarıya geçiş için 0 ile 40 aralığını kullanın
* kırmızıdan macentaya geçiş için 255 ile 220 aralığını kullanın
