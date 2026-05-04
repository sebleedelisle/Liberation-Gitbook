---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / 동기화

음악 동기화는 Liberation의 핵심 요소입니다. 음악의 템포와 비트를 맞추면 모든 요소가 동기화된 상태로 동작합니다. MIDI clock(또는 Ableton Link)을 사용할 수 있다면 수동 동기화는 전혀 신경 쓰지 않아도 됩니다. 그렇지 않더라도 걱정하지 마세요. _Live_ tempo 기능을 사용해 수동으로 맞출 수 있습니다.

음악 또는 조명 소프트웨어를 사용해 본 경험이 있다면 이 과정이 익숙할 것입니다. 그렇지 않다면 라이브 쇼에 들어가기 전에 집에서 시스템에 익숙해지고 충분히 연습해 두는 것이 좋습니다.

## Tempo 패널

_Tempo_ 패널은 항상 화면에 표시되며 모든 동기화 설정을 포함합니다. 상단에는 현재 마디/비트 카운터와 재생/일시정지, 되감기/빨리감기 버튼이 있는 트랜스포트가 표시됩니다.

그 아래에는 비트 마커가 표시됩니다. 비트에 맞춰 "깜박이는" 네 개의 사각형입니다. 이 _beat marker_ 는 매우 유용한 시각화 도구이며, _Live_ tempo 시스템을 사용할 때 계속 참고하게 됩니다.

### 템포 설정

템포를 설정하는 방법은 다음과 같습니다.

* _Tempo_ 슬라이더를 클릭한 채 드래그
* _Tempo_ 슬라이더를 Shift-클릭한 채 드래그하여 0.1 단위로 변경
* _Tempo_ 슬라이더를 더블 클릭하고 숫자를 직접 입력
* APC40의 _Tempo_ 노브 사용(0.1 단위로 조정하려면 Shift 누르기)
* Tap Tempo

{% hint style="info" %}
Tempo는 "분당 비트 수(beats per minute)"로 정의되며, 일반적인 기본값은 보통 120입니다.
{% endhint %}

## Tap Tempo

비트에 맞춰 _TAP_ 버튼을 클릭하면 템포가 자동으로 설정됩니다. _RESET_ 버튼으로 마디의 시작점을 설정합니다.

{% hint style="info" %}
Tap Tempo 시스템은 잠시 탭을 쉬었거나 몇 개의 비트를 놓친 경우도 인식할 수 있을 만큼 똑똑합니다. 더블 타임으로 탭하기 시작하면 템포를 두 배로 설정하려는 것으로 이해하며, 하프 타임으로 탭하는 경우도 마찬가지로 인식합니다.

또한 두 사람이 동시에 템포를 탭하는 경우(예: 한 명은 키보드, 한 명은 APC40)도 파악할 수 있습니다. Liberation은 중복 탭을 평균 처리합니다.
{% endhint %}

#### 키보드 명령:

T - tap tempo\
R - 마디 reset\
Y - 템포를 가장 가까운 분당 비트 수로 반올림

{% hint style="info" %}
요즘 대부분의 음악은 디지털 방식으로 제작되므로 템포가 반올림된 정수일 가능성이 높습니다. 따라서 탭한 템포가 거의 맞는 것 같다면 Y 키를 사용하거나(APC40 tempo 노브를 한 "틱" 움직여) 정수로 반올림하세요.
{% endhint %}

#### APC40 컨트롤:

APC40에는 전용 _TAP TEMPO_ 버튼이 있으며, 연결된 풋스위치를 사용해 발로 탭할 수도 있습니다!

_TEMPO_ 노브를 사용해 조정합니다. 미세 조정을 하려면 _TEMPO_ 노브를 사용하는 동안 _SHIFT_ 를 누르세요.

_METRONOME_ 버튼을 사용해 **마디를 reset**합니다. (_METRONOME_ 버튼도 비트에 맞춰 켜집니다.)

_TEMPO_ 노브를 오른쪽 또는 왼쪽으로 한 "틱" 돌리면 **템포를 반올림**하여 정수 BPM 값으로 올리거나 내릴 수 있습니다.

