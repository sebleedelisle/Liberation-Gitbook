# ✅ Hızlı başlangıç kılavuzu

## Giriş

**Liberation**’a hoş geldiniz; yeni nesil lazer gösterisi yazılımı.

Liberation güçlü ve kapsamlı bir modern yazılımdır. Yaratıcılığınızı özgürce ifade edebilmeniz için kullanılabilirlik ve güvenilirlik temelleri üzerine kurulmuştur. Hızlı, verimli ve akıcıdır. Kısa sürede çalışmaya başlamak için bu _Hızlı başlangıç kılavuzunu_ izleyin!

### Lazerleri yönetme

Liberation, hiç fiziksel lazer bağlı olmasa bile lazerleri kurup görselleştirebileceğiniz kadar esnektir. Hazır olduğunuzda da her çıkışı sorunsuz şekilde bir lazer kontrolcüsüne atayabilirsiniz.

{% hint style="info" %}
Liberation içinde istediğiniz kadar lazer kurabilir ve görselleştirebilirsiniz. Lisans katmanları (Hobbyist, Pro vb.) yalnızca _devreye alabileceğiniz_ lazer sayısını sınırlar. Yani ücretsiz lisansla bile 100 lazerli bir lazer gösterisi tasarlayabilirsiniz. Yükseltme yalnızca bunu gerçek lazerlerde çalıştırma aşamasında gerekir.
{% endhint %}

