---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### 소개

Liberation의 3D visualiser는 매우 유용한 기능입니다. 레이저가 전혀 없어도 쇼를 설계하고 다듬을 수 있습니다! 특히 많은 수의 레이저를 사용하는 복잡한 설정에서 매우 중요한 도구로 활용됩니다.

### 3D 공간 탐색하기

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser 뷰</p></figcaption></figure>

* 클릭한 상태로 드래그하면 오비트 포인트를 중심으로 뷰가 회전합니다.
* 마우스 휠을 사용하면 오비트 포인트를 향해 앞뒤로 이동합니다.
* shift 키를 누른 상태로 클릭해 드래그하면 카메라가 XY 평면을 따라 좌우 및 상하로 수평 이동(strafe)합니다.
* Visualiser의 아무 곳이나 더블 클릭하면 카메라 위치가 초기화됩니다.

### Settings

_Window_ 메뉴에서 _3D Visualiser Settings_ 패널을 엽니다.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings 패널</p></figcaption></figure>

* **Visualiser size** - 앱의 나머지 영역에 비해 Visualiser의 크기를 변경합니다.
* **Brightness Adjustment** - 레이저가 표시되는 밝기를 변경합니다.
* **Show laser numbers** - 각 레이저 위에 해당 번호를 표시합니다.
* **Show zone names** - 각 레이저 아래에 해당 zone 이름을 표시합니다.

### Camera settings

이 설정들은 대부분 3D 공간의 가상 카메라와 관련되어 있습니다. 이 설정의 프리셋을 저장하고 다시 불러올 수 있는 드롭다운이 표시됩니다.

* **Camera distance -** 카메라는 항상 _Orbit point_를 바라봅니다. Camera distance는 카메라가 이 지점에서 얼마나 떨어져 있는지를 나타냅니다. 마우스 스크롤 휠로도 이 설정을 조정할 수 있습니다.
* **FOV -** Field of view입니다. 카메라가 얼마나 광각인지 또는 얼마나 줌인되어 있는지를 결정합니다.
* **Orbit position** - 오비트 포인트를 중심으로 한 현재 회전을 나타냅니다. 첫 번째 값은 X축 회전(pitch)이고, 두 번째 값은 Y축 회전(yaw)입니다.
* **Orbit centre point** - 3D 공간에서 오비트 포인트의 위치(x, y, z)입니다.
* **Grid height** - "ground"(즉 y = 0인 위치)로부터 그리드의 높이입니다.

### Content settings

이 설정들은 3D 환경 안에서 레이저(및 Canvas)가 배치되는 위치를 결정합니다. 이 설정의 프리셋을 저장하고 다시 불러올 수 있는 드롭다운이 표시됩니다.

#### Lasers

각 레이저에는 작은 흰색 삼각형으로 펼칠 수 있는 고유한 설정 그룹이 있습니다.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D Visualiser 레이저 설정</p></figcaption></figure>

* **3D Position** - 레이저의 x, y, z 위치입니다.
* **3D Orientation** - 레이저가 x, y, z 각 축을 기준으로 회전한 값입니다.
* **Flip X / Flip Y** - 레이저의 가상 출력을 반전합니다. 참고: 이 설정은 일반적으로 필요하지 않습니다. 하드웨어와의 불일치를 수정하려면 레이저 flip / orientation 설정을 사용하는 것이 더 좋습니다.
* **Output Range horizontal / vertical** - 레이저 스캐너의 최대/최소 각도와 관련된 설정입니다. 60º가 표준이지만, 사용하는 레이저가 다르다면 조정할 수 있습니다.

#### Canvas

Canvas 시스템을 사용하는 경우, 3D 뷰 안에 Canvas 이미지를 포함하도록 선택할 수도 있습니다. 체크박스를 활성화해 Canvas를 렌더링하고, position, orientation, scale 설정을 사용해 3D 뷰 안에서 어떻게 보일지 결정합니다.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D Visualiser Canvas 설정</p></figcaption></figure>

{% hint style="info" %}
"유령" 레이저가 보이나요? 3D Visualiser는 레이저 설정과 어느 정도 독립적으로 동작하므로, Liberation에 있는 레이저보다 Visualiser 안에 더 많은 레이저가 있을 수 있습니다. 프로젝트에 레이저를 추가하면 Visualiser 안에도 새 레이저 오브젝트가 추가됩니다. 하지만 레이저를 삭제해도 Visualiser에는 "유령" 레이저 오브젝트가 남아 있습니다.

모든 유령 레이저를 제거하려면 _Remove extra 3D laser objects_ 버튼(3D Visualiser settings 패널 하단)을 클릭합니다.

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
