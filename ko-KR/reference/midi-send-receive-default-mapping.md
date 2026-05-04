---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ MIDI 송수신 기본 매핑

**Clip의 켜기/끄기는 채널 1~14의 MIDI note on / off로 트리거됩니다**

Clip에는 가로(x) 및 세로(y) 위치가 있습니다. Clip을 오른쪽 클릭하면 해당 위치를 확인할 수 있습니다. MIDI는 0,0부터 Clip을 트리거할 수 있습니다.

{% hint style="info" %}
이 방식의 Clip 제어는 절대 위치를 사용하므로, Clip Deck을 스크롤해도 Clip 위치는 변경되지 않습니다.
{% endhint %}

MIDI 채널 1의 노트 1은 Clip 0,0이고, 노트 2는 Clip 0,1, 노트 3은 Clip 0,2입니다. 행 방향으로 아래로 내려가고 열 방향으로 이동합니다. 128에 도달하면 다음 채널로 이동해 다시 시작합니다. 따라서 MIDI로 접근할 수 있는 Clip은 총 128 x 14 = 1792개입니다.

Clip 좌표에 대한 MIDI 노트:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>노트 : 1</td><td>노트 : 6</td><td>노트 : 11</td><td>노트 : 16</td><td>노트 : 20</td></tr><tr><td><strong>y : 1</strong></td><td>노트 : 2</td><td>노트 : 7</td><td>노트 : 12</td><td>노트 : 17</td><td>...등</td></tr><tr><td><strong>y : 2</strong></td><td>노트 : 3</td><td>노트 : 8</td><td>노트 : 13</td><td>노트 : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>노트 : 4</td><td>노트 : 9</td><td>노트 : 14</td><td>노트 : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>노트 : 5</td><td>노트 : 10</td><td>노트 : 15</td><td>노트 : 20</td><td></td></tr></tbody></table>

MIDI note on 이벤트는 Clip을 시작하고, 이에 해당하는 note off 이벤트는 Clip을 중지합니다. 이는 Group의 trigger mode와 관계없이 적용됩니다. 이 시스템은 원래 재생 및 녹화를 위해 설계되었으므로, 노트로 Clip을 토글하는 방식은 적합하지 않았습니다.

### **효과**

**채널 15**의 MIDI control change(CC) 메시지는 효과를 조정합니다.\
Effect 1은 CC 0-3, 값 0-127을 사용합니다\
Effect 2는 CC 4-7, 값 0-127을 사용합니다\
Effect 3은 CC 8-11, 값 0-127을 사용합니다\
… 이런 식으로 계속됩니다.

각 4개 컨트롤 그룹은 해당 효과의 레벨과 3개 파라미터를 제어합니다.

<table><thead><tr><th width="164">Effect :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Level</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parameter 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...등</td></tr><tr><td><strong>Parameter 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parameter 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **전역 설정**

**채널 16**의 MIDI control change 메시지는 전역 설정을 변경합니다.\
CC 1 : Shift X(가로) 0-127, 64가 중앙\
CC 2 : Shift Y(세로) 0-127, 64가 중앙\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

그리고 중요한 항목입니다.\
CC 15 : Global brightness

이 시스템은 원래 녹화 및 재생을 위해 설계되었으며, Logic, Ableton 또는 기타 DAW를 사용해 타임라인 애니메이션을 만들 수 있도록 합니다. 라이브 제어에도 사용할 수는 있지만, 해당 용도로 최적화되어 있지는 않으며 APC40 setup과 비교하면 일부 라이브 제어 기능이 빠져 있습니다.