Varsayılan kurulumda yatay olarak dizilmiş 8 lazer bulunur, ancak bunu istediğiniz gibi özelleştirebilirsiniz. Yazılımı tanırken bu varsayılanı korumak muhtemelen en iyisidir; daha sonra donanım kurulumunuza uyacak şekilde ayarlayabilirsiniz. (Bkz. [Projenizi ayarlama](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Önemli: Herhangi bir lazeri devreye almadan önce riskleri anladığınızdan emin olun ve [Lazerleri ayarlama](../setting-up/setting-up-lasers.md "mention") bölümünü dikkatlice inceleyin.
{% endhint %}

## Yazılıma genel bakış

### Güvenlik kapatması

Lazerleri çalıştırdığınız her zaman elinizin altında bir **donanımsal acil durdurma düğmesi** bulunmalıdır (bkz. [Acil durdurma ve güvenlik kilitleme bağlantıları](../hardware/emergency-stop-interlocks.md "mention")). Ancak her şeyi daha az acil bir şekilde devreden çıkarmak isterseniz _**DISARM ALL**_ düğmesini veya `Escape` tuşunu kullanabilirsiniz (APC40 üzerindeki _**SESSION**_ tuşu da kullanılabilir). Ayrıca ekrandaki kaydırıcıyı veya APC40 üzerindeki ana fader’ı kullanarak Global Brightness değerini azaltabilirsiniz.

### Kaydırıcı öğeleri

Liberation genelinde çeşitli kaydırıcılar ve kontroller bulunur.

{% hint style="info" %}
Kaydırıcının sağladığından daha hassas kontrol gerekirse, yeni bir değer yazmak için bir kaydırıcıya `Cmd / Ctrl` tuşuyla tıklayın.
{% endhint %}

### Klavye kısayolları

Klavye kısayollarının tam listesini burada bulabilirsiniz: [Klavye kısayolları](../reference/keyboard-shortcuts.md "mention")

### Ekran yerleşimi

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Belirli bir düğmenin ne işe yaradığından emin değil misiniz? Açıklamasını görmek için fare imlecini üzerine getirin!
{% endhint %}

#### Menü

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menüde tüm dosya içe/dışa aktarma seçeneklerini ve panelleri açma komutlarını bulabilirsiniz. Ayrıca bilgisayarı aboneliğinizle yetkilendirme seçeneği de buradadır (_Liberation -> Authorise/Deauthorise this computer_).

#### Simge çubuğu

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Tüm lazerleri devreye alma/devreden çıkarma, Global Brightness, Test Pattern ve 3D, Canvas ile Output view arasında geçiş yapma gibi yaygın görevler burada bulunur.

### Görünümler

Ekranın sol üstündeki büyük alan 3 ana görünümden biri olabilir: **3D**, **CANVAS** ve **OUTPUT.** Bunlar arasında simge çubuğundaki düğmelerle geçiş yapabilirsiniz. Alternatif olarak `Tab` tuşuyla 3D view ile OUTPUT view arasında geçiş yapabilir, ardından sırayla her lazer çıkışı arasında dolaşmaya devam edebilirsiniz.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view, lazerlerinizin nasıl görüneceğini gösterir ve kendi lazer kurulumunuza uyacak şekilde yapılandırılabilir. Kamerayı döndürmek için tıklayıp sürükleyin; ileri ve geri hareket etmek için fare tekerleğini kullanın. Birçok başka seçeneği _3D Visualiser settings_ panelinde bulabilirsiniz (_View -> 3D Visualiser Settings_). Bkz. [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view, her lazer için zone ve mask ayarlamak için kullanılır. (Sol üst köşedeki büyük sayıya dikkat edin; hangi lazer üzerinde olduğunuzu kolayca görebilirsiniz!)

Bu görünüm, ilgili lazerin tüm çıkışını ve her zone öğesinin bu çıkış içinde nerede durduğunu temsil eder. Varsayılan olarak her lazerde yalnızca bir zone bulunur, ancak makul olduğu sürece istediğiniz kadar zone ekleyebilirsiniz; hepsini bu görünümde görürsünüz.

{% hint style="info" %}
**Zone nedir?**

Zone, lazer içeriğini yönlendirebileceğiniz, bir lazerin çıkışı içindeki alandır. Bir lazerde birden fazla zone olabilir. En basit zone türü _beam_ zone’dur; ayrıca _canvas_ zone ve _DMX_ zone türleri de vardır. Bu kılavuzda çoğunlukla, genelde havada atmosferik beam efektleri oluşturmak için kullanılan beam zone öğelerine odaklanacağız.
{% endhint %}

Düzenlemek istediğiniz lazeri şu yöntemlerden biriyle seçebilirsiniz:

* üstteki çubukta bulunan numaralı düğmeler
* istediğiniz lazerin sayı tuşuna basmak (_1-9 tuşları_)
* bir sonrakine geçmek için `Tab` tuşu

Kuruluma yeni bir lazer eklemek için _+_ düğmesine basın. (_Laser Overview_ panelinde ayrıca bir _ADD LASER_ düğmesi de vardır.)

Kurulumdan bir lazer silmek için _Laser Overview_ panelindeki kırmızı ⊖ düğmesine basın.

Yakınlaştırmak ve uzaklaştırmak için fare tekerleğini kullanabilir; görünümü taşımak için zone olmayan herhangi bir yere tıklayıp sürükleyebilirsiniz.

Seçmek için bir zone öğesine tıklayın, ardından köşe noktalarını fareyle ayarlayın. Bir köşeyi sürüklerken tekdüze olmayan bir şekil oluşturmak için `Alt / Option` tuşunu kullanın. Zone türünü değiştirme dahil daha fazla seçenek görmek için zone üzerinde sağ tıklayın.

Sol tarafta bir dizi simge düğmesinden oluşan bir çubuk bulunur. Herhangi bir düğmenin ne yaptığını görmek için fare imlecini üzerine getirin. Buradaki düğmeler beam zone, canvas zone ve mask eklemenizi sağlar. Ayrıca yalnızca bu lazer için Test Pattern ayarlama seçenekleri ile grid ve snapping ayarları da vardır.

Daha fazla ayrıntı için bkz. [Output view](../output-view/ "mention").

#### Canvas

Canvas sistemi çoğunlukla grafikler ve mimari mapping için kullanılır. Karmaşık görüntüleri birden fazla lazer arasında dağıtabilir ve her bölüm için perspektif düzeltmesi yapabilirsiniz. Bkz. [Grafikler ve Canvas sistemi](../graphics-and-the-canvas-system/ "mention").

### APC40 MIDI kontrolcüsü

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberation’ı fare ve klavyeyle kontrol etmek mümkündür, ancak bir APC40 MIDI kontrol arayüzü kullanmak çok daha iyidir (Mark 2 en iyi seçenektir, ancak Mark 1 de çalışır).

Ayrıca bkz.: [APC40 referansı](../reference/apc40-reference.md "mention")

Liberation, APC Mini ve MIDI Fighter Twister desteği de sunar. Yine de çoğu durumda en iyi seçenek APC40 Mark 2’dir.&#x20;

### Clips ve efektler

{% hint style="info" %}
**Clip nedir?**

Clip, Liberation içindeki herhangi bir lazer içeriği için kullanılan kapsayıcıdır. Clip öğeleri beam veya grafik animasyonlar içerebilir ve genellikle döngü şeklinde çalışır. Herhangi bir zone içine (veya _Canvas hedef alanına_) yönlendirilebilir ve Clip Deck içindeki Clip düğmeleriyle tetiklenir.
{% endhint %}

#### Clip Deck genel bakış

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Bu grid _Clip Deck_ olarak bilinir ve tüm lazer Clip öğelerinin saklandığı yerdir. APC40 üzerindeki 8 x 5 düğme grid’iyle doğrudan eşleşecek şekilde tasarlanmıştır.

**Clip Deck içinde gezinme.**

Clip Deck’i sola ve sağa kaydırmak için şunları kullanabilirsiniz:

* Sol ve sağ ok tuşları. Tek seferde tam bir sayfa kaydırmak için `Cmd / Ctrl` ekleyin.
* Trackpad: Kaydırma hareketi
* Fare: Farenizde yatay kaydırma varsa, imleç Clip Deck üzerindeyken bunu kullanabilirsiniz
* APC40 kaydırma düğmesi
* APC40 _<- DEVICE ->_ düğmeleri

Yerinizin nerede olduğunu anlamanıza yardımcı olmak için üst kısımda Clip Deck’in küçük bir görselleştiricisi bulunur. Ayrıca bkz. [Clips ve Clip Deck](../clips/ "mention")

#### Clip başlatma ve durdurma

Bir Clip başlatmak için Clip düğmesine basın (fareyle veya APC40 ile). Durdurmak için tekrar basın. Bir Clip başlattığınızda, _shift_ tuşunu basılı tutmadığınız sürece aynı renkteki diğer tüm Clip öğeleri otomatik olarak durur.

Bazı Clip öğeleri _Flash mode_ içinde olabilir (varsayılan olarak kırmızı olanlar). Bu durumda Clip düğmesini bıraktığınız anda dururlar.

_STOP_ düğmesi o anda çalışan tüm Clip öğelerini durdurur.

#### Clip için çıkış zone ayarlama

Clip düğmelerinin altında zone düğmelerini görürsünüz; varsayılan olarak beam zone 1’den 8’e kadar (_BEAM 1_, _BEAM 2_ vb.). Zone düğmeleri, seçili Clip için hangi zone öğelerinin atanmış olduğunu göstermek üzere yanar.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Zone düğmelerinin iki sıra altında X/Y çevirme düğmelerini görürsünüz. Clip öğesini yatay ve dikey çevirmek için bunları açıp kapatabilirsiniz.

{% hint style="info" %}
Bu zone atamalarının ve X/Y çevirme ayarlarının Clip öğesinin kendisine bağlı olduğunu unutmayın; o Clip’i bir sonraki çalıştırışınızda korunurlar. Bunlar genel bir ayar değildir.
{% endhint %}

Clip için daha fazla ayarı düzenlemek üzere Clip üzerinde sağ tıklayın. Ayrıca bkz. [Clip ayarları](../clips/clip-settings.md "mention")

### Gruplar

Her Clip öğesinin renkli bir çerçevesi olduğunu fark edeceksiniz; bu renk, hangi _grup_ içinde olduğunu gösterir. APC40 üzerindeki Clip düğmeleri de bu renkte yanar.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grup 1</td><td>Camgöbeği</td></tr><tr><td>Grup 2</td><td>Turuncu</td></tr><tr><td>Grup 3</td><td>Kırmızı</td></tr><tr><td>Grup 4</td><td>İndigo</td></tr><tr><td>Grup 5</td><td>Yeşil</td></tr></tbody></table>

Grup sistemi çok esnektir ve şunları yapmanızı sağlar:

* Bir gruptaki Clip öğeleri çalışmaya devam ederken başka bir gruptakileri açıp kapatmak
* Bir grup içindeki tüm Clip öğelerine zone ve X/Y çevirme ayarlarını hızlıca atamak
* Bir Clip için _Flash mode_ ayarlamak (Grup 3 varsayılan olarak _Flash mode_ durumundadır)

Gruplarda ayrıca geçiş giriş/çıkış ayarları bulunur; bu ayarlar Clip öğeleri tarafından devralınabilir veya geçersiz kılınabilir.

Clip öğesinin grubunu sağ tıklama menüsündeki düğmelerle atayabilirsiniz. APC40 kullanıyorsanız grup düğmesine basıp _basılı tutarken_ Clip düğmelerine basabilirsiniz.

Bir grup içindeki tüm Clip öğeleri için zone ayarlarını değiştirme

APC40 kullanırken grup düğmesine basın, ardından _basılı tutarken_ o grup içindeki tüm Clip öğeleri için zone ve X/Y düğmelerini açıp kapatın.

Ayrıca bkz. [Clip grupları](../clips/groups.md "mention")

### Efektler

Liberation’daki efekt sistemi, Clip çıkışını gerçek zamanlı olarak değiştirmek için güçlü ve çok yönlü bir yöntemdir. Varsayılan efekt düğmeleri 1-8, zone düğmelerinin altındadır.

#### Efekt uygulama

Efekti açıp kapatmak için bir efekt düğmesine basın. Daha da iyisi, efektleri kademeli olarak açıp kapatmak için APC40 üzerindeki 1-8 slider’larını kullanın.

#### Efekt parametreleri

Her efektin _parametresini_ ayarlamak için 1-8 rotary kontrolcülerini kullanın\*. (Veya fareyle sağ tıklayarak level ve parametreyi ayarlayabilirsiniz.) Parametre değişikliği, efektin nasıl ayarlandığına bağlı olarak farklı şeyler yapar. Varsayılan efektler için aşağıdaki listeye bakın.

{% hint style="info" %}
Efekt düğmelerinde gördüğünüz küçük sayılar, efektin _level_ ve _parameter_ değerlerini gösterir. _Level_, APC40 üzerindeki fader ile kontrol edilir veya düğmeye tıklayıp sürükleyebilirsiniz. Parametre, APC40 üzerindeki rotary kontrollerle ayarlanır veya fareyle sağ tıklayarak ayarlayabilirsiniz.
{% endhint %}

_\*Rotary kontrolcüler 1-8, APC40 Mk2’de üst sıra boyunca; Mk1’de ise sağ üsttedir. Ayrıca bkz.:_ [APC40 referansı](../reference/apc40-reference.md "mention")

#### Varsayılan efektler

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Clip çıkışına kaotik bir hareket uygular. Parametre, kaosun miktarını/hızını ayarlar.
2. **Sine wave** :\
   Tüm içeriği hareket eden bir sinüs dalgası üzerinden büker. Parametre, dalga boyunu ayarlar.
3. **Rotation** :\
   Her şeyi döndürür. Parametre, dönüş hızını ayarlar.
4. **Horizontal flip** :\
   Her şeyi yatay olarak sıkıştırıp esnetir. Parametre, hızı ayarlar.
5. **Scale** :\
   Her şeyi tekrar tekrar tam boyuttan sıfıra ölçekler. Parametre, hızı ayarlar.
6. **Hue** :\
Her şeyin hue değerini değiştirir, ancak saturation değerini değiştirmez (yani beyaz olan her şey beyaz kalır). Parametre, hue değerini ayarlar.
7. **Saturation and hue** :\
Her şeyin hue değerini değiştirir ve rengi tamamen saturate eder (yani beyaz olan her şey renge dönüşür). Parametre, hue değerini ayarlar.
8. **Flash** :\
   Her şeyin parlaklığını tekrar tekrar tamdan sıfıra yanıp söndürür. Parametre, flash hızını ayarlar.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alt sırada, hazır hue ve saturation değerleri uygulamak için 16 renk efekti daha bulunur.

Bunların varsayılan efektler olduğunu unutmayın; ancak neredeyse istediğiniz her şeyi yapacak şekilde düzenlenebilirler!

#### _“Şu anda seçili Clip”_ nedir?

Bir Clip başlattığınızda, etkin olduğunu göstermek için yanar. Ayrıca etrafında beyaz bir çerçeve bulunur; bu çerçeve bunun o anda _seçili_ Clip olduğunu gösterir. Zone düğmelerini açıp kapattığınızda veya Clip ayarlarını değiştirdiğinizde, bu değişiklikler _şu anda seçili Clip_ üzerine uygulanır.

{% hint style="info" %}
Bir Clip öğesini tetiklemeden seçmek için Clip düğmesine basmadan önce `Alt / Option` tuşuna basın. Bu, Clip çalışmadan zone ve diğer ayarlarını düzenlemek için iyi bir yöntemdir.
{% endhint %}

### Clip Settings paneli

Ölçekleme, X/Y konumu ve güçlü zone gecikme sistemine erişim için _Clip Settings_ panelini kullanın.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings paneli

Tüm zone öğeleri genelindeki tüm çıkışı etkileyen genel çıkış ayarlarını düzenlemek için _Global Settings_ panelini bulun.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Hiçbir Clip çalmıyorken tüm _Global settings_ değerlerini otomatik olarak sıfırlamak için AUTO RESET seçeneğini açın.&#x20;

### Zamanlama

Neredeyse tüm lazer gösterilerinde bir tür müzik altyapısı bulunur. Bu nedenle Liberation’daki zamanlama sistemi, dakika başına vuruş cinsinden bir tempo etrafında kuruludur. _Tempo Panel_ içinde zamanı temsil eden bir görünüm görebilirsiniz; her kare bir vuruşu temsil eder ve karelerin ritme uygun şekilde yanıp söndüğünü görürsünüz.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

MIDI clock ve Ableton Link dahil birden fazla senkronizasyon seçeneği vardır. Müziğin temposunu biliyorsanız ekrandaki kaydırıcıyı veya APC40 Tempo düğmesini kullanarak manuel ayarlayabilirsiniz. Ancak _Tap Tempo_ sistemiyle müzikle tempoda kalabilirsiniz.

#### Tap Tempo

_Tap Tempo_, müzik uygulamalarında yaygın kullanılan bir terimdir. Müzik çalarken ritme uygun şekilde dokunarak tempoyu ayarlamanızı sağlar. Ekrandaki düğmeyi kullanabilirsiniz; ancak _T_ tuşunu veya APC40 üzerindeki _Tap Tempo_ düğmesini kullanmanız önerilir (isterseniz ayak pedalı bile kullanabilirsiniz).

Tempoyu ölçünün başına sıfırlamak için _R_ tuşuna veya _Metronome_ düğmesine (APC40) basın.

Tempoyu tam sayıya yuvarlamak için _Y_ tuşuna basın veya _Tempo_ düğmesini (APC40) çevirin. Bu, dakika başına vuruş sayısı genellikle tam sayı olan elektronik müzik için faydalı olabilir.

### Clip Deck düzenleme

Clip Deck üzerinde bir Clip öğesini taşımak için tıklayıp yeni konumuna sürükleyin. Sürüklerken sola ve sağa kaydırmak için imleç tuşlarını (veya APC40 üzerindeki kaydırma tekerleğini/düğmelerini) kullanabilirsiniz.

Kopya oluşturmak için sürüklerken `Alt / Option` tuşuna basın.

Bir Clip öğesini başlatmadan seçmek için `Alt / Option` tuşuyla tıklayın.

Çoklu seçim için bir Clip öğesine `Alt / Option + Shift` tuşuyla tıklayın veya “lasso” seçimi yapmak için bir Clip dışındaki alana tıklayıp sürükleyin.&#x20;

Tıklayıp sürükleme, seçili TÜM Clip öğelerini sürükler.

Bir veya daha fazla Clip öğesini silmek için bunları Clip Deck dışına sürükleyin (bir çöp kutusu simgesi görünür) veya Clip sağ tıklama menüsündeki DELETE düğmesini kullanın.

### Laser Overview paneli

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview_ paneli, o anda çalışan lazerlerinizin durumuna hızlıca bakmanızı sağlar. Sağdaki yeşil kare, lazer kontrolcüsünün sorunsuz çalıştığını gösterir. Turuncuya dönerse ara sıra veri kesintileri vardır; kırmızıysa bağlantı kopmuştur. Griyse hiçbir kontrolcüye bağlı değildir.&#x20;

Ortadaki grafik, frame uzunluklarının geçmişidir; sağdaki sayı ise mevcut frame rate değeridir. İçerik ne kadar karmaşıksa frame rate o kadar düşük olur (yani daha fazla titreme görülür). Yaklaşık 25fps altındaki her şey biraz titrek görünmeye başlar.&#x20;

### Lazerlere bağlanma - Controller Assignment paneli

_Controller Assignment_ panelini açmak için _Assign Laser Controllers_ düğmesine tıklayın. (Bu panele menü çubuğundan _View -> Controller Assignment_ yoluyla da erişilebilir.)

Burada hangi lazer çıkışlarının hangi lazer kontrolcülerine gideceğini seçebilirsiniz. Sağdaki listeden kontrolcüleri sürükleyip soldaki yuvalara bırakın. Kontrolcülerinizi eşleştirildikleri lazere uyacak şekilde yeniden adlandırabilirsiniz (kalem simgeli düğmeyi kullanın).

Daha fazla ayrıntı için [Controller Assignment](../setting-up/controller-assignment.md "mention") bölümünü okuyun.

{% hint style="danger" %}
Herhangi bir lazeri devreye almadan önce [Lazerleri ayarlama](../setting-up/setting-up-lasers.md "mention") bölümünü mutlaka inceleyin.
{% endhint %}

### Lazer çıkış paneli

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Bu panel, _şu anda seçili lazer_ için ayarları gösterir (üstteki sayıyla temsil edilir). O anda seçili lazeri değiştirmek için _tab_ tuşunu kullanın, bir sayı tuşuna basın, _Laser Overview_ panelindeki veya _Output view_ içindeki lazer numarasına tıklayın.

* **Number button** lazeri devreye alır ve devreden çıkarır; kırmızıysa lazer devrededir.
* **Brightness** lazer parlaklığını diğer lazerlerden bağımsız olarak ayarlar (ve _Global Brightness_ ayarıyla birlikte uygulanır; yani ikisi de %50 ise lazeriniz %25 seviyesinde olur).
* **Test Pattern** yalnızca bu lazer için bir test deseni açar (genel Test Pattern ayarını geçersiz kılar).
* **Orientation** yana veya baş aşağı asılmış lazerler için düzeltme yapar.
* **Flip Horizontal and Flip Vertical** lazer çıkışını ters çevirir. Tutarsız kablolanmış lazerlerde çıkış düzeltmesi için kullanışlıdır.
* **Copy Laser Settings** bu lazerdeki çeşitli ayarları diğer lazerlere kopyalamanızı sağlayan bir panel açar.

### Tarayıcı ayarları

Gösteri lazerleri, tek bir lazer ışınını son derece hızlı hareket ettirip açıp kapatarak havada şekiller çizer. Çizgi, şekil ve görüntü olarak gördüğünüz şey aslında ışının, gözlerinizin takip edemeyeceği kadar hızlı yollar izlemesidir.

Point stream, lazere bir sonraki konuma nereye hareket edeceğini ve ışının ne zaman açık veya kapalı olacağını söyleyen veridir. Liberation’da Clip öğeleri, lazerlere gönderilirken gerçek zamanlı olarak bu point stream’e dönüştürülür.

Liberation, bu point stream’in nasıl üretileceği üzerinde ayrıntılı kontrol sağlar. Böylece her lazer için akıcılık, parlaklık ve performans arasında denge kurabilirsiniz.

{% hint style="info" %}
Önceden hesaplanmış point stream kullanan eski lazer yazılımlarına alışkınsanız, bu yaklaşım ilk başta farklı gelebilir. Ancak gerçek zamanlı nokta üretimi, aynı içeriğin her lazer için farklı şekilde optimize edilmesini sağlar. Bu, farklı tarayıcı hızına veya kalitesine sahip birden fazla lazerle çalışmayı, içeriği çoğaltmadan veya yeniden oluşturmadan kolaylaştırır. Ayrıca Clip dosyalarını çok küçük tutar; bu yüzden varsayılan Liberation Clip Deck’in tamamı gigabaytlar yerine yalnızca birkaç megabayttır.
{% endhint %}

Temel tarayıcı ayarları şunlardır:

* **Speed** tarayıcı hızıdır; yani lazerin şekil çizmek için ne kadar hızlı hareket ettiğidir. Geleneksel lazer yazılımlarında point rate ayarlamaya karşılık gelir, ancak Liberation’da lazerin ne kadar hızlı hareket ettiğini _point rate değerinden bağımsız olarak_ değiştirebilirsiniz. Bunu ayarlamanız gerekmez.
* **Scanner sync** (bazen _blank shift_, önceki adıyla Colour Shift olarak bilinir) Tarayıcılar lazeri çok hızlı hareket ettirir, ancak parlaklık ve renk değişimi genellikle hareketle senkron değildir. Bu durum, beam ve çizgilerin kenarında küçük titrek ışık “kuyrukları” olarak görünür. Hareket ve rengi birbiriyle senkron hâle getirmek için bu ayarı kullanın. Bkz. [Laser Settings](../setting-up/laser-settings/ "mention")

Diğer gelişmiş tarayıcı ayarları [Gelişmiş](../advanced/ "mention") bölümünde ele alınır.

### Zoning

Lazerleri kurma ve zoning işlemleri için tam kılavuza buradan bakın: [Lazerleri ayarlama](../setting-up/setting-up-lasers.md "mention")
