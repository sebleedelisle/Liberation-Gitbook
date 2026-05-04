---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive 系統與 APC40 控制是分開的，它提供一種方式，讓 MIDI 資料可以進出 Liberation。啟動與停止 Clip、調整全域設定、效果與 Clip 參數等功能，都有對應的 MIDI 指令。

{% hint style="info" %}
MIDI Send/Receive 系統最初是在 Liberation 還沒有任何 Timeline 功能之前建立的；它是一種替代做法，可用來將演出錄製到 Logic Pro 或 Cubase 這類音樂軟體中，並從中播放回來。

它讓你可以直接控制 Clip、效果與設定，不受顯示畫面與 Clip Deck 捲動位置影響。較系統性的現場控制功能，例如 tap tempo、指定 zone，以及 arm/disarm，尚未實作。
{% endhint %}

### MIDI Send/Receive 設定

開啟 _MIDI Send/Receive_ panel（從選單 _View -> MIDI Send/Receive_）。你會看到可以選擇 _SEND、RECEIVE_ 或 _BOTH_ 傳送與接收，也可以選擇要使用哪些 MIDI 介面。

{% hint style="danger" %}
請謹慎使用 _BOTH_ 設定。MIDI 裝置與軟體可以設定成把收到的資料再送回去，這可能會造成 MIDI 資料的回授迴圈，這可不是好事！
{% endhint %}

### MIDI mapping

請參閱 [MIDI 傳送/接收預設對應](../reference/midi-send-receive-default-mapping.md "mention")

我計畫未來加入更可自訂的 MIDI mapping；在此之前，你可以使用 [BOME](https://www.bome.com/products/miditranslator) 和 [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) 這類應用程式，在 Liberation 與你的自訂硬體之間轉換 MIDI 資料。
