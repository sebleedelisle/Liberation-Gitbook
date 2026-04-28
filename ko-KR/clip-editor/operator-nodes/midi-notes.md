---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

입력되는 MIDI 노트가 특정 범위 안에서 빔이나 도형을 트리거하는 “레이저 하프” 스타일 효과를 만듭니다. 이 노드는 전달된 콘텐츠를 각 노트의 _source_로 사용합니다. 점을 입력하면 점이 한 줄로 생성되고, 원 같은 도형을 입력하면 원이 한 줄로 생성됩니다. 더 복잡한 도형도 같은 방식으로 복제됩니다.

Liberation이 수신할 MIDI 인터페이스는 **Liberation → Settings** (`Cmd / Ctrl + ,`)에서 선택할 수 있습니다.

* **midi channel** – 수신할 MIDI 채널입니다(0 = 모든 채널, 1–16 = 특정 채널).
* **width** – 노트가 펼쳐질 전체 너비입니다.
* **midi note min / max** – 범위의 가장 낮은 MIDI 노트 값과 가장 높은 MIDI 노트 값입니다.
* **ignore out of range notes** – 설정된 범위를 벗어난 노트를 필터링합니다. 비활성화하면 범위를 벗어난 노트가 가장 가까운 사용 가능한 노트로 "클램프"됩니다(높은 노트는 범위의 맨 위를, 낮은 노트는 범위의 맨 아래를 트리거).
* **auto extend range** – 범위 밖의 노트가 연주되면 범위를 자동으로 넓힙니다.

{% hint style="info" %}
어떤 노트 범위가 들어오는지 잘 모르겠다면 **auto extend range**를 켜고, **midi note min**은 매우 높게, **midi note max**는 매우 낮게 설정한 뒤 노트를 연주해 보세요. 시스템이 모든 노트를 감지하고 범위를 자동으로 확장합니다. 필요한 노트를 모두 확인했다면 **auto extend range**를 끄면 범위가 고정됩니다.
{% endhint %}

* **leave all notes visible** – 노트가 연주 중인지와 관계없이 범위 안의 모든 노트에 대해 빔이나 도형을 생성하여 “레이저 하프” 효과를 만듭니다.
* **hit colour** – 노트가 트리거될 때 표시되는 색상입니다.
* **hit colour hold time** – 페이드되기 전에 hit colour가 최대 밝기로 유지되는 시간입니다. 값은 초 단위입니다(0–1). _100% = 1초._
* **hit colour decay time** – hold time 이후 hit colour가 다시 원래 상태로 페이드되는 데 걸리는 시간입니다. 값은 초 단위입니다(0–1). _100% = 1초._

{% hint style="info" %}
콘텐츠가 이미 순수한 흰색이라면 hit colour를 흰색으로 설정해도 차이가 없습니다. 가장 좋은 결과를 얻으려면 콘텐츠에는 채도가 높은 색을 사용하고 hit colour는 흰색으로 설정하세요. 노트가 트리거될 때 보기 좋은 플래시 효과가 만들어집니다.
{% endhint %}

* **note off fade out time** – 노트에서 손을 뗀 뒤 페이드되는 데 걸리는 시간입니다. 값은 초 단위입니다(0–1). _100% = 1초._
* **hit scale factor** – 노트가 트리거될 때 얼마나 커지는지 설정합니다(예: 2 = 두 배 크기).
* **hit scale hold time** – 다시 줄어들기 전에 노트가 확대된 상태로 유지되는 시간입니다. 값은 초 단위입니다(0–1). _100% = 1초._
* **hit scale decay time** – 노트가 원래 크기로 돌아가는 데 걸리는 시간입니다. 값은 초 단위입니다(0–1). _100% = 1초._
* **note off shrink time** – 노트에서 손을 뗀 뒤 원래 크기로 줄어드는 데 걸리는 시간입니다. 값은 초 단위입니다(0–1). _100% = 1초._ (**leave all notes visible**이 활성화되어 있으면 효과가 없습니다.)

{% hint style="info" %}
스케일링 - 콘텐츠가 단일 점이면 스케일링은 효과가 없습니다!
{% endhint %}
