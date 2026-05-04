---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 載入與儲存

Liberation 會持續將狀態儲存到磁碟，因此即使遇到停電或系統問題，重新啟動時也會從上次離開的狀態繼續；你的 zones、時間軸或其他內容應該都不會遺失。

不過，你也可以匯出目前的設定，用於備份或轉移到另一台電腦。

### 專案匯入 / 匯出

Project 檔案會儲存目前設定中的幾乎所有內容，包括：

* 下方 [Laser Settings 匯入 / 匯出](loading-and-saving.md#laser-settings-import-export "mention")所列的所有內容
* Clips、效果和群組設定
* 你的所有時間軸（不包含音訊和影片媒體）
* Art-Net 設定
* MIDI 傳送 / 接收設定
* 節拍 / 同步設定

目前不會儲存和載入：

* MIDI notes node 和 Sound Input Oscillator 所使用的音訊與 MIDI 輸入設定（但_會_儲存 MIDI 傳送 / 接收設定，以及 timecode 音訊輸入）
* 介面縮放
* Canvas guide images 使用的媒體
* 時間軸中的音訊和影片媒體
* Text node 使用的字型

{% hint style="danger" %}
時間軸中的音訊和影片檔不會隨 Project 檔案一起儲存，因此如果你要轉移到另一台電腦，請務必另外儲存這些檔案。請參閱[關於時間軸媒體檔案的重要注意事項](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Laser Settings 匯入 / 匯出

* 每一台雷射的 Laser Settings
* Beam zones
* Canvas target areas
* DMX zones
* Laser controller 指派（以及你已重新命名的任何 controllers 的別名）
* 雷射掃描器與色彩校正設定和 presets
* 3D 視覺化設定和 presets

### Clip Deck 匯入 / 匯出

* 所有 Clips 及其 zone 指派、設定和參數
* 所有群組設定、flash mode、fade in/out 時間等

目前不會儲存和載入：

* 所有效果及其參數與設定

{% hint style="info" %}
**不載入整個專案，只從 Project 檔案載入 Clips**

若要只從專案匯入 Clips，請選擇 _**Clips->Import Clip Deck**_，然後不要選擇 clip deck 檔案（.cpdk），改選 Project 檔案。
{% endhint %}

### 附加 Clip Deck

你可以使用 _Append Clip Deck_，將已匯出的 clip deck 檔案中的 Clips 加到目前專案。Clips 會加到目前 Clip Deck 的結尾，但檔案中的效果和群組設定不會匯入。

### Export Selected Clips

目前已選取的任何 Clips 都會匯出到檔案中。群組設定和效果不會儲存，只會儲存 Clips。請注意，目前正在執行的 active Clips 不會匯出，除非它們同時也被選取。

{% hint style="info" %}
按住 Option/Alt - Shift - 點擊 Clips 可選取它們（或使用套索）。你可以從 Clips 周圍的粗白色外框判斷哪些 Clips 已被選取。請參閱[啟動與停止 Clips](clips/starting-stopping-clips.md "mention")
{% endhint %}

### 效果匯入 / 匯出

載入和儲存所有效果，以及其群組設定與參數。

{% hint style="info" %}
**不載入整個專案，只從 Project 檔案載入效果**

若要只從專案匯入效果，請選擇 _**Effects->Import Effects**_，然後不要選擇效果檔案（.efts），改選 Project 檔案。
{% endhint %}

### 時間軸匯出

匯出包含一個或多個時間軸的時間軸檔案。請注意，匯出的時間軸檔案一定會包含 Clip Deck（不過你可以選擇要匯回哪些 Clips，請參閱下方[時間軸匯入](loading-and-saving.md#timeline-import "mention")）

如果你的 Project 檔案中有多個時間軸，會開啟一個面板，讓你選擇要匯出的時間軸。

{% hint style="danger" %}
時間軸中的音訊和影片檔不會隨時間軸檔案一起儲存，因此如果你要將內容轉移到另一台電腦，請務必另外儲存這些檔案。請參閱[關於時間軸媒體檔案的重要注意事項](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### 時間軸匯入

從單一時間軸檔案匯入一個或多個時間軸。選取時間軸檔案後，會開啟一個含有多個匯入選項的面板。

如果時間軸檔案中有多個時間軸，所有時間軸都會列出。勾選你要包含的項目。

* Replace existing timelines\
  會刪除你目前所有時間軸，並以匯入的時間軸取代
* Import used clips only\
  只會匯入已使用的 Clips，並將 Clips 排列成群組，每個時間軸各一個群組。如果未選取此選項，時間軸檔案中的整個 Clip Deck 會附加到你現有的 Clips 後方。
* Replace existing clip deck\
  使用時間軸檔案中的 Clips 取代你目前的 Clip Deck。只有在選取 _Replace existing timelines_ 時才可使用。

{% hint style="info" %}
**不載入整個專案，只從 Project 檔案載入時間軸**

若要只從專案匯入時間軸，請選擇 _**Timeline->Import Timeline(s)**_，然後不要選擇時間軸檔案（.ltml），改選 Project 檔案。
{% endhint %}

### DMX / Art-Net 匯入 / 匯出

儲存和載入 Art-Net nodes 及其 IP 位址。也包含 DMX zones，以及你的所有 DMX presets。

### 關於時間軸媒體檔案的重要注意事項

音訊和影片檔目前**不會**隨時間軸檔案一起匯出，因此如果你需要將內容移到另一台電腦，請務必一併包含這些檔案。

{% hint style="info" %}
**時間軸如何尋找媒體檔案**

載入時間軸時，它會查看時間軸（或 Project）檔案所在的同一個資料夾，並搜尋其中以及任何子資料夾。因此，只要檔案位於同一個資料夾或其子資料夾中（例如 _/videos_ 或 _/sound_），載入時就會找到它們。
{% endhint %}
