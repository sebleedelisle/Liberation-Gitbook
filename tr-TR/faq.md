---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ SSS

## Donanım

#### **Liberation Windows’ta çalışır mı?**

Evet - Liberation, Mac sürümüyle tamamen aynı özelliklerle **Windows 10 ve 11’i (64-bit)** tam olarak destekler. Her sürüm iki platform için aynı anda yayınlanır.

#### **Liberation Mac’te çalışır mı?**

Evet - Liberation, Windows sürümüyle tam özellik eşdeğerliğiyle **Mac’i (macOS 12 Monterey ve sonrası)** tam olarak destekler. Tüm güncellemeler birlikte yayınlanır.

#### **Gerekli minimum bilgisayar özellikleri nedir?**

Kaç lazer kontrol etmek istediğinize bağlıdır. Yalnızca birkaç lazer kullanıyorsanız düşük özellikli bir bilgisayar yeterli olur. Apple Silicon işlemcili herhangi bir Mac çok iyi çalışır ve 100’e kadar lazeri kontrol edebilmelidir. Kritik ve karmaşık gösteriler yapıyorsanız bütçenizin elverdiği en iyi bilgisayarı öneririz.

#### **Liberation ile kaç lazer kontrol edebilirim?**

Liberation tek bir bilgisayarda çok sayıda lazer çalıştırabilir. 100’den fazla laser controller ile test edilmiştir; bu yüzden yanıt şunlara bağlıdır:

* bilgisayarınızın CPU’su
* ağ hızı
* abonelik türünüz

#### **Hangi MIDI controller cihazlarını kullanabilirim?**

Liberation, popüler APC40 Mk2 MIDI controller etrafında tasarlanmış ve optimize edilmiştir. APC40 Mk1 ile de çalışır. Bkz. [APC40 ile canlı kontrol](midi-control/live-control-with-the-apc40.md)

Zaman içinde daha fazla MIDI controller desteği ekliyoruz; şu anda APC Mini Mk2 ve MIDI Fighter Twister da desteklenir.

Ek MIDI kontrolü sunan MIDI Send/Receive sistemi de vardır. Bkz. [MIDI Send/Receive](midi-control/midi-send-receive.md)

Daha fazla bilgi için bkz. [MIDI kontrolü](midi-control/).

#### **Herhangi bir MIDI controller ile kullanabilir miyim?**

