---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Dalga osilatörleri

## Bu sayfada:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Testere dişi dalga](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Üçgen dalga](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sinüs dalgası](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Kare dalga](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Gürültü](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Özel Osilatör](wave-oscillators.md#custom-oscillator-1)

## Wave oscillator ayarları

Tüm Wave oscillator’larda aşağıdaki ayarlar bulunur:

* **range min / range max** - osilatörün kontrol ettiği özelliğin değer aralığını belirler. Dalga formu en alttayken özellik _range min_ değerine, en üstteyken _range max_ değerine ayarlanır.

{% hint style="info" %}
Örneğin bir noktanın -100 ile 100 arasında sola ve sağa hareket etmesini istiyorsanız, osilatörü _x özellik soketine_ bağlayıp _range min_ değerini -100, _range max_ değerini 100 olarak ayarlarsınız.
{% endhint %}

* **duration** - bir tam döngünün ya da _loop_ işleminin tamamlanması için geçen süre. Bu değer, tempoya göre ölçü cinsinden hesaplanır. Yani ¼ tek bir vuruştur. 1 tam bir ölçüdür vb.
* **duration multiplier** - temel süreyi seçilen bir katsayıyla ölçekler. Örneğin duration dörtlük notaya, multiplier ise 3’e ayarlanırsa osilatör üç dörtlük nota kadar sürer; yani noktalı yarım nota. Kesirli çarpanlar da desteklenir. Tam sayı olmayan değerler ayarlamak için kaydırıcıyı sürüklerken _SHIFT_ tuşunu basılı tutun. Bu, faz kaydırma efektleri veya küçük zamanlama kaymaları oluşturmak için kullanışlıdır.
* **offset** - dalganın başlangıç ofsetini, sürenin yüzdesi olarak belirler. Dalganın yolun dörtte birinden başlamasını istiyorsanız bunu 25% olarak ayarlayın.
* **repeat count** - loop durmadan önce kaç kez çalışacağını belirler. Varsayılan değer _FOREVER_ şeklindedir; ancak osilatörün süresiz çalışmasını istemiyorsanız bunu değiştirebilirsiniz. Durduktan sonra özellik, dalganın sonundaki değere ayarlanır.
* **delay count** - osilatör çalışmaya başlamadan önceki gecikmeyi vuruş cinsinden belirler. Çalışmaya başlamadan önce özellik, dalganın başlangıcındaki değere ayarlanır.

{% hint style="info" %}
_repeat count_ ve _delay count_ ayarlarını dikkatli kullanarak oldukça karmaşık animasyonlar oluşturabilirsiniz; neredeyse kendi timeline’ı gibi!
{% endhint %}

## Ortak ayarlar

* **steps** - hareketi belirli sayıda ayrık adıma böler. Özelliklerin yumuşak hareket etmek yerine değerlere “zıplamasını” istediğiniz durumlar için uygundur.

{% hint style="info" %}
Adımların değere göre değil zamana göre bölündüğünü unutmayın. Yani 1 ölçü duration değerine sahip ve 4 adıma bölünmüş bir dalgada özellik her vuruşta anında değişir.
{% endhint %}

* **clamp min / clamp max -** dalganın ölçeğini minimum veya maksimum değerlerinin ötesine artırır ve sonucu sınırlar.

{% hint style="info" %}
_clamp_ kavramını açıklamak biraz zor; dalga formunun grafiğin üstünden ya da altından dışarı taştığını ve sonra kenarlara sıkıştırıldığını düşünün. Bunları denemenizi öneririm! Özellikle bir testere dişi dalganın geç başlamasını veya erken bitmesini istiyorsanız çok kullanışlıdır.
{% endhint %}

* **ease function** - Sawtooth ve Triangle dalgalarında ayrıca animasyon eğrisini hafifçe değiştiren ve animasyonlarınızı çok daha etkileyici hale getirebilen bir ease function bulunur.
  * **LINEAR** - varsayılandır; yumuşatma yoktur, min ve max değerler arasında doğrusal şekilde hareket eder.
* **EASE OUT** - hızlı başlar ve sona yaklaşırken yavaşlar. Fiziği simüle etmek, örneğin durana kadar yavaşlama efekti için çok iyidir.
  * **EASE IN** - yavaş başlar ve kademeli olarak hızlanır. Momentum birikimini simüle etmek için uygundur.
  * **EASE IN/OUT** - ikisinin birleşimidir ve oldukça organik bir hareket verir.

{% hint style="warning" %}
**Yumuşatma -** Özellikle robotik görünen bir hareket istemiyorsanız, mümkün olduğunca varsayılan doğrusal animasyondan kaçınmanızı öneririm. Yumuşatma, animasyonlarınızı çok daha akıcı ve organik hale getirebilir!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Testere dişi dalga

Bazen _rampa dalga formu_ olarak da bilinir; çünkü döngüsü boyunca yukarı doğru rampalanır ve döngünün sonunda keskin şekilde düşer. _hue_ veya _rotation_ gibi özellikleri döngüsel olarak değiştiren bir loop oluşturduğu için muhtemelen en yaygın dalga osilatörüdür.

Aşağıdaki ayarlar için yukarıdaki bölümlere bakın:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Testere dişi dalgaya özel:

