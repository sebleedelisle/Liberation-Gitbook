---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Wave oscillators

## 이 페이지의 내용 :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sawtooth wave](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Triangle wave](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sine wave](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Square wave](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Wave oscillator 설정

모든 Wave oscillator에는 다음 설정이 있습니다 :

* **range min / range max** - oscillator가 제어하는 속성의 값 범위를 정합니다. 파형이 가장 아래에 있을 때 속성은 _range min_으로 설정되고, 가장 위에 있을 때 _range max_로 설정됩니다.

{% hint style="info" %}
예를 들어 점이 -100과 100 사이에서 좌우로 움직이게 하려면 oscillator를 _x property socket_에 연결하고, _min range_를 -100, _max range_를 100으로 설정합니다.
{% endhint %}

* **duration** - 한 번의 전체 사이클(또는 _loop_)이 완료되는 데 걸리는 시간입니다. 마디 단위의 템포를 기준으로 합니다. 따라서 ¼은 한 박자, 1은 한 마디입니다.
* **duration multiplier** - 기본 duration에 선택한 배율을 적용합니다. 예를 들어 duration이 4분음표로 설정되어 있고 multiplier가 3이면 oscillator는 4분음표 세 개 길이(점2분음표) 동안 지속됩니다. 소수 배율도 지원됩니다. 슬라이더를 드래그하는 동안 _SHIFT_를 누르면 정수가 아닌 값을 설정할 수 있으며, 페이징 효과나 미묘한 타이밍 변화를 만들 때 유용합니다.
* **offset** - duration에 대한 백분율로 지정하는 파형의 시작 오프셋입니다. 파형을 1/4 지점부터 시작하고 싶다면 25%로 설정합니다.
* **repeat count** - loop가 멈추기 전까지 반복되는 횟수입니다. 기본값은 _FOREVER_이지만, oscillator가 무한히 실행되지 않게 하려면 변경할 수 있습니다. 멈춘 후에는 속성이 파형 끝의 값으로 설정됩니다.
* **delay count** - oscillator가 실행되기 전까지의 지연 시간으로, 박자 단위입니다. 실행되기 전에는 속성이 파형 시작의 값으로 설정됩니다.

{% hint style="info" %}
_repeat count_와 _delay count_를 잘 활용하면 마치 자체 타임라인처럼 매우 복잡한 애니메이션을 만들 수 있습니다!
{% endhint %}

## 공통 설정

* **steps** - 움직임을 여러 개의 개별 단계로 나눕니다. 속성이 부드럽게 움직이기보다 특정 값으로 “점프”하게 만들고 싶을 때 좋습니다.

{% hint style="info" %}
steps는 값이 아니라 시간을 기준으로 나뉩니다. 따라서 duration이 1마디인 파형을 4 steps로 나누면 속성이 매 박자마다 즉시 변경됩니다.
{% endhint %}

* **clamp min / clamp max -** 파형의 스케일을 최소값 또는 최대값 너머로 늘린 뒤 결과를 클램프합니다.

{% hint style="info" %}
_clamp_ 개념은 설명하기가 조금 어렵지만, 파형이 그래프의 위쪽이나 아래쪽을 벗어난 뒤 가장자리에서 잘려 고정된다고 생각하면 됩니다. 직접 실험해 보는 것을 권장합니다! 특히 sawtooth가 늦게 시작되거나 일찍 끝나게 만들고 싶을 때 매우 유용합니다.
{% endhint %}

* **ease function** - Sawtooth와 Triangle wave에는 애니메이션 곡선을 미묘하게 바꾸는 ease function도 있습니다. 이를 사용하면 애니메이션을 훨씬 더 표현력 있게 만들 수 있습니다!
  * **LINEAR** - 기본값입니다. easing 없이 min과 max 값 사이를 선형으로 이동합니다.
  * **EASE OUT** - 빠르게 시작한 뒤 끝에 가까워질수록 느려집니다. 멈추기 전 감속처럼 물리적인 움직임을 시뮬레이션하는 데 매우 좋습니다.
  * **EASE IN** - 천천히 시작해서 점차 빨라집니다. 관성이 쌓이는 느낌을 시뮬레이션하기에 좋습니다.
  * **EASE IN/OUT** - 두 방식을 조합한 것으로, 매우 자연스러운 움직임을 만듭니다.

{% hint style="warning" %}
**Easing -** 일부러 로봇처럼 보이는 움직임을 원하지 않는 한, 가능하면 기본 linear 애니메이션은 피하는 것이 좋습니다. Easing을 사용하면 애니메이션이 훨씬 더 흐르듯 자연스럽게 보입니다!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sawtooth wave

사이클 동안 위로 상승하다가 끝에서 급격히 떨어지기 때문에 _ramp waveform_이라고도 합니다. _hue_나 _rotation_처럼 순환하는 속성의 loop를 만들 수 있어 아마 가장 흔히 사용하는 wave oscillator일 것입니다.