[APC40 레퍼런스](reference/apc40-reference.md "mention")도 참고하세요.

### Nudge tempo

실제 템포에 충분히 가깝게 맞췄다고 생각하지만 시간이 지나면서 박자가 어긋난다면 _NUDGE_ 버튼을 사용해 보정하세요.

Liberation 템포가 음악보다 앞서가고 있다면, 다시 맞을 때까지 _NUDGE -_ 를 길게 눌러 일시적으로 느리게 만듭니다.

Liberation 템포가 음악보다 뒤처지고 있다면, 다시 맞을 때까지 _NUDGE +_ 를 길게 눌러 일시적으로 빠르게 만듭니다.

{% hint style="info" %}
화면의 NUDGE 버튼을 사용하거나 APC40의 전용 버튼을 사용할 수 있습니다.
{% endhint %}

### Half time / double time

_÷2_ 및 _x2_ 버튼을 사용해 템포를 영구적으로 절반 또는 두 배로 변경합니다. Tempo Multiplier와 달리, 현재 템포 자체에 적용되는 영구 변경입니다.

## Tempo Multiplier

_Tempo Multiplier_ 시스템을 사용하면 이전 템포로 돌아가기 전에 템포를 일시적으로 조정할 수 있습니다.

_TEMPO MULTIPLIER_ 버튼 또는 APC40의 _BANK_ 버튼을 눌러 _Tempo Multiplier_ 를 토글합니다. 화면 슬라이더 또는 APC40 A-B 슬라이더로 조정합니다. 또는 _25%, 50%, 100% 200%_ 프리셋 버튼을 사용합니다.

## 외부 템포 소스

### MIDI Clock

외부 MIDI clock 신호에 동기화하려면 _MIDI CLOCK_ 라디오 버튼을 선택하고 드롭다운 메뉴에서 MIDI 장치를 선택합니다. 드롭다운 메뉴 옆의 색상 상태 표시등을 확인하세요.

* Green - MIDI clock 신호를 수신 중
* Orange - MIDI 장치에 연결할 수 있지만 현재 clock 신호가 없음
* Red - MIDI 장치에 연결할 수 없음

{% hint style="info" %}
MIDI Clock은 일련의 프레임(4분음표당 24개)을 브로드캐스트하지만, 메시지 안에는 위치 데이터가 없습니다. 즉, 박자를 유지하는 데는 도움이 되지만 마디는 여전히 reset해야 할 수 있습니다.

Liberation MIDI Clock tempo 소스는 **MIDI Machine Control (MMC)** 메시지에도 반응하므로, clock 소스가 이를 전송한다면 마디를 수동으로 reset할 필요가 없습니다.
{% endhint %}



### Ableton Link

Ableton Link와 동기화하려면 템포 소스로 _ABLETON LINK_ 를 선택합니다. Liberation은 로컬 네트워크의 Link 세션에 참여하고, 다른 Link 지원 앱에서 공유되는 템포와 비트 위상을 따릅니다.

Ableton Link는 MIDI 포트를 사용하지 않으며, 절대적인 곡 위치 정보도 전달하지 않습니다. Liberation의 마디 시작을 쇼의 특정 순간에 맞춰야 하는 경우 마디 리셋 컨트롤을 사용하세요.

### Timeline

각 timeline에는 고유한 템포가 있으며, 고정값이거나 _Tempo Map_ 일 수 있습니다. _Tempo Map_ 을 사용하면 timeline 내 특정 시점에서 템포를 조정할 수 있습니다.

템포 소스로 _TIMELINE_ 을 선택하면 timeline 템포가 사용됩니다.

{% hint style="info" %}
어떤 템포 소스와도 timeline을 함께 실행할 수 있습니다! 예를 들어 클릭에 맞춰 연주하지 않는 라이브 밴드라면 timeline을 수동으로 시작한 뒤 _LIVE_ tempo 소스를 사용해 동기화를 유지할 수 있습니다. MIDI clock 신호가 있다면 그것을 사용할 수도 있습니다!
{% endhint %}
