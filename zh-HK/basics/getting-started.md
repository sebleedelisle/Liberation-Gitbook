# ✅ 快速入門指南

## 簡介

歡迎使用 **Liberation** —— 新一代雷射表演軟件。

Liberation 是功能強大而複雜的現代軟件；它以易用性和可靠性為基礎，讓你能自由發揮創意。它快速、高效而流暢；跟隨這份_快速入門指南_，你很快就可以開始使用！

### 管理雷射

Liberation 具備足夠彈性，即使完全沒有連接實體雷射，你也可以設定雷射並進行視覺化預覽。當你準備好正式輸出時，就可以順暢地把每個 output 指派到雷射控制器。

{% hint style="info" %}
你可以在 Liberation 內設定和預覽任意數量的雷射，授權級別（Hobbyist、Pro 等）只會限制你可以 _arm_ 的雷射數量。這代表即使使用免費授權，你也可以設計包含 100 部雷射的表演。只有到真正要在實體雷射上運行時，才需要升級。
{% endhint %}

預設設定有 8 部雷射以水平方式排列，但你可以按需要自訂。剛開始熟悉軟件時，建議先保留這個預設；之後再調整至配合你的硬件設定。（請參閱[設定你的專案](../setting-up/setting-up-your-project.md)）&#x20;

{% hint style="warning" %}
重要：在你 arm 任何雷射之前，請先確保你了解相關風險，並仔細閱讀[設定雷射](../setting-up/setting-up-lasers.md)章節。
{% endhint %}

## 軟件概覽

### 安全關閉

任何時候運行雷射，都必須備有**硬件緊急停止按鈕**（請參閱[緊急停止互鎖](../hardware/emergency-stop-interlocks.md)）。但如果你只是想以較不緊急的方式 disarm 所有項目，可以使用 _**DISARM ALL**_ 按鈕，或按 `Escape` 鍵（或 APC40 上的 _**SESSION**_ 鍵）。你亦可以使用畫面上的 slider，或 APC40 的 main fader，降低全域亮度。

### Slider 元件

Liberation 內有各種 slider 和控制項。

{% hint style="info" %}
如果你需要比 slider 更精確的控制，可按住 `Cmd / Ctrl` 並點擊 slider，然後輸入新的數值。
{% endhint %}

### 鍵盤快捷鍵

完整鍵盤快捷鍵列表可在此找到：[鍵盤快捷鍵](../reference/keyboard-shortcuts.md)

### 畫面佈局

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
不確定某個按鈕有甚麼作用？把滑鼠移到按鈕上方，即可查看說明！
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menu 內可找到所有檔案匯入／匯出選項，以及開啟各個 panel 的選項。你亦可以在這裡使用訂閱授權此電腦（在 _Liberation -> Authorise/Deauthorise this computer_）。

#### Icon bar

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

常用工作都可在這裡找到，例如 arm／disarm 所有雷射、全域亮度、test pattern，以及在 3D、Canvas 和 Output view 之間切換。

### Views

畫面左上方的大區域可以顯示 3 個主要 view 之一：**3D**、**CANVAS** 和 **OUTPUT**。你可以使用 icon bar 按鈕切換（或使用 `Tab` 鍵在 3D 和 OUTPUT view 之間切換，之後繼續按 Tab 逐一切換每個 laser output）。

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view 會顯示你的雷射效果外觀，並可設定至配合你的雷射配置。點擊並拖曳可旋轉相機，使用滑鼠滾輪可向前／向後移動視角。你可在 _3D Visualiser settings_ panel（_View -> 3D Visualiser Settings_）找到更多選項。請參閱 [3D Visualiser](../setting-up/3d-visualiser.md)。

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view 用於為每部雷射設定 zones 和 masks。（留意左上角的大號數字，方便你清楚知道目前正在查看哪一部雷射！）

