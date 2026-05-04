---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 建立 DMX 區域

1. 連接你的 Art-Net node，並按照[連接至 Art-Net node](../connecting-to-an-artnet-node.md "mention")完成設定。
2. 開啟 **DMX Zones**，然後按 **ADD DMX ZONE**。
3. 將該 zone 的 **Node**、**Universe** 及 **Address** 設定為與燈具相符。
4. 為燈具選擇一個 **Preset**。Preset 會定義哪些 DMX channel 接收固定值、內容開／關值、RGB 顏色、X/Y 位置、亮度，或明確的 DMX Value 輸入。
5. 按 **Edit DMX profile/channel mapping**（滑桿圖示）以編輯 channel mapping。預設 Preset 一開始會包含內容開／關 channel 及 RGB 顏色 channel。
6. 以分配至 beam zone 或 canvas zone 的相同方式，將 Clip 分配至 DMX zone。
7. 當你準備好讓該 zone 輸出 DMX 時，按 **ARM**。

{% hint style="warning" %}
只有已啟用輸出的 DMX zone 會傳送即時數值。未啟用輸出的 DMX zone 會將其已映射 channel 清除為零，設定燈具時會較安全。
{% endhint %}

DMX 輸出亦受你的授權等級限制。如果 **ARM** 按鈕已停用，請檢查你的等級是否包含 DMX 輸出，或已啟用輸出的 DMX zone 數量是否已達上限。
