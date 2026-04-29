---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ 快速入門指南

## 簡介

歡迎使用 **Liberation** — 新一代雷射秀軟體。

Liberation 是功能強大且複雜的現代軟體；它以易用性與可靠性為基礎，讓你能自由發揮創意。它快速、高效率且流程順暢；跟著這份_快速入門指南_，你很快就能開始使用！

### 管理雷射

Liberation 非常彈性，即使沒有連接任何實體雷射，你也可以設定雷射並進行視覺化。等你準備好實際輸出時，再將每個輸出順暢地指派到雷射控制器即可。

{% hint style="info" %}
你可以在 Liberation 中設定並視覺化任意數量的雷射；授權方案（Hobbyist、Pro 等）只會限制你可以_啟用輸出_的雷射數量。也就是說，即使使用免費授權，你仍然可以設計包含 100 台雷射的雷射秀。只有在你要實際用真實雷射執行時，才需要升級。
{% endhint %}

預設配置會將 8 台雷射水平排開，但你可以依需求自訂。剛開始熟悉軟體時，建議先保留這個預設值；之後再調整成符合你的硬體配置。（請參閱[設定你的專案](setting-up/setting-up-your-project.md)）

{% hint style="warning" %}
重要：在啟用任何雷射輸出之前，請務必了解相關風險，並仔細閱讀[設定雷射](setting-up/setting-up-lasers.md)章節。
{% endhint %}

## 軟體概覽

### 安全關閉

只要你正在使用雷射，就必須隨手備有**硬體緊急停止按鈕**（請參閱[緊急停止與聯鎖](hardware/emergency-stop-interlocks.md)）。如果只是想以較不緊急的方式停用所有輸出，可以使用 _**DISARM ALL**_ 按鈕，或按 `Escape` 鍵（也可以按 APC40 上的 _**SESSION**_ 鍵）。你也可以使用畫面上的滑桿，或 APC40 的主推桿來降低 Global Brightness。

### 滑桿元件

Liberation 中有各種滑桿與控制項。

{% hint style="info" %}
如果需要比滑桿更精準的控制，可以在滑桿上按 `Cmd / Ctrl` + 點擊，直接輸入新的數值。
{% endhint %}

### 鍵盤快捷鍵

完整的鍵盤快捷鍵清單可在這裡找到：[鍵盤快捷鍵](reference/keyboard-shortcuts.md)

### 畫面配置

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
不確定某個按鈕的功能嗎？將滑鼠游標停在它上面，就會看到說明！
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menu 中可以找到所有檔案匯入／匯出選項，也可以用來開啟各個面板。你也可以在這裡使用訂閱授權這台電腦（位於 _Liberation -> Authorise/Deauthorise this computer_）。

#### Icon bar

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

常用工作都可以在這裡找到，例如啟用／停用所有雷射輸出、Global Brightness、Test Pattern，以及在 3D、Canvas 和 Output view 之間切換。

### Views

畫面左上方的大區域可以顯示 3 個主要 view 之一：**3D**、**CANVAS** 和 **OUTPUT**。使用 icon bar 按鈕在它們之間切換（也可以按 `Tab` 鍵在 3D 和 OUTPUT view 之間切換，接著繼續按 Tab 依序切換每個雷射輸出）。

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view 會顯示雷射看起來的樣子，並且可以設定成符合你自己的雷射配置。按住並拖曳可旋轉攝影機，使用滑鼠滾輪可向前或向後移動。你可以在 _3D Visualiser settings_ 面板中找到更多選項（_View -> 3D Visualiser Settings_）。請參閱 [3D Visualiser](setting-up/3d-visualiser.md)。

#### Output View

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view 用於設定每台雷射的 zones 和 masks。（注意左上角的大型數字，方便你清楚知道目前正在操作哪一台雷射！）

這個 view 代表該雷射的完整輸出範圍，以及每個 zone 在其中的位置。預設每台雷射只有一個 zone，但你可以依實際可行範圍新增多個 zones，並且會在這個 view 中看到它們。

