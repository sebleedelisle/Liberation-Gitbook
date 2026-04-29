---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scanner teknik özellikleri ve Liberation

### Scanner teknik özelliklerinin karmaşık gerçeği

Nokta hızları ve scanner teknik özellikleri biraz kafa karıştırıcı olabilir. Sık sık 30kpps @ 8º veya 50kpps @ 4º gibi değerler görürsünüz, ancak bu sayıların gerçekte neyi ifade ettiği her zaman açık değildir.

{% hint style="info" %}
Sorumluluk reddi - Scanner donanımı uzmanı değilim, ancak donanım ayarı yapmak yerine yazılım ve point stream üretimiyle farklı kalitedeki scanner sistemlerinin iyi görünmesini sağlama konusunda yıllara dayanan pratik deneyimim var. Bu açıklamalar o deneyime dayanıyor.
{% endhint %}

#### **Bu değerler nereden geliyor?**

“30K” ve “50K” gibi terimler, scanner sistemlerinin belirli koşullarda bu nokta hızlarında ILDA test pattern kullanılarak değerlendirilmesine dayanan kısa ifadelerdir.

Bir scanner için şöyle bir değer verildiğinde: _30Kpps @ 8°_ aslında şu anlama gelir:

> “Bu scanner, doğru ayarlandığında 8° tarama açısında saniyede 30.000 nokta ile ILDA test pattern’ı yeniden üretebilir.”

Bu, gerçek dünya performansının kapsamlı veya tamamen standartlaştırılmış bir ölçümü değildir. Hatta başlangıçta bir benchmark olarak tasarlanmamıştı; bir **ayar prosedürü** için kullanılıyordu. Bilinen bir deseni sabit bir nokta hızında çalıştırırsınız (ör. saniyede 30.000 nokta) ve doğru görünene kadar damping ve gain ayarlarını yaparsınız.

Yine de elimizdeki en yaygın referans hâlâ budur ve en azından güvenilir üreticilerde scanner kalitesi hakkında iyi bir fikir verebilir. Ama _daha az güvenilir_ olanlarda...

#### Scanner sistemlerini belirtilen değerlere göre test etmek istiyorsanız

{% hint style="danger" %}
**Bu ileri seviye bir tekniktir ve dikkatli olmazsanız scanner sistemlerinize zarar verebilirsiniz. Ne yaptığınızı bilmiyorsanız önerilmez.**
{% endhint %}

[ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) çıktısı verebilen bir yazılım bulmanız gerekir. LaserShowGen bunu yapabiliyor olabilir diye düşünüyorum. Ardından çıkış boyutunu belirtilen tarama açısına uyacak şekilde ayarlayın (ör. 8°). Çıktıyı nasıl analiz edeceğinizle ilgili öneriler için ILDA belgelerine bakın.

#### Neden iyi bir benchmark olmayabilir?

Öncelikle, scanner sistemleriniz iyi olsa bile test pattern yanlış görünebilir; çünkü ayarları bu test için optimize edilmiş olmayabilir.

“İyi” ve “kötü” scanner ayrımı için genel bir kılavuz olarak faydalı olabilir, ancak üreticiler bazen bu teknik özellikleri fazlasıyla esnek yorumlayabilir.

#### Peki iyi bir scanner nasıl seçilir?

Bence en önemli şey, güvenilir bir üretici tarafından yapılmış olmaları. Cambridge Technology (CT), Eye Magic (EMS) ve ScannerMAX (Pangolin’in bir iştiraki) gibi pahalı üst seviye scanner üreticileri her zaman iyidir; bu markalarla genelde yanlış yapmazsınız. Ama bir çift scanner yaklaşık 1000 $ seviyesine geldiğinde, yeni başlayan çoğumuz için bu tutar lazerlerimizden bile pahalı olabilir!

Bu yüzden ben çoğunlukla Çinli üreticiler kullandım. Dragon Tiger (DT) scanner sistemleri makul kaliteli ve uygun fiyatlıdır; sanırım LightSpace de bunları kullanıyor. Birçok başka üretici de (bazı modellerde OPT ve Able dahil) DT tabanlı sistemler kullanır.

Phenix Technology (PT) genel olarak daha alt seviyededir, ancak dürüst olmak gerekirse çoğu iş için muhtemelen yeterlidir.

**Scanner sistemleriniz markasızsa, kalite konusunda endişelenmeniz gereken yer muhtemelen orasıdır!**

#### Liberation nasıl yardımcı olur?

Öncelikle, çoğu iş için gerçekten pahalı scanner sistemlerine ihtiyacınız yoktur. Uygun fiyatlı 30kpps DT, hatta PT bile yeterli olacaktır. Varsayılan scanner ayarları bilinçli olarak temkinli tutulmuştur ve çoğu durumda _bunları ayarlamanız gerekmez_ (_Scanner sync_ hariç).

