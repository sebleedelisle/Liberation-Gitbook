# ✅ 빠른 시작 가이드

## 소개

**Liberation**에 오신 것을 환영합니다. Liberation은 차세대 레이저 쇼 소프트웨어입니다.

Liberation은 강력하고 복잡한 현대적 소프트웨어이지만, 사용성과 안정성의 기본 원칙 위에 만들어져 창의성을 자유롭게 표현할 수 있도록 설계되었습니다. 빠르고 효율적이며 매끄럽게 작동합니다. 이 _빠른 시작 가이드_를 따라 하면 짧은 시간 안에 기본 사용을 시작할 수 있습니다!

### 레이저 관리

Liberation은 매우 유연해서 실제 레이저가 전혀 연결되어 있지 않아도 레이저를 설정하고 시각화할 수 있습니다. 준비가 되면 각 output을 laser controller에 매끄럽게 할당할 수 있습니다.

{% hint style="info" %}
Liberation 안에서는 원하는 만큼 많은 레이저를 설정하고 시각화할 수 있습니다. 라이선스 등급(Hobbyist, Pro 등)은 _arm 상태로 전환할 수 있는_ 레이저 수만 제한합니다. 즉, 무료 라이선스만으로도 100대의 레이저 쇼를 설계할 수 있습니다. 실제 레이저에서 실행해야 할 때만 업그레이드하면 됩니다.
{% endhint %}

기본 설정에는 레이저 8대가 가로로 배치되어 있지만, 원하는 방식으로 변경할 수 있습니다. 소프트웨어에 익숙해지는 동안에는 이 기본값을 유지하는 것이 좋고, 나중에 실제 하드웨어 구성에 맞게 조정하면 됩니다. ([프로젝트 설정하기](../setting-up/setting-up-your-project.md) 참조)&#x20;

{% hint style="warning" %}
중요: 레이저를 arm 상태로 전환하기 전에 관련 위험을 반드시 이해하고, [레이저 설정하기](../setting-up/setting-up-lasers.md) 장을 주의 깊게 확인하세요.
{% endhint %}

## 소프트웨어 개요

### 안전 차단

레이저를 실행할 때는 항상 **하드웨어 비상 정지 버튼**을 가까이에 두어야 합니다([비상 정지 및 인터록](../hardware/emergency-stop-interlocks.md) 참조). 덜 긴급한 상황에서 전체 출력을 disarm 상태로 전환하려면 _**DISARM ALL**_ 버튼이나 `Escape` 키 또는 APC40의 _**SESSION**_ 키를 사용할 수 있습니다. 화면의 슬라이더나 APC40의 메인 페이더로 Global Brightness를 낮출 수도 있습니다.

### 슬라이더 요소

Liberation 전반에는 다양한 슬라이더와 컨트롤이 있습니다.

{% hint style="info" %}
슬라이더보다 더 정밀한 제어가 필요하면 `Cmd / Ctrl` 키를 누른 상태로 슬라이더를 클릭해 새 값을 직접 입력할 수 있습니다.
{% endhint %}

### 키보드 단축키

전체 키보드 단축키 목록은 여기에서 확인할 수 있습니다: [키보드 단축키](../reference/keyboard-shortcuts.md)

### 화면 구성

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
특정 버튼의 기능이 궁금한가요? 마우스를 올리면 설명이 표시됩니다!
{% endhint %}

#### 메뉴

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

메뉴에서는 모든 파일 가져오기/내보내기 옵션을 찾고 panel을 열 수 있습니다. 여기에서 구독으로 컴퓨터를 인증하는 옵션도 사용할 수 있습니다(_Liberation -> Authorise/Deauthorise this computer_).

#### 아이콘 바

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

모든 레이저의 arm/disarm 전환, Global Brightness, test pattern, 3D, Canvas, Output view 전환 같은 자주 쓰는 작업을 여기에서 사용할 수 있습니다.

### Views

