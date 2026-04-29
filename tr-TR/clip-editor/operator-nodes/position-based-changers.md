---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Konuma dayalı değiştiriciler

Bu node ailesi, içeriği konuma göre değiştirir. Varsayılan olarak efekt yatay bir eksen boyunca uygulanır (soldan sağa), ancak bu ekseni istediğin açıya döndürebilirsin. Her node ayrıca _radial_ modu içerir; bu modda efekt, her noktanın merkeze göre açısıyla belirlenir.

* **Colour Changer by Position** – seçilen eksen boyunca veya radial açı çevresinde renkleri kaydırır.\
  \&#xNAN;_Örnek: Bir çizgi boyunca akan gökkuşağı gradyanı oluştur veya bir dairede radial modu kullanarak renk çarkı efekti üret._
* **Wave Shift by Position** – sinüs dalgası bozulması uygular ve içeriği dikey olarak (veya seçilen eksene dik yönde) kaydırır.\
  \&#xNAN;_Örnek: Bir çizgiyi su gibi dalgalandır veya radial modu kullanarak bir dairenin merkezden dışa doğru nabız gibi atmasını sağla._
* **Noise Shift by Position** – simplex noise bozulması uygular ve içeriği dikey olarak (veya seçilen eksene dik yönde) kaydırır.\
  \&#xNAN;_Örnek: Wave Shift örneğine benzer, ancak daha organik ve rastgele bir karakterle; doğal çeşitlilik eklemek için idealdir._

## &#x20;Konuma göre renk değiştirme

Bu node, içeriğinde konuma göre renk değişiklikleri uygular. Varsayılan olarak eksen yataydır (0°), ancak ekseni döndürebilir veya radial moda geçebilirsin.

* **wavelength** – tekrarlanan renk döngüsünün boyutunu ayarlar.
  * _Linear mode:_ 100% değerinde, tam bir döngü içeriğin tam genişliğini kaplar.
  * _Radial mode:_ 100% değerinde, tam bir döngü tam daireyi (360°) kaplar. Değerler dairenin yüzdesidir: ör. 50% = yarım daire (180°).
* **offset** – renk döngüsünün başlangıç noktasını, wavelength yüzdesi olarak kaydırır. Renkler arasında düzgün geçiş yapmak için bunu modüle edebilirsin (ör. testere dişi oscillator ile).
* **repeat** – etkinleştirildiğinde döngü içerik boyunca tekrarlanır. Devre dışıysa gradyan yalnızca bir kez uygulanır: başlangıçtan önceki her şey başlangıç rengi, sondan sonraki her şey bitiş rengi olur.
* **pingpong** – etkinleştirildiğinde her tekrar yön değiştirir ve aynalanmış bir efekt oluşturur. _Repeat_ devre dışıysa gradyan bir kez ileri, sonra geri gider. _Not: Pingpong modunda wavelength hem ileri hem de geri taramayı kapsar._
* **linear angle** – efektin eksenini döndürür. 0° = yatay.
* **radial** – radial moda geçer ve renkleri merkezden olan açıya göre uygular.
* **radial smooth loop** – wavelength değerini dairenin 100% değerine eşit bölünecek şekilde otomatik ayarlar; böylece döngünün sarıldığı yerde görünür bir ek oluşmasını önler.

**Renk Modları**

Bunlar, renk ayarlarının hangi yönlerinin içeriğe uygulanacağını belirler. Ayrıca bkz.: [Renk ayarları ve HSB](../fundamentals/colour-settings-and-hsb.md).

* **hue mode**
  * _OFF_ – hue değişmez.
  * _FIXED_ – hue sabit bir değere zorlanır.
  * _SHIFTED_ – hue belirtilen miktar kadar kaydırılır (farklı renkli öğeler ayrı kalır, ancak renk çarkı üzerinde birlikte kayar).
* **saturation mode**
  * _OFF_ – saturation değişmez.
  * _FIXED_ – saturation belirtilen değere ayarlanır.
* **brightness mode**
  * _OFF_ – brightness değişmez.
  * _FIXED_ – brightness belirtilen değere ayarlanır.
  * _MULTIPLY_ – brightness belirtilen değerle ölçeklenir. Bu, dinamikleri korur (ör. yanıp sönen öğeler yine yanıp söner, ancak sınırlı brightness aralığında kalır).

**Başlangıç / Bitiş Değerleri**

Bu kaydırıcılar, seçilen eksen boyunca (veya radial tarama boyunca) uygulanacak renk aralığını tanımlar.

* **start hue** – gradyanın başlangıcındaki hue.
* **end hue** – gradyanın sonundaki hue.
* **start saturation** – başlangıçtaki saturation.
* **end saturation** – sondaki saturation.
* **start brightness** – başlangıçtaki brightness.
* **end brightness** – sondaki brightness.
* **blend** – renk değişimini orijinal renklerle karıştırır. 100% değerinde efekt, orijinal renklerin tamamen yerini alır.

**Örnek 1: Kayan Gökkuşağı Gradyanı**

Varsayılan ayarlarla başlayarak:

