---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Renk değiştirme

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Renk değiştirme

Gelen tüm içeriğin renklerini değiştirir. Sabit HSB değerleri ayarlayabilir veya gradyan sistemine geçip özel bir gradyandan renk örnekleri alabilirsiniz.

* **hue, saturation, brightness** - renk değerleri; bkz. [Renk ayarları ve HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - renk tonu değiştirilmez
  * FIXED - öğelerin renk tonu, hue değerine ayarlanır
  * SHIFT - öğelerin renk tonu bu değer kadar kaydırılır; böylece farklı renkteki öğeler farklı kalır, yalnızca renk tonu ekseninde kayar.
* **saturation mode** -
  * OFF - doygunluk değiştirilmez
  * FIXED - doygunluk belirtilen değere sabitlenir.
* **brightness mode** -
  * OFF - parlaklık değiştirilmez
  * FIXED - öğelerin parlaklığı brightness değerine ayarlanır
  * MULTIPLY - öğelerin parlaklığı brightness değeriyle ölçeklenir; yani yanıp sönüyorlarsa yine yanıp sönerler, ancak yalnızca burada belirtilen parlaklık seviyesine kadar çıkarlar.
* **gradient mode** - sabit HSB kaydırıcılarından gradyan düzenleyiciye geçer. node, gradyandan bir renk örnekler ve ardından bunu yukarıdaki ton, doygunluk ve parlaklık modlarını kullanarak uygular.
* **gradient position** - gradyanda hangi noktanın örnekleneceğini seçer. Zaman içinde gradyan boyunca geçiş yapmak için bunu Sawtooth Oscillator ile %0'dan %100'e canlandırın.
* **blend** - renk değiştirmenin ne kadar güçlü uygulanacağını belirler. 0% hiç uygulanmaz, 100% tamamen uygulanır, 50% ise mevcut renk ile yeni değerlerin birleşimidir.

{% hint style="info" %}
Colour Change node, tüm giriş için gradyandan tek bir renk örnekler. Gradyanın konuma göre şeklin üzerine yayılmasını istiyorsanız bunun yerine [konuma dayalı değiştiriciler](position-based-changers.md "mention") kullanın.
{% endhint %}

### Gradyan düzenleyici

**gradient mode** açıkken gradyan düzenleyici ana kontrollerin altında görünür.

* Renk durağı eklemek için gradyan çubuğuna tıklayın.
* Bir durağı seçmek için sol tıklayın, ardından taşımak için yana doğru sürükleyin.
* Seçili bir durağı kaldırmak için çubuktan aşağı doğru uzağa sürükleyin veya Delete/Backspace tuşuna basın. Bir gradyanda her zaman en az iki durak kalır.
* Bir durağı renk seçiciyle düzenlemek için sağ tıklayın.
* Seçili durağı hassas şekilde düzenlemek için **Position**, **Hue**, **Saturation** ve **Brightness** seçeneklerini kullanın.
* **interpolation**, duraklar arasında renklerin nasıl harmanlanacağını seçer:
* **HSB** - ton, doygunluk ve parlaklığı harmanlar. Renk çarkı etrafında yumuşak gökkuşağı tarzı hareketler için en uygunudur.
* **RGB** - kırmızı, yeşil ve mavi değerleri doğrudan harmanlar. Bu genellikle daha çok bir ekran veya ışık konsolu renk geçişi gibi hissettirir.
* **NONE** - harmanlama yapmadan bir duraktan sonrakine atlar.
* **hue direction**, HSB interpolasyonunda kullanılabilir:
* **AUTO** - ton çarkında en kısa yolu izler.
* **FORWARDS** - ton değerleri boyunca her zaman ileri yönde ilerler.
* **BACKWARDS** - ton değerleri boyunca her zaman geri yönde ilerler.
