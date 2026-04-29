---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Uyumlu lazerler ve denetleyiciler (DAC'ler)

### Hangi lazerler Liberation ile uyumludur?

Lazerinizde standart bir ILDA girişi varsa, Liberation ile kullanabilirsiniz. Bunun için Ether Dream veya Helios DAC gibi uyumlu bir lazer denetleyicisi de gerekir ([Uyumlu lazer denetleyicileri](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - ev kullanımı için en ekonomik seçenek</p></figcaption></figure>

Aşağıdaki durumlarda harici bir denetleyiciye veya ILDA girişine ihtiyacınız yoktur:

* Lazerinizin içinde Ether Dream takılıysa veya;
* Wicked Lasers üretimi bir LaserCube kullanıyorsanız veya;
* Dahili Mercury bulunan bir X-Laser armatürünüz varsa veya;
* Dahili AVB denetleyicili bir Laser Animation Sollinger lazeriniz varsa (şu anda yalnızca macOS üzerinde test aşamasında)

{% hint style="info" %}
**Lazer denetleyicisi nedir?**

Lazer denetleyicisi (veya DAC), Liberation’dan gelen dijital veriyi alıp lazerinizin tarayıcılarını ve çıkışını kontrol etmek için gereken analog sinyallere dönüştüren bir donanım aygıtıdır. DAC adı da buradan gelir: Digital to Analog Converter, yani dijital-analog dönüştürücü.

Denetleyici bilgisayarınıza USB üzerinden veya standart bir bilgisayar ağı üzerinden bağlanır. Harici bir aygıt olabilir ya da lazerin içine takılmış olabilir.

Harici ise, lazerinize ILDA bağlantısı üzerinden bağlarsınız. ILDA, eski tip 25 pinli “D” konektör kullanan bir endüstri standardıdır. Bir ILDA kablosu alın, bir ucunu denetleyiciye, diğer ucunu lazere takın.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>Harici bir Ether Dream üzerindeki ILDA çıkışı</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>ILDA girişi dahil çeşitli bağlantıları gösteren bir lazerin arka paneli</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Standart bir ILDA kablosu</p></figcaption></figure>

### Benim için en uygun denetleyici hangisi?

Ev kullanıcısıysanız veya bilgisayara yakın konumdaki 4 ya da daha az lazerle küçük gösteriler yapıyorsanız, **Helios DAC** gibi USB denetleyiciler **en ekonomik** seçenektir.

**Ether Dream** gibi ağ DAC’leri, ağ kurmakta sorun yaşamayan ve çok sayıda lazer çalıştırmak isteyen **profesyonel** lazer operatörleri için **en iyi seçenektir**. Şimdiye kadar yapılan tüm büyük Liberation gösterileri Ether Dream ile çalıştırıldı.

Bir **LaserCube** kullanıyorsanız ayrı bir lazer denetleyicisine hiç ihtiyacınız yoktur. Liberation tüm LaserCube modelleriyle uyumludur. Eski modeller USB kablosuyla bağlanır, yeni modeller ise ağ üzerinden bağlanır.

En kolay seçeneği arayan bir profesyonelseniz, dahili Mercury bulunan X-Laser ünitelerini veya AVB kullanan Laser Animation Sollinger lazerleri değerlendirin.

### Uyumlu lazer denetleyicileri

#### Ether Dream (Ağ)

[Ether Dream](https://ether-dream.com) on yılı aşkın süredir kullanılmaktadır ve şu anda 4. sürümdedir. Liberation, Ether Dream 1, 2 ve 3. sürümlerle de çalışır. Son derece güvenilirdir.

Standart bir ağ üzerinden bağlanırsınız. Bağımsız üniteler olarak satın alınabilirler; hatta daha iyisi, lazerlerin içine takılabilirler.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) yeni başlayanlar için en iyi seçenektir ve Ether Dream’den daha ucuzdur. Ancak USB üzerinden bağlandığı için uzun kablo mesafeleri için önerilmez. Ayrıca 4’ten fazla cihaza bağlandığınızda, özellikle Windows üzerinde, USB veri ve sürücü sorunları yaşayabilirsiniz.

Ama evde yalnızca birkaç lazer çalıştırmak istiyorsanız, en ucuz ve en basit seçenektir.

#### Mercury (X-Laser ünitelerine dahili)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system), lazerleri geleneksel bir ışık konsolundan doğrudan çalıştırmak isteyen ışık tasarımcıları için geliştirilmiş, X-Laser’ın güçlü DMX lazer kontrol sistemidir. En son firmware güncellemesiyle Mercury artık **Ether Dream emülasyonu** da içerir. Bu sayede Liberation ile ve Ether Dream destekleyen diğer tüm yazılımlarla sorunsuz çalışır.

#### AVB (Laser Animation Sollinger ünitelerine dahili)

**AVB**, yüksek performanslı ve düşük gecikmeli ses ile veri akışı için kullanılan açık, ağ tabanlı bir protokoldür. Birçok LaserAnimation Sollinger projektörde AVB desteği doğrudan donanıma dahildir. Bu sayede Liberation, harici DAC gerektirmeden ağ üzerinden bu cihazlara bağlanabilir. Liberation’daki AVB desteği şu anda **yalnızca macOS üzerinde ve test aşamasındadır**; ayrıca **AVB destekli uyumlu ağ aygıtları** gerektirir. Doğru kurulduğunda profesyonel gösteriler için daha basit bir iş akışı, daha az harici aygıt ve güçlü güvenilirlik sunar.

#### Gelecekte desteklenecek denetleyiciler:

* [IDN](http://www.ilda-digital.com) (ILDA tarafından geliştirilen açık bir ağ protokolü; herhangi bir üretici tarafından uygulanabilir)

### Kablolama önerileri

En iyi performans için USB DAC’leri bilgisayarınıza yakın tutun ve lazerlere daha uzun ILDA kabloları kullanarak bağlayın. Ancak dikkatli olun; ILDA kabloları söküm sırasında kanca gibi bir yerlere takılabilir!

Ether Dream kullanıyorsanız, hepsini yine bir arada tutup uzun ILDA kablolarıyla lazerlere bağlayabilirsiniz. Alternatif olarak Ether Dream ünitelerini lazerlere yakın kurup daha uzun ağ kabloları kullanabilirsiniz.

İdeal kurulum, Ether Dream ünitelerinin veya diğer denetleyicilerin doğrudan lazerlerinizin içine takılı olmasıdır. Birleşik Krallık’ta bunu sizin için Stanwax Laser’dan Rob yapabilir.
