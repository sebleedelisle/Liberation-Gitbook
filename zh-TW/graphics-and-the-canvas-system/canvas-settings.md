---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-settings
---

# 🟩 Canvas settings

按一下左側工具列頂端的 _Canvas settings_ 按鈕，開啟 _Canvas settings_ 面板。

### Width and Height

使用這些可拖曳的滑桿，變更整個 Canvas 的整體寬度與高度。這些尺寸可以概略視為像素大小，但全部都是相對值。

雙擊滑桿即可輸入數值。

{% hint style="info" %}
這裡補充一點比較技術性的細節：雷射是相對於 Canvas 解析度移動，而不是相對於 zone 大小移動。這是因為 Canvas 中較大的 zone，在實際投影時通常也會對應到較大的區域。

這只是個小細節，對你來說可能不太需要在意，但它有助於讓各個 canvas zone 之間的效能與可見度更平均。
{% endhint %}

### Zone brightness

使用這個設定可調整粉紅色 zone 外框在 Canvas view 中顯示的亮度。這有助於讓內容更清楚，也能避免這個 view 看起來太雜亂。
