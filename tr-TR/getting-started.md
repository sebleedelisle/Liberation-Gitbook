---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Hızlı başlangıç kılavuzu

## Giriş

**Liberation** uygulamasına hoş geldiniz: yeni nesil lazer gösteri yazılımı.

Liberation güçlü ve kapsamlı bir modern yazılımdır; yaratıcılığınızı özgürce ifade edebilmeniz için kullanılabilirlik ve güvenilirlik temelleri üzerine kurulmuştur. Hızlı, verimli ve akıcıdır. Kısa sürede çalışmaya başlamak için bu _Hızlı başlangıç kılavuzu_ adımlarını izleyin!

### Lazerleri yönetme

Liberation, hiç gerçek lazer bağlı olmasa bile lazerleri ayarlayıp görselleştirebileceğiniz kadar esnektir. Hazır olduğunuzda da her çıkışı sorunsuz şekilde bir lazer denetleyicisine atayabilirsiniz.

{% hint style="info" %}
Liberation içinde istediğiniz kadar lazer ayarlayabilir ve görselleştirebilirsiniz. Lisans katmanları (Hobbyist, Pro vb.) yalnızca _etkinleştirebileceğiniz_ lazer sayısını sınırlar. Bu, ücretsiz lisansla bile 100 lazerli gösteriler tasarlayabileceğiniz anlamına gelir. Yükseltme yalnızca gösteriyi gerçek lazerlerde çalıştıracağınız zaman gerekir.
{% endhint %}

