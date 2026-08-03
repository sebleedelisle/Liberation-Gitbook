---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas 目標區域

我們已經知道如何將 Canvas 的部分內容送到每部 laser 內的 zone，但要先將內容放入 Canvas，你會需要使用（名稱有點令人混淆，但其實很準確的）_Canvas 目標區域_。

_Canvas 目標區域_ 是 Canvas 上可用來繪製 Clip 的區段，在 _CANVAS_ view 中會以藍色外框矩形表示。

很多時候你可能只需要一個 Canvas 目標區域，然後再將它分割成多個 zone，送往不同的 laser。

有時你亦可能想為建築物的不同部分使用多個 Canvas 目標區域，或者利用它們之間的 zone delay。（沒錯！Zone delay 在不同 Canvas 目標區域之間仍然有效！）

### 將 Clip 送到 Canvas 目標區域

如果你查看 Clip Deck，在 beam zone 按鈕旁邊會看到 Canvas 目標區域按鈕。你可能需要捲動 output 按鈕才看得到它們；可以使用 `Shift + Left / Right Arrow`、畫面上的 ZONE PAGE 按鈕，或 APC40 按鈕（見 [APC40 參考](../reference/apc40-reference.md)）。

指定 Clip 到 Canvas 目標區域的方法，與使用 beam zone 按鈕完全相同，只需切換這些按鈕即可。

### 新增／編輯 Canvas 目標區域

在頂部選單列選擇 _View -> Canvas Target Areas_，你會看到專案中每個 Canvas 目標區域的所有設定。

最上方有 _ADD CANVAS TARGET AREA_ 按鈕。

使用帶有減號的紅色按鈕刪除 Canvas 目標區域。

使用滑桿調整大小和位置。雙擊滑桿可輸入數值。

### Scale mode

* **FIT TO AREA** - 將內容縮小至完整置入 Canvas 目標區域內，同時保持長寬比。（這是預設設定）
* **FILL AREA** - 將內容拉伸以填滿 Canvas 目標區域，同時保持長寬比。內容可能會在邊緣被裁切。
* **STRETCH TO FIT** - 將內容拉伸至填滿整個 Canvas 目標區域，忽略長寬比。
