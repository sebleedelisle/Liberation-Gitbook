---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardware

#### **Liberation은 Windows에서 실행되나요?**

예. Liberation은 **Windows 10 및 11(64-bit)**을 완전히 지원하며, Mac 버전과 동일한 기능을 제공합니다. 모든 릴리스는 두 플랫폼용으로 동시에 배포됩니다.

#### **Liberation은 Mac에서 실행되나요?**

예. Liberation은 **Mac(macOS 12 Monterey 이상)**을 완전히 지원하며, Windows 버전과 동일한 기능을 제공합니다. 모든 업데이트는 함께 배포됩니다.

#### **필요한 최소 사양은 무엇인가요?**

제어하려는 레이저 수에 따라 다릅니다. 몇 대의 레이저만 사용하는 경우에는 낮은 사양의 컴퓨터로도 충분합니다. Apple Silicon Mac은 모두 매우 잘 동작하며, 최대 100대의 레이저까지 제어할 수 있습니다. 중요한 현장에서 복잡한 쇼를 운영한다면 가능한 한 성능이 좋은 컴퓨터를 권장합니다.

#### **Liberation으로 몇 대의 레이저를 제어할 수 있나요?**

Liberation은 한 대의 컴퓨터에서 많은 레이저를 구동할 수 있습니다. 100대 이상의 레이저 컨트롤러로 테스트되었으므로, 실제 가능한 수는 다음 요소에 따라 달라집니다.

* 컴퓨터 CPU
* 네트워크 속도
* 구독 유형

#### **어떤 MIDI 컨트롤러를 사용할 수 있나요?**

Liberation은 널리 사용되는 APC40 Mk2 MIDI 컨트롤러를 기준으로 설계 및 최적화되었습니다. APC40 Mk1도 지원합니다. [APC40으로 라이브 제어](midi-control/live-control-with-the-apc40.md)를 참조하세요.

지원 MIDI 컨트롤러는 점진적으로 추가하고 있으며, 현재 APC Mini Mk2와 MIDI Fighter Twister도 지원합니다.

추가 MIDI 제어를 제공하는 MIDI Send/Receive 시스템도 있습니다. [MIDI Send/Receive](midi-control/midi-send-receive.md)를 참조하세요.

자세한 내용은 [midi-control](midi-control/)을 참조하세요.

#### **아무 MIDI 컨트롤러나 사용할 수 있나요?**

