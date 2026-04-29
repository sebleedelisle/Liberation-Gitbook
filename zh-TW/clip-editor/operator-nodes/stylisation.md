---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 風格化 nodes

## &#x20;Randomise

使用連續的雜訊場，為傳入的元素建立分散的副本。換句話說，它會以可控且帶有「雜訊」的方式複製並移動你的形狀與點。內容不再整齊地停留在同一個位置，而是產生多個版本並位移、擴散，就像粒子在流場中移動一樣。

* **count** – 每個傳入元素的副本數量（1–20）。設為 1 時，每個元素會產生一個帶有抖動的位置版本。較高的值會建立多個分散副本。
* **noise offset** – 在雜訊場中循環位移（0–100%）。它會無縫循環，因此用 Oscillator Node 來動畫化此參數時，所有副本會一起產生平順、連續的動作。
* **noise jitter** – 控制雜訊的紋理尺度。較低的值會產生寬廣、平滑的變化；較高的值會讓位置更緊密且更不規則。這會改變圖樣，而不是改變效果強度。
* **change between points** – 控制每個副本相對於前一個副本的差異程度。低值會讓副本聚集且相似；高值會讓副本分散，並產生更大的變化。
* **face direction** – 旋轉每個副本，使其面向雜訊場中的移動方向，可產生順著流向排列的箭頭／粒子效果。
* **amount** – 整體效果強度（0–100%）。同時縮放位移量，以及 Face direction 產生的旋轉量。

{% hint style="info" %}
Randomise node 是 Randomise 效果的核心！
{% endhint %}

## &#x20;Trails

為你的內容建立回聲效果，讓原始內容移動時，後方留下逐漸淡出或縮放的副本。

* **change render profile for trail** – 開啟時，所有 trail 副本都會使用選取的 **render profile**。_請參閱_ [Render profile](../fundamentals/render-profile.md)。
* **render profile** – 上方開關啟用時，trail 副本要使用的 profile。常見用法是主內容設為 **DETAIL**，但回聲以 **FAST** 來算圖；這樣主要形狀能保持清楚細節，同時更有效率地算出 trails。
* **delay** – 以音樂時間設定 trail 副本之間的間距，單位為 **1/64 音符步進**。\
  參考如下：
  * 16 = 1/16 小節（十六分音符）
  * 32 = 1/8 小節（八分音符）
  * 64 = 1/4 小節（四分音符）
  * 128 = 1/2 小節（二分音符）
  * 256 = 1 小節
* **trail size** – 在即時內容後方繪製多少個 trail 副本。
* **freeze trails** – 將平滑流動的 trails 轉換成一連串凍結的快照。適合製作斷奏感、與節拍同步的 trail 效果。
* **brightness start / brightness end** – 將亮度套用到整段 trail，從最新的副本（**start**）到最舊的副本（**end**）。通常將 **brightness start** 設為 100%，並將 **brightness end** 設為 0%，回聲就會逐漸淡出。
* **scale start / scale end** – 將縮放套用到整段 trail，從最新的副本（start）到最舊的副本（end）。如果要讓 trails 縮小到消失，請將 **scale start** 設為 100%，並將 **scale end** 設為 0%。

## &#x20;Shimmer

為內容加入閃爍的亮度變化，從柔和的微光到強烈的頻閃都可以製作。

* **speed** – shimmer 隨時間變化的速度。值越高閃爍越快；0 會暫停效果。
* **separation** – 控制相鄰點／元素之間的差異程度。
  * 0：所有內容一起 shimmer。
  * \>0：鄰近的點會逐漸取得不同相位，因此 shimmer 會在形狀上產生變化。
  * <0：與上述相同，但相位推進方向相反。
* **threshold** – 點不再平滑淡入淡出，而是依照亮度完全開啟或關閉。較亮的元素會更頻繁地亮起，但請注意，亮度 100% 的元素會永遠開啟，亮度 0% 的元素會永遠關閉。適合製作俐落的閃光或星光效果。

{% hint style="info" %}
開啟 **threshold** 是一個很實用的隱藏功能，可以讓粒子或內容更有生命感。點會依照亮度快速開關，而不是淡入淡出。因為任一時間實際繪製的點變少，結果通常會有更亮的輸出和更平滑的動畫。

