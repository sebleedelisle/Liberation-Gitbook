---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 색상 설정 및 HSB

Liberation에서 색상은 RGB가 아니라 HSB로 정의됩니다. 처음에는 익숙하지 않을 수 있지만, 익숙해지면 훨씬 더 직관적인 방식이라고 느끼실 것입니다.

{% hint style="info" %}
RGB 사용을 선호한다면 색상 설정에서 색상 사각형을 클릭하면 됩니다. 그러면 RGB와 HSB 옵션을 제공하는 colour editor panel이 열립니다.
{% endhint %}

### HSB - Hue, Saturation and Brightness

#### Hue

색상의 Hue 범위는 0부터 255까지입니다. 0은 빨간색이며, 값을 올리면 무지개의 모든 색상인 주황, 노랑, 초록, 시안, 파랑, 보라, 마젠타를 지나 255에서 다시 빨간색으로 돌아옵니다.

이 값은 순환 구조이므로 triangle wave를 사용해 모든 색상을 순환시킬 수 있습니다.

#### Saturation

이 설정은 색상의 채도 또는 선명도를 조정합니다. 즉, 색상이 얼마나 _컬러풀한지_를 나타내며 범위는 0부터 255까지입니다. Saturation을 0으로 설정하면 회색 계열이 되고, 255로 설정하면 완전한 무지개 색상이 됩니다. 중간 값은 파스텔처럼 옅은 색상을 만듭니다.

{% hint style="info" %}
colour라는 단어에 추가 모음이 들어가 있어 미국 사용자분들께는 양해를 구합니다. Liberation은 영국에서 제작되었기 때문에 기본 표기는 영국식 영어입니다. 앞으로는 프랑스어, 스페인어, 독일어, 이탈리아어, 중국어 간체, 그리고 물론 미국식 영어 번역도 제공하고 싶습니다. :innocent:
{% endhint %}

#### Brightness

아마 가장 이해하기 쉬운 설정입니다. 0은 완전한 검정이고, 255는 최대 밝기입니다.

### 사용 예

#### 무지개 순환 :

_Brightness_와 _Saturation_을 255로 설정합니다. _Sawtooth_ oscillator를 _Hue_ socket에 연결하고, 범위를 0에서 255로 조정합니다.

#### 밝기 펄스 :

_Sawtooth_ oscillator를 _Brightness_ socket에 연결하고, 범위를 255에서 0으로 조정합니다. clamp min과 max를 추가로 조정하여 변화가 진행되는 시간을 세밀하게 제어할 수 있습니다. 그런 다음 easing functions를 사용해 애니메이션을 더 다듬을 수 있습니다.

#### 강한 플래시 / 스트로브 :

_Hue_와 _Saturation_을 사용하거나 colour picker를 클릭해 색상을 선택합니다. _Square Wave_ oscillator를 _Brightness_ socket에 연결하고, 범위를 255에서 0으로 조정합니다.

#### 사용자 지정 Hue 범위 순환 :

_Brightness_와 _Saturation_을 255로 설정합니다. _Triangle Wave_ oscillator를 _Hue_ socket에 연결하고, 범위를 조정합니다 :

* 파란색에서 시안까지는 70에서 128 범위를 사용합니다
* 빨간색에서 노란색까지는 0에서 40 범위를 사용합니다
* 빨간색에서 마젠타까지는 255에서 220 범위를 사용합니다
