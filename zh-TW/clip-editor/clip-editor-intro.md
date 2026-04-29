---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Clip Editor 簡介

Clip Editor 是建立雷射內容的多用途工具，也是 Liberation 的核心。你可以很容易做出簡單內容，同時它也有足夠彈性，可以製作非常精細、複雜的效果。

{% hint style="info" %}
以 node 為基礎的 editor 是 Liberation 最早做出來的部分！它源自 2018 年在英國一場雷射聚會中，與 Rob Stanley 討論「物件導向」雷射內容設計工具會是什麼樣子。

雖然看起來簡單，但這其實是個相當複雜的系統。不過到了 2019 年初，我已經做出能證明概念可行的 demo，也因此開啟了這整段旅程！
{% endhint %}

它是一個以 node 為基礎的視覺化 editor（或稱 [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)）。如果你用過 TouchDesigner、MaxMSP 或 VVVV，應該會覺得很熟悉。不過 Clip Editor 稍微不同，也相對簡單一些，因為它是專門為向量圖形設計的。

你可以在 clip 按鈕上按右鍵，然後選擇 _EDIT CLIP_ 來開啟 Clip Editor。或者在空的 clip 按鈕上按右鍵，選擇 _CREATE AND EDIT CLIP_。

### 概覽

在 Clip Editor 中你會看到：

* 上方的 **Creator** 與 **Operator node buttons**
* 左側的 **Oscillator node buttons**
* 右側面板中的內容預覽；如果你點選某個 node，還會看到第二個預覽，顯示該 node 本身的內容。
* 目前正在編輯的 clip 的所有 nodes 與連線（如果是新的 clip，這裡會是空的）
* 含有各種選項的 Clip Editor 面板

編輯時，你也會在背景的 3D 視覺化預覽中看到這個 clip 的樣子。

{% hint style="info" %}
如果你在 3D 視覺化預覽中看不到任何輸出，可能需要使用 zone 按鈕開啟你想要的 zones。你也需要確認 _Preview to lasers_ 已啟用，請參考下方的 [Clip Editor 面板](clip-editor-intro.md#clip-editor-panel)。
{% endhint %}

### 建立 clip

通常你會從一個或多個 [Creator nodes](creator-nodes.md) 開始，然後從左到右連接用來處理內容的 [運算子 nodes](operator-nodes/)。當你把 Creators 和／或 Operators 移到一起時，你會看到它們自動彼此連接。你也可以把它們拖開，讓它們再次斷開連接。

### 將 nodes 加入 clip

從上方或左側的其中一個 node 按鈕點擊並拖曳到 Clip Editor 中的空白區域。

### 調整 node 的設定

點擊齒輪圖示按鈕（node 右上角），即可開啟該 node 的屬性面板。

### 啟用與停用 node

點擊電源圖示按鈕（node 左上角）即可啟用或停用 node。node 會變暗，表示它目前不是作用中。請注意，即使 Operator 被停用，內容仍然會通過它，但該 node 不會影響內容。

### 將 nodes 連接在一起

內容由 Creator node 產生，並從左到右沿著 nodes 傳遞；每個 Operator 都會以某種方式影響內容，然後再傳給下一個 Operator。路徑最後剩下的內容就是這個 clip 的內容。當你把 Creators 和 Operators 移近時，它們會自動彼此連接。若要分開，請再次把它們拖開。

{% hint style="info" %}
你可以將多個 node 連接到下一個 node 的輸入。這在合併多個內容片段時很有幫助。
{% endhint %}

### Node 屬性與 sockets

每個 node 底部都有一排 sockets，每個 socket 代表該 node 內的一個屬性，例如亮度、位置、縮放、旋轉等。

[Oscillator nodes](oscillators/) 可以從下方連接到這些 sockets，用來讓這些設定產生動畫。Oscillator nodes 的輸出位於上方；點擊並拖曳即可拉出連線，然後放到其他 nodes 的屬性 socket 中。

### Oscillator nodes

Oscillator nodes 用來隨時間改變屬性。它們通常代表鋸齒波或正弦波等波形，但有些 Oscillator nodes 會使用外部輸入（例如麥克風輸入音量）作為來源。

{% hint style="info" %}
如果你用過類比合成器，應該會熟悉 oscillator 的概念；它們常用來產生波形，或隨時間調整聲音。Liberation 中的 Oscillators 也有類似用途。

**有趣小知識：** _Liberation_ 這個名稱的靈感來自 Moog Liberation，那是一把 1980 年推出的「keytar」合成器，並因 Herbie Hancock、Jean-Michel Jarre，甚至 James Brown 的使用而聞名！
{% endhint %}

Oscillators 一定會有 _range_ 設定，用來控制要調整之屬性的最小值與最大值。而 _Wave Oscillators_ 一定會有 _duration_ 設定，用來決定 oscillator 改變數值的速度。更多資訊請參考 [波形振盪器](oscillators/wave-oscillators.md)。

### Clip Editor 面板

* Timer - 面板上方會顯示 clip 播放進行中的目前時間
* _RETRIGGER_ - 從頭重新啟動 clip；如果你的 clip 不會循環，這特別實用
* _Preview to lasers_ - 勾選此項時，你在編輯這個 clip 的同時會看到 3D 視覺化預覽更新。如果關閉，你會看到 editor 外正在播放的 clips。這是全域設定，不是每個 clip 各自的設定。
* _UNDO/REDO_ - 用於 Clip Editor 本身。也對應到 `Cmd / Ctrl + Z` 和 `Cmd / Ctrl + Shift + Z`。
* _SAVE CLIP_ - 儲存你的編輯，但會在覆寫前提醒你
* _SAVE AS A COPY_ - 將你的 clip 儲存到 Clip Deck 中下一個可用的位置。這會成為此 clip 的新位置，之後所有儲存都會存到這個新位置。
* _EXIT EDITOR_ - 關閉 Clip Editor。如果有未儲存的變更，你會看到確認面板。
