---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation 節點

## &#x20;Randomise

使用連貫的 noise field，為輸入元素建立分散的複本。換句話說，它會以受控、帶有「noise」的方式複製並移動你的形狀和點。內容不再整齊地停留在同一位置，而是產生多個會偏移和散開的版本，就像粒子在流動中移動。

* **count** – 每個輸入元素的複本數量（1–20）。設為 1 時，每個元素會產生一個帶有抖動的版本。較高數值會建立多個分散複本。
* **noise offset** – 在 noise field 中循環移動（0–100%）。它會無縫循環，所以用 Oscillator Node 為它製作動畫時，所有複本會一起產生平滑、連續的動作。
* **noise jitter** – 控制 noise 的紋理比例。較低數值會產生寬闊、平滑的變化；較高數值會產生更緊密、更不規則的位置。這會改變圖案，而不是強度。
* **change between points** – 控制每個複本與上一個複本之間的差異。低數值會令複本保持集中且相似；高數值會令它們散開，並有更大的變化。
* **face direction** – 旋轉每個複本，令它面向 noise field 中的移動方向，產生與流動方向對齊的箭頭／粒子。
* **amount** – 效果的整體強度（0–100%）。同時縮放位移，以及來自 **face direction** 的旋轉。

{% hint style="info" %}
Randomise 節點是 Randomise effect 的核心！
{% endhint %}

## &#x20;Trails

為你的內容建立回聲，在原始內容移動時，在其後方留下會淡出或縮放的複本。

* **change render profile for trail** – 開啟後，所有 trail 複本都會使用所選的 **render profile**。_請參閱_ [渲染設定檔](../fundamentals/render-profile.md "mention")。
* **render profile** – 當上方開關開啟時，trail 複本使用的 profile。常見用法是主內容設為 **DETAIL**，而回聲以 **FAST** 渲染；這樣主形狀可以保持清晰細節，同時更有效率地渲染 trails。
* **delay** – 以音樂時間設定 trail 複本之間的間距，單位為 **1/64 音符步距**。\
  參考值：
  * 16 = 1/16 小節（十六分音符）
  * 32 = 1/8 小節（八分音符）
  * 64 = 1/4 小節（四分音符）
  * 128 = 1/2 小節（二分音符）
  * 256 = 1 小節
* **trail size** – 在即時內容後方繪製多少個 trail 複本。
* **prefill trails** – Clip 開始時立即填滿 trail history，而不是等回聲在最初幾拍逐漸建立。
* **freeze trails** – 將平滑流動的 trails 變成一連串凍結的快照。適合建立斷奏、與拍子同步的 trail 效果。
* **brightness start / brightness end** – 在 trail 上套用亮度，由最新的複本（**start**）到最舊的複本（**end**）。通常將 **brightness start** 設為 100%，並將 **brightness end** 設為 0%，回聲便會淡出。
* **scale start / scale end** – 在 trail 上套用縮放，由最新的複本（start）到最舊的複本（end）。如要 trails 縮小至消失，請將 **scale start** 設為 100%，並將 **scale end** 設為 0%。

## &#x20;Shimmer

為你的內容加入閃爍的亮度變化，效果可由柔和閃光到強烈頻閃。

* **speed** – shimmer 隨時間變化的速度。較高數值會閃爍得更快；0 會暫停效果。
* **separation** – 相鄰點／元素之間的差異程度。
  * 0：所有內容一起 shimmer。
  * \>0：附近的點會逐漸取得不同相位，所以 shimmer 會沿形狀產生變化。
  * <0：與上方相同，但相位推進方向相反。
* **threshold** – 不再平滑淡入淡出，而是根據亮度讓點完全開啟或關閉。較亮的元素會更頻繁亮起；但請注意，100% 亮度的元素會一直開啟，而 0% 亮度的元素會一直關閉。適合製作清脆的閃粉或星光效果。

{% hint style="info" %}
開啟 **threshold** 是其中一個很實用的隱藏功能，可以令你的粒子或內容更有生命感。點不會淡入淡出，而是根據亮度快速開關。由於任何一刻繪製的點更少，結果會有更亮的輸出和更順滑的動畫。

