---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Giriş

Liberation içindeki 3D Visualiser son derece kullanışlı bir özelliktir; hiç lazer kullanmadan gösterilerinizi tasarlayıp geliştirebilirsiniz! Özellikle çok sayıda lazer içeren karmaşık kurulumlarda benim için vazgeçilmez bir araç olduğunu kanıtladı.

### 3D alanda gezinme

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser görünümü</p></figcaption></figure>

* Görünümü yörünge noktasının etrafında döndürmek için tıklayıp sürükleyin
* Yörünge noktasına doğru ileri ve geri hareket etmek için fare tekerleğini kullanın
* Kamerayı XY düzlemi boyunca sola, sağa, yukarı ve aşağı yatay olarak hareket ettirmek için shift tuşunu basılı tutarken tıklayıp sürükleyin
* Kamera konumunu sıfırlamak için visualiser üzerinde herhangi bir yere çift tıklayın

### Ayarlar

_Window_ menüsünden _3D Visualiser Settings_ panelini açın.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings paneli</p></figcaption></figure>

* **Visualiser size** - visualiser boyutunu uygulamanın geri kalanına göre değiştirir
* **Brightness Adjustment** - lazerlerin ne kadar parlak görüneceğini değiştirir
* **Show laser numbers** - her lazerin üzerinde ilgili numarayı gösterir
* **Show zone names** - her lazerin altında ilgili zone adlarını gösterir

### Kamera ayarları

Bu ayarlar çoğunlukla 3D alandaki sanal kamerayla ilgilidir. Bu ayarlar için kaydedip yeniden yükleyebileceğiniz preset’lerin bulunduğu bir açılır menü görebilirsiniz.

* **Camera distance -** Kamera her zaman kendi _Orbit point_ konumuna bakar. Kamera mesafesi, kameranın bu noktadan ne kadar uzakta olduğunu belirtir. Bu ayarı fare kaydırma tekerleğiyle de değiştirebilirsiniz.
* **FOV -** Görüş alanı; kameranın ne kadar geniş açılı veya yakınlaştırılmış olduğunu belirler.
* **Orbit position** - yörünge noktası etrafındaki mevcut dönüşü tanımlar. İlk değer X ekseni etrafındaki dönüşü (pitch), ikinci değer ise Y ekseni etrafındaki dönüşü (yaw) belirtir.
* **Orbit centre point** - yörünge noktasının 3D alandaki x, y, z konumudur.
* **Grid height** - ızgaranın “zeminden” yüksekliğidir (yani y = 0 olan yerden).

### İçerik ayarları

Bu ayarlar, lazerlerin ve Canvas öğesinin 3D ortamda nereye yerleştirileceğini belirler. Bu ayarlar için kaydedip yeniden yükleyebileceğiniz preset’lerin bulunduğu bir açılır menü görebilirsiniz.

#### Lazerler

Her lazerin, küçük beyaz üçgeni kullanarak genişletebileceğiniz kendi ayar grubu vardır.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiser lazer ayarları</p></figcaption></figure>

* **3D Position** - lazerin x, y ve z konumu.
* **3D Orientation** - lazerin x, y ve z eksenlerinin her biri etrafındaki dönüşü.
* **Flip X / Flip Y** - lazerin sanal Output yönünü çevirir. NOT: Normalde buna gerek olmamalıdır; donanımınızdaki tutarsızlıkları düzeltmek için lazer çevirme / yönlendirme ayarlarını kullanmak daha iyidir.
* **Output Range horizontal / vertical** - lazer tarayıcılarınızın maksimum / minimum açısıyla ilgilidir. 60º standarttır, ancak lazerleriniz farklıysa bunu ayarlayabilirsiniz.

#### Canvas

Canvas sistemini kullanıyorsanız, Canvas görüntüsünü 3D view içine dahil etmeyi de seçebilirsiniz. Canvas öğesini görüntülemek için onay kutusunu etkinleştirin ve 3D view içinde nasıl görüneceğini belirlemek için konum, yönlendirme ve ölçek ayarlarını kullanın.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiser Canvas ayarları</p></figcaption></figure>

{% hint style="info" %}
“Hayalet” lazerler mi görüyorsunuz? 3D Visualiser, lazer kurulumundan bir ölçüde bağımsızdır ve visualiser içinde Liberation projenizde olduğundan daha fazla lazer bulunması mümkündür. Projenize bir lazer eklediğinizde, visualiser içine yeni bir lazer nesnesi de eklenir. Ancak bir lazeri silerseniz, visualiser içinde hâlâ bir “hayalet” lazer nesnesi kalır.

Tüm hayalet lazerlerden kurtulmak için _Remove extra 3D laser objects_ düğmesine tıklayın (3D Visualiser ayarları panelinin en altında).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
