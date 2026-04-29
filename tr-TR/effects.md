---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Efektler

Liberation içindeki efekt sistemi, Clip çıkışını gerçek zamanlı değiştirmek için eğlenceli ve çok yönlü bir yöntemdir. Efektler tamamen esnektir; her şeyi açıp kapatmak, döndürmek, renkleri değiştirmek, hatta rastgele hareket ettirmek için kullanılabilir.

Clip Editor içinde yapabildiğiniz her şey efekt olarak kullanılabilir. Hatta efektler, Clips ile tamamen aynı node editor üzerinden düzenlenir. Bkz. [Efektleri düzenleme](effects.md#editing-effects). Yaratıcı olasılıklar neredeyse sınırsızdır.

Varsayılan efekt düğmeleri 1-8, zone düğmelerinin altındadır; 9-24 arasındaki efektler ise alttaki küçük düğmelerdir.

#### Efekt uygulama

Bir efekti açıp kapatmak için efekt düğmesine basın. Daha iyisi, APC40 slider 1-8 ile efektleri yumuşak şekilde açıp kapatabilirsiniz. APC40 olmadan bir efekti yumuşak şekilde açmak için düğmeye tıklayıp yukarı-aşağı sürükleyin. Alternatif olarak efekt düğmesine sağ tıklayın ve seviye slider’ını ayarlayın.

{% hint style="warning" %}
Efekt düğmesine basmak o efekti hemen etkinleştirir. Ancak seviye sıfırsa hiçbir şey olmaz! Seviyeyi değiştirmek için düğmeye tıklayıp sürükleyin, sağ tıklayıp _level_ slider’ını kullanın veya APC40 fader’larını kullanın.
{% endhint %}

#### Efektler ve Clip için zone gecikmesi

Efektler, o anda çalışan her Clip için zone gecikmesi ayarını devralır. Yani Clip içinde soldan sağa ilerleyen bir gecikme varsa ve yanıp sönme efektini eklerseniz, yanıp sönme de soldan sağa gecikmeli olur.

{% hint style="info" %}
Clip içindeki zone gecikmesinin efektler tarafından nasıl devralındığını anlatmak gerçekten çok zordur, ama denediğinizde hemen anlaşılır!

Bence bu, Liberation içinde yerleşik olan en eğlenceli ve yaratıcı araçlardan biri. Deneyin, ne demek istediğimi göreceksiniz!
{% endhint %}

#### Efekt parametreleri

Efektinize bir _Parameter node_ ile parametre ekleyin. Parameter sistemi, efektinizin içindeki birden fazla ayarı dışarıdan ayarlamanın bir yoludur. Daha fazla bilgi için bkz. [Parametre kontrolü](clip-editor/oscillators/parameter-control.md).

Her efektin _parameter_ değerini ayarlamak için rotary controller 1-8’i kullanın. Alternatif olarak efekt düğmesine sağ tıklayıp parameter slider’larını ayarlayın. Parameter değişikliği, efektin nasıl kurulduğuna bağlı olarak farklı şeyler yapar. Varsayılan efektlerin neler yaptığını ve parametrelerinin neyi değiştirdiğini aşağıdaki listede görebilirsiniz.

{% hint style="info" %}
Rotary controller 1-8, APC40 Mk2 üzerinde üst sırada; Mk1 üzerinde ise sağ üsttedir. Ayrıca bkz. [APC40 referansı](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Efekt düğmelerinde gördüğünüz küçük sayılar, efektin _level_ ve _parameter_ değerlerini gösterir. _level_, APC40 üzerindeki fader ile kontrol edilir; isterseniz düğmeye tıklayıp sürükleyebilirsiniz. Parameter, APC40 üzerindeki rotary controller’lar ile ayarlanır; isterseniz sağ tıklayıp fareyle de ayarlayabilirsiniz.
{% endhint %}

#### Varsayılan efektler

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Clip çıkışına kaotik bir hareket uygular. Parameter, kaos miktarını/hızını ayarlar.
2. **Sine wave** :\
   Tüm içeriği hareket eden bir sinüs dalgası boyunca büker. Parameter, dalga boyunu ayarlar.
3. **Rotation** :\
   Her şeyi döndürür. Parameter, dönüş hızını ayarlar.
4. **Horizontal flip** :\
   Her şeyi yatay olarak sıkıştırır ve esnetir. Parameter, hızı ayarlar.
5. **Scale** :\
   Her şeyi sürekli olarak tam boyuttan sıfıra ölçekler. Parameter, hızı ayarlar.
6. **Hue** :\
   Her şeyin tonunu değiştirir, ancak doygunluğu değiştirmez (yani beyaz olan her şey beyaz kalır). Parameter, tonu ayarlar.
7. **Saturation and hue** :\
   Her şeyin tonunu değiştirir ve rengi tamamen doygun hale getirir (yani beyaz olan her şey seçilen renge dönüşür). Parameter, tonu ayarlar.
8. **Flash** :\
   Her şeyin parlaklığını sürekli olarak tam değerden sıfıra yanıp söndürür. Parameter, yanıp sönme hızını ayarlar.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Alt sırada, önceden ayarlanmış ton ve doygunluk değerlerini uygulayan 16 renk efekti daha vardır.

Bunların varsayılan efektler olduğunu unutmayın; ancak neredeyse istediğiniz her şeyi yapacak şekilde düzenlenebilirler!

### Gruplara uygula

Efektin hangi grupları etkileyeceğini seçebilirsiniz. Sağ tıklayın ve _Apply to groups_ etiketli grup onay kutularını açıp kapatın.

Bu kurulumu genellikle canvas grafikleri ve lazer ışınlarıyla ayrı ayrı çalışırken kullanıyorum. Tüm canvas Clips öğelerini group 5’e atıyorum ve sonra bu grafik Clips öğelerini etkilemesini istemediğim efektlerde bu grubu hariç tutuyorum.

Aynı anda iki lazer grubuna canlı olarak iki farklı renk değişimi uygulamak için de kullanabilirsiniz. İki renk değiştirme efekti oluşturun ve her birinin hangi Clip gruplarına uygulanacağını seçin.

### MX group

_Mutually Exclusive_ ifadesinin kısaltmasıdır. Efektleri, aynı grupta aynı anda yalnızca bir efekt etkin olabilecek şekilde gruplamanın bir yoludur. Varsayılan renk değiştirme efektlerinden yalnızca birinin aynı anda etkin olabildiğine dikkat edin. Bunun nedeni hepsinin MX Group 1 içinde olmasıdır.

_MX Group_ ayarı 0 ise bu işlev devre dışı bırakılır.

### Efektleri düzenleme

Herhangi bir efekte sağ tıklayın ve efekt düzenleyiciyi açmak için _EDIT EFFECT_ düğmesine tıklayın. Bu düzenleyicinin Clip Editor ile aynı olduğuna dikkat edin!

Efektinizi, herhangi bir Clip düzenler gibi düzenleyin. Bkz. [Clip Editor](clip-editor/).

En az bir Creator node olması gerekir; bu herhangi bir şey olabilir (çizgi, daire, şekil, hatta metin!), ancak efekt düğmesi önizlemesinde en mantıklı görünen şeyi seçmeniz muhtemelen daha iyi olur.

Efektler uygulandığında, efekt içindeki tüm Creator nodes, o anda çalışan Clips öğelerinin çıkışıyla değiştirilir.

{% hint style="warning" %}
Son derece sıkıcı teknik nedenlerden dolayı, bir efektin içindeyken "trails" nodes etkin değildir. Aynı durum, pattern nodes içindeki "delay" ayarı için de geçerlidir (aynı sistemi kullanırlar). Bu durum gelecek sürümlerde düzeltilecektir.
{% endhint %}
