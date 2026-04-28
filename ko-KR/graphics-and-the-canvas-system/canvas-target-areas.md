---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas target areas

Canvas의 일부를 각 laser 안의 zone으로 가져오는 방법은 이미 알고 있습니다. 하지만 먼저 Canvas에 콘텐츠를 넣으려면, 이름이 다소 헷갈리지만 정확한 _Canvas target areas_가 필요합니다.

_Canvas target areas_는 Clip을 그려 넣을 수 있는 Canvas의 영역이며, _CANVAS_ 보기에서는 파란색 윤곽선 사각형으로 표시됩니다.

대부분의 경우 Canvas target area는 하나만 있으면 충분할 수 있으며, 그런 다음 이를 여러 zone으로 나누어 서로 다른 laser로 보낼 수 있습니다.

때로는 건물의 서로 다른 부분을 위해 여러 Canvas target area를 사용하거나, 그 사이의 zone delay를 활용하고 싶을 수도 있습니다. (네! zone delay는 Canvas target area 사이에서도 계속 작동합니다!)

### Clip을 Canvas target area로 보내기

Clip Deck을 보면 beam zone 버튼 옆에 Canvas target area 버튼이 있습니다. 이 버튼들이 보이도록 Output 버튼을 스크롤해야 할 수 있습니다. `Shift + Left / Right Arrow`를 사용하거나, 화면의 ZONE PAGE 버튼 또는 APC40 버튼을 사용하세요([apc40-reference.md](../reference/apc40-reference.md) 참고).

Beam zone 버튼을 사용할 때와 정확히 같은 방식으로 이 버튼들을 토글하여 Clip을 Canvas target area에 할당합니다.

### Canvas target area 추가 / 편집

상단 메뉴 바에서 _View -> Canvas Target Areas_를 선택하면 프로젝트에 있는 각 Canvas target area의 모든 설정을 볼 수 있습니다.

그리고 상단에는 _ADD CANVAS TARGET AREA_ 버튼이 있습니다.

빨간색 마이너스 기호 버튼을 사용해 Canvas target area를 삭제합니다.

슬라이더를 사용해 크기와 위치를 조정합니다. 값을 직접 입력하려면 슬라이더를 더블 클릭하세요.

### Scale mode

* **FIT TO AREA** - 콘텐츠의 종횡비를 유지하면서 Canvas target area 안에 완전히 들어가도록 축소합니다. (기본 설정)
* **FILL AREA** - 콘텐츠의 종횡비를 유지하면서 Canvas target area를 채우도록 늘립니다. 콘텐츠가 가장자리에서 잘릴 수 있습니다.
* **STRETCH TO FIT** - 종횡비를 무시하고 콘텐츠가 Canvas target area 전체를 채우도록 늘립니다.
