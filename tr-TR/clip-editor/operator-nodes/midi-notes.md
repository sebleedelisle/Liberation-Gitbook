---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Gelen MIDI notalarının belirli bir aralık boyunca ışınları veya şekilleri tetiklediği “lazer arpı” tarzı efektler oluşturur. Node, içine gönderdiğiniz içeriği her nota için _kaynak_ olarak kullanır: Bir nokta verirseniz bir nokta sırası elde edersiniz. Daire gibi bir şekil verirseniz bir daire sırası elde edersiniz; daha karmaşık şekiller de aynı şekilde çoğaltılır.

Liberation uygulamasının hangi MIDI arayüzünü dinleyeceğini **Liberation → Settings** (`Cmd / Ctrl + ,`) bölümünden seçebilirsiniz.

* **MIDI channel** – dinlenecek MIDI kanalı (0 = tüm kanallar, 1–16 = belirli kanal)
* **width** – notaların yayıldığı toplam genişlik.
* **MIDI note min / max** – aralıktaki en düşük ve en yüksek MIDI nota değerleri.
* **ignore out of range notes** – ayarlanan aralığın dışındaki notaları filtreler. Devre dışıysa aralık dışındaki notalar en yakın kullanılabilir notaya “sabitlenir” (yüksek notalar aralığın üstünü, düşük notalar aralığın altını tetikler).
* **auto extend range** – aralığın dışında notalar çalınırsa aralığı otomatik olarak genişletir.

{% hint style="info" %}
Hangi nota aralığını aldığınızdan emin değil misiniz? **auto extend range** seçeneğini açın, **MIDI note min** değerini çok yüksek ve **MIDI note max** değerini çok düşük ayarlayın, ardından notalarınızı çalın. Sistem hepsini yakalar ve aralığı sizin için genişletir. Her şeyi yakaladıktan sonra aralığı kilitlemek için **auto extend range** seçeneğini kapatmanız yeterli.
{% endhint %}

* **leave all notes visible** – aralıktaki tüm notalar için, çalınıp çalınmadıklarına bakmadan ışınlar veya şekiller oluşturur; böylece “lazer arpı” efekti verir.
* **hit colour** – bir nota tetiklendiğinde görünen renk.
* **hit colour hold time** – hit renginin solmaya başlamadan önce tam parlaklıkta ne kadar süre kalacağı. Değer saniye cinsindendir (0–1). _100% = 1 saniye._
* **hit colour decay time** – bekleme süresinden sonra hit renginin geri solmasının ne kadar süreceği. Değer saniye cinsindendir (0–1). _100% = 1 saniye._

{% hint style="info" %}
İçeriğiniz zaten saf beyazsa hit rengini beyaz yapmak herhangi bir fark yaratmaz. En iyi sonuç için içeriğinizde doygun bir renk kullanın ve hit rengini beyaz olarak ayarlayın; notalar tetiklendiğinde oldukça hoş bir flaş efekti verir.
{% endhint %}

* **note off fade out time** – nota bırakıldıktan sonra solmasının ne kadar süreceği. Değer saniye cinsindendir (0–1). _100% = 1 saniye._
* **hit scale factor** – nota tetiklendiğinde ne kadar büyütüleceği (örn. 2 = iki kat boyut).
* **hit scale hold time** – notanın tekrar küçülmeden önce büyütülmüş halde ne kadar kalacağı. Değer saniye cinsindendir (0–1). _100% = 1 saniye._
* **hit scale decay time** – notanın özgün boyutuna dönmesinin ne kadar süreceği. Değer saniye cinsindendir (0–1). _100% = 1 saniye._
* **note off shrink time** – nota bırakıldıktan sonra özgün boyutuna küçülmesinin ne kadar süreceği. Değer saniye cinsindendir (0–1). _100% = 1 saniye._ (**leave all notes visible** etkin olduğunda etkisi yoktur.)

{% hint style="info" %}
Ölçekleme: İçeriğiniz tek bir noktaysa ölçeklemenin hiçbir etkisi olmayacağını unutmayın!
{% endhint %}
