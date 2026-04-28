---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Clip Editor 소개

Clip Editor는 레이저 콘텐츠를 만드는 다재다능한 방법이며 Liberation의 핵심입니다. 간단한 콘텐츠는 쉽게 만들 수 있고, 동시에 매우 정교하고 복잡한 효과를 만들 수 있을 만큼 유연합니다.

{% hint style="info" %}
노드 기반 에디터는 Liberation에서 가장 먼저 만들어진 부분입니다! 2018년 영국 레이저 모임에서 Rob Stanley와 “객체 지향” 레이저 콘텐츠 디자이너는 어떤 모습일지 이야기하던 중 탄생했습니다.

겉보기에는 단순해 보이지만 실제로는 구축하기 꽤 복잡한 시스템입니다. 그래도 2019년 초에는 개념을 증명하는 작동 데모를 만들었고, 그것이 이 여정의 시작이 되었습니다!
{% endhint %}

Clip Editor는 노드 기반 비주얼 에디터(또는 [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph))입니다. TouchDesigner, MaxMSP, VVVV 같은 제품을 사용해 본 적이 있다면 익숙할 것입니다. 다만 Clip Editor는 벡터 그래픽에 맞게 특별히 설계되었기 때문에 약간 다르고 조금 더 단순합니다.

Clip 버튼을 마우스 오른쪽 버튼으로 클릭하고 _EDIT CLIP_ 을 선택하면 Clip Editor를 열 수 있습니다. 또는 비어 있는 Clip 버튼을 마우스 오른쪽 버튼으로 클릭하고 _CREATE AND EDIT CLIP_ 을 선택합니다.

### 개요

Clip Editor에서 볼 수 있는 항목은 다음과 같습니다.

* 상단의 **Creator** 및 **Operator node buttons**
* 왼쪽의 **Oscillator node buttons**
* 오른쪽 패널의 콘텐츠 미리보기. 노드를 클릭하면 해당 노드 자체의 콘텐츠를 보여 주는 두 번째 미리보기도 표시됩니다.
* 편집 중인 Clip의 모든 노드와 연결(새 Clip인 경우 비어 있습니다)
* 다양한 옵션이 있는 Clip Editor 패널

편집하는 동안에는 배경의 3D visualiser에서도 Clip이 어떻게 보이는지 확인할 수 있습니다.

{% hint style="info" %}
3D visualiser에 출력이 보이지 않는다면 zone 버튼을 사용해 원하는 zone을 켜야 할 수 있습니다. 또한 _Preview to lasers_ 가 활성화되어 있는지도 확인해야 합니다. 아래 [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel)을 참고하세요.
{% endhint %}

### Clip 만들기

일반적으로 하나 이상의 [creator nodes](creator-nodes.md)로 시작한 다음, 콘텐츠를 처리하는 [operators](operator-nodes/)를 왼쪽에서 오른쪽으로 연결합니다. Creator 및/또는 Operator를 서로 가까이 이동하면 자동으로 연결되는 것을 볼 수 있습니다. 다시 서로 멀리 드래그하면 연결을 해제할 수 있습니다.

### Clip에 노드 추가하기

상단 또는 왼쪽의 노드 버튼 중 하나를 클릭한 뒤 Clip Editor 안의 빈 공간으로 드래그합니다.

### 노드 설정 조정하기

노드의 속성 패널을 열려면 톱니바퀴 아이콘 버튼(노드 오른쪽 위)을 클릭합니다.

### 노드 활성화 및 비활성화하기

노드를 활성화하거나 비활성화하려면 전원 아이콘 버튼(노드 왼쪽 위)을 클릭합니다. 노드가 현재 활성 상태가 아님을 나타내기 위해 흐리게 표시됩니다. Operator가 비활성화되어 있어도 콘텐츠는 계속 통과하지만, 해당 노드는 콘텐츠에 영향을 주지 않습니다.

### 노드 연결하기

