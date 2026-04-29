---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Canvas 개요

Liberation Canvas 시스템은 비교적 단순하지만, 처음에는 헷갈릴 수 있습니다. 시작하는 데 도움이 되도록 개념을 간단히 정리해 보겠습니다.

{% hint style="info" %}
**잠깐, Canvas 시스템이 꼭 필요한가요?**

아닐 수도 있습니다! 하나의 그래픽을 하나의 레이저에 투사하기만 한다면 beam zone으로 쉽게 처리할 수 있습니다. 다만 기본적으로 beam zone 콘텐츠는 좌우 반전되어 있으므로, Clip에 X flip을 적용해야 합니다.

하지만 그래픽 콘텐츠를 여러 레이저에 나누어 보내거나, 건축물에 매핑하기 위해 여러 섹션으로 분할하려는 경우에는 Canvas 시스템을 사용하면 됩니다.
{% endhint %}

### Canvas

먼저 Canvas 자체가 있습니다. _CANVAS_ view에서 보이는 것이 바로 이 Canvas입니다. 말 그대로 큰 캔버스를 나타내며, 이 공간 안의 어디에든 콘텐츠를 그릴 수 있습니다.

### Canvas target area

Canvas view에서 파란색 윤곽선 사각형으로 표시되는 영역이며, 콘텐츠를 보낼 수 있는 대상 영역입니다. Clip을 beam zone으로 보내는 것과 같은 방식으로, Clip의 콘텐츠를 Canvas target area로 보냅니다. Clip Deck에서 beam zone 버튼 오른쪽에 Canvas target area 버튼이 표시됩니다.

{% hint style="info" %}
Clip Deck에 Canvas 버튼이 보이지 않는다면 `Shift + Left / Right Arrow`로 beam zone 버튼을 스크롤해 보세요. 각 Canvas target area마다 _CANVAS 1, CANVAS 2_ 등으로 표시된 버튼이 보일 것입니다.
{% endhint %}

### Canvas zone

Canvas zone은 Canvas 안에서 레이저로 보낼 영역입니다. Canvas view에서 분홍색 윤곽선 사각형으로 표시됩니다. 각 zone을 우클릭한 다음 할당할 레이저를 선택할 수 있습니다. 이제 해당 레이저의 _OUTPUT_ view로 전환하면 새 zone이 나타난 것을 볼 수 있습니다.

{% hint style="danger" %}
경고 - 레이저가 armed 상태이면 기본 Canvas zone에서 콘텐츠가 갑자기 투사되기 시작할 수 있습니다. Canvas zone을 레이저에 할당하기 전에 레이저를 disarm하는 것이 좋습니다.
{% endhint %}

{% hint style="info" %}
_OUTPUT_ view에서 _add canvas zone_ 버튼을 클릭해 Canvas zone을 레이저에 할당할 수도 있습니다. [Zones](../output-view/zones.md)를 참조하세요.
{% endhint %}

### Guide image

Canvas에 guide image를 추가하고, 이를 그래픽의 템플릿으로 사용할 수 있습니다. 콘텐츠가 더 잘 보이도록 guide image의 색상 틴트(우클릭 메뉴)를 조정하고 어둡게 만드는 것이 좋습니다.

{% hint style="info" %}
건축물 매핑에서는 건물의 모든 표면을 평평하고 왜곡 없는 이미지로 표현한 ‘펼친’ 시각 자료를 만들어 두면 도움이 됩니다. 각 섹션의 원근 보정은 _OUTPUT_ view의 Canvas zone을 사용해 처리할 수 있습니다.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>영국 Gateshead에 있는 Saltwell Hall을 위한 ‘평면화된’ guide image</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Liberation 초기 버전(c2017!)의 Canvas zone입니다. 분홍색 사각형은 Canvas의 어떤 부분을 표시할지 선택하며, 아래의 Output view는 해당 zone이 각 레이저의 어느 부분으로 보내지는지 보여줍니다.</p></figcaption></figure>

### 3D visualiser의 Canvas

복잡한 멀티 레이저 투사 시스템을 3D visualiser에서 그대로 재현하는 것은 상당히 번거로울 수 있습니다. 대신 Canvas를 3D 공간 안에 배치하는 옵션이 있습니다. _3D visualiser settings_ panel에서 _Show canvas_ checkbox를 활성화하세요. Canvas에 guide image가 있다면 visualiser에도 함께 표시됩니다.

{% hint style="info" %}
visualiser는 여전히 Canvas 투사를 레이저에서 나오는 공중 효과로 표시합니다. 그냥 시야 밖으로 옮겨도 되고, 원한다면 Canvas와 맞춰 정렬할 수도 있습니다.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>3D visualiser에서 레이저 빔을 Canvas 이미지와 정확히 맞췄을 때는 정말 만족스럽습니다!</p></figcaption></figure>