다음 항목은 위 섹션을 참조하세요 :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Sawtooth 전용 :

* **cycle range compensation** - **steps**가 설정되어 있을 때 사용할 수 있으며, 예를 들어 0에서 360까지의 rotation처럼 값을 순환시키는 데 좋습니다. 이 설정을 사용하지 않으면 시작값과 끝값이 같아져 시작 지점에서 걸리는 현상이 생길 수 있습니다(0과 360은 같은 각도이기 때문입니다). 이 설정을 켜면 step 위치가 올바르게 맞도록 최대 범위가 줄어듭니다.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Triangle wave

매 사이클마다 시작점으로 점프하는 _sawtooth wave_와 달리, _triangle wave_는 앞으로 선형 이동한 뒤 다시 뒤로 선형 이동합니다.

다음 항목은 위 섹션을 참조하세요 :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sine wave

가장 부드러운 파형입니다! 진자처럼 두 값 사이를 부드럽게 진동합니다.

다음 항목은 위 섹션을 참조하세요 :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Square wave

가장 단순한 파형입니다. 두 값 사이를 앞뒤로 번갈아 오갑니다!

다음 항목은 위 섹션을 참조하세요 :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Square wave 전용 :

* **pulse width** - 전체 duration을 기준으로 파형이 최대값에 머무는 시간의 길이입니다. 기본값은 50%이며, 정확히 절반씩 나뉩니다. “켜진” 상태가 전체 시간의 1/4만 되게 하려면 25%로 설정합니다. 이 pulse가 발생하는 시점은 _offset_ 값으로 조정할 수 있습니다.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Liberation의 장점 중 하나는 무작위이지만 반복 가능한 효과를 생성할 수 있다는 점입니다. _noise_ oscillator를 사용하면 원하는 만큼 디테일하거나 떨림이 있는, 자연스러운 looping 랜덤 움직임을 만들 수 있습니다.

다음 항목은 위 섹션을 참조하세요 :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Noise 전용 :

* **noise type** - noise를 생성하는 데 사용되는 알고리즘입니다.
  * **SIMPLEX** - 기본값입니다. 물결치듯 오르내리는 값이며, loop로 반복됩니다.
  * **RANDOM** - 더 전통적인 난수 알고리즘을 사용하며, 완전히 노이즈가 많고 혼돈스러운 결과를 만듭니다.

{% hint style="info" %}
**Simplex noise**는 Ken Perlin이 1983년에 영화 _Tron_ 작업의 일부로 개발한 "Perlin noise" 알고리즘을 개선하기 위해 2001년에 설계한 것입니다. 그는 이 작업으로 오스카상을 받았습니다!

이른바 "gradient" noise는 이전의 “기계적인” 컴퓨터 생성 이미지에 대한 그의 불만에서 탄생했습니다. CGI 분야에서는 구름, 수면, 또는 사실적인 지형을 위한 height-map을 렌더링하는 데 특히 좋습니다.

하지만 Liberation에서는 예측하기 어려워 보이면서도 여전히 부드럽고 자연스러운 움직임을 만드는 데 좋습니다.
{% endhint %}

* **seed** - noise를 생성하는 데 사용되는 값입니다. 현재 noise wave의 모양이 마음에 들지 않으면 이 값을 변경해 보세요.

{% hint style="info" %}
재미있는 nerdy fact! 완벽하게 loop되는 simplex noise를 얻기 위해 저는 2D noise 평면 위에서 원을 따라 반복하고 있습니다. 그리고 seed 값을 바꾸면 이 평면이 3차원 방향으로 이동합니다!
{% endhint %}

* **simplex detail** - noise가 얼마나 디테일하거나 떨리는지 변경합니다. 반복 패턴이 덜 눈에 띄게 만들고 싶다면 duration을 늘리고 이 값을 높이세요.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

완전히 사용자 지정된 waveform을 만듭니다. 복잡한 애니메이션을 만드는 데 매우 유용합니다.

다음 항목은 위 섹션을 참조하세요 :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

그 아래에는 positions와 values 목록이 있습니다. duration은 64 steps로 나뉘며, 이 지점들 중 어디에든 값을 배치할 수 있습니다.

각 step에는 다음 설정이 있습니다 :

* **Step** - duration 안에서의 시간 step입니다. 0은 시작 지점, 64는 끝 지점입니다.
* **Level** - 해당 time step에서의 wave 레벨입니다. level 범위는 0에서 1 사이입니다.
* **Animation type** - drop down menu에서 이전 step에서 이 level까지 어떻게 이동할지 선택할 수 있습니다.
  * **None** - 전환 없이 지정한 시간에 바로 이 level로 점프합니다.
  * **Linear** - 이전 level에서 이 level까지 완전히 선형으로 이동합니다.
  * **Ease in / Ease out / Ease in/out** - 이전 level에서 이 level까지 easing을 적용해 이동합니다. animation type에 대한 설명은 위의 _ease function_을 참조하세요.

***
