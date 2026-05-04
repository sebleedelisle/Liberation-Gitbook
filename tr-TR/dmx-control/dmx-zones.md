---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX zones

DMX zone, lazer noktaları yerine Art-Net/DMX gönderen Liberation Output zone türleridir. Beam zone ve canvas zone ile birlikte görünürler; böylece Clip öğeleri aynı zone seçici iş akışıyla bunlara atanabilir.

Bunları yönetmek için menüden **DMX Zones** öğesini açın veya Laser Overview içindeki DMX bölümünü kullanın.

* **ADD DMX ZONE** - yeni bir DMX zone oluşturur.
* **ARM** - ilgili zone için DMX çıkışını etkinleştirir. Silahlandırılmamış bir DMX zone, eşlenmiş kanallarını sıfıra temizler.
* **Node** - Art-Net node numarasını seçer.
* **Universe** - Art-Net universe değerini seçer. Gösterilen değer 1 tabanlıdır; yani Universe 1, ilk universe anlamına gelir.
* **Address** - armatürün başlangıç adresini ayarlar. Gösterilen değer burada da 1 tabanlıdır.
* **Preset** - Clip içeriğini DMX kanallarına eşleyen DMX preset öğesini seçer.
* **Edit DMX zone settings** (kalem simgesi) - manuel zone yönlendirme ve armatür yönü gibi zone ayarlarını açar.
* **Edit DMX profile/channel mapping** (kaydırıcılar simgesi) - DMX preset/kanal düzenleyicisini açar.
* **Delete** - DMX zone öğesini kaldırır.

### Silahlandırma sınırları

Aynı anda silahlandırılabilecek DMX zone sayısı, lisans seviyenize bağlıdır. Lisans seviyeniz DMX çıkışına izin vermiyorsa veya en fazla sayıda DMX zone öğesini zaten silahlandırdıysanız, ek zone öğeleri için **ARM** düğmesi devre dışı kalır ve üzerine gelindiğinde giriş yasak simgesi gösterir.

Daha fazla zone silahlandırmadan önce başka bir DMX zone öğesini devre dışı bırakın veya daha yüksek DMX sınırına sahip bir lisans seviyesi kullanın.
