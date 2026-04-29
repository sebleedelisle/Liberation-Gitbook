---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Giriş

Liberation, Art-Net üzerinden ışık efektleri oluşturmanızı ve DMX uyumlu lazerleri kontrol etmenizi sağlayan esnek ve güçlü bir DMX sistemi içerir. Aydınlatmanızı lazer gösterinizle senkron tutmayı kolaylaştırmak için tasarlanmıştır; ayrı bir ışık masasına gerek yoktur.

{% hint style="info" %}
**Art-Net nedir ve DMX ile nasıl ilişkilidir?**

**DMX**, ışıkları, lazerleri, duman makinelerini ve diğer sahne efektlerini kontrol etmek için yıllardır kullanılan bir sistemdir. Kontrol sinyallerini özel kablolar üzerinden gönderir (genellikle XLR konnektörlerle) ve her cihaz ne yapacağını anlamak için belirli bir kanal grubunu dinler.

**Art-Net**, aynı DMX verisini normal bir bilgisayar ağı üzerinden göndermenin daha yeni bir yoludur. Özel kablolar kullanmak yerine her şeyi Ethernet üzerinden, internet veya yerel ağ trafiği gibi gönderir.

Liberation’da tüm DMX çıkışı Art-Net kullanılarak gönderilir. Art-Net uyumlu cihazları doğrudan kontrol etmek için kullanabilir veya bir **Art-Net node** bağlayabilirsiniz. Bu küçük kutu, Art-Net’i tekrar standart DMX’e dönüştürür. Böylece Art-Net desteği olmayan geleneksel DMX ışıklarını ve efektlerini de kontrol edebilirsiniz.
{% endhint %}

Bunu duman makineleri, haze makineleri, CO₂ jetleri, soğuk kıvılcım makineleri ve benzeri birçok farklı sahne ekipmanını kontrol etmek için de kullanabilirsiniz. DMX destekliyorsa, bunu bir DMX zone olarak ayarlayabilir ve lazer içeriğinizle birlikte doğrudan Liberation’dan tetikleyebilirsiniz.

DMX cihazları **DMX zones** olarak eklenir ve zone listesinde lazer beam zones ve Canvas hedef alanlarının yanında görünür. Her DMX zone, Liberation’a lazer Clips içindeki konum, renk ve parlaklık gibi özellikleri DMX kanal değerlerine nasıl eşleyeceğini söyleyen bir **DMX preset** kullanır.

Bir Clip’i DMX zone içine gönderdiğinizde, Liberation Clip içindeki ilk öğeye bakar ve preset’e göre bu öğenin özelliklerini dönüştürür. Böylece lazerler için zaten kullandığınız aynı Clips üzerinden ışıkları ve DMX efektlerini doğrudan sürmek kolaylaşır.

#### Glastonbury’de Liberation

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Liberation DMX sisteminin ilk gerçek testi, Reach Lasers’ın Arcadia “spider” sahnesinin bir parçası olarak toplam 90 beam kaynağı kurduğu Glastonbury 2023’te yapıldı.

18 lazer dahili Ether Dream ile kontrol edildi; ayrıca 12 adet 6 başlı beam bar, Art-Net ve DMX üzerinden kontrol edildi.
