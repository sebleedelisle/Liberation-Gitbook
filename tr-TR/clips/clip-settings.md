---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip ayarları

### Clip ayarları paneli

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip ayarları paneli</p></figcaption></figure>

Clip çıkış boyutunu _Scale X_ ve _Scale Y_ ile değiştirin. _SHIFT_ tuşuna basmadığınız sürece bu iki değer birlikte kilitli hareket eder.

Clip için yatay ve dikey konumu _Shift X_ ve _Shift Y_ ile değiştirin.

_Zone Delay/Chase_ başlı başına anlatılacak kadar eğlenceli bir özellik. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Parameters panel

Clip Deck’in sağındaki panel, bağlama göre değişen sekiz parametre gösterir. Bir Clip seçiliyken ilk kontroller seçili Clip için _Shift X_, _Shift Y_ ve _Zone Delay_ değerleridir; ardından genel _Spin_ ve _Scale_ kontrolleri gelir.

Aynı parametreler desteklenen MIDI kontrolcülerine de yansıtılır. Seçili bir Clip yoksa Clip’e özel alanlar boş kalır. Bir group düğmesini basılı tutarsanız ilk iki kontrol, o group için fade in ve fade out sürelerine dönüşür.

### Clip kilitleme

Bir Clip kilitliyse taşınamaz veya silinemez. Bir Clip kilitlemek için sağ tıklama menüsündeki _Locked_ onay kutusunu kullanın. Clip ayarları panelinde birkaç ek seçenek bulunur.

* _UNLOCK ALL -_ Clip Deck içindeki tüm Clips kilidini açar.
* _AUTO-LOCK_ - _Auto-Lock_ açıkken, otomatik olarak oynatılan her Clip (timeline veya MIDI kayıt/oynatma sistemiyle) kilitlenir. Logic Pro veya benzeri bir yazılımda bir gösteri programladıysanız ve gösteride kullanılan Clips üzerinde yanlışlıkla düzenleme yapmak istemiyorsanız kullanışlıdır.
* _LOCKED CLIPS ZONES_ - bu açıksa, kilitli hiçbir Clip için zones değiştirilemez.
* _LOCKED CLIPS PARAMS_ - bu açıksa, kilitli hiçbir Clip için parametreler (scale, shift vb.) değiştirilemez.

### Sağ tıklama menüsü

Bir Clip üzerine sağ tıkladığınızda, o Clip için bazı seçenekleri içeren bir menü açılır. Bu menüdeki ilk birkaç öğe hakkında daha fazla bilgi için [Clip Editor’a giriş](../clip-editor/clip-editor-intro.md "mention"), [Clip ayarları](clip-settings.md "mention") ve [Clip grupları](groups.md "mention") bölümlerine bakın.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips varsayılan olarak _retrigger_ şeklinde ayarlanır. Bu, ne zaman basarsanız basın Clip çalışmaya o anda başlar anlamına gelir. Yani geç başlatırsanız, Clip animasyonu da biraz geç kalır ve zamanlamadan çıkar.

{% hint style="info" %}
Retrigger edilmiş bir Clip çalışırken _Tap Tempo_ kullanırsanız, tam vuruşta başlatmamış olsanız bile sistem Clip zamanlamasını düzene sokar.
{% endhint %}

_Retrigger_ etkin değilse, Clip her zaman zamanında olur; sanki Clip clock en başındayken başlatılmış gibidir. Harici bir clock sinyaliyle müzikle kusursuz şekilde senkronize olduğunuz durumlar için uygundur.

{% hint style="info" %}
Clips genellikle sürekli döngüye girecek şekilde tasarlanır, ancak yalnızca bir kez veya birkaç tur çalışacak şekilde de tasarlayabilirsiniz. Bunların _retrigger_ olarak ayarlı kaldığından emin olun; aksi halde yeniden başlamazlar!
{% endhint %}

### Transition in/out time (fade)

Clips, saniye cinsinden bir süreyle fade in ve fade out yapacak şekilde ayarlanabilir. Varsayılan olarak fade süresi, ilgili group ayarlarından devralınır (group düğmesine sağ tıklayarak değiştirilebilir).

Clip için bağlı olduğu group değerinden farklı bir fade süresi istiyorsanız önce _USE GROUP DEFAULT_ düğmesini kapatın, ardından Clip için _In time_ ve _Out time_ kaydırıcılarını ayarlayın.
