---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX zones

DMX zone 是 Liberation 的輸出 zone，會送出 Art-Net/DMX，而不是雷射點。它們會與 beam zone 和 canvas zone 一起顯示，因此 Clip 可以用相同的 zone 選擇流程指派給它們。

從選單開啟 **DMX Zones**，或使用 Laser overview 中的 DMX 區段來管理它們。

* **ADD DMX ZONE** - 建立新的 DMX zone。
* **ARM** - 啟用該 zone 的 DMX 輸出。未啟用的 DMX zone 會將其對應的 channel 清為零。
* **Node** - 選擇 Art-Net node 編號。
* **Universe** - 選擇 Art-Net universe。顯示值從 1 開始，因此 Universe 1 是第一個 universe。
* **Address** - 設定 fixture 的起始 address。顯示值同樣從 1 開始。
* **Preset** - 選擇將 Clip 內容對應到 DMX channel 的 DMX preset。
* **Edit DMX zone settings**（鉛筆圖示）- 開啟 zone 設定，例如手動 zone forwarding 和 fixture orientation。
* **Edit DMX profile/channel mapping**（滑桿圖示）- 開啟 DMX preset/channel 編輯器。
* **Delete** - 移除 DMX zone。

### 啟用數量限制

可同時啟用的 DMX zone 數量取決於您的授權等級。如果您的等級不允許 DMX 輸出，或已啟用的 DMX zone 數量已達上限，其他 zone 的 **ARM** 按鈕會停用，滑鼠停留時會顯示禁止進入圖示。

若要啟用更多 zone，請先停用另一個 DMX zone，或使用 DMX 限制較高的授權等級。
