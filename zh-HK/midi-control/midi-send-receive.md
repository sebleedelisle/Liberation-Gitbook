---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive 系統與 APC40 控制分開運作，用於將 MIDI 資料傳入及傳出 Liberation。啟動和停止 clips、調整全域設定、effects 及 clip 參數等功能，都有相應的 MIDI 指令。

{% hint style="info" %}
MIDI Send/Receive 系統最初是在 Liberation 尚未有任何 Timeline 功能之前建立；當時這是一個變通方法，讓你可以將 show 錄製到 Logic Pro 或 Cubase 等音樂軟件中，並從中播放。

它讓你可以直接控制 clips、effects 及 settings，不受顯示畫面和 clip deck 捲動位置影響。較系統性的現場控制功能，例如 tap tempo、指派 zones，以及 arming/disarming，則未有實作。
{% endhint %}

### MIDI Send/Receive 設定

開啟 _MIDI Send/Receive_ panel（使用選單 _View -> MIDI Send/Receive_）。你會看到可以選擇 _SEND, RECEIVE,_ 或 _BOTH_ 傳送和接收，亦可以選擇要使用哪些 MIDI interfaces。

{% hint style="danger" %}
請小心使用 _BOTH_ 設定。MIDI 裝置和軟件可以設定為把接收到的資料再傳送出去，這可能會造成 MIDI 資料 feedback loop，並不是好事！
{% endhint %}

### MIDI 對應

請參閱 [MIDI 傳送／接收預設對應](../reference/midi-send-receive-default-mapping.md "mention")

我計劃日後加入更高度自訂的 MIDI mapping；在此之前，你可以使用 [BOME](https://www.bome.com/products/miditranslator) 和 [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) 等應用程式，在 Liberation 和你的自訂硬件之間轉換資料。