{% hint style="info" %}
**什麼是 zone？**

zone 是雷射輸出中的一個空間，你可以將雷射內容導向其中。每台雷射也可以有多個 zones。最簡單的 zone 類型是 _beam_ zone，但也有 _canvas_ zones 和 _DMX_ zones。本指南主要會著重在 beam zones，通常用來在空氣中產生氣氛型光束效果。
{% endhint %}

你可以用以下任一方式選取要編輯的雷射：

* 使用頂端列中的編號按鈕
* 按下你要的雷射編號鍵（_1-9_ 鍵）
* 使用 `Tab` 鍵依序切換

按下 _+_ 按鈕可將新的雷射加入配置。（_Laser Overview_ 面板中也有 _ADD LASER_ 按鈕）

在 _Laser Overview_ 面板中按下紅色 ⊖ 按鈕，可從配置中刪除雷射。

你可以使用滑鼠滾輪放大與縮小；在沒有 zone 的任意位置按住並拖曳，可移動畫面。

點擊 zone 可選取它，接著用滑鼠調整它的角點。拖曳角點時按住 `Alt / Option` 鍵，可進行非等比例調整。在 zone 上按右鍵可查看更多選項，包括變更 zone 類型。

左側有一列圖示按鈕，將滑鼠游標停在任何按鈕上都可看到功能說明。這些按鈕可讓你新增 beam zones、canvas zones 和 masks。也有一些選項可只為這台雷射設定 Test Pattern，以及格線與吸附設定。

更多詳細資訊請參閱 [Output view](output-view/)。

#### Canvas

Canvas 系統主要用於圖形與建築投影對位。你可以將複雜影像分配到多台雷射上，並對每個區段進行透視校正。請參閱[圖形與 Canvas 系統](graphics-and-the-canvas-system/)。

### APC40 MIDI 控制器

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

雖然可以用滑鼠和鍵盤控制 Liberation，但使用 APC40 MIDI 控制介面會好很多（Mark 2 最佳，Mark 1 也可使用）。

另請參閱：[APC40 參考](reference/apc40-reference.md)

我們現在也已支援 APC Mini Mark 2 和 MIDI Fighter Twister，並且正在開發更多控制器支援。不過在大多數情況下，APC40 Mark 2 仍是最佳選擇。

### Clips 與效果

{% hint style="info" %}
**什麼是 Clip？**

Clip 是 Liberation 中用來裝載任何雷射內容的容器。Clips 可以包含光束或圖形動畫，通常會以循環方式播放。它們可以導向任何 zone（或 _Canvas target area_），並透過 Clip Deck 中的 Clip 按鈕觸發。
{% endhint %}

#### Clip Deck 概覽

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

這個格狀區域稱為 _Clip Deck_，所有雷射 Clips 都儲存在這裡。它的設計可直接對應到 APC40 上 8 x 5 的按鈕格。

**瀏覽 Clip Deck。**

你可以用以下方式左右捲動 Clip Deck：

* 左右方向鍵。加上 `Cmd / Ctrl` 可一次捲動一整頁。
* 觸控板：滑動
* 滑鼠：如果你的滑鼠支援橫向捲動，將游標停在 Clip Deck 上即可使用
* APC40 捲動旋鈕
* APC40 _<- DEVICE ->_ 按鈕

為了幫助你掌握位置，頂端有一個 Clip Deck 的迷你 visualiser。另請參閱 [Clips 與 Clip Deck](clips/)

#### 啟動與停止 Clips

按下 Clip 按鈕（用滑鼠或 APC40 都可以）即可啟動 Clip。再次按下可停止。當你啟動某個 Clip 時，除非按住 _shift_，否則所有相同顏色的其他 Clips 會自動停止。

有些 Clips 會處於 _Flash mode_（預設是紅色 Clips），這種情況下，只要你放開 Clip 按鈕，它們就會停止。

