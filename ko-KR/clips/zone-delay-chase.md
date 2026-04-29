---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

레이저가 많을수록 더 재미있다는 데는 모두 동의하겠지만, 모든 레이저가 정확히 같은 동작만 한다면 창의적인 가능성을 놓치게 됩니다.

Zone delay 시스템은 존마다 변화를 주는 간단하면서도 효과적인 방법이며, 멀티 레이저 설정을 최대한 활용할 수 있게 해줍니다. 더 전통적인 chase 효과를 만드는 데도 사용할 수 있습니다.

#### 작동 방식

_Zone delay_는 각 존에서 클립의 타이밍에 지연을 추가하여, 존 전체에 걸쳐 쓸려 지나가는 듯한 효과를 만듭니다.

이미 실행 중인 클립에 zone delay를 적용하면 매우 효과적입니다. APC40의 관련 컨트롤을 사용해 레벨과 패턴을 조정할 수 있습니다. ([APC40 레퍼런스](../reference/apc40-reference.md) 참고). 또는 _Clip Settings_ 패널을 사용할 수도 있습니다.

Zone delay 설정:

* **Zone delay** - 각 존에 적용되는 지연 시간의 양을 제어합니다. 단위는 64분음표입니다.
* **Pattern** - 존 순서를 선택합니다.
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
패턴은 존 번호를 기준으로 동작하며, 존이 왼쪽에서 오른쪽 순서로 배치되어 있다고 가정합니다. Zone delay는 패턴을 계산할 때 canvas 존과 DMX 존을 서로 별도의 그룹으로 처리합니다.
{% endhint %}

* **Delay mode**
  1. No delay - chase mode에서 사용합니다.
  2. Delay - 기본 모드로, 각 존의 타이밍을 지연시킵니다.
  3. Delay with re-trigger - 패턴을 따라 진행될 때마다 클립을 처음으로 되돌립니다. _Chase mode_와 함께 사용하면 좋습니다.
* **Chase mode** - chase mode를 켜면 각 존이 전통적인 chase 효과처럼 켜지고 꺼집니다. _Fade in, Hold,_ 및 _Fade out_ 설정을 사용해 chase의 모양을 조정합니다. 이 설정들은 zone delay 값에 대한 비율로 지정됩니다. 따라서 값이 1이면 _Zone delay_ 값에 지정된 시간과 동일합니다. 설명으로는 조금 이해하기 어려울 수 있으니, 직접 시도해 보는 것을 권장합니다.

{% hint style="info" %}
Zone delay는 활성화된 모든 효과에도 적용됩니다. 예를 들어 flashing 효과는 클립 자체의 애니메이션뿐 아니라 존 전체에 걸쳐서도 지연됩니다.
{% endhint %}

클립에 어떤 형태의 _Zone delay_라도 적용되어 있으면, 클립 오른쪽 위에 점 세 개 아이콘이 표시됩니다. 이 점들은 해당 클립의 _Zone delay_ 스타일을 보여주도록 애니메이션됩니다. 자세한 내용은 [클립 버튼의 작은 아이콘은 무엇인가요?](what-are-the-small-icons-on-the-clip-buttons.md)를 참고하세요.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>클립에 zone delay가 적용되어 있으며 해당 모드를 나타내는 점 세 개 기호</p></figcaption></figure>

{% hint style="info" %}
Zone delay는 각 클립에 속한 설정입니다. 전역 설정이 아니며, 클립의 창의적 디자인을 구성하는 요소입니다.
{% endhint %}
