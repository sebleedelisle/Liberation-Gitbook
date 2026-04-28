---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ 소개

Liberation에는 Art-Net을 통해 조명 효과를 만들고 DMX 호환 레이저를 제어할 수 있는 유연하고 강력한 DMX 시스템이 포함되어 있습니다. 별도의 조명 콘솔 없이도 조명을 레이저 쇼와 쉽게 동기화할 수 있도록 설계되었습니다.

{% hint style="info" %}
**Art-Net이란 무엇이며, DMX와는 어떤 관계가 있나요?**

**DMX**는 조명, 레이저, 스모크 머신 및 기타 무대 효과를 제어하는 데 오랫동안 사용되어 온 시스템입니다. 특수 케이블(일반적으로 XLR 커넥터 사용)을 통해 제어 신호를 보내며, 각 fixture는 지정된 채널 세트를 수신해 어떤 동작을 할지 판단합니다.

**Art-Net**은 동일한 DMX 데이터를 일반 컴퓨터 네트워크를 통해 전송하는 더 새로운 방식입니다. 특수 케이블을 사용하는 대신, 인터넷이나 로컬 네트워크 트래픽처럼 Ethernet을 통해 모든 데이터를 전송합니다.

Liberation에서는 모든 DMX output이 Art-Net을 사용해 전송됩니다. Art-Net 호환 장치를 직접 제어하는 데 사용할 수 있으며, **Art-Net node**를 연결할 수도 있습니다. Art-Net node는 Art-Net을 표준 DMX로 다시 변환하는 작은 장치입니다. 즉, 장치 자체가 Art-Net을 지원하지 않더라도 기존 DMX 조명과 효과 장비를 계속 제어할 수 있습니다.
{% endhint %}

스모크 머신, 헤이저, CO₂ 제트, 콜드 스파크 머신 등 다양한 무대 장비를 제어하는 데도 사용할 수 있습니다. DMX를 지원한다면 DMX zone으로 설정하고, 레이저 콘텐츠와 함께 Liberation에서 바로 트리거할 수 있습니다.

DMX fixture는 **DMX zone**으로 추가되며, 레이저 빔 zone 및 Canvas 타깃 영역과 함께 zone 목록에 표시됩니다. 각 DMX zone은 **DMX preset**을 사용합니다. DMX preset은 위치, 색상, 밝기 같은 레이저 Clip의 속성을 DMX 채널 값에 어떻게 매핑할지 Liberation에 알려줍니다.

Clip을 DMX zone으로 보내면 Liberation은 Clip의 첫 번째 요소를 확인하고 preset에 따라 해당 속성을 변환합니다. 이를 통해 레이저에 이미 사용하고 있는 동일한 Clip으로 조명과 DMX 효과를 직접 구동할 수 있습니다.

#### Glastonbury에서의 Liberation

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Liberation DMX 시스템의 첫 실제 테스트는 Glastonbury 2023에서 진행되었습니다. 당시 Reach Lasers는 Arcadia "spider" 스테이지의 일부로 총 90개의 빔 소스를 설치했습니다.

18대의 레이저는 내부 Ether Dream으로 제어되었고, 추가로 12대의 6-head beam bar는 Art-Net과 DMX를 통해 제어되었습니다.