Daha iyi scanner sistemleriniz olsa bile, gerekenden daha zorlamanın bir anlamı yoktur. Bu, kullanım ömürlerini belirgin şekilde uzatır.

#### "Point stream" nedir?

Bu terimi muhtemelen daha önce duymuşsunuzdur; scanner yolunu bu şekilde kontrol ederiz.

Point stream, her biri bir renge sahip X/Y konumlarından oluşan bir listedir. Beyaz bir çizgi gibi bir şey çizmek için, o çizgi boyunca beyaza ayarlanmış bir nokta dizisi gönderirsiniz. Scanner daha sonra sabit bir hızda, yani saniye başına nokta hızında (PPS), noktadan noktaya hareket eder ve ışın şekli çizer.

#### Geleneksel lazer yazılımlarında bu nasıl çalışır?

Geleneksel lazer yazılımları her cue için bir point stream saklar. Animasyonlu cue’larda bu genellikle her frame için ayrı bir point stream anlamına gelir. Önemli nokta şudur: Her şey tamamen önceden belirlenmiştir. Sonuç olarak, nokta hızını artırmak scanner sistemlerinin aynı önceden tanımlanmış veri içinde daha hızlı hareket etmesini sağlar.

{% hint style="info" %}
Eski yazılımlarda bu yaklaşım gerekliydi; bilgisayarlar point stream’leri gerçek zamanlı üretmek için yeterince hızlı değildi. Bu yüzden genellikle her animasyon frame’i için veriyi önceden üretmekte kullanılan ayrı bir cue editor bulunur.

Bu aynı zamanda içeriğin neden gigabaytlarca yer kaplayabildiğini de açıklar. Aslında oldukça yüksek örnekleme hızlarında büyük, sıkıştırılmamış dalga formları saklamış olursunuz.
{% endhint %}

#### Liberation’da "point rate" neden daha az anlamlı?

Liberation point stream’i gerçek zamanlı üretir; bu da bize çok büyük bir esneklik sağlar. Laser Settings panelindeki "Scanner speed" ayarına dikkat edin. Bu ayar scanner sistemlerini hızlandırıp yavaşlatmamızı sağlar, ancak önemli olan şu: Temel nokta hızını (PPS) **değiştirmez**.

#### Bir dakika, nasıl yani?

Biliyorum, ilk başta tuhaf geliyor.

Liberation point stream’i gerçek zamanlı ürettiği için bu point stream’i ayarlayabilir. Noktalar birbirinden ne kadar uzaksa scanner o kadar hızlı hareket eder. Noktalar birbirine ne kadar yakınsa scanner o kadar yavaş hareket eder.

{% hint style="info" %}
Liberation’ın son sürümlerinde gerçek _point rate_ değeri (gelişmiş ayarlarda) scanner hızını hiç etkilemez. Bunun yerine renderer, scanner hareketini değiştirmeden, nokta dağılımını seçilen nokta hızına uyacak şekilde ayarlar.

Bunun nokta yolunun “çözünürlüğü” üzerinde bir etkisi vardır, ancak bu çoğunlukla grafiklerde fark yaratır (ve _scanner sync_ ayarının daha hassas yapılmasına yardımcı olabilir).
{% endhint %}

#### Harika! Peki bütün bunlar pratikte ne anlama geliyor?

İyi soru. Benim önerilerim şunlar:

* Markasız scanner sistemlerinden kaçının. Daha hızlı scanner alabiliyorsanız alın; minimum 30KPPS.
* Çoğu durumda DT30 scanner yeterlidir, daha ucuz lazerlerde PT30 scanner da muhtemelen sorun çıkarmaz.
* Grafik yapıyorsanız, çoğu durumda daha hızlı scanner yerine daha fazla lazer daha iyi sonuç verir.
* Daha üst seviye kurulumlara geçtiğinizde, bilinen üst seviye markaların herhangi biri gayet iyi olacaktır.
* Yalnızca en ucuz markasız scanner sistemlerini alabiliyorsanız, Liberation’ın varsayılan ayarları oldukça temkinlidir ve temel beam çalışmaları için muhtemelen kabul edilebilir sonuç alırsınız. Zorlanıyorsa **Speed** ayarını düşürün (ama point rate değerini değiştirmeyin!).

#### Peki ILDA Test Pattern?

…kalibrasyon ve referans aracı olarak hâlâ çok kullanışlıdır, ancak hiçbir zaman kapsamlı bir benchmark olarak tasarlanmamıştır ve üreticiler tarafından yanlış kullanılabilir veya gevşek şekilde yorumlanabilir.
