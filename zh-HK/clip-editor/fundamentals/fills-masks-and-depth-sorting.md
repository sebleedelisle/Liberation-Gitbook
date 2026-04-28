---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 填色、遮罩及深度排序

### 描邊、填色及遮罩

你會留意到部分 Creator 節點有 _Fill state_ 選項；你可以用描邊（外框）繪製，或作為遮罩（覆蓋下面的內容）繪製，亦可以兩者同時使用。

當你將圖形渲染為遮罩時，就好像它被填滿成黑色，而其下方的任何內容都會被遮住。

{% hint style="info" %}
用雷射畫一條線（或 _stroke_）相當簡單；你只要讓雷射由線的起點掃描到終點。這就是你的線！

不過填滿圖形就較困難；如果你想用顏色填滿一個圖形，可以手動用交叉排線畫線並填滿，但 Liberation 目前還未能自動做到這一點。而且即使我們做到，你仍然會看到下面其他線條透出來。

但我們可以做到的是用 _黑色_ 填滿圖形。在背後，Liberation 會進行所有計算，移除位於黑色填滿圖形下方的內容。相信我，這件事很繁瑣！

但它的效果非常好，能營造出黑色填滿圖形的錯覺。
{% endhint %}

### 深度排序

由於某些圖形可以 _覆蓋_ 其他圖形，Liberation 必須按深度為它們排序。預設情況下，元素會按其 z 位置進行深度排序。如果它們位於相同的 z 位置，則會按其圖層位置排序；你可以使用每個 Creator 內的 _MOVE TO FRONT_ 和 _MOVE TO BACK_ 按鈕來更改圖層位置。
