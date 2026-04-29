---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ 波形振盪器

## 本頁內容：

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [鋸齒波](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [三角波](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [正弦波](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [方波](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [雜訊](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [自訂振盪器](wave-oscillators.md#custom-oscillator-1)

## 波形振盪器設定

所有波形振盪器都有以下設定：

* **range min / range max** - 決定振盪器所控制屬性的數值範圍。當波形位於底部時，屬性會設為 _range min_；當波形位於頂部時，屬性會設為 _range max_。

{% hint style="info" %}
例如，如果你想讓一個點在 -100 到 100 之間左右移動，可以將振盪器連接到 _x property socket_，將 _min range_ 設為 -100，並將 _max range_ 設為 100。
{% endhint %}

* **duration** - 完成一個完整週期（或 _loop_）所需的時間長度。這是相對於 tempo 的小節長度。因此 ¼ 代表一拍，1 代表一個完整小節，依此類推。
* **duration multiplier** - 以指定倍率縮放基礎 duration。例如，如果 duration 設為四分音符，multiplier 設為 3，振盪器就會持續三個四分音符（附點二分音符）。也支援小數倍率——拖曳滑桿時按住 _SHIFT_ 可設定非整數值，這對相位偏移效果或製造細微的時間位移很有用。
* **offset** - 波形起始位置的偏移量，以 duration 的百分比表示。如果你想讓波形從四分之一的位置開始，請將此值設為 25%。
* **repeat count** - loop 在停止前執行的次數。預設為 _FOREVER_，但如果你不希望振盪器無限執行，可以更改此值。停止後，屬性會設為波形結束時的值。
* **delay count** - 振盪器開始執行前的延遲拍數。在開始執行前，屬性會設為波形起始時的值。

{% hint style="info" %}
謹慎使用 _repeat count_ 和 _delay count_，可以建立非常複雜的動畫，有點像是它自己的時間軸！
{% endhint %}

## 通用設定

* **steps** - 將動作分割成多個離散步階。當你希望屬性「跳」到某個值，而不是平滑移動時很適合使用。

{% hint style="info" %}
請注意，steps 是依時間分割，而不是依數值分割。因此，如果一個 duration 為 1 小節的波形分成 4 個 steps，屬性就會每一拍瞬間改變一次。
{% endhint %}

* **clamp min / clamp max -** 將波形尺度增加到超出其最小值或最大值，然後將結果限制在範圍內。

{% hint style="info" %}
_clamp_ 的概念有點難解釋，但你可以想像波形超出圖表的頂部或底部，然後被夾回邊界。我建議你實際試試看！如果你想讓鋸齒波較晚開始或較早結束，這些設定會非常有用。
{% endhint %}

* **ease function** - Sawtooth 和 Triangle 波形也有 ease function，可細微改變動畫曲線，讓動畫更有表現力！
  * **LINEAR** - 預設值，沒有 easing，只是在最小值與最大值之間以線性方式移動。
  * **EASE OUT** - 一開始快速，接近結尾時放慢。很適合模擬物理效果，例如減速到停止。
  * **EASE IN** - 一開始緩慢，然後逐漸加速。適合模擬動量累積。
  * **EASE IN/OUT** - 兩者的結合，動作非常自然。

{% hint style="warning" %}
**Easing -** 除非你特別想要機械感的效果，否則我會建議盡量避免使用預設的線性動畫。Easing 可以讓動畫流暢、自然許多！
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> 鋸齒波

有時也稱為 _ramp waveform_，因為它會向上爬升，然後在週期結尾突然下降。這可能是最常用的波形振盪器，因為它可以為 _hue_ 或 _rotation_ 這類屬性建立循環。

請參考上方章節中的：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

鋸齒波專用設定：

* **cycle range compensation** - 在設定 **steps** 時可用，很適合用於循環數值，例如從 0 到 360 的旋轉。未啟用時，起始值與結束值會相同，這可能會造成在起點卡住（因為 0 和 360 是相同角度）。啟用後，最大範圍會縮小，以修正 step 位置。

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> 三角波

不同於每個週期都跳回起點的 _鋸齒波_，_三角波_ 會先線性向前移動，接著再線性向後移動。

請參考上方章節中的：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> 正弦波

最平滑的波形！像鐘擺一樣，在兩個數值之間柔和地振盪。

請參考上方章節中的：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> 方波

最簡單的波形——它只是在兩個數值之間來回切換！

請參考上方章節中的：

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

方波專用設定：

* **pulse width** - 波形維持在最大值的時間長度，相對於整體 duration。預設為 50%，也就是剛好各半。如果你只想讓它在四分之一的時間內為「on」，請設為 25%。你可以使用 _offset_ 值調整這個 pulse 發生的時間。

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> 雜訊

Liberation 的強項之一，是能產生隨機但可重複的效果。_noise_ 振盪器可用來建立自然、有機的循環隨機動作，細節或抖動程度都可以依需求調整。

請參考上方章節中的：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

雜訊專用設定：

* **noise type** - 用來產生雜訊的演算法。
  * **SIMPLEX** - 預設值，會產生起伏流動、並以 loop 重複的數值。
  * **RANDOM** - 使用較傳統的隨機數演算法，完全雜亂且混沌。

{% hint style="info" %}
**Simplex noise** 由 Ken Perlin 在 2001 年設計，是對他在 1983 年開發的「Perlin noise」演算法的改良；該演算法是他參與電影 _Tron_ 製作時的成果之一（他也因此獲得奧斯卡獎！）

這種所謂的「gradient」noise，源自於他對早期「機械感」電腦生成影像的不滿。在 CGI 領域，它特別適合用來算繪雲、水面，甚至是逼真地形的 height-map。

但在 Liberation 中，它很適合用來產生看似不可預測、卻依然平滑自然的動作。
{% endhint %}

* **seed** - 用來產生雜訊的數值。如果你不喜歡目前 noise wave 的樣子，可以試著更改這個值。

{% hint style="info" %}
有趣的 nerd 小知識！為了取得完美循環的 simplex noise，我會在 2D noise plane 上沿著圓形迭代。而改變 seed 值，會讓這個平面在第 3 個維度中移動！
{% endhint %}

* **simplex detail** - 改變雜訊的細節程度或抖動程度。如果你想讓重複圖樣比較不明顯，可以提高 duration，並增加此值。

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> 自訂振盪器

建立完全自訂的波形。這對建立複雜動畫非常有用。

請參考上方章節中的：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

下方會列出一組位置與數值。duration 會分成 64 個 steps，你可以在其中任一點放置數值。

每個 step 都有以下設定：

* **Step** - duration 內的時間 step。0 位於開頭，64 位於結尾。
* **Level** - 該時間 step 的波形 level。level 範圍介於 0 到 1。
* **Animation type** - 下拉式選單可讓你選擇要如何從上一個 step 移動到這個 level。
  * **None** - 沒有轉場，只是在指定時間直接跳到這個 level。
  * **Linear** - 從上一個 level 到這個 level 的完全線性移動。
  * **Ease in / Ease out / Ease in/out** - 從上一個 level 到這個 level 之間套用 easing。動畫類型的說明請參考上方的 _ease function_。

***