這個 view 代表該雷射的整個 output，以及每個 zone 在當中的位置。預設每部雷射只有一個 zone，但你可以在合理可行的範圍內加入任意數量的 zones，並會在此 view 中看到全部 zones。

{% hint style="info" %}
**甚麼是 zone？**

Zone 是雷射 output 內的一個空間，你可以把雷射內容導向其中。每部雷射可以有多於一個 zone。最簡單的 zone 類型是 _beam_ zone，但亦有 _canvas_ zones 和 _DMX_ zones。本指南主要集中於 beam zones，它們通常用於在空氣中建立大氣光束效果。
{% endhint %}

你可以用以下方式選擇要編輯的雷射：

* 上方列中的編號按鈕
* 按下你想選擇的雷射編號鍵 _（1-9_ keys\_）\_
* 使用 `Tab` 鍵逐一循環切換

按下 _+_ 按鈕可在設定中加入新雷射。（_Laser Overview_ panel 內亦有 _ADD LASER_ 按鈕）

在 _Laser Overview_ panel 內按紅色 ⊖ 按鈕，可從設定中刪除雷射。

你可以使用滑鼠滾輪放大及縮小，亦可在沒有 zone 的位置點擊並拖曳以移動畫面。

點擊 zone 可選取它，然後用滑鼠調整其角位控制點。拖曳角位時按住 `Alt / Option` 鍵，可令調整變為非等比例。在 zone 上按右鍵可查看更多選項，包括更改 zone 類型。

左側有一列 icon buttons；把滑鼠移到任何按鈕上方，即可查看其功能說明。這裡的按鈕可讓你加入 beam zones、canvas zones 和 masks。亦有選項可只為這部雷射設定 test pattern，以及 grid 和 snapping 設定。

更多詳情請參閱 [Output 視圖／Zones](../output-view/)。

#### Canvas

Canvas 系統主要用於圖形及建築投影映射。你可以把複雜圖像分配到多部雷射，並為每個部分進行透視校正。請參閱[圖形與 Canvas 系統](../graphics-and-the-canvas-system/)。

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

雖然可以使用滑鼠和鍵盤控制 Liberation，但使用 APC40 MIDI control interface 會好得多（Mark 2 最佳，但 Mark 1 亦可使用）。

另請參閱：[APC40 參考](../reference/apc40-reference.md)

我們現時亦已支援 APC Mini Mark 2 和 MIDI Fighter Twister，並正在開發更多支援。不過在大多數情況下，APC40 Mark 2 仍然是最佳選擇。&#x20;

### Clips 與 effects

{% hint style="info" %}
**甚麼是 clip？**

Clip 是 Liberation 內用來容納任何雷射內容的容器。Clips 可包含 beams 或圖形動畫，而且通常是一個循環播放的片段。它們可被導向任何 zone（或 _Canvas target area_），並透過 clip deck 內的 clip buttons 觸發。
{% endhint %}

#### Clip deck 概覽

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

這個格狀區域稱為 _clip deck_，是所有 laser clips 儲存的位置。它設計為可直接對應到 APC40 上的 8 x 5 按鈕格。

**瀏覽 clip deck。**

你可以用以下方式左右捲動 clip deck：

* 左右方向鍵。加上 `Cmd / Ctrl` 可一次捲動一整頁。
* Trackpad：Swipe
* Mouse：如果你的滑鼠支援橫向捲動，可在滑鼠停留於 clip deck 上方時使用
* APC40 scroll knob
* APC40 _<- DEVICE ->_ 按鈕

為方便你確認位置，頂部有一個 clip deck 的 mini visualiser。另請參閱 [Clips 及 Clip Deck](../clips/)

#### 啟動與停止 clips

按下 clip button（使用滑鼠或 APC40）即可啟動 clip。再按一次即可停止。當你啟動某個 clip 時，除非按住 _shift_，否則所有相同顏色的其他 clips 都會自動停止。

