---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube tanıtım görseli Wicked Lasers’ın izniyle kullanılmıştır</p></figcaption></figure>

Wicked Lasers’ın [LaserCube](https://www.laseros.com/lasercube/) cihazı, farklı güç seçenekleriyle sunulan, son derece kompakt ve pille çalışan bir lazer ünitesidir. Kullanımı kolay akıllı telefon uygulaması sayesinde hobi kullanıcıları arasında popülerdir; ancak yeni modeller profesyonel gösterilerde kullanılabilecek kadar yeteneklidir.

Telefon uygulaması LaserOS adını taşır ve masaüstü sürümü de vardır. Ücretsiz indirilebilir, kullanması oldukça keyiflidir ve çoğu kullanıcı için yeterlidir. Ancak birden fazla lazerle daha büyük gösteriler yapıyorsanız daha özel ve güçlü bir çözüme ihtiyaç duyarsınız; Liberation tam da burada devreye girer.

### LaserCube bağlantısı kurma

İlk LaserCube modelleri USB üzerinden kontrol edilir. Güncel modellerin tamamında ise yerleşik bir ağ denetleyicisi bulunur. Ağ üzerinden kontrol edilen bu küpler “LaserCube Wifi” olarak bilinir. Liberation, ister USB ile ister ağ üzerinden bağlansın, her iki LaserCube türünü de destekler.\*

\*(LaserCube ağ protokolü desteği 0.7.3 sürümünde eklenmiştir)

### USB LaserCube

LaserCube cihazınızı bir micro USB kablosuyla bilgisayarınıza bağlayın, ardından _Controller Assignment_ panelinde arayın. (Bkz. [Controller Assignment](../setting-up/controller-assignment.md)). Otomatik olarak görünmezse _REFRESH_ düğmesine basın.

### Ağ üzerinden LaserCube “Wifi”

{% hint style="danger" %}
“Wifi” modeller kablosuz ağ üzerinden çalışacak şekilde tasarlanmış olsa da bu önerilmez; büyük olasılıkla kesilmeler ve takılmalar yaşarsınız. Bunun yerine, tıpkı Ether Dream kullanırken yapacağınız gibi LaserCube cihazınızı RJ45 soketiyle kablolu bir ağa bağlayın.
{% endhint %}

LaserCube cihazınızı kablolu ağınıza bağlayın.

LaserCube cihazınızı “LAN Client” moduna alın ve ağınızda bir router bulunduğundan emin olun. LaserCube, IP adresini router üzerinden alır ve ardından _Controller Assignment_ panelinde görünmelidir. (Bkz. [Controller Assignment](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Router olmadan bir ağ kurup tüm cihazlara sabit IP adresleri vermek mümkündür; etkinlik sektöründe bu oldukça yaygındır. Ben kişisel olarak ağa bir router eklemeyi tercih ediyorum ve ağ konusunda daha az deneyimli olan herkese bu seçeneği öneriyorum.

Router, her cihaza dinamik olarak bir IP adresi atar. Bence bu yöntem daha basit ve hata yapma olasılığı daha düşüktür.
{% endhint %}

{% hint style="danger" %}
Ether Dream’den farklı olarak, _**LaserCube cihazları buffer under-run, kayıp paket veya başka bir bozuk / hatalı veri durumunda LAZER ÇIKIŞINI KAPATMAZ**_.

Bunun yerine kaldıkları yerden devam ederler. Bazı durumlarda bu, aktif bir ışının zone olarak belirlenmemiş alanlardan geçmesine ve daha da kötüsü, yazılımda tanımlı mask alanlarını kesmesine neden olabilir.

LaserCube tasarımcıları/geliştiricileriyle bu konuda görüşüyorum ve ileride bir firmware güncellemesiyle bunun düzeltilmesini umuyorum. Ancak o zamana kadar lazerin gitmesini istemediğiniz her yeri fiziksel olarak maskelemeniz gerekir.

Açık olmak gerekirse, bunu zaten muhtemelen yapmanız gerekir. Ancak ben kameraları ve projektörleri korumak için yazılım mask kullanıyorum. Bu yüzden, LaserCube ağ protokolüyle bunu yapmanın Ether Dream’e göre daha tehlikeli olduğunu unutmayın. Ether Dream herhangi bir hata veya eksik veri olduğunda hemen güvenlik durdurma moduna geçer.

Ayrıca, bunu zaten söyledim ama **LaserCube cihazınız için kablolu bağlantı kullanın**. Wifi yeterli olmayacak ve bu sorunu daha da kötüleştirecektir.
{% endhint %}
