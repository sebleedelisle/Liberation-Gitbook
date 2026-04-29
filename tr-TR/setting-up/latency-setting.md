---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Gecikme ayarı

_Settings_ panelinde (_Liberation->Settings_ veya CMD/CTRL ,) _Latency(ms)._ etiketli bir kaydırıcı görürsünüz. (Liberation’ın eski sürümlerinde bu ayar Laser Overview panelindeydi)

{% hint style="info" %}
Varsayılan 150 ms gecikme ayarı çoğu durumda yeterli olur. Ancak ağ sorunları yaşıyorsanız bu değeri artırmayı deneyebilirsiniz.
{% endhint %}

### Ayrıntılı açıklama

Bu "kare gecikmesi" ayarı, Liberation’ın bir kare oluşturması ile lazerin o kareyi çıkışa vermeye başlaması arasındaki en uzun süredir. Bu değeri artırırsanız Liberation ile lazer çıkışı arasında hafif bir gecikme fark edebilirsiniz.

Daha uzun kare gecikmesinin avantajı, Liberation’ın laser controller aygıtlarının arabelleklerini olabildiğince erken içerikle doldurabilmesidir. Ağda yoğunluk olursa controller aygıtının noktaları tüketip boşta kalma olasılığı azalır.

Bu genellikle yalnızca ağ DAC cihazları için geçerlidir ve 100 ms ayarı, hız ile ağ gecikmelerine karşı koruma arasında iyi bir denge sağlar. Gerçekten güçlü bir ağınız varsa bunu 50 ms’ye düşürebilirsiniz.&#x20;
