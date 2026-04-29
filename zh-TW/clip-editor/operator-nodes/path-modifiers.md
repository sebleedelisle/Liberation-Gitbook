---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 路徑修改器

## &#x20;Dotter

這個 node 會將線條與形狀內容替換成等距排列的點（現有的點會保持不變）。

* **Colour** – 點的顏色。如果已啟用 _Inherit Colour_，此設定會被忽略，請見下方說明。_另請參閱_ [色彩設定與 HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – 點與點之間的距離，以像素為單位。數值越小 = 點越多，數值越大 = 點越少。
* **Offset** – 以間距百分比偏移點的起始位置。可製作動畫（例如搭配鋸齒波 Oscillator Node）來建立「移動」點效果。
* **Keep Original** – 啟用時會保留原始線條／形狀，並將點繪製在其上方。
* **Render Profile** – 選擇算繪品質。_請參閱_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – 自動調整間距，讓路徑長度可被平均分割。
* **Fade Out Ends** – 逐漸降低靠近路徑起點與終點的點亮度。當你用鋸齒波 Oscillator Node 製作 **Offset** 動畫時很有用，可讓點移動到形狀末端時平順淡入／淡出。

## &#x20;Trimmer

這個 node 會修剪線條與形狀的可見長度，讓你隨時間顯示、隱藏或製作動畫。

* **Offset** – 控制形狀可見部分的起始位置。即使 _Trim Size_ 為 0%，將 Offset 從 0% 動畫到 100% 時，形狀會被畫出、在 50% 時完全可見，接著再次消失。
* **Trim Size** – 設定保留形狀的比例，以總長度百分比表示。
* **Loop** – 將形狀視為連續迴圈，因此結尾會接回開頭，而不是消失。
* **All Shapes** – 合併所有輸入形狀，並像單一路徑一樣進行修剪。若停用，則每個形狀會個別修剪。
* **Add Dot at Start / Add Dot at End** – 在修剪點加入所選顏色的點。（如果沒有套用修剪，就不會加入點。）
* **Colour** – 修剪點的顏色。_另請參閱_ [色彩設定與 HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – 選擇點所使用的 render profile。_請參閱_ [Render Profile](../fundamentals/render-profile.md)
