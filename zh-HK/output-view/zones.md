---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones（區域）

在大部分項目中，你最常使用的 zone 類型是 _Beam zone_。這種 zone 是為空氣中的大氣光束效果而設計。另一種 zone 是 _Canvas zone_（請參閱[圖形與 Canvas 系統](../graphics-and-the-canvas-system/)）。

{% hint style="danger" %}
**警告 - Laser 運行時移動 zone 必須極度小心**，並將亮度調到最低。關於如何安全啟用 laser 及設定 zone，請參閱[設定 Laser](../setting-up/setting-up-lasers.md)的完整指南。
{% endhint %}

你可以用滑鼠點擊並拖曳 zone。開啟測試圖案即可查看該 zone 的投射位置。

{% hint style="info" %}
使用方向鍵可**微調**目前選取的 zone／控制點。按住 `Shift` 鍵可用較大的步幅微調。
{% endhint %}

{% hint style="info" %}
小貼士：你可以快速將 zone 設定複製到多部 laser！請參閱[複製 Laser 設定](../setting-up/copy-laser-settings.md)
{% endhint %}

### 新增 beam zone

點擊工具列頂部的 _Add a new beam zone_ 按鈕，新的 zone 便會出現。請注意，beam zone 會按新增次序排序，但你可以重新排列它們。請參閱[重新排序 Beam zone](re-ordering-beam-zones.md)

### 新增現有 canvas zone

點擊 _Add existing canvas zone_ 按鈕後，你會看到可用的 canvas zone 清單，並可為這部 laser 開啟或關閉它們。請參閱[圖形與 Canvas 系統](../graphics-and-the-canvas-system/)

### Zone 形狀類型

Zone 形狀共有 3 種：

* **Quad** - 預設的矩形 zone 形狀，可以是整齊對齊座標軸的矩形，也可以作變形。最適合較大的矩形 zone，或需要透視修正的 canvas zone。
* **Line/Curve** - 由 2 個或以上控制點及厚度定義的 zone。適合幼身 zone，或用於在露台、橋樑或其他曲線形狀上終止光束。
* **Segmented** - 可細分成多個較小 quad 的 zone。適合建築 mapping。

在任何 zone 上按右鍵即可開啟其設定。在此右鍵選單中，你可以：

* 重新命名 zone（這有助你在 clip deck 中識別它，特別是 zone 很多的時候！）
* 啟用／停用 zone
* 鎖定其位置
* 更改其形狀類型
* 重設為預設位置
* 存取該形狀類型專用的設定
* 刪除它
* 新增 _Alt Zone_（請參閱[Alt Zone 系統](alt-zone-system.md)）

{% hint style="danger" %}
**警告 -** Laser 啟用時更改 zone 類型必須非常小心。Zone 會回到該形狀上一次的位置／大小，因此輸出可能會突然改變。最好先關閉 laser，才更改 zone 類型。
{% endhint %}

### Quad zone 形狀

你可以用滑鼠移動 quad 的每個角。`Alt / Option`-點擊某個角，可將它獨立於其他角移動並令 quad 變形。Quad 一旦變形後，所有角都可以自由移動。

你可以使用右鍵選單中的 _REMOVE DISTORTION_ 按鈕移除變形，並將其還原為與座標軸對齊的矩形。

#### 透視修正

此選項可透過右鍵選單中的切換按鈕設定，並決定變形方式。用於 beam 時最好保持關閉；但如果此 zone 是將圖形投射到平面上，請開啟此選項，輸出便會作透視修正。

{% hint style="info" %}
如果 _Perspective correction_ 關閉，內容會使用 _bi-linear interpolation_ 進行變形。換句話說，內容會在 quad 內平均分佈。因此它最適合 beam。

開啟 perspective correction 後，內容會使用透視變形，並修正前縮效果。因此，如果你以斜角將圖形投射到牆上，可以用它來反變形輸出，修正投影失真。
{% endhint %}

### Line / Curve zone 形狀

Line / Curve zone 形狀已成為我最近演出中的首選，也可以說它其實應該成為 beam zone 的預設形狀。

很多時候，我的 zone 都要很幼，才能放進場地中狹窄難處理的位置，或建築物窗戶之間的空間。我發現當 quad 的四個角非常接近時，要調整它們會相當麻煩。因此 Line / Curve zone 就誕生了！

對於直線，你只需要兩個點，然後在右鍵選單中調整 _Zone thickness_。這是建立簡單 zone 最快的方法。

`Alt / Option`-點擊線段可新增更多控制點。這些控制點會自動平滑處理，形成流暢的形狀；你亦可以調整 _Smooth level_，修平任何突兀的位置。

`Alt / Option`-點擊控制點可將其刪除。

如果你熟悉向量繪圖應用程式（Inkscape、Illustrator 等），亦可以使用 _Manually adjust bezier curves_ 選項，讓自己精細調整所有控制點。

### Segmented zone 形狀

這種細分 zone 可讓你進行非常精細的修正，適合用於 mapping 到複雜形狀。你可以使用右鍵選單中的 + 和 - 按鈕新增或移除細分。

### 如何編輯被另一個 zone 完全覆蓋的 zone

在上方的 zone 上按右鍵，然後點擊掛鎖按鈕將其鎖定。現在你應該可以編輯和調整下方的 zone。

<br>

{% hint style="info" %}
只要將 Beam zone 加入你的輸出，它便可在 clip deck 中加入到 clip。
{% endhint %}
