---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### 簡介

Liberation 的 3D Visualiser 是非常實用的功能——即使完全沒有激光器，你也可以設計和微調表演！對我來說，它一直是非常有價值的工具，特別是在激光器數量多、設定十分複雜的場景。

### 在 3D 空間中導航

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser 視圖</p></figcaption></figure>

* 按住並拖曳，以軌道中心點為中心旋轉視圖
* 使用滑鼠滾輪，向軌道中心點前後移動
* 按住 shift 鍵同時按住並拖曳，可沿 XY 平面向左、右、上、下橫向移動相機（strafe）
* 在 visualiser 上任何位置雙擊，可重設相機位置

### 設定

透過 _Window_ menu 開啟 _3D Visualiser Settings_ panel。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings panel</p></figcaption></figure>

* **Visualiser size** - 更改 visualiser 相對於應用程式其他部分的大小
* **Brightness Adjustment** - 更改激光顯示的亮度
* **Show laser numbers** - 在每個激光器上方顯示相應編號
* **Show zone names** - 在每個激光器下方顯示相應 zone 名稱

### 相機設定

這些設定主要與 3D 空間中的虛擬相機有關。你會看到一個下拉選單，內有這些設定的 preset，可供儲存和重新載入。

* **Camera distance -** 相機會一直指向其 _Orbit point_。Camera distance 指相機與此點之間的距離。你亦可以使用滑鼠滾輪調整此設定。
* **FOV -** Field of view（視野）——決定相機的廣角程度／放大程度。
* **Orbit position** - 描述目前圍繞軌道中心點的旋轉。第一個數值是圍繞 X 軸的旋轉（pitch），第二個數值是圍繞 Y 軸的旋轉（yaw）。
* **Orbit centre point** - 軌道中心點在 3D 空間中的位置，x、y、z。
* **Grid height** - grid 相對於「地面」的高度（即 y = 0 的位置）。

### 內容設定

這些設定決定激光器（以及 Canvas）在 3D 環境中的放置位置。你會看到一個下拉選單，內有這些設定的 preset，可供儲存和重新載入。

#### 激光器

每個激光器都有自己的設定群組，可使用細小的白色三角形展開。

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiser 激光器設定</p></figcaption></figure>

* **3D Position** - 激光器的 x、y、z 位置。
* **3D Orientation** - 激光器圍繞 x、y、z 各軸的旋轉。
* **Flip X / Flip Y** - 翻轉激光器的虛擬輸出——注意，這通常不應該是必要的；較好的做法是使用激光器的 flip／orientation 設定，修正硬件之間的不一致。
* **Output Range horizontal / vertical** - 與激光器掃描器的最大／最小角度有關。60º 是標準值，但如果你的激光器不同，可以在此調整。

#### Canvas

如果你正在使用 Canvas system，也可以選擇在 3D view 中加入 Canvas 圖像。啟用剔選方格後，Canvas 會在其中顯示；然後使用位置、方向和比例設定，決定它在 3D view 中的外觀。

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiser Canvas 設定</p></figcaption></figure>

{% hint style="info" %}
看到「幽靈」激光器？3D Visualiser 與激光器設定在某程度上是獨立的，因此 visualiser 內的激光器數量可能會多於 Liberation 內的數量。當你在專案中加入激光器時，visualiser 內也會加入一個新的激光器物件。但如果你刪除激光器，visualiser 內仍會保留一個「幽靈」激光器物件。

如要移除所有幽靈激光器，請按一下 _Remove extra 3D laser objects_ button（位於 3D Visualiser settings panel 底部）。

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