화면 왼쪽 위의 큰 영역은 세 가지 주요 view 중 하나로 표시됩니다: **3D**, **CANVAS**, **OUTPUT.** 아이콘 바 버튼으로 전환할 수 있습니다. 또는 `Tab` 키를 사용해 3D view와 OUTPUT view 사이를 전환하고, 이후 각 레이저 output을 순서대로 계속 이동할 수 있습니다.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view는 레이저가 어떻게 보일지 보여 주며, 실제 레이저 구성과 일치하도록 설정할 수 있습니다. 클릭 후 드래그하면 카메라가 회전하고, 마우스 휠을 사용하면 앞뒤로 이동할 수 있습니다. _3D Visualiser settings_ panel(_View -> 3D Visualiser Settings_)에서 더 많은 옵션을 찾을 수 있습니다. [3D Visualiser](../setting-up/3d-visualiser.md)를 참조하세요.

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view는 각 레이저의 zones 및 masks를 설정하는 데 사용합니다. 왼쪽 위에 큰 숫자가 표시되어 현재 어떤 레이저를 보고 있는지 쉽게 알 수 있습니다.

이 view는 해당 레이저 전체 output과 그 안에서 각 zone 영역이 어디에 위치하는지를 나타냅니다. 기본적으로 레이저마다 zone 영역은 하나뿐이지만, 실제로 관리 가능한 범위 안에서 원하는 만큼 zones를 추가할 수 있으며 이 view에서 모두 확인할 수 있습니다.

{% hint style="info" %}
**zone이란 무엇인가요?**

zone은 laser output 안에서 레이저 콘텐츠를 보낼 수 있는 공간입니다. 레이저 하나에 여러 zone 영역을 둘 수 있습니다. 가장 단순한 유형은 _beam_ zone이며, 그 외에도 _canvas_ zones와 _DMX_ zones가 있습니다. 이 가이드에서는 주로 beam zones에 집중합니다. beam zones는 일반적으로 공기 중에 분위기 있는 빔 효과를 만드는 데 사용됩니다.
{% endhint %}

편집할 레이저는 다음 방법으로 선택할 수 있습니다.

* 상단 바의 번호 버튼
* 원하는 레이저 번호 키 누르기 _(1~9_ keys\_)\_
* `Tab` 키로 하나씩 순환

설정에 새 레이저를 추가하려면 _+_ 버튼을 누릅니다. (_Laser Overview_ panel에도 _ADD LASER_ 버튼이 있습니다.)

설정에서 레이저를 삭제하려면 _Laser Overview_ panel의 빨간색 ⊖ 버튼을 누릅니다.

마우스 스크롤 휠로 확대/축소할 수 있고, zone 영역이 아닌 곳을 클릭 후 드래그하면 view를 이동할 수 있습니다.

zone 영역을 클릭해 선택한 다음, 마우스로 모서리 점을 조정합니다. 모서리를 드래그하는 동안 `Alt / Option` 키를 누르면 비균일하게 조정할 수 있습니다. zone 영역을 오른쪽 클릭하면 zone 유형 변경을 포함한 추가 옵션을 볼 수 있습니다.

왼쪽에는 여러 아이콘 버튼이 있는 바가 있습니다. 버튼 위에 마우스를 올리면 기능 설명이 표시됩니다. 여기의 버튼으로 beam zones, canvas zones, masks를 추가할 수 있습니다. 또한 이 레이저에만 test pattern을 설정하는 옵션과 그리드 및 스냅 설정도 있습니다.

자세한 내용은 [Output view](../output-view/)를 참조하세요.

#### Canvas

Canvas 시스템은 주로 그래픽과 건축물 매핑에 사용됩니다. 복잡한 이미지를 여러 레이저에 분산하고 각 섹션의 원근을 보정할 수 있습니다. [그래픽 및 Canvas 시스템](../graphics-and-the-canvas-system/)을 참조하세요.

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

마우스와 키보드로 Liberation을 제어할 수도 있지만, APC40 MIDI control interface를 사용하는 것이 훨씬 좋습니다(Mark 2가 가장 좋지만 Mark 1도 작동합니다).

함께 보기: [APC40 참조](../reference/apc40-reference.md)

현재 APC Mini Mark 2와 MIDI Fighter Twister 지원도 구현되어 있으며, 더 많은 장치를 개발 중입니다. 하지만 대부분의 경우 APC40 Mark 2가 가장 좋은 선택입니다.&#x20;

### Clips 및 효과

{% hint style="info" %}
**Clip이란 무엇인가요?**

