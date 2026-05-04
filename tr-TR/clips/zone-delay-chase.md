---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Daha fazla lazerin daha fazla eğlence anlamına geldiği konusunda hepimiz hemfikiriz. Ama hepsi aynı şeyi yapıyorsa yaratıcı olasılıkların önemli bir kısmını kaçırırsınız.

Zone delay sistemi, zone öğeleri arasında çeşitlilik oluşturmanın basit ama etkili bir yoludur ve çoklu lazer kurulumundan gerçekten en iyi şekilde yararlanmanızı sağlar. Daha geleneksel bir chase efekti yapmak için de kullanılabilir.

#### Nasıl çalışır

_Zone delay_, Clip zamanlamasına her zone için bir gecikme ekler ve zones arasında bir tür süpürme hareketi oluşturur.

Zaten çalışan bir Clip üzerine zone delay eklemek çok etkilidir. Seviyeyi ve pattern seçimini ayarlamak için APC40 üzerindeki ilgili kontrolü kullanın. (Bkz. [APC40 referansı](../reference/apc40-reference.md "mention")). İsterseniz _Clip Settings_ panelini de kullanabilirsiniz.

Zone delay ayarları:

* **Zone delay** - her zone için uygulanan gecikme süresini kontrol eder; 64’lük nota değerleriyle ölçülür.
* **Pattern** - zone sırasını seçin
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern, zone numaralarına göre çalışır ve zones öğelerinin soldan sağa sıralı olduğunu varsayar. Zone delay, pattern hesaplaması yaparken canvas zones ve DMX zones öğelerini ayrı gruplar olarak değerlendirir.
{% endhint %}

* **Delay mode**
  1. No delay - chase mode içinde bunu kullanın
  2. Delay - varsayılan moddur; her zone için zamanlamayı geciktirir
  3. Delay with re-trigger - Pattern boyunca her seferinde Clip öğesini başa sarar. Bu, _Chase mode_ ile iyi çalışır.
* **Chase mode** - chase mode açıkken her zone, geleneksel bir chase efekti gibi açılıp kapanır. Chase görünümünü _Fade in, Hold,_ ve _Fade out_ ayarlarıyla düzenleyin. Bu ayarlar, zone delay değerinin oranı olarak belirlenir; yani 1 değeri, _Zone delay_ değerinde belirtilen süreyle aynı olur. Anlatması biraz zor, bu yüzden tavsiyem kendiniz denemeniz.

{% hint style="info" %}
Zone delay, etkin olan tüm efektlere de uygulanır. Örneğin yanıp sönen bir efekt, Clip içindeki animasyonla birlikte zones arasında gecikmeli ilerler.
{% endhint %}

Bir Clip herhangi bir _Zone delay_ kullandığında, Clip öğesinin sağ üst köşesinde üç noktalı bir simge görürsünüz. Bu noktalar, o Clip için kullanılan _Zone delay_ stilini gösterecek şekilde animasyonludur. Daha fazla bilgi için [Clip düğmelerindeki küçük simgeler nelerdir?](what-are-the-small-icons-on-the-clip-buttons.md "mention") bölümüne bakın.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Bir Clip içinde zone delay olduğunu ve hangi modda olduğunu gösteren üç nokta simgesi</p></figcaption></figure>

{% hint style="info" %}
Zone delay, her Clip öğesine ait bir ayardır; global değildir. Bir Clip öğesinin yaratıcı tasarımının parçasıdır.
{% endhint %}
