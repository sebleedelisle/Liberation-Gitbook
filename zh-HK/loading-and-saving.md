---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 載入與儲存

Liberation 會持續將狀態儲存到磁碟，因此即使遇上停電或系統問題，重新啟動時亦會由上次的位置繼續；你的 zones、timeline 或其他內容一般不會遺失。

不過，你仍然可以匯出目前設定，用於備份或轉移到另一部電腦。

### Project 匯入／匯出

Project 檔案會儲存你目前設定中的幾乎所有內容，包括：

* 以下 [Laser settings 匯入／匯出](loading-and-saving.md#laser-settings-import-export)所列的全部內容
* Clips、effects 及 group settings
* 你的所有 timelines（不包括音訊及影片媒體）
* ArtNet 設定
* MIDI 傳送／接收設定
* Tempo／同步設定

目前不會儲存及載入：

* MIDI notes node 及 Sound Input Oscillator 所使用的聲音及 MIDI 輸入設定（但它_會_儲存 MIDI 傳送／接收設定，以及 timecode 聲音輸入）
* Interface scaling
* Canvas guide images 的媒體
* Timelines 的聲音及影片媒體
* Text node 使用的字型

{% hint style="danger" %}
Timeline 中的聲音及影片檔案不會隨 project 檔案一同儲存；如果你想轉移到另一部電腦，請務必另外儲存這些檔案。請參閱 [關於 timeline 媒體檔案的重要注意事項](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Laser settings 匯入／匯出

* 每部 laser 的 Laser settings
* Beam zones
* Canvas target areas
* DMX zones
* Laser controller assignment（以及你曾重新命名的 controller aliases）
* Laser scanner 及 colour calibration 設定與 presets
* 3D visualiser 設定與 presets

### Clip Deck 匯入／匯出

* 所有 clips 及其 zone assignments、settings 和 parameters
* 所有 group settings、flash mode、fade in/out times 等

目前不會儲存及載入：

* 所有 effects 及其 parameters 和 settings

{% hint style="info" %}
**從 project 檔案載入 clips，而不載入整個 project**

如只要從 project 匯入 clips，請選擇 _**Clips->Import Clip Deck**_，然後不要選擇 clip deck 檔案（.cpdk），改為選擇 project 檔案。
{% endhint %}

### Append clip deck

你可以使用 _Append Clip Deck_，將已匯出的 clip deck 檔案中的 clips 加入目前 project。Clips 會加入到目前 clip deck 的末端，但檔案內的 effects 及 group settings 不會匯入。

### Export Selected Clips

所有目前已選取的 clips 都會匯出到一個檔案。Group settings 及 effects 不會儲存，只會儲存 clips。請注意，目前正在執行的 active clips 不會匯出，除非它們同時亦已被選取。

{% hint style="info" %}
按住 Option/Alt - shift - click clips 以選取它們（或使用 lasso）。你可以透過 clips 周圍的粗白色外框辨認哪些 clips 已被選取。請參閱 [啟動／停止 Clips](clips/starting-stopping-clips.md)
{% endhint %}

### Effects 匯入／匯出

載入及儲存所有 effects，以及其 group settings 和 parameters。

{% hint style="info" %}
**從 project 檔案載入 effects，而不載入整個 project**

如只要從 project 匯入 effects，請選擇 _**Effects->Import Effects**_，然後不要選擇 effects 檔案（.efts），改為選擇 project 檔案。
{% endhint %}

### Timeline 匯出

匯出包含一個或多個 timelines 的 timeline 檔案。請注意，匯出的 timeline 檔案一定會包含 clipdeck（不過你可以選擇要重新匯入哪些 clips，請參閱下方的 [Timeline 匯入](loading-and-saving.md#timeline-import)）

如果你的 project 檔案中有多個 timeline，系統會開啟一個面板，讓你選擇要匯出的 timelines。

{% hint style="danger" %}
Timeline 中的聲音及影片檔案不會隨 timeline 檔案一同儲存；如果你想將內容轉移到另一部電腦，請務必另外儲存這些檔案。請參閱 [關於 timeline 媒體檔案的重要注意事項](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Timeline 匯入

從單一 timeline 檔案匯入一個或多個 timelines。選取 timeline 檔案後，系統會開啟一個包含多個匯入選項的面板。

如果 timeline 檔案中有多個 timeline，它們會全部列出。勾選你想包含的項目。

* Replace existing timelines\
  會刪除目前所有 timelines，並以匯入的 timelines 取代
* Import used clips only\
  只會匯入已使用的 clips，並會將 clips 按 group 排列，每個 timeline 對應一個 group。如果未選取此選項，timeline 檔案中的整個 clip deck 會附加到你現有的 clips。
* Replace existing clip deck\
  以 timeline 檔案中的 clips 取代目前的 clip deck。只在已選取 _Replace existing timelines_ 時可用。

{% hint style="info" %}
**從 project 檔案載入 timelines，而不載入整個 project**

如只要從 project 匯入 timelines，請選擇 _**Timeline->Import Timeline(s)**_，然後不要選擇 timeline 檔案（.ltml），改為選擇 project 檔案。
{% endhint %}

### DMX / ArtNet 匯入／匯出

儲存及載入 ArtNet nodes，以及其 IP addresses。亦包括 DMX zones 及你所有的 DMX presets。

### 關於 timeline 媒體檔案的重要注意事項

聲音及影片檔案目前**不會**隨 timeline 檔案一同匯出；如果你需要將內容移到另一部電腦，請確保一併包含這些檔案。

{% hint style="info" %}
**Timeline 如何尋找媒體檔案**

載入 timeline 時，它會在 timeline（或 project）檔案所在的同一資料夾中尋找，並搜尋其中及所有子資料夾。因此，只要檔案位於同一資料夾或其子資料夾（例如 _/videos_ 或 _/sound_），載入時便會找到它們。
{% endhint %}