Clip은 Liberation 안의 모든 레이저 콘텐츠를 담는 컨테이너입니다. Clips에는 beams 또는 그래픽 애니메이션이 포함될 수 있으며, 일반적으로 반복 재생되는 사이클입니다. Clip 콘텐츠는 어떤 zone 또는 _Canvas target area_로도 보낼 수 있고, Clip Deck 안의 Clip 버튼으로 트리거합니다.
{% endhint %}

#### Clip Deck 개요

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

이 그리드는 _Clip Deck_이라고 하며, 모든 레이저 Clips가 저장되는 곳입니다. APC40의 8 x 5 버튼 그리드에 직접 매핑되도록 설계되었습니다.

**Clip Deck 탐색**

Clip Deck은 다음 방법으로 좌우 스크롤할 수 있습니다.

* 왼쪽/오른쪽 화살표 키. `Cmd / Ctrl`을 함께 누르면 한 페이지씩 스크롤합니다.
* 트랙패드: 스와이프
* 마우스: 마우스에 가로 스크롤이 있으면 Clip Deck 위에 올린 상태로 사용할 수 있습니다.
* APC40 스크롤 노브
* APC40 _<- DEVICE ->_ 버튼

위치를 파악하기 쉽도록 상단에는 Clip Deck의 미니 visualiser가 있습니다. 함께 보기: [Clips](../clips/)

#### Clip 시작 및 중지

Clip 버튼을 누르면(마우스 또는 APC40 사용) Clip 재생이 시작됩니다. 다시 누르면 중지됩니다. Clip 재생을 시작하면 _shift_를 누르고 있지 않은 한 같은 색상의 다른 모든 Clips는 자동으로 중지됩니다.

일부 Clips는 _Flash mode_ 상태일 수 있습니다(기본값에서는 빨간색 Clips). 이 경우 Clip 버튼에서 손을 떼는 즉시 중지됩니다.

_STOP_ 버튼은 현재 실행 중인 모든 Clips를 중지합니다.

#### Clip output zones 설정

Clip 버튼 아래에는 zone 버튼이 표시됩니다. 기본값은 beam zones 1~8입니다(_BEAM 1_, _BEAM 2_ 등). zone 버튼의 불빛은 현재 선택된 Clip에 어떤 zones가 할당되어 있는지 나타냅니다.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

zone 버튼에서 두 줄 아래에는 X/Y flip 버튼이 있습니다. 이 버튼을 토글하면 Clip이 가로 또는 세로로 뒤집힙니다.

{% hint style="info" %}
이 zone 할당 및 X/Y flip 설정은 Clip 자체에 연결되어 있습니다. 다음에 해당 Clip을 실행할 때도 유지됩니다. Global 설정이 아닙니다.
{% endhint %}

Clip을 오른쪽 클릭하면 더 많은 Clip 설정을 편집할 수 있습니다. [Clip 설정](../clips/clip-settings.md)도 참조하세요.

### Groups

각 Clip에는 색상 외곽선이 있으며, 이 색상은 Clip이 속한 _group_을 나타냅니다. APC40의 Clip 버튼도 이 색상으로 켜집니다.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>청록색</td></tr><tr><td>Group 2</td><td>주황색</td></tr><tr><td>Group 3</td><td>빨간색</td></tr><tr><td>Group 4</td><td>남색</td></tr><tr><td>Group 5</td><td>초록색</td></tr></tbody></table>

group 시스템은 매우 유연하며 다음을 할 수 있습니다.

* 한 group의 Clips는 계속 실행하면서 다른 group을 토글
* group 안의 모든 Clips에 zones 및 X/Y flips를 빠르게 할당
* Clip에 _Flash mode_ 설정(Group 3은 기본적으로 _Flash mode_로 설정됨)

Groups에는 전환 in/out 설정도 있으며, 이 설정은 Clips가 상속하거나 개별적으로 재정의할 수 있습니다.

Clip의 group은 오른쪽 클릭 메뉴의 버튼으로 지정할 수 있습니다. APC40을 사용할 때는 group 버튼을 누른 상태에서 Clip 버튼을 누르면 됩니다.

group 안의 모든 Clips에 대한 zone 설정 변경

APC40을 사용할 때는 group 버튼을 누른 다음, _계속 누른 상태에서_ zone 및 X/Y 버튼으로 해당 group 안의 모든 Clips에 대한 zone 설정을 토글합니다.

