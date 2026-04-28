---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

모든 콘텐츠를 x, y 및/또는 z 축을 따라 이동합니다. 좌표계는 중앙을 기준으로 하며, x 및 y 축은 +/-200까지 확장됩니다. [co-ordinate-system.md](../fundamentals/co-ordinate-system.md)를 참조하세요.

* **x** - x 축을 따라 이동할 거리입니다(왼쪽 - 오른쪽).
* **y** - y 축을 따라 이동할 거리입니다(위 - 아래).

#### 3D 옵션(3D가 선택된 경우 사용 가능)

* **z** - z 축을 따라 이동할 거리입니다(화면 안쪽과 바깥쪽 방향).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

모든 콘텐츠를 회전합니다. 값의 단위는 도(degree)입니다. [co-ordinate-system.md](../fundamentals/co-ordinate-system.md)를 참조하세요.

* **rotation** - 콘텐츠가 시계 방향으로 회전되는 각도입니다. 모든 요소는 중심인 원점(0,0)을 기준으로 회전합니다.
* **pivot point x / pivot point y** - 이 값을 사용해 회전 원점을 오프셋합니다.

#### 3D 옵션(3D가 선택된 경우 사용 가능)

* **rotation x** - x 축을 중심으로 한 회전입니다(피치).
* **rotation y** - y 축을 중심으로 한 회전입니다(요).
* **pivot point z** - z 축에서의 회전 오프셋 위치입니다.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

모든 콘텐츠의 크기를 조정합니다.

* **scale** - 스케일 비율(%)입니다.
* **scale x / scale y** - 가로 및/또는 세로 방향으로 스케일을 조정하려면 이 옵션을 사용합니다.

{% hint style="warning" %}
어떤 축에서든 0%로 스케일되면 해당 요소는 사라집니다!
{% endhint %}
