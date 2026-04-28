# ✅ Laser output 설정 패널

_Laser output_ 설정 패널은 _View -> Laser Output Settings._ 메뉴에서 엽니다.

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

현재 선택된 레이저의 설정이 표시되며, 선택할 레이저는 다음 방법으로 변경할 수 있습니다.

* _Laser overview_ 패널의 숫자 버튼 사용
* 키보드의 숫자 키 사용. 1부터 0까지의 키로 레이저 1 - 10을 엽니다.
* `Tab` 키로 레이저를 순서대로 전환합니다(`Shift + Tab`은 반대 방향).

이 패널 상단에는 다음 항목이 있습니다.

* 숫자 버튼 - 클릭하면 이 레이저를 arm/disarm합니다. 레이저가 armed 상태이면 빨간색으로 표시됩니다.
* 이 레이저에만 적용되는 _Brightness_ 슬라이더. 이 값은 global brightness와 함께 적용됩니다.
* _Test Pattern_ 토글 및 패턴 선택기. 이 레이저에만 사용할 특정 테스트 패턴을 선택할 수 있습니다. (이 컨트롤은 Output view 툴바에도 동일하게 표시됩니다.)

### 출력 방향 / 미러링 보정

다음 항목은 Liberation에서 일관되게 동작하도록 레이저 설정을 보정하는 데 사용합니다.

* **Flip horizontal / vertical** - 이 옵션으로 레이저 출력을 보정할 수 있습니다.

{% hint style="info" %}
레이저 배선이 잘못되었거나, 레이저 후면의 X/Y flip 버튼이 올바르게 설정되지 않은 경우가 아니라면 horizontal / vertical flip 설정을 변경할 필요가 없습니다. 특정 클립의 출력만 뒤집고 싶다면 클립 자체에서 설정할 수 있습니다.
{% endhint %}

* **Orientation** - 레이저가 옆으로 세워져 있거나 거꾸로 설치된 경우, 이 설정으로 회전을 보정할 수 있습니다.
* **Fine position adjustments** - 아주 작은 위치/회전 이동을 보정하는 데 사용할 수 있습니다. 레이저를 밤새 또는 장시간 켜 둔 뒤 발생하는 drift/settling을 보정하도록 설계되었습니다.

{% hint style="info" %}
orientation / mirroring 보정은 3D Visualiser의 내용을 변경하지 않습니다. 실제 레이저 출력이 3D Visualiser의 내용과 일치하도록 보정하는 데 사용해야 합니다.
{% endhint %}

### Copy laser settings

[#copy-laser-settings](./#copy-laser-settings)를 참고하세요.

### Scanner settings

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed 설정은 스캐너가 얼마나 빠르게 움직이는지 결정합니다.

{% hint style="danger" %}
기본 설정은 상당히 보수적이지만, 너무 빠르게 구동하면 스캐너가 손상될 수 있습니다. 특히 speed를 높일 때는 주의하세요.
{% endhint %}

{% hint style="info" %}
이 Speed 설정은 point rate를 변경하지 않습니다. 대신 포인트 사이의 간격을 조정합니다. 자세한 내용은 [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md)를 참고하세요.
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

스캐너가 빔을 움직이는 동안 빔의 색상이 바뀌고 켜지거나 꺼집니다. 이 두 동작은 보통 서로 완벽하게 동기화되어 있지 않습니다. 이 설정을 조정해 타이밍을 맞출 수 있습니다.

{% hint style="info" %}
이 설정은 _blank shift_라고도 불리지만, 개인적으로는 _scanner sync_라는 용어가 조금 더 정확하다고 생각합니다. 스캐너 움직임에 대한 모든 색상 변경의 타이밍을 조정하기 때문입니다.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>레이저 "꼬리" - Colour shift가 올바르게 설정되지 않음</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>레이저 "꼬리" 없음! Colour shift 양호!</p></figcaption></figure></div>

레이저 출력에 작은 "꼬리"가 보인다면 scanner sync 조정이 필요할 가능성이 높습니다. 무엇을 조정해도 꼬리가 계속 보인다면 스캐너/레이저 드라이버가 처리할 수 있는 것보다 빠르게 구동하고 있을 가능성이 큽니다. scanner speed를 낮춰 보세요.

#### Scanner presets

미리 설계된 스캐너 설정을 선택할 때 사용합니다. 기본 옵션으로도 대부분 문제없으므로, 스캐너가 특히 나쁘거나(또는 좋은) 경우가 아니라면 이 설정을 변경할 필요는 없습니다. 더 자세히 알고 싶다면 [scanner-presets.md](../../advanced/scanner-presets.md)를 참고하세요.

#### Colour calibration

이 시스템을 사용해 레이저의 밝기 곡선과 화이트 밸런스를 보정할 수 있습니다. [colour-calibration.md](../../advanced/colour-calibration.md)를 참고하세요.

#### Advanced settings

일반적으로 이 설정을 건드릴 필요는 없지만, 궁금하다면 [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md)를 참고하세요.
