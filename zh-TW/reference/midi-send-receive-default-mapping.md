---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI 傳送/接收預設對應

**Clip 的開啟與關閉會由第 1 到第 14 通道的 MIDI Note On/Off 觸發**

Clip 具有水平 (x) 與垂直 (y) 位置；在 Clip 上按右鍵即可看到它的位置。MIDI 可以從 0,0 開始觸發 Clip。

{% hint style="info" %}
請注意，使用此系統控制 Clip 時是以絕對位置控制；捲動 Clip Deck 時，Clip 位置不會跟著改變。
{% endhint %}

MIDI 第 1 通道的音符 1 對應 Clip 0,0，音符 2 對應 Clip 0,1，音符 3 對應 Clip 0,2；先沿列向下遞增，再往下一欄前進。到達 128 後會移到下一個通道並重新開始。因此您總共有 128 x 14 = 1792 個 Clip 可透過 MIDI 存取。

Clip 座標對應的 MIDI 音符：

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>音符：1</td><td>音符：6</td><td>音符：11</td><td>音符：16</td><td>音符：20</td></tr><tr><td><strong>y : 1</strong></td><td>音符：2</td><td>音符：7</td><td>音符：12</td><td>音符：17</td><td>……依此類推</td></tr><tr><td><strong>y : 2</strong></td><td>音符：3</td><td>音符：8</td><td>音符：13</td><td>音符：18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>音符：4</td><td>音符：9</td><td>音符：14</td><td>音符：19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>音符：5</td><td>音符：10</td><td>音符：15</td><td>音符：20</td><td></td></tr></tbody></table>

請注意，MIDI Note On 事件會啟動 Clip，對應的 Note Off 事件會停止 Clip。這不受群組上的觸發模式影響。這套系統原本是為播放與錄製設計，因此如果用音符切換 Clip 開/關，反而不合適。

### **效果**

在**第 15 通道**上的 MIDI Control Change (CC) 訊息會調整效果。\
效果 1 使用 CC 0-3，值為 0-127\
效果 2 使用 CC 4-7，值為 0-127\
效果 3 使用 CC 8-11，值為 0-127\
……依此類推。

每 4 個 CC 為一組，控制該效果的強度與 3 個參數：

<table><thead><tr><th width="164">效果：</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>強度</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>參數 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>……依此類推</td></tr><tr><td><strong>參數 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>參數 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **全域設定**

在**第 16 通道**上的 MIDI Control Change 訊息會變更全域設定：\
CC 1：Shift X（水平）0 -127，64 為置中\
CC 2：Shift Y（垂直）0 -127，64 為置中\
CC 4：Scale X\
CC 5：Scale Y\
CC 8：Rotation 3D (Y)\
CC 9：Rotation 2D (Z)

還有很重要的：\
CC 15：Global Brightness

請注意，這套系統原本是為錄製與播放設計，可讓您使用 Logic、Ableton 或其他 DAW 建立時間軸動畫。雖然您可以用它進行即時控制，但它尚未針對此用途最佳化；與 APC40 設定相比，部分即時控制功能並未提供。
