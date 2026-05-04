---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Global Transformations

클립 변환(shift x/y, scale x/y) 외에도 실행하는 모든 클립에 적용되는 Global Transformations가 있습니다. 이를 확인하려면 _Global Transformations_ 패널을 엽니다. (이 패널은 보통 _Clip Settings_ 옆 탭에 있습니다.)

기본적으로 이 설정들은 재생 중인 클립이 더 이상 없으면 모두 즉시 초기화됩니다. 이 초기화 동작은 _Global Transformations_ 패널 하단의 _AUTO RESET_ 버튼으로 비활성화할 수 있습니다.

{% hint style="info" %}
Global Transformations는 Canvas에는 영향을 주지 않으며, Beam 및 DMX 존에만 적용됩니다.
{% endhint %}

### Scale X/Y

가로 및 세로 스케일입니다. `Shift`를 누르지 않는 한 두 값은 함께 잠겨 있습니다. 기본적으로 APC40 Device Control 노브 4와 8에도 매핑되어 있으며, Clip Deck 오른쪽의 상황별 Parameters 패널에 표시됩니다.

### Shift X/Y

가로 및 세로 이동입니다. 모든 요소를 가로/세로 방향으로 이동합니다.

### Spin

모든 콘텐츠를 중심 기준으로 회전시킵니다. 양수 값은 시계 방향으로, 음수 값은 반시계 방향으로 회전합니다. 이 설정이 _Rotation_ 변환에 영향을 주는 것을 확인할 수 있습니다. 기본적으로 APC40 Device Control 노브 3에 매핑되어 있으며, Clip Deck 오른쪽의 상황별 Parameters 패널에 표시됩니다.

### Spin 3D

모든 콘텐츠를 Y축(중앙의 세로선)을 기준으로 회전시킵니다. 이 설정이 _Rotation3D_ 변환에 영향을 주는 것을 확인할 수 있습니다. 기본적으로 APC40 Device Control 노브 7에 매핑되어 있으며, Clip Deck 오른쪽의 상황별 Parameters 패널에 표시됩니다.

### Rotation

중심을 기준으로 한 회전이며, 값의 단위는 도입니다.

### Rotation 3D

Y축(중앙의 세로선)을 기준으로 한 회전이며, 값의 단위는 도입니다.

### Auto reset

켜져 있으면 현재 실행 중인 모든 클립이 비활성화되는 즉시 모든 Global Transformations가 초기화됩니다. 따라서 다음에 클립을 실행할 때 예상치 못한 결과가 나오지 않도록 할 수 있습니다!
