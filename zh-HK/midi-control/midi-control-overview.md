---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI 控制概覽

Liberation 可以透過幾種方式使用 MIDI：

* 作為現場控制器使用。APC40 Mk1/Mk2、APC Mini 及 MIDI Fighter Twister 在有相應裝置可用時可自動連接。請參閱 [現場 MIDI 控制器](live-control-with-the-apc40.md "mention")。
* 作為時鐘同步來源，使用 MIDI clock 及 MIDI song position 訊息。請參閱 [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* 作為 MIDI notes node 上的互動輸入，用來製作「laser harp」風格效果。請參閱 [MIDI 音符](../clip-editor/operator-nodes/midi-notes.md "mention")
* 透過 MIDI Send/Receive 系統，作為較通用的輸入／輸出系統。請參閱 [MIDI Send/Receive](midi-send-receive.md "mention")

支援的現場控制器會跟隨 Liberation 畫面上的狀態：Clip 按鈕會以所屬群組顏色亮起，zone 按鈕會顯示 zone 狀態，而已對應的旋鈕或編碼器會跟隨目前效果或 Parameters panel 的控制項。