部分 clips 會處於 _Flash mode_（預設為紅色 clips），這些 clips 會在你放開 clip button 時立即停止。

_STOP_ 按鈕會停止所有目前正在運行的 clips。

#### 為 clip 設定 output zones

在 clip buttons 下方，你會看到 zone buttons；預設為 beam zones 1 至 8（_BEAM 1_、_BEAM 2_ 等）。Zone buttons 會亮起，以表示哪些 zones 已指派給目前選取的 clip。

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

在 zone buttons 下方兩行，你會看到 X/Y flip buttons；切換這些按鈕可水平和垂直翻轉 clip。

{% hint style="info" %}
請注意，這些 zone 分配和 X/Y flip 設定是連結到 clip 本身；下次運行該 clip 時仍會保留。它們不是全域設定。
{% endhint %}

在 clip 上按右鍵可編輯更多 clip 設定。另請參閱 [Clip 設定](../clips/clip-settings.md)

### Groups

你會留意到每個 clip 都有彩色外框，而這個顏色代表它所屬的 _group_。APC40 的 clip buttons 亦會以這個顏色亮起。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>群組 1</td><td>青色</td></tr><tr><td>群組 2</td><td>橙色</td></tr><tr><td>群組 3</td><td>紅色</td></tr><tr><td>群組 4</td><td>靛藍色</td></tr><tr><td>群組 5</td><td>綠色</td></tr></tbody></table>

Group 系統非常靈活，可讓你：

* 保持某個 group 內的 clips 繼續運行，同時切換另一個 group
* 快速為某個 group 內所有 clips 指派 zones 和 X/Y flips
* 為 clip 設定 _Flash mode_（Group 3 預設設定為 _Flash mode_）

Groups 亦有 transition in/out 設定，可由其 clips 繼承，或被覆寫。

你可以使用右鍵選單中的按鈕指派 clip 所屬 group；或使用 APC40，按住 group button，並在_仍然按住時_按下 clip buttons。

更改某個 group 內所有 clips 的 zone 設定

使用 APC40 時，先按下 group button，然後在_仍然按住時_使用 zone 和 X/Y buttons，切換該 group 內所有 clips 的 zone 設定。

另請參閱 [Clip 群組](../clips/groups.md)

### Effects

Liberation 的 effects 系統是一個強大而多用途的方式，可即時更改 clip output。預設 effects buttons 1-8 位於 zone buttons 下方。

#### 套用 effect

按下 effect button 可切換 effect；更好的做法是使用 APC40 sliders 1-8 淡入淡出 effects。

#### Effect parameters

使用 rotary controllers 1-8\* 調整每個 effect 的 _parameter_。（你亦可用滑鼠按右鍵調整 level 和 parameter）。Parameter 的改變會因 effect 的設定方式而有不同作用。預設 effects 請見下方列表。

{% hint style="info" %}
你在 effect buttons 上看到的小數字，代表該 effect 的 _level_ 和 _parameter_。_Level_ 由 APC40 上的 fader 控制，或你可以在按鈕上點擊並拖曳。Parameter 由 APC40 上的 rotaries 調整，或你可以按右鍵用滑鼠調整。
{% endhint %}

_\*Rotary controllers 1-8 位於 APC40 Mk2 頂部，或 Mk1 的右上方。另請參閱：_ [APC40 參考](../reference/apc40-reference.md)

#### 預設 effects

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**：\
   為 clip output 套用混亂的移動。Parameter 會調整混亂程度／速度。
2. **Sine wave**：\
   以移動中的 sine wave 扭曲所有內容。Parameter 會調整波長。
3. **Rotation**：\
   令所有內容旋轉。Parameter 會調整旋轉速度。
4. **Horizontal flip**：\
   令所有內容在水平方向壓縮和伸展。Parameter 會調整速度。
5. **Scale**：\
   重複把所有內容由完整大小縮放至零。Parameter 會調整速度。
