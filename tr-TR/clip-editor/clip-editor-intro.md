---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Clip Editor ile Tanışma

Clip Editor, lazer içeriği oluşturmak için çok yönlü bir araçtır ve Liberation’ın merkezinde yer alır. Basit şeyler yapmak kolaydır; aynı zamanda oldukça gelişmiş ve karmaşık efektler oluşturabilecek kadar esnektir.

{% hint style="info" %}
Node tabanlı editor, Liberation’ın geliştirilen ilk parçasıydı! 2018’de Birleşik Krallık’taki bir lazer buluşmasında Rob Stanley ile “nesne yönelimli” bir lazer içerik tasarımcısının nasıl görüneceği üzerine yaptığımız bir sohbetten doğdu.

Basit görünse de, aslında geliştirmesi oldukça karmaşık bir sistem. Yine de 2019’un başında fikri kanıtlayan çalışan bir demom vardı ve bu yolculuk böyle başladı!
{% endhint %}

Bu, TouchDesigner, MaxMSP veya VVVV gibi ürünleri kullandıysanız size tanıdık gelecek node tabanlı bir görsel editördür (veya [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)). Ancak Clip Editor biraz farklı ve özellikle vektör grafikler için tasarlandığından bir ölçüde daha basittir.

Clip Editor açmak için Clip düğmesine sağ tıklayıp _EDIT CLIP_ seçin. Ya da boş bir Clip düğmesine sağ tıklayıp _CREATE AND EDIT CLIP_ seçin.

### Genel bakış

Clip Editor içinde şunları görürsünüz:

* Üst kısımda **Creator** ve **Operator node düğmeleri**
* Sol tarafta **Oscillator node düğmeleri**
* Sağdaki panelde içeriğin bir önizlemesi; bir node üzerine tıklarsanız, o node üzerindeki içeriği gösteren ikinci bir önizleme de görünür.
* Düzenlediğiniz Clip için tüm node öğeleri ve bağlantılar (yeni bir Clip ise burası boş olur)
* Çeşitli seçeneklerin bulunduğu Clip Editor paneli

Düzenleme yaparken, Clip içeriğinin arka plandaki 3D görselleştiricide nasıl göründüğünü de görürsünüz.

