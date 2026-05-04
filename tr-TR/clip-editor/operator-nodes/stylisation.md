---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stilizasyon nodes

## &#x20;Randomise

Gelen öğelerin tutarlı bir noise alanı kullanılarak dağılmış kopyalarını oluşturur. Başka bir deyişle, şekillerinizi ve noktalarınızı kontrollü, “gürültülü” bir şekilde kopyalayıp hareket ettirir. Her şey tek bir yerde düzenli durmak yerine, akış içinde hareket eden parçacıklar gibi kayan ve yayılan birden fazla sürüm elde edersiniz.

* **count** – gelen her öğe için kopya sayısı (1–20). 1 değerinde, her öğenin tek bir titretilmiş sürümünü alırsınız. Daha yüksek değerler, birden fazla dağılmış kopya oluşturur.
* **noise offset** – noise alanı içinde döngüsel olarak ilerler (0–100%). Kesintisiz döngü yapar; bu yüzden bunu bir Oscillator Node ile anime etmek, tüm kopyaların birlikte akıcı ve sürekli hareket etmesini sağlar.
* **noise jitter** – noise dokusunun ölçeğini kontrol eder. Daha düşük değerler geniş ve yumuşak varyasyon verir. Daha yüksek değerler daha sıkı ve daha düzensiz yerleşim oluşturur. Bu, etkinin gücünü değil deseni değiştirir.
* **change between points** – her kopyanın bir öncekinden ne kadar farklı olacağını kontrol eder. Düşük değerler kopyaları kümelenmiş ve benzer tutar. Yüksek değerler daha fazla varyasyonla yayılmalarını sağlar.
* **face direction** – her kopyayı noise alanındaki hareket yönüne bakacak şekilde döndürür; akışla hizalanan oklar/parçacıklar üretir.
* **amount** – efektin genel gücü (0–100%). Hem yer değiştirmeyi hem de **face direction** kaynaklı döndürmeyi ölçekler.

{% hint style="info" %}
Randomise adlı node, Randomise efektinin merkezindedir!
{% endhint %}

## &#x20;Trails

İçeriğinizin yankılarını oluşturur; orijinal hareket ederken arkasında solan veya ölçeklenen kopyalar bırakır.

* **change render profile for trail** – açıksa, tüm trail kopyaları seçili **render profile** değerini kullanır. _Bkz._ [Render profili](../fundamentals/render-profile.md "mention").
* **render profile** – yukarıdaki anahtar açıkken trail kopyaları için kullanılacak profil. Genellikle ana içerik **DETAIL** olarak ayarlanmışken yankıların **FAST** olarak render edilmesi için kullanılır. Böylece ana şekillerde net ayrıntı korunur, trails ise daha verimli render edilir.
* **delay** – trail kopyaları arasındaki aralığı müzikal zamanla ayarlar; **1/64 nota adımları** cinsinden ölçülür.\
  Referans olarak:
  * 16 = 1/16 ölçü (onaltılık nota)
  * 32 = 1/8 ölçü (sekizlik nota)
  * 64 = 1/4 ölçü (dörtlük nota)
  * 128 = 1/2 ölçü (ikilik nota)
  * 256 = 1 ölçü
* **trail size** – canlı içeriğin arkasına çizilecek trail kopyası sayısı.
* **prefill trails** – Clip başladığında iz geçmişini hemen doldurur; yankıların ilk birkaç vuruş boyunca oluşmasını beklemez.
* **freeze trails** – akıcı şekilde ilerleyen trails görünümünü donmuş anlık görüntüler dizisine dönüştürür. Kesik, beat ile senkron trail efektleri oluşturmak için kullanışlıdır.
* **brightness start / brightness end** – trail boyunca parlaklığı en yeni kopyadan (**start**) en eski kopyaya (**end**) uygular. Genellikle **brightness start** 100%, **brightness end** 0% olarak ayarlanır; böylece yankılar sönerek kaybolur.
* **scale start / scale end** – trail boyunca ölçeklemeyi en yeni kopyadan (start) en eski kopyaya (end) uygular. Sıfıra kadar küçülen trails için **scale start** değerini 100%, **scale end** değerini 0% yapın.

