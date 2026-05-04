---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive システムは APC40 コントロールとは別の仕組みで、Liberation へ MIDI データを入力したり、Liberation から出力したりするためのものです。Clip の開始／停止、グローバル設定、エフェクト、Clip パラメーターの調整などの機能には、それぞれ対応する MIDI コマンドがあります。

{% hint style="info" %}
MIDI Send/Receive システムは、Liberation に Timeline 機能がまだなかった時期に最初に作られました。Logic Pro や Cubase などの音楽ソフトウェアにショーを録音し、再生するための回避策として使えるものでした。

表示状態や Clip Deck のスクロール位置に関係なく、Clip、エフェクト、設定を直接制御できます。tap tempo、zone の割り当て、arming/disarming など、よりシステム全体に関わるライブ制御機能は実装されていません。
{% endhint %}

### MIDI Send/Receive 設定

_MIDI Send/Receive_ パネルを開きます（メニューの _View -> MIDI Send/Receive_）。_SEND, RECEIVE,_ または送受信両方の _BOTH_ を選択でき、使用する MIDI インターフェースも選べます。

{% hint style="danger" %}
_BOTH_ 設定は注意して使用してください。MIDI デバイスやソフトウェアは、受信したデータを送り返すように設定できる場合があります。その場合、MIDI データのフィードバックループが発生する可能性があり、好ましくありません。
{% endhint %}

### MIDI マッピング

[MIDI 送受信のデフォルトマッピング](../reference/midi-send-receive-default-mapping.md "mention") を参照してください。

今後、より柔軟にカスタマイズできる MIDI マッピングを追加する予定ですが、それまでは [BOME](https://www.bome.com/products/miditranslator) や [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) などのアプリを使って、Liberation と独自のハードウェア間の変換を行えます。