Bunu gelecekte mümkün kılacak yapılandırılabilir bir MIDI sistemi üzerinde çalışıyoruz. Bu arada bazı kullanıcılar, herhangi bir MIDI mesajını MIDI Send/Receive sistemi için dönüştürebilen bir MIDI yorumlayıcı kullanarak başarılı sonuç aldı; ancak bu zahmetli ve ileri seviye bir süreçtir. Bu kurulumla ilgili öneriler için [forumda](https://forum.liberationlaser.com) arama yapabilirsiniz, ancak pratikte en iyi seçenek APC40’tır.

## Laser controller cihazları

#### **Hangi laser controller cihazları Liberation ile uyumludur?**

* [Ether Dream (önerilir)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [X-Laser Mercury](https://x-laser.com/pages/mercury-laser-control-system) (firmware güncellemesi yapmanız gerekebilir)
* LaserCube USB (ve LaserDock)
* LaserCube ağ protokolü (kablolu bağlantıyla)
* [LASollinger lazerlerinde](https://laseranimation.com/en/) kullanılan AVB (şu anda yalnızca macOS’ta test aşamasında)

Daha fazla bilgi için bkz. [Uyumlu lazerler ve controller/DAC cihazları](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Neden \[başka marka] laser controller desteği yok?**

Yazılım ve donanım arasında daha fazla birlikte çalışabilirliği teşvik etmek için Liberation yalnızca yayınlanmış bir iletişim protokolü olan DAC cihazlarını destekler. Bunun lazer sektörü için en doğru yol olduğuna inanıyorum.

#### **Lazerimin Liberation ile kullanılıp kullanılamayacağını nasıl anlarım?**

Lazerinizde aşağıdakilerden biri varsa Liberation ile kullanabilirsiniz:

* Harici **ILDA girişi** – uyumlu harici controller ile kullanılan 25-pin D konnektör.
* Dahili takılı **Ether Dream**.
* Herhangi bir **LaserCube** (hem USB hem Wi-Fi LaserCube ile çalışır).
* **Dahili Mercury sistemi bulunan bir X-Laser ünitesi** (Ether Dream modunda).
* **Dahili AVB bulunan LaserAnimation Sollinger projektör** (yalnızca macOS, AVB uyumlu ağ cihazları gerektirir, şu anda test aşamasında).

Daha fazla bilgi için bkz. [Uyumlu lazerler ve controller/DAC cihazları](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Liberation’ı LaserCube ile kullanabilir miyim?**

Evet, Liberation herhangi bir LaserCube ile doğrudan çalışır. Bkz. [LaserCube](hardware/lasercube.md)

## Lisanslar

#### **Lisans fiyatı nedir?**

Güncel fiyatlar için [mağaza](https://liberationlaser.com/shop) sayfasına bakın.

#### **Lisans kademeleri arasındaki sınırlamalar nelerdir?**

Güncel lisans seçenekleri için [mağaza](https://liberationlaser.com/shop) sayfasına bakın.

Ücretsiz kademe dahil **her** kademede istediğiniz kadar lazerle gösteri kurabilir, önizleme yapabilir ve tasarlayabilirsiniz. Bunun dışında tek sınırlama, aynı anda _arm_ durumuna alabileceğiniz lazer sayısıdır. Diğer tüm Liberation özellikleri herkes tarafından kullanılabilir.

#### **Daha yüksek bir kademeye geçebilir miyim?**

İstediğiniz zaman daha yüksek bir kademeye geçebilirsiniz. Mevcut lisansınızda kalan süre için kısmi iade alırsınız ve yeni planınız hemen başlar. Bkz. [Lisansınızı yükseltme veya düşürme](installation/upgrade-downgrade-your-license.md)

#### **Lisansımı düşürebilir miyim?**

İstediğiniz zaman daha düşük bir kademeye geçebilirsiniz, ancak değişiklik mevcut lisans döneminizin sonunda yürürlüğe girer. Bkz. [Lisansınızı yükseltme veya düşürme](installation/upgrade-downgrade-your-license.md)

#### **Bilgisayarımı lisansımla nasıl yetkilendiririm?**

Bir lisans satın aldıktan sonra bilgisayarı Liberation yazılımının içinden yetkilendirebilirsiniz. _About_ ekranında, web sitesinde oturum açmanızı isteyen bir _Authorise_ düğmesi göreceksiniz. Yetkilendirme işlemini tamamlamak için ekrandaki talimatları izleyin. Bkz. [Yetkilendirme ve yetkiyi kaldırma](installation/authorising-and-de-authorising.md)

#### **Bilgisayarımı internete ne sıklıkla bağlamam gerekir?**

Lisans her yenilendiğinde Liberation’ın dahili lisansını güncellemek için internete bağlanmanız gerekir. Aylık yinelenen ödeme kullanıyorsanız her ay bağlanmanız gerekir.

#### **Yenilemeden sonra bilgisayarımı internete bağlayamazsam ne olur?**

Lisansınız yenilendikten sonra Liberation, internete bağlanıp dahili lisansını güncellemeniz için 7 günlük ek süre tanır. Bu sürenin ardından Liberation _Free_ moduna döner.

#### **Kredi kartımın süresi dolarsa ne olur?**

Ödeme sağlayıcımızdan bir e-posta bildirimi alırsınız ve ödeme bilgilerinizi güncellemeniz gerekir. Web sitesinde oturum açın ve abonelikler sayfasındaki _Update payment details_ bağlantısını kullanın.

#### **Yinelenen lisansımı nasıl iptal ederim?**

Web sitesinde oturum açın, _Your subscriptions_ sayfasını açın, iptal etmek istediğiniz aboneliği seçin ve ardından _Cancel Subscription_ bağlantısına tıklayın. Lisans dönemi bitene kadar Liberation’ı kullanmaya devam edebilirsiniz.

#### **Liberation’ı kaç bilgisayara kurabilirim?**

Liberation’ı istediğiniz kadar bilgisayara kurabilirsiniz. Lisans yetkilendirmesi yalnızca lazer/DMX çıkışını etkinleştirmek için gerekir ve lisans kademeniz aynı anda kaç bilgisayarın çıkış için yetkilendirilebileceğini belirler. Bkz. [Lisanslama nasıl çalışır](installation/how-licensing-works.md)

#### **Lisansımı bir bilgisayardan diğerine nasıl taşırım?**

* Artık kullanmak istemediğiniz bilgisayarda Liberation’ı açın
* İnternete bağlı olduğunuzdan emin olun ve _About_ ekranındaki _De-authorise this computer_ düğmesine tıklayın
* Şimdi Liberation’ı yeni bilgisayarda açın
* _About_ ekranındaki _Authorise this computer_ düğmesine tıklayın.
* Web sitesi açılır; oturum açın ve yetkilendirmeyi tamamlamak için ekrandaki talimatları izleyin

Artık erişiminiz olmayan bir bilgisayarın yetkisini uzaktan da kaldırabilirsiniz (bazı sınırlamalarla). Bkz. [Yetkilendirme ve yetkiyi kaldırma](installation/authorising-and-de-authorising.md)

#### **Kaybolan veya çalınan bir bilgisayarda Liberation yetkisini kaldırabilir miyim?**

Bilgisayarın yetkisini web sitesi üzerinden kaldırabilirsiniz. Liberation kurulumu son yenilemenizden beri çevrimiçi olmadıysa bu işlem hemen yapılabilir.

Aksi durumda yetki kaldırma işlemi abonelik yenilendiğinde veya bilgisayar internete bağlandığında, hangisi önce gerçekleşirse, yürürlüğe girer. Yeni bir bilgisayarı acilen yeniden yetkilendirmeniz gerekiyorsa destek ekibiyle iletişime geçin.

### Liberation’ı kullanma

#### Varsayılan kurulumda 8 lazer var - bunu nasıl değiştiririm?

Bkz. [Projenizi ayarlama](setting-up/setting-up-your-project.md) ve [Lazer ekleme ve kaldırma](setting-up/adding-removing-lasers.md)

#### Bir lazerdeki zone ayarlarını diğerlerine kopyalayabilir miyim?

Evet! Bkz. [Zone ayarlarını lazerler arasında kopyalama](output-view/copy-zones-between-lasers.md)

#### Kaydırıcı kullanmak yerine sayı yazabilir miyim?

Evet. `Cmd / Ctrl` tuşuna basılı tutarak kaydırıcıya tıklayın; değeri klavyeyle girebilirsiniz.

#### **Liberation’ı müzikle nasıl senkronize ederim?**

Beklediğiniz gibi çalışan akıllı bir “tap tempo” sistemi vardır; ayrıca harici MIDI clock veya Ableton Link de kullanabilirsiniz. Bkz. [Tempo senkronizasyonu](tempo-synchronisation.md). Zaman çizelgesi, herhangi bir ses arayüzü üzerinden gelen LTC/SMPTE timecode ile senkronize edilebilir. Bkz. [Timecode](timecode.md).

#### Lazerden en iyi çıkışı almak için hangi ayarları yapmam gerekir?

Ana ayar _Colour Shift_ ayarıdır; bu ayar aynaların hareket etmesiyle lazerlerin parlaklık değiştirmesi arasındaki küçük gecikmeyi telafi eder. Lazer noktalarında/ışınlarında küçük “kuyruklar” varsa bunu ayarlamanız gerekir. (“Kuyruk” örneği için [Laser Settings](setting-up/laser-settings.md) sayfasındaki fotoğraflara bakın)

Scanner hızını da değiştirmeyi deneyebilirsiniz: scanner’larınız basitse daha yavaş, iyiyse daha hızlı kullanabilirsiniz. Ancak **dikkatli olun; scanner’ları çok zorlamak onlara zarar verebilir.**

Bazı hazır scanner ayarları da vardır. Varsayılan seçenek temkinlidir ve çoğu lazer ışını gereksinimi için uygundur. Daha iyi scanner’larınız varsa başka preset seçenekleri, grafikler için ayarlanmış preset seçenekleri de vardır.

Daha fazla bilgi için bkz. [Laser Settings](setting-up/laser-settings.md); kendi preset ayarlarınızı oluşturma hakkında bilgi için bkz. [Scanner ön ayarları](advanced/scanner-presets.md) (ileri seviye, hazırlanıyor)

Renk dengesini _Colour calibration_ ayarlarıyla da düzeltebilirsiniz. Bkz. [Renk kalibrasyonu](advanced/colour-calibration.md) (ileri seviye teknik)

#### _Latency(ms)_ ayarı ne işe yarar?

Bu, frame gecikmesidir; yani bir frame oluşturulduktan sonra lazerlere gönderilene kadar geçebilecek maksimum süredir. Normalde bunu ayarlamanız gerekmez, ancak ağ sorunları yaşıyorsanız artırmayı deneyebilirsiniz. Daha fazla ayrıntı için bkz. [Latency ayarı](setting-up/latency-setting.md).

### Clips

#### Bir Clip çalıştırmadan zone ve ayarlarını nasıl düzenlerim?

Etkinleştirmeden _o anda seçili Clip_ yapmak için `Alt / Option` tuşuna basılı tutarak tıklayın. Ayrıca bkz. [Clips başlatma ve durdurma](clips/starting-stopping-clips.md)

#### Clips nasıl kopyalanır?

`Alt / Option` tuşunu basılı tutarken tıklayıp sürükleyin. Ayrıca bkz. [Clip Deck düzenleme](clips/organising-your-clip-deck.md)

#### Clips nasıl silinir?

Clip öğelerini Clip Deck dışına sürükleyin. Ayrıca bkz. [Clip Deck düzenleme](clips/organising-your-clip-deck.md)

#### Çoklu seçim, silme, Clip Deck öğelerini birleştirme vb. işlemleri nasıl yaparım?

Bkz. [Clip Deck düzenleme](clips/organising-your-clip-deck.md)

#### Clip üzerindeki küçük mikrofon simgesi ve diğer simgeler ne anlama geliyor?

Bu simgeler, bir Clip öğesinin ses veya MIDI girişi aldığını gösterir; 3 nokta ise zone gecikmesi olduğunu belirtir. Bkz. [Clip düğmelerindeki küçük simgeler ne anlama geliyor?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
