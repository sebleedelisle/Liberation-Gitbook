---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 效果

Liberation 的效果系統是一個有趣又靈活的方法，可以即時改變 Clip 輸出。效果非常彈性，可以用來令所有內容閃動、旋轉、變色，甚至隨機飛來飛去！

凡是在 Clip 編輯器做到的事，都可以用作效果。事實上，效果就是用與 Clip 完全相同的 node 編輯器來編輯！請參閱 [編輯效果](effects.md#editing-effects "mention")。創作可能性幾乎無限。

預設效果按鈕 1-8 位於 zone 按鈕下方，而效果 9-24 則是底部的小按鈕。

#### 套用效果

按下效果按鈕可切換效果；更好的做法是使用 APC40 slider 1-8 淡入及淡出效果。如沒有 APC40，要淡入效果，可在按鈕上按住並上下拖曳。或者在效果按鈕上右擊，然後調整 level slider。

{% hint style="warning" %}
按下效果按鈕會立即啟用該效果。不過請注意，如果 level 設為零，將不會有任何變化！按住並拖曳按鈕以更改 level，或右擊並使用 _level_ slider，或使用 APC40 fader。
{% endhint %}

#### 效果與 Clip 的 zone delay

效果會沿用每個正在播放 Clip 的 zone delay 設定。因此，如果你的 Clip 有一個由左至右移動的延遲，而你加入閃動效果，閃動亦會由左至右延遲。

{% hint style="info" %}
Clip 的 zone delay 如何由效果繼承，是那種很難用文字說明、但一試就明白的功能！

我會說，這是 Liberation 內置最有趣、最具創意的工具之一。試試看，你就會明白我的意思！
{% endhint %}

#### 效果參數

使用 _Parameter node_ 為你的效果加入參數。Parameter 系統是一種從外部調整效果內多個設定的方法。更多資料請參閱 [參數控制](clip-editor/oscillators/parameter-control.md "mention")。

使用 rotary controller 1-8 調整每個效果的 _parameter_。或者右擊效果按鈕，然後調整 parameter slider。parameter 的變化會因應效果的設定方式而有不同作用。請參閱以下預設效果清單，了解它們的 parameter 作用。

{% hint style="info" %}
Rotary controller 1-8 位於 APC40 Mk2 頂部一排，以及 Mk1 的右上方。另請參閱：[APC40 參考](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
你在效果按鈕上看到的小數字，代表該效果的 _level_ 和 _parameter_。_level_ 由 APC40 上的 fader 控制，或你可以在按鈕上按住拖曳。parameter 由 APC40 上的 rotary 控制，或你可以右擊並用滑鼠調整。
{% endhint %}

#### 預設效果

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   對 Clip 輸出套用混亂的移動。parameter 會調整混亂的幅度／速度。
2. **Sine wave** :\
   以移動中的正弦波扭曲所有內容。parameter 會調整波長。
3. **Rotation** :\
   令所有內容旋轉。parameter 會調整旋轉速度。
4. **Horizontal flip** :\
   水平方向壓縮及拉伸所有內容。parameter 會調整速度。
5. **Scale** :\
   反覆將所有內容由完整大小縮放至零。parameter 會調整速度。
6. **Hue** :\
改變所有內容的 hue，但不改變 saturation（即任何白色內容仍會保持白色）。parameter 會調整 hue。
7. **Saturation and hue** :\
改變所有內容的 hue，並同時將顏色完全飽和（即任何白色內容都會變成該顏色）。parameter 會調整 hue。
8. **Flash** :\
   反覆將所有內容的亮度由完整降至零。parameter 會調整閃動速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一排還有另外 16 個顏色效果，可套用預設的 hue 和 saturation 值。

請注意，這些是預設效果，但你可以編輯它們，幾乎做到任何你想要的效果！

### 套用至群組

你可以選擇哪些群組會受效果影響。右擊並切換標示為 _Apply to groups_ 的群組核取方塊。

我主要在分開處理 canvas graphics 和 laser beams 時使用這種設定。我會將所有 canvas Clip 指派到 group 5，然後在不想影響這些圖像 Clip 的效果中排除此群組。

你亦可以用它即場同時對兩組 laser 套用 2 種不同顏色變化。建立兩個顏色變化效果，然後選擇每個效果要套用到哪些 Clip 群組。

### MX group

_Mutually Exclusive_ 的縮寫，這是一種將效果分組的方法，使同一群組內同一時間只能有一個效果處於啟用狀態。留意預設顏色變化效果中，同一時間只能啟用其中一個。這是因為它們全部都在 MX Group 1。

如果 _MX Group_ 設定為 0，此功能會被停用。

### 編輯效果

在任何效果上右擊，然後按 _EDIT EFFECT_ 按鈕開啟效果編輯器。留意這個編輯器與 Clip 編輯器完全相同！

像編輯任何 Clip 一樣編輯你的效果。請參閱 [Clip 編輯器](clip-editor/ "mention")。

你需要至少一個 creator node；它可以是任何東西（line、circle、shape，甚至 text！），但最好選擇在效果按鈕預覽中最合理的內容。

套用效果時，效果內所有 creator node 都會被目前正在播放的 Clip 輸出取代。

{% hint style="warning" %}
由於一些極其繁瑣的技術原因，在效果內無法啟用 "trails" node。同樣情況亦適用於 pattern node 內的 "delay" 設定（它們使用相同系統）。這會在未來版本中修正。
{% endhint %}
