---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 路徑修改器

## &#x20;Dotter

此 node 會將線條及形狀內容取代為平均間距的點（現有的點不會改變）。

* **Colour** – 點的顏色。如已啟用 _Inherit Colour_，此設定會被忽略；詳見下方。_另請參閱_ [顏色設定及 HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – 點與點之間的距離，以像素計算。數值越小 = 點越多；數值越大 = 點越少。
* **Offset** – 以間距的百分比移動點的起始位置。可作動畫處理（例如配合鋸齒波 Oscillator Node），製作「行走中」的點效果。
* **Keep Original** – 啟用後會保留原本的線條／形狀，並在其上方繪製點。
* **Render Profile** – 選擇渲染質素。_請參閱_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – 自動調整間距，令路徑長度可被平均分割。
* **Fade Out Ends** – 在路徑的起點及終點附近逐漸降低點的亮度。當你用鋸齒波 Oscillator Node 為 **Offset** 製作動畫時很有用，因為點移到形狀末端時會平滑淡入／淡出。

## &#x20;Trimmer

此 node 會修剪線條及形狀的可見長度，讓你隨時間顯示、隱藏或製作動畫。

* **Offset** – 控制形狀可見部分的起點。即使 _Trim Size_ 為 0%，將 Offset 從 0% 動畫至 100% 亦會令形狀逐步繪出、在 50% 時完全可見，然後再次消失。
* **Trim Size** – 設定保留形狀的比例，以其總長度的百分比計算。
* **Loop** – 將形狀視為連續循環，因此終點會連回起點，而不是消失。
* **All Shapes** – 將所有輸入形狀合併，並視作單一路徑進行修剪。關閉時，每個形狀會獨立修剪。
* **Add Dot at Start / Add Dot at End** – 在修剪點加入所選顏色的點。（如果沒有套用修剪，則不會加入點。）
* **Colour** – 修剪點的顏色。_另請參閱_ [顏色設定及 HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – 選擇點的 render profile。_請參閱_ [Render Profile](../fundamentals/render-profile.md)