_STOP_ 按鈕會停止所有目前正在播放的 Clips。

#### 設定 Clip 的輸出 zones

在 Clip 按鈕下方，你會看到 zone 按鈕，預設為 beam zones 1 到 8（_BEAM 1_、_BEAM 2_ 等）。zone 按鈕會亮起，表示目前選取的 Clip 已指派到哪些 zones。

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

在 zone 按鈕下方兩列，你會看到 X/Y 翻轉按鈕；切換這些按鈕可將 Clip 水平或垂直翻轉。

{% hint style="info" %}
請注意，這些 zone 分配與 X/Y 翻轉設定是連結到 Clip 本身的；下次執行該 Clip 時會保留。它們不是全域設定。
{% endhint %}

在 Clip 上按右鍵可編輯更多 Clip 設定。另請參閱 [Clip 設定](clips/clip-settings.md)

### Groups

你會注意到每個 Clip 都有彩色外框，這個顏色代表它所屬的 _group_。APC40 的 Clip 按鈕也會以這個顏色亮起。

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>青色</td></tr><tr><td>Group 2</td><td>橘色</td></tr><tr><td>Group 3</td><td>紅色</td></tr><tr><td>Group 4</td><td>靛色</td></tr><tr><td>Group 5</td><td>綠色</td></tr></tbody></table>

group 系統非常彈性，可讓你：

* 讓某個 group 中的 Clips 持續播放，同時切換另一個 group 中的 Clips
* 快速將 zones 和 X/Y 翻轉指派給同一 group 內的所有 Clips
* 為 Clip 設定 _Flash mode_（Group 3 預設為 _Flash mode_）

Groups 也有淡入／淡出轉場設定，可由其中的 Clips 繼承，或由 Clip 自行覆寫。

你可以使用右鍵選單中的按鈕指派 Clip 的 group；或是在 APC40 上按住 group 按鈕，並在_按住不放時_按下 Clip 按鈕。

變更同一 group 內所有 Clips 的 zone 設定

使用 APC40 時，按下 group 按鈕，接著在_按住不放時_使用 zone 與 X/Y 按鈕，切換該 group 內所有 Clips 的 zone 設定。

另請參閱 [Clip 群組](clips/groups.md)

### Effects

Liberation 的效果系統是一套強大且靈活的方式，可即時改變 Clip 輸出。預設效果按鈕 1-8 位於 zone 按鈕下方。

#### 套用效果

按下效果按鈕可切換效果；更好的方式是使用 APC40 滑桿 1-8，將效果淡入或淡出。

#### 效果參數

使用旋轉控制器 1-8\* 調整每個效果的 _parameter_。（你也可以用滑鼠按右鍵來調整 level 和 parameter）。parameter 變化會依效果設定而有不同作用。預設效果請參考下方清單。

{% hint style="info" %}
你在效果按鈕上看到的小數字，代表該效果的 _level_ 和 _parameter_。_level_ 由 APC40 上的推桿控制，也可以在按鈕上點擊並拖曳。parameter 則由 APC40 上的旋鈕調整，或可用滑鼠按右鍵調整。
{% endhint %}

_\*旋轉控制器 1-8 位於 APC40 Mk2 頂端；在 Mk1 上則位於右上方。另請參閱：_ [APC40 參考](reference/apc40-reference.md)

#### 預設效果

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   對 Clip 輸出套用混亂的移動效果。parameter 會調整混亂的程度／速度。
2. **Sine wave** :\
   讓所有內容沿著移動中的正弦波變形。parameter 會調整波長。
3. **Rotation** :\
   讓所有內容旋轉。parameter 會調整旋轉速度。
4. **Horizontal flip** :\
   將所有內容在水平方向壓縮與拉伸。parameter 會調整速度。
5. **Scale** :\
   反覆將所有內容從完整大小縮放到零。parameter 會調整速度。
