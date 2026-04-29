---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ 快速入門指南

## 簡介

歡迎使用 **Liberation**——新一代激光表演軟件。

Liberation 是功能強大而複雜的現代軟件；它以易用性和可靠性為基礎，讓你可以自由發揮創意。它快速、高效而流暢；跟隨這份 _快速入門指南_，你很快就可以開始使用！

### 管理激光

Liberation 非常靈活，即使完全沒有連接實際激光，你也可以設定激光並進行視覺化。到你準備好實際輸出時，可以無縫地把每個 output 指派到 laser controller。

{% hint style="info" %}
你可以在 Liberation 內設定和視覺化任意數量的激光，授權級別（Hobbyist、Pro 等）只會限制你可以 _arm_ 的激光數量。這代表即使使用免費授權，你也可以設計包含 100 支激光的表演。只有在實際用真實激光運行時，你才需要升級。
{% endhint %}

預設設定是 8 支激光水平排列，但你可以按需要自訂。剛開始熟習軟件時，建議先保留這個預設；之後可以再調整至配合你的硬件設定。（請參閱 [設定你的專案](setting-up/setting-up-your-project.md)）

{% hint style="warning" %}
重要：在 arm 任何激光之前，請確保你了解相關風險，並仔細閱讀 [設定激光](setting-up/setting-up-lasers.md) 章節。
{% endhint %}

## 軟件概覽

### 安全停機

任何時候運行激光，你都必須準備好一個 **硬件緊急停止按鈕**（請參閱 [緊急停止 / 互鎖](hardware/emergency-stop-interlocks.md)）。如果你只想以較非緊急的方式停用所有輸出，可以使用 _**DISARM ALL**_ 按鈕，或按 `Escape` 鍵（或 APC40 上的 _**SESSION**_ 鍵）。你亦可以使用畫面上的滑桿，或 APC40 上的主 fader，降低全域亮度。

### 滑桿元素

Liberation 內有不同滑桿和控制項。

{% hint style="info" %}
如果你需要比滑桿更精確的控制，可以 `Cmd / Ctrl`-click 滑桿以輸入新數值。
{% endhint %}

### 鍵盤快捷鍵

完整鍵盤快捷鍵列表可在此查看：[鍵盤快捷鍵](reference/keyboard-shortcuts.md)

### 畫面配置

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
不確定某個按鈕有甚麼作用？把滑鼠移到按鈕上，就會顯示說明！
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menu 是你可以找到所有檔案匯入／匯出選項，以及開啟各個 panel 的地方。你亦可以在這裡用你的訂閱授權此電腦（在 _Liberation -> Authorise/Deauthorise this computer_）。

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

常用功能都可以在這裡找到，例如 arm／disarm 所有激光、全域亮度、test pattern，以及在 3D、Canvas 和 Output view 之間切換。

### Views

畫面左上方的大區域可以顯示 3 個主要 view 之一：**3D**、**CANVAS** 和 **OUTPUT**。你可以用 icon bar 按鈕切換它們（或使用 `Tab` 鍵在 3D 和 OUTPUT view 之間切換，然後繼續逐一切換每個 laser output）。

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view 會顯示你的激光看起來的效果，並可設定成配合你自己的激光配置。按住並拖曳可旋轉 camera，使用滑鼠滾輪可向前或向後移動。你可以在 _3D Visualiser settings_ panel（_View -> 3D Visualiser Settings_）找到更多選項。請參閱 [3D Visualiser](setting-up/3d-visualiser.md)。

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view 用於為每支激光設定 zones 和 masks。（留意左上角的巨大數字，方便你清楚知道目前正在查看哪一支激光！）

這個 view 代表該激光的完整 output，以及每個 zone 在其中的位置。預設每支激光只有一個 zone，但你可以在合理可行範圍內加入任意數量的 zones，並會在此 view 看到全部 zones。

{% hint style="info" %}
**甚麼是 zone？**

Zone 是激光 output 內的一個空間，你可以把 laser content 指向其中。每支激光亦可以有多於一個 zone。最簡單的 zone 類型是 _beam_ zone，但亦有 _canvas_ zones 和 _DMX_ zones。本指南主要集中介紹 beam zones，它們通常用於在空氣中製作 atmospheric beam effects。
{% endhint %}

你可以使用以下方式選擇要編輯的激光：

* 上方列中的編號按鈕
* 按下你想選擇的激光編號鍵 _（1-9 鍵）_
* 使用 `Tab` 鍵逐一循環切換

按 _+_ 按鈕可把新激光加入設定。（_Laser Overview_ panel 內亦有 _ADD LASER_ 按鈕）

在 _Laser Overview_ panel 中按紅色 ⊖ 按鈕，可從設定中刪除一支激光。

