---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas 概覽

Liberation Canvas 系統相對簡單，但一開始可能會有點難理解。以下是一個概念性概覽，幫助你上手。

{% hint style="info" %}
**等等，我需要使用 Canvas 系統嗎？**

未必！如果你只是把單一圖像投射到單一雷射上，用 beam zone 就可以輕鬆做到（不過預設情況下，beam zone 內容會水平反轉，所以你需要對 clip 做 X flip）。

但如果你想將圖像內容分散到多部雷射，或者把內容分拆成不同部分以映射到建築物上，Canvas 系統就可以幫到你！
{% endhint %}

### Canvas

首先，是 Canvas 本身。這就是你在 _CANVAS_ view 中看到的內容，代表一塊大型的「畫布」；你可以在這個空間內任何位置繪製內容。

### Canvas 目標範圍

在 Canvas view 中，這些範圍會以藍色外框矩形顯示，它們是你可以發送內容的目標範圍。你可以把某個 clip 的內容發送到 Canvas 目標範圍，方式就像把 clip 發送到 beam zone 一樣。在 clip deck 中，你會在 beam zone 按鈕右邊看到 Canvas 目標範圍按鈕。

{% hint style="info" %}
如果你在 clip deck 中看不到 Canvas 按鈕，請嘗試用 `Shift + Left / Right Arrow` 捲動 beam zone 按鈕。你應該會看到每個 Canvas 目標範圍都有一個按鈕，標籤為 _CANVAS 1, CANVAS 2_ 等。
{% endhint %}

### Canvas zone

Canvas zone 是 Canvas 內你選擇發送到雷射的範圍。在 Canvas view 中，它們會以粉紅色外框矩形表示。你可以在每個 zone 上按右鍵，然後選擇要指派到哪些雷射。如果你現在切換到該雷射的 _OUTPUT_ view，會看到一個新的 zone 已經出現。

{% hint style="danger" %}
警告：如果雷射已 armed，你可能會突然開始在預設 Canvas zone 中投射內容。最好先 disarm 該雷射，再把 Canvas zone 指派給它。
{% endhint %}

{% hint style="info" %}
你也可以在 _OUTPUT_ view 中按 _add canvas zone_ 按鈕，將 Canvas zone 指派到雷射。請參閱 [區域](../output-view/zones.md)。
{% endhint %}

### Guide images

你可以把 guide image 加入 Canvas，並用它作為圖像內容的模板。建議調整 guide image 的 colour tint（右鍵選單），並把它調暗，這樣會更容易在其上方看清你的內容。

{% hint style="info" %}
進行建築映射時，我發現製作一張建築物的「展開」視覺圖很有幫助，將建築物所有表面表示成一張平面、未變形的圖片。各個部分的透視校正可以在 _OUTPUT_ view 中使用 Canvas zone 完成。
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>英國 Gateshead 的 Saltwell Hall「展平」guide image</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Liberation 早期雛形版本中的 Canvas zone（約 2017 年！）請留意粉紅色矩形會選擇要顯示 Canvas 的哪一部分，而下方的 output view 則顯示這些 zone 會送到每部雷射的哪一部分。</p></figcaption></figure>

### 3D visualiser 中的 Canvas

要在 3D visualiser 中重建你複雜的多雷射投影系統，可能會相當繁瑣（至少可以這樣說）！所以，你可以選擇把 Canvas 放到 3D 空間中。在 _3D visualiser settings_ panel 中啟用 _Show canvas_ checkbox。（你在 Canvas 中加入的任何 guide image 也會在 visualiser 中顯示。）

{% hint style="info" %}
請注意，visualiser 仍會把 Canvas 投影顯示為由雷射發出的空氣中光束效果。你可以簡單地把它們移出視野；如果想更進一步，也可以把它們與 Canvas 對齊！
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>當你在 3D visualiser 中把雷射光束與 Canvas 圖像對齊時，效果會非常令人滿足！</p></figcaption></figure>
