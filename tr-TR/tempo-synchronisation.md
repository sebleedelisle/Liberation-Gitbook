---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / senkronizasyon

Müzik senkronizasyonu Liberation için temel bir öğedir; tempo ve vuruşları müzikle eşleştirdiğinizde her şeyin senkronize olduğundan emin olabilirsiniz. MIDI clock veya Ableton Link kullanabiliyorsanız manuel senkronizasyonla hiç uğraşmanız gerekmez. Kullanamıyorsanız sorun değil; _Live_ tempo özelliğiyle manuel olarak eşleştirme yapabilirsiniz.

Müzik veya ışık yazılımlarıyla deneyiminiz varsa bu süreç size tanıdık gelecektir. Yoksa canlı gösteriye çıkmadan önce sistemi tanımak ve evde pratik yapmak için biraz zaman ayırmanız iyi olur.

## Tempo paneli

_Tempo_ paneli her zaman ekranda görünür ve tüm senkronizasyon ayarlarını içerir. Üst kısımda mevcut ölçü/vuruş sayacını ve play/pause ile rewind/fastforward düğmelerini içeren transport kontrollerini görürsünüz.

Bunun altında vuruş göstergesi yer alır: vuruşa göre “nabız gibi atan” dört kare. Bu _vuruş göstergesi_ son derece kullanışlı bir görselleştirmedir ve _Live_ tempo sistemini kullanırken ona sık sık bakarsınız.

### Tempoyu ayarlama

Tempoyu ayarlamak için şu seçenekleriniz vardır:

* _Tempo_ slider üzerinde tıklayıp sürükleyin
* Tempoyu 0,1’lik artışlarla değiştirmek için _Tempo_ slider üzerinde Shift ile tıklayıp sürükleyin
* _Tempo_ slider üzerine çift tıklayıp sayıyı manuel olarak yazın
* APC40 üzerindeki _Tempo_ knob öğesini kullanın (0,1’lik artışlar için shift tuşuna basın)
* Tap Tempo kullanın

{% hint style="info" %}
Tempo, “dakikadaki vuruş sayısı” olarak tanımlanır ve geleneksel varsayılan değer genellikle 120’dir.
{% endhint %}

## Tap Tempo

_TAP_ düğmesine vuruşla aynı zamanda tıklayarak tempoyu otomatik ayarlayın. Ölçünün başlangıcını _RESET_ düğmesiyle ayarlayın.

{% hint style="info" %}
Tap Tempo sistemi, bir süre vurmaya ara verdiğinizi veya birkaç vuruş kaçırdığınızı anlayacak kadar akıllıdır. Double time vurmaya başlarsanız tempoyu iki katına çıkarmak istediğinizi anlar; half time vurduğunuzda da aynı şekilde çalışır.

Aynı anda iki kişinin tempo vurduğunu da anlayabilir (örneğin biri klavyeden, diğeri APC40 üzerinden). Liberation, çift vuruşların ortalamasını alır.
{% endhint %}

#### Klavye komutları:

T - tap tempo\
R - ölçüyü sıfırla\
Y - tempoyu dakikadaki en yakın tam vuruş değerine yuvarla.

{% hint style="info" %}
Günümüzde çoğu müzik dijital olarak üretildiği için tempo büyük olasılıkla yuvarlanmış bir tam sayıdır. Bu yüzden vurduğunuz tempo yakın görünüyorsa Y tuşunu kullanın veya APC40 tempo knob öğesini bir “tık” hareket ettirerek tam sayıya yuvarlayın.
{% endhint %}

#### APC40 kontrolleri:

APC40 üzerinde özel bir _TAP TEMPO_ düğmesi bulunur. İsterseniz bağlı bir footswitch kullanarak ayağınızla da tempo vurabilirsiniz!

Ayarlamak için _TEMPO_ knob öğesini kullanın. Hassas ayar için _TEMPO_ knob öğesini kullanırken _SHIFT_ düğmesine basın.

