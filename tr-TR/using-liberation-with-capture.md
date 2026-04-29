---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Capture ile Liberation Kullanımı

Liberation, harici görselleştirici olarak [Capture](https://capture.se) desteği sunar (sürüm 1.0.3 ve sonrası). Capture’ı iş akışınızda zaten kullanıyorsanız, Liberation’ın canlı lazer çıkışını 3D sahnenizde görselleştirmek için kullanabilirsiniz.

### Nasıl çalışır?

Özel bir bağlantı işlemi veya manuel eşleştirme gerekmez.

Şu koşullar sağlandığı sürece:

* Liberation ve Capture aynı ağda olmalı
* Güvenlik duvarınız bağlantıya izin vermeli

…Liberation içinde ayarladığınız tüm lazerler Capture içinde otomatik olarak medya kaynakları olarak görünür. IP adresi yapılandırmanız veya özel bir şeyi etkinleştirmeniz gerekmez; kendiliğinden görünür.

### Capture içinde lazerleri görme

Liberation içinde yapılandırılmış tüm lazerler, Capture içinde kullanılabilir medya kaynakları olarak görünür.

Çıkışı gerçekten görebilmek için:

* Liberation içinde lazerin durumu armed olmalıdır
* Kaynak, Capture içinde bir lazer fixture öğesine bağlanmış olmalıdır

Lazer armed durumuna alındığında Capture, Liberation’dan gelen canlı çıkış akışını görselleştirir. Liberation içinde bir lazer disarmed durumundaysa, Capture içinde kaynak olarak görünmeye devam eder ancak herhangi bir çıkış vermez.

Capture içinde lazer kurulumu hakkında daha fazla yönerge ve destek için [capture.se](https://www.capture.se/) belgelerine bakın. <br>

### Lisans sınırları ve armed lazerler

Capture bağlantıları, fiziksel lazer çıkışlarıyla tamamen aynı şekilde değerlendirilir.

Bu şu anlama gelir:

* Yalnızca lisans seviyenizin izin verdiği sayıda lazeri armed durumuna alabilirsiniz
* Yalnızca armed durumundaki lazerler Capture’a etkin olarak veri gönderir

### Capture’a ihtiyacım var mı?

Hayır.

Liberation, her zaman kullanılabilen ve lisans seviyenize bağlı olmayan yerleşik bir 3D görselleştirici içerir. Harici yazılıma ihtiyaç duymadan gösterileri doğrudan Liberation içinde tasarlayabilir ve önizleyebilirsiniz.

Capture, aydınlatma veya gösteri tasarımı için zaten kullanıyorsanız yalnızca ek bir seçenektir.

### Sorun giderme

Lazerler Capture içinde görünmüyorsa:

* Her iki uygulamanın da aynı ağda olduğunu kontrol edin
* Güvenlik duvarı ayarlarınızı kontrol edin
* Liberation içinde lazerin armed durumunda olduğundan emin olun
