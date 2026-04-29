---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Projelerinizin çoğunda kullanacağınız ana zone türü _Beam zone_ olur. Bu zone, havadaki atmosferik beam efektleri için tasarlanmıştır. Diğer zone türü ise _Canvas zone_ türüdür (Bkz. [Grafikler ve Canvas sistemi](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**UYARI - Lazer çalışırken zone öğelerini taşırken son derece dikkatli olun** ve parlaklığı mümkün olan en düşük seviyeye indirin. Lazerleri güvenli şekilde etkinleştirme ve zone ayarı yapma hakkında kapsamlı bir rehber için [Lazerleri ayarlama](../setting-up/setting-up-lasers.md) bölümüne bakın
{% endhint %}

Zone öğelerini fareyle tıklayıp sürükleyerek taşıyabilirsiniz. Bu zone öğesinin nereye gittiğini görmek için bir test pattern açın.

{% hint style="info" %}
Seçili zone/point öğesini **küçük adımlarla hareket ettirmek** için ok tuşlarını kullanın. Daha büyük adımlarla hareket ettirmek için `Shift` tuşuna basın.
{% endhint %}

{% hint style="info" %}
İpucu: zone ayarlarını birden fazla lazer arasında hızlıca kopyalayabilirsiniz! Bkz. [Laser Settings ayarlarını kopyalama](../setting-up/copy-laser-settings.md)
{% endhint %}

### Yeni bir beam zone ekleme

Araç çubuğunun üst kısmındaki _Add a new beam zone_ düğmesine tıklayın; yeni bir zone görünür. Beam zone öğeleri eklenme sırasına göre sıralanır, ancak bu sırayı değiştirebilirsiniz. Bkz. [Beam zone sırasını değiştirme](re-ordering-beam-zones.md)

### Mevcut bir canvas zone ekleme

_Add existing canvas zone_ düğmesine tıklayın. Kullanılabilir canvas zone öğelerinin listesini görürsünüz ve bu lazer için bunları açıp kapatabilirsiniz. Bkz. [Grafikler ve Canvas sistemi](../graphics-and-the-canvas-system/)

### Zone şekil türleri

3 zone şekil türü vardır:

* **Quad** - Varsayılan dikdörtgen zone şeklidir; düzgün (eksenlere hizalı) olabilir veya bozulmuş olabilir. Daha büyük dikdörtgen zone öğeleri ya da perspektif düzeltmesi gerektiren canvas zone öğeleri için en uygundur.
* **Line/Curve** - 2 veya daha fazla nokta ve bir kalınlıkla tanımlanan zone türüdür. İnce zone öğeleri veya balkon, köprü ya da diğer eğrisel şekillerde sınırlandırma yapmak için idealdir.
* **Segmented** - Daha küçük quad parçalarına bölünebilen bir zone türüdür. Mimari mapping için idealdir.

Ayarlarını açmak için herhangi bir zone öğesine sağ tıklayın. Bu sağ tık menüsünden şunları yapabilirsiniz:

* Zone adını değiştirme (özellikle çok sayıda zone varsa clip deck içinde tanımayı kolaylaştırır!)
* Zone öğesini etkinleştirme/devre dışı bırakma
* Konumunu kilitleme
* Şekil türünü değiştirme
* Varsayılan konuma sıfırlama
* Şekil türüne özel ayarlara erişme
* Silme
* Bir _Alt Zone_ ekleme (Bkz. [Alt Zone sistemi](alt-zone-system.md))

{% hint style="danger" %}
**UYARI -** Lazer etkin durumdayken zone türünü değiştirirken çok dikkatli olun. Zone, o şekil için son kullanılan konuma / boyuta döner; bu nedenle Output aniden değişebilir. Zone türünü değiştirmeden önce lazeri kapatmanız en iyisidir.
{% endhint %}

### Quad zone şekli

Quad öğesinin her köşesini fareyle taşıyabilirsiniz. Bir köşeyi diğerlerinden bağımsız hareket ettirmek ve quad şeklini bozmak için köşeye `Alt / Option` tuşuyla tıklayın. Quad bozulduktan sonra tüm köşeler serbestçe hareket edebilir.

Bozulmayı kaldırıp eksenlere hizalı dikdörtgene geri döndürmek için sağ tık menüsündeki _REMOVE DISTORTION_ düğmesini kullanabilirsiniz.

#### Perspektif düzeltmesi

Bu seçenek sağ tık menüsündeki aç/kapat düğmesiyle ayarlanır ve bozulma yöntemini belirler. Beam kullanımı için bunu kapalı tutmak en iyisidir; ancak bu zone düz bir yüzeye grafik yansıtıyorsa açın. Böylece Output perspektif düzeltmeli olur.

{% hint style="info" %}
_Perspective correction_ kapalıysa içerik _çift doğrusal enterpolasyon_ kullanılarak bozulur. Başka bir deyişle içerik quad boyunca eşit aralıklarla dağıtılır. Bu yüzden beam kullanımı için daha uygundur.

Perspective correction açıkken içerik, perspektif bükme yöntemiyle bozulur ve bu yöntem kısalma etkisini telafi eder. Yani grafikleri bir duvara eğik açıyla yansıtıyorsanız, Output üzerindeki bozulmayı gidermek ve projeksiyon bozulmasını düzeltmek için bunu kullanabilirsiniz.
{% endhint %}

### Line / Curve zone şekli

Line / Curve zone şekli son gösterilerde benim vazgeçilmez seçeneğim haline geldi; hatta beam zone için varsayılan seçeneğin bu olması gerektiği bile söylenebilir.

Çoğu zaman zone öğelerimin, mekanlardaki dar ve zor alanlara ya da binalardaki pencerelerin arasına sığması için ince olması gerekiyor. Köşeler birbirine bu kadar yakınken bir quad öğesinin dört köşesini ayarlamanın oldukça uğraştırıcı olabildiğini fark ettim. Line / Curve zone böyle ortaya çıktı!

Düz çizgiler için tek ihtiyacınız iki nokta ve ardından sağ tık menüsünden _Zone thickness_ ayarını yapmak. Basit zone öğeleri oluşturmanın en hızlı yolu budur.

Ek noktalar oluşturmak için çizgiye `Alt / Option` tuşuyla tıklayın. Bu noktalar akıcı bir şekil oluşturmak için otomatik olarak yumuşatılır; kıvrımları gidermek için _Smooth level_ ayarını düzenleyebilirsiniz.

Bir noktayı silmek için noktaya `Alt / Option` tuşuyla tıklayın.

Ya da vektör grafik uygulamalarıyla (Inkscape, Illustrator vb.) deneyimliyseniz, tüm kontrol noktalarında ince ayar yapmak için _Manually adjust bezier curves_ seçeneğini kullanabilirsiniz.

### Segmented zone şekli

Bu alt bölümlere ayrılmış zone, son derece ayrıntılı düzeltmeler yapmanızı sağlar ve karmaşık şekillere mapping yaparken kullanışlıdır. Sağ tık menüsündeki + ve - düğmelerini kullanarak alt bölümler ekleyebilir veya kaldırabilirsiniz.

### Tamamen başka bir zone tarafından kapatılmış bir zone nasıl düzenlenir

Üstteki zone öğesine sağ tıklayın ve kilit düğmesine tıklayarak kilitleyin. Artık alttaki zone öğesini düzenleyip ayarlayabilmeniz gerekir.

<br>

{% hint style="info" %}
Output öğenize bir Beam zone eklediğinizde, bu zone clip deck içinde bir Clip'e eklenebilir hale gelir.
{% endhint %}
