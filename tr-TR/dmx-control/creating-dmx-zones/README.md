---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 DMX zone oluşturma

1. Art-Net node cihazınızı bağlayın ve [Art-Net node cihazına bağlanma](../connecting-to-an-artnet-node.md "mention") bölümündeki adımlarla kurun.
2. **DMX Zones** bölümünü açın ve **ADD DMX ZONE** seçeneğine tıklayın.
3. zone için **Node**, **Universe** ve **Address** ayarlarını fixture ile eşleşecek şekilde ayarlayın.
4. Fixture için bir **Preset** seçin. Preset; hangi DMX kanallarının sabit değerler, içerik açık/kapalı değerleri, RGB renk, X/Y konumu, parlaklık veya açık DMX Value girişleri alacağını tanımlar.
5. Kanal eşlemesini düzenlemek için **Edit DMX profile/channel mapping** seçeneğine (kaydırıcılar simgesi) tıklayın. Varsayılan preset, içerik açık/kapalı kanalı ve RGB renk kanallarıyla başlar.
6. Clip öğelerini beam veya canvas zone için atadığınız şekilde DMX zone öğesine atayın.
7. zone üzerinden DMX çıkışı vermeye hazır olduğunuzda **ARM** düğmesine basın.

{% hint style="warning" %}
Yalnızca etkinleştirilmiş DMX zone öğeleri canlı değer gönderir. Etkinleştirilmemiş DMX zone öğeleri, eşlenmiş kanallarını sıfıra çeker; bu, fixture kurulumu sırasında daha güvenlidir.
{% endhint %}

DMX çıkışı, lisans seviyenizle de sınırlıdır. **ARM** düğmesi devre dışıysa lisans seviyenizin DMX çıkışını içerip içermediğini veya etkinleştirilebilecek maksimum DMX zone sayısına ulaşılıp ulaşılmadığını kontrol edin.
