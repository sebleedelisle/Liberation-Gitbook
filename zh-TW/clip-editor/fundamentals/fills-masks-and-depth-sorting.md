---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 填色、mask 與深度排序

### 線條、填色與 mask

你會注意到有些 Creator nodes 有 _Fill state_ 選項；你可以用線條（外框）繪製它們，也可以作為 mask（覆蓋下方內容）繪製，或兩者同時使用。

當你把一個形狀渲染成 mask 時，就像它被填成黑色一樣，底下的任何內容都會被遮住。

{% hint style="info" %}
用雷射畫一條線（或 _stroke_）很簡單；你只要讓雷射從線的起點掃描到終點。線就畫好了！

不過填滿形狀就比較困難；如果你想要用顏色填滿形狀，可以手動用交叉線條來填色，但 Liberation 目前還不能自動做到這件事。就算我們真的這樣做了，你仍然會看到底下其他線條透出來。

但我們能做的是用 _黑色_ 填滿形狀。在背後，Liberation 會進行所有計算，移除位於黑色填滿形狀下方的內容。相信我，這很繁瑣！

但它運作得很好，也能營造出黑色填滿形狀的效果。
{% endhint %}

### 深度排序

由於某些形狀可以_覆蓋_其他形狀，Liberation 必須依照深度為它們排序。預設情況下，元素會依照 z 位置進行深度排序。如果它們位於相同的 z 位置，則會依照圖層位置排序；你可以使用每個 Creator 內的 _MOVE TO FRONT_ 和 _MOVE TO BACK_ 按鈕來變更圖層位置。
