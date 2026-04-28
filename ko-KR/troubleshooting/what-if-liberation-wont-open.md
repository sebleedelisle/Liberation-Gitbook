---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Liberation이 열리지 않으면 어떻게 하나요?

드문 경우지만, Liberation이 실행되지 않거나 열리자마자 충돌할 수 있습니다. 대부분 로컬 구성 파일 중 하나가 손상되었을 때 발생합니다. 보통 시스템 충돌이나 컴퓨터에서 예상치 못한 문제가 발생한 뒤에 생깁니다.

다행히 로컬 설정을 초기화하면 쉽게 해결할 수 있습니다. macOS와 Windows에서 진행하는 방법은 다음과 같습니다.

> **중요**
>
> * 작업을 시작하기 전에 Liberation을 닫으세요.
> * 아래 단계는 로컬 설정, 로그, 캐시에만 영향을 줍니다. 라이선스와 계정은 안전합니다.

***

#### 작업 폴더 위치

Liberation의 각 버전에는 고유한 작업 폴더가 있습니다. 예를 들어 1.0.0 버전을 사용 중이라면 폴더 이름은 1.0.0입니다.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**폴더를 빠르게 여는 방법**

**macOS**

1. Finder에서 **Shift + Cmd + G**를 누릅니다.
2.  이 경로를 붙여넣고 **Enter**를 누릅니다.

    ```
    ~/Library/Application Support/Liberation
    ```
3. 사용 중인 버전 번호와 일치하는 폴더를 엽니다. 예: `1.0.0`.

**Windows**

1.  **Win + R**을 누르고, 아래 경로를 붙여넣은 다음 **Enter**를 누릅니다.

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 사용 중인 버전 번호와 일치하는 폴더를 엽니다. 예: `1.0.0`.

> **Windows 팁**: File Explorer로 직접 찾아가는 경우 숨김 항목을 표시하세요: **View > Show > Hidden items**.

***

#### 1단계 – 설정 파일을 안전하게 초기화하기

버전 폴더 안에서 다음 위치를 엽니다.

```
data/liberation/
```

liberation 폴더 안에서 se`ttings.json`라는 파일을 찾을 수 있습니다. 이 파일을 삭제하세요.

* **macOS 예시**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows 예시**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

이제 Liberation을 실행해 보세요. 열리면 완료입니다.

***

#### 2단계 – 문제가 있는 clip 확인하기

clip을 편집하는 중에 Liberation이 충돌했다면 해당 clip 파일의 어떤 부분이 문제를 일으키고 있을 수 있습니다.

settings.json 파일과 같은 폴더에서 clipEdit`.json`라는 파일을 찾을 수 있습니다.

이 파일을 안전한 위치(예: Desktop)에 백업한 다음, Liberation 작업 폴더에서 삭제하세요.

Liberation을 다시 실행해 보세요. 이제 정상적으로 열리면 백업해 둔 파일을 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)으로 보내 주세요. 문제 원인을 조사하는 데 도움이 됩니다.

***

#### 3단계 - 전체 작업 폴더를 백업한 뒤 삭제하기

1단계와 2단계로 해결되지 않았다면:

1. 전체 버전 폴더를 **백업**합니다.
   * macOS: `1.0.0` 폴더를 오른쪽 클릭하고 **Compress**를 선택해 zip 파일을 만들거나, Desktop처럼 안전한 위치에 복사합니다.
   * Windows: `1.0.0` 폴더를 오른쪽 클릭하고 **Send to > Compressed (zipped) folder**를 선택하거나, Desktop처럼 안전한 위치에 복사합니다.
2. 백업한 뒤 Liberation 작업 위치에서 원본 `1.0.0` 폴더를 **삭제**합니다.
3. Liberation을 다시 실행합니다. 새 작업 폴더가 다시 생성됩니다.

이제 Liberation이 열리면 4단계로 진행하세요.

***

#### 4단계 - 백업 보내기

이 백업은 문제의 원인을 확인하고 향후 버전에서 예방하는 데 도움이 됩니다.

3단계에서 만든 **백업**을 아직 zip으로 압축하지 않았다면 압축한 다음, 원인 진단을 위해 이메일로 보내 주세요.

* **받는 사람**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **제목**: Liberation start-up fix - working folder backup
* **본문**: 다음 내용을 포함해 주세요.
  * 운영 체제 및 버전(예: macOS 14.6 또는 Windows 11 23H2)
  * Liberation 버전(예: 1.0.0)
  * 문제가 해결된 단계가 있다면 해당 단계(1단계, 2단계 또는 3단계)
  * 문제가 시작되기 전에 어떤 일이 있었는지에 대한 간단한 설명
* **첨부 파일**: `1.0.0` 작업 폴더의 zip 백업 파일.

> zip 파일이 이메일로 보내기에는 너무 크다면 클라우드 드라이브에 업로드하고 링크를 공유해 주세요.

***

#### 3단계 후에도 여전히 실행되지 않나요?

작업 폴더를 삭제한 뒤에도 Liberation이 열리지 않는다면:

* 컴퓨터를 재부팅한 뒤 다시 시도하세요.
* 새 폴더 생성을 차단할 수 있는 antivirus 또는 보안 도구를 일시적으로 비활성화한 뒤 실행해 보세요.
* 기존 설치 위에 최신 Liberation 빌드를 다시 설치하세요.
* 위 방법이 모두 작동하지 않으면 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)으로 지원팀에 문의하세요. 자세한 설명과 함께, `logs` 하위 폴더가 있다면 해당 crash log도 보내 주세요.

***

#### 요약

1. 버전별 작업 폴더에서 `data/liberation/settings.json`을 삭제합니다.
2. clip을 편집 중이었다면 `data/liberation/clipEdit.json`을 백업한 뒤 삭제합니다.
3. 그래도 열리지 않으면 전체 `1.0.0` 폴더(또는 사용 중인 버전 폴더)를 백업한 뒤 삭제합니다.
4. 3단계로 해결되었거나 해결되지 않았더라도, 백업을 zip으로 압축해 OS 및 Liberation 버전과 함께 [**info@liberationlaser.com**](mailto:info@liberationlaser.com)으로 보내 주세요.
