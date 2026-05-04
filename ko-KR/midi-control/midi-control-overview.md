---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 MIDI 제어 개요

Liberation에서 MIDI를 사용하는 방법은 여러 가지가 있습니다.

* 라이브 컨트롤러로 사용합니다. 일치하는 장치가 사용 가능하면 APC40 Mk1/Mk2, APC Mini 및 MIDI Fighter Twister가 자동으로 연결될 수 있습니다. [라이브 MIDI 컨트롤러](live-control-with-the-apc40.md "mention")를 참조하세요.
* MIDI clock 및 MIDI song position 메시지를 사용하는 클록 동기화 소스로 사용합니다. [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")을 참조하세요.
* MIDI notes node에서 “laser harp” 스타일 효과를 만들기 위한 인터랙티브 입력으로 사용합니다. [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")를 참조하세요.
* MIDI Send/Receive 시스템을 사용한 보다 일반적인 입출력 시스템으로 사용합니다. [MIDI Send/Receive](midi-send-receive.md "mention")를 참조하세요.

지원되는 라이브 컨트롤러는 Liberation의 화면 상태를 따릅니다. Clip 버튼은 해당 그룹 색상으로 켜지고, zone 버튼은 zone 상태를 표시하며, 매핑된 노브나 인코더는 현재 효과 또는 Parameters 패널의 컨트롤을 따라갑니다.
