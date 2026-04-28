---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ 호환되는 레이저와 컨트롤러(DAC)

### Liberation과 호환되는 레이저는 무엇인가요?

레이저에 표준 ILDA 입력이 있다면, Ether Dream 또는 Helios DAC 같은 호환 레이저 컨트롤러와 함께 Liberation에서 사용할 수 있습니다([전체 목록은 아래 참고](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - 가정용으로 가장 저렴한 옵션</p></figcaption></figure>

다음에 해당하는 경우에는 외부 컨트롤러나 ILDA 입력이 필요하지 않습니다.

* 레이저 내부에 Ether Dream이 설치되어 있는 경우, 또는;
* Wicked Lasers의 LaserCube를 사용하는 경우, 또는;
* Mercury가 내장된 X-Laser 조명 기기를 사용하는 경우, 또는;
* AVB 컨트롤러가 내장된 Laser Animation Sollinger 레이저를 사용하는 경우(현재 macOS에서만 테스트 중)

{% hint style="info" %}
**레이저 컨트롤러란 무엇인가요?**

레이저 컨트롤러(또는 DAC)는 Liberation에서 보내는 디지털 데이터를 받아, 레이저의 스캐너와 출력을 제어하는 데 필요한 아날로그 신호로 변환하는 하드웨어 장치입니다. 그래서 DAC(Digital to Analog Converter, 디지털-아날로그 변환기)라고 부릅니다.

컨트롤러는 USB 또는 표준 컴퓨터 네트워크를 통해 컴퓨터에 연결됩니다. 외부 장치일 수도 있고, 레이저 내부에 설치되어 있을 수도 있습니다.

외부 장치인 경우 ILDA 연결을 통해 레이저에 연결합니다. ILDA는 구형 25핀 'D' 커넥터를 사용하는 업계 표준입니다. ILDA 케이블을 준비해 한쪽 끝은 컨트롤러에, 다른 한쪽 끝은 레이저에 연결하면 됩니다.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>외장 Ether Dream의 ILDA 출력</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>ILDA 입력을 포함한 여러 연결 단자가 있는 레이저 후면 패널</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>표준 ILDA 케이블</p></figcaption></figure>

### 어떤 컨트롤러가 가장 적합한가요?

가정 사용자이거나, 컴퓨터와 가까운 위치에서 4대 이하의 레이저로 소규모 쇼를 운영한다면 **Helios DAC** 같은 USB 컨트롤러가 **가장 경제적인** 옵션입니다.

**Ether Dream** 같은 네트워크 DAC는 네트워크 설정에 익숙하고 많은 수의 레이저를 운용하려는 **전문 레이저 운영자에게 가장 적합한** 옵션입니다. 지금까지 진행된 대규모 Liberation 쇼는 모두 Ether Dream으로 운영되었습니다.

**LaserCube**가 있다면 별도의 레이저 컨트롤러가 전혀 필요하지 않습니다. Liberation은 모든 LaserCube와 호환됩니다. 초기 모델은 USB 케이블로 연결하고, 최신 모델은 네트워크를 통해 연결합니다.

가장 간단한 옵션을 찾는 전문가라면 Mercury가 내장된 X-Laser 장비나 AVB를 사용하는 Laser Animation Sollinger 레이저를 고려해 보세요.

### 호환되는 레이저 컨트롤러

#### Ether Dream (Network)

[Ether Dream](https://ether-dream.com)은 10년 넘게 사용되어 왔으며 현재 버전 4까지 출시되어 있습니다(Liberation은 Ether Dream 버전 1, 2, 3과도 함께 사용할 수 있습니다). 매우 안정적인 장치입니다.

표준 네트워크를 통해 연결합니다. 독립형 장치로 구매할 수도 있고, 더 좋은 방법으로는 레이저 내부에 장착할 수도 있습니다.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/)는 입문자에게 가장 좋은 옵션이며 Ether Dream보다 저렴합니다. 다만 USB로 연결되기 때문에 긴 케이블 연결에는 권장하지 않습니다. 또한 4대 이상 연결하면, 특히 Windows에서 USB 데이터 및 드라이버 문제가 발생할 수 있습니다.

하지만 집에서 레이저 몇 대만 운용하려는 경우에는 가장 저렴하고 간단한 옵션입니다.

#### Mercury (Built-in to X-Laser units)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system)는 X-Laser의 강력한 DMX 레이저 제어 시스템으로, 전통적인 조명 콘솔에서 레이저를 직접 운용하려는 조명 디자이너를 위해 설계되었습니다. 최신 펌웨어 업데이트를 통해 Mercury에는 **Ether Dream 에뮬레이션**도 포함되었으며, 이제 Liberation은 물론 Ether Dream을 지원하는 다른 소프트웨어와도 원활하게 작동합니다.

#### AVB (Built into Laser Animation Sollinger units)

**AVB**는 고성능, 저지연 오디오 및 데이터 스트리밍을 위한 개방형 네트워크 기반 프로토콜입니다. 많은 LaserAnimation Sollinger 프로젝터는 하드웨어에 AVB 지원이 직접 포함되어 있어, 외부 DAC 없이도 Liberation이 네트워크를 통해 연결할 수 있습니다. Liberation의 AVB 지원은 현재 **macOS 전용이며 테스트 중**이고, **호환되는 AVB 지원 네트워크 장치**가 필요합니다. 올바르게 설정하면 전문 쇼에서 더 단순한 작업 흐름, 더 적은 외부 장치, 안정적인 신뢰성을 제공합니다. I

#### 향후 지원 예정인 컨트롤러:

* [IDN](http://www.ilda-digital.com) (ILDA의 개방형 네트워크 프로토콜로, 모든 제조사가 구현할 수 있음)

### 케이블 연결 제안

최적의 성능을 위해 USB DAC는 컴퓨터 가까이에 두고, 더 긴 ILDA 케이블을 사용해 레이저에 연결하세요. (단, ILDA 케이블은 철수 작업 중 주변에 걸려 갈고리처럼 작용할 수 있으니 주의하세요!)

Ether Dream을 사용하는 경우에도 모두 한곳에 모아 두고 긴 ILDA 케이블로 레이저에 연결할 수 있습니다. 또는 레이저 가까이에 설치하고 더 긴 네트워크 케이블을 사용할 수도 있습니다.

가장 이상적인 구성은 Ether Dream(또는 다른 컨트롤러)을 레이저 내부에 직접 설치하는 것입니다(영국에서는 Stanwax Laser의 Rob이 이 작업을 해 줍니다).
