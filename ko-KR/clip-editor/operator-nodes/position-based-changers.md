---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 위치 기반 변경 노드

이 계열의 노드는 위치에 따라 콘텐츠를 변경합니다. 기본적으로 효과는 가로 축(왼쪽에서 오른쪽) 방향으로 적용되지만, 이 축을 원하는 각도로 회전할 수 있습니다. 각 노드에는 _radial_ 모드도 포함되어 있으며, 이 모드에서는 중심을 기준으로 각 포인트가 이루는 각도에 따라 효과가 적용됩니다.

* **Colour Changer by Position** – 선택한 축을 따라 또는 radial 각도 주변으로 색상을 이동합니다.\
  \&#xNAN;_예: 선을 가로지르는 무지개 그라디언트를 만들거나, 원에 radial 모드를 사용해 컬러 휠 효과를 만들 수 있습니다._
* **Wave Shift by Position** – 사인파 왜곡을 적용하여 콘텐츠를 세로 방향(또는 선택한 축에 수직인 방향)으로 오프셋합니다.\
  \&#xNAN;_예: 선이 물결처럼 흔들리게 만들거나, radial 모드를 사용해 원이 중심에서 바깥쪽으로 맥동하게 만들 수 있습니다._
* **Noise Shift by Position** – simplex noise 왜곡을 적용하여 콘텐츠를 세로 방향(또는 선택한 축에 수직인 방향)으로 오프셋합니다.\
  \&#xNAN;_예: Wave Shift 예와 비슷하지만 더 유기적이고 무작위적인 느낌을 만들 수 있어, 자연스러운 변화를 추가하기에 적합합니다._

## &#x20;위치에 따른 색상 변경

이 노드는 위치를 기준으로 콘텐츠 전체에 색상 변화를 적용합니다. 기본 축은 가로(0°)이지만, 축을 회전하거나 radial 모드로 전환할 수 있습니다.

* **wavelength** – 반복되는 색상 주기의 크기를 설정합니다.
  * _Linear 모드:_ 100%에서는 전체 콘텐츠 너비에 한 번의 전체 주기가 걸쳐집니다.
  * _Radial 모드:_ 100%에서는 전체 원(360°)에 한 번의 전체 주기가 걸쳐집니다. 값은 원의 백분율입니다. 예: 50% = 반원(180°).
* **offset** – 색상 주기의 시작점을 wavelength의 백분율로 이동합니다. 이 값을 변조하면(예: sawtooth oscillator 사용) 색상을 부드럽게 순환시킬 수 있습니다.
* **repeat** – 활성화하면 주기가 콘텐츠 전체에서 반복됩니다. 비활성화하면 그라디언트가 한 번만 적용됩니다. 시작 전의 모든 부분은 시작 색상, 끝 이후의 모든 부분은 끝 색상이 됩니다.
* **pingpong** – 활성화하면 각 반복이 반대 방향으로 번갈아 진행되어 미러 효과가 만들어집니다. _Repeat_가 비활성화되어 있으면 그라디언트가 한 번 앞으로 진행한 뒤 다시 돌아옵니다. _참고: Pingpong 모드에서는 wavelength가 전진 및 복귀 스윕을 모두 포함합니다._
* **linear angle** – 효과의 축을 회전합니다. 0° = 가로.
* **radial** – radial 모드로 전환하여 중심으로부터의 각도를 기준으로 색상을 적용합니다.
* **radial smooth loop** – wavelength가 원의 100%에 균등하게 나누어지도록 자동 조정하여, 주기가 감기는 지점에 보이는 이음새가 생기지 않게 합니다.

**색상 모드**

이 설정들은 색상 조정의 어떤 요소를 콘텐츠에 적용할지 결정합니다. 참고: [색상 설정 및 HSB](../fundamentals/colour-settings-and-hsb.md).

* **hue mode**
  * _OFF_ – hue가 변경되지 않습니다.
  * _FIXED_ – hue가 고정값으로 설정됩니다.
  * _SHIFTED_ – hue가 지정한 양만큼 오프셋됩니다. 서로 다른 색상의 요소들은 구분을 유지한 채, 컬러 휠을 따라 함께 이동합니다.
* **saturation mode**
  * _OFF_ – saturation이 변경되지 않습니다.
  * _FIXED_ – saturation이 지정한 값으로 설정됩니다.
* **brightness mode**
  * _OFF_ – brightness가 변경되지 않습니다.
  * _FIXED_ – brightness가 지정한 값으로 설정됩니다.
  * _MULTIPLY_ – brightness가 지정한 값에 따라 스케일됩니다. 이 방식은 동적인 변화를 유지합니다. 예를 들어 깜박이는 요소는 계속 깜박이지만, 제한된 밝기 범위 안에서 동작합니다.

**시작 / 끝 값**

이 슬라이더들은 선택한 축(또는 radial 스윕)을 따라 적용되는 색상 범위를 정의합니다.

* **start hue** – 그라디언트 시작 지점의 hue입니다.
* **end hue** – 그라디언트 끝 지점의 hue입니다.
* **start saturation** – 시작 지점의 saturation입니다.
* **end saturation** – 끝 지점의 saturation입니다.
* **start brightness** – 시작 지점의 brightness입니다.
* **end brightness** – 끝 지점의 brightness입니다.
* **blend** – 색상 변화를 원래 색상과 혼합합니다. 100%에서는 효과가 원래 색상을 완전히 대체합니다.

**예제 1: 슬라이딩 무지개 그라디언트**

