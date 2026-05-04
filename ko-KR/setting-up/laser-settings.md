---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Laser output 설정 패널

메뉴 _View -> Laser Output Settings_ 에서 _Laser output_ 설정 패널을 엽니다.

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

현재 선택된 레이저의 설정이 표시되며, 다음 방법으로 변경할 수 있습니다.

* _Laser overview_ 패널의 번호 버튼 사용
* 키보드의 숫자 키 사용. 1~0 키로 레이저 1~10을 엽니다.
* `Tab` 키로 레이저를 순환 선택합니다(`Shift + Tab`은 역방향).

이 패널 상단에는 다음 항목이 있습니다.

* 번호 버튼 - 클릭하면 이 레이저를 arm/disarm합니다. 레이저가 armed 상태일 때 빨간색으로 표시됩니다.
* 이 레이저에만 적용되는 _Brightness_ 슬라이더. 이 값은 global brightness와 함께 적용됩니다.
* _Test Pattern_ 토글 및 패턴 선택기. 이 레이저에만 적용할 특정 테스트 패턴을 선택할 수 있습니다. (이 컨트롤은 Output view toolbar에도 동일하게 표시됩니다.)

### Output 방향 / 미러링 보정

다음 요소들은 레이저 설정을 보정하여 Liberation에서 일관되게 동작하도록 하기 위한 것입니다.

* **Flip horizontal / vertical** - 이 옵션으로 레이저 출력을 보정할 수 있습니다.

{% hint style="info" %}
레이저 배선이 잘못되었거나 뒷면의 X/Y flip 버튼이 올바르게 설정되어 있지 않은 경우가 아니라면 horizontal / vertical flip 설정을 변경할 필요가 없습니다. 특정 Clip의 출력만 뒤집고 싶다면 Clip 자체에서 설정할 수 있습니다.
{% endhint %}

* **Orientation** - 레이저가 옆으로 눕혀 설치되었거나 거꾸로 설치된 경우, 이 설정으로 회전을 보정할 수 있습니다.
* **Fine position adjustments** - 아주 작은 위치 이동/회전 보정에 사용할 수 있습니다. 레이저를 밤새 또는 장시간 켜 둔 뒤 발생하는 드리프트/안정화 오차를 보정하기 위한 기능입니다.

{% hint style="info" %}
orientation / mirroring 보정은 3D Visualiser의 내용을 변경하지 않습니다. 실제 레이저 출력이 3D Visualiser에 표시된 내용과 일치하도록 보정할 때 사용해야 합니다!
{% endhint %}

### Copy laser settings

[#copy-laser-settings](laser-settings.md#copy-laser-settings "mention")를 참조하세요.

### Scanner 설정

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed 설정은 스캐너가 움직이는 속도를 결정합니다.

{% hint style="danger" %}
기본 설정은 꽤 보수적이지만, 너무 빠르게 구동하면 스캐너가 손상될 수 있습니다. 특히 속도를 높일 때는 주의하세요.
{% endhint %}

{% hint style="info" %}
이 Speed 설정은 point rate를 변경하지 않습니다. 대신 포인트들이 얼마나 넓게 분포되는지를 조정합니다. 자세한 내용은 [◼️ Liberation이 레이저 콘텐츠를 생성하는 방식](../advanced/how-liberation-generates-laser-content.md "mention")를 참조하세요.
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

스캐너가 빔을 움직이는 동안 빔의 색상이 바뀌고 켜졌다 꺼집니다. 보통 이 두 동작은 서로 완벽하게 동기화되어 있지 않습니다. 이 설정을 조정해 두 타이밍을 다시 맞춥니다.

{% hint style="info" %}
이 기능은 때때로 _blank shift_ 라고도 부르지만, 개인적으로는 _scanner sync_ 라는 용어를 더 선호합니다. 스캐너 움직임에 대한 모든 색상 변화의 타이밍을 조정한다는 점에서 조금 더 정확한 표현입니다.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>레이저 “꼬리” - Colour shift가 올바르게 설정되지 않은 상태</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>레이저 “꼬리” 없음! Colour shift 양호!</p></figcaption></figure></div>

레이저 출력에 작은 “꼬리”가 보인다면 scanner sync 조정이 필요할 가능성이 높습니다. 어떻게 조정해도 꼬리가 계속 보인다면 스캐너/레이저 드라이버를 처리 가능한 속도보다 빠르게 구동하고 있을 가능성이 큽니다. scanner speed를 낮춰 보세요.

#### Scanner presets

미리 설계된 스캐너 설정을 선택할 때 사용합니다. 기본 옵션은 보통 충분하므로, 스캐너 성능이 특히 나쁘거나(또는 좋은) 경우가 아니라면 이 설정을 변경할 필요가 없습니다. 더 자세히 알아보려면 [◼️ 스캐너 프리셋 및 렌더 프로필](../advanced/scanner-presets.md "mention")를 참조하세요.

#### Colour calibration

이 시스템을 사용해 레이저의 밝기 커브와 화이트 밸런스를 보정할 수 있습니다. [색상 보정](../advanced/colour-calibration.md "mention")를 참조하세요.

#### Advanced settings

일반적으로 이 설정을 건드릴 필요는 없지만, 궁금하다면 [◼️ 고급 레이저 설정](../advanced/advanced-laser-settings.md "mention")를 참조하세요.
