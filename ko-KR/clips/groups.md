---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/groups
---

# 🟩 Clip 그룹

각 Clip에는 색상 테두리가 있으며, 이 색상은 해당 Clip이 속한 _group_을 나타냅니다. APC40 Clip 버튼도 해당 Group 색상으로 켜집니다.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>시안</td></tr><tr><td>Group 2</td><td>주황</td></tr><tr><td>Group 3</td><td>빨강</td></tr><tr><td>Group 4</td><td>인디고</td></tr><tr><td>Group 5</td><td>초록</td></tr></tbody></table>

Group 시스템은 매우 유연하며, 다음과 같은 작업을 할 수 있습니다.

* 한 Group의 Clip은 계속 재생하면서 다른 Group을 전환하기
* Group 내 모든 Clip에 zone과 X/Y flip을 빠르게 할당하기
* Clip에 _Flash mode_ 설정하기(Group 3은 기본적으로 _Flash mode_로 설정되어 있음)
* Clip이 상속하거나 개별적으로 재정의할 수 있는 기본 transition in/out 시간 설정하기

_group_ 시스템을 어떻게 사용할지는 사용자에게 달려 있습니다. 다만 zone/laser가 많다면 서로 다른 laser 그룹에 서로 다른 Group을 사용하는 것이 도움이 될 수 있습니다. 물론 사용 방식은 자유입니다. 시작점으로, 저는 보통 Group을 다음과 같이 사용합니다.

<table data-header-hidden><thead><tr><th width="108"></th><th width="121"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>시안</td><td>가장 자주 사용하는 beam zone의 기본 Group입니다.</td></tr><tr><td>Group 2</td><td>주황</td><td>보조 laser beam zone Group입니다.</td></tr><tr><td>Group 3</td><td>빨강</td><td><em>flash</em> mode에 할당되며, 라이브로 연주하는 보통 빠른 빛의 stab에 사용합니다.</td></tr><tr><td>Group 4</td><td>인디고</td><td>느린 기본 fade in/out을 사용하는 더 느리고 부드러운 Clip입니다.</td></tr><tr><td>Group 5</td><td>초록</td><td>Graphics / canvas Clip입니다.</td></tr></tbody></table>

### _Group_ 버튼

_Group_ 버튼은 Clip Deck 오른쪽에 있으며, 버튼을 활성화하면 다음을 할 수 있습니다.

* Clip을 Group에 할당
* Group 내 모든 Clip의 zone 설정과 X/Y flip 변경

_group_ 버튼을 활성화하려면 다음 중 하나를 사용합니다.

* APC40에서 _group_ 버튼을 길게 누릅니다.
* 화면의 _group_ 버튼을 마우스로 클릭합니다. 다시 클릭하면 꺼집니다.

_group_ 버튼이 활성화된 상태에서 Clip을 누르면 해당 Group에 쉽게 할당할 수 있습니다. (Clip의 우클릭 메뉴로도 Group을 할당할 수 있습니다.)

### Group 내 모든 Clip의 zone 설정 변경

_group_ 버튼이 활성화되면 _zone_ 버튼(BEAM 1 - 8, CANVAS 1 등)이 다음과 같이 켜집니다.

* OFF : 이 zone은 해당 Group의 어떤 Clip에도 설정되어 있지 않습니다.
* FLASHING : 이 zone은 Group 내 Clip 중 _**일부**_**&#x20;에는 설정되어 있지만&#x20;**_**전체**_에는 설정되어 있지 않습니다.
* ON : 이 zone은 Group 내 _**모든**_ Clip에 설정되어 있습니다.

zone 버튼을 눌러 해당 Group의 _**모든**_ Clip에서 그 zone을 활성화하거나 비활성화합니다.

X/Y flip 버튼에도 정확히 같은 개념이 적용됩니다.
