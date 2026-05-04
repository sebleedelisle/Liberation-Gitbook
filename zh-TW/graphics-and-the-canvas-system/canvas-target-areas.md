---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas 目標區域

我們已經知道如何把 Canvas 的一部分送進每台雷射的 zone；但要先把內容放進 Canvas，你會需要使用名稱有點容易混淆、但其實很精準的 _Canvas 目標區域_。

_Canvas 目標區域_ 是 Canvas 上可用來繪製 Clip 的區段，在 _CANVAS_ view 中會以藍色外框矩形表示。

很多時候你可能只需要一個 Canvas 目標區域，然後再把它分割成多個 zone，送到不同的雷射。

有時候，你也可能會想為建築物的不同部分使用多個 Canvas 目標區域，或利用它們之間的 zone delay。（沒錯！zone delay 在不同 Canvas 目標區域之間仍然有效！）

### 將 Clip 送到 Canvas 目標區域

如果你查看 Clip Deck，在 beam zone 按鈕旁邊會看到 Canvas 目標區域按鈕。你可能需要捲動 Output 按鈕才看得到它們；可以使用 `Shift + Left / Right Arrow`、畫面上的 ZONE PAGE 按鈕，或 APC40 按鈕（請參閱 [APC40 參考資料](../reference/apc40-reference.md "mention")）。

指派 Clip 到 Canvas 目標區域的方式，和使用 beam zone 按鈕完全相同：切換這些按鈕即可。

### 新增／編輯 Canvas 目標區域

在頂端選單列選擇 _View -> Canvas Target Areas_，你會看到專案中每個 Canvas 目標區域的所有設定。

最上方有 _ADD CANVAS TARGET AREA_ 按鈕。

使用帶有減號的紅色按鈕可刪除 Canvas 目標區域。

使用滑桿調整大小與位置。雙擊滑桿可輸入數值。

### 縮放模式

* **FIT TO AREA** - 將內容縮小到完整放入 Canvas 目標區域內，同時維持長寬比。（這是預設設定）
* **FILL AREA** - 將內容縮放到填滿 Canvas 目標區域，同時維持長寬比。內容可能會被邊緣裁切。
* **STRETCH TO FIT** - 將內容拉伸到填滿整個 Canvas 目標區域，不維持長寬比。