6. **Hue** :\
   改變所有內容的色相，但不改變飽和度（也就是白色仍會保持白色）。parameter 會調整色相。
7. **Saturation and hue** :\
   改變所有內容的色相，並將顏色完全飽和（也就是白色會變成該顏色）。parameter 會調整色相。
8. **Flash** :\
   反覆讓所有內容的亮度從全亮閃爍到零。parameter 會調整閃爍速度。

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

底部列還有另外 16 個顏色效果，可套用預設的色相與飽和度值。

請注意，這些是預設效果，但它們幾乎可以被編輯成任何你想要的效果！

#### 什麼是_「目前選取的 Clip」_？

當你啟動某個 Clip 時，它會亮起，表示正在作用中。它也會有白色外框，表示這是目前_選取_的 Clip。每當你切換 zone 按鈕或調整 Clip 設定時，這些操作都會套用到_目前選取的 Clip_。

{% hint style="info" %}
若要選取 Clip 但不觸發它，請先按住 `Alt / Option` 鍵，再按 Clip 按鈕。這是調整它的 zones 與其他設定、但不執行它的好方法。
{% endhint %}

### Clip Settings 面板

使用 _Clip Settings_ 面板可編輯縮放、X/Y 位置，並存取強大的 zone delay 系統。

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings 面板

在 _Global Settings_ 面板中，可以調整會影響所有 zones 中所有輸出的全域輸出設定。

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

開啟 AUTO RESET 後，只要沒有 Clips 正在播放，就會自動重設所有 _Global settings_。

### Timing

幾乎所有雷射表演都會有某種音樂聲軌，因此 Liberation 的 timing 系統是以每分鐘拍數（BPM）為基礎。在 _Tempo Panel_ 中，你可以看到時間的表示方式；每個方格代表一拍，並會依照節拍閃爍。

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

有多種同步選項，包括 MIDI clock 和 Ableton Link。如果你知道音樂的速度，可以使用畫面上的滑桿或 APC40 Tempo 旋鈕手動調整；也可以使用 _Tap Tempo_ 系統跟上音樂節奏\_.\_

#### Tap Tempo

_Tap Tempo_ 是音樂應用程式中常用的術語，可讓你在音樂播放時，依照拍點敲擊來設定速度。你可以使用畫面上的按鈕，但建議使用 _T_ 鍵或 APC40 上的 _Tap Tempo_ 按鈕（如果你偏好，也可以使用腳踏開關）。

按下 _R_ 鍵或 _Metronome_ 按鈕（APC40）可將速度重設到小節開頭。

按下 _Y_ 鍵或轉動 _Tempo_ 旋鈕（APC40），可將速度四捨五入為整數。這對電子音樂很有用，因為電子音樂通常會使用整數 BPM。

### 整理你的 Clip Deck

若要在 Clip Deck 上移動 Clip，請點擊並拖曳到新位置。拖曳時，你可以使用方向鍵（或 APC40 上的捲動滾輪／按鈕）左右捲動。

拖曳時按住 `Alt / Option` 鍵可建立複本。

按住 `Alt / Option` 並點擊 Clip，可在不啟動它的情況下選取它。

按住 `Alt / Option + Shift` 並點擊 Clip 可多選，或在 Clip 外側點擊並拖曳進行「套索」選取。

點擊並拖曳時，會拖曳所有已選取的 Clips。

若要刪除一個或多個 Clips，可以將它們拖出 Clip Deck（會出現垃圾桶圖示），或使用 Clip 右鍵選單中的 DELETE 按鈕。

### Laser Overview 面板

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_ 可讓你快速查看目前正在執行的雷射狀態。右側的綠色方塊表示雷射控制器狀態正常。如果變成橘色，表示偶爾會有斷訊；如果是紅色，表示已中斷連線。如果是灰色，則表示完全沒有連接到控制器。