1. Node için **Linear** modu açık bırak (0° açı = yatay).
2. **wavelength** değerini 100% olarak bırak (tam genişliği kaplar ve varsayılan bu olmalıdır).
3. Başlangıç ve bitiş değerlerini varsayılan olarak bırak.
4. **repeat** seçeneğini etkinleştir.
5. **offset** ayarına 0% ile 100% arasında giden bir **Sawtooth Oscillator** ekle.

***

**Örnek 2: Siyah–Beyaz–Siyah Gradyan (Pingpong)**

Varsayılan ayarlarla başlayarak:

1. Node için **Linear** modu açık bırak (0° açı = yatay).
2. **wavelength** değerini 100% olarak bırak (tam genişliği kaplar ve varsayılan bu olmalıdır).
3. **repeat** seçeneğini kapat.
4. **start brightness** değerini 0 yap (siyah).
5. **end brightness** değerini 100 yap (beyaz).
6. **start saturation** ve **end saturation** değerlerini 0 yap (gri tonlamaya dönüştürür).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. **pingpong** seçeneğini etkinleştir.

_Sonuç: gradyan genişlik boyunca siyahtan beyaza, sonra tekrar siyaha döner._\
İçeriğin kendi hue ve saturation değerlerini korumasını istiyorsan Saturation mode seçeneğini OFF yap. \\

***

**Örnek 3: Dönen Gökkuşağı Çarkı (Radial)**

1. **radial** modunu etkinleştir.
2. **wavelength** değerini 100% yap (tam 360° tarama).
3. **repeat** seçeneğini aç.
4. **offset** ayarına 0% ile 100% arasında giden bir **Sawtooth Oscillator** ekle.

_Sonuç: dairenin etrafında sürekli dönen, kesintisiz bir renk çarkı._

## &#x20;Konuma göre dalga kaydırma

Bu node, içeriğine dalga bozulması uygular ve noktaları seçilen eksene dik yönde (veya merkezden radial olarak) kaydırır.

* **Wavelength** – dalga döngüsünün uzunluğunu ayarlar.
  * _Linear mode:_ 100% değerinde, tam bir döngü içeriğin tam genişliğini kaplar.
  * _Radial mode:_ 100% değerinde, tam bir döngü tam 360° değerini kaplar. (Değerler dairenin yüzdesidir: 50% = yarım tur, 25% = çeyrek tur vb.)
* **Size** – dalganın genliğini kontrol eder (içeriğin ne kadar yer değiştireceği).
* **Offset** – dalgayı eksen boyunca (veya radial modda dairenin etrafında) kaydırır. Bu, wavelength yüzdesidir; bu yüzden dalgayı hareket ettirmek için bir **Oscillator Node** ile canlandırabilirsin.
* **Radial** – linear moddan radial moda geçer; böylece yer değiştirme merkezden olan açıya göre belirlenir.
* **Radial Smooth Loop** – wavelength değerini dairenin 100% değerine eşit bölünecek şekilde ayarlar; böylece sarma noktasında görünür ek oluşmasını önler.
* **Triangle** – dalga biçimini sinüsten üçgene değiştirir.
* **Absolute** – dalganın mutlak değerini alır ve yalnızca yukarı yönlü yer değiştirmeler oluşturur (negatif tarafı pozitif tarafın üzerine katlar).
* **Angle** – dalganın eksenini döndürür. 0° = yatay.

## &#x20;Konuma göre noise kaydırma

Bu node, içeriği bir noise alanı (türbülans gibi) kullanarak bozar ve noktaları seçilen eksene dik yönde (veya merkezden radial olarak) kaydırır. _Wave Shift_ ile karşılaştırıldığında sonuç daha organik ve rastgeledir.

* **Detail** – noise yapısının ne kadar ince olacağını kontrol eder. Daha yüksek değerler = daha keskin, daha ayrıntılı değişim. Daha düşük değerler = daha yumuşak değişim.
* **Wavelength** – noise deseninin ölçeğini ayarlar.
  * _Linear mode:_ 100% değerinde, tam bir noise döngüsü içeriğin genişliğini kaplar.
  * _Radial mode:_ 100% değerinde, tam bir döngü tam 360° değerini kaplar.
* **Size** – yer değiştirme miktarını kontrol eder (noise bozulmasının genliği).
* **Offset** – noise desenini eksen boyunca (veya dairenin etrafında) kaydırır. Bu, wavelength yüzdesidir; bu yüzden noise akıyormuş gibi göstermek için bir **Oscillator Node** ile canlandırabilirsin.
* **Depth Offset** – 3D noise alanı içinde ilerler ve zaman içinde değişim oluşturur. Bir Oscillator Node ile canlandırıldığında özellikle etkilidir.
* **Depth Detail** – derinlik boyutu boyunca değişimin ne kadar ayrıntılı olacağını kontrol eder.
* **Absolute** – noise değerinin mutlak değerini alır ve negatif değerleri pozitiflere katlar (yalnızca tek taraflı yer değiştirme üretir).
* **Radial** – linear moddan radial moda geçer; böylece yer değiştirme merkezden olan açıya göre belirlenir.
* **Radial Smooth Loop** – wavelength değerini dairenin 100% değerine eşit bölünecek şekilde ayarlar; radial modda görünür ek oluşmasını önler.
