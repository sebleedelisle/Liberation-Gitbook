---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

將所有內容建立鏡像複本。預設鏡像軸是位於中間的垂直線。

* **angle** - 鏡像軸線的角度。
* **offset position** - 平移鏡像軸（以垂直於軸線的方向移動）
* **delay** - 鏡像內容的時間延遲。請注意，只有在內容帶有某種動畫時，這個設定才會有效果。

#### 3D 選項（選取 3D 時可用）

* **angle X / angle Y** - 鏡像軸會變成一個平面，你可以使用這些設定在 3D 中旋轉該平面。

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

以圓形排列方式複製內容。

* **radius** - 內容在旋轉前，從中心點位移的距離。
* **count** - 要建立的物件複本數量。
* **use each objects pivot point** - 選取後，每個元素會以自己的中心點為基準進行位移與旋轉。（只有在複製多個元素時才會有效果）
* **delay** - 為每個複製出的元素加入逐漸增加的時間延遲。請注意，內容需要帶有某種動畫，才會有明顯效果。
* **rotation** - 加到元素上的旋轉偏移量。

#### 3D 選項（選取 3D 時可用）

* **rotation x / rotation y** - 讓整個圓形排列繞 x 軸與 y 軸旋轉。

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

以列與欄組成的格狀排列方式複製內容。

* **spacing** - 元素之間的距離
* **count X**- 水平方向的複本數量（欄）
* **count Y**- 垂直方向的複本數量（列）
* **horizontal alignment** - 欄的起始位置：LEFT、CENTRE 或 RIGHT
* **vertical alignment** - 列的起始位置：TOP、MIDDLE 或 BOTTOM
* **delay** - 為每個複製出的元素加入逐漸增加的時間延遲。請注意，內容需要帶有某種動畫，才會有明顯效果。
