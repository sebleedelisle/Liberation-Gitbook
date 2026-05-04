---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas 概觀

Liberation 的 Canvas 系統相對簡單，但一開始可能會有點讓人混淆。以下先用概念性的方式說明，幫助你快速上手。

{% hint style="info" %}
**等等，我需要使用 Canvas 系統嗎？**

不一定！如果你只是要把單一圖形投射到單一雷射，可以很容易地使用 beam zone 完成（不過 beam zone 的內容預設會水平翻轉，所以你需要對 Clip 做 X flip）。

但如果你想把圖形內容分散到多台雷射上，或是拆成不同區段來對應建築物表面，那 Canvas 系統就很適合！
{% endhint %}

### Canvas

首先是 Canvas 本身。這就是你在 _CANVAS_ view 中看到的內容，代表一個很大的「畫布」，你可以在這個空間內的任何位置繪製內容。

### Canvas 目標區域

這些會在 Canvas view 中顯示為藍色外框矩形，是你可以送出內容的區域。你會把某個 Clip 的內容送到 Canvas 目標區域，就像把 Clip 送到 beam zone 一樣。在 Clip Deck 中，Canvas 目標區域按鈕會出現在 beam zone 按鈕的右側。

{% hint style="info" %}
如果你在 Clip Deck 中看不到 Canvas 按鈕，請試著用 `Shift + Left / Right Arrow` 捲動 beam zone 按鈕。你應該會看到每個 Canvas 目標區域都有一個按鈕，標示為 _CANVAS 1, CANVAS 2_ 等等。
{% endhint %}

### Canvas zones

Canvas zones 是 Canvas 內你選擇要送到雷射的區域。它們會在 Canvas view 中以粉紅色外框矩形表示。你可以在每個 zone 上按右鍵，選擇要指派給哪些雷射。如果你接著切換到該雷射的 _OUTPUT_ view，就會看到新的 zone 已經出現。

{% hint style="danger" %}
警告：如果雷射處於 armed 狀態，你可能會突然開始在預設的 canvas zone 中投射內容。建議先將雷射 disarm，再把 canvas zones 指派給它。
{% endhint %}

{% hint style="info" %}
你也可以在 _OUTPUT_ view 中點擊 _add canvas zone_ 按鈕，將 canvas zone 指派給雷射。請參閱 [Zones](../output-view/zones.md "mention")。
{% endhint %}

### 參考圖片

你可以將參考圖片加入 Canvas，並把它當作圖形的範本使用。建議調整參考圖片的色調（右鍵選單），並將它調暗，這樣比較容易看清楚疊在上面的內容。

{% hint style="info" %}
在做建築 mapping 時，我發現先製作一張建築物的「展開」視覺圖很有幫助：把建築物上的所有表面表示成一張平面、未變形的圖片。各區段的透視校正可以在 _OUTPUT_ view 中使用 canvas zone 來完成。
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>英國 Gateshead 的 Saltwell Hall「攤平」參考圖片</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Liberation 早期版本（約 2017 年！）中的 canvas zones。請注意，粉紅色矩形用來選擇要顯示 Canvas 的哪一部分，而下方的 Output views 則顯示這些 zones 會送到各台雷射的哪個部分。</p></figcaption></figure>

### 3D visualiser 中的 Canvas

要在 3D visualiser 中重建複雜的多雷射投影系統，可能會相當麻煩（說得保守一點）。因此，你可以選擇把 Canvas 放進 3D 空間中。請在 _3D visualiser settings_ panel 中啟用 _Show canvas_ 核取方塊。（你在 Canvas 中加入的任何參考圖片，也會顯示在 visualiser 中。）

{% hint style="info" %}
請注意，visualiser 仍會把 Canvas 投影顯示成從雷射發出的空氣光束效果。你可以直接把它們移出視野；或者，如果你想做得更精準，也可以把它們和 Canvas 對齊！
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>當你在 3D visualiser 中把雷射光束和 Canvas 圖像對齊時，效果會非常有成就感！</p></figcaption></figure>
