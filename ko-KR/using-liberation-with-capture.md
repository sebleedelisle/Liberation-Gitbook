---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Capture와 함께 Liberation 사용하기

Liberation은 외부 비주얼라이저로 [Capture](https://capture.se)를 지원합니다(버전 1.0.3 이상). 이미 작업 흐름에서 Capture를 사용하고 있다면, 3D 장면 안에서 Liberation의 라이브 레이저 출력을 시각화하는 데 사용할 수 있습니다.

### 작동 방식

별도의 연결 절차나 수동 링크 설정은 필요하지 않습니다.

다음 조건만 충족하면 됩니다.

* Liberation과 Capture가 같은 네트워크에 있음
* 방화벽에서 연결을 허용함

…그러면 Liberation에서 설정한 모든 레이저가 Capture 안에 미디어 소스로 자동 표시됩니다. IP 주소를 설정하거나 특별한 기능을 활성화할 필요가 없습니다. 그냥 나타납니다.

### Capture 안에서 레이저 보기

Liberation에서 구성된 모든 레이저는 Capture에서 사용 가능한 미디어 소스로 표시됩니다.

실제로 출력을 보려면:

* 레이저가 Liberation에서 armed 상태여야 함
* 해당 소스가 Capture 안의 레이저 fixture에 연결되어 있어야 함

armed 상태가 되면 Capture는 Liberation의 라이브 출력 스트림을 시각화합니다. Liberation에서 레이저가 disarmed 상태가 되면 Capture에는 소스로 계속 표시되지만, 아무것도 출력하지 않습니다.

Capture에서 레이저를 설정하는 방법에 대한 자세한 안내와 지원은 [capture.se](https://www.capture.se/) 문서를 참조하세요. <br>

### 라이선스 제한과 armed 레이저

Capture 연결은 실제 물리적 레이저 출력과 정확히 동일하게 취급됩니다.

즉:

* 라이선스 등급에서 허용하는 수만큼만 레이저를 armed 상태로 설정할 수 있습니다
* armed 상태인 레이저만 Capture로 데이터를 실제 전송합니다

### Capture가 꼭 필요한가요?

전혀 필요하지 않습니다.

Liberation에는 내장 3D 비주얼라이저가 포함되어 있으며, 이 기능은 항상 사용할 수 있고 라이선스 등급에 의존하지 않습니다. 외부 소프트웨어 없이 Liberation 안에서 직접 쇼를 설계하고 미리 볼 수 있습니다.

Capture는 이미 조명 또는 쇼 디자인에 사용하고 있는 경우 선택할 수 있는 추가 옵션일 뿐입니다.

### 문제 해결

Capture에 레이저가 표시되지 않는 경우:

* 두 애플리케이션이 같은 네트워크에 있는지 확인하세요
* 방화벽 설정을 확인하세요
* 레이저가 Liberation에서 armed 상태인지 확인하세요
