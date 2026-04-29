---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Clip Editor 簡介

Clip Editor 是建立激光內容的多用途工具，也是 Liberation 的核心。它可以輕鬆製作簡單內容，同時亦有足夠彈性，建立非常精細和複雜的效果。

{% hint style="info" %}
節點式編輯器是 Liberation 最早製作的部分！它源自 2018 年在英國一次激光聚會中，與 Rob Stanley 討論「物件導向」激光內容設計器會是甚麼樣子。

雖然看起來簡單，但要建立這套系統其實相當複雜。不過到 2019 年初，我已經有一個可運作的 demo 證明了這個概念，亦由此展開了整個旅程！
{% endhint %}

它是一個節點式視覺編輯器（或稱為 [節點圖架構](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)）。如果你用過 TouchDesigner、MaxMSP 或 VVVV，應該會覺得很熟悉。不過 Clip Editor 有一點不同，也相對簡單，因為它是專為向量圖形而設計的。

你可以在 clip 按鈕上按右鍵，然後選擇 _EDIT CLIP_ 來開啟 Clip Editor。或者在空白 clip 按鈕上按右鍵，然後選擇 _CREATE AND EDIT CLIP_。

### 概覽

在 Clip Editor 中，你會看到：

* 頂部的 **Creator** 和 **Operator node buttons**
* 左側的 **Oscillator node buttons**
* 右側面板中的內容預覽；如果你按一下某個節點，會看到第二個預覽，顯示該節點本身的內容。
* 你正在編輯的 clip 的所有節點和連接（如果是新的 clip，這裡會是空白）
* Clip Editor 面板及各種選項

編輯時，你亦會在背景的 3D Visualiser 中看到這個 clip 的效果。

{% hint style="info" %}
如果你在 3D Visualiser 中看不到任何輸出，可能需要使用 zone 按鈕開啟你想使用的 zone。你亦需要確認 _Preview to lasers_ 已啟用，請參閱下方的 [Clip Editor 面板](clip-editor-intro.md#clip-editor-panel)。
{% endhint %}

### 建立 clip

通常你會由一個或多個 [Creator 節點](creator-nodes.md)開始，然後由左至右連接用來處理內容的 [Operator 節點](operator-nodes/)。當你把 Creator 和／或 Operator 移近時，你會看到它們自動互相連接。你亦可以將它們拖開，重新中斷連接。

### 將節點加入 clip

從頂部或左側其中一個 node button 按住並拖曳到 Clip Editor 內的空白位置。

### 調整節點設定

按一下齒輪圖示按鈕（節點右上角），即可開啟該節點的屬性面板。

### 啟用和停用節點

按一下電源圖示按鈕（節點左上角），即可啟用或停用該節點。節點會變暗，表示它目前未啟用。請注意，即使 Operator 已停用，內容仍然會通過該 Operator，但該節點不會影響內容。

### 將節點互相連接

內容由 Creator 節點建立，並沿節點由左至右傳遞；每個 Operator 都會以某種方式影響內容，然後傳遞到下一個 Operator。路徑末端剩下的內容，就是這個 clip 的內容。當你把 Creator 和 Operator 移近時，它們會自動互相連接。要分開它們，只需再次將它們拖開。

{% hint style="info" %}
你可以將多個節點連接到下一個節點的輸入。這對合併多段內容很有用。
{% endhint %}

### 節點屬性和 socket

每個節點底部都有一排 socket，每個 socket 代表該節點內的一個屬性，例如亮度、位置、縮放、旋轉等。

[Oscillator 節點](oscillators/)可以從下方連接到這些 socket，用來為這些設定製作動畫。Oscillator 節點頂部有一個輸出；按住並拖曳即可拉出連接，然後放到其他節點的其中一個屬性 socket。

### Oscillator 節點

Oscillator 節點用來隨時間改變屬性。它們通常代表鋸齒波或正弦波等波形，但部分 Oscillator 節點會使用外部輸入（例如咪高峰輸入音量）作為來源。

{% hint style="info" %}
如果你曾經使用過 analog synth，應該會熟悉 oscillator 的概念：它們通常用來產生波形，或隨時間調整聲音。Liberation 中的 Oscillator 作用相近。

**趣聞：** _Liberation_ 這個名稱的靈感來自 Moog Liberation，一款於 1980 年推出的合成器「keytar」，並由 Herbie Hancock、Jean-Michel Jarre，甚至 James Brown 等人使用而聞名！
{% endhint %}

Oscillator 一定有 _range_ 設定，用來控制要調整的屬性的最小值和最大值。而 _Wave Oscillators_ 一定有 _duration_ 設定，用來決定 Oscillator 改變數值的速度。詳情請參閱 [波形振盪器](oscillators/wave-oscillators.md)。

### Clip Editor 面板

* Timer - 面板頂部會顯示 clip 播放進度的目前時間
* _RETRIGGER_ - 從開頭重新啟動 clip；如果你的 clip 不會循環，這會特別有用
* _Preview to lasers_ - 勾選後，你在編輯此 clip 時會看到 3D Visualiser 更新。如果關閉，你會看到 editor 以外正在播放的 clip。這是全域設定，不是個別 clip 的設定。
* _UNDO/REDO_ - 用於 Clip Editor 本身。亦對應至 `Cmd / Ctrl + Z` 和 `Cmd / Ctrl + Shift + Z`。
* _SAVE CLIP_ - 儲存你的編輯，但會提示你有關覆寫的警告
* _SAVE AS A COPY_ - 將你的 clip 儲存到 clip deck 中下一個可用位置。這會成為該 clip 的新位置，之後所有儲存都會儲存在這個新位置。
* _EXIT EDITOR_ - 關閉 Clip Editor。如果你有未儲存的變更，系統會顯示確認面板。
