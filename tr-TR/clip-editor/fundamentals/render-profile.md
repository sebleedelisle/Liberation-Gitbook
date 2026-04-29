---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profili

Her _Creator_ node içinde bir _Render Profile_ ayarı bulunur. Bu ayar, şekillerin lazerlerle nasıl çizileceğini (veya _render_ edileceğini) belirler.

**Çoğu kullanım için&#x20;**_**DEFAULT**_**&#x20;ayarı fazlasıyla yeterlidir**. Ancak grafiklerle veya karmaşık içeriklerle çalışıyorsanız, her şeklin nasıl render edileceği üzerinde daha fazla kontrol isteyebilirsiniz.

{% hint style="info" %}
Çoğu lazer yazılımından farklı olarak Liberation, lazer controller cihazlarına gönderilmeden hemen önce nokta akışını gerçek zamanlı olarak oluşturur. Bu, disk alanından ciddi ölçüde tasarruf sağlar; Clips, önceden render edilmiş MB boyutundaki nokta akışları yerine yalnızca birkaç kB yer kaplar.

Bu ayrıca, aynı içeriği Clip üzerinde değişiklik yapmadan her lazer için farklı scanner türlerine göre ayarlayabileceğiniz anlamına gelir.

Daha fazla ayrıntı için bkz. [Liberation lazer içeriğini nasıl oluşturur](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Üç hazır _Render Profile_ vardır: _DEFAULT_, _FAST_ ve _DETAIL._

_**DEFAULT**_ - çoğu şey için en iyi seçenek olan, iyi bir genel profildir

_**FAST** -_ Clip içinde çok fazla içerik varsa ve bunların bir kısmı gerçekten basit noktalar ve düz çizgilerden oluşuyorsa, bu seçeneği seçtiğinizde titreşim daha az olabilir.

_**DETAIL**_ - keskin köşeler gerektiren bir şey çiziyorsanız bu seçeneği kullanın. Ancak scanner cihazlarınızın daha yavaş hareket edeceğini ve bunun Output tarafında titreşime yol açabileceğini unutmayın.

{% hint style="info" %}
Clip Editor içinde Creators öğelerini farklı Render Profile seçeneklerine atayabilirsiniz, ancak her lazer bu profilleri kendi scanner ayarlarına göre işler. Bkz. [Scanner ön ayarları](../../advanced/scanner-presets.md)
{% endhint %}
