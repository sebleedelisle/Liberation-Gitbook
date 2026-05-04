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

## Wave oscillator 設定

所有 Wave oscillator 都有以下設定：

* **range min / range max** - 決定振盪器所控制屬性的數值範圍。當波形在最低點時，屬性會設定為 _range min_；當波形在最高點時，屬性會設定為 _range max_。

{% hint style="info" %}
例如，如果你想讓一個點在 -100 至 100 之間左右移動，可以將振盪器連接到 _x property socket_，將 _min range_ 設為 -100，並將 _max range_ 設為 100。
{% endhint %}

* **duration** - 完成一個完整週期（或 _loop_）所需的時間長度。這個時間相對於 tempo，以小節為單位。因此 ¼ 是一拍，1 是一個完整小節，如此類推。
* **duration multiplier** - 以指定倍數縮放基礎 duration。例如，如果 duration 設為四分音符，而 multiplier 為 3，振盪器便會持續三個四分音符（一個附點二分音符）。亦支援小數倍數——拖動滑桿時按住 _SHIFT_ 可設定非整數值，適合用於相位效果或製造細微的時間偏移。
* **offset** - 波形的起始偏移，以 duration 的百分比表示。如果你想讓波形從四分之一位置開始，便將此值設為 25%。
* **repeat count** - loop 在停止前執行的次數。預設為 _FOREVER_，但如果你不想振盪器無限期運行，可以更改此值。停止後，屬性會設定為波形結尾的值。
* **delay count** - 振盪器開始運行前的延遲拍數。在開始運行之前，屬性會設定為波形起點的值。

{% hint style="info" %}
善用 _repeat count_ 和 _delay count_ 可以建立非常複雜的動畫，有點像自成一條 timeline！
{% endhint %}

## 通用設定

* **steps** - 將動作分割成多個離散步階。適合想讓屬性「跳到」某些值，而不是平滑移動的情況。

{% hint style="info" %}
請注意，steps 是按時間而不是按數值分割。因此，如果一個波形分成 4 個 steps，duration 為 1 個小節，屬性便會每一拍即時改變一次。
{% endhint %}

* **clamp min / clamp max -** 將波形縮放至超出其最小值或最大值，然後限制結果。

{% hint style="info" %}
_clamp_ 這個概念比較難解釋，但你可以想像波形超出了圖表的頂部或底部，然後被限制在邊界上。我建議你實際試試！如果你想讓鋸齒波較遲開始或較早結束，它們會非常有用。
{% endhint %}

* **ease function** - Sawtooth 和 Triangle waves 亦有 ease function，可細微改變動畫曲線，令動畫更有表現力！
  * **LINEAR** - 預設值，沒有 easing，只會在線性方式下於 min 和 max 值之間移動。
* **EASE OUT** - 開始時較快，接近結尾時逐漸減慢。很適合模擬物理效果，例如慢慢停下來。
  * **EASE IN** - 開始時較慢，然後逐漸加速。適合模擬動量累積。
  * **EASE IN/OUT** - 兩者的組合，動作非常自然。

{% hint style="warning" %}
**Easing -** 除非你特別想要機械感的效果，否則我建議盡量避免使用預設的 linear animation。Easing 可以令動畫流暢、自然得多！
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> 鋸齒波

有時亦稱為 _ramp waveform_，因為它會向上斜升，然後在週期結尾急速下降。這可能是最常用的 wave oscillator，因為它可以為 _hue_ 或 _rotation_ 等循環屬性建立 loop。

請參閱上方章節了解：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

鋸齒波專用：

* **cycle range compensation** - 在設定了 **steps** 時可用，適合用於循環數值，例如從 0 到 360 的 rotation。未啟用時，起點和終點的值會相同，可能導致在起點停滯（因為 0 和 360 是同一個角度）。啟用後，最大範圍會被縮減，以修正 step 的位置。

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> 三角波

與每個週期都會跳回起點的 _sawtooth wave_ 不同，_triangle wave_ 會先線性向前移動，然後再線性向後移動。

請參閱上方章節了解：

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

最平滑的波形！像鐘擺一樣，在兩個值之間柔和地振盪。

請參閱上方章節了解：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> 方波

最簡單的波形——只是在兩個值之間來回切換！

請參閱上方章節了解：

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

方波專用：

* **pulse width** - 波形處於最大值的時間長度，相對於整體 duration。預設為 50%，即剛好一半一半。如果你只想讓它在四分之一時間內為「開啟」狀態，請設為 25%。你可以使用 _offset_ 值調整這個 pulse 發生的時間。

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> 雜訊

Liberation 的其中一個強項，是可以產生隨機但可重複的效果。_noise_ 振盪器可用來建立自然、有 loop 的隨機動作，細節或抖動程度可按需要調整。

請參閱上方章節了解：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

雜訊專用：

* **noise type** - 用於產生 noise 的演算法。
  * **SIMPLEX** - 預設值，會產生起伏流動、並以 loop 重複的數值。
  * **RANDOM** - 使用較傳統的隨機數演算法，效果完全雜亂而混沌。

{% hint style="info" %}
**Simplex noise** 由 Ken Perlin 於 2001 年設計，是他在 1983 年開發的「Perlin noise」演算法的改良版；當時該演算法是他為電影 _Tron_ 工作時開發的（他亦因此獲得奧斯卡獎！）

這種所謂的「gradient」noise，源於他對以往電腦生成影像過於「機械感」的不滿。在 CGI 世界中，它特別適合用來渲染雲、水面，甚至用作真實地形的 height-map。

但在 Liberation 中，它很適合用於看似不可預測、但仍然平滑自然的動作。
{% endhint %}

* **seed** - 用於建立 noise 的值。如果你不喜歡目前 noise wave 的效果，可以嘗試更改這個值。

{% hint style="info" %}
有趣的宅知識！為了取得完美 loop 的 simplex noise，我會在 2D noise plane 上沿圓形路徑迭代。而更改 seed 值，則會令這個平面在第 3 個維度中移動！
{% endhint %}

* **simplex detail** - 更改 noise 的細節或抖動程度。如果你想令重複圖案不那麼明顯，可以提高 duration 並增加此值。

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> 自訂振盪器

建立完全自訂的波形。這對建立複雜動畫非常有用。

請參閱上方章節了解：

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

下方是一組位置和數值。duration 會分成 64 個 steps，你可以在任何一個點放置數值。

每個 step 都有以下設定：

* **Step** - duration 內的時間 step。0 是起點，64 是終點。
* **Level** - 該時間 step 的波形 level。level 範圍為 0 至 1。
* **Animation type** - 下拉選單可讓你選擇要如何從上一個 step 移動到這個 level。
  * **None** - 沒有 transition，只會在指定時間直接跳到這個 level。
  * **Linear** - 從上一個 level 到這個 level 的完全線性移動。
  * **Ease in / Ease out / Ease in/out** - 在上一個 level 和這個 level 之間套用 easing。動畫類型說明請參閱上方的 _ease function_。

***
