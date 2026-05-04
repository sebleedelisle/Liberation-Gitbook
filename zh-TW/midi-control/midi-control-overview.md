---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI 控制概觀

Liberation 使用 MIDI 的方式有幾種：

* 作為現場控制器使用。當對應裝置可用時，APC40 Mk1/Mk2、APC Mini 與 MIDI Fighter Twister 可以自動連線。請參閱[現場 MIDI 控制器](live-control-with-the-apc40.md "mention")。
* 使用 MIDI clock 與 MIDI song position 訊息作為時脈同步來源。請參閱 [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* 在 MIDI notes node 上作為互動式輸入，用來製作「雷射豎琴」風格的效果。請參閱 [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* 使用 MIDI Send/Receive 系統作為較通用的輸入/輸出系統。請參閱 [MIDI Send/Receive](midi-send-receive.md "mention")

支援的現場控制器會跟隨 Liberation 畫面上的狀態：Clip 按鈕會以其群組顏色亮起，zone 按鈕會顯示 zone 狀態，而已映射的旋鈕或編碼器會跟隨目前的效果或 Parameters 面板控制項。