현재는 앞으로 이를 가능하게 할 구성 가능한 MIDI 시스템을 개발 중입니다. 그동안 일부 사용자는 MIDI Send/Receive 시스템용으로 임의의 MIDI 메시지를 변환할 수 있는 MIDI 인터프리터를 사용해 성공한 사례가 있습니다. 하지만 이는 번거롭고 고급 사용자에게 적합한 작업입니다. 이 설정에 대한 조언은 [forum](https://forum.liberationlaser.com)에서 검색해 보세요. 현실적으로는 APC40이 가장 좋은 선택입니다.

## Laser controllers

#### **Liberation과 호환되는 레이저 컨트롤러는 무엇인가요?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (펌웨어 업데이트가 필요할 수 있음)
* LaserCube USB(및 LaserDock)
* LaserCube network protocol(유선 연결 사용)
* [LASollinger lasers](https://laseranimation.com/en/)에서 사용하는 AVB(현재 macOS에서만 테스트 중)

자세한 내용은 [호환되는 레이저와 컨트롤러(DAC)](hardware/compatible-lasers-and-controllers-dacs.md)를 참조하세요.

#### **왜 \[다른 브랜드의] 레이저 컨트롤러는 지원하지 않나요?**

소프트웨어와 하드웨어 간의 더 나은 상호 운용성을 장려하기 위해, Liberation은 공개된 통신 프로토콜이 있는 DAC만 지원합니다. 이것이 레이저 업계가 나아가야 할 가장 좋은 방향이라고 생각합니다.

#### **내 레이저를 Liberation과 함께 사용할 수 있는지 어떻게 알 수 있나요?**

레이저에 다음 중 하나가 있다면 Liberation과 함께 사용할 수 있습니다.

* 외부 **ILDA input** – 호환되는 외부 컨트롤러와 함께 사용하는 25핀 D 커넥터.
* 내부에 설치된 **Ether Dream**.
* 모든 **LaserCube**(USB 및 Wi-Fi LaserCube 모두 지원).
* **Mercury 시스템이 내장된 X-Laser 장비**(Ether Dream 모드).
* **AVB가 내장된 LaserAnimation Sollinger 프로젝터**(macOS 전용, AVB 호환 네트워크 장치 필요, 현재 테스트 중).

자세한 내용은 [호환되는 레이저와 컨트롤러(DAC)](hardware/compatible-lasers-and-controllers-dacs.md)를 참조하세요.

#### **Liberation을 LaserCube와 함께 사용할 수 있나요?**

예. Liberation은 모든 LaserCube와 직접 동작합니다. [LaserCube](hardware/lasercube.md)를 참조하세요.

## Licences

#### **라이선스 가격은 얼마인가요?**

현재 가격은 [shop](https://liberationlaser.com/shop) 페이지를 참조하세요.

#### **라이선스 등급별 제한 사항은 무엇인가요?**

현재 라이선스 옵션은 [shop](https://liberationlaser.com/shop) 페이지를 참조하세요.

무료 등급을 포함한 **모든** 등급에서 원하는 수만큼 레이저를 설정하고, 미리 보고, 쇼를 디자인할 수 있습니다. _arm_할 수 있는 레이저 수를 제외하면 다른 제한은 전혀 없습니다. 그 밖의 모든 Liberation 기능은 모두에게 제공됩니다.

#### **새 등급으로 업그레이드할 수 있나요?**

언제든지 더 높은 등급으로 업그레이드할 수 있습니다. 현재 라이선스의 남은 기간에 대한 일부 환불을 받게 되며, 새 플랜은 즉시 시작됩니다. [라이선스 업그레이드 / 다운그레이드](installation/upgrade-downgrade-your-license.md)를 참조하세요.

#### **라이선스를 다운그레이드할 수 있나요?**

언제든지 다운그레이드할 수 있지만, 변경 사항은 현재 라이선스 기간이 끝난 후 적용됩니다. [라이선스 업그레이드 / 다운그레이드](installation/upgrade-downgrade-your-license.md)를 참조하세요.

#### **내 라이선스로 컴퓨터를 어떻게 인증하나요?**

라이선스를 구매한 후에는 Liberation 소프트웨어 안에서 컴퓨터를 인증할 수 있습니다. _About_ 화면에 _Authorise_ 버튼이 표시되며, 이 버튼을 누르면 웹사이트에 로그인하라는 메시지가 나타납니다. 화면의 안내에 따라 인증 절차를 완료하세요. [인증 및 인증 해제](installation/authorising-and-de-authorising.md)를 참조하세요.

#### **컴퓨터를 인터넷에 얼마나 자주 연결해야 하나요?**

라이선스가 갱신될 때마다 Liberation을 인터넷에 연결해 내부 라이선스를 업데이트해야 합니다. 월간 반복 결제의 경우 매월 연결해야 합니다.

#### **갱신 후 컴퓨터를 인터넷에 연결할 수 없으면 어떻게 되나요?**

Liberation은 라이선스 갱신 후 7일의 유예 기간을 제공하며, 이 기간 안에 인터넷에 연결해 내부 라이선스를 업데이트할 수 있습니다. 이 기간이 지나면 Liberation은 _Free_ 모드로 돌아갑니다.

#### **신용카드가 만료되면 어떻게 되나요?**

결제 제공업체에서 이메일 알림을 받게 되며, 결제 정보를 업데이트해야 합니다. 웹사이트에 로그인한 뒤 구독 페이지에서 _Update payment details_ 링크를 사용하세요.

#### **반복 라이선스는 어떻게 취소하나요?**

웹사이트에 로그인하고 _Your subscriptions_ 페이지를 연 다음, 취소할 구독을 선택하고 _Cancel Subscription_ 링크를 클릭하세요. 라이선스 기간이 끝날 때까지는 Liberation을 계속 사용할 수 있습니다.

#### **Liberation을 몇 대의 컴퓨터에 설치할 수 있나요?**

Liberation은 원하는 수만큼 컴퓨터에 설치할 수 있습니다. 라이선스 인증은 레이저 / DMX 출력을 활성화할 때만 필요하며, 라이선스 등급에 따라 동시에 출력용으로 인증할 수 있는 컴퓨터 수가 결정됩니다. [라이선스 작동 방식](installation/how-licensing-works.md)를 참조하세요.

#### **라이선스를 한 컴퓨터에서 다른 컴퓨터로 어떻게 옮기나요?**

* 더 이상 사용하지 않을 컴퓨터에서 Liberation을 엽니다.
* 인터넷에 연결되어 있는지 확인한 뒤 _About_ 화면에서 _De-authorise this computer_ 버튼을 클릭합니다.
* 이제 새 컴퓨터에서 Liberation을 엽니다.
* _About_ 화면에서 _Authorise this computer_ 버튼을 클릭합니다.
* 웹사이트가 열리면 로그인하고 화면의 안내에 따라 인증을 완료합니다.

더 이상 접근할 수 없는 컴퓨터도 원격으로 인증 해제할 수 있습니다(일부 제한 있음). [인증 및 인증 해제](installation/authorising-and-de-authorising.md)를 참조하세요.

#### **분실되거나 도난당한 컴퓨터에서 Liberation 인증을 해제할 수 있나요?**

웹사이트를 통해 해당 컴퓨터의 인증을 해제할 수 있습니다. 마지막 갱신 이후 해당 Liberation 설치가 온라인 상태가 된 적이 없다면 즉시 처리할 수 있습니다.

그렇지 않은 경우, 구독이 갱신되거나 해당 컴퓨터가 인터넷에 연결될 때 중 먼저 발생하는 시점에 인증 해제가 적용됩니다. 새 컴퓨터를 긴급하게 다시 인증해야 한다면 지원팀에 문의하세요.

### Using Liberation

#### 기본 설정에는 레이저가 8대 있습니다. 이것을 어떻게 변경하나요?

[프로젝트 설정하기](setting-up/setting-up-your-project.md) 및 [레이저 추가 / 제거](setting-up/adding-removing-lasers.md)를 참조하세요.

#### 한 레이저의 zone 설정을 다른 레이저로 복사할 수 있나요?

예! [레이저 간 존 복사](output-view/copy-zones-between-lasers.md)를 참조하세요.

#### 슬라이더 대신 숫자를 입력할 수 있나요?

예. 슬라이더를 `Cmd / Ctrl`-클릭하면 키보드로 값을 입력할 수 있습니다.

#### **Liberation을 음악과 어떻게 동기화하나요?**

기대하는 방식으로 동작하는 지능형 "tap tempo" 시스템이 있으며, 외부 MIDI clock 또는 Ableton Link도 사용할 수 있습니다. [Tempo / 동기화](tempo-synchronisation.md)를 참조하세요. 타임라인은 오디오 인터페이스를 통해 들어오는 LTC/SMPTE timecode에 동기화할 수 있습니다. [Timecode](timecode.md)를 참조하세요.

#### 레이저에서 최상의 출력을 얻으려면 어떤 설정을 조정해야 하나요?

주요 설정은 _Colour Shift_입니다. 이 설정은 미러가 움직이는 시점과 레이저 밝기가 변하는 시점 사이의 작은 지연을 보정합니다. 레이저 점/빔에 작은 '꼬리'가 보인다면 이 값을 조정해야 합니다. ('꼬리'의 예시는 [Laser output 설정 패널](setting-up/laser-settings.md) 페이지의 사진을 참조하세요.)

스캐너 속도도 변경해 볼 수 있습니다. 스캐너가 기본형이면 더 느리게, 성능이 좋으면 더 빠르게 설정할 수 있습니다. 하지만 **너무 강하게 구동하면 스캐너가 손상될 수 있으므로 주의해서 사용하세요.**

몇 가지 사전 설정된 스캐너 설정도 있습니다. 기본 옵션은 보수적인 설정이며 대부분의 레이저 빔 요구 사항에 적합합니다. 더 좋은 스캐너를 사용하는 경우를 위한 다른 프리셋도 있고, 그래픽에 맞게 조정된 프리셋도 있습니다.

자세한 내용은 [Laser output 설정 패널](setting-up/laser-settings.md)를 참조하세요. 직접 프리셋을 만드는 방법은 [◼️ 스캐너 프리셋 및 렌더 프로필](advanced/scanner-presets.md)를 참조하세요(고급, 작성 중).

_Colour calibration_ 설정을 사용해 색상 밸런스도 보정할 수 있습니다. [색상 보정](advanced/colour-calibration.md)를 참조하세요(고급 기법).

#### _Latency(ms)_ 설정은 무엇을 하나요?

이는 프레임 지연 시간, 즉 프레임이 생성된 뒤 레이저로 전송될 때까지의 최대 시간입니다. 일반적으로 조정할 필요는 없지만, 네트워크 문제가 있다면 값을 높여 볼 수 있습니다. 자세한 내용은 [지연 시간 설정](setting-up/latency-setting.md)를 참조하세요.

### Clips

#### Clip을 실행하지 않고 zone과 설정을 조정하려면 어떻게 하나요?

Clip을 활성화하지 않고 _현재 선택된 Clip_으로 만들려면 `Alt / Option`-클릭하세요. [Clip 시작 / 중지](clips/starting-stopping-clips.md)도 참조하세요.

#### Clip을 어떻게 복사하나요?

`Alt / Option` 키를 누른 상태에서 클릭하고 드래그하세요. [Clip Deck 구성하기](clips/organising-your-clip-deck.md)도 참조하세요.

#### Clip을 어떻게 삭제하나요?

Clip Deck 밖으로 클릭해서 드래그하세요. [Clip Deck 구성하기](clips/organising-your-clip-deck.md)도 참조하세요.

#### 여러 개를 선택하거나, 삭제하거나, Clip Deck을 결합하는 등의 작업은 어떻게 하나요?

[Clip Deck 구성하기](clips/organising-your-clip-deck.md)를 참조하세요.

#### Clip에 있는 작은 마이크 기호와 기타 아이콘은 무엇을 의미하나요?

해당 Clip이 사운드 또는 MIDI 입력을 받는다는 것을 표시합니다. 또한 3개의 점은 zone delay가 있음을 나타냅니다. [클립 버튼의 작은 아이콘은 무엇인가요?](clips/what-are-the-small-icons-on-the-clip-buttons.md)를 참조하세요.