기본 설정에서 시작합니다:

1. 노드를 **Linear** 모드로 둡니다(0° angle = 가로).
2. **wavelength**를 100%로 둡니다(전체 너비에 걸치며, 기본값이어야 합니다).
3. 시작값과 끝값은 기본값으로 둡니다.
4. **repeat**를 활성화합니다.
5. 0%에서 100%까지 이동하는 **Sawtooth Oscillator**를 **offset** 설정에 추가합니다.

***

**예제 2: 검정–흰색–검정 그라디언트(Pingpong)**

기본 설정에서 시작합니다:

1. 노드를 **Linear** 모드로 둡니다(0° angle = 가로).
2. **wavelength**를 100%로 둡니다(전체 너비에 걸치며, 기본값이어야 합니다).
3. **repeat**를 끕니다.
4. **start brightness**를 0(검정)으로 설정합니다.
5. **end brightness**를 100(흰색)으로 설정합니다.
6. **start saturation**과 **end saturation**을 0으로 설정합니다(그레이스케일로 변환).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. **pingpong**을 활성화합니다.

_결과: 그라디언트가 너비를 따라 검정에서 흰색으로, 다시 검정으로 페이드됩니다._\
콘텐츠의 hue와 saturation을 유지하려면 Saturation mode를 OFF로 설정하세요. \\

***

**예제 3: 회전하는 무지개 휠(Radial)**

1. **radial** 모드를 활성화합니다.
2. **wavelength**를 100%로 설정합니다(전체 360° 스윕).
3. **repeat**를 켭니다.
4. 0%에서 100%까지 이동하는 **Sawtooth Oscillator**를 **offset** 설정에 추가합니다.

_결과: 원 주위를 계속 회전하는 이음새 없는 컬러 휠이 만들어집니다._

## &#x20;위치에 따른 Wave shift

이 노드는 콘텐츠 전체에 wave 왜곡을 적용하여, 선택한 축에 수직인 방향(또는 중심에서 radial 방향)으로 포인트를 이동합니다.

* **Wavelength** – wave 주기의 길이를 설정합니다.
  * _Linear 모드:_ 100%에서는 전체 콘텐츠 너비에 한 번의 전체 주기가 걸쳐집니다.
  * _Radial 모드:_ 100%에서는 전체 360°에 한 번의 전체 주기가 걸쳐집니다. (값은 원의 백분율입니다. 50% = 반 바퀴, 25% = 1/4 바퀴 등.)
* **Size** – wave의 진폭을 제어합니다(콘텐츠가 이동하는 거리).
* **Offset** – 축을 따라 wave를 이동합니다(radial 모드에서는 원 둘레를 따라 이동). 이 값은 wavelength의 백분율이므로, **Oscillator Node**로 애니메이션하여 wave가 진행하는 효과를 만들 수 있습니다.
* **Radial** – linear 모드에서 radial 모드로 전환하여, 중심으로부터의 각도를 기준으로 displacement가 적용되도록 합니다.
* **Radial Smooth Loop** – wavelength가 원의 100%에 균등하게 나누어지도록 조정하여, 감기는 지점에 보이는 이음새가 생기지 않게 합니다.
* **Triangle** – 파형 모양을 sine에서 triangle로 변경합니다.
* **Absolute** – wave의 절댓값을 사용하여 위쪽 displacement만 만듭니다(음수 쪽을 양수 쪽으로 접습니다).
* **Angle** – wave의 축을 회전합니다. 0° = 가로.

## &#x20;위치에 따른 Noise shift

이 노드는 turbulence와 같은 noise field를 사용해 콘텐츠를 왜곡하며, 선택한 축에 수직인 방향(또는 중심에서 radial 방향)으로 포인트를 이동합니다. _Wave Shift_와 비교하면 결과가 더 유기적이고 무작위적입니다.

* **Detail** – noise의 세밀함을 제어합니다. 값이 높을수록 더 선명하고 디테일한 변화가 만들어집니다. 값이 낮을수록 변화가 더 부드러워집니다.
* **Wavelength** – noise 패턴의 스케일을 설정합니다.
  * _Linear 모드:_ 100%에서는 noise의 한 전체 주기가 콘텐츠 너비에 걸쳐집니다.
  * _Radial 모드:_ 100%에서는 한 전체 주기가 전체 360°에 걸쳐집니다.
* **Size** – displacement 양(noise 왜곡의 진폭)을 제어합니다.
* **Offset** – 축을 따라 noise 패턴을 이동합니다(또는 원 둘레를 따라 이동). 이 값은 wavelength의 백분율이므로, **Oscillator Node**로 애니메이션하여 noise가 “흐르는” 효과를 만들 수 있습니다.
* **Depth Offset** – 3D noise field를 따라 이동하여 시간에 따른 변화를 만듭니다. Oscillator Node로 애니메이션할 때 특히 효과적입니다.
* **Depth Detail** – depth 차원에서 변화가 얼마나 디테일하게 나타나는지 제어합니다.
* **Absolute** – noise의 절댓값을 사용하여 음수 값을 양수로 접습니다(한쪽 방향의 displacement만 생성).
* **Radial** – linear 모드에서 radial 모드로 전환하여, 중심으로부터의 각도를 기준으로 displacement가 적용되도록 합니다.
* **Radial Smooth Loop** – wavelength가 원의 100%에 균등하게 나누어지도록 조정하여, radial 모드에서 보이는 이음새가 생기지 않게 합니다.
