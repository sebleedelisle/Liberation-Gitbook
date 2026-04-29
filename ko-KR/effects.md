---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 효과

Liberation의 효과 시스템은 Clip 출력을 실시간으로 바꾸는 재미있고 다양한 방식입니다. 효과는 완전히 유연하게 사용할 수 있으며, 전체를 깜빡이게 하거나, 회전시키거나, 색상을 바꾸거나, 무작위로 움직이게 할 수도 있습니다!

Clip editor에서 할 수 있는 모든 작업을 효과로 사용할 수 있습니다. 실제로 효과는 Clip과 완전히 동일한 node editor로 편집합니다! [효과](effects.md#editing-effects)를 참고하세요. 창의적인 가능성은 사실상 무한합니다.

기본 효과 버튼 1-8은 zone 버튼 아래에 있으며, 효과 9-24는 하단의 작은 버튼입니다.

#### 효과 적용하기

효과 버튼을 눌러 효과를 켜거나 끌 수 있습니다. 더 좋은 방법은 APC40 슬라이더 1-8을 사용해 효과를 페이드 인/아웃하는 것입니다. APC40 없이 효과를 페이드 인하려면 버튼을 클릭한 뒤 위아래로 드래그하세요. 또는 효과 버튼을 우클릭하고 level 슬라이더를 조정하세요.

{% hint style="warning" %}
효과 버튼을 누르면 해당 효과가 즉시 활성화됩니다. 다만 level이 0으로 설정되어 있으면 아무 일도 일어나지 않습니다! 버튼을 클릭/드래그해 level을 변경하거나, 우클릭 후 _level_ 슬라이더를 사용하거나, APC40 fader를 사용하세요.
{% endhint %}

#### 효과와 Clip의 zone delay

효과는 현재 실행 중인 각 Clip의 zone delay 설정을 그대로 사용합니다. 따라서 Clip에 왼쪽에서 오른쪽으로 이동하는 delay가 있고 여기에 flashing 효과를 추가하면, flash도 왼쪽에서 오른쪽으로 delay됩니다.

{% hint style="info" %}
Clip의 zone delay가 효과에 상속되는 방식은 설명하기는 매우 어렵지만, 직접 사용해 보면 바로 이해되는 기능 중 하나입니다!

개인적으로는 Liberation에 내장된 가장 재미있고 창의적인 도구 중 하나라고 생각합니다. 한번 사용해 보면 무슨 뜻인지 알 수 있을 것입니다!
{% endhint %}

#### 효과 파라미터

_Parameter node_를 사용해 효과에 파라미터를 추가하세요. Parameter 시스템은 효과 내부의 여러 설정을 외부에서 조정하는 방법입니다. 자세한 내용은 [Parameter Control](clip-editor/oscillators/parameter-control.md)를 참고하세요.

rotary controller 1-8을 사용해 각 효과의 _parameter_를 조정합니다. 또는 효과 버튼을 우클릭하고 parameter 슬라이더를 조정하세요. parameter 변경은 효과가 어떻게 구성되어 있는지에 따라 서로 다른 동작을 합니다. 기본 효과와 각 파라미터의 동작은 아래 목록을 참고하세요.

{% hint style="info" %}
rotary controller 1-8은 APC40 Mk2의 상단, Mk1의 오른쪽 상단에 있습니다. 참고: [APC40 레퍼런스](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
효과 버튼에 보이는 작은 숫자는 효과의 _level_ 및 _parameter_를 의미합니다. _level_은 APC40의 fader로 제어하거나 버튼을 클릭-드래그해 조정할 수 있습니다. parameter는 APC40의 rotary로 조정하거나, 우클릭해 마우스로 조정할 수 있습니다.
{% endhint %}

#### 기본 효과

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Clip 출력에 혼란스러운 움직임을 적용합니다. parameter는 혼란의 양/속도를 조정합니다.
2. **Sine wave** :\
   모든 콘텐츠를 움직이는 sine wave를 따라 왜곡합니다. parameter는 파장을 조정합니다.
3. **Rotation** :\
   전체를 회전시킵니다. parameter는 회전 속도를 조정합니다.
4. **Horizontal flip** :\
   전체를 가로 방향으로 찌그러뜨리고 늘립니다. parameter는 속도를 조정합니다.
5. **Scale** :\
   전체 크기를 full에서 zero까지 반복해서 스케일합니다. parameter는 속도를 조정합니다.
6. **Hue** :\
   전체의 hue를 변경하지만 saturation은 변경하지 않습니다(즉, 흰색은 흰색으로 유지됩니다). parameter는 hue를 조정합니다.
7. **Saturation and hue** :\
   전체의 hue를 변경하고 색상을 완전히 saturate합니다(즉, 흰색도 해당 색상으로 바뀝니다). parameter는 hue를 조정합니다.
8. **Flash** :\
   전체 밝기를 full에서 zero까지 반복해서 깜빡입니다. parameter는 flash 속도를 조정합니다.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

하단 줄에는 사전 설정된 hue 및 saturation 값을 적용하는 16개의 추가 색상 효과가 있습니다.

이 효과들은 기본 효과일 뿐이며, 원하는 거의 모든 동작을 하도록 편집할 수 있습니다!

### 그룹에 적용

효과가 영향을 줄 그룹을 선택할 수 있습니다. 우클릭한 뒤 _Apply to groups_로 표시된 그룹 체크박스를 켜거나 끄세요.

저는 주로 Canvas 그래픽과 laser beam을 별도로 작업할 때 이 설정을 사용합니다. 모든 Canvas Clip을 group 5에 할당한 다음, 이러한 그래픽 Clip에 영향을 주고 싶지 않은 효과에서는 이 그룹을 제외합니다.

이 기능을 사용해 두 그룹의 laser에 서로 다른 두 가지 색상 변경을 동시에 라이브로 적용할 수도 있습니다. 색상 변경 효과 두 개를 만들고, 각 효과를 적용할 Clip group을 선택하세요.

### MX group

_Mutually Exclusive_의 약자로, 같은 그룹 안에서는 한 번에 하나의 효과만 활성화되도록 효과를 묶는 방식입니다. 기본 색상 변경 효과 중 하나만 동시에 활성화될 수 있다는 점을 확인해 보세요. 이는 모두 MX Group 1에 속해 있기 때문입니다.

_MX Group_ 설정이 0이면 이 기능은 비활성화됩니다.

### 효과 편집

아무 효과나 우클릭한 뒤 _EDIT EFFECT_ 버튼을 클릭하면 effect editor가 열립니다. 이 editor가 clip editor와 동일하다는 점을 확인할 수 있습니다!

일반 Clip을 편집하는 것과 같은 방식으로 효과를 편집하세요. [clip-editor](clip-editor/)를 참고하세요.

creator node가 최소 하나는 필요합니다. 이는 무엇이든 될 수 있지만(line, circle, shape, text까지도 가능), 효과 버튼 preview에서 가장 의미 있게 보이는 것을 선택하는 것이 좋습니다.

효과가 적용되면, 효과 안의 모든 creator node는 현재 실행 중인 Clip의 출력으로 대체됩니다.

{% hint style="warning" %}
매우 번거로운 기술적인 이유로, 효과 내부에서는 "trails" node가 활성화되지 않습니다. pattern node 안의 "delay" 설정도 마찬가지입니다(같은 시스템을 사용합니다). 이 문제는 향후 버전에서 수정될 예정입니다.
{% endhint %}