함께 보기: [Groups](../clips/groups.md)

### 효과

Liberation의 효과 시스템은 Clip output을 실시간으로 변경하는 강력하고 다용도적인 방법입니다. 기본 효과 버튼 1~8은 zone 버튼 아래에 있습니다.

#### 효과 적용

효과 버튼을 눌러 효과를 토글할 수 있습니다. 더 좋은 방법은 APC40 슬라이더 1~8을 사용해 효과를 페이드 인/아웃하는 것입니다.

#### 효과 파라미터

각 효과의 _parameter_를 조정하려면 rotary controllers 1~8\*을 사용합니다. 또는 마우스로 오른쪽 클릭해 level과 parameter를 조정할 수도 있습니다. parameter 변경은 효과 설정에 따라 서로 다른 동작을 합니다. 기본 효과는 아래 목록을 참조하세요.

{% hint style="info" %}
효과 버튼에 표시되는 작은 숫자는 효과의 _level_과 _parameter_를 의미합니다. _level_은 APC40의 페이더로 제어하거나 버튼을 클릭 후 드래그해 조정할 수 있습니다. parameter는 APC40의 rotary로 조정하거나 마우스 오른쪽 클릭으로 조정할 수 있습니다.
{% endhint %}

_\*Rotary controllers 1~8은 APC40 Mk2에서는 상단에, Mk1에서는 오른쪽 상단에 있습니다. 함께 보기:_ [APC40 참조](../reference/apc40-reference.md)

#### 기본 효과

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Clip output에 무작위적인 움직임을 적용합니다. parameter는 무작위성의 양/속도를 조정합니다.
2. **Sine wave** :\
   모든 콘텐츠를 움직이는 사인파 형태로 왜곡합니다. parameter는 파장을 조정합니다.
3. **Rotation** :\
   모든 것을 회전시킵니다. parameter는 회전 속도를 조정합니다.
4. **Horizontal flip** :\
   모든 것을 가로 방향으로 압축하고 늘립니다. parameter는 속도를 조정합니다.
5. **Scale** :\
   모든 것을 전체 크기에서 0까지 반복적으로 스케일합니다. parameter는 속도를 조정합니다.
6. **Hue** :\
   모든 요소의 hue를 변경하지만 saturation은 변경하지 않습니다(예: 흰색은 흰색으로 유지). parameter는 hue를 조정합니다.
7. **Saturation and hue** :\
   모든 요소의 hue를 변경하고 색상을 완전히 포화시킵니다(예: 흰색이 해당 색상으로 바뀜). parameter는 hue를 조정합니다.
8. **Flash** :\
   모든 요소의 밝기를 전체에서 0까지 반복적으로 깜박이게 합니다. parameter는 flash 속도를 조정합니다.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

하단 행에는 사전 설정된 hue 및 saturation 값을 적용하는 16개의 추가 색상 효과가 있습니다.

이것들은 기본 효과일 뿐이며, 거의 원하는 어떤 동작이든 하도록 편집할 수 있습니다!

#### _“현재 선택된 Clip”_이란 무엇인가요?

Clip 재생을 시작하면 활성 상태임을 나타내기 위해 불이 켜집니다. 또한 흰색 외곽선이 표시되며, 이것은 현재 _선택된_ Clip임을 의미합니다. zone 버튼을 토글하거나 Clip 설정을 조정할 때마다 이 변경 사항은 _현재 선택된 Clip_에 적용됩니다.

{% hint style="info" %}
Clip을 트리거하지 않고 선택하려면 Clip 버튼을 누르기 전에 `Alt / Option` 키를 누릅니다. 실행하지 않은 상태에서 zones 및 기타 설정을 조정할 때 좋은 방법입니다.
{% endhint %}

### Clip Settings panel

_Clip Settings_ panel을 사용해 스케일, X/Y 위치를 편집하고 강력한 zone delay 시스템에 접근할 수 있습니다.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Global Settings panel

_Global Settings_ panel에서 모든 zones에 걸친 전체 output에 영향을 주는 Global output 설정을 조정할 수 있습니다.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

AUTO RESET을 켜면 재생 중인 Clips가 없을 때마다 모든 _Global settings_가 자동으로 초기화됩니다.&#x20;