**Ölçüyü sıfırlamak** için _METRONOME_ düğmesini kullanın. (_METRONOME_ düğmesinin vuruşla aynı zamanda yandığını da unutmayın.)

**Tempoyu** yukarı veya aşağı doğru tam bir BPM değerine **yuvarlamak** için _TEMPO_ knob öğesini sağa veya sola bir “tık” çevirin.

Ayrıca bkz. [APC40 referansı](reference/apc40-reference.md)

### Tempoyu kaydırma

Gerçek tempoya yeterince yakın olduğunuzdan eminseniz ancak zamanla senkron dışına kaydığınızı fark ediyorsanız düzeltmek için _NUDGE_ düğmelerini kullanın.

Liberation temposu müziğin önüne geçiyorsa yeniden hizalanana kadar geçici olarak yavaşlatmak için _NUDGE -_ düğmesini basılı tutun.

Liberation temposu müziğin gerisinde kalıyorsa yeniden hizalanana kadar geçici olarak hızlandırmak için _NUDGE +_ düğmesini basılı tutun.

{% hint style="info" %}
Ekrandaki NUDGE düğmelerini veya APC40 üzerindeki özel düğmeleri kullanabilirsiniz.
{% endhint %}

### Half time / double time

Tempoyu kalıcı olarak yarıya indirmek veya iki katına çıkarmak için _÷2_ ve _x2_ düğmelerini kullanın. Tempo çarpanından farklı olarak bu, mevcut tempoda kalıcı bir değişiklik yapar.

## Tempo Multiplier

_Tempo Multiplier_ sistemi, tempoyu geçici olarak ayarlayıp sonra önceki değerine döndürmenizi sağlar.

_Tempo Multiplier_ özelliğini açıp kapatmak için _TEMPO MULTIPLIER_ düğmesine veya APC40 üzerindeki _BANK_ düğmesine basın. Ekrandaki slider ile ya da APC40 A-B slider kullanarak ayarlayın. Alternatif olarak _25%, 50%, 100% 200%_ preset düğmelerini kullanın.

## Harici tempo kaynakları

### MIDI Clock

Harici bir MIDI clock sinyaliyle senkronize etmek için _MIDI CLOCK_ radio button öğesini seçin ve açılır menüden MIDI cihazını seçin. Açılır menülerin yanındaki renkli durum ışığına dikkat edin:

* Yeşil - MIDI clock sinyali alınıyor
* Turuncu - MIDI cihazına bağlanabiliyor, ancak şu anda clock sinyali yok
* Kırmızı - MIDI cihazına bağlanamıyor

{% hint style="info" %}
MIDI Clock bir dizi frame yayınlar (çeyrek nota başına 24 adet), ancak mesajların içinde konum verisi yoktur. Bu, ritimde kalmaya yardımcı olduğu anlamına gelir; yine de ölçüyü sıfırlamanız gerekebilir.

Liberation MIDI Clock tempo kaynağı ayrıca **MIDI Machine Control (MMC)** mesajlarına da yanıt verir. Clock kaynağınız bunları iletiyorsa ölçüyü manuel olarak sıfırlamanız gerekmez.
{% endhint %}



### Timeline

Her timeline kendi temposuna sahiptir; bu sabit bir değer veya _Tempo Map_ olabilir. _Tempo Map_, timeline içindeki belirli zamanlarda tempoyu ayarlamanızı sağlar.

Tempo kaynağı olarak _TIMELINE_ seçildiğinde timeline temposu kullanılır.

{% hint style="info" %}
Bir timeline öğesini tempo kaynaklarının _herhangi biriyle_ birlikte çalıştırabilirsiniz! Yani click track ile çalmayan canlı bir grubunuz varsa timeline öğesini manuel olarak başlatıp _LIVE_ tempo kaynağını kullanarak senkronize tutabilirsiniz. Ya da bir MIDI clock sinyaliniz varsa onu kullanabilirsiniz!
{% endhint %}
