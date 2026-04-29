---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

在大多數專案中，你最常使用的 zone 類型會是 _Beam zone_。這是專為空氣中的光束效果設計的 zone。另一種 zone 類型是 _Canvas zone_（請參閱 [圖形與 Canvas 系統](../graphics-and-the-canvas-system/)）。

{% hint style="danger" %}
**警告 - 雷射運作中移動 zone 時請務必格外小心**，並將亮度調到最低。請參閱 [設定雷射](../setting-up/setting-up-lasers.md)，了解如何安全地啟用雷射並設定 zones 的完整指南。
{% endhint %}

你可以用滑鼠點擊並拖曳 zones 來移動它們。開啟 test pattern，就能看到該 zone 會輸出到哪裡。

{% hint style="info" %}
使用方向鍵可以**微調**目前選取的 zone/點。按住 `Shift` 鍵可用較大的步距微調。
{% endhint %}

{% hint style="info" %}
小技巧：你可以快速將 zone 設定複製到多台雷射！請參閱 [複製雷射設定](../setting-up/copy-laser-settings.md)
{% endhint %}

### 新增 beam zone

點擊工具列上方的 _Add a new beam zone_ 按鈕，就會出現新的 zone。請注意，beam zones 會依照你新增的順序排序，但你可以重新排序。請參閱 [重新排序 beam zones](re-ordering-beam-zones.md)

### 新增現有的 canvas zone

點擊 _Add existing canvas zone_ 按鈕後，你會看到可用的 canvas zones 清單，並可以針對這台雷射切換它們的開關。請參閱 [圖形與 Canvas 系統](../graphics-and-the-canvas-system/)

### Zone 形狀類型

共有 3 種 zone 形狀類型：

* **Quad** - 預設的矩形 zone 形狀，可以是規則矩形（與座標軸對齊）或變形。最適合較大的矩形 zones，或需要透視校正的 canvas zones。
* **Line/Curve** - 由 2 個以上的點和厚度定義的 zone。非常適合細長 zones，或用來限制輸出到陽台、橋梁或其他曲線形狀上。
* **Segmented** - 可細分成較小四邊形的 zone。非常適合建築投影對位。

在任何 zone 上按右鍵即可開啟其設定。你可以在這個右鍵選單中：

* 重新命名 zone（這有助於在 clip deck 中辨識，尤其是 zones 很多的時候！）
* 啟用/停用 zone
* 鎖定其位置
* 變更其形狀類型
* 重設為預設位置
* 存取該形狀類型專屬的設定
* 刪除它
* 新增 _Alt Zone_（請參閱 [Alt Zone 系統](alt-zone-system.md)）

{% hint style="danger" %}
**警告 -** 雷射啟用時變更 zone 類型請務必非常小心。zone 會回到該形狀上次使用的位置/大小，因此輸出可能會突然改變。變更 zone 類型前，最好先關閉雷射。
{% endhint %}

### Quad zone 形狀

你可以用滑鼠移動 quad 的每個角。對角落按 `Alt / Option`-click，可讓該角獨立於其他角移動並讓 quad 變形。quad 一旦變形後，所有角都可以自由移動。

你可以使用右鍵選單中的 _REMOVE DISTORTION_ 按鈕移除變形，並讓它回到與座標軸對齊的矩形。

#### 透視校正

這個選項可用右鍵選單中的切換按鈕設定，用來決定變形方法。用於光束時最好保持關閉；但如果這個 zone 是將圖形投射到平面上，請將它開啟，輸出就會套用透視校正。

{% hint style="info" %}
如果 _Perspective correction_ 關閉，內容會使用_雙線性插值_進行變形。換句話說，內容會平均分布在整個 quad 上。這就是它最適合光束的原因。

開啟透視校正後，內容會使用透視變形來調整縮短效應。因此，如果你以斜角將圖形投射到牆面上，可以用這個功能校正輸出並修正投影變形。
{% endhint %}

### Line / Curve zone 形狀

Line / Curve zone 形狀已經成為我最近演出中的首選，也可以說它其實應該成為 beam zones 的預設選項。

很多時候，我的 zones 必須很細，才能塞進場館中尷尬的狹窄空間，或是建築物窗戶之間的區域。我發現當 quad 的四個角彼此非常靠近時，要調整它們會變得非常麻煩。因此 Line / Curve zone 就誕生了！

如果是直線，你只需要兩個點，然後在右鍵選單中調整 _Zone thickness_。這是建立簡單 zones 最快的方式。

在直線上按 `Alt / Option`-click 可建立更多點。這些點會自動平滑化，形成流暢的形狀，你也可以調整 _Smooth level_ 來消除任何不順的折角。

在某個點上按 `Alt / Option`-click 可刪除該點。

或者，如果你熟悉向量繪圖軟體（Inkscape、Illustrator 等），可以使用 _Manually adjust bezier curves_ 選項，細部調整所有控制點。

### Segmented zone 形狀

這個細分 zone 可讓你進行非常精細的校正，適合用於映射到複雜形狀上。你可以使用右鍵選單中的 + 和 - 按鈕新增或移除細分。

### 如何編輯被另一個 zone 完全覆蓋的 zone

在上方的 zone 上按右鍵，然後點擊鎖頭按鈕將它鎖定。接著你應該就能編輯並調整下方的 zone。

<br>

{% hint style="info" %}
將 Beam zone 新增到 Output 後，它就可以加入 clip deck 中的 clip。
{% endhint %}
