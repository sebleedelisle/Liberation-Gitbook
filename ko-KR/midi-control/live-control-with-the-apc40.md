---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 라이브 MIDI 컨트롤러

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

APC40은 Liberation의 기본 하드웨어 컨트롤러입니다. 적극 권장되는 장비이며, Liberation은 처음부터 이 하드웨어를 중심으로 설계되었다고 해도 무리가 없습니다. APC40을 연결하면 Liberation이 즉시 자동으로 연결합니다.

{% hint style="warning" %}
_이런! 공연 중간에 USB 플러그가 빠졌어요!_

당황하지 마세요. 다시 연결하기만 하면 됩니다. Liberation이 자동으로 다시 연결하므로 문제없습니다.
{% endhint %}

### APC40 Mark 1 또는 Mark 2?

간단히 말해, Mark 2를 권장합니다. 풀컬러 버튼을 지원해 Liberation clip deck 인터페이스와 더 잘 맞기 때문입니다. Mark 1 버전도 급할 때 사용할 수는 있지만, 화면에 표시되는 레이아웃과 약간 다르고 버튼 색상이 빨강, 주황, 초록으로만 표시되어 clip 색상과 일치하지 않기 때문에 조금 더 혼란스러울 수 있습니다.

{% hint style="info" %}
오리지널 APC40 Mark 1은 2009년에 출시되었으며(!), 금속 바디 구조와 튼튼한 콘솔형 폼팩터 때문에 여전히 선호하는 사용자도 있습니다. 업데이트된 Mark 2는 2014년에 출시되었고 2024년에 단종되었지만, 비주얼 아티스트(Resolume 등)와 레이저 아티스트의 수요로 인해 2025년에 다시 생산될 예정입니다.
{% endhint %}

APC40에서 사용할 수 있는 전체 컨트롤 목록은 [APC40 레퍼런스](../reference/apc40-reference.md "mention")를 참조하세요.

### APC Mini

Liberation 1.0.3에는 APC Mini 프로파일도 포함되어 있습니다. 이 프로파일은 8x5 Clip 그리드, zone 버튼, zone X/Y 반전 컨트롤, 그룹 버튼, 모든 Clip 정지, Clip 페이지 이동, zone 페이지 이동, 탭 템포, 마디 리셋, 템포 너지에 매핑되어 있습니다. 페이더는 이펙트 레벨을 제어하고, Shift 상태의 페이더는 이펙트 파라미터를 제어합니다. 마지막 페이더는 Global Brightness를 제어합니다.

### MIDI Fighter Twister

MIDI Fighter Twister 프로파일은 Clip 실행보다 인코더 중심의 제어에 맞춰져 있습니다. 인코더 한 줄은 이펙트 슬롯 1~8의 파라미터 1을 제어하고, 다른 한 줄은 Clip shift, zone delay, global spin/scale, 그룹 페이드 등을 포함한 Parameters panel의 8개 상황별 컨트롤을 따릅니다.
