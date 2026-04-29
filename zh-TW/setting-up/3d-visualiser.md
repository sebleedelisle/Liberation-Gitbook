---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### 簡介

Liberation 的 3D visualiser 是非常實用的功能——即使完全沒有雷射，也能設計並調整你的演出！對我來說，這一直是非常有價值的工具，尤其是在使用大量雷射、設定特別複雜的場合。

### 在 3D 空間中導覽

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser view</p></figcaption></figure>

* 按住並拖曳可繞著環繞點旋轉視角
* 使用滑鼠滾輪可朝環繞點前進或後退
* 按住 shift 鍵並同時按住拖曳，可沿 XY 平面將 camera 向左、右、上、下平移（strafe）
* 在 visualiser 任意位置按兩下，可重設 camera 位置

### Settings

透過 _Window_ 選單開啟 _3D Visualiser Settings_ 面板。

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings 面板</p></figcaption></figure>

* **Visualiser size** - 調整 visualiser 相對於 app 其他部分的大小
* **Brightness Adjustment** - 調整雷射顯示的亮度
* **Show laser numbers** - 在每台雷射上方顯示對應編號
* **Show zone names** - 在每台雷射下方顯示對應的 zone 名稱

### Camera settings

這些設定主要與 3D 空間中的虛擬 camera 有關。你可以看到一個下拉選單，裡面有這些設定的 preset，可供儲存與重新載入。

* **Camera distance -** camera 會一直指向它的_環繞點_。Camera distance 是指 camera 與此點之間的距離。你也可以使用滑鼠滾輪調整這項設定。
* **FOV -** Field of view（視野）——決定 camera 的廣角程度或縮放程度。
* **Orbit position** - 描述目前繞著環繞點的旋轉狀態。第一個值是繞 X 軸的旋轉（pitch），第二個值是繞 Y 軸的旋轉（yaw）。
* **Orbit centre point** - 環繞點在 3D 空間中的位置，x、y、z。
* **Grid height** - grid 相對於「地面」的高度（也就是 y = 0 的位置）。

### Content settings

這些設定決定雷射（以及 Canvas）在 3D 環境中的放置位置。你可以看到一個下拉選單，裡面有這些設定的 preset，可供儲存與重新載入。

#### Lasers

每台雷射都有自己的設定群組，可以使用小白色三角形展開。

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiser 雷射設定</p></figcaption></figure>

* **3D Position** - 雷射的 x、y、z 位置。
* **3D Orientation** - 雷射繞 x、y、z 各軸的旋轉。
* **Flip X / Flip Y** - 翻轉雷射的虛擬輸出。注意，這通常不應該是必要的；若要修正硬體上的不一致，最好使用雷射的 flip / orientation 設定。
* **Output Range horizontal / vertical** - 與雷射 scanner 的最大／最小角度有關。60º 是標準值，但如果你的雷射不同，也可以自行調整。

#### Canvas

如果你使用 Canvas 系統，也可以選擇在 3D view 中包含 Canvas 影像。勾選核取方塊即可在其中顯示 Canvas，並使用位置、方向與縮放設定來決定它在 3D view 中的呈現方式。

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiser Canvas 設定</p></figcaption></figure>

{% hint style="info" %}
看到「幽靈」雷射嗎？3D Visualiser 和雷射設定在某種程度上是獨立的，因此 visualiser 中的雷射數量可能會比 Liberation 裡的雷射更多。當你將雷射新增到專案時，visualiser 內也會新增一個新的雷射物件。但如果你刪除一台雷射，visualiser 中仍會留下這個「幽靈」雷射物件。

若要移除所有幽靈雷射，請按一下 _Remove extra 3D laser objects_ 按鈕（位於 3D Visualiser settings 面板底部）。

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
