---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX 區域

DMX zone 是 Liberation 的 Output zone，會傳送 Art-Net/DMX，而不是雷射點。它們會與 beam zone 和 canvas zone 一同顯示，因此可透過相同的 zone 選擇流程將 Clip 指派到這些 zone。

從選單開啟 **DMX Zones**，或使用 Laser overview 內的 DMX 區段來管理它們。

* **ADD DMX ZONE** - 建立新的 DMX zone。
* **ARM** - 啟用該 zone 的 DMX 輸出。未啟動的 DMX zone 會將其已映射的通道清除為零。
* **Node** - 選擇 Art-Net node 編號。
* **Universe** - 選擇 Art-Net universe。顯示值以 1 為起點，因此 Universe 1 是第一個 universe。
* **Address** - 設定燈具的起始地址。顯示值同樣以 1 為起點。
* **Preset** - 選擇用於將 Clip 內容映射至 DMX 通道的 DMX preset。
* **Edit DMX zone settings**（鉛筆圖示）- 開啟 zone 設定，例如手動 zone forwarding 及燈具方向。
* **Edit DMX profile/channel mapping**（滑桿圖示）- 開啟 DMX preset／通道編輯器。
* **Delete** - 移除 DMX zone。

### 啟動限制

可同時啟動的 DMX zone 數量取決於你的授權等級。如果你的等級不允許 DMX 輸出，或你已經啟動了可用的 DMX zone 數量上限，其他 zone 的 **ARM** 按鈕會停用，滑鼠停留時會顯示禁止進入圖示。

如要啟動更多 zone，請先停用另一個 DMX zone，或使用 DMX 限制較高的授權等級。