你可以用滑鼠滾輪放大和縮小；在沒有 zone 的地方按住並拖曳，可移動畫面。

按一下 zone 可選取它，然後用滑鼠調整其角點。拖曳角點時按住 `Alt / Option` 鍵，可作非等比例調整。右鍵點擊 zone 可查看更多選項，包括更改 zone 類型。

左側有一列圖示按鈕，把滑鼠移到任何按鈕上即可看到其功能說明。這些按鈕可讓你加入 beam zones、canvas zones 和 masks。這裡亦有選項可只為這支激光設定 test pattern，以及 grid 和 snapping 設定。

更多詳情請參閱 [Output 視圖／Zones](output-view/)。

#### Canvas

Canvas 系統主要用於圖像和建築 mapping。你可以把複雜圖像分佈到多支激光上，並對每個部分作 perspective correction。請參閱 [圖像與 Canvas 系統](graphics-and-the-canvas-system/)。

### APC40 MIDI controller

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

雖然你可以用滑鼠和鍵盤控制 Liberation，但使用 APC40 MIDI control interface 會好得多（Mark 2 最佳，Mark 1 亦可使用）。

另請參閱：[APC40 參考](reference/apc40-reference.md)

我們現在亦已加入對 APC Mini Mark 2 和 MIDI Fighter Twister 的支援，更多控制器正在開發中。不過在大多數情況下，APC40 Mark 2 仍然是最佳選擇。

### Clips 和 effects

{% hint style="info" %}
**甚麼是 clip？**

Clip 是 Liberation 內任何 laser content 的容器。Clips 可以包含 beams 或 graphical animations，通常會以循環方式播放。它們可以指向任何 zone（或 _Canvas target area_），並透過 clip deck 內的 clip buttons 觸發。
{% endhint %}

#### Clip deck overview

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

這個 grid 稱為 _clip deck_，是所有 laser clips 的存放位置。它設計成可直接對應 APC40 上 8 x 5 的按鈕 grid。

**瀏覽 clip deck。**

你可以使用以下方式左右捲動 clip deck：

* 左右方向鍵。加入 `Cmd / Ctrl` 可一次捲動一整頁。
* Trackpad：Swipe
* Mouse：如果你的滑鼠支援橫向捲動，把滑鼠移到 clip deck 上方時即可使用
* APC40 scroll knob
* APC40 _<- DEVICE ->_ 按鈕

為了幫助你掌握位置，上方有一個 clip deck 的 mini visualiser。另請參閱 [Clips 及 Clip Deck](clips/)

#### 開始和停止 clips

按下 clip button（使用滑鼠或 APC40）即可啟動 clip。再次按下即可停止。當你啟動一個 clip 時，所有同色的其他 clips 都會自動停止，除非你按住 _shift_。

部分 clips 會處於 _Flash mode_（預設為紅色 clips），這種情況下，當你放開 clip button 時它們會立即停止。

_STOP_ 按鈕會停止所有目前正在播放的 clips。

#### 設定 clip 的 output zones

在 clip buttons 下方，你會看到 zone buttons，預設為 beam zones 1 至 8（_BEAM 1_、_BEAM 2_ 等）。Zone buttons 會亮起，顯示哪些 zones 已指派給目前選取的 clip。

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

在 zone buttons 下方兩行，你會看到 X/Y flip buttons；切換它們可水平和垂直翻轉 clip。

{% hint style="info" %}
請注意，這些 zone 分配和 X/Y flip 設定是連接到 clip 本身；下次你運行該 clip 時仍會保留。它們不是全域設定。
{% endhint %}

右鍵點擊 clip 可編輯更多 clip 設定。另請參閱 [Clip 設定](clips/clip-settings.md)

### Groups

你會留意到每個 clip 都有彩色外框，而這個顏色代表它所屬的 _group_。APC40 的 clip buttons 亦會以這個顏色亮起。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>青色</td></tr><tr><td>Group 2</td><td>橙色</td></tr><tr><td>Group 3</td><td>紅色</td></tr><tr><td>Group 4</td><td>靛藍色</td></tr><tr><td>Group 5</td><td>綠色</td></tr></tbody></table>

Group 系統非常靈活，可讓你：

* 讓某個 group 內的 clips 繼續播放，同時切換另一個 group
* 快速為同一 group 內所有 clips 指派 zones 和 X/Y flips
* 為 clip 設定 _Flash mode_（Group 3 預設設為 _Flash mode_）

Groups 亦有 transition in/out 設定，可由其 clips 繼承，或被覆寫。

你可以用右鍵選單中的按鈕指派 clip 的 group；或者使用 APC40 時，按住 group button，並在 _仍然按住它的時候_ 按下 clip buttons。

