---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation, ışıkları, piroteknikleri, videoyu ve backing track'leri zamanında tutmak için canlı müzik gösterilerinde yaygın olarak kullanılan harici bir SMPTE/LTC timecode sinyaliyle senkronizasyonu destekler.

{% hint style="info" %}
SMPTE/LTC nedir?

SMPTE bir timecode standardıdır; LTC ise bu timecode bilgisinin ses sinyaline dönüştürülmüş hâlidir. Bu sesi dinlerseniz rahatsız edici, tiz bir cızırtı gibi gelir; ancak bilgisayarlar için yüksek çözünürlüklü zamanlama bilgisidir.

**Meraklısına bilgiler!**

Geçmişte SMPTE, video ve sesi senkron tutmak için kullanılırdı. Analog banda senkronlama yapılırken de bir kanala timecode sesi kaydedilirdi; buna bazen bandı "striping" yapmak denirdi. Bu timecode kanalını, birden fazla teyp cihazını birbiriyle senkron tutmak ya da bir MIDI sequencer'ı banda senkronlamak için kullanabilirdiniz. (Böylece MIDI enstrümanlarını banda kaydetmenize gerek kalmazdı; miks yaparken sequencer'ın bunları canlı çalmasını sağlayabilirdiniz!)

SMPTE, standardı tanımlayan Society of Motion Picture and Television Engineers'ın kısaltmasıdır. LTC ise _Linear TimeCode_ anlamına gelir.
{% endhint %}

Bilgisayarınızdaki herhangi bir ses arabirimi üzerinden LTC timecode sinyali alabilirsiniz; ancak en az bir ayarlanabilir XLR girişi ve izleme özelliği olan profesyonel bir arabirim kullanmanız önerilir.

[M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) ile iyi deneyimlerim oldu; kulaklıkla izleme, 2 XLR girişi var ve özel sürücü gerektirmiyor (en azından macOS'ta). Yalnızca timecode için kullanacaksanız biraz daha ucuz olan [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) modelini alabilirsiniz (yalnızca bir girişi var ve MIDI yok), ama açıkçası makul kalitede herhangi bir ses arabirimi iş görmelidir.

{% hint style="info" %}
LTC timecode sinyalleri genellikle dengeli XLR kablolar üzerinden dağıtılır; çünkü düşük seviyeli ses sinyallerini uzun mesafelere iletecek kadar dayanıklıdırlar. (XLR, genellikle mikrofonlarla kullanılan silindirik jak konnektörüdür.)
{% endhint %}

### Donanım bağlantıları

Timecode sinyalinin XLR kablosunu ses arabiriminize takın ve düzgün bir sinyal aldığınızdan emin olun. Ses arabirimindeki seviyeyi, sinyal güçlü olacak ama clipping yapmayacak şekilde ayarlayın. Ses arabiriminizde kulaklık çıkışı varsa timecode'u dinleyerek kesilme ya da bozulma olmadığını ve üzerinde fazla gürültü bulunmadığını kontrol edebilirsiniz.

{% hint style="info" %}
Teorik olarak sinyali MacBook'unuzdaki jak girişinden almak mümkündür, ancak bunun için özel bir kablo gerekir. Bu jaklar genellikle 4 kutuplu TRRS mini jaklardır. Açıkçası bu konnektörlerden hangisinin ses girişi için kullanılabileceğinden ve hangi voltaj seviyesini kabul edebileceğinden emin değilim (bir yerde +/-1V olduğunu okumuştum, ama bunu kendi sorumluluğunuzda kullanın!).

Bunu denemek yerine ucuz bir USB ses arabirimi edinmeniz bence çok daha iyi olur.
{% endhint %}

Ses arabiriminizde herhangi bir giriş izleme özelliği yoksa sinyal aldığınızdan emin olmak için macOS sistem ayarlarından (_Sound_ altında) kontrol edebilirsiniz. (Windows'ta _Sound Control Panel_ kullanın.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS, Sound sistem ayarları panelinde herhangi bir ses arabirimi için giriş seviyesini gösterir</p></figcaption></figure>

### Liberation içinde ayarlama

1. Timecode ayarları penceresinde ses arabiriminizi ve doğru giriş kanalını seçin.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Açılır menüde ses arabiriminizdeki her giriş kanalı için ayrı seçenekler bulunduğunu unutmayın.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Soldaki kareye dikkat edin: geçerli bir timecode sinyali alıyorsanız yeşil olur. Almıyorsanız kırmızı olur.

2. Gelen timecode için doğru kare hızını seçin. Size timecode sağlayan kişi kare hızının ne olduğunu söyleyebilmelidir. (Yanlış seçerseniz yine senkron olur, ancak her saniye küçük bir "atlama" fark edersiniz.)
3. Timeline çubuğundaki küçük saat simgesini kullanarak Timeline timecode ayarlarını açın ve SMPTE(LTC) seçeneğini seçin.

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Başlangıç offset değerini (saat, dakika, saniye, kare) şarkının başlangıcıyla eşleşecek şekilde ayarlayın. Birden fazla timeline varsa bu seçenekleri her biri için ayrı ayrı ayarlamanız gerekir.

{% hint style="info" %}
Turne dünyasında yaygın bir kullanım, her şarkıyı farklı bir saatte başlatmaktır; örneğin ilk şarkı için 01:00:00:00, ikinci şarkı için 02:00:00:00 ve böyle devam eder.

Liberation, timecode'a bağlı olarak timeline arasında otomatik geçiş yapar; bu yüzden gösteri sırasında timeline'ları elle değiştirmeniz gerekmez.
{% endhint %}

MIDI Clock ve Ableton Link'ten farklı olarak SMPTE'nin saat, dakika, saniye ve kare cinsinden ölçülen _mutlak_ bir zaman sistemi olduğunu unutmayın. Liberation'ın temel zaman sistemi beat ve bar üzerine kuruludur; bu yüzden timecode aldığınızda timeline içinde ayarlanmış tempoyu kullanır. Bu temponun, timecode ile senkronlanan müzikle de uyumlu olduğundan emin olmanız gerekir.
