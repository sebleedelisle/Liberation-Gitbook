---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 불러오기와 저장

Liberation은 상태를 디스크에 지속적으로 저장합니다. 따라서 정전이나 시스템 문제가 발생하더라도, 다시 시작하면 중단된 지점에서 바로 이어서 작업할 수 있습니다. zones, timeline 또는 기타 콘텐츠를 잃어버릴 일은 거의 없습니다.

다만 백업하거나 다른 컴퓨터로 옮기기 위해 현재 설정을 내보낼 수 있습니다.

### Project 가져오기/내보내기

Project 파일은 현재 설정의 거의 모든 내용을 저장합니다. 포함되는 항목은 다음과 같습니다.

* 아래 [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export)에 자세히 설명된 모든 항목
* Clips, effects 및 group settings
* 모든 timelines(오디오 및 비디오 미디어 제외)
* Artnet 설정
* MIDI 송신/수신 설정
* Tempo / 동기화 설정

현재 저장 및 불러오기가 지원되지 않는 항목은 다음과 같습니다.

* MIDI notes node 및 Sound Input Oscillator에서 사용하는 Sound 및 Midi 입력 설정(MIDI 송신/수신 설정과 timecode sound input은 저장됩니다)
* Interface scaling
* Canvas guide images용 미디어
* timelines용 Sound 및 Video 미디어
* Text node에서 사용하는 Fonts

{% hint style="danger" %}
timeline의 Sound 및 video 파일은 project 파일과 함께 저장되지 않습니다. 다른 컴퓨터로 옮기려면 반드시 별도로 저장하세요. [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files)를 참고하세요.
{% endhint %}

### Laser settings 가져오기/내보내기

* 모든 laser의 Laser settings
* Beam zones
* Canvas target areas
* DMX zones
* Laser controller assignment(이름을 변경한 controller의 aliases 포함)
* Laser scanner 및 colour calibration settings와 presets
* 3D visualiser settings와 presets

### Clip Deck 가져오기/내보내기

* 모든 clips와 해당 zone assignments, settings 및 parameters
* 모든 group settings, flash mode, fade in/out times 등

현재 저장 및 불러오기가 지원되지 않는 항목은 다음과 같습니다.

* 모든 effects와 해당 parameters 및 settings

{% hint style="info" %}
**전체 project를 불러오지 않고 project 파일에서 clips만 불러오기**

project에서 clips만 가져오려면 _**Clips->Import Clip Deck**_을 선택한 다음, clip deck 파일(.cpdk) 대신 project 파일을 선택하세요.
{% endhint %}

### Clip Deck 추가

_Append Clip Deck_을 사용하면 내보낸 clip deck 파일의 clips를 현재 project에 추가할 수 있습니다. Clips는 현재 clip deck의 끝에 추가되지만, 파일 안의 effects 및 group settings는 가져오지 않습니다.

### 선택한 Clips 내보내기

현재 선택된 clips가 파일로 내보내집니다. Group settings와 effects는 저장되지 않고 clips만 저장됩니다. 현재 실행 중인 active clips는 함께 선택되어 있지 않으면 내보내지지 않습니다.

{% hint style="info" %}
clips를 선택하려면 Option/Alt - shift - click을 사용하세요(또는 lasso를 사용). 선택된 clips는 두꺼운 흰색 외곽선으로 구분할 수 있습니다. [starting-stopping-clips.md](clips/starting-stopping-clips.md)를 참고하세요.
{% endhint %}

### Effects 가져오기/내보내기

모든 effects를 해당 group settings 및 parameters와 함께 불러오고 저장합니다.

{% hint style="info" %}
**전체 project를 불러오지 않고 project 파일에서 effects만 불러오기**

project에서 effects만 가져오려면 _**Effects->Import Effects**_를 선택한 다음, effects 파일(.efts) 대신 project 파일을 선택하세요.
{% endhint %}

### Timeline 내보내기

하나 이상의 timelines가 포함된 timeline 파일을 내보냅니다. 내보낸 timeline 파일에는 clipdeck이 항상 포함됩니다. 단, 다시 가져올 때 어떤 clips를 가져올지는 선택할 수 있습니다. 아래 [#timeline-import](loading-and-saving.md#timeline-import)를 참고하세요.

project 파일에 timeline이 둘 이상 있으면, 내보낼 timelines를 선택할 수 있는 패널이 열립니다.

{% hint style="danger" %}
timeline의 Sound 및 video 파일은 timeline 파일과 함께 저장되지 않습니다. 콘텐츠를 다른 컴퓨터로 옮기려면 반드시 별도로 저장하세요. [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files)를 참고하세요.
{% endhint %}

### Timeline 가져오기

하나의 timeline 파일에서 하나 이상의 timelines를 가져옵니다. timeline 파일을 선택하면 여러 가져오기 옵션이 있는 패널이 열립니다.

timeline 파일에 timeline이 둘 이상 있으면 모두 목록에 표시됩니다. 포함할 항목을 선택하세요.

* Replace existing timelines\
  현재 timelines를 모두 삭제하고 가져온 timelines로 대체합니다.
* Import used clips only\
  사용된 clips만 가져오며, 각 timeline마다 하나의 group이 되도록 clips를 groups로 정리합니다. 이 옵션을 선택하지 않으면 timeline 파일의 전체 clip deck이 기존 clips에 추가됩니다.
* Replace existing clip deck\
  현재 clip deck을 timeline 파일의 clips로 대체합니다. _Replace existing timelines_가 선택된 경우에만 사용할 수 있습니다.

{% hint style="info" %}
**전체 project를 불러오지 않고 project 파일에서 timelines만 불러오기**

project에서 timelines만 가져오려면 _**Timeline->Import Timeline(s)**_를 선택한 다음, timeline 파일(.ltml) 대신 project 파일을 선택하세요.
{% endhint %}

### DMX / Artnet 가져오기/내보내기

Artnet nodes와 해당 IP addresses를 저장하고 불러옵니다. DMX zones와 모든 DMX presets도 포함됩니다.

### timeline media files에 대한 중요 참고 사항

Sound 및 video 파일은 현재 timeline 파일과 함께 내보내지지 **않습니다**. 따라서 콘텐츠를 다른 컴퓨터로 옮겨야 한다면 해당 파일도 반드시 포함하세요.

{% hint style="info" %}
**timeline이 media files를 찾는 방식**

timeline이 로드되면 timeline(또는 project) 파일과 같은 폴더를 확인하고, 그 안과 모든 하위 폴더를 검색합니다. 따라서 파일이 같은 폴더 또는 하위 폴더(예: _/videos_ 또는 _/sound_)에 있으면 로드할 때 찾을 수 있습니다.
{% endhint %}