更改同一 group 內所有 clips 的 zone 設定

使用 APC40 時，按下 group button，然後在 _仍然按住它的時候_ 使用 zone 和 X/Y buttons，為該 group 內所有 clips 切換 zone 設定。

另請參閱 [Clip 群組](clips/groups.md)

### Effects

Liberation 的 effects 系統是一個功能強大且靈活的方式，可即時改變 clip output。預設 effects buttons 1-8 位於 zone buttons 下方。

#### 套用 effect

按下 effect button 可切換 effect；更好的方法是使用 APC40 sliders 1-8 來淡入淡出 effects。

#### Effect parameters

使用 rotary controllers 1-8\* 調整每個 effect 的 _parameter_。（或者你可以用滑鼠右鍵調整 level 和 parameter）。Parameter 的變化會視乎 effect 的設定而有不同作用。以下列表說明預設 effects。

{% hint style="info" %}
Effect buttons 上的小數字代表 effect 的 _level_ 和 _parameter_。_level_ 由 APC40 上的 fader 控制，或者你可以在按鈕上 click-drag。Parameter 則由 APC40 上的 rotaries 調整，或者你可以用滑鼠右鍵調整。
{% endhint %}

_\*Rotary controllers 1-8 位於 APC40 Mk2 的頂部，以及 Mk1 的右上方。另請參閱：_ [APC40 參考](reference/apc40-reference.md)

#### 預設 effects

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**：\
   對 clip output 套用混亂的移動。Parameter 會調整混亂程度／速度。
2. **Sine wave**：\
   以移動的 sine wave 扭曲所有內容。Parameter 會調整 wavelength。
3. **Rotation**：\
   讓所有內容旋轉。Parameter 會調整旋轉速度。
4. **Horizontal flip**：\
   水平方向壓縮和拉伸所有內容。Parameter 會調整速度。
5. **Scale**：\
   反覆把所有內容由完整大小縮放至零。Parameter 會調整速度。
6. **Hue**：\
   改變所有內容的 hue，但不改變 saturation（即白色內容仍會保持白色）。Parameter 會調整 hue。
7. **Saturation and hue**：\
   改變所有內容的 hue，並把顏色完全飽和（即白色內容會變成該顏色）。Parameter 會調整 hue。
8. **Flash**：\
   反覆把所有內容的亮度由完整亮度閃至零。Parameter 會調整 flash 速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部一行還有另外 16 個 colour effects，可套用預設 hue 和 saturation 值。

請注意，這些是預設 effects，但你可以編輯它們，幾乎做到任何你想要的效果！

#### 甚麼是 _「目前選取的 clip」_？

當你啟動一個 clip，它會亮起表示正在運行。它亦會有白色外框，表示這是目前選取的 clip。每當你切換 zone buttons 或調整 clip settings，這些操作都會套用到 _目前選取的 clip_。

{% hint style="info" %}
如要在不觸發 clip 的情況下選取它，請在按 clip button 前先按住 `Alt / Option` 鍵。這是調整其 zones 和其他設定而不運行它的好方法。
{% endhint %}

### Clip settings panel

使用 _Clip Settings_ panel 可編輯 scaling、X/Y position，並存取功能強大的 zone delay 系統。

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global settings panel

使用 _Global Settings_ panel 可調整影響所有 zones 中所有 output 的全域 output 設定。

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

開啟 AUTO RESET 後，每當沒有 clips 正在播放，就會自動重設所有 _Global settings_。

### Timing

幾乎所有激光演出都有某種音樂聲軌，因此 Liberation 的 timing 系統以每分鐘拍數（beats per minute）的 tempo 為基礎。在 _Tempo Panel_ 中，你可以看到時間的表示方式；每個方格代表一拍，並會按拍子閃動。

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

系統提供多種同步選項，包括 MIDI clock 和 Ableton Link。如果你知道音樂的 tempo，可以用畫面上的滑桿或 APC40 Tempo knob 手動調整；你亦可以使用 _Tap Tempo_ 系統\_，\_跟隨音樂節拍。

#### Tap Tempo

_Tap Tempo_ 是音樂應用程式中常用的術語，讓你在音樂播放時按著節拍 tap 來設定 tempo。你可以使用畫面上的按鈕，不過建議使用 _T_ 鍵或 APC40 上的 _Tap Tempo_ 按鈕（如果你喜歡，甚至可以使用 foot switch）。

按 _R_ 鍵或 _Metronome_ 按鈕（APC40）可把 tempo 重設到小節開頭。

按 _Y_ 鍵或轉動 _Tempo_ knob（APC40），可把 tempo 四捨五入至整數。這對電子音樂很有用，因為其每分鐘拍數通常是整數。

### 整理你的 clip deck