콘텐츠는 Creator 노드로 만들어지고, 왼쪽에서 오른쪽으로 노드를 따라 전달됩니다. 각 Operator는 어떤 방식으로든 콘텐츠에 영향을 준 다음 다음 Operator로 전달합니다. 경로 끝에 남는 결과가 Clip의 콘텐츠입니다. Creator와 Operator는 서로 가까이 이동하면 자동으로 연결됩니다. 분리하려면 다시 서로 멀리 드래그합니다.

{% hint style="info" %}
하나 이상의 노드를 다음 노드의 입력에 연결할 수 있습니다. 여러 콘텐츠 조각을 결합할 때 유용합니다.
{% endhint %}

### 노드 속성과 소켓

각 노드의 하단에는 소켓 배열이 있으며, 각 소켓은 brightness, position, scale, rotation 등 노드 내부의 속성을 나타냅니다.

[Oscillator nodes](oscillators/)는 아래쪽에서 이 소켓에 연결할 수 있으며, 이러한 설정에 애니메이션을 적용하는 데 사용됩니다. Oscillator 노드는 상단에 출력이 있습니다. 클릭한 뒤 드래그하여 연결을 꺼내 다른 노드의 속성 소켓 중 하나에 놓습니다.

### Oscillator 노드

Oscillator 노드는 시간에 따라 속성을 변경하는 데 사용됩니다. 일반적으로 톱니파나 사인파 같은 파형을 나타내지만, 일부 Oscillator 노드는 마이크 입력 레벨 같은 외부 입력을 소스로 사용합니다.

{% hint style="info" %}
아날로그 신디사이저를 사용해 본 적이 있다면 Oscillator 개념이 익숙할 것입니다. Oscillator는 일반적으로 파형을 만들거나 시간에 따라 사운드를 조정하는 데 사용됩니다. Liberation의 Oscillator도 비슷한 역할을 합니다.

**재미있는 사실:** _Liberation_ 이라는 이름은 1980년에 출시된 신디사이저 “키타”인 Moog Liberation에서 영감을 받았습니다. 이 악기는 Herbie Hancock, Jean-Michel Jarre, 심지어 James Brown을 통해 유명해졌습니다!
{% endhint %}

Oscillator에는 조정할 속성의 최소값과 최대값을 제어하는 _range_ 설정이 항상 있습니다. 또한 _Wave Oscillators_ 에는 Oscillator가 값을 얼마나 빠르게 변경할지 결정하는 _duration_ 설정이 항상 있습니다. 자세한 내용은 [wave-oscillators.md](oscillators/wave-oscillators.md)를 참고하세요.

### Clip Editor 패널

* Timer - 패널 상단에서 Clip이 진행되는 현재 시간을 볼 수 있습니다.
* _RETRIGGER_ - Clip을 처음부터 다시 시작합니다. Clip이 반복되지 않을 때 특히 유용합니다.
* _Preview to lasers_ - 이 항목을 선택하면 이 Clip을 편집하는 동안 3D visualiser가 업데이트되는 것을 볼 수 있습니다. 끄면 에디터 밖에서 실행 중인 Clip들이 표시됩니다. 이 설정은 Clip별 설정이 아니라 전역 설정입니다.
* _UNDO/REDO_ - Clip Editor 자체에 대한 실행 취소/다시 실행입니다. `Cmd / Ctrl + Z` 및 `Cmd / Ctrl + Shift + Z`에도 매핑되어 있습니다.
* _SAVE CLIP_ - 편집 내용을 저장하지만 덮어쓰기에 대한 경고를 표시합니다.
* _SAVE AS A COPY_ - Clip을 Clip Deck에서 다음 사용 가능한 슬롯에 저장합니다. 이 위치가 Clip의 새 위치가 되며, 이후의 모든 저장은 이 새 위치에 저장됩니다.
* _EXIT EDITOR_ - Clip Editor를 닫습니다. 저장하지 않은 변경 사항이 있으면 확인 패널이 표시됩니다.
