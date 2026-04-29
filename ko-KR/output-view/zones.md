---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

대부분의 프로젝트에서 주로 사용하게 될 zone 유형은 _Beam zone_입니다. 공기 중의 대기형 빔 효과를 위해 설계된 zone입니다. 다른 유형의 zone은 _Canvas zone_입니다([그래픽과 Canvas 시스템](../graphics-and-the-canvas-system/) 참조).

{% hint style="danger" %}
**경고 - 레이저가 작동 중일 때 zone을 이동할 때는 극도로 주의하고** brightness를 가능한 한 낮게 줄이십시오. 레이저를 안전하게 활성화하고 zoning하는 전체 가이드는 [레이저 설정 절차 개요](../setting-up/setting-up-lasers.md)를 참조하십시오.
{% endhint %}

마우스로 zone을 클릭하고 드래그하여 이동할 수 있습니다. test pattern을 켜서 해당 zone이 어디로 출력되는지 확인하십시오.

{% hint style="info" %}
화살표 키를 사용해 현재 선택된 zone/point를 **조금씩 이동**할 수 있습니다. 더 큰 간격으로 이동하려면 `Shift` 키를 누르십시오.
{% endhint %}

{% hint style="info" %}
팁: 여러 레이저에 zone 설정을 빠르게 복사할 수 있습니다! [레이저 간 설정 복사](../setting-up/copy-laser-settings.md)를 참조하십시오.
{% endhint %}

### 새 beam zone 추가하기

toolbar 상단의 _Add a new beam zone_ 버튼을 클릭하면 새 zone이 나타납니다. beam zone은 추가한 순서대로 정렬되지만, 순서를 다시 정렬할 수 있습니다. [빔 존 재정렬](re-ordering-beam-zones.md)를 참조하십시오.

### 기존 canvas zone 추가하기

_Add existing canvas zone_ 버튼을 클릭하면 사용 가능한 canvas zone 목록이 표시되며, 이 레이저에서 각 zone을 켜거나 끌 수 있습니다. [그래픽과 Canvas 시스템](../graphics-and-the-canvas-system/)를 참조하십시오.

### Zone shape 유형

Zone shape 유형은 3가지입니다.

* **Quad** - 기본 직사각형 zone shape입니다. 균일한 형태(axis aligned)로 사용할 수도 있고 왜곡할 수도 있습니다. 큰 직사각형 zone이나 perspective correction이 필요한 canvas zone에 적합합니다.
* **Line/Curve** - 2개 이상의 point와 thickness로 정의되는 zone입니다. 얇은 zone이나 발코니, 다리 또는 기타 곡선 형태에 맞춰 종료해야 하는 경우에 적합합니다.
* **Segmented** - 더 작은 quad로 세분화할 수 있는 zone입니다. 건축물 mapping에 적합합니다.

아무 zone이나 오른쪽 클릭하면 해당 설정이 열립니다. 이 오른쪽 클릭 메뉴에서 다음을 할 수 있습니다.

* zone 이름 변경(특히 zone이 많을 때 clip deck에서 식별하기에 유용합니다!)
* zone 활성화/비활성화
* 위치 잠금
* shape type 변경
* 기본 위치로 재설정
* shape type별 설정 접근
* 삭제
* _Alt Zone_ 추가([Alt zone 시스템](alt-zone-system.md) 참조)

{% hint style="danger" %}
**경고 -** 레이저가 활성화된 상태에서 zone type을 변경할 때는 매우 주의하십시오. zone은 해당 shape의 마지막 위치/크기로 돌아가므로 output이 갑자기 바뀔 수 있습니다. zone type을 변경하기 전에는 레이저를 끄는 것이 가장 좋습니다.
{% endhint %}

### Quad zone shape

마우스로 quad의 각 모서리를 이동할 수 있습니다. 모서리를 `Alt / Option`-클릭하면 다른 모서리와 독립적으로 이동하여 quad를 왜곡할 수 있습니다. 한 번 quad가 왜곡되면 모든 모서리를 자유롭게 이동할 수 있습니다.

오른쪽 클릭 메뉴의 _REMOVE DISTORTION_ 버튼을 사용하면 왜곡을 제거하고 axis-aligned 직사각형으로 되돌릴 수 있습니다.

#### Perspective correction

이 옵션은 오른쪽 클릭 메뉴의 toggle 버튼으로 설정할 수 있으며, 왜곡 방식을 결정합니다. 빔에는 이 옵션을 꺼 두는 것이 가장 좋지만, 이 zone이 평평한 면에 graphics를 투사하는 경우에는 켜면 output에 perspective correction이 적용됩니다.

{% hint style="info" %}
_Perspective correction_이 꺼져 있으면 content는 _bi-linear interpolation_을 사용해 왜곡됩니다. 즉, content가 quad 전체에 균일하게 배치됩니다. 그래서 빔에 더 적합합니다.

perspective correction을 켜면 content는 원근 warping을 사용해 왜곡되며, 단축 효과를 보정합니다. 따라서 벽에 비스듬한 각도로 graphics를 투사하는 경우, 이를 사용해 output 왜곡을 보정하고 projection distortion을 수정할 수 있습니다.
{% endhint %}

### Line / Curve zone shape

Line / Curve zone shape은 최근 쇼에서 제가 가장 자주 사용하는 옵션이 되었으며, beam zone의 기본값이 되어야 한다고 해도 무리가 없을 정도입니다.

대부분의 경우 제 zone은 공연장의 좁고 애매한 공간이나 건물의 창문 사이에 맞추기 위해 얇아야 합니다. 이렇게 모서리들이 서로 가까이 있으면 quad의 네 모서리를 조정하는 것이 매우 번거롭다는 것을 알게 되었습니다. 그래서 Line / Curve zone이 탄생했습니다!

직선의 경우 point 2개만 있으면 됩니다. 그런 다음 오른쪽 클릭 메뉴에서 _Zone thickness_를 조정하십시오. 간단한 zone을 만드는 가장 빠른 방법입니다.

선 위를 `Alt / Option`-클릭하면 point를 추가로 만들 수 있습니다. 이 point들은 자동으로 부드럽게 처리되어 흐르는 형태를 만들며, _Smooth level_을 조정해 꺾인 부분을 완화할 수 있습니다.

point를 `Alt / Option`-클릭하면 삭제할 수 있습니다.

또는 vector graphics 앱(Inkscape, Illustrator 등)에 익숙하다면 _Manually adjust bezier curves_ 옵션을 사용해 모든 control point를 세밀하게 조정할 수 있습니다.

### Segmented zone shape

이 세분화된 zone은 매우 세밀한 보정을 가능하게 하며, 복잡한 형태에 mapping할 때 유용합니다. 오른쪽 클릭 메뉴의 + 및 - 버튼을 사용해 subdivision을 추가하거나 제거할 수 있습니다.

### 다른 zone으로 완전히 덮인 zone을 편집하는 방법

위에 있는 zone을 오른쪽 클릭한 다음 padlock 버튼을 클릭해 잠그십시오. 그러면 아래에 있는 zone을 편집하고 조정할 수 있습니다.

<br>

{% hint style="info" %}
Output에 Beam zone을 추가하면 clip deck의 clip에 추가할 수 있게 됩니다.
{% endhint %}