中間的圖表是 frame length 的歷史記錄，右側數字則是目前的 frame rate。內容越複雜，frame rate 就越低（也就是越容易閃爍）。低於約 25fps 時，看起來就會開始有點閃爍。

### 連接雷射 — Controller Assignment 面板

點擊 _Assign Laser Controllers_ 按鈕可開啟 _Controller Assignment_ 面板。（此面板也可以從選單列的 _View -> Controller Assignment_ 存取）。

你可以在這裡選擇哪些雷射輸出要送到哪些雷射控制器。將右側清單中的控制器拖放到左側的插槽中。你可以重新命名控制器，讓名稱符合與它配對的雷射（使用筆形圖示按鈕）。

更多詳細資訊請閱讀 [Controller Assignment](setting-up/controller-assignment.md)章節。

{% hint style="danger" %}
在啟用任何雷射輸出之前，請務必先閱讀[設定雷射](setting-up/setting-up-lasers.md)章節。
{% endhint %}

### 雷射輸出面板

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

此面板會顯示_目前選取的雷射_設定（由頂端的數字表示）。可使用 _tab_ 鍵、按下數字鍵、點擊 _Laser Overview_ 面板中的雷射編號，或在 _output view_ 中點擊雷射編號來變更目前選取的雷射。

* **Number button** 啟用或停用該雷射輸出；如果是紅色，表示該雷射已啟用輸出。
* **Brightness** 調整此雷射的亮度，不受其他雷射影響（並會與 _Global Brightness_ 設定相乘；也就是說，如果兩者都是 50%，你的雷射輸出會是 25%）。
* **Test Pattern** 只為此雷射開啟測試圖樣（會覆寫全域 Test Pattern 設定）
* **Orientation** 修正側掛或倒掛的雷射。
* **Flip Horizontal and Flip Vertical** 反轉雷射輸出。對於配線不一致的雷射，可用於輸出校正。
* **Copy Laser Settings** 開啟一個面板，讓你將此雷射的各種設定複製到其他雷射。

### Scanner settings

顯示用雷射的工作方式，是讓單一雷射光束以極高速度移動，並透過開關光束來在空氣中畫出形狀。你看到的線條、形狀與影像，其實是光束以快到眼睛無法跟上的速度描繪路徑。

point stream 是告訴雷射下一步要移動到哪裡、以及光束何時開啟或關閉的資料。在 Liberation 中，Clips 會在送往雷射時即時轉換成這個 point stream。

Liberation 可讓你細部控制 point stream 的產生方式，讓每台雷射都能在流暢度、亮度與效能之間取得平衡。

{% hint style="info" %}
如果你習慣使用依賴預先計算 point stream 的舊式雷射軟體，這種方式一開始可能會覺得不同。不過，即時產生 points 可讓相同內容針對每台雷射做不同最佳化。當你要同時使用多台掃描速度或品質不同的雷射時，不必複製或重建內容，就能更容易處理。它也讓 Clip 檔案非常小，這就是為什麼整個預設 Liberation Clip Deck 只有幾 MB，而不是好幾 GB。
{% endhint %}

基本 scanner settings 包括：

* **Speed** 是 scanner speed，也就是雷射移動並畫出形狀的速度。這相當於傳統雷射軟體中的 point rate 調整，但在 Liberation 中，你可以在_不受 point rate 影響_的情況下改變雷射移動速度。你通常不需要調整這個設定。
* **Scanner sync**（有時稱為 _blank shift_，以前稱為 Colour Shift）掃描器會讓雷射快速移動，但亮度與顏色變化通常會與移動不同步。這會在光束與線條邊緣呈現為細小閃爍的光「尾巴」。使用這個調整項目，可讓移動與顏色彼此同步。請參閱 [Laser Settings](setting-up/laser-settings.md)

其他進階 scanner settings 會在[進階](advanced/)章節中說明。

### Zoning

如需雷射設定與 zoning 的完整指南，請參閱：[設定雷射](setting-up/setting-up-lasers.md)
