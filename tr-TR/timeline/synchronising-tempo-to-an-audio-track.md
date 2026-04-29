---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Tempoyu bir ses parçasıyla senkronize etme

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Tempoyu bir ses parçasıyla senkronize etme" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Liberation’ın zaman çizelgesi sabit veya değişen tempolarla çalışacak şekilde tasarlanmıştır, ancak güvenilir senkronizasyon her zaman tempoyu bulmak ve sesi doğru hizalamakla başlar. Bu bölümde önerilen iş akışı açıklanır.

#### 1. İlk kuvvetli vuruşu hizalayın

Ses parçanızı zaman çizelgesine ekleyin ve bir vuruşa oturduğundan emin olun. Böylece parçanın **ilk müzikal kuvvetli vuruşu** tam olarak bir ölçünün başlangıcıyla hizalanır.

Bu adım çok önemlidir.

Ses doğal olarak kuvvetli vuruşta başlamıyorsa iki seçeneğiniz vardır:

* **Clip gecikmesini ayarlayın**\
  Ses Clip öğesine sağ tıklayın ve ilk kuvvetli vuruş bir vuruş veya ölçü işaretiyle hizalanana kadar Delay değerini ayarlayın.
* **Sesi harici olarak kırpın**\
  Ses dosyasını Audacity gibi harici bir düzenleyicide, dosya tam olarak ilk kuvvetli vuruşta başlayacak şekilde düzenleyin, ardından yeniden içe aktarın.

{% hint style="info" %}
**Önemli:**\
Sesin başlangıcı bir vuruşa veya ölçüye hizalı değilse, tempoyu değiştirdiğinizde müziğin algılanan başlangıç konumu ileri geri kayar. Bu da doğru tempo eşleştirmeyi son derece zorlaştırır.
{% endhint %}

#### 2. Başlangıç temposunu ayarlayın

BPM hakkında kabaca bir fikriniz varsa, bu değeri zaman çizelgesindeki tempo kontrolüne girin ve oynatmayı baştan başlatın.

Parça çalarken vuruş ve ölçü işaretlerini dikkatle izleyin.

* İşaretler müziğin önüne geçiyorsa tempoyu biraz düşürün.
* Geride kalıyorsa tempoyu biraz artırın.
* Oynatmayı durdurun, tempoyu ayarlayın ve tekrar deneyin.

Modern müziklerin çoğunda tempo, tam sayı BPM değerinde sabittir. Doğru değeri bulduğunuzda, tüm parça boyunca kilitli kalmalıdır.

#### 3. Dalga formunu görsel kılavuz olarak kullanın

Ses dalga formu, tempo eşleştirirken kullanışlı bir referanstır.

* Transient’ler ve tepe noktaları dikey ölçü işaretleriyle hizalanmalıdır.
* Birden fazla ölçü boyunca hizalamayı kontrol etmek için yakından yakınlaştırın.

**İpucu:**\
Zaman çizelgesini yakınlaştırmak için fare tekerleğini veya trackpad hareketini kullanın. Sola ve sağa gitmek için yatay kaydırma tekerleğini veya hareketini kullanın. Yakınlaştırılmış çalışmak küçük ayarlamaları çok daha kolay hale getirir.

#### 4. Tam sayı olmayan BPM kullanan parçalar

Parça tam sayı BPM kullanmıyorsa kayma daha kademeli olur.

* Daha fazla yakınlaştırın.
* Daha küçük tempo ayarlamaları yapın.
* Yalnızca ilk birkaç ölçü yerine parçanın daha uzun bölümleri boyunca hizalamayı kontrol edin.

#### 5. Tempo değişiklikleri olan müzikler

Müzik hızlanıyor veya yavaşlıyorsa Tempo Map kullanın:

* Parçayı çalın ve vuruş işaretlerini izleyin.
* Kayma fark edilir hale geldiğinde, o noktaya bir tempo değişikliği ekleyin.
* Yeni bölüm için tempo tekrar kilitlenene kadar tempoyu ayarlayın.

Müzikteki her tempo değişikliği için bu işlemi tekrarlayın.

#### 6. Harici tempo analizi (isteğe bağlı)

Son çare olarak parçayı Logic Pro gibi bir DAW içinde analiz edip otomatik olarak bir tempo haritası oluşturabilirsiniz. Bunun çoğu zaman çok sayıda tempo değişikliği ürettiğini unutmayın; bazen her ölçü için bir değişiklik oluşturur ve bu, çoğu gösteri için gerekenden daha ayrıntılı olabilir.
