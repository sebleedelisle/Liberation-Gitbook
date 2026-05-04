---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ DMX 존

DMX zone은 레이저 포인트 대신 Art-Net/DMX를 전송하는 Liberation 출력 zone입니다. beam zone 및 canvas zone과 함께 표시되므로, 동일한 zone 선택 워크플로에서 Clip을 할당할 수 있습니다.

메뉴에서 **DMX Zones**를 열거나 Laser overview의 DMX 섹션을 사용해 관리할 수 있습니다.

* **ADD DMX ZONE** - 새 DMX zone을 만듭니다.
* **ARM** - 해당 zone의 DMX 출력을 활성화합니다. 무장되지 않은 DMX zone은 매핑된 채널을 0으로 지웁니다.
* **Node** - Art-Net node 번호를 선택합니다.
* **Universe** - Art-Net 유니버스를 선택합니다. 표시되는 값은 1부터 시작하므로, Universe 1이 첫 번째 유니버스입니다.
* **Address** - 픽스처의 시작 주소를 설정합니다. 표시되는 값도 1부터 시작합니다.
* **Preset** - Clip 콘텐츠를 DMX 채널에 매핑하는 DMX 프리셋을 선택합니다.
* **Edit DMX zone settings**(연필 아이콘) - 수동 zone 포워딩 및 픽스처 방향과 같은 zone 설정을 엽니다.
* **Edit DMX profile/channel mapping**(슬라이더 아이콘) - DMX 프리셋/채널 편집기를 엽니다.
* **Delete** - DMX zone을 제거합니다.

### 무장 제한

동시에 무장할 수 있는 DMX zone 수는 라이선스 등급에 따라 달라집니다. 현재 등급에서 DMX 출력을 허용하지 않거나 이미 최대 개수의 DMX zone을 무장한 경우, 추가 zone의 **ARM** 버튼이 비활성화되며 마우스를 올리면 진입 금지 아이콘이 표시됩니다.

더 많은 zone을 무장하려면 먼저 다른 DMX zone의 무장을 해제하거나, DMX 제한이 더 높은 라이선스 등급을 사용하세요.
