---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Scanner 規格與 Liberation

### Scanner 規格的實際情況其實有點混亂

點速率和 scanner 規格有時會令人有點困惑。你經常會見到 30kpps @ 8º 或 50kpps @ 4º 這類規格，但這些數字實際代表甚麼，未必一眼就看得出。

{% hint style="info" %}
免責聲明 - 我不是 scanner 硬件專家，但我有多年實戰經驗，透過軟件和 point stream 生成，而不是硬件調校，令不同質素的 scanner 都能有不錯的顯示效果。以下內容是基於這些經驗。
{% endhint %}

#### **這些數字從何而來**

「30K」和「50K」這類說法，是基於在特定條件下，以相應點速率使用 ILDA test pattern 評估 scanner 表現的簡寫。

當一個 scanner 標示為類似：_30Kpps @ 8°_，真正意思是：

> 「在正確調校下，這個 scanner 可以在 8° 掃描角度，以每秒 30,000 點重現 ILDA test pattern。」

這不是一個全面或完全標準化的真實世界性能量度。事實上，它最初根本不是設計成 benchmark，而是用於一個**調校程序**。你以固定點速率（例如每秒 30,000 點）播放一個已知 pattern，然後調整 damping 和 gain，直到顯示看起來正確。

不過，它仍然是目前最廣泛使用的參考；至少對於信譽良好的製造商來說，它可以讓你大概判斷 scanner 的質素。但如果是_信譽較差_的製造商，就另作別論了……

#### 如果你想按標稱規格測試 scanner

{% hint style="danger" %}
**這是進階技巧；如果不小心，可能會損壞你的 scanner。除非你清楚自己在做甚麼，否則不建議使用。**
{% endhint %}

你需要找一個可以輸出 [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) 的軟件——我記得 LaserShowGen 可能做到——然後把輸出大小調整至指定掃描角度（例如 8°）。如何分析輸出，請參考 ILDA 文件的建議。

#### 為甚麼它未必是好 benchmark

首先，即使你的 scanner 本身很好，如果它們的調校不是針對這個 test pattern 優化，顯示出來也可能不正確。

它可以作為判斷 scanner「好」與「差」的一般參考，但製造商有時會對這些規格採取相當寬鬆的詮釋。

#### 那我應該怎樣選擇好的 scanner？

我認為最重要是確保它們由信譽良好的製造商生產。高階昂貴的 scanner 製造商，例如 Cambridge Technology (CT)、Eye Magic (EMS) 和 ScannerMAX（Pangolin 旗下子公司），通常都很可靠，基本上不會出錯。但當一對 scanner 要價約 $1000，對很多剛起步的人來說，這甚至比自己的 laser 還要貴！

所以我大多數時間都使用中國製造商的產品。Dragon Tiger (DT) scanner 價錢合理，表現亦不錯；我認為 LightSpace 也是使用它們。很多其他製造商（包括部分型號的 OPT 和 Able）亦使用基於 DT 的系統。

Phenix Technology (PT) 一般屬於較低階，但坦白說，對大多數用途來說應該都可以。

**如果你的 scanner 是沒有品牌的，那就大概是你需要擔心質素的時候！**

#### Liberation 如何幫助

首先，對大多數用途來說，你不需要非常昂貴的 scanner！價錢較相宜的 30kpps DT，甚至 PT，都已經足夠。預設 scanner 設定是刻意保守的，而且大部分情況下_你不應需要調整它們_（_Scanner sync_ 除外）。

即使你有更好的 scanner，也沒有必要把它們推到比實際需要更高的負載。這會大幅延長它們的壽命。

#### 甚麼是「point stream」？

你可能以前聽過這個詞——它就是我們控制 scanner 路徑的方式。

Point stream 是一串 X/Y 位置清單，每個位置都帶有顏色。要畫一條白線，你會沿着該線送出一連串點，全部設定為白色。Scanner 之後會以固定速率——每秒點數（PPS）——由一點移到下一點，光束就會描繪出該形狀。

#### 傳統 laser 軟件如何運作

傳統 laser 軟件會為每個 cue 儲存一個 point stream。對於動畫 cue，這通常代表每一格 frame 都有獨立的 point stream。重點是所有內容都是完全預先決定的。因此，提高點速率會令 scanner 更快地穿過同一批預先定義的資料。

{% hint style="info" %}
對於較舊的軟件，這種做法是必要的——當時電腦速度不足以即時生成 point stream。這就是為甚麼通常會有一個獨立的 cue editor，用來預先生成每格動畫的資料。

這也解釋了為甚麼內容可以佔用數 GB 空間。你實際上是在以相當高的 sample rate 儲存大量未壓縮的波形。
{% endhint %}

#### 為甚麼在 Liberation 中「point rate」的意義較低

Liberation 會即時生成 point stream，這為我們帶來很大的彈性。留意 Laser Settings panel 內的 "Scanner speed" 設定。它讓我們加快或減慢 scanner，但重要的是，它**不會**改變底層的點速率（PPS）。

#### 等等，甚麼？怎樣做到？

我知道，初聽起來有點奇怪。

因為 Liberation 會即時生成 point stream，所以它可以調整該 point stream。點與點之間分佈得越疏，scanner 移動得越快。點與點之間越接近，scanner 移動得越慢。

{% hint style="info" %}
在近期版本的 Liberation 中，實際的 _point rate_（位於 advanced settings）完全不會影響 scanner speed。Renderer 會調整點的分佈以配合所選點速率，同時保持 scanner 的運動不變。

這確實會影響 point path 的「解像度」，但主要只會在 graphics 上造成差異（亦有助更精細地調整 _scanner sync_ 設定）。
{% endhint %}

#### 很好！那這一切實際代表甚麼？

好問題。以下是我的建議：

* 避免使用沒有品牌的 scanner。如果可以買到更快的 scanner，就選更快的——最低 30KPPS。
* 大多數情況下，DT30 scanner 已經足夠；在較便宜的 laser 中，PT30 scanner 應該也可以。
* 如果你做 graphics，大多數情況下，增加 laser 數量會比使用更快的 scanner 更有幫助。
* 當你使用較高階的 setup 時，任何成熟的高階品牌都會很好。
* 如果你只能買到最便宜的無品牌 scanner，Liberation 的預設設定相當保守，做基本 beam work 應該也會有不錯結果。如果它表現吃力，請降低 **Speed** 設定（但不要改變 point rate！）。

#### 那 ILDA Test Pattern 呢？

……它作為校準和參考工具仍然非常有用，但它從來不是設計成全面 benchmark，而且可能被製造商誤用或以寬鬆方式詮釋。
