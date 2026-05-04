---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Liberation açılmazsa ne yapmalı?

Nadiren de olsa Liberation başlamayabilir veya açıldıktan hemen sonra çökebilir. Bu durum neredeyse her zaman yerel yapılandırma dosyalarından birinin bozulmasından kaynaklanır; genellikle sistem çökmesi ya da bilgisayarınızda beklenmeyen bir olay sonrasında olur.

Neyse ki yerel ayarlarınızı sıfırlayarak bunu kolayca düzeltebilirsiniz. macOS ve Windows üzerinde bunu nasıl yapacağınız aşağıda açıklanmıştır.

> **Önemli**
>
> * Herhangi bir işlem yapmadan önce Liberation’ı kapatın.
> * Bu adımlar yalnızca yerel ayarları, günlükleri ve önbellekleri etkiler. Lisansınız ve hesabınız güvendedir.

***

#### Çalışma klasörünü nerede bulabilirsiniz?

Liberation’ın her sürümünün kendi çalışma klasörü vardır. Örneğin 1.0.3 sürümünü çalıştırıyorsanız klasör adı 1.0.3 olur.

* **macOS**: `~/Library/Application Support/Liberation/1.0.3`
* **Windows**: `AppData\Local\Liberation\1.0.3`

**Klasörü hızlıca açma**

**macOS**

1. Finder’da **Shift + Cmd + G** tuşlarına basın.
2.  Bu yolu yapıştırın ve **Enter** tuşuna basın:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Sürüm numaranızla eşleşen klasörü açın; örneğin `1.0.3`.

**Windows**

1.  **Win + R** tuşlarına basın, bunu yapıştırın ve **Enter** tuşuna basın:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Sürüm numaranızla eşleşen klasörü açın; örneğin `1.0.3`.

> **Windows için ipucu**: Bunun yerine Dosya Gezgini ile göz atıyorsanız gizli öğeleri etkinleştirin: **Görünüm > Göster > Gizli öğeler**.

***

#### Adım 1 – Ayarlar dosyanızı güvenli şekilde sıfırlayın

Sürüm klasörünüzün içinde şunu açın:

```
data/liberation/
```

liberation klasörünün içinde `settings.json` adlı bir dosya bulmanız gerekir. Bu dosyayı silin.

* **macOS örneği**: `~/Library/Application Support/Liberation/1.0.3/data/liberation/settings.json`
* **Windows örneği**: `%LOCALAPPDATA%\Liberation\1.0.3\data\liberation\settings.json`

Şimdi Liberation’ı başlatmayı deneyin. Açılırsa işlem tamamdır.

***

#### Adım 2 – Sorunlu bir Clip olup olmadığını kontrol edin

Liberation bir Clip düzenlerken çöktüyse, bu Clip dosyasındaki bir şey soruna neden oluyor olabilir.

settings.json dosyanızla aynı klasörde `clipEdit.json` adlı bir dosya bulmanız gerekir.

Bu dosyayı güvenli bir yere yedekleyin (örneğin Masaüstü), ardından Liberation çalışma klasöründen silin.

Liberation’ı tekrar başlatmayı deneyin. Şimdi normal şekilde açılıyorsa, soruna neyin neden olduğunu inceleyebilmemiz için lütfen yedeklediğiniz dosyayı [**info@liberationlaser.com**](mailto:info@liberationlaser.com) adresine e-postayla gönderin.

***

#### Adım 3 - Tüm çalışma klasörünü yedekleyin, ardından silin

Adım 1 ve Adım 2 işe yaramadıysa:

1. Sürüm klasörünün tamamını **yedekleyin**:
* macOS: `1.0.3` klasörüne sağ tıklayın ve zip oluşturmak için **Compress** seçeneğini seçin ya da Masaüstü gibi güvenli bir yere kopyalayın.
* Windows: `1.0.3` klasörüne sağ tıklayın ve **Send to > Compressed (zipped) folder** seçeneğini seçin ya da Masaüstü gibi güvenli bir yere kopyalayın.
2. Yedek aldıktan sonra, özgün `1.0.3` klasörünü Liberation çalışma konumundan **silin**.
3. Liberation’ı tekrar başlatın. Yeni bir çalışma klasörü otomatik olarak oluşturulur.

Liberation şimdi açılıyorsa Adım 4’e geçin.

***

#### Adım 4 - Yedeği bize gönderin

Bu, soruna neyin neden olduğunu belirlememize ve gelecekteki sürümlerde bunu önlememize yardımcı olur.

Adım 3’teki **yedeğinizi** henüz zip yapmadıysanız sıkıştırın, ardından nedeni teşhis edebilmemiz için e-postayla gönderin.

* **Kime**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Konu**: Liberation başlangıç düzeltmesi - çalışma klasörü yedeği
* **Gövde**: Lütfen şunları ekleyin:
  * İşletim sistemi ve sürümü (örn. macOS 14.6 veya Windows 11 23H2)
* Liberation sürümü (örn. 1.0.3)
  * Varsa hangi adımın sorunu çözdüğü (Adım 1, Adım 2 veya Adım 3)
  * Sorun başlamadan önce ne olduğuna dair kısa bir açıklama
* **Ek**: `1.0.3` çalışma klasörünüzün ziplenmiş yedeği.

> Zip dosyası e-posta için çok büyükse bir bulut sürücüsüne yükleyin ve bağlantı paylaşın.

***

#### Adım 3’ten sonra hâlâ başlamıyor mu?

Çalışma klasörünü sildikten sonra Liberation hâlâ açılmıyorsa:

* Bilgisayarınızı yeniden başlatın ve tekrar deneyin.
* Yeni klasörleri engelleyebilecek antivirüs veya güvenlik araçlarını geçici olarak devre dışı bırakın, ardından başlatmayı deneyin.
* En yeni Liberation derlemesini mevcut kurulumunuzun üzerine yeniden yükleyin.
* Yukarıdakilerin hiçbiri işe yaramazsa ayrıntılarla ve varsa `logs` alt klasöründeki çökme günlükleriyle birlikte [**info@liberationlaser.com**](mailto:info@liberationlaser.com) adresinden destek ekibiyle iletişime geçin.

***

#### Özet

1. Sürüme ait çalışma klasörünüzdeki `data/liberation/settings.json` dosyasını silin.
2. Bir Clip düzenliyorduysanız `data/liberation/clipEdit.json` dosyasını yedekleyin, ardından silin.
3. Hâlâ açılmıyorsa `1.0.3` klasörünün (veya kendi sürüm klasörünüzün) tamamını yedekleyin, ardından silin.
4. Adım 3 sorunu çözerse (veya çözmezse), yedeği zipleyip işletim sisteminiz ve Liberation sürümünüzle birlikte [**info@liberationlaser.com**](mailto:info@liberationlaser.com) adresine gönderin.