6. **Hue**：\
   更改所有內容的 hue，但不改變 saturation（即任何白色內容仍保持白色）。Parameter 會調整 hue。
7. **Saturation and hue**：\
   更改所有內容的 hue，並把顏色完全飽和（即任何白色內容都會變成該顏色）。Parameter 會調整 hue。
8. **Flash**：\
   重複把所有內容的亮度由全亮閃爍至零。Parameter 會調整閃爍速度。

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一行另有 16 個 colour effects，可套用預設 hue 和 saturation 值。

請注意，這些只是預設 effects；你可以把它們編輯成幾乎任何想要的效果！

#### 甚麼是 _「目前選取的 clip」_？

當你啟動某個 clip 時，它會亮起以表示正在運行。它亦會有白色外框，表示這是目前_選取_的 clip。每當你切換 zone buttons 或調整 clip 設定時，這些操作都會套用到_目前選取的 clip_。

{% hint style="info" %}
如要在不觸發 clip 的情況下選取它，請在按下 clip button 前先按住 `Alt / Option` 鍵。這是調整其 zones 和其他設定而不運行它的好方法。
{% endhint %}

### Clip settings panel

使用 _Clip Settings_ panel 可編輯 scaling、X/Y position，並存取強大的 zone delay 系統。

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global settings panel

在 _Global Settings_ panel 中，可調整影響所有 zones 上所有 output 的全域 output 設定。

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

開啟 AUTO RESET 後，當沒有 clips 正在播放時，會自動重設所有 _Global settings_。&#x20;

### Timing

幾乎所有雷射展示都有某種音樂配樂，因此 Liberation 的 timing 系統以每分鐘拍數（beats per minute）的 tempo 為基礎。在 _Tempo Panel_ 中，你可以看到時間的表示方式；每個方格代表一拍，並會按節拍閃爍。

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

系統提供多種同步選項，包括 MIDI clock 和 Ableton Link。如果你知道音樂的 tempo，可以使用畫面上的 slider 或 APC40 Tempo knob 手動調整；亦可以使用 _Tap Tempo_ 系統\_，\_跟隨音樂節拍。

#### Tap Tempo

_Tap Tempo_ 是音樂 app 中常用的術語，讓你在音樂播放時按節拍點按，以設定 tempo。你可以使用畫面上的按鈕，不過建議使用 _T_ 鍵或 APC40 上的 _Tap Tempo_ 按鈕（如果你喜歡，甚至可以使用腳踏開關）。

按 _R_ 鍵或 _Metronome_ 按鈕（APC40），可把 tempo 重設到小節開頭。

按 _Y_ 鍵或轉動 _Tempo_ knob（APC40），可把 tempo 四捨五入為整數。這對於通常使用整數 BPM 的電子音樂很有用。

### 整理你的 clip deck

如要在 clip deck 上移動 clip，點擊並拖曳它到新位置。拖曳時，你可以使用方向鍵（或 APC40 上的 scroll wheel/buttons）左右捲動。

拖曳時按住 `Alt / Option` 鍵可建立副本。

`Alt / Option`-click clip 可在不啟動它的情況下選取它。

`Alt / Option + Shift`-click clip 可多重選取，或在 clip 以外位置點擊並拖曳，以「lasso」方式選取。&#x20;

點擊並拖曳會拖曳所有已選取的 clips。

如要刪除一個或多個 clips，可把它們拖離 clip deck（會出現垃圾桶圖示），或使用 clip 右鍵選單中的 DELETE 按鈕。

### Laser overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ 讓你快速查看目前正在運行的雷射狀態。右側的綠色方格表示雷射控制器狀態正常。如果變成橙色，代表偶爾有 drop-outs；如果變成紅色，代表已斷線。如果是灰色，則代表完全沒有連接到控制器。&#x20;

