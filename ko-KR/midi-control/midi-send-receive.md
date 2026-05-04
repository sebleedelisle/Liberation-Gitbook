---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive 시스템은 APC40 컨트롤과 별개로 동작하며, Liberation 안팎으로 MIDI 데이터를 주고받기 위한 방법입니다. 클립 시작/정지, 글로벌 설정 조정, 이펙트 및 클립 파라미터 같은 기능에는 각각 연결된 MIDI 명령이 있습니다.

{% hint style="info" %}
MIDI Send/Receive 시스템은 Liberation에 Timeline 기능이 생기기 전에 처음 만들어졌습니다. Logic Pro나 Cubase 같은 음악 소프트웨어에 쇼를 녹음하고 재생하기 위해 사용할 수 있는 우회 방법이었습니다.

디스플레이와 Clip Deck 스크롤 위치와 관계없이 클립, 이펙트, 설정을 직접 제어할 수 있습니다. tap tempo, zone 할당, arming/disarming 같은 더 시스템적인 라이브 제어 기능은 구현되어 있지 않습니다.
{% endhint %}

### MIDI Send/Receive 설정

_MIDI Send/Receive_ 패널을 엽니다(메뉴 _View -> MIDI Send/Receive_). 사용할 MIDI 인터페이스를 선택할 수 있으며, _SEND, RECEIVE,_ 또는 _BOTH_ 중에서 송신과 수신 방식을 선택할 수 있습니다.

{% hint style="danger" %}
_BOTH_ 설정은 주의해서 사용하세요. MIDI 장치와 소프트웨어는 입력받은 데이터를 다시 보내도록 설정될 수 있습니다. 이 경우 MIDI 데이터의 피드백 루프가 발생할 수 있으며, 이는 좋지 않습니다!
{% endhint %}

### MIDI 매핑

[MIDI 송수신 기본 매핑](../reference/midi-send-receive-default-mapping.md "mention")을 참조하세요.

앞으로 훨씬 더 사용자 지정이 가능한 MIDI 매핑을 추가할 계획입니다. 그전까지는 [BOME](https://www.bome.com/products/miditranslator) 및 [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) 같은 앱을 사용해 Liberation과 사용자 지정 하드웨어 사이의 MIDI 데이터를 변환할 수 있습니다.
