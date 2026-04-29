---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ 컨트롤러 할당

Liberation에서 레이저 설정을 완료한 후에는 각 레이저를 실제 환경의 레이저 컨트롤러에 할당할 수 있습니다. 사용할 수 있는 하드웨어를 확인하려면 [호환되는 레이저와 컨트롤러(DAC)](../hardware/compatible-lasers-and-controllers-dacs.md)를 참고하세요. 컨트롤러는 USB 또는 네트워크를 통해 연결됩니다.

* _View -> Controller Assignment_ 메뉴 옵션에서 _Controller Assignment_ 패널을 엽니다. 또는 _Laser Overview_ 패널의 _ASSIGN LASER CONTROLLERS_ 버튼을 사용할 수도 있습니다.

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment 패널"><figcaption></figcaption></figure>

* 패널은 두 부분으로 나뉘며, 왼쪽에는 레이저 목록이, 오른쪽에는 사용 가능한 컨트롤러 목록이 표시됩니다. 목록에 레이저 컨트롤러가 보이지 않으면 _REFRESH_ 버튼을 누르세요. 문제가 계속되면 [문제 해결](../troubleshooting/)을 참고하세요.
* 레이저에 컨트롤러를 할당하려면 오른쪽에서 왼쪽의 빈 레이저 슬롯으로 클릭한 상태로 드래그하세요. 이렇게 하면 Liberation이 어떤 레이저에 어떤 컨트롤러를 사용할지 알 수 있습니다. 마음이 바뀌면 컨트롤러를 위아래로 자유롭게 드래그하여 다른 레이저로 옮길 수 있습니다.

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="컨트롤러 목록" width="375"><figcaption></figcaption></figure>

* 컨트롤러 옆에 초록색 사각형이 표시되면 Liberation이 해당 컨트롤러에 성공적으로 연결되었다는 뜻입니다.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream과 Helios DAC가 각각 레이저 2와 3에 할당된 상태</p></figcaption></figure>

{% hint style="info" %}
컨트롤러에 연결할 때마다 레이저는 자동으로 disarm됩니다.
{% endhint %}

* 주황색 사각형 🟧은 컨트롤러에 간헐적인 연결 문제가 있다는 뜻입니다. 보통 네트워크 문제로 인해 발생하며, [문제 해결](../troubleshooting/)을 참고하세요.
* 빨간색 사각형 🟥은 컨트롤러에 연결할 수 없다는 뜻입니다. [문제 해결](../troubleshooting/)을 참고하세요.
* _disconnect button_ (X)은 컨트롤러 연결을 해제하지만 레이저 할당에서는 제거하지 않습니다. 이후 _reconnect button_ (새로고침 화살표 아이콘)을 사용해 다시 연결하거나, _disconnect button_ 을 한 번 더 클릭하여 할당을 지울 수 있습니다.
* _Advanced feature :_ 차트처럼 보이는 버튼을 클릭하면 컨트롤러 analytics 패널이 열립니다. 이 고급 기능은 데이터 스트림에 대한 자세한 정보를 제공하며 문제 해결에 도움이 될 수 있습니다. 일부 컨트롤러 유형에서는 이 옵션을 사용할 수 없을 수도 있습니다.
* _rename button_ (연필)을 사용해 이 컨트롤러의 이름을 원하는 대로 변경할 수 있습니다. 특정 하드웨어와 쉽게 연결해 떠올릴 수 있는 이름으로 지정하는 것이 좋습니다. 레이저에 내장된 컨트롤러라면 그에 맞게 이름을 지정할 수 있습니다. 예: _LaserCube Ultra #1_ 또는 _Triton T5 #3._ 이 이름은 Liberation 설치 환경에 저장되며 이후 계속 표시됩니다. 레이저를 빠르게 식별하는 데 매우 유용합니다.

{% hint style="info" %}
Pro tip - 오른쪽의 컨트롤러를 **더블 클릭**하면 왼쪽에서 다음으로 사용 가능한 레이저에 자동으로 할당됩니다. 할당해야 할 레이저가 많을 때 시간을 크게 줄일 수 있습니다!
{% endhint %}

_DISCONNECT ALL_ 및 _RECONNECT ALL_ 버튼을 사용하면 모든 연결을 빠르게 재설정할 수 있습니다. 네트워크 문제가 있을 때 유용합니다.
