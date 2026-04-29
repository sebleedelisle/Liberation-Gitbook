---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Renk kalibrasyonu

Renk kalibrasyonu, projektörünüzdeki kırmızı, yeşil ve mavi lazerlerin tüm parlaklık seviyelerinde düzgün ve öngörülebilir şekilde ışık vermesini sağlar. Farklı projektörlerde doğrusal olmayan parlaklık eğrileri olabilir; yani %50 kırmızı, %100 kırmızının yarısı kadar yoğun görünmek yerine çok daha parlak veya daha sönük görünebilir. Kalibrasyon bunu düzeltir; renkler temiz karışır, degradeler yumuşak görünür ve beyaz dengelenir.

#### Projektörünüzü ısıtma

Lazer diyotlarının davranışı ısındıkça değişir. Kalibrasyondan önce projektörünüzün her zaman dengelenmesini bekleyin:

* En az **15–20 dakika** boyunca **White rectangle test pattern (11)** gibi parlak bir kare yansıtın.
* Bu, ayarladığınız renk dengesinin gösteri sırasında tutarlı kalmasını sağlar.

#### Kalibrasyon testinin çalışma şekli

Kalibrasyon için test pattern kullanın (bkz. [Test pattern](../output-view/test-patterns.md))

* **5** – Kırmızı
* **6** – Yeşil
* **7** – Mavi
* **8** – Beyaz

Bunların her biri dört hareketli çizgi gösterir:

* **Üst çizgi** – Tam hızda %100 parlaklık
* **İkinci çizgi** – %75 hızda %75 parlaklık
* **Üçüncü çizgi** – %50 hızda %50 parlaklık
* **Dördüncü çizgi** – %25 hızda %25 parlaklık

Hem parlaklık _hem de hız_ birlikte ölçeklendiği için çizgilerin hepsi aynı parlaklıkta görünmelidir. Bir çizgi daha açık veya daha koyu görünüyorsa, eşleşene kadar ilgili kaydırıcıyı ayarlayın.

Her test pattern ayrıca **%0 parlaklıkta** beşinci bir çizgiye sahiptir; bu çizgi görünmemelidir. Bu, çok düşük seviyelerde hiç ışık vermeyen lazerleri düzeltmek için kullanılır. Lazeriniz düşük parlaklıkta görünmez kalıyorsa, çizgi zar zor görünene kadar **0% setting** değerini kademeli olarak artırın, ardından çizgi tekrar kaybolana kadar biraz geri alın. Amaç, lazerin ışık vermeye başladığı eşiği bulmak ve hemen altında kalmaktır; böylece fade geçişleri alt aralığı kesmeden doğal şekilde başlar.

#### Colour Calibration panelini kullanma

Panel, her kanal için (kırmızı, yeşil, mavi) 100, 75, 50, 25 ve %0 seviyelerinde bağımsız kontroller sağlar.

1. **Bir test pattern seçin** (kırmızıyla başlayın).
2. **Kaydırıcıları ayarlayın**; 100, 75, 50 ve %25 çizgileri aynı parlaklıkta görünmelidir.
3. “Kapalı” çizgi hâlâ belli belirsiz görünüyorsa **0% slider** üzerinde ince ayar yapın.
4. **Yeşil ve mavi için tekrarlayın.**
5. **White test pattern (8)** seçeneğine geçin. Dört çizginin hepsi eşit görünmeli ve beyaz nötr olmalıdır (renk kayması olmamalıdır).

#### Beyaz dengesini ayarlama

Bu sistemi **beyaz dengesi** ayarlamak için de kullanabilirsiniz. Her kanalı ayrı ayrı kalibre ettikten sonra **White test pattern (8)** seçeneğine geçin. Çıkış renkli görünüyorsa (örneğin fazla yeşil veya fazla mavi), çizgiler nötr beyaz görünene kadar kırmızı, yeşil ve mavi kanalların göreli seviyelerini ayarlayın. Lazerlerinizin güçleri birbirinden oldukça farklı olsa bile kalibrasyon, onları birbirine yaklaştırmaya ve daha temiz, daha dengeli bir renk karışımı üretmeye yardımcı olur.

#### Kalibrasyonunuzu kaydetme

* Geçerli preset üzerine yazmak için **Store** kullanın.
* Yeni bir preset oluşturmak için **Store As** kullanın (birden fazla lazerle çalışıyorsanız kullanışlıdır).