* **cycle range compensation** - **steps** ayarlı olduğunda kullanılabilir. Örneğin 0’dan 360’a bir rotation gibi değerleri döngüsel kullanmak için uygundur. Bu ayar kapalıyken başlangıç ve bitiş değerleri aynı olur; bu da başlangıç noktasında takılmaya yol açabilir, çünkü 0 ve 360 aynı açıdır. Bunu açtığınızda adım konumlarını düzeltmek için maksimum aralık azaltılır.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Üçgen dalga

Her döngüde başa sıçrayan _testere dişi dalganın_ aksine, _üçgen dalga_ doğrusal olarak ileri ve sonra geri hareket eder.

Aşağıdaki ayarlar için yukarıdaki bölümlere bakın:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sinüs dalgası

En yumuşak dalga formu! İki değer arasında bir sarkaç gibi nazikçe salınır.

Aşağıdaki ayarlar için yukarıdaki bölümlere bakın:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Kare dalga

En basit dalga formu; iki değer arasında ileri geri gidip gelir!

Aşağıdaki ayarlar için yukarıdaki bölümlere bakın:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Kare dalgaya özel:

* **pulse width** - dalganın genel duration değerine göre maksimum değerinde kaldığı süre. Varsayılan değer 50%’dir; yani süre tam olarak yarı yarıyadır. Yalnızca sürenin dörtte biri boyunca “açık” olmasını istiyorsanız 25% olarak ayarlayın. Bu darbenin ne zaman gerçekleşeceğini _offset_ değeriyle ayarlayabilirsiniz.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Gürültü

Liberation yazılımının güçlü yönlerinden biri, rastgele ama tekrarlanabilir efektler üretebilmesidir. _noise_ osilatörü, istediğiniz kadar ayrıntı veya titreşim içeren organik, döngülü ve rastgele bir hareket oluşturmak için kullanılabilir.

Aşağıdaki ayarlar için yukarıdaki bölümlere bakın:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Gürültüye özel:

* **noise type** - gürültüyü üretmek için kullanılan algoritma.
  * **SIMPLEX** - varsayılandır; yükselip alçalan, dalgalanan ve loop içinde tekrarlanan bir değer üretir.
  * **RANDOM** - daha geleneksel bir rastgele sayı algoritması kullanır; tamamen gürültülü ve kaotiktir.

{% hint style="info" %}
**Simplex noise**, Ken Perlin tarafından 2001 yılında, 1983’te _Tron_ filmi üzerindeki çalışmaları sırasında geliştirdiği “Perlin noise” algoritmasının geliştirilmiş hali olarak tasarlandı. Bu çalışmasıyla Oscar kazandı!

Bu “gradient” gürültü, daha önceki “makine gibi” görünen bilgisayar üretimli görüntülerden duyduğu rahatsızlıktan doğdu. CGI dünyasında özellikle bulutları, su yüzeylerini ve hatta gerçekçi arazi için height-map’leri oluşturmakta çok başarılıdır.

Liberation içinde ise hâlâ yumuşak ve organik kalan, görünüşte öngörülemez hareketler oluşturmak için kullanışlıdır.
{% endhint %}

* **seed** - gürültüyü oluşturmak için kullanılan değer. Elinizdeki gürültü dalgasının görünümünü beğenmezseniz bu değeri değiştirmeyi deneyin.

{% hint style="info" %}
Eğlenceli ve nerd bir bilgi! Kusursuz şekilde loop yapan simplex noise elde etmek için 2D gürültü düzleminde bir daire etrafında ilerliyorum. Seed değerini değiştirmek ise bu düzlemi 3. boyutta hareket ettiriyor!
{% endhint %}

* **simplex detail** - gürültünün ne kadar ayrıntılı veya titreşimli olduğunu değiştirir. Tekrarlanan desenin daha az belirgin olmasını istiyorsanız duration değerini artırın ve bu değeri yükseltin.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Özel Osilatör

Tamamen özel dalga formları oluşturur. Karmaşık animasyonlar oluşturmak için çok kullanışlıdır.

Aşağıdaki ayarlar için yukarıdaki bölümlere bakın:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Bunun altında konum ve değerlerden oluşan bir liste bulunur. Duration 64 adıma bölünür ve bu noktalardan herhangi birine değer yerleştirebilirsiniz.

Her adımda aşağıdaki ayarlar bulunur:

* **Step** - duration içindeki zaman adımı. 0 başlangıçta, 64 ise sondadır.
* **Level** - o zaman adımındaki dalga seviyesi. Level değeri 0 ile 1 arasındadır.
* **Animation type** - açılır menü, önceki adımdan bu seviyeye nasıl geçileceğini seçmenizi sağlar.
  * **None** - geçiş yoktur; belirtilen zamanda doğrudan bu seviyeye atlar.
  * **Linear** - önceki seviyeden bu seviyeye tamamen doğrusal bir hareket yapar.
  * **Ease in / Ease out / Ease in/out** - önceki seviyeden bu seviyeye yumuşatılmış geçiş yapar. Animasyon türlerinin açıklaması için yukarıdaki _ease function_ bölümüne bakın.

***
