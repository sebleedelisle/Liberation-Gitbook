---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ DMX 존 만들기

1. Art-Net node를 연결하고 [Art-Net node에 연결하기](../connecting-to-an-artnet-node.md "mention")에 따라 설정합니다.
2. **DMX Zones**를 열고 **ADD DMX ZONE**을 클릭합니다.
3. fixture와 일치하도록 zone의 **Node**, **Universe**, **Address**를 설정합니다.
4. fixture에 사용할 **Preset**을 선택합니다. preset은 고정값, 콘텐츠 켜기/끄기 값, RGB 색상, X/Y 위치, 밝기 또는 명시적인 DMX Value 입력을 받을 DMX channel을 정의합니다.
5. channel mapping을 편집하려면 **Edit DMX profile/channel mapping**(슬라이더 아이콘)을 클릭합니다. 기본 preset은 콘텐츠 켜기/끄기 channel과 RGB 색상 channel로 시작합니다.
6. beam zone 또는 canvas zone에 할당하는 것과 같은 방식으로 DMX zone에 Clip을 할당합니다.
7. zone에서 DMX를 출력할 준비가 되면 **ARM**을 누릅니다.

{% hint style="warning" %}
ARM 상태인 DMX zone만 실시간 값을 전송합니다. ARM 상태가 아닌 DMX zone은 매핑된 channel을 0으로 초기화하므로 fixture를 설정할 때 더 안전합니다.
{% endhint %}

DMX 출력은 licence tier에 따라서도 제한됩니다. **ARM** 버튼이 비활성화되어 있으면 현재 tier에 DMX 출력이 포함되어 있는지, 또는 ARM 상태인 DMX zone의 최대 개수에 이미 도달했는지 확인하세요.
