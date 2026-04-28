---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ 지연 시간 설정

_Settings_ 패널(_Liberation->Settings_ 또는 CMD/CTRL ,)에서 _Latency(ms)_ 라벨이 붙은 슬라이더를 볼 수 있습니다. (이전 버전의 Liberation에서는 Laser Overview 패널에 있었습니다.)

{% hint style="info" %}
기본 지연 시간 설정인 150ms는 대부분의 경우에 적합합니다. 다만 네트워크 문제가 있다면 값을 높여 보는 것이 좋습니다.
{% endhint %}

### 자세한 설명

이 "프레임 지연 시간" 설정은 Liberation이 프레임을 생성한 시점부터 레이저가 해당 프레임 출력을 시작할 때까지의 최대 시간입니다. 이 값을 높이면 Liberation과 레이저 출력 사이에 약간의 지연이 느껴질 수 있습니다.

프레임 지연 시간을 길게 설정하면 Liberation이 가능한 한 빨리 레이저 컨트롤러의 버퍼를 콘텐츠로 채울 수 있습니다. 따라서 네트워크에 혼잡이 발생해도 컨트롤러에 포인트가 부족해질 가능성이 줄어듭니다.

이 설정은 보통 네트워크 DAC에만 해당되며, 100ms 정도가 속도와 네트워크 지연에 대한 보호 사이의 좋은 균형입니다. 네트워크 상태가 매우 좋다면 50ms까지 낮출 수 있습니다.&#x20;
