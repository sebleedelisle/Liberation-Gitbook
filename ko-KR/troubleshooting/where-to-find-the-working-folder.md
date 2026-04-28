---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/where-to-find-the-working-folder
---

# ✅ 작업 폴더 위치 찾기

#### 작업 폴더 위치 찾기

Liberation의 각 버전에는 자체 작업 폴더가 있습니다. 예를 들어 버전 1.0.0을 실행 중이라면 폴더 이름은 1.0.0입니다.

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

1.  **Win + R**을 누른 다음 아래 내용을 붙여넣고 **Enter**를 누릅니다.

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 사용 중인 버전 번호와 일치하는 폴더를 엽니다. 예: `1.0.0`.

> **Windows 팁**: 대신 File Explorer에서 찾아보는 경우 숨겨진 항목을 표시하세요. **View > Show > Hidden items**.
