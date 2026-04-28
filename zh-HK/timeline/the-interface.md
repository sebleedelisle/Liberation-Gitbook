---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/the-interface
---

# 🟧 介面

### Timeline 介面

如果你以前用過音樂或影片軟件，timeline 的概念應該會很熟悉：它是一個橫向格線，時間由左至右推進，你可以將 clips 放在上面，定義何時播放甚麼內容。

如果你未接觸過 timeline，可以把它想像成樂譜或舞台 cue sheet —— 每個區塊都是一段在指定時間觸發的內容。這是一種有條理的方式，用來設計你的激光表演如何隨時間展開。

***

#### Timeline Bar 控制項

**Enable Button**

在你可以操作 timeline 之前，必須先啟用它。按一下 **ENABLE** toggle（啟用時為橙色），即可啟用 timeline 進行編輯及播放。

**Timeline Name**

目前 timeline 的名稱會顯示在 enable button 旁邊（預設為 **「Timeline」**）。按一下名稱即可重新命名 —— 在管理多首歌曲或多個段落時很有用。

**Timeline List（三條橫線圖示）**

按一下可開啟 timeline list。你可以在這裏切換不同 timeline，或在 show 中新增／移除 timeline。

**Lock Button**

保護你的 timeline，避免意外修改。啟用後，編輯功能會停用，直至解鎖為止。

**Add Clips Button**

將 clip deck 中目前所有已選取的 clips，加到 timeline 目前 playhead 的位置。這非常適合從現場演出或預先準備好的選擇中建立 timeline。

**Insert Audio File**

開啟檔案對話框，選擇要插入 timeline 開始位置的音訊檔案。支援格式：WAV、MP3、OGG、FLAC。適合用來將 timeline 與音樂同步。

**Default Clip Duration**

設定使用拖放或 + button 新增到 timeline 的 clips 預設長度（以 bars 計）。在建立 sequences 時可加快工作流程。

**Volume**

調整 timeline 上所有 audio clips 的播放音量。不會影響激光輸出。

***

#### Transport 及播放

**Transport Controls**

用於瀏覽的標準 transport 按鈕

* Forward / back（每次移動一個 bar）
* Stop / Rewind to start
* Play / pause
* Record

**Bar / Beat / Step Display**

以 bars:beats:frames 格式顯示目前 timeline 位置。播放進行時會即時更新。

***

#### 同步及時間設定

**Tempo Map Button**

啟用 tempo mapping。開啟後，timeline 頂部會出現一個新列，你可以在該處按右鍵加入 tempo changes。非常適合 tempo 會變化或包含 tempo ramps 的曲目。

**Timecode Panel**

開啟 timecode settings panel。你可以在這裏設定 Liberation 與 LTC、MIDI Clock 或 Ableton Link 同步，確保與外部系統精準對齊。

**SNAP Toggle**

啟用後，clips 及編輯操作會貼齊格線。這可讓精準對齊更容易。停用後則可自由放置。

**Snap Size**

設定格線解析度 —— bars、beats 或 steps。在進行精細編輯或快速重新對齊時很有用。

***

#### 顯示及播放行為

**Auto Scroll（滑板圖示）**

啟用後，播放期間 timeline 會自動捲動以跟隨 playhead。

**Scrub Mode（燈泡圖示）**

啟用後，當你手動移動 playhead 時，激光會即時輸出。這有助預覽特定 frames，但請小心使用，尤其是配合高功率投影機時。

**Loop Playback**

從 timeline 開始位置循環播放至已設定的 timeline 長度。適合處理特定段落或播放背景 visuals。

**Timeline Length**

設定 timeline 的總長度（以 bars 計）。拖曳即可調整，或雙擊直接輸入數值。
