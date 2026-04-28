---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/co-ordinate-system
---

# 🟩 좌표계

Clip 콘텐츠는 화면 중앙에 원점(0,0)이 있는 x/y 좌표계를 사용합니다.

* 가로축 x에서는 왼쪽이 음수, 오른쪽이 양수입니다.
* 세로축 y에서는 위쪽이 음수, 아래쪽이 양수입니다.

Clip의 너비와 높이는 400픽셀이므로, 보이는 영역의 좌표 범위는 -200에서 200까지입니다.

{% hint style="info" %}
Clip editor는 _벡터_ 형태를 만듭니다. 즉, 픽셀로 저장되는 것이 아니라 형태가 그려지는 방식을 정의하는 좌표 집합으로 저장됩니다. 이는 Photoshop과 달리 Inkscape나 Illustrator가 콘텐츠를 정의하는 방식과 비슷합니다.
{% endhint %}

### 3D

또한 3D 공간에서 z축을 따라 앞뒤로 이동할 수 있습니다. 기본적으로 모든 요소의 z 위치는 0입니다.

* z축에서는 사용자에게서 멀어지는 뒤쪽이 음수, 사용자 쪽으로 가까워지는 앞쪽이 양수입니다.