如要在 clip deck 上移動 clip，按住並拖曳它到新位置。拖曳時，你可以使用游標鍵（或 APC40 上的 scroll wheel／buttons）左右捲動。

拖曳時按住 `Alt / Option` 鍵可建立副本。

`Alt / Option`-click clip 可選取它而不啟動。

`Alt / Option + Shift`-click clip 可多重選取，或在 clip 外按住並拖曳以用「lasso」方式選取。

按住並拖曳會拖曳所有已選取的 clips。

如要刪除一個或多個 clips，可以把它們拖離 clip deck（會出現垃圾桶圖示），或使用 clip 右鍵選單中的 DELETE 按鈕。

### Laser overview panel

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser overview panel_ 可讓你快速查看目前正在運行的激光狀態。右方的綠色方格表示 laser controller 狀態正常。如果變成橙色，代表偶爾有 drop-outs；如果變成紅色，代表已斷線。如果是灰色，代表完全未連接到 controller。

中間的圖表是 frame length 的歷史記錄，右方數字是目前 frame rate。內容越複雜，frame rate 就會越慢（即更容易閃爍）。低於約 25fps 時，看起來就會開始有點閃。

### 連接到激光——Controller Assignment panel

按 _Assign Laser Controllers_ 按鈕可開啟 _Controller Assignment_ panel。（你亦可以透過 menu bar 的 _View -> Controller Assignment_ 存取此 panel）。

你可以在這裡選擇哪些 laser outputs 送到哪些 laser controllers。把右側列表中的 controllers 拖放到左側的 slots。你可以重新命名 controllers，使其名稱與配對的激光一致（使用 pen icon button）。

更多詳情請閱讀 [控制器指派](setting-up/controller-assignment.md) 章節。

{% hint style="danger" %}
在 arm 任何激光之前，請務必閱讀 [設定激光](setting-up/setting-up-lasers.md)章節。
{% endhint %}

### Laser output panel

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

此 panel 顯示 _目前選取的激光_（由頂部數字表示）的設定。你可以使用 _tab_ 鍵、按數字鍵、在 _Laser Overview_ panel 中按激光編號，或在 _output view_ 中按激光編號，來更改目前選取的激光。

* **Number button** arm 和 disarm 該激光；如果是紅色，代表該激光已 armed。
* **Brightness** 獨立於其他激光調整此激光亮度（並會與 _global brightness_ 設定相乘——即如果兩者都是 50%，你的激光會是 25%）。
* **Test Pattern** 只為這支激光開啟 test pattern（會覆寫全域 test pattern 設定）
* **Orientation** 修正側掛或倒掛激光的方向。
* **Flip Horizontal and Flip Vertical** 反轉激光 output。對修正接線不一致的激光 output 很有用。
* **Copy Laser Settings** 開啟一個 panel，讓你把這支激光的各種設定複製到其他激光。

### Scanner settings

演出用激光的工作方式，是把單一 laser beam 以極高速移動，並不斷開關光束來在空氣中繪畫形狀。你看到的線條、形狀和圖像，其實是光束以快過眼睛可追蹤的速度描繪路徑。

Point stream 是告訴激光下一步移到哪裡，以及光束何時開關的資料。在 Liberation 中，clips 會在送到激光時即時轉換成這個 point stream。

Liberation 讓你詳細控制這個 point stream 的生成方式，使你可以為每支激光平衡流暢度、亮度和效能。

{% hint style="info" %}
如果你習慣使用依賴預先計算 point streams 的舊式激光軟件，這種方式起初可能會感覺不同。不過，即時 point generation 讓同一份內容可以針對每支激光作不同優化。當多支激光有不同 scanner 速度或質素時，這樣會更容易處理，無需複製或重建內容。它亦令 clip 檔案非常細小，這就是整個預設 Liberation clip deck 只有幾 MB，而不是幾 GB 的原因。
{% endhint %}

基本 scanner settings 包括：

* **Speed** 是 scanner speed，即激光移動繪畫形狀的速度。這相當於傳統激光軟件中的 point rate 調整，但在 Liberation 中，你可以 _獨立於 point rate_ 更改激光移動速度。你通常不需要調整它。
* **Scanner sync**（有時稱為 _blank shift，以前稱為 Colour Shift_）Scanners 會非常快速地移動激光，但亮度和顏色的變化通常會與移動不同步。這會在 beams 和 lines 邊緣出現細小閃爍的光「尾巴」。使用此調整可令移動和顏色彼此同步。請參閱 [Laser 設定](setting-up/laser-settings.md)

其他進階 scanner settings 會在 [進階](advanced/)章節中說明。

### Zoning

有關設定和 zoning 激光的完整指南，請參閱：[設定激光](setting-up/setting-up-lasers.md)
