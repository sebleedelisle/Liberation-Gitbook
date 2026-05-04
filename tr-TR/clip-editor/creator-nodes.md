---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Tek bir nokta / ışın oluşturur.

* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **Colour** - noktanın rengi. Bkz. [Renk ayarları ve HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Bir çizgi / ışık perdesi oluşturur.

* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **Size** - çizginin uzunluğu
* **Colour** - çizginin rengi. Bkz. [Renk ayarları ve HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - çizginin derece cinsinden açısı
* **resolution** - bkz. [Çözünürlük](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ çizginin başlangıç noktasını ve dönüş merkezini belirler
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Bir daire / koni oluşturur.

* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **radius** - dairenin yarıçapı
* **Colour** - dairenin rengi. Bkz. [Renk ayarları ve HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* **resolution** - bkz. [Çözünürlük](fundamentals/resolution.md "mention")
* **Fill state** - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Eşkenar çokgenler oluşturur: üçgen, kare, beşgen vb.

* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **size** - merkezden her köşeye olan mesafe
* **Colour** - çokgenin rengi. Bkz. [Renk ayarları ve HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - şeklin derece cinsinden döndürülmüş açısı
* **resolution** - bkz. [Çözünürlük](fundamentals/resolution.md "mention")
* **Fill state** - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Özel şekiller için bir SVG dosyası yükler.

{% hint style="warning" %}
Liberation, _SVGTiny_ formatıyla uyumludur. InkScape önerilir, ancak çoğu vektör grafik uygulaması bu formatta dışa aktarım yapabilir. Dışa aktarmadan önce metinleri şekillere dönüştürdüğünüzden emin olun. Liberation çizgi konturlarını çizer ve isteğe bağlı olarak dolguları mask olarak kullanır. Çizgilerinizin siyah olmadığından emin olun; aksi halde renk değiştirici olmadan görünmezler!
{% endhint %}

* **Import SVG** - diskten bir SVG dosyası yükler.

{% hint style="info" %}
Bir SVG yüklendikten sonra içerik dönüştürülür ve Clip içine kaydedilir. Bu nedenle, daha sonra mask ayarlarını değiştirmek istemediğiniz sürece dosyaya referans tutmanız gerekmez.
{% endhint %}

* **Use fills as masks** - dolgu içeren tüm şekilleri mask olarak işler; yani siyahla doldurulmuş gibi kullanır. SVG içinde dolgu içeren şekiller varsa bu otomatik olarak ayarlanır. Dolgu içeren şekil yoksa devre dışı bırakılır. Bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - SVG içindeki şekillerin konturu yoksa bunları çizemeyiz! Bu seçenek, dolgu içeren her şekle bir kontur (yani _stroke_) ekler. SVG içinde stroke uygulanmış şekil yoksa otomatik olarak ayarlanır. Dolgu içeren şekil yoksa devre dışı bırakılır.
* **Invert black lines** - SVG içindeki tüm çizgiler siyahsa onları göremezsiniz! Bu seçenek çizgileri beyaza çevirir. SVG içinde yalnızca siyah şekiller varsa otomatik olarak ayarlanır; hiç siyah şekil yoksa devre dışı bırakılır.
* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **scale** - SVG boyutunu ayarlar. SVG yüklendiğinde bu değer otomatik olarak hesaplanır (görselin görünür olduğundan emin olmak için), ancak sonrasında elle düzenlenebilir.
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - görselin derece cinsinden döndürülmüş açısı
* **resolution** - bkz. [Çözünürlük](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Bir SVG dosyası dizisinden animasyon oluşturur.

* **Import SVG Sequence** - tüm SVG dosyalarını içeren klasörü seçin. Dosyaların alfanümerik sırayla yüklendiğini unutmayın.

{% hint style="info" %}
SVG dizisi yüklendikten sonra içerik dönüştürülür ve Clip içine kaydedilir. Bu nedenle, daha sonra mask ayarlarını değiştirmek istemediğiniz sürece dosyalara referans tutmanız gerekmez.
{% endhint %}

* **Use fills as masks** - dolgu içeren tüm şekilleri mask olarak işler; yani siyahla doldurulmuş gibi kullanır. SVG dosyalarınızdan herhangi birinde dolgu içeren şekiller varsa bu otomatik olarak ayarlanır. Hiçbirinde dolgu içeren şekil yoksa devre dışı bırakılır. Bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - SVG dosyalarınızdaki şekillerin konturu yoksa bunları çizemeyiz! Bu seçenek, dolgu içeren her şekle bir kontur (yani _stroke_) ekler. SVG dosyalarınızda stroke uygulanmış şekil yoksa otomatik olarak ayarlanır. Hiçbirinde dolgu içeren şekil yoksa devre dışı bırakılır.
* **Invert black lines** - SVG dosyalarınızdaki tüm çizgiler siyahsa onları göremezsiniz! Bu seçenek çizgileri beyaza çevirir. SVG dosyalarınızda yalnızca siyah şekiller varsa otomatik olarak ayarlanır; hiç siyah şekil yoksa devre dışı bırakılır.
* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **scale** - görselin boyutunu ayarlar.
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - görselin derece cinsinden döndürülmüş açısı
* **resolution** - bkz. [Çözünürlük](fundamentals/resolution.md "mention")
* **speed** - tüm animasyonun ölçü cinsinden süresi.
* **time per frame** - bu ayar etkinse süre, animasyonun tamamı yerine kare başına uygulanır. Yani _speed_ ¼ olarak ayarlanırsa her kare 1 vuruş sürer.
* **animation direction** -
  * _FORWARDS_ - animasyon ileri oynar ve sonra başa dönerek döngüye girer
  * _BACKWARDS_ - animasyon geri oynar ve sonra sona dönerek döngüye girer
  * _PINGPONG_ - animasyon ileri, ardından geri oynayarak döngüye girer
  * _MANUAL_ - geçerli kare _position manual_ ayarıyla belirlenir
* **position manual** - geçerli kareyi ayarlar; %0 ilk kare, %100 son karedir. Bu değer elle veya harici bir osilatörle ayarlanabilir.
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

TrueType veya OpenType font kullanarak metin oluşturur.

* **Text** - istediğiniz metni buraya yazın
* **Font** - istediğiniz fontu seçin

{% hint style="info" %}
Liberation’a daha fazla font eklemek için .ttf veya .otf dosyalarını Liberation çalışma klasörünün içindeki `data/fonts` klasörüne kopyalayın, ardından Liberation’ı yeniden başlatın.
{% endhint %}

* **Render profile** - bkz. [Render profili](fundamentals/render-profile.md "mention")
* **horizontal alignment** - metin hizalamasını seçmek için _LEFT_, _CENTRE_ veya _RIGHT_ seçin.
* **Fill state** - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - metin boyutu
* **monospace** - her karakteri aynı genişlikte çizer. Sayılar değişirken metin yana kaymadığı için zamanlayıcılar ve sayaçlar için kullanışlıdır.
* **character spacing** - karakterler arasındaki boşluğu ayarlar. Daha geniş harf aralığı için artırın veya metni sıklaştırmak için azaltın.
* **colour -** bkz. [Renk ayarları ve HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** ve **y** position - bkz. [Koordinat sistemi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - görselin derece cinsinden döndürülmüş açısı
* **resolution** - bkz. [Çözünürlük](fundamentals/resolution.md "mention")
* **reveal** - metni her seferinde bir karakter olacak şekilde kademeli olarak ortaya çıkarmak için kullanın. Bu değer %0 ile %50 arasındayken metin soldan sağa doğru kademeli olarak görünür. %50 ile %100 arasındayken metin soldan sağa doğru kaybolur. Animasyon oluşturmak için bu sokete bir osilatör bağlayabilirsiniz.
* **reveal by word** - etkin olduğunda _reveal_ karakter bazında değil, kelime bazında çalışır.
* **countdown** - yazılan metni bir geri sayımla değiştirir. Geri sayım sıfıra ulaştığında normal **Text** değeri gösterilir.
* **use seconds** - gerçek saniyelerle sayar. Bu kapalıyken geri sayım vuruş tabanlıdır: iki vuruş bir saniye sayılır, bu nedenle 120bpm gerçek saniyelerle eşleşir.
* **show minutes/seconds** - kalan süreyi dakika ve saniye olarak gösterir. Bir saatten uzunsa saatleri de ekler.
* **countdown to date/time** - bir sayıdan geriye saymak yerine belirli bir UTC tarih ve saatine geri sayar.
* **countdown datetime** - **countdown to date/time** açıkken UTC hedef tarih/saat değerini ayarlar.
* **start number** - **countdown to date/time** kapalıyken başlangıç sayısıdır.
* _MOVE TO FRONT / MOVE TO BACK_ - bkz. [Fill, mask ve derinlik sıralaması](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Font açılır menüsü açıksa yukarı ve aşağı ok tuşları kullanılabilir fontlar arasında adım adım geçer.
{% endhint %}
