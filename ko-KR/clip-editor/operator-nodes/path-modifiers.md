---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

이 노드는 선과 도형 콘텐츠를 일정한 간격의 점으로 대체합니다(기존 점은 변경되지 않습니다).

* **Colour** – 점의 색상입니다. _Inherit Colour_가 활성화되어 있으면 무시됩니다. 아래 내용을 참고하세요. _관련 항목_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – 점 사이의 거리이며 픽셀 단위로 측정됩니다. 값이 작을수록 점이 많아지고, 값이 클수록 점이 적어집니다.
* **Offset** – 간격에 대한 백분율로 점의 시작 위치를 이동합니다. 애니메이션할 수 있으며(예: sawtooth Oscillator Node 사용), 점이 “이동하는” 효과를 만들 수 있습니다.
* **Keep Original** – 활성화하면 원래 선/도형이 유지되고 그 위에 점이 그려집니다.
* **Render Profile** – 렌더링 품질을 선택합니다. _참조_ [render-profile.md](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – 경로 길이가 균등하게 나누어지도록 간격을 자동 조정합니다.
* **Fade Out Ends** – 경로의 시작과 끝으로 갈수록 점의 밝기를 점진적으로 줄입니다. sawtooth Oscillator Node로 **Offset**을 애니메이션할 때 유용하며, 점이 도형 끝으로 이동할 때 부드럽게 페이드 인/아웃됩니다.

## &#x20;Trimmer

이 노드는 선과 도형의 보이는 길이를 잘라내어, 시간에 따라 나타내거나 숨기거나 애니메이션할 수 있게 합니다.

* **Offset** – 도형에서 보이는 부분이 시작되는 위치를 제어합니다. _Trim Size_가 0%여도 Offset을 0% → 100%로 애니메이션하면 도형이 그려지기 시작하고, 50%에서 완전히 보인 뒤, 다시 사라집니다.
* **Trim Size** – 도형 전체 길이에 대한 백분율로 유지할 부분의 길이를 설정합니다.
* **Loop** – 도형을 연속 루프로 처리하여, 끝부분이 사라지는 대신 시작 부분으로 다시 연결되게 합니다.
* **All Shapes** – 모든 입력 도형을 결합해 하나의 경로처럼 트리밍합니다. 꺼져 있으면 각 도형이 개별적으로 트리밍됩니다.
* **Add Dot at Start / Add Dot at End** – 트림 지점에 선택한 색상의 점을 추가합니다. (트림이 적용되지 않은 경우 점은 추가되지 않습니다.)
* **Colour** – 트림 점의 색상입니다. _관련 항목_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – 점에 사용할 렌더 프로필을 선택합니다. _참조_ [render-profile.md](../fundamentals/render-profile.md)
