---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

사운드 입력 레벨을 속성 값으로 변환합니다.

{% hint style="info" %}
Sound input oscillator는 기본 사운드 인터페이스를 사용하지만, _Preferences_에서 변경할 수 있습니다. _Liberation -> Preferences_ 메뉴를 여세요.

_Sound Input_ 설정에서 사용할 사운드 인터페이스를 선택할 수 있으며, 볼륨 레벨을 조정하기 위한 몇 가지 추가 설정도 사용할 수 있습니다.
{% endhint %}

* **range min / range max** - 파형이 매핑될 최소값과 최대값입니다.
* **channel** - 사운드 인터페이스에 입력 채널이 둘 이상 있는 경우, 여기에서 어떤 채널을 받을지 선택할 수 있습니다.

{% hint style="info" %}
믹싱 데스크에서 여러 개의 사운드 피드를 받아오는 것도 재미있는 기법입니다. 이렇게 하면 서로 다른 Clip이 서로 다른 악기에 반응하도록 만들 수 있습니다.
{% endhint %}

{% hint style="info" %}
모든 _Sound Inputs_에서 한 번에 하나의 사운드 인터페이스만 사용할 수 있습니다(_App Settings_ 패널에서 선택). 이 용도로 둘 이상의 인터페이스를 사용하려면 macOS에서 [Aggregate Device를 생성](https://support.apple.com/en-gb/HT202000)하여 여러 입력을 하나의 가상 사운드 소스로 결합할 수 있습니다. (Windows에도 이 작업을 해주는 앱이 많이 있지만, 직접 사용해 보지는 않았습니다.)
{% endhint %}

* **clamp min / clamp max** - 반응할 레벨 범위를 선택할 때 사용합니다. 게이트와 리미트 설정(_App Settings_ 패널)이 제대로 조정되어 있다면 이 값을 조정할 필요는 없지만, 창의적인 효과를 만들 때 사용할 수 있습니다.

{% hint style="info" %}
Clip 버튼에 작은 마이크 아이콘이 보이면 해당 Clip에 _Sound Input_ oscillator가 있다는 뜻입니다.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