### 타이밍

거의 모든 레이저 디스플레이에는 음악 사운드트랙이 있으므로, Liberation의 타이밍 시스템은 분당 비트 수(BPM) 단위의 tempo를 기준으로 합니다. _Tempo Panel_에서는 시간을 시각적으로 볼 수 있습니다. 각 사각형은 한 박자를 나타내며, 박자에 맞춰 깜박이는 것을 확인할 수 있습니다.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

MIDI clock 및 Ableton Link를 포함한 여러 동기화 옵션이 있습니다. 음악의 tempo를 알고 있다면 화면의 슬라이더나 APC40 Tempo 노브로 수동 조정할 수 있습니다. 또한 _Tap Tempo_ 시스템을 사용해 음악에 맞출 수도 있습니다\_.\_

#### Tap Tempo

_Tap Tempo_는 음악 앱에서 흔히 쓰이는 용어로, 음악이 재생되는 동안 박자에 맞춰 탭하여 tempo를 설정할 수 있게 해 줍니다. 화면의 버튼을 사용할 수도 있지만, _T_ 키나 APC40의 _Tap Tempo_ 버튼을 사용하는 것을 권장합니다. 원한다면 풋 스위치도 사용할 수 있습니다.

tempo를 마디의 시작으로 재설정하려면 _R_ 키 또는 APC40의 _Metronome_ 버튼을 누릅니다.

tempo를 정수로 반올림하려면 _Y_ 키를 누르거나 APC40의 _Tempo_ 노브를 돌립니다. 분당 비트 수가 정수인 경우가 많은 전자 음악에서 유용할 수 있습니다.

### Clip Deck 정리

Clip Deck에서 Clip 위치를 옮기려면 클릭 후 새 위치로 드래그합니다. 드래그하는 동안 커서 키 또는 APC40의 스크롤 휠/버튼을 사용해 좌우로 스크롤할 수 있습니다.

드래그하는 동안 `Alt / Option` 키를 누르면 복사본이 만들어집니다.

Clip을 시작하지 않고 선택하려면 `Alt / Option` 키를 누른 상태로 Clip을 클릭합니다.

여러 항목을 선택하려면 `Alt / Option + Shift` 키를 누른 상태로 Clip을 클릭하거나, Clip 바깥을 클릭 후 드래그해 “lasso” 선택을 합니다.&#x20;

클릭 후 드래그하면 선택된 모든 Clips가 함께 드래그됩니다.

하나 이상의 Clips를 삭제하려면 Clip Deck 밖으로 드래그하거나(휴지통 아이콘이 표시됨), Clip 오른쪽 클릭 메뉴의 DELETE 버튼을 사용합니다.

### Laser Overview panel

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

_Laser Overview panel_은 현재 실행 중인 레이저의 상태를 빠르게 보여 줍니다. 오른쪽의 초록색 사각형은 laser controller가 정상 상태임을 나타냅니다. 주황색으로 바뀌면 가끔 drop-out이 발생하는 상태이고, 빨간색이면 연결이 끊어진 상태입니다. 회색이면 controller에 전혀 연결되어 있지 않은 상태입니다.&#x20;

가운데 그래프는 프레임 길이의 기록이며, 오른쪽 숫자는 현재 프레임 레이트입니다. 콘텐츠가 복잡할수록 프레임 레이트가 낮아집니다(즉 더 깜박여 보임). 약 25fps 이하에서는 다소 깜박이는 것처럼 보이기 시작합니다.&#x20;

### 레이저 연결 - Controller Assignment panel

_Assign Laser Controllers_ 버튼을 클릭하면 _Controller Assignment_ panel이 열립니다. 이 panel은 메뉴 바의 _View -> Controller Assignment_에서도 열 수 있습니다.

여기에서 어떤 레이저 outputs가 어떤 laser controllers로 갈지 선택할 수 있습니다. 오른쪽 목록에서 controllers를 왼쪽 슬롯으로 드래그 앤 드롭합니다. controllers의 이름은 어떤 레이저와 페어링되어 있는지에 맞게 변경할 수 있습니다(펜 아이콘 버튼 사용).

자세한 내용은 [Controller Assignment](../setting-up/controller-assignment.md) 장을 읽어 보세요.

