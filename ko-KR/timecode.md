---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation은 외부 SMPTE/LTC timecode 신호와의 동기화를 지원합니다. 이 신호는 라이브 음악 공연에서 조명, 파이로, 비디오, 백킹 트랙의 타이밍을 맞추는 데 흔히 사용됩니다.

{% hint style="info" %}
SMPTE/LTC란?

SMPTE는 timecode 표준이고, LTC는 이 timecode를 오디오 신호로 변환한 것입니다. 이 오디오를 들어 보면 듣기 싫은 높은 피치의 삐걱거리는 소리처럼 들리지만, 컴퓨터에게는 고해상도 타이밍 정보입니다.

**전문가용 참고 정보!**

역사적으로 SMPTE는 비디오와 오디오를 동기화하는 데 사용되었습니다. 또는 아날로그 테이프와 동기화할 때는 한 트랙에 timecode 오디오를 녹음했는데, 이를 테이프를 "striping"한다고 부르기도 했습니다. 이 timecode 트랙을 사용해 여러 테이프 데크의 타이밍을 서로 맞추거나, MIDI 시퀀서를 테이프와 동기화할 수 있었습니다. (그래서 MIDI 악기를 테이프에 녹음할 필요 없이, 믹싱하는 동안 시퀀서가 라이브로 재생하게 할 수 있었습니다!)

SMPTE는 이 표준을 정의한 Society of Motion Picture and Television Engineers의 약자입니다. LTC는 _Linear TimeCode_의 약자입니다.
{% endhint %}

컴퓨터의 어떤 사운드 인터페이스로도 LTC timecode 신호를 받을 수 있지만, 최소 하나의 조정 가능한 XLR 입력과 모니터링 기능이 있는 전문 인터페이스를 사용하는 것을 권장합니다.

[M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html)는 헤드폰 모니터링, XLR 입력 2개를 제공하고 별도 드라이버가 필요 없어서(적어도 macOS에서는) 사용 경험이 좋았습니다. timecode 용도로만 사용할 예정이라면 조금 더 저렴한 [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html)를 사용할 수도 있습니다(입력이 하나뿐이고 MIDI는 없음). 하지만 솔직히 말해 어느 정도 품질이 괜찮은 사운드 인터페이스라면 대부분 작동할 것입니다.

{% hint style="info" %}
LTC timecode 신호는 일반적으로 밸런스드 XLR 케이블을 통해 분배됩니다. 낮은 레벨의 오디오 신호를 긴 거리로 안정적으로 전송하기에 충분히 견고하기 때문입니다. (XLR은 보통 마이크에 사용하는 배럴 잭 커넥터입니다.)
{% endhint %}

### 하드웨어 연결

timecode 신호 XLR 케이블을 사운드 인터페이스에 연결하고, 신호가 제대로 들어오는지 확인합니다. 레벨이 충분히 강하지만 클리핑되지 않도록 사운드 인터페이스의 레벨을 조정합니다. 사운드 인터페이스에 헤드폰 잭이 있다면 timecode를 들어 보고 글리치가 없고 노이즈가 너무 많지 않은지 확인할 수 있습니다.

{% hint style="info" %}
이론적으로는 MacBook의 잭 소켓을 통해 신호를 받을 수도 있지만, 이를 위해서는 커스텀 케이블이 필요합니다. 이 잭은 일반적으로 4극 TRRS 미니 잭이며, 솔직히 이 커넥터 중 어떤 핀을 오디오 입력으로 사용할 수 있는지 확실하지 않습니다. 또한 어떤 전압 레벨까지 허용되는지도 확실하지 않습니다(어딘가에서 +/-1V라고 읽은 적은 있지만, 사용은 본인 책임입니다!).

이 방법을 시도하기보다는 저렴한 USB 사운드 인터페이스를 구하는 편이 더 낫다고 생각합니다.
{% endhint %}

사운드 인터페이스에 입력 모니터링 기능이 전혀 없다면 macOS 시스템 설정의 _Sound_에서 신호가 들어오는지 확인할 수 있습니다. (Windows에서는 _Sound Control Panel_을 사용하세요.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS는 Sound 시스템 설정 패널에서 모든 사운드 인터페이스의 입력 레벨을 표시합니다.</p></figcaption></figure>

### Liberation에서 설정하기

1. Timecode settings Window에서 사운드 인터페이스와 올바른 입력 채널을 선택합니다.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
드롭다운 메뉴에는 사운드 인터페이스의 각 입력 채널에 대한 별도 옵션이 있습니다.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

왼쪽의 사각형을 확인하세요. 유효한 timecode 신호를 수신 중이면 녹색으로 표시됩니다. 그렇지 않으면 빨간색으로 표시됩니다.

2. 들어오는 timecode의 올바른 프레임레이트를 선택합니다. timecode를 제공하는 사람에게 프레임레이트가 무엇인지 물어보면 됩니다. (잘못 선택해도 동기화는 되지만, 매초마다 약간의 "skip"이 보일 것입니다.)
3. 타임라인 바의 작은 시계 아이콘을 사용해 Timeline의 timecode 설정을 열고, SMPTE(LTC) 옵션을 선택합니다.

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. 곡의 시작 지점에 맞게 start offset(시, 분, 초, 프레임)을 조정합니다. 여러 타임라인이 있는 경우 각 타임라인마다 이 옵션을 별도로 설정해야 합니다.

{% hint style="info" %}
투어 업계에서는 각 곡을 서로 다른 시간에서 시작하는 것이 일반적인 관례입니다. 예를 들어 첫 번째 곡은 01:00:00:00, 두 번째 곡은 02:00:00:00처럼 설정합니다.

Liberation은 timecode에 따라 자동으로 해당 타임라인으로 전환하므로, 공연 중에 타임라인을 수동으로 변경할 필요가 없습니다.
{% endhint %}

MIDI Clock 및 Ableton Link와 달리 SMPTE는 시, 분, 초, 프레임으로 측정되는 _절대_ 시간 시스템입니다. Liberation의 핵심 시간 시스템은 비트와 마디를 기반으로 하므로, timecode를 수신하면 타임라인에 설정된 템포를 사용합니다. 이 템포가 timecode에 동기화된 음악과도 맞는지 확인해야 합니다.