## &#x20;Shimmer

İçeriğinize hafif parıltıdan yoğun strobe etkisine kadar değişebilen, titreşen bir parlaklık varyasyonu ekler.

* **speed** – shimmer değerinin zaman içinde ne kadar hızlı değiştiğini belirler. Daha yüksek değerler daha hızlı titreşim oluşturur; 0 efekti duraklatır.
* **separation** – komşu noktaların/öğelerin birbirinden ne kadar farklı olacağını belirler.
  * 0: her şey birlikte shimmer yapar.
  * \>0: yakındaki noktalar giderek farklı fazlar alır; böylece shimmer şekil boyunca değişir.
  * <0: yukarıdakiyle aynıdır, ancak faz ilerlemesi ters yönde çalışır.
* **threshold** – noktalar artık yumuşakça solmak yerine parlaklıklarına bağlı olarak tamamen açık veya kapalı yanıp söner. Daha parlak öğeler daha sık görünür; ancak 100% parlaklıktaki öğelerin her zaman açık, 0% parlaklıktaki öğelerin ise her zaman kapalı olduğunu unutmayın. Keskin ışıltı veya yıldız ışığı efektleri için kullanışlıdır.

{% hint style="info" %}
**threshold** seçeneğini açmak, parçacıklarınıza veya içeriğinize gerçekten canlılık katabilen harika gizli özelliklerden biridir. Noktalar solmak yerine, parlaklıklarına göre hızla açılıp kapatılır. Herhangi bir anda daha az nokta çizildiği için sonuç daha parlak Output ve daha akıcı animasyondur.

Ancak içeriğiniz zaten 100% parlaklıktaysa hiçbir şey yapmayacağını unutmayın!
{% endhint %}

* **use whole shape** – tüm şekle tek bir shimmer değerini eşit şekilde uygular. Kapalıyken node, şekilleri alt bölümlere ayırır; böylece farklı parçalar benekli bir görünüm için bağımsız olarak parıldayabilir.

## &#x20;Particles

Bu, içeriğinize göre parçacıklar üreten ve anime eden deneysel bir efekttir. İçeri giren nokta tabanlı tüm öğeler yayıcı konumları olarak işlenir. Parçacık yolları önceden hesaplandığı için giriş içeriğiniz değişirse parçacıkları güncellemek üzere yenilemeniz/yeniden hesaplatmanız gerekebilir (herhangi bir ayarı değiştirmeniz yeterlidir).

**General**

* **keep original** – açıksa, orijinal içerik korunur ve parçacıklar üzerine eklenir. Yayıcı noktaların görünür kalmasını istediğinizde kullanışlıdır.
* **number of particles** – her yayımda kaç parçacık oluşturulacağını belirler. Daha yüksek değerler daha yoğun efektler, daha düşük değerler daha sade sonuçlar üretir.
* **emission period** – parçacıkların yayıldığı döngü aralığıdır (ölçü cinsinden). 100% değerinde döngü boyunca eşit dağılırlar; daha küçük değerler onları patlamalar için bir araya toplar.
* **loop length** – parçacık döngüsünün ne kadar süreceğini belirler; müzikal ölçü cinsinden ölçülür.
* **loop count** – sıfırlanmadan önce döngünün kaç kez tekrarlanacağını belirler. 1 olarak ayarlanırsa parçacıklar her seferinde tam olarak aynı simülasyonu izler; bu da sonucu tamamen tekrarlanabilir yapar. Daha yüksek değerler, döngü sıfırlanmadan önce daha fazla varyasyon ekler.
* **delay** – zamanlama efektleri için yayımın başlangıç zamanını belirli sayıda 1/64 nota kadar kaydırır.