Varsayılan kurulumda yatay olarak yayılmış 8 lazer bulunur, ancak bunu istediğiniz şekilde özelleştirebilirsiniz. Yazılımı tanırken bu varsayılan düzeni korumak muhtemelen en iyisidir; daha sonra donanım kurulumunuza uyacak şekilde ayarlayabilirsiniz. (Bkz. [Projenizi ayarlama](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Önemli: Herhangi bir lazeri etkinleştirmeden önce riskleri anladığınızdan emin olun ve [Lazerleri ayarlama](setting-up/setting-up-lasers.md "mention") bölümünü dikkatlice okuyun.
{% endhint %}

## Yazılıma genel bakış

### Güvenlik kapatma

Lazerleri çalıştırırken elinizin altında mutlaka bir **donanımsal acil durdurma butonu** bulunmalıdır (bkz. [Acil durdurma ve kilitlemeler](hardware/emergency-stop-interlocks.md "mention")). Ancak her şeyi daha az acil bir şekilde devre dışı bırakmak isterseniz _**DISARM ALL**_ düğmesini, `Escape` tuşunu veya APC40 üzerindeki _**SESSION**_ tuşunu kullanabilirsiniz. Ayrıca ekrandaki sürgüyü veya APC40 üzerindeki ana fader’ı kullanarak genel parlaklığı azaltabilirsiniz.

### Sürgü öğeleri

Liberation genelinde çeşitli sürgüler ve kontroller bulunur.

{% hint style="info" %}
Sürgünün sunduğundan daha hassas bir kontrol gerekiyorsa yeni bir değer yazmak için sürgüye `Cmd / Ctrl` tuşuyla birlikte tıklayın.
{% endhint %}

### Klavye kısayolları

Klavye kısayollarının tam listesine buradan ulaşabilirsiniz: [Klavye kısayolları](reference/keyboard-shortcuts.md "mention")

### Ekran düzeni

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Belirli bir düğmenin ne işe yaradığından emin değil misiniz? Açıklamasını görmek için fare imlecini düğmenin üzerinde bekletin!
{% endhint %}

#### Menü

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menüde tüm dosya içe/dışa aktarma seçeneklerini ve panelleri açma komutlarını bulabilirsiniz. Bilgisayarı aboneliğinizle yetkilendirme seçeneği de burada bulunur (_Liberation -> Authorise/Deauthorise this computer_).

#### Simge çubuğu

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Tüm lazerleri etkinleştirme/devre dışı bırakma, Global Brightness, Test Pattern ve 3D, Canvas ile Output view arasında geçiş yapma gibi sık kullanılan işlemler burada bulunur.

### Görünümler

Ekranın sol üstündeki geniş alan üç ana görünümden biri olabilir: **3D**, **CANVAS** ve **OUTPUT.** Bunlar arasında geçiş yapmak için simge çubuğundaki düğmeleri kullanın. Alternatif olarak `Tab` tuşuyla 3D view ve Output view arasında geçiş yapabilir, ardından her lazer çıkışını sırayla dolaşmaya devam edebilirsiniz.

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view, lazerlerinizin nasıl görüneceğini gösterir ve kendi lazer kurulumunuza uyacak şekilde yapılandırılabilir. Kamerayı döndürmek için tıklayıp sürükleyin; ileri ve geri hareket etmek için fare tekerleğini kullanın. Birçok ek seçeneği _3D Visualiser settings_ panelinde bulabilirsiniz (_View -> 3D Visualiser Settings_). Bkz. [3D Görselleştirici](setting-up/3d-visualiser.md "mention").

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view, her lazer için zone ve mask yapılandırmak üzere kullanılır. (Sol üst köşedeki çok büyük sayıya dikkat edin; böylece hangi lazer üzerinde olduğunuzu kolayca görebilirsiniz!)

Bu görünüm, ilgili lazerin tüm çıkışını ve her zone öğesinin bu çıkış içinde nerede bulunduğunu temsil eder. Varsayılan olarak her lazerde yalnızca bir zone bulunur, ancak pratik olduğu sürece istediğiniz kadar zone ekleyebilirsiniz; hepsini bu görünümde görürsünüz.

{% hint style="info" %}
**Zone nedir?**

Zone, bir lazerin çıkışı içinde lazer içeriğini yönlendirebileceğiniz bir alandır. Bir lazerde birden fazla zone bulunabilir. En basit zone türü _beam_ zone türüdür; ayrıca _canvas_ zone ve _DMX_ zone türleri de vardır. Bu kılavuzda çoğunlukla, genelde havada atmosferik beam efektleri oluşturmak için kullanılan beam zone öğelerine odaklanacağız.
{% endhint %}

Düzenlemek istediğiniz lazeri şu yöntemlerle seçebilirsiniz:

* üstteki çubukta yer alan numaralı düğmeler
* istediğiniz lazerin numara tuşuna basma (_1-9 tuşları_)
* birinden diğerine geçmek için `Tab` tuşu

Kuruluma yeni bir lazer eklemek için _+_ düğmesine basın. (_Laser Overview_ panelinde ayrıca bir _ADD LASER_ düğmesi de vardır.)

Kurulumdan bir lazer silmek için _Laser Overview_ panelindeki kırmızı ⊖ düğmesine basın.

Yakınlaştırmak ve uzaklaştırmak için fare kaydırma tekerleğini kullanabilir; görünümü taşımak için zone olmayan herhangi bir yere tıklayıp sürükleyebilirsiniz.

Bir zone seçmek için üzerine tıklayın, ardından köşe noktalarını fareyle ayarlayın. Bir köşeyi sürüklerken onu oransız hale getirmek için `Alt / Option` tuşunu kullanın. Zone türünü değiştirme dahil daha fazla seçeneği görmek için zone üzerinde sağ tıklayın.

Sol tarafta bir dizi simge düğmesi bulunan bir çubuk vardır; ne işe yaradığını görmek için herhangi bir düğmenin üzerinde imleci bekletin. Buradaki düğmeler beam zone, canvas zone ve mask eklemenizi sağlar. Ayrıca yalnızca bu lazer için Test Pattern ayarlama seçenekleri ile grid ve snapping ayarları da bulunur.

Daha fazla ayrıntı için bkz. [Output view](output-view/ "mention").

#### Canvas

Canvas sistemi çoğunlukla grafikler ve mimari mapping için kullanılır. Karmaşık görüntüleri birden fazla lazer arasında dağıtabilir ve her bölümü perspektife göre düzeltebilirsiniz. Bkz. [Grafikler ve Canvas sistemi](graphics-and-the-canvas-system/ "mention").

### APC40 MIDI denetleyici

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Liberation uygulamasını fare ve klavyeyle kontrol etmek mümkün olsa da, APC40 MIDI kontrol arayüzü kullanmak çok daha iyidir (Mark 2 en iyi seçenektir, ancak Mark 1 de çalışır).

Ayrıca bkz.: [APC40 başvurusu](reference/apc40-reference.md "mention")

Liberation, APC Mini ve MIDI Fighter Twister desteği de sunar. APC40 Mark 2 çoğu durumda hâlâ en iyi seçenektir.

### Clips ve efektler

{% hint style="info" %}
**Clip nedir?**

Clip, Liberation içinde herhangi bir lazer içeriği için kullanılan bir kapsayıcıdır. Clip içinde beam veya grafik animasyonlar bulunabilir ve genellikle döngü halinde çalışır. İçerik herhangi bir zone içine veya _Canvas hedef alanına_ yönlendirilebilir ve Clip Deck içindeki Clip düğmeleriyle tetiklenir.
{% endhint %}

#### Clip Deck genel bakış

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Bu ızgara _Clip Deck_ olarak bilinir ve tüm lazer Clip öğelerinin saklandığı yerdir. APC40 üzerindeki 8 x 5 düğme ızgarasıyla doğrudan eşleşecek şekilde tasarlanmıştır.

**Clip Deck içinde gezinme.**

Clip Deck alanını sola ve sağa kaydırmak için şunları kullanabilirsiniz:

* Sol ve sağ ok tuşları. Tek seferde tam bir sayfa kaydırmak için `Cmd / Ctrl` tuşunu ekleyin.
* Trackpad: Kaydırma hareketi
* Fare: Farenizde yana kaydırma özelliği varsa, imleç Clip Deck üzerindeyken bunu kullanabilirsiniz
* APC40 kaydırma düğmesi
* APC40 _<- DEVICE ->_ düğmeleri

Yönünüzü bulmanıza yardımcı olmak için üst kısımda Clip Deck için küçük bir görselleştirici bulunur. Ayrıca bkz. [Clips ve Clip Deck](clips/ "mention")

#### Clip başlatma ve durdurma

Bir Clip başlatmak için Clip düğmesine basın (fareyle veya APC40 ile). Durdurmak için tekrar basın. Bir Clip başlattığınızda, _shift_ tuşunu basılı tutmadığınız sürece aynı renkteki diğer tüm Clip öğeleri otomatik olarak durur.

Bazı Clip öğeleri _Flash mode_ durumunda olur (varsayılan olarak kırmızı olanlar). Bu durumda Clip düğmesini bıraktığınız anda dururlar.

_STOP_ düğmesi, o anda çalışan tüm Clip öğelerini durdurur.

#### Clip için çıkış zone öğelerini ayarlama

Clip düğmelerinin altında zone düğmelerini görürsünüz; varsayılan olarak beam zone 1’den 8’e kadardır (_BEAM 1_, _BEAM 2_ vb.). Zone düğmeleri, o anda seçili Clip öğesine hangi zone öğelerinin atandığını göstermek için yanar.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Zone düğmelerinin iki satır altında X/Y flip düğmelerini görürsünüz; Clip öğesini yatay ve dikey çevirmek için bunları açıp kapatın.

{% hint style="info" %}
Bu zone atamalarının ve X/Y flip ayarlarının Clip öğesinin kendisine bağlı olduğunu unutmayın; aynı Clip bir sonraki çalıştırıldığında korunurlar. Global bir ayar değildir.
{% endhint %}

Clip için daha fazla ayarı düzenlemek üzere Clip üzerinde sağ tıklayın. Ayrıca bkz. [Clip ayarları](clips/clip-settings.md "mention")

### Gruplar

Her Clip öğesinin renkli bir dış çizgisi olduğunu fark edeceksiniz; bu renk, hangi _grup_ içinde olduğunu temsil eder. APC40 üzerindeki Clip düğmeleri de bu renkte yanar.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grup 1</td><td>Camgöbeği</td></tr><tr><td>Grup 2</td><td>Turuncu</td></tr><tr><td>Grup 3</td><td>Kırmızı</td></tr><tr><td>Grup 4</td><td>Çivit mavisi</td></tr><tr><td>Grup 5</td><td>Yeşil</td></tr></tbody></table>

Grup sistemi çok esnektir ve şunları yapmanızı sağlar:

* Bir gruptaki Clip öğeleri çalışmaya devam ederken başka bir gruptaki öğeleri açıp kapatmak
* Bir grup içindeki tüm Clip öğelerine hızlıca zone ve X/Y flip atamak
* Bir Clip için _Flash mode_ ayarlamak (Grup 3 varsayılan olarak _Flash mode_ durumundadır)

Gruplarda ayrıca içeri/dışarı geçiş ayarları bulunur; bu ayarlar gruptaki Clip öğeleri tarafından devralınabilir veya geçersiz kılınabilir.

Clip öğesinin grubunu sağ tık menüsündeki düğmeleri kullanarak atayabilirsiniz. APC40 kullanıyorsanız grup düğmesine basıp _basılı tutarken_ Clip düğmelerine basabilirsiniz.

Bir grup içindeki tüm Clip öğeleri için zone ayarlarını değiştirme

APC40 kullanırken grup düğmesine basın, ardından _basılı tutmaya devam ederken_ o grup içindeki tüm Clip öğeleri için zone ve X/Y düğmelerini kullanarak zone ayarlarını açıp kapatın.

Ayrıca bkz. [Clip grupları](clips/groups.md "mention")

### Efektler

Liberation içindeki efekt sistemi, Clip çıkışını gerçek zamanlı olarak değiştirmek için güçlü ve çok yönlü bir yöntemdir. Varsayılan efekt düğmeleri 1-8, zone düğmelerinin altında bulunur.

#### Efekt uygulama

Efekti açıp kapatmak için bir efekt düğmesine basın. Daha da iyisi, efektleri kademeli olarak açıp kapatmak için APC40 sürgüleri 1-8’i kullanın.

#### Efekt parametreleri

Her efektin _parameter_ değerini ayarlamak için rotary controller 1-8\* kullanın. (İsterseniz fareyle sağ tıklayarak level ve parameter değerlerini de ayarlayabilirsiniz.) Parameter değişimi, efektin nasıl kurulduğuna bağlı olarak farklı şeyler yapar. Varsayılan efektler için aşağıdaki listeye bakın.

{% hint style="info" %}
Efekt düğmelerinde gördüğünüz küçük sayılar, efektin _level_ ve _parameter_ değerlerini gösterir. _Level_, APC40 üzerindeki fader ile kontrol edilir veya düğme üzerinde tıklayıp sürükleyebilirsiniz. Parameter, APC40 üzerindeki rotary controller ile ayarlanır veya fareyle sağ tıklayarak ayarlayabilirsiniz.
{% endhint %}

_\*Rotary controller 1-8, APC40 Mk2 üzerinde üst kısımda; Mk1 üzerinde sağ üstte bulunur. Ayrıca bkz.:_ [APC40 başvurusu](reference/apc40-reference.md "mention")

#### Varsayılan efektler

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Clip çıkışına kaotik bir hareket uygular. Parameter, kaos miktarını/hızını ayarlar.
2. **Sine wave** :\
   Tüm içeriği hareketli bir sinüs dalgası boyunca büker. Parameter, dalga boyunu ayarlar.
3. **Rotation** :\
   Her şeyi döndürür. Parameter, dönüş hızını ayarlar.
4. **Horizontal flip** :\
   Her şeyi yatay olarak sıkıştırır ve esnetir. Parameter, hızı ayarlar.
5. **Scale** :\
   Her şeyi tekrar tekrar tam boyuttan sıfıra ölçekler. Parameter, hızı ayarlar.
6. **Hue** :\
Her şeyin tonunu değiştirir, ancak doygunluğu değiştirmez (yani beyaz olan her şey beyaz kalır). Parameter, hue değerini ayarlar.
7. **Saturation and hue** :\
Her şeyin tonunu değiştirir ve rengi tamamen doygun hale getirir (yani beyaz olan her şey renge dönüşür). Parameter, hue değerini ayarlar.
8. **Flash** :\
   Her şeyin parlaklığını tekrar tekrar tamdan sıfıra düşürüp yükseltir. Parameter, flash hızını ayarlar.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alt satırda, önceden ayarlanmış hue ve saturation değerlerini uygulamak için 16 ek renk efekti bulunur.

Bunların varsayılan efektler olduğunu, ancak neredeyse istediğiniz her şeyi yapacak şekilde düzenlenebileceklerini unutmayın!

#### _"currently selected clip"_ nedir?

Bir Clip başlattığınızda aktif olduğunu göstermek için yanar. Ayrıca etrafında beyaz bir dış çizgi bulunur; bu, o anda _seçili_ Clip olduğunu gösterir. Zone düğmelerini açıp kapattığınızda veya Clip ayarlarını değiştirdiğinizde, bunlar _currently selected clip_ için uygulanır.

{% hint style="info" %}
Bir Clip öğesini tetiklemeden seçmek için Clip düğmesine basmadan önce `Alt / Option` tuşuna basın. Bu, Clip çalışmadan zone ve diğer ayarlarını düzenlemek için iyi bir yöntemdir.
{% endhint %}

### Clip Settings paneli

Ölçeklendirme, X/Y konumu ve güçlü zone delay sistemine erişim için _Clip Settings_ panelini kullanın.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings paneli

Tüm zone öğeleri genelindeki tüm çıkışları etkileyen global çıkış ayarlarını değiştirmek için _Global Settings_ panelini açın.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Hiç Clip çalışmıyorken tüm _Global settings_ değerlerini otomatik olarak sıfırlamak için AUTO RESET özelliğini açın.

### Zamanlama

Neredeyse tüm lazer gösterilerinde bir tür müzik altyapısı bulunur. Bu nedenle Liberation içindeki zamanlama sistemi, dakika başına vuruş cinsinden bir tempo üzerine kuruludur. _Tempo Panel_ içinde zamanın bir temsilini görebilirsiniz; her kare bir vuruşu temsil eder ve ritme göre yanıp söndüklerini görürsünüz.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

MIDI clock ve Ableton Link dahil birden fazla senkronizasyon seçeneği vardır. Müziğin temposunu biliyorsanız ekrandaki sürgüyü veya APC40 Tempo düğmesini kullanarak manuel ayarlayabilirsiniz. Ayrıca _Tap Tempo_ sistemiyle müzikle eş zamanlı kalabilirsiniz.

#### Tap Tempo

_Tap Tempo_, müzik uygulamalarında yaygın kullanılan bir terimdir ve müzik çalarken tempoyu ayarlamak için vuruşa uygun şekilde tempo tutmanızı sağlar. Ekrandaki düğmeyi kullanabilirsiniz; ancak _T_ tuşunu veya APC40 üzerindeki _Tap Tempo_ düğmesini kullanmanız önerilir (isterseniz ayak pedalı bile kullanabilirsiniz).

Tempoyu ölçünün başına sıfırlamak için _R_ tuşuna veya _Metronome_ düğmesine (APC40) basın.

Tempoyu tam sayıya yuvarlamak için _Y_ tuşuna basın veya _Tempo_ düğmesini (APC40) çevirin. Bu, dakika başına vuruş sayısı genellikle tam sayı olan elektronik müzik için kullanışlı olabilir.

### Clip Deck düzenleme

Clip Deck üzerinde bir Clip taşımak için tıklayıp yeni konuma sürükleyin. Sürüklerken sola ve sağa kaydırmak için imleç tuşlarını veya APC40 üzerindeki kaydırma tekerleğini/düğmelerini kullanabilirsiniz.

Kopya oluşturmak için sürüklerken `Alt / Option` tuşuna basın.

Bir Clip öğesini başlatmadan seçmek için `Alt / Option` tuşuyla birlikte tıklayın.

Çoklu seçim için `Alt / Option + Shift` tuşlarıyla birlikte bir Clip öğesine tıklayın veya “lasso” seçimi yapmak için Clip dışında bir alana tıklayıp sürükleyin.

Tıklayıp sürükleme işlemi TÜM seçili Clip öğelerini sürükler.

Bir veya daha fazla Clip öğesini silmek için bunları Clip Deck dışına sürükleyin (bir çöp kutusu simgesi görünür) veya Clip sağ tık menüsündeki DELETE düğmesini kullanın.

### Laser Overview paneli

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_, o anda çalışan lazerlerinizin durumuna hızlıca bakmanızı sağlar. Sağdaki yeşil kare, lazer denetleyicisinin sorunsuz çalıştığını gösterir. Turuncuya dönerse ara sıra veri kaybı yaşanıyordur; kırmızı olursa bağlantı kesilmiştir. Gri ise hiçbir denetleyiciye bağlı değildir.

Ortadaki grafik kare uzunluklarının geçmişini gösterir; sağdaki sayı ise mevcut kare hızıdır. İçerik ne kadar karmaşıksa kare hızı o kadar düşük olur (yani daha fazla titreme görülür). Yaklaşık 25 fps altındaki değerler biraz titreşimli görünmeye başlar.

### Lazerlere bağlanma - Controller Assignment paneli

_Controller Assignment_ panelini açmak için _Assign Laser Controllers_ düğmesine tıklayın. (Bu panele menü çubuğundan _View -> Controller Assignment_ yoluyla da erişebilirsiniz.)

Hangi lazer çıkışlarının hangi lazer denetleyicilerine gideceğini burada seçebilirsiniz. Sağdaki listeden denetleyicileri sürükleyip soldaki yuvalara bırakın. Denetleyicilerinizi eşleştirildikleri lazerle uyumlu olacak şekilde yeniden adlandırabilirsiniz (kalem simgesi düğmesini kullanın).

Daha fazla ayrıntı için [Controller Assignment](setting-up/controller-assignment.md "mention") bölümünü okuyun.

{% hint style="danger" %}
Herhangi bir lazeri etkinleştirmeden önce [Lazerleri ayarlama](setting-up/setting-up-lasers.md "mention") bölümünü mutlaka okuyun.
{% endhint %}

### Laser Settings paneli

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Bu panel, _currently selected laser_ için ayarları gösterir (üstteki sayı ile temsil edilir). O anda seçili lazeri değiştirmek için _tab_ tuşunu kullanın, bir sayı tuşuna basın, _Laser Overview_ panelinde veya _output view_ içinde bir lazer numarasına tıklayın.

* **Number button** lazeri etkinleştirir ve devre dışı bırakır; kırmızıysa lazer etkindir.
* **Brightness** lazer parlaklığını diğer lazerlerden bağımsız olarak ayarlar (ve _global brightness_ ayarıyla birleştirilir; yani ikisi de %50 ise lazeriniz %25 seviyesinde olur).
* **Test Pattern** yalnızca bu lazer için bir test deseni açar (global test deseni ayarını geçersiz kılar).
* **Orientation** yana veya baş aşağı kurulmuş lazerleri düzeltir.
* **Flip Horizontal and Flip Vertical** lazer çıkışını ters çevirir. Kablolaması tutarsız olan lazerlerde çıkış düzeltmesi için kullanışlıdır.
* **Copy Laser Settings** bu lazerden diğerlerine çeşitli ayarları kopyalamanızı sağlayan bir panel açar.

### Tarayıcı ayarları

Gösteri lazerleri, tek bir lazer ışınını son derece hızlı hareket ettirip açıp kapatarak havada şekiller çizer. Çizgi, şekil ve görüntü olarak gördüğünüz şey aslında ışının, gözünüzün takip edemeyeceği kadar hızlı şekilde izler çizmesidir.

Nokta akışı, lazere bir sonraki nereye hareket edeceğini ve ışının ne zaman açık veya kapalı olması gerektiğini söyleyen veridir. Liberation içinde Clip öğeleri lazerlere gönderilirken gerçek zamanlı olarak bu nokta akışına dönüştürülür.

Liberation, bu nokta akışının nasıl oluşturulacağı üzerinde ayrıntılı kontrol sağlar; böylece her lazer için akıcılık, parlaklık ve performans arasında denge kurabilirsiniz.

{% hint style="info" %}
Önceden hesaplanmış nokta akışlarına dayanan eski lazer yazılımlarına alışkınsanız bu yaklaşım ilk başta farklı gelebilir. Ancak gerçek zamanlı nokta üretimi, aynı içeriğin her lazer için farklı şekilde optimize edilmesini sağlar. Bu, farklı tarayıcı hızlarına veya kalitesine sahip birden fazla lazerle çalışmayı, içeriği çoğaltmadan veya yeniden oluşturmadan kolaylaştırır. Ayrıca Clip dosyalarını çok küçük tutar; bu yüzden tüm varsayılan Liberation Clip Deck yalnızca birkaç megabayttır, gigabaytlarca yer kaplamaz.
{% endhint %}

Temel tarayıcı ayarları şunlardır:

* **Speed** tarayıcı hızıdır; yani lazerin şekiller çizmek için ne kadar hızlı hareket ettiğidir. Bu, geleneksel lazer yazılımlarında nokta hızını ayarlamaya denktir, ancak Liberation içinde lazerin hareket hızını _nokta hızından bağımsız_ olarak değiştirebilirsiniz. Bunu ayarlamanız gerekmez.
* **Scanner sync** (bazen _blank shift_, daha önce Colour Shift olarak bilinir) Tarayıcılar lazeri çok hızlı hareket ettirir, ancak genellikle parlaklık ve renk değişimi hareketle senkronize değildir. Bu durum beam ve çizgilerin kenarında küçük, titrek ışık “kuyrukları” olarak görünür. Hareket ve rengin birbiriyle senkronize olması için bu ayarı kullanın. Bkz. [Laser Settings](setting-up/laser-settings.md "mention")

Diğer gelişmiş tarayıcı ayarları [Gelişmiş](advanced/ "mention") bölümünde ele alınır.

### Zoning

Lazerleri ayarlama ve zoning konusunda eksiksiz bir kılavuz için bkz.: [Lazerleri ayarlama](setting-up/setting-up-lasers.md "mention")
