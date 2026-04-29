---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 效果

Liberation 的效果系統是一種有趣又多用途的方式，可即時改變 Clip 的輸出。效果非常彈性，可以讓所有內容閃爍開關、旋轉、變換顏色，甚至隨機飛舞！

你在 Clip Editor 裡能做的任何事，都可以用來做成效果。事實上，效果使用的就是和 Clips 完全相同的 node editor！請參閱 [編輯效果](effects.md#editing-effects)。創作上的可能性幾乎是無限的。

預設的效果按鈕 1-8 位於 zone 按鈕下方，效果 9-24 則是底部的小按鈕。

#### 套用效果

按下效果按鈕可以切換效果；更好的方式是使用 APC40 的滑桿 1-8 來淡入淡出效果。若沒有 APC40，也可以在按鈕上按住並上下拖曳來淡入效果。或是在效果按鈕上按右鍵，調整 level 滑桿。

{% hint style="warning" %}
按下效果按鈕會立刻啟用該效果。不過請注意，如果 level 設為零，就不會有任何變化！請點擊/拖曳按鈕來變更 level，或按右鍵使用 _level_ 滑桿，或使用 APC40 的 fader。
{% endhint %}

#### 效果與 Clip 的 zone delay

效果會沿用目前正在執行的每個 Clip 的 zone delay 設定。因此，如果你的 Clip 有一個從左到右移動的 delay，而你加入閃爍效果，閃爍也會從左到右延遲。

{% hint style="info" %}
Clip 的 zone delay 如何被效果繼承，是那種非常難用文字描述、但實際試一次就很明顯的功能！

我會說這是 Liberation 內建最有趣、最有創造性的工具之一。試試看，你就會懂我的意思！
{% endhint %}

#### 效果參數

使用 _Parameter node_ 為你的效果加入參數。Parameter 系統是一種從外部調整效果內多個設定的方式。更多資訊請參閱 [參數控制](clip-editor/oscillators/parameter-control.md)。

使用旋鈕控制器 1-8 來調整每個效果的 _parameter_。或是在效果按鈕上按右鍵，調整 parameter 滑桿。parameter 的變化會依效果設定方式而產生不同作用。以下列出預設效果，以及它們的 parameter 作用。

{% hint style="info" %}
旋鈕控制器 1-8 位於 APC40 Mk2 的頂部，或 APC40 Mk1 的右上方。另請參閱：[APC40 參考](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
你在效果按鈕上看到的小數字，代表該效果的 _level_ 和 _parameter_。_level_ 由 APC40 上的 fader 控制，也可以在按鈕上點擊拖曳。parameter 則由 APC40 上的旋鈕調整，也可以按右鍵用滑鼠調整。
{% endhint %}

#### 預設效果

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   對 Clip 輸出套用混亂的移動。parameter 會調整混亂的程度/速度。
2. **Sine wave** :\
   讓所有內容沿著移動的正弦波變形。parameter 會調整波長。
3. **Rotation** :\
   讓所有內容旋轉。parameter 會調整旋轉速度。
4. **Horizontal flip** :\
   將所有內容水平壓縮與拉伸。parameter 會調整速度。
5. **Scale** :\
   反覆將所有內容從完整大小縮放到零。parameter 會調整速度。
6. **Hue** :\
   改變所有內容的色相，但不改變飽和度（也就是白色的內容仍會保持白色）。parameter 會調整色相。
7. **Saturation and hue** :\
   改變所有內容的色相，並讓顏色完全飽和（也就是白色的內容會變成該顏色）。parameter 會調整色相。
8. **Flash** :\
   反覆讓所有內容的亮度從全亮閃到零。parameter 會調整閃爍速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一列另外有 16 個顏色效果，可套用預設的色相與飽和度值。

請注意，這些是預設效果，但你可以編輯它們，讓它們幾乎做任何你想要的事！

### 套用到群組

你可以選擇哪些群組會受到效果影響。按右鍵並切換標示為 _Apply to groups_ 的群組核取方塊。

我主要在分開處理 canvas 圖形與雷射光束時使用這個設定。我會把所有 canvas Clips 指派到群組 5，然後在不想影響這些圖形 Clips 的效果中排除此群組。

你也可以用它來現場同時對兩組雷射套用 2 種不同的顏色變化。建立兩個顏色變化效果，並選擇各自要套用到哪些 Clip 群組。

### MX group

_Mutually Exclusive_ 的縮寫，這是一種將效果分組的方式，讓同一群組中同一時間只能有一個效果處於啟用狀態。注意預設的顏色變化效果一次只能啟用其中一個。這是因為它們全部都在 MX Group 1 中。

如果 _MX Group_ 設定為 0，這項功能會停用。

### 編輯效果

在任何效果上按右鍵，然後點擊 _EDIT EFFECT_ 按鈕開啟效果編輯器。請注意，這個編輯器和 Clip Editor 完全相同！

用編輯任何 Clip 的方式來編輯你的效果。請參閱 [Clip Editor](clip-editor/)。

你需要至少有一個 Creator node；它可以是任何東西（線條、圓形、形狀，甚至文字！），但你應該選擇在效果按鈕預覽中最合理的內容。

套用效果時，效果中的所有 Creator nodes 都會被目前正在執行的 Clips 輸出取代。

{% hint style="warning" %}
基於非常繁瑣的技術原因，在效果內部時無法啟用 "trails" nodes。pattern nodes 裡的 "delay" 設定也是一樣（它們使用相同系統）。這會在未來版本中修正。
{% endhint %}
