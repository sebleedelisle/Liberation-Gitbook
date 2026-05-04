---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Canlı MIDI kontrolörleri

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

Liberation için varsayılan donanım controller budur; kesinlikle önerilir. Hatta Liberation’ın en başından beri bu donanım etrafında tasarlandığını söylemek yanlış olmaz. APC40 cihazını takar takmaz Liberation otomatik olarak hemen bağlanır.

{% hint style="warning" %}
_Eyvah! Gösterinin ortasında USB fişim çıktı!_

Panik yapmayın; tekrar takmanız yeterli. Liberation otomatik olarak yeniden bağlanır, sorun olmaz.
{% endhint %}

### APC40 Mark 1 mi Mark 2 mi?

Kısaca, Mark 2 önerilir. Tam renkli düğmeleri vardır ve Liberation Clip Deck arayüzündeki renklere daha yakın görünür. Mark 1 sürümü gerektiğinde iş görür, ancak ekrandaki düzenden biraz farklı olduğu için daha kafa karıştırıcı olabilir. Ayrıca düğmeleri yalnızca kırmızı, turuncu veya yeşil yanabildiğinden Clip renkleriyle eşleşmez.

{% hint style="info" %}
Orijinal APC40 Mark 1, 2009’da(!) çıktı ve bazı kişiler metal gövdesi ile sağlam, konsol benzeri formu nedeniyle hâlâ onu tercih ediyor. Güncellenmiş Mark 2 ise 2014’te çıktı. 2024’te üretimi durdurulmuş olsa da görsel sanatçılar (Resolume vb.) ve lazer sanatçılarından gelen talep nedeniyle 2025’te yeniden üretime giriyor.
{% endhint %}

APC40 üzerindeki tüm kontrollerin listesi için bkz. [APC40 referansı](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 ayrıca bir APC Mini profili içerir. Bu profil 8x5 Clip ızgarasını, zone için düğmeleri, zone X/Y çevirme kontrollerini, grup düğmelerini, tüm Clip öğelerini durdurmayı, Clip sayfası geçişini, zone sayfası geçişini, tap tempo, bar reset ve tempo nudge kontrollerini eşler. Sürgüleri efekt düzeylerini kontrol eder; Shift ile kullanılan sürgüler ise efekt parametrelerini kontrol eder. Son sürgü Global Brightness değerini kontrol eder.

### MIDI Fighter Twister

MIDI Fighter Twister profili, Clip başlatmadan çok enkoder ağırlıklı kontrol için tasarlanmıştır. Bir enkoder satırı 1-8 arasındaki efekt slotları için parametre 1’i kontrol eder; başka bir satır ise Clip kaydırma, zone gecikmesi, global döndürme/ölçekleme ve grup fade kontrolleri dahil olmak üzere Parameters panelindeki sekiz bağlamsal kontrolü izler.
