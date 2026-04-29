---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>LaserCube 홍보 이미지 제공: Wicked Lasers</p></figcaption></figure>

Wicked Lasers의 [LaserCube](https://www.laseros.com/lasercube/)는 배터리로 구동되는 매우 컴팩트한 레이저 장치로, 여러 출력 구성으로 제공됩니다. 사용하기 쉬운 스마트폰 앱 덕분에 취미 사용자들에게 인기가 많지만, 최신 모델은 전문 쇼에서도 사용할 수 있을 만큼 충분한 성능을 갖추고 있습니다.

휴대폰 앱(LaserOS라고 하며 데스크톱용도 제공)은 무료로 다운로드할 수 있고 재미있게 사용해 볼 수 있으며, 대부분의 사용자에게는 충분합니다. 하지만 여러 대의 레이저로 더 큰 쇼를 운영한다면 더 전문적이고 강력한 도구가 필요합니다. 이때 Liberation을 사용할 수 있습니다.

### LaserCube에 연결하기

초기 LaserCube는 USB로 제어되지만, 현재 모델은 모두 내장 네트워크 컨트롤러를 갖추고 있습니다. 이러한 네트워크 제어 방식의 큐브는 "LaserCube Wifi"라고 합니다. Liberation은 USB로 연결하든 네트워크로 연결하든 두 종류의 LaserCube를 모두 지원합니다\*.

\*(LaserCube 네트워크 프로토콜 지원은 버전 0.7.3에서 도입되었습니다)

### USB LaserCube

micro USB 케이블로 LaserCube를 컴퓨터에 연결한 다음 _Controller Assignment_ 패널에서 확인합니다([컨트롤러 할당](../setting-up/controller-assignment.md) 참고). 자동으로 표시되지 않으면 _REFRESH_ 버튼을 누르세요.

### 네트워크 LaserCube "Wifi"

{% hint style="danger" %}
"Wifi" 큐브는 무선 네트워크를 통해 작동하도록 설계되어 있지만, 이 방식은 권장하지 않습니다. 드롭아웃이나 글리치가 발생할 가능성이 높습니다. 대신 Ether Dreams를 사용할 때처럼 RJ45 소켓을 사용해 LaserCube를 유선 네트워크에 연결하세요.
{% endhint %}

LaserCube를 유선 네트워크에 연결합니다.

LaserCube를 "LAN Client" 모드로 설정하고 네트워크에 라우터가 있는지 확인합니다. LaserCube는 라우터에서 IP 주소를 받아오며, 이후 _Controller Assignment_ 패널에 표시되어야 합니다([컨트롤러 할당](../setting-up/controller-assignment.md) 참고).

{% hint style="info" %}
라우터 없이 네트워크를 구성하고 모든 장치에 고정 IP 주소를 지정할 수도 있으며, 이벤트 업계에서는 매우 흔한 방식입니다. 개인적으로는 네트워크에 라우터를 추가하는 방식을 선호하며, 네트워크 경험이 많지 않은 사용자에게는 이 옵션을 권장합니다.

라우터가 모든 장치에 IP 주소를 동적으로 할당하므로 더 간단하고 오류가 적다고 생각합니다.
{% endhint %}

{% hint style="danger" %}
Ether Dream과 달리, _**LaserCube는 버퍼 언더런, 패킷 손실 또는 기타 손상되거나 잘못된 데이터를 만나도 레이저를 블랭킹하지 않습니다**_.

대신 마지막으로 멈춘 지점부터 계속 진행합니다. 경우에 따라 이로 인해 활성 빔이 zones 안에 있지 않은 영역을 가로지를 수 있으며, 더 심각하게는 소프트웨어 masks를 가로질러 지나갈 수도 있습니다.

저는 LaserCube의 설계자/개발자들과 이 문제에 대해 논의 중이며, 향후 펌웨어 업데이트로 해결되기를 기대하고 있습니다. 하지만 그전까지는 레이저가 닿으면 안 되는 모든 위치를 반드시 물리적으로 마스킹해야 합니다.

공정하게 말하면, 사실 이는 어쨌든 해야 하는 조치입니다. 다만 저는 카메라와 프로젝터를 보호하기 위해 소프트웨어 masks를 사용합니다. 따라서 LaserCube 네트워크 프로토콜을 사용할 때는 Ether Dream을 사용할 때보다 이 방식이 더 위험하다는 점을 인지해야 합니다. Ether Dream은 오류나 누락된 데이터가 발생하는 즉시 안전 정지 모드로 들어갑니다.

또한 이미 말했지만 **LaserCube에는 유선 연결을 사용하세요**. Wifi로는 충분하지 않으며 이 문제를 더 악화시킬 수 있습니다.
{% endhint %}