但請記得，如果你的內容本來就已經是 100% 亮度，這個設定不會產生效果！
{% endhint %}

* **use whole shape** – 將單一 shimmer 值均勻套用到整個形狀。關閉時，node 會將形狀細分，讓不同部分可各自獨立閃爍，形成斑點感。

## &#x20;Particles

這是一個實驗性效果，會根據你的內容產生並動畫化粒子。任何傳入的點狀元素都會被視為發射器位置。由於粒子路徑是預先計算的，如果你的輸入內容改變，可能需要重新整理／重新計算來更新粒子（只要變更任一設定即可）。

**General**

* **keep original** – 開啟時，原始內容會保留，粒子會疊加在上方。當你希望發射器點保持可見時很有用。
* **number of particles** – 每次發射建立的粒子數量。較高的值會產生更密集的效果，較低的值則較簡潔。
* **emission period** – 粒子發射所涵蓋的循環區段（以小節為單位）。設為 100% 時，粒子會平均分布在整個循環中；較小的值會將粒子集中在一起，形成爆發效果。
* **loop length** – 粒子循環持續多久，以音樂小節計算。
* **loop count** – 在重設之前，循環會重複幾次。若設為 1，粒子每次都會遵循完全相同的模擬結果，因此可完美重現。較高的值會在循環重設前加入更多變化。
* **delay** – 以 1/64 音符為單位位移發射開始時間，用於時間點效果。

**Motion**

* **speed** – 粒子離開發射器的速度。
* **speed variation** – 加入隨機性，讓粒子不會全部以相同速率移動，可產生更自然的擴散。
* **direction** – 設定粒子發射的基本方向，由 **x, y, z angles** 定義。這些角度會在 3D 空間中旋轉發射向量，因此你可以讓粒子筆直向上、向側邊，或朝任何斜向發射。可搭配 **spread** 產生更寬的錐形或更混亂的爆發。

{% hint style="info" %}
**歐拉角**\
Liberation 使用 **Euler angles** 來描述 3D 空間中的方向。它們就是圍繞三個主要軸的旋轉：

* **X** – 向前／向後傾斜（像點頭）
* **Y** – 向左／向右轉動（像搖頭表示「不」）
* **Z** – 順時針／逆時針滾轉（像把頭往側邊傾斜）

調整這三個值，就能把粒子指向任何方向。
{% endhint %}

* **direction variation** – 在該方向周圍加入隨機擴散。適合製作錐形、噴灑或爆炸效果。
* **drag** – 讓粒子隨時間減速。較高的值會讓粒子感覺更重、更遲滯。
* **gravity** – 將粒子向下拉（正值）或向上推（負值）。
* **gravity variation** – 為每個粒子加入重力變化，讓運動更混亂。

**Life**

* **life duration** – 粒子存在的時間長度（以 1/64 音符單位計算）。較短的值會讓粒子快速消失；較長的值則會讓粒子維持可見更久。
* **life variation** – 為粒子壽命加入隨機性，避免所有粒子同時消失。
* **start delay / start delay variation** – 延遲每個粒子變成可見的時間（以 1/64 音符步進為單位）。在這段期間粒子已經產生並開始移動，但亮度維持在 0，因此會一直不可見，直到延遲時間結束。當你想製作延遲出現的煙火「閃光」時很有用。

**Colour & brightness**

* **hue start** – 粒子的初始顏色。
* **hue variation** – 加入隨機性，讓粒子不會全部以相同顏色開始。
* **hue change** – 在粒子生命週期中改變色相，產生會變色的 trails。
* **brightness start / brightness end** – 將亮度套用到粒子的生命週期。通常將 brightness start 設高、brightness end 設低，讓粒子自然淡出。
* **brightness variation** – 隨機化起始亮度，產生更有動態的外觀。
* **saturation start / saturation end** – 設定起始與結束時顏色的鮮豔程度。
* **saturation variation** – 隨機化飽和度，讓粒子之間產生變化。

**Simulation**

* **time adjustment** – 加快或放慢整個粒子模擬。適合用來同步不同速度，或誇張化動作。