中間的圖表是 frame lengths 的歷史記錄，右側數字是目前 frame rate。內容越複雜，frame rate 就會越慢（即更容易閃爍）。低於約 25fps 的內容會開始看起來有點閃爍。&#x20;

### 連接到雷射 — Controller Assignment panel

點擊 _Assign Laser Controllers_ 按鈕可開啟 _Controller Assignment_ panel。（亦可透過 menu bar 中的 _View -> Controller Assignment_ 存取此 panel）。

你可以在這裡選擇哪些 laser outputs 會送到哪些 laser controllers。把右側列表中的 controllers 拖放到左側 slots。你可以重新命名 controllers，使其名稱配合所配對的雷射（使用筆形圖示按鈕）。

更多詳情請閱讀 [控制器指派](../setting-up/controller-assignment.md)章節。

{% hint style="danger" %}
在你 arm 任何雷射之前，請務必先閱讀[設定雷射](../setting-up/setting-up-lasers.md)章節。
{% endhint %}

### Laser output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

此 panel 會顯示_目前選取的雷射_設定（由頂部的數字表示）。你可以使用 _tab_ 鍵、按下數字鍵、點擊 _Laser Overview_ panel 中的雷射編號，或在 _output view_ 中點擊雷射編號，來更改目前選取的雷射。

* **Number button** arm 和 disarm 雷射；如果是紅色，代表該雷射已 armed。
* **Brightness** 獨立於其他雷射調整雷射亮度（並會與 _global brightness_ 設定合併計算——即如果兩者都是 50%，你的雷射會是 25%）。
* **Test Pattern** 只為這部雷射開啟 test pattern（會覆寫 global test pattern 設定）
* **Orientation** 校正側掛或倒置安裝的雷射。
* **Flip Horizontal and Flip Vertical** 反轉雷射 output。對於接線不一致的雷射，作 output 校正時很有用。
* **Copy Laser Settings** 開啟一個 panel，讓你把這部雷射的各種設定複製到其他雷射。

### Scanner settings

顯示用雷射的運作方式，是把單一雷射光束以極高速度移動，並開關光束以在空氣中繪畫形狀。你看到的線條、形狀和影像，其實是光束以快到眼睛追不上的速度描繪路徑。

Point stream 是告訴雷射下一步要移到哪裡，以及光束何時應該開啟或關閉的資料。在 Liberation 中，clips 會在送到雷射時即時轉換成這個 point stream。

Liberation 讓你詳細控制 point stream 的產生方式，讓你可以為每部雷射在流暢度、亮度和效能之間取得平衡。

{% hint style="info" %}
如果你習慣使用依賴預先計算 point streams 的舊式雷射軟件，這種方式一開始可能會覺得不同。不過，即時 point generation 可讓相同內容針對每部雷射作不同最佳化。這使你更容易同時使用 scanner speed 或品質不同的多部雷射，而不需要複製或重建內容。它亦令 clip 檔案非常細小，因此整個預設 Liberation clip deck 只有數 MB，而不是數 GB。
{% endhint %}

基本 scanner settings 包括：

* **Speed** 是 scanner speed，即雷射移動以繪畫形狀的速度。這相當於在傳統雷射軟件中調整 point rate，但在 Liberation 中，你可以_獨立於 point rate_ 更改雷射移動速度。你通常不需要調整這項。
* **Scanner sync**（有時稱為 _blank shift_，之前稱為 Colour Shift）Scanners 會非常快速地移動雷射，但亮度和顏色的變化通常會與移動不同步。這會在 beams 和 lines 邊緣顯示為細小閃爍的光「尾巴」。使用此調整可令移動和顏色彼此同步。請參閱 [Laser Settings](../setting-up/laser-settings/)

其他進階 scanner settings 會在[進階](../advanced/)章節中說明。

### Zoning

如需設定和 zoning 雷射的完整指南，請參閱：[設定雷射](../setting-up/setting-up-lasers.md)
