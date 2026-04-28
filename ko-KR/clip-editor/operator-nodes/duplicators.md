---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

모든 콘텐츠의 미러 복제본을 만듭니다. 기본적으로 미러 축은 중앙의 세로선입니다.

* **angle** - 미러 축 선의 각도입니다.
* **offset position** - 미러 축을 이동합니다(축에 수직인 방향으로 이동).
* **delay** - 미러링된 콘텐츠의 시간 지연입니다. 콘텐츠에 어떤 형태의 애니메이션이 있을 때만 효과가 있습니다.

#### 3D 옵션(3D가 선택된 경우 사용 가능)

* **angle X / angle Y** - 미러 축이 평면이 되며, 이 설정으로 3D 공간에서 평면을 회전할 수 있습니다.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

콘텐츠를 원형 패턴으로 복제합니다.

* **radius** - 회전하기 전에 콘텐츠를 중심점에서 얼마나 떨어뜨려 이동할지 지정하는 거리입니다.
* **count** - 만들 객체 복사본의 수입니다.
* **use each objects pivot point** - 선택하면 각 요소가 자체 중심점을 기준으로 이동하고 회전합니다. (복제되는 요소가 여러 개일 때만 효과가 있습니다)
* **delay** - 각 복제 요소에 점점 더 긴 시간 지연을 추가합니다. 이 효과가 눈에 띄려면 콘텐츠에 어떤 형태의 애니메이션이 있어야 합니다.
* **rotation** - 요소에 추가되는 오프셋 회전입니다.

#### 3D 옵션(3D가 선택된 경우 사용 가능)

* **rotation x / rotation y** - 전체 원형 패턴을 x축과 y축을 기준으로 회전합니다.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

콘텐츠를 행과 열로 이루어진 그리드 패턴으로 복제합니다.

* **spacing** - 요소 사이의 거리입니다.
* **count X**- 가로 방향 복사본 수입니다(열).
* **count Y**- 세로 방향 복사본 수입니다(행).
* **horizontal alignment** - 열의 시작점입니다. LEFT, CENTRE 또는 RIGHT입니다.
* **vertical alignment** - 행의 시작점입니다. TOP, MIDDLE 또는 BOTTOM입니다.
* **delay** - 각 복제 요소에 점점 더 긴 시간 지연을 추가합니다. 이 효과가 눈에 띄려면 콘텐츠에 어떤 형태의 애니메이션이 있어야 합니다.