{% hint style="danger" %}
레이저를 arm 상태로 전환하기 전에 반드시 [레이저 설정하기](../setting-up/setting-up-lasers.md) 장을 확인하세요.
{% endhint %}

### Laser Output panel

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

이 panel은 _현재 선택된 레이저_의 설정을 보여 줍니다(상단 숫자로 표시). 현재 선택된 레이저는 _tab_ 키, 번호 키, _Laser Overview_ panel의 레이저 번호 클릭, 또는 _output view_에서 레이저 번호 클릭으로 변경할 수 있습니다.

* **Number button** 레이저의 arm/disarm 상태를 전환합니다. 빨간색이면 레이저가 armed 상태입니다.
* **Brightness** 다른 레이저와 독립적으로 레이저 밝기를 조정합니다. 이 값은 _global brightness_ 설정과 결합됩니다. 예를 들어 둘 다 50%이면 실제 레이저 밝기는 25%가 됩니다.
* **Test Pattern** 이 레이저에만 test pattern을 켭니다(Global test pattern 설정을 재정의).
* **Orientation** 옆으로 또는 거꾸로 설치된 레이저를 보정합니다.
* **Flip Horizontal and Flip Vertical** 레이저 output을 반전합니다. 배선이 일관되지 않은 레이저의 output 보정에 유용합니다.
* **Copy Laser Settings** 이 레이저의 여러 설정을 다른 레이저로 복사할 수 있는 panel을 엽니다.

### Scanner 설정

디스플레이용 레이저는 하나의 레이저 빔을 매우 빠르게 움직이고 켜고 끄면서 공중에 형태를 그립니다. 선, 형태, 이미지로 보이는 것은 실제로는 눈이 따라갈 수 없을 만큼 빠르게 경로를 추적하는 빔입니다.

point stream은 레이저가 다음에 어디로 이동해야 하는지, 빔을 언제 켜고 꺼야 하는지를 알려 주는 데이터입니다. Liberation에서는 Clips가 레이저로 전송될 때 실시간으로 이 point stream으로 변환됩니다.

Liberation은 이 point stream이 생성되는 방식을 세밀하게 제어할 수 있게 해 주며, 각 레이저에 대해 부드러움, 밝기, 성능 사이의 균형을 맞출 수 있습니다.

{% hint style="info" %}
미리 계산된 point streams에 의존하는 오래된 레이저 소프트웨어에 익숙하다면 이 방식이 처음에는 다르게 느껴질 수 있습니다. 하지만 실시간 point 생성 방식은 같은 콘텐츠를 각 레이저에 맞게 다르게 최적화할 수 있게 해 줍니다. 따라서 scanner 속도나 품질이 서로 다른 여러 레이저를 사용할 때 콘텐츠를 복제하거나 다시 만들지 않아도 작업하기가 더 쉽습니다. 또한 Clip 파일 크기가 매우 작게 유지되므로, Liberation의 전체 기본 Clip Deck도 기가바이트가 아니라 몇 메가바이트에 불과합니다.
{% endhint %}

기본 scanner 설정은 다음과 같습니다.

* **Speed** scanner 속도입니다. 즉 레이저가 형태를 그리기 위해 얼마나 빠르게 움직이는지를 의미합니다. 기존 레이저 소프트웨어에서 point rate를 조정하는 것과 비슷하지만, Liberation에서는 point rate와 _독립적으로_ 레이저 이동 속도를 변경할 수 있습니다. 일반적으로 조정할 필요는 없습니다.
* **Scanner sync**(때로는 _blank shift_, 이전 명칭은 Colour Shift) scanners는 레이저를 매우 빠르게 움직이지만, 보통 밝기와 색상 변화가 움직임과 동기화되어 있지 않습니다. 이 경우 beams와 선의 가장자리에 작게 깜박이는 빛의 “꼬리”가 나타납니다. 이 조정값을 사용해 움직임과 색상이 서로 동기화되도록 맞춥니다. [Laser Settings](../setting-up/laser-settings/)를 참조하세요.

그 외의 고급 scanner 설정은 [고급](../advanced/) 장에서 다룹니다.

### Zoning

레이저 설정 및 zoning에 대한 전체 가이드는 다음을 참조하세요: [레이저 설정하기](../setting-up/setting-up-lasers.md)
