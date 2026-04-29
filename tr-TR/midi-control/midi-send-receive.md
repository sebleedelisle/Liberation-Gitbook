---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive sistemi APC40 kontrollerinden ayrıdır ve MIDI verilerini Liberation içine alıp Liberation dışına göndermenin bir yoludur. Clip başlatma ve durdurma, genel ayarları düzenleme, efektler ve Clip parametreleri gibi işlevlerin her birine karşılık gelen bir MIDI komutu vardır.

{% hint style="info" %}
MIDI Send/Receive sistemi ilk olarak, Liberation içinde henüz Timeline işlevi yokken geliştirildi. Logic Pro veya Cubase gibi müzik yazılımlarına bir gösteriyi kaydedip oradan oynatmak için kullanabileceğiniz bir geçici çözüm olarak tasarlanmıştı.

Ekran görünümünden ve Clip Deck kaydırma konumundan bağımsız olarak Clips, efektler ve ayarlar üzerinde doğrudan kontrol sağlar. Tap tempo, zones atama ve arm/disarm gibi daha sistem düzeyindeki canlı kontrol özellikleri uygulanmamıştır.
{% endhint %}

### MIDI Send/Receive ayarları

_MIDI Send/Receive_ panelini açın (_View -> MIDI Send/Receive_ menüsünden). Kullanmak istediğiniz MIDI arayüzlerini seçebilmenin yanında, gönderme ve alma için _SEND, RECEIVE_ veya _BOTH_ seçeneklerinin bulunduğunu göreceksiniz.

{% hint style="danger" %}
_BOTH_ ayarını dikkatli kullanın. MIDI cihazları ve yazılımları, aldıkları veriyi geri gönderecek şekilde yapılandırılabilir. Bu durum MIDI verilerinde bir geri besleme döngüsüne yol açabilir ve bu iyi bir şey değildir!
{% endhint %}

### MIDI eşlemesi

Bkz. [MIDI gönderme/alma varsayılan eşlemesi](../reference/midi-send-receive-default-mapping.md)

Gelecekte çok daha özelleştirilebilir MIDI eşlemesi eklemeyi planlıyorum. Şimdilik Liberation ile özel donanımınız arasında dönüşüm yapmak için [BOME](https://www.bome.com/products/miditranslator) ve [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) gibi uygulamaları kullanabilirsiniz.
