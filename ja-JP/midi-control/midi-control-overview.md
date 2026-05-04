---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI control の概要

Liberation では、MIDI をいくつかの方法で使用できます。

* ライブコントローラーとして。APC40 Mk1/Mk2、APC Mini、MIDI Fighter Twister は、対応するデバイスが利用可能な場合に自動接続できます。詳しくは [ライブ MIDI コントローラー](live-control-with-the-apc40.md "mention") を参照してください。
* MIDI clock と MIDI song position メッセージを使用したクロック同期ソースとして。詳しくは [MIDI clock](../tempo-synchronisation.md#midi-clock "mention") を参照してください。
* MIDI notes node へのインタラクティブ入力として使用し、「レーザーハープ」風のエフェクトを作成できます。詳しくは [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention") を参照してください。
* MIDI Send/Receive システムを使用した、より汎用的な入力／出力システムとして。詳しくは [MIDI Send/Receive](midi-send-receive.md "mention") を参照してください。

対応しているライブコントローラーは、Liberation の画面上の状態に追従します。Clip ボタンは各グループの色で点灯し、zone ボタンは zone の状態を表示します。また、マッピング済みのノブやエンコーダーは、現在のエフェクトまたは Parameters パネルのコントロールに追従します。
