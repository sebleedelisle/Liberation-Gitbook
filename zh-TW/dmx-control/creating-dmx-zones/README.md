---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 建立 DMX zone

1. 連接你的 Art-Net node，並依照[連接到 Art-Net node](../connecting-to-an-artnet-node.md "mention")完成設定。
2. 開啟 **DMX Zones**，然後按一下 **ADD DMX ZONE**。
3. 將該 zone 的 **Node**、**Universe** 和 **Address** 設定為與燈具相符。
4. 為燈具選擇一個 **Preset**。Preset 會定義哪些 DMX 通道接收固定值、內容開／關值、RGB 色彩、X/Y 位置、亮度，或明確的 DMX Value 輸入。
5. 按一下 **Edit DMX profile/channel mapping**（滑桿圖示）來編輯通道對應。預設的 preset 會從內容開／關通道和 RGB 色彩通道開始。
6. 指派 Clip 到 DMX zone 的方式，和指派到 beam zone 或 canvas zone 相同。
7. 當你準備好讓該 zone 輸出 DMX 時，按下 **ARM**。

{% hint style="warning" %}
只有已啟用輸出的 DMX zone 會送出即時數值。未啟用輸出的 DMX zone 會將其對應通道清為零，這在設定燈具時比較安全。
{% endhint %}

DMX 輸出也會受到你的授權等級限制。如果 **ARM** 按鈕無法使用，請檢查你的等級是否包含 DMX 輸出，或已啟用輸出的 DMX zone 數量是否已達上限。
