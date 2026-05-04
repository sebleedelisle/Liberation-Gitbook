---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/starting-stopping-clips
---

# ✅ Clip 시작 / 중지

{% hint style="info" %}
화면상의 버튼으로 Clip을 시작하고 중지할 수 있지만, APC40 MIDI 컨트롤러를 사용하는 것이 훨씬 좋습니다. Liberation은 이 하드웨어와 잘 작동하도록 최적화되어 있으며, 레이저 운용 환경에서 중요한 장비로 고려하는 것이 좋습니다.
{% endhint %}

### Clip 시작 및 중지

Clip을 시작하려면 해당 Clip의 버튼을 누르세요(화면에서 누르거나 MIDI 컨트롤러에서 누를 수 있습니다).

Clip을 중지하려면 같은 버튼을 다시 누르세요.

새 Clip을 시작하면(같은 group 안에서) 먼저 실행 중이던 Clip은 자동으로 중지됩니다.

다른 Clip을 중지하지 않고 새 Clip을 시작하려면 다음 중 하나를 사용하세요.

* 새 Clip을 시작하는 동안 `Shift` 키(또는 APC40 Shift 버튼)를 누릅니다. 또는
* 새 Clip을 시작하는 동안 현재 실행 중인 Clip을 다시 누릅니다.

Clip group들은 서로 독립적이므로, 한 group에서 Clip을 시작해도 다른 group의 Clip에는 영향을 주지 않습니다. [Clip 그룹](groups.md "mention")를 참고하세요.

### Flash mode

Clip이 _flash mode_로 설정된 group 안에 있으면 약간 다르게 동작합니다. Clip 버튼을 누르고 있는 동안에만 Clip이 계속 실행됩니다. 버튼에서 손을 떼는 즉시 중지됩니다. (기본적으로 Clip group 3, 즉 빨간색 group은 _flash mode_로 설정되어 있습니다.)

### 모든 Clip 중지

**실행 중인 모든 Clip을 중지**하려면 **STOP** 버튼을 누르세요.

{% hint style="info" %}
Clip의 fade out 시간을 건너뛰고 즉시 blackout하려면 **STOP** 버튼을 **두 번** 누르세요.
{% endhint %}

특정 group에서 실행 중인 모든 Clip을 중지하려면 해당 group 버튼을 누른 다음 **STOP** 버튼을 누르세요.

하나의 Clip만 남기고 모든 Clip을 중지하려면 유지하려는 실행 중인 Clip을 누른 상태에서 **STOP** 버튼도 함께 누르세요. 그런 다음 Clip 버튼에서 손을 떼세요. (여러 Clip에서도 작동합니다. 한 번에 누르고 있을 수 있는 만큼 가능합니다!)

### 현재 선택된 Clip

<figure><img src="../.gitbook/assets/clips-selected-active.png" alt="" width="269"><figcaption><p>현재 실행 중인 두 개의 Clip입니다. 흰색 외곽선은 오른쪽 Clip이 <em>현재 선택된 Clip</em>임을 나타냅니다.</p></figcaption></figure>

Clip이 현재 실행 중이면 화면에서 밝게 표시됩니다(그리고 mini clip visualiser 표시가 깜박입니다). 또한 마지막으로 누른 Clip 주위에 흰색 외곽선이 표시되는 것도 볼 수 있습니다. 이는 해당 Clip이 _현재 선택된 Clip_임을 나타냅니다.

Clip을 활성화하지 않고 선택하려면 Clip을 `Alt / Option`-클릭하세요. 여러 Clip을 선택하려면 `Alt / Option + Shift`-클릭을 사용하세요.

Clip Deck에서 lasso를 클릭하고 드래그하여 여러 Clip을 선택할 수도 있습니다.

{% hint style="info" %}
APC40에도 선택을 위한 `Alt` 및 `Shift` 버튼이 있습니다.
{% endhint %}
