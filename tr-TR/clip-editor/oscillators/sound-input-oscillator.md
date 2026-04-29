---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Ses girişi osilatörü

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Ses giriş seviyesini bir özellik değerine dönüştürür.

{% hint style="info" %}
Sound input osilatörü varsayılan ses arayüzünü kullanır, ancak bunu _Preferences_ içinde değiştirebilirsiniz. _Liberation -> Preferences_ menüsünü açın.

_Sound Input_ ayarları altında, kullanmak istediğiniz ses arayüzünü seçebilir ve ses seviyesini ayarlamak için bazı ek ayarları değiştirebilirsiniz.
{% endhint %}

* **range min / range max** - dalga formunun eşlendiği minimum ve maksimum değerler
* **channel** - Ses arayüzünüzde birden fazla giriş kanalı varsa, burada hangi kanalı alacağınızı seçebilirsiniz.

{% hint style="info" %}
Miks masasından birden fazla ses beslemesi almak eğlenceli bir tekniktir; böylece farklı Clip öğelerinin farklı müzik enstrümanlarına tepki vermesini sağlayabilirsiniz.
{% endhint %}

{% hint style="info" %}
Tüm _Sound Inputs_ genelinde aynı anda yalnızca bir ses arayüzü kullanabilirsiniz (_App Settings_ panelinde seçilir). Bunun için birden fazla arayüz kullanmak istiyorsanız, macOS’te girişleri tek bir sanal ses kaynağında birleştirmek için [bir Aggregate Device oluşturabilirsiniz](https://support.apple.com/en-gb/HT202000). (Windows’ta da bunu yapan birçok uygulama var, ancak ben denemedim).
{% endhint %}

* **clamp min / clamp max** - hangi seviye aralığına tepki vermek istediğinizi seçmek için bunu kullanın. Gate ve limit ayarları (_App Settings_ panelinde) doğru ayarlandıysa bunu değiştirmeniz gerekmez, ancak bazı yaratıcı efektler için kullanılabilir.

{% hint style="info" %}
Bir Clip düğmesinde _Sound Input_ osilatörü olduğunda üzerinde küçük bir mikrofon simgesi görürsünüz.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
