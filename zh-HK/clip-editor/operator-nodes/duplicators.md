---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

為所有內容建立鏡像複本。預設情況下，鏡像軸是位於中間的垂直線。

* **angle** - 鏡像軸線的角度。
* **offset position** - 平移鏡像軸（以垂直於軸線的方向移動）
* **delay** - 鏡像內容的時間延遲。請注意，只有在內容包含某種動畫時，此設定才會有效果。

#### 3D 選項（選取 3D 時可用）

* **angle X / angle Y** - 鏡像軸會變成一個平面，你可以使用這些設定在 3D 中旋轉該平面。

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

以圓形圖案複製內容。

* **radius** - 內容在旋轉前，從中心點平移的距離。
* **count** - 要建立的物件複本數量。
* **use each objects pivot point** - 選取後，每個元素會圍繞自身中心點平移及旋轉。（只有在複製多個元素時才會有效果）
* **delay** - 為每個複製出來的元素加入逐步增加的時間延遲。請注意，內容需要包含某種動畫，此設定才會有明顯效果。
* **rotation** - 加到元素上的偏移旋轉。

#### 3D 選項（選取 3D 時可用）

* **rotation x / rotation y** - 圍繞 x 軸及 y 軸旋轉整個圓形圖案。

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

以列與欄組成的網格圖案複製內容。

* **spacing** - 元素之間的距離
* **count X**- 水平方向的複本數量（欄）
* **count Y**- 垂直方向的複本數量（列）
* **horizontal alignment** - 欄的起始點：LEFT、CENTRE 或 RIGHT
* **vertical alignment** - 列的起始點：TOP、MIDDLE 或 BOTTOM
* **delay** - 為每個複製出來的元素加入逐步增加的時間延遲。請注意，內容需要包含某種動畫，此設定才會有明顯效果。