{% hint style="info" %}
3D görselleştiricide herhangi bir çıkış görmüyorsanız, istediğiniz zone öğelerini açmak için zone düğmelerini kullanmanız gerekebilir. Ayrıca _Preview to lasers_ seçeneğinin etkin olduğundan emin olun; aşağıdaki [Clip Editor paneli](clip-editor-intro.md#clip-editor-panel) bölümüne bakın.
{% endhint %}

### Clip oluşturma

Genellikle bir veya daha fazla [Creator node öğesi](creator-nodes.md) ile başlar ve içeriği işleyen [Operator node öğelerini](operator-nodes/) soldan sağa bağlarsınız. Creator ve/veya Operator öğelerini birbirine yaklaştırdığınızda otomatik olarak bağlandıklarını fark edersiniz. Tekrar ayırmak için birbirinden uzağa sürükleyebilirsiniz.

### Clip’e node ekleme

Üstteki veya soldaki node düğmelerinden birine tıklayıp Clip Editor içindeki boş bir alana sürükleyin.

### Bir node için ayarları değiştirme

O node için özellikler panelini açmak üzere dişli simgesi düğmesine (node öğesinin sağ üstünde) tıklayın.

### Bir node öğesini etkinleştirme ve devre dışı bırakma

Node öğesini etkinleştirmek veya devre dışı bırakmak için güç simgesi düğmesine (node öğesinin sol üstünde) tıklayın. Node öğesi, o anda etkin olmadığını göstermek için soluk görünür. Bir Operator devre dışı olsa bile içeriğin içinden geçmeye devam ettiğini, ancak node öğesinin içeriği etkilemediğini unutmayın.

### Node öğelerini birbirine bağlama

İçerik bir Creator node ile oluşturulur ve node öğeleri boyunca soldan sağa aktarılır; her Operator içeriği bir şekilde etkiler ve bir sonraki Operator öğesine iletir. Yolun sonunda ne kaldıysa, Clip içeriği odur. Creator ve Operator öğeleri birbirine yaklaştırıldığında otomatik olarak bağlanır. Ayırmak için tekrar birbirinden uzağa sürükleyin.

{% hint style="info" %}
Birden fazla node öğesini bir sonraki node girişine bağlayabilirsiniz. Bu, birden fazla içerik parçasını birleştirmek için kullanışlıdır.
{% endhint %}

### Node özellikleri ve soketler

Her node öğesinin alt kısmında bir dizi soket bulunur. Her soket, node içindeki parlaklık, konum, ölçek, döndürme vb. bir özelliği temsil eder.

[Oscillator node öğeleri](oscillators/) bu soketlere alttan bağlanabilir ve bu ayarları canlandırmak için kullanılabilir. Oscillator node öğelerinin üst kısmında bir çıkış bulunur; bağlantıyı çıkarmak için tıklayıp sürükleyin ve diğer node öğelerinden birinin özellik soketine bırakın.

### Oscillator node öğeleri

Oscillator node öğeleri, özellikleri zaman içinde değiştirmek için kullanılır. Genellikle testere dişi veya sinüs dalgası gibi dalga biçimlerini temsil ederler; ancak bazı Oscillator node öğeleri kaynak olarak harici girişleri (örneğin mikrofon giriş seviyesini) kullanır.

{% hint style="info" %}
Daha önce analog synth kullandıysanız, dalga biçimleri oluşturmak veya sesi zaman içinde ayarlamak için yaygın olarak kullanılan osilatör kavramına aşinasınızdır. Liberation içindeki Oscillator öğeleri de benzer bir iş yapar.

**Eğlenceli bilgi:** _Liberation_ adı, 1980’de piyasaya çıkan ve Herbie Hancock, Jean-Michel Jarre hatta James Brown tarafından ünlü hale getirilen “keytar” synthesizer Moog Liberation’dan ilham aldı!
{% endhint %}

Oscillator öğelerinde, ayarlanacak özelliğin minimum ve maksimum değerini kontrol eden _range_ ayarları her zaman bulunur. _Wave Oscillators_ öğelerinde ise Oscillator değerinin ne kadar hızlı değişeceğini belirleyen bir _duration_ ayarı her zaman bulunur. Daha fazla bilgi için [Wave Oscillator node öğeleri](oscillators/wave-oscillators.md) bölümüne bakın.

### Clip Editor paneli

* Timer - panelin üst kısmında, Clip ilerledikçe geçerli zamanı görürsünüz
* _RETRIGGER_ - Clip’i baştan yeniden başlatır; Clip döngü yapmıyorsa özellikle kullanışlıdır
* _Preview to lasers_ - bu işaretliyken, bu Clip’i düzenledikçe 3D görselleştiricinin güncellendiğini görürsünüz. Kapatırsanız, editor dışında çalışan Clip öğelerini görürsünüz. Bu ayar Clip başına değil, global bir ayardır.
* _UNDO/REDO_ - Clip Editor içindir. Ayrıca `Cmd / Ctrl + Z` ve `Cmd / Ctrl + Shift + Z` kısayollarına atanmıştır.
* _SAVE CLIP_ - düzenlemelerinizi kaydeder, ancak üzerine yazma konusunda sizi uyarır
* _SAVE AS A COPY_ - Clip içeriğinizi Clip Deck içinde sıradaki kullanılabilir yuvaya kaydeder. Bu, Clip için yeni konum olur ve sonraki tüm kaydetmeler bu yeni yerde yapılır.
* _EXIT EDITOR_ - Clip Editor kapatır. Kaydedilmemiş değişiklikleriniz varsa bir onay paneli gösterilir.
