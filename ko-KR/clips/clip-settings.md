---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Clip settings

### Clip settings 패널

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Clip settings 패널</p></figcaption></figure>

_Scale X_ 및 _Scale Y_를 사용해 Clip의 출력 크기를 변경합니다. _SHIFT_ 키를 누르지 않는 한 두 값은 함께 잠겨 있습니다.

_Shift X_ 및 _Shift Y_를 사용해 Clip의 가로 및 세로 위치를 변경합니다.

_Zone Delay/Chase_는 별도 섹션이 필요할 만큼 재미있는 기능입니다. [Zone delay / chase](zone-delay-chase.md)

### Clip 잠금

Clip이 잠겨 있으면 이동하거나 삭제할 수 없습니다. Clip을 잠그려면 오른쪽 클릭 메뉴의 _Locked_ 체크박스를 사용합니다. Clip settings 패널에서는 몇 가지 추가 옵션을 사용할 수 있습니다.

* _UNLOCK ALL -_ Clip Deck의 모든 Clip 잠금을 해제합니다.
* _AUTO-LOCK_ - _Auto-Lock_이 켜져 있으면 자동으로 재생되는 Clip(타임라인 또는 MIDI 녹음/재생 시스템으로 재생되는 Clip)이 잠깁니다. Logic Pro(또는 유사한 프로그램)에서 쇼를 프로그래밍했고, 쇼에 사용되는 Clip을 실수로 편집하고 싶지 않을 때 유용합니다.
* _LOCKED CLIPS ZONES_ - 이 옵션이 켜져 있으면 잠긴 Clip의 존을 변경할 수 없습니다.
* _LOCKED CLIPS PARAMS_ - 이 옵션이 켜져 있으면 잠긴 Clip의 파라미터(스케일, 시프트 등)를 변경할 수 없습니다.

### 오른쪽 클릭 메뉴

Clip을 오른쪽 클릭하면 해당 Clip에 대한 몇 가지 옵션이 포함된 메뉴가 나타납니다. 이 메뉴의 처음 몇 항목에 대한 자세한 내용은 [Clip Editor 소개](../clip-editor/clip-editor-intro.md), [Clip settings](clip-settings.md) 및 [Clip 그룹](groups.md)를 참고하세요.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Clip settings 오른쪽 클릭 메뉴</p></figcaption></figure>

### Retrigger

기본적으로 Clip은 _retrigger_로 설정되어 있습니다. 즉, 언제 누르든 Clip은 그 순간부터 실행을 시작합니다. 따라서 늦게 시작하면 Clip의 애니메이션도 약간 늦어져 타이밍이 어긋납니다.

{% hint style="info" %}
Retrigger된 Clip이 실행 중일 때 _Tap Tempo_를 하면, 비트에 정확히 맞춰 시작하지 않았더라도 시스템이 Clip을 타이밍에 맞도록 “퀀타이즈”합니다.
{% endhint %}

_Retrigger_가 활성화되어 있지 않으면 Clip은 항상 타이밍에 맞습니다. 마치 Clock의 맨 처음부터 Clip이 시작된 것처럼 동작합니다. 외부 Clock 신호를 통해 음악과 완벽하게 동기화되어 있을 때 적합합니다.

{% hint style="info" %}
Clip은 보통 계속 반복되도록 설계하지만, 한 번만 실행되거나 몇 번만 반복되도록 만들 수도 있습니다. 이런 Clip은 반드시 _retrigger_로 설정해 두세요. 그렇지 않으면 다시 시작되지 않습니다!
{% endhint %}

### 전환 인/아웃 시간(페이드)

Clip은 초 단위로 지정한 시간 동안 페이드 인/아웃되도록 설정할 수 있습니다. 기본적으로 페이드 시간은 해당 그룹 설정을 상속합니다(그룹 버튼을 오른쪽 클릭하여 변경할 수 있음).

Clip의 그룹과 다른 페이드 시간을 사용하려면 먼저 _USE GROUP DEFAULT_ 버튼을 끈 다음, Clip의 _In time_ 및 _Out time_ 슬라이더를 조정합니다.