**Motion**

* **speed** – parçacıkların yayıcıdan ne kadar hızlı uzaklaştığını belirler.
* **speed variation** – parçacıkların hepsinin aynı hızda hareket etmemesi için rastgelelik ekler. Daha doğal bir yayılım oluşturur.
* **direction** – parçacıkların ateşlendiği temel yönü belirler; **x, y, z açıları** ile tanımlanır. Bu açılar ateşleme vektörünü 3D uzayda döndürür; böylece parçacıkları doğrudan yukarı, yana veya herhangi bir çapraz yöne yöneltebilirsiniz. Daha geniş koniler veya daha kaotik patlamalar için **spread** ile birlikte kullanın.

{% hint style="info" %}
**Euler açıları**\
Liberation, 3D uzayda yönelimi tanımlamak için **Euler açıları** kullanır. Bunlar, üç ana eksen etrafındaki basit dönüşlerdir:

* **X** – öne/arkaya eğilme (başınızı sallayarak “evet” demek gibi)
* **Y** – sola/sağa dönme (başınızı sallayarak “hayır” demek gibi)
* **Z** – saat yönünde/saat yönünün tersine yuvarlanma (başınızı yana eğmek gibi)

Bu üç değeri ayarlayarak parçacıkları istediğiniz yöne çevirebilirsiniz.
{% endhint %}

* **direction variation** – bu yönün etrafına rastgele yayılım ekler. Koniler, püskürmeler veya patlamalar oluşturmak için kullanışlıdır.
* **drag** – parçacıkları zamanla yavaşlatır. Daha yüksek değerler onları daha ağır ve daha hantal hissettirir.
* **gravity** – parçacıkları aşağı çeker (pozitif) veya yukarı iter (negatif).
* **gravity variation** – her parçacık için yerçekimine varyasyon ekleyerek hareketi daha kaotik hale getirir.

**Life**

* **life duration** – parçacıkların ne kadar süre var olacağını belirler (1/64 nota birimleriyle ölçülür). Daha kısa değerlerde parçacıklar hızla kaybolur; daha uzun değerlerde ise daha uzun süre görünür kalır.
* **life variation** – parçacık ömrüne rastgelelik ekler; böylece hepsi aynı anda kaybolmaz.
* **start delay / start delay variation** – her parçacığın ne zaman görünür hale geleceğini geciktirir (1/64 nota adımlarıyla). Parçacık bu süre boyunca zaten oluşturulmuş ve hareket ediyor olur, ancak parlaklığı 0’da tutulur; bu yüzden gecikme dolana kadar görünmez kalır. Gecikmeli havai fişek “kıvılcımlarının” belirmesini istediğinizde kullanışlıdır.

**Colour & brightness**

* **hue start** – parçacıkların başlangıç rengi.
* **hue variation** – parçacıkların hepsinin aynı renkle başlamaması için rastgelelik ekler.
* **hue change** – parçacığın ömrü boyunca hue değerini kaydırır ve renk değiştiren trails oluşturur.
* **brightness start / brightness end** – parçacığın ömrü boyunca parlaklığı uygular. Genellikle **brightness start** yüksek, **brightness end** düşük ayarlanır; böylece parçacıklar doğal şekilde sönerek kaybolur.
* **brightness variation** – daha dinamik bir görünüm için başlangıç parlaklığını rastgeleleştirir.
* **saturation start / saturation end** – rengin başlangıçta ve sonda ne kadar canlı olacağını ayarlar.
* **saturation variation** – parçacıklar arasında çeşitlilik için saturation değerini rastgeleleştirir.

**Simulation**

* **time adjustment** – tüm parçacık simülasyonunu hızlandırır veya yavaşlatır. Farklı tempolara senkronlamak ya da hareketi abartmak için kullanışlıdır.
