---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas genel bakışı

Liberation Canvas sistemi oldukça basittir, ancak ilk başta kafa karıştırabilir. Başlamak için kavramsal bir genel bakış aşağıda.

{% hint style="info" %}
**Bir dakika, canvas sistemine ihtiyacım var mı?**

Belki yoktur! Tek bir grafiği tek bir lazere yansıtıyorsanız, bunu bir beam zone ile kolayca yapabilirsiniz. Ancak varsayılan olarak beam zone içeriği yatay çevrilmiş gelir, bu yüzden Clip için X flip uygulamanız gerekir.

Ama grafik içeriğini birden fazla lazere yaymak ya da mimari yüzeylere eşlemek için farklı bölümlere ayırmak istiyorsanız, canvas sistemi tam bunun için var.
{% endhint %}

### Canvas

Öncelikle canvas vardır. _CANVAS_ view içinde gördüğünüz alan budur; büyük bir tuvali temsil eder ve bu alanın istediğiniz yerine içerik çizebilirsiniz.

### Canvas hedef alanları

Bunlar Canvas view içinde mavi çerçeveli dikdörtgenler olarak gösterilir ve içerik gönderebileceğiniz alanlardır. Bir Clip içeriğini bir canvas hedef alanına gönderirsiniz; bu, bir Clip öğesini beam zone göndermeye benzer. Clip Deck içinde, beam zone düğmelerinin sağ tarafında canvas hedef alanı düğmelerini görürsünüz.

{% hint style="info" %}
Clip Deck içinde canvas düğmelerini göremiyorsanız, beam zone düğmelerini `Shift + Left / Right Arrow` ile kaydırmayı deneyin. Her canvas hedef alanı için _CANVAS 1, CANVAS 2_ vb. etiketli bir düğme görmelisiniz.
{% endhint %}

### Canvas zones

Canvas zones, canvas içindeki ve bir lazere göndermeyi seçtiğiniz alanlardır. Canvas view içinde pembe çerçeveli dikdörtgenler olarak gösterilirler. Her zone üzerinde sağ tıklayıp atanmasını istediğiniz lazerleri seçebilirsiniz. Şimdi o lazer için _OUTPUT_ view öğesine geçerseniz yeni bir zone oluştuğunu görürsünüz.

{% hint style="danger" %}
UYARI - lazer armed durumdaysa, varsayılan bir canvas zone içinde aniden içerik yansıtmaya başlayabilirsiniz. Canvas zones atamadan önce lazeri disarm etmek en güvenlisidir.
{% endhint %}

{% hint style="info" %}
Bir canvas zone öğesini bir lazere _OUTPUT_ view içindeki _add canvas zone_ düğmesine tıklayarak da atayabilirsiniz. Bkz. [Zones](../output-view/zones.md "mention").
{% endhint %}

### Kılavuz görseller

Canvas içine bir kılavuz görsel ekleyebilir ve bunu grafikleriniz için şablon olarak kullanabilirsiniz. İçeriğinizi üzerinde daha kolay görebilmek için kılavuz görselin renk tonunu ayarlamanız (sağ tık menüsü) ve görseli koyulaştırmanız önerilir.

{% hint style="info" %}
Mimari mapping için, binadaki tüm yüzeyleri düz ve bozulmamış bir görüntü olarak temsil eden “açılmış” bir bina görseli üretmenin faydalı olduğunu gördüm. Farklı bölümlere yönelik perspektif düzeltmesi, _OUTPUT_ view içindeki canvas zone kullanılarak yapılabilir.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Gateshead, Birleşik Krallık’taki Saltwell Hall için “düzleştirilmiş” bir kılavuz görsel</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Liberation uygulamasının çok erken bir sürümünde canvas zones (c2017!) Pembe dikdörtgenlerin canvas içinden hangi bölümün gösterileceğini seçtiğine, alttaki Output view öğelerinin ise bu zone öğelerinin her lazerin hangi bölümüne gideceğini gösterdiğine dikkat edin.</p></figcaption></figure>

### 3D visualiser içinde Canvas

Karmaşık, çok lazerli projeksiyon sisteminizi 3D visualiser içinde yeniden oluşturmak muhtemelen epey zahmetli olurdu. Bunun yerine canvas öğesini 3D alan içine yerleştirme seçeneğiniz vardır. _3D visualiser settings_ panelinde _Show canvas_ onay kutusunu etkinleştirin. (Canvas içindeki kılavuz görseller de visualiser içinde görünür.)

{% hint style="info" %}
Visualiser, canvas projeksiyonlarını yine lazerlerden çıkan atmosferik efektler olarak göstermeye devam eder. İsterseniz bunları görünümün dışına taşıyabilir ya da biraz uğraşarak canvas ile hizalayabilirsiniz.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>3D visualiser içinde lazerden gelen ışınları canvas görseliyle hizaladığınızda sonuç son derece tatmin edici olabilir!</p></figcaption></figure>
