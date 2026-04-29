---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Controller Assignment

Liberation içinde lazerleri ayarladıktan sonra, her birini gerçek dünyadaki bir lazer denetleyicisine atayabilirsiniz. (Kullanabileceğiniz donanımları kontrol etmek için [uyumlu lazerler ve denetleyiciler (DAC’ler)](../hardware/compatible-lasers-and-controllers-dacs.md) bölümüne bakın.) Denetleyiciler USB üzerinden veya ağ üzerinden bağlanır.

* _View -> Controller Assignment_ menü seçeneğiyle _Controller Assignment_ panelini açın. (Alternatif olarak _Laser Overview_ panelindeki _ASSIGN LASER CONTROLLERS_ düğmesini de kullanabilirsiniz.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment paneli"><figcaption></figcaption></figure>

* Panel ikiye ayrılmıştır: solda lazerlerin listesi, sağda ise kullanılabilir denetleyicilerin listesi bulunur. Lazer denetleyicinizi listede görmüyorsanız _REFRESH_ düğmesine basın. Sorun yaşamaya devam ederseniz [sorun giderme](../troubleshooting/) bölümüne bakın.
* Bir denetleyiciyi bir lazere atamak için sağ taraftan tıklayıp sürükleyerek soldaki boş bir lazer yuvasına bırakın. Bu işlem Liberation’a hangi denetleyiciyi hangi lazer için kullanacağını söyler. (Fikrinizi değiştirirseniz denetleyicileri bir lazerden diğerine serbestçe yukarı veya aşağı sürükleyebilirsiniz.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Denetleyici listesi" width="375"><figcaption></figcaption></figure>

* Denetleyicinin yanında yeşil bir kare görüyorsanız Liberation bu denetleyiciye başarıyla bağlanmış demektir.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Sırasıyla 2 ve 3 numaralı lazerlere atanmış bir Ether Dream ve bir Helios DAC</p></figcaption></figure>

{% hint style="info" %}
Bir denetleyiciye her bağlandığınızda lazer çıkışının otomatik olarak devre dışı bırakılacağını unutmayın.
{% endhint %}

* Turuncu kare 🟧, denetleyicinin ara sıra bağlantı sorunları yaşadığı anlamına gelir. Bu genellikle bir ağ sorunundan kaynaklanır; [sorun giderme](../troubleshooting/) bölümüne bakın.
* Kırmızı kare 🟥, denetleyiciye ulaşılamadığı anlamına gelir; [sorun giderme](../troubleshooting/) bölümüne bakın.
* _Bağlantıyı kes düğmesi_ (X), denetleyicinin bağlantısını keser ancak lazer atamasını temizlemez. Daha sonra _yeniden bağlan düğmesini_ (yenileme oku simgesi) kullanarak tekrar bağlanabilir veya atamayı temizlemek için _bağlantıyı kes düğmesine_ yeniden tıklayabilirsiniz.
* _Gelişmiş özellik:_ Grafik gibi görünen düğmeye tıklayarak denetleyici analiz panelini açın. Bu gelişmiş özellik, veri akışı hakkında ayrıntılı bilgi verir ve sorunları gidermenize yardımcı olabilir. (Bu seçenek bazı denetleyici türlerinde kullanılamayabilir.)
* Bu denetleyiciyi istediğiniz şekilde yeniden adlandırmak için _yeniden adlandır düğmesini_ (kalem) kullanabilirsiniz. Belirli bir donanımla ilişkilendirmeyi kolaylaştıracak bir ad vermek mantıklıdır. Denetleyici bir lazerin içine yerleşikse buna uygun bir ad verebilirsiniz; örneğin _LaserCube Ultra #1_ veya _Triton T5 #3._ Bu adlar Liberation kurulumunuzla birlikte kaydedilir ve bundan sonra görünür; lazerlerinizi hızlıca tanımanız için gerçekten faydalı olabilir.

{% hint style="info" %}
İpucu: Sağdaki bir denetleyiciye **çift tıklayarak** onu soldaki bir sonraki kullanılabilir lazere otomatik olarak atayabilirsiniz. Atanacak çok sayıda lazeriniz varsa bu ciddi zaman kazandırır!
{% endhint %}

Tüm bağlantıları hızlıca sıfırlamak için _DISCONNECT ALL_ ve _RECONNECT ALL_ düğmelerini kullanabilirsiniz. Ağ sorunları yaşıyorsanız bu işlem faydalıdır.
