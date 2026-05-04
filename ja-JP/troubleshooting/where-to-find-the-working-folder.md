---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/where-to-find-the-working-folder
---

# ✅ working folder の場所

#### working folder の場所

Liberation の各バージョンには、それぞれ専用の working folder があります。たとえばバージョン 1.0.3 を実行している場合、フォルダー名は 1.0.3 になります。

* **macOS**: `~/Library/Application Support/Liberation/1.0.3`
* **Windows**: `AppData\Local\Liberation\1.0.3`

**フォルダーをすばやく開く方法**

**macOS**

1. Finder で **Shift + Cmd + G** を押します。
2.  次のパスを貼り付けて **Enter** を押します。

    ```
    ~/Library/Application Support/Liberation
    ```
3. 使用中のバージョン番号と一致するフォルダーを開きます。例：`1.0.3`

**Windows**

1.  **Win + R** を押し、次を貼り付けて **Enter** を押します。

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 使用中のバージョン番号と一致するフォルダーを開きます。例：`1.0.3`

> **Windows のヒント**: File Explorer から参照する場合は、隠し項目を有効にしてください：**View > Show > Hidden items**。
