---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

들어오는 모든 콘텐츠의 색상을 변경합니다. 고정 HSB 값을 설정하거나, 그라디언트 시스템으로 전환해 사용자 지정 그라디언트에서 색상을 샘플링할 수 있습니다.

* **hue, saturation, brightness** - 색상 값입니다. [색상 설정 및 HSB](../fundamentals/colour-settings-and-hsb.md "mention")를 참고하세요.
* **hue mode** -
  * OFF - hue가 변경되지 않습니다.
  * FIXED - 요소의 hue가 hue 값으로 설정됩니다.
  * SHIFT - 요소의 hue가 해당 값만큼 오프셋됩니다. 따라서 서로 다른 색상의 요소는 서로 다른 상태를 유지하면서 hue 값에 따라 이동됩니다.
* **saturation mode** -
  * OFF - saturation이 변경되지 않습니다.
  * FIXED - saturation이 지정한 값으로 고정됩니다.
* **brightness mode** -
  * OFF - brightness가 변경되지 않습니다.
  * FIXED - 요소의 brightness가 brightness 값으로 설정됩니다.
  * MULTIPLY - 요소의 brightness가 brightness 값과 결합됩니다. 따라서 깜빡이는 요소는 계속 깜빡이지만, 여기서 지정한 brightness까지만 표시됩니다.
* **gradient mode** - 고정 HSB 슬라이더 대신 그라디언트 편집기로 전환합니다. 이 node는 그라디언트에서 색상 하나를 샘플링한 다음, 위의 색조, 채도, 밝기 모드를 사용해 적용합니다.
* **gradient position** - 그라디언트에서 어느 지점을 샘플링할지 선택합니다. Sawtooth Oscillator로 이 값을 0%에서 100%까지 애니메이션하면 시간에 따라 그라디언트를 순환할 수 있습니다.
* **blend** - Colour changer가 적용되는 강도입니다. 0%는 전혀 적용하지 않음, 100%는 완전히 적용함, 50%는 기존 색상과 새 값을 조합한 상태입니다.

{% hint style="info" %}
Colour Change node는 전체 입력에 대해 그라디언트에서 색상 하나를 샘플링합니다. 위치에 따라 도형 전체에 그라디언트가 적용되도록 하려면 대신 [위치 기반 변경 node](position-based-changers.md "mention")를 사용하세요.
{% endhint %}

### 그라디언트 편집기

**gradient mode**가 켜져 있으면 기본 컨트롤 아래에 그라디언트 편집기가 나타납니다.

* 그라디언트 바를 클릭해 색상 스톱을 추가합니다.
* 스톱을 왼쪽 클릭해 선택한 다음, 좌우로 드래그해 이동합니다.
* 선택한 스톱을 바에서 아래로 멀리 드래그하거나 Delete/Backspace를 눌러 제거합니다. 그라디언트에는 항상 최소 두 개의 스톱이 유지됩니다.
* 스톱을 오른쪽 클릭해 색상 선택기로 편집합니다.
* **Position**, **Hue**, **Saturation**, **Brightness**를 사용해 선택한 스톱을 정확하게 편집합니다.
* **interpolation**은 스톱 사이에서 색상이 혼합되는 방식을 선택합니다.
* **HSB** - 색조, 채도, 밝기를 혼합합니다. 색상환을 따라 부드럽게 움직이는 무지개 스타일 표현에 가장 적합합니다.
* **RGB** - 빨강, 초록, 파랑 값을 직접 혼합합니다. 화면이나 조명 콘솔의 컬러 페이드에 더 가깝게 느껴지는 경우가 많습니다.
* **NONE** - 혼합 없이 한 스톱에서 다음 스톱으로 즉시 전환합니다.
* **hue direction**은 HSB 보간에서 사용할 수 있습니다.
* **AUTO** - 색조 휠에서 가장 짧은 경로를 사용합니다.
* **FORWARDS** - 항상 색조 값을 정방향으로 진행합니다.
* **BACKWARDS** - 항상 색조 값을 역방향으로 진행합니다.
