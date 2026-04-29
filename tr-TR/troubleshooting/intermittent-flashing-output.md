---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Kesintili / yanıp sönen çıkış

_Laser Overview_ panelini açın ve sorun yaşadığınız lazerin yanındaki bağlantı ışığına bakın.

**Bağlantı ışığı sürekli yeşil DEĞİLSE:**\
Bu durumda sorun büyük olasılıkla ağdan veya CPU performansından kaynaklanıyordur:

**Ağ performansı -**

* Bir Wi-Fi ağına bağlı olmadığınızdan emin olun. Her zaman kablolu bağlantı kullanmalısınız. İşletim sisteminizin Wi-Fi yerine kablolu ağı önceliklendirdiğinden emin olun; emin değilseniz Wi-Fi’ı devre dışı bırakın.
* Ağ adaptörünüzü kontrol edin ve farklı bir USB-C adaptörü deneyin.
* Windows kullanıcıları: ağ sürücülerinizi kontrol edin / yükseltin, uygun ağ test araçlarını çalıştırın.
* Tüm kabloları, anahtarları ve yönlendiricileri kontrol edin. Her kabloyu yöntemli şekilde değiştirip test edin.
* Anahtarlar, yönlendiriciler ve tüm Ether Dream cihazları dahil olmak üzere tüm ağ ekipmanınızı yeniden başlatın.

**CPU performansı**

Eski veya düşük özellikli bir bilgisayarınız varsa Liberation’ı çalıştırmak için fazla yavaş kalabilir. Simge çubuğunun sağ tarafındaki kare hızı göstergesini kontrol edin.

Burada iki sayı bulunur: gerçek kare hızı ve hedef kare hızı. Gerçek kare hızı 30’un altına düşerse sorun yaşayabilirsiniz.

Aşağıdaki işlemler yardımcı olabilir:

* Kullanmadığınız lazerleri kaldırın; örneğin yalnızca bir lazer bağlıysa diğerlerini silin.
* Output view veya Canvas view görünümüne geçin.
* Diğer tüm programları kapatın, ağ güvenlik duvarı ayarlarını kontrol edin, antivirüs, Dropbox vb. uygulamaları kapatın.
* Ekran çözünürlüğünüzü düşürün ve Liberation penceresini küçültün.

Bunların hiçbiri işe yaramazsa bilgisayarınızı yükseltmeyi düşünün.

***

**Bağlantı ışığı sürekli yeşilse:**

Bu durumda sorun büyük olasılıkla donanımla ilgilidir. Bu konu bu kılavuzun kapsamı dışındadır, ancak aşağıdakileri deneyebilirsiniz:

* SFS (Scan Fail Safety) sistemini devre dışı bırakın. Bazı lazerlerde, tarayıcılar hareket etmeyi durdurursa, yani güçlü ve sabit bir ışın oluşursa çıkışı devre dışı bırakan bir işlev bulunur. Bu sistemler biraz fazla temkinli / güvenilmez olabilir.

{% hint style="danger" %}
Scan Fail Safety sistemini devre dışı bırakırken son derece dikkatli olun. Güçlü sabit ışınlar yanmaya neden olabilir! Elinizin altında bir durdurma düğmesi ve yangın söndürücü olduğundan emin olun.
{% endhint %}

* Güvenlik kilitleme kablolarını ve sistemlerini kontrol edin.
* Controller ile lazer arasındaki tüm kabloları kontrol edin.

Bir [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp), lazer sorunlarını gidermek için çok değerli bir araç olabilir.
