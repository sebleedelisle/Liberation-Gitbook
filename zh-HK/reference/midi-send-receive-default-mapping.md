---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI 傳送／接收預設對應

**Clip 的開啟和關閉由通道 1 至 14 的 MIDI note on / off 觸發**

Clip 有水平（x）和垂直（y）位置；在 Clip 上按右鍵即可看到其位置。MIDI 可由 0,0 開始觸發 Clip。

{% hint style="info" %}
請注意，使用此系統控制 Clip 時位置是絕對的；當你捲動 Clip Deck 時，Clip 位置不會改變。
{% endhint %}

MIDI 通道 1、note 1 是 Clip 0,0，note 2 是 Clip 0,1，note 3 是 Clip 0,2，如此按列向下、按欄向右遞增。到達 128 後會移到下一個通道並重新開始。因此，你總共有 128 x 14 = 1792 個 Clip 可透過 MIDI 存取。

Clip 座標的 MIDI note：

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...如此類推</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

請注意，MIDI note on 事件會啟動 Clip，而對應的 note off 事件會停止 Clip。這不受群組的觸發模式影響。此系統最初是為播放和錄製而設計，因此如果讓 note 以切換方式控制 Clip，效果並不理想。

### **效果**

**通道 15** 上的 MIDI control change（CC）訊息會調整效果。\
Effect 1 使用 CC 0-3，數值 0-127\
Effect 2 使用 CC 4-7，數值 0-127\
Effect 3 使用 CC 8-11，數值 0-127\
……如此類推。

每四個控制項為一組，用於控制該效果的 Level 及 3 個參數：

<table><thead><tr><th width="164">效果：</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...如此類推</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **全域設定**

**通道 16** 上的 MIDI control change 訊息會更改全域設定：\
CC 1 : Shift X（水平）0 -127，64 為中間值\
CC 2 : Shift Y（垂直）0 -127，64 為中間值\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D（Y）\
CC 9 : Rotation 2D（Z）

另請特別注意：\
CC 15 : Global brightness

請注意，此系統最初是為錄製和播放而設計，讓你可以使用 Logic、Ableton 或其他 DAW 建立時間軸動畫。雖然你可以將它用於現場控制，但它並未針對此用途最佳化，而且與 APC40 設定相比，缺少部分現場控制功能。
