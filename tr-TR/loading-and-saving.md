---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Yükleme ve kaydetme

Liberation durumunu sürekli diske kaydeder. Böylece elektrik kesintisi veya sistem sorunu yaşarsanız, uygulama kaldığı yerden açılır; zones, timeline veya diğer içeriklerinizi kaybetmemeniz gerekir.

Bununla birlikte, yedek almak veya başka bir bilgisayara taşımak için kurulumunuzu dışa aktarabilirsiniz.

### Project içe/dışa aktarma

Project dosyası mevcut kurulumunuzdaki neredeyse her şeyi saklar. Buna şunlar dahildir:

* Aşağıdaki [Laser Settings içe/dışa aktarma](loading-and-saving.md#laser-settings-import-export) bölümünde açıklanan her şey
* Clips, efektler ve grup ayarları
* Tüm timeline öğeleriniz (ses ve video medyaları hariç)
* Art-Net kurulumu
* MIDI gönderme/alma ayarları
* Tempo / senkronizasyon ayarları

Şu anda şunları kaydedip yüklemez:

* MIDI notes node ve Sound Input Oscillator içinde kullanılan ses ve MIDI giriş ayarları (MIDI gönderme/alma ayarlarını ve timecode ses girişini _kaydeder_)
* Arayüz ölçeklendirmesi
* Canvas kılavuz görselleri için medya
* Timeline için ses ve video medyaları
* Text node içinde kullanılan yazı tipleri

{% hint style="danger" %}
Timeline içindeki ses ve video dosyaları project dosyalarıyla birlikte kaydedilmez. Bu yüzden içeriği başka bir bilgisayara taşımak istiyorsanız bu dosyaları ayrıca kaydettiğinizden emin olun. Bkz. [Timeline medya dosyaları hakkında önemli not](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Laser Settings içe/dışa aktarma

* Her lazer için Laser Settings
* Beam zones
* Canvas hedef alanları
* DMX zones
* Laser controller ataması (ve yeniden adlandırdığınız controller öğeleri için takma adlar)
* Lazer tarayıcı ve renk kalibrasyonu ayarları ve preset’leri
* 3D görselleştirici ayarları ve preset’leri

### Clip Deck içe/dışa aktarma

* Tüm Clips ve bunların zone atamaları, ayarları ve parametreleri
* Tüm grup ayarları, flash mode, fade in/out süreleri vb.

Şu anda şunları kaydedip yüklemez:

* Tüm efektler ve bunların parametreleri ile ayarları

{% hint style="info" %}
**Tüm project dosyasını yüklemeden project dosyasından Clips yükleme**

Bir project içinden yalnızca Clips öğelerini içe aktarmak için _**Clips->Import Clip Deck**_ seçeneğini seçin ve clip deck dosyası (.cpdk) seçmek yerine bir project dosyası seçin.
{% endhint %}

### Append Clip Deck

_Append Clip Deck_ kullanarak dışa aktarılmış bir clip deck dosyasındaki Clips öğelerini mevcut project dosyanıza ekleyebilirsiniz. Clips, mevcut Clip Deck sonuna eklenir; ancak dosyadaki efektler ve grup ayarları içe aktarılmaz.

### Export Selected Clips

O anda seçili olan Clips bir dosyaya dışa aktarılır. Grup ayarları ve efektler kaydedilmez; yalnızca Clips kaydedilir. Şu anda çalışan aktif Clips, ayrıca seçili değilse dışa aktarılmaz.

{% hint style="info" %}
Clips seçmek için Option/Alt - shift - tıklama kullanın (veya lasso kullanın). Hangi Clips öğelerinin seçili olduğunu, etraflarındaki kalın beyaz çerçeveden anlayabilirsiniz. Bkz. [Clip başlatma ve durdurma](clips/starting-stopping-clips.md)
{% endhint %}

### Efektleri içe/dışa aktarma

Tüm efektleri, grup ayarları ve parametreleriyle birlikte yükler ve kaydeder.

{% hint style="info" %}
**Tüm project dosyasını yüklemeden project dosyasından efekt yükleme**

Bir project içinden yalnızca efektleri içe aktarmak için _**Effects->Import Effects**_ seçeneğini seçin ve efekt dosyası (.efts) seçmek yerine bir project dosyası seçin.
{% endhint %}

### Timeline dışa aktarma

Bir veya daha fazla timeline içeren bir timeline dosyası dışa aktarır. Clip Deck her zaman dışa aktarılan timeline dosyalarına dahil edilir (ancak içe aktarırken hangi Clips öğelerinin geri alınacağını seçebilirsiniz; aşağıdaki [Timeline içe aktarma](loading-and-saving.md#timeline-import) bölümüne bakın).

Project dosyanızda birden fazla timeline varsa, dışa aktarmak istediğiniz timeline öğelerini seçmenizi sağlayan bir panel açılır.

{% hint style="danger" %}
Timeline içindeki ses ve video dosyaları timeline dosyalarıyla birlikte kaydedilmez. Bu yüzden içeriğinizi başka bir bilgisayara taşımak istiyorsanız bu dosyaları ayrıca kaydettiğinizden emin olun. Bkz. [Timeline medya dosyaları hakkında önemli not](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Timeline içe aktarma

Tek bir timeline dosyasından bir veya daha fazla timeline içe aktarır. Timeline dosyanızı seçtikten sonra, birden fazla içe aktarma seçeneği içeren bir panel açılır.

Timeline dosyasında birden fazla timeline varsa hepsi listelenir. Dahil etmek istediklerinizi işaretleyin.

* Replace existing timelines\
  Mevcut timeline öğelerinizin tamamını siler ve içe aktarılanlarla değiştirir.
* Import used clips only\
  Yalnızca kullanılan Clips öğelerini içe aktarır ve Clips öğelerini her timeline için bir grup olacak şekilde gruplar halinde düzenler. Bu seçenek seçilmezse, timeline dosyasının tüm Clip Deck içeriği mevcut Clips listenizin sonuna eklenir.
* Replace existing clip deck\
  Mevcut Clip Deck içeriğinizi timeline dosyasındaki Clips ile değiştirir. Yalnızca _Replace existing timelines_ seçiliyse kullanılabilir.

{% hint style="info" %}
**Tüm project dosyasını yüklemeden project dosyasından timeline yükleme**

Bir project içinden yalnızca timeline öğelerini içe aktarmak için _**Timeline->Import Timeline(s)**_ seçeneğini seçin ve timeline dosyası (.ltml) seçmek yerine bir project dosyası seçin.
{% endhint %}

### DMX / Art-Net içe/dışa aktarma

Art-Net nodes ayarlarını IP adresleriyle birlikte kaydeder ve yükler. DMX zones ve tüm DMX preset’leriniz de buna dahildir.

### Timeline medya dosyaları hakkında önemli not

Ses ve video dosyaları şu anda timeline dosyasıyla birlikte dışa **aktarılmaz**. Bu yüzden içeriği başka bir bilgisayara taşımanız gerekiyorsa bu dosyaları da eklediğinizden emin olun.

{% hint style="info" %}
**Timeline medya dosyalarını nasıl bulur**

Timeline yüklendiğinde, timeline (veya project) dosyasıyla aynı klasöre bakar ve bu klasörün içinde ve tüm alt klasörlerinde arama yapar. Dosyalar aynı klasörde veya bir alt klasörde olduğu sürece (örneğin _/videos_ veya _/sound_), yükleme sırasında bulunurlar.
{% endhint %}