但請記住，如果你的內容本身已經是 100% 亮度，它就不會有任何效果！
{% endhint %}

* **use whole shape** – 將同一個 shimmer 值平均套用到整個形狀。關閉時，節點會細分形狀，讓不同部分可獨立閃爍，形成帶有斑點的外觀。

## &#x20;Particles

這是一個實驗性效果，會根據你的內容產生並製作粒子動畫。任何輸入的點狀元素都會被視為 emitter 位置。由於粒子路徑是預先計算的，如果你的輸入內容有變，可能需要重新整理／重新計算以更新粒子（只要改動任何設定即可）。

**General**

* **keep original** – 開啟後會保留原始內容，並在其上方加入粒子。當你想 emitter 點保持可見時很有用。
* **number of particles** – 每次 emission 建立多少粒子。較高數值會產生較密集的效果；較低數值則更簡約。
* **emission period** – 發射粒子的 loop 範圍（以小節計）。設為 100% 時，粒子會平均分佈在 loop 中；較小數值會將它們集中在一起，形成爆發效果。
* **loop length** – 粒子 loop 持續多久，以音樂小節計算。
* **loop count** – loop 在重設前重複多少次。設為 1 時，粒子每次都會遵循完全相同的模擬，令效果可完美重複。較高數值會在週期重設前引入更多變化。
* **delay** – 以 1/64 音符數量偏移 emission 的開始時間，用於時間效果。

**Motion**

* **speed** – 粒子離開 emitter 的速度。
* **speed variation** – 加入隨機性，令粒子不會全部以同一速度移動，產生更自然的散佈。
* **direction** – 設定粒子發射的基本方向，由 **x, y, z angles** 定義。這些角度會在 3D 空間中旋轉發射向量，所以你可以將粒子指向正上方、側方，或任何對角方向。配合 **spread** 使用，可製作更寬的錐形或更混亂的爆發。

{% hint style="info" %}
**Euler angles（歐拉角）**\
Liberation 使用 **Euler angles** 描述 3D 空間中的方向。它們其實就是圍繞三個主要軸的旋轉：

* **X** – 向前／向後傾斜（像點頭）
* **Y** – 向左／向右轉（像搖頭表示「不」）
* **Z** – 順時針／逆時針滾轉（像把頭側向傾斜）

調整這三個數值，就可以將粒子指向任何方向。
{% endhint %}

* **direction variation** – 在該方向周圍加入隨機散佈。適合製作錐形、噴射或爆炸。
* **drag** – 令粒子隨時間減速。較高數值會令它們感覺更重、更遲緩。
* **gravity** – 將粒子向下拉（正值）或向上推（負值）。
* **gravity variation** – 為每個粒子加入不同的 gravity 變化，令動作更混亂。

**Life**

* **life duration** – 粒子存在多久（以 1/64 音符單位計）。較短數值會令粒子快速消失；較長數值則會令它們在較長時間內保持可見。
* **life variation** – 為粒子壽命加入隨機性，令它們不會同時消失。
* **start delay / start delay variation** – 延遲每個粒子變得可見的時間（以 1/64 音符步距計）。在這段時間內，粒子已經產生並正在移動，但亮度會保持為 0，所以會一直不可見，直到 delay 結束。當你想延遲出現煙花式「火花」時很有用。

**Colour & brightness**

* **hue start** – 粒子的初始顏色。
* **hue variation** – 加入隨機性，令粒子不會全部以同一顏色開始。
* **hue change** – 在粒子壽命期間偏移色相，產生會變色的 trails。
* **brightness start / brightness end** – 在粒子的整個生命週期套用亮度。通常將 brightness start 設高、brightness end 設低，令粒子自然淡出。
* **brightness variation** – 隨機化起始亮度，令外觀更有動感。
* **saturation start / saturation end** – 設定開始和結束時顏色的鮮明程度。
* **saturation variation** – 隨機化 saturation，令粒子之間有變化。

**Simulation**

* **time adjustment** – 加快或減慢整個粒子模擬。適合用來同步不同 tempo，或誇張化動作。
