---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Liberation が開かない場合は？

まれに、Liberation が起動しなかったり、開いた直後にクラッシュしたりすることがあります。ほとんどの場合、ローカル設定ファイルのいずれかが破損していることが原因です。通常は、システムクラッシュやコンピューター上で予期しない問題が起きた後に発生します。

幸い、ローカル設定をリセットするだけで簡単に修正できます。macOS と Windows での手順は以下のとおりです。

> **重要**
>
> * 作業を始める前に Liberation を閉じてください。
> * これらの手順が影響するのは、ローカル設定、ログ、キャッシュのみです。ライセンスとアカウントには影響しません。

***

#### 作業フォルダーの場所

Liberation の各バージョンには、それぞれ専用の作業フォルダーがあります。たとえば、バージョン 1.0.0 を使用している場合、フォルダー名は 1.0.0 になります。

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**フォルダーをすばやく開く方法**

**macOS**

1. Finder で **Shift + Cmd + G** を押します。
2.  次のパスを貼り付けて **Enter** を押します。

    ```
    ~/Library/Application Support/Liberation
    ```
3. 使用しているバージョン番号と一致するフォルダーを開きます。例：`1.0.0`

**Windows**

1.  **Win + R** を押し、次を貼り付けて **Enter** を押します。

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 使用しているバージョン番号と一致するフォルダーを開きます。例：`1.0.0`

> **Windows のヒント**: File Explorer から参照する場合は、隠し項目を有効にしてください：**View > Show > Hidden items**。

***

#### Step 1 – 設定ファイルを安全にリセットする

バージョンフォルダー内で、次を開きます。

```
data/liberation/
```

liberation フォルダー内に `settings.json` というファイルがあります。このファイルを削除します。

* **macOS の例**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows の例**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

ここで Liberation を起動してみてください。開くようになれば、これで完了です。

***

#### Step 2 – 問題のある Clip を確認する

Clip の編集中に Liberation がクラッシュした場合、その Clip ファイルに関する何かが問題を引き起こしている可能性があります。

settings.json ファイルと同じフォルダー内に、`clipEdit.json` というファイルがあります。

このファイルを安全な場所（たとえば Desktop）にバックアップしてから、Liberation の作業フォルダーから削除します。

もう一度 Liberation を起動してみてください。正常に開くようになった場合は、問題の原因を調査できるよう、バックアップしたファイルを [**info@liberationlaser.com**](mailto:info@liberationlaser.com) までメールでお送りください。

***

#### Step 3 - バックアップしてから作業フォルダー全体を削除する

Step 1 と Step 2 で解決しなかった場合：

1. バージョンフォルダー全体を**バックアップ**します。
   * macOS: `1.0.0` フォルダーを右クリックして **Compress** を選択し zip を作成するか、Desktop など安全な場所にコピーします。
   * Windows: `1.0.0` フォルダーを右クリックして **Send to > Compressed (zipped) folder** を選択するか、Desktop など安全な場所にコピーします。
2. バックアップ後、Liberation の作業場所から元の `1.0.0` フォルダーを**削除**します。
3. Liberation を再度起動します。新しい作業フォルダーが自動的に作成されます。

これで Liberation が開くようになった場合は、Step 4 に進んでください。

***

#### Step 4 - バックアップを送信する

これにより、問題の原因を特定し、今後のバージョンで防止できるようになります。

Step 3 の**バックアップ**をまだ zip 化していない場合は zip に圧縮し、原因を診断できるようメールでお送りください。

* **宛先**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **件名**: Liberation start-up fix - working folder backup
* **本文**: 次の内容を含めてください。
  * オペレーティングシステムとバージョン（例：macOS 14.6 または Windows 11 23H2）
  * Liberation のバージョン（例：1.0.0）
  * どの手順で解決したか（該当する場合。Step 1、Step 2、または Step 3）
  * 問題が発生する前に何が起きたかの簡単な説明
* **添付ファイル**: `1.0.0` 作業フォルダーの zip バックアップ。

> zip がメールで送るには大きすぎる場合は、クラウドドライブにアップロードしてリンクを共有してください。

***

#### Step 3 の後も起動しない場合

作業フォルダーを削除した後も Liberation が開かない場合：

* コンピューターを再起動して、もう一度試してください。
* 新しいフォルダーの作成をブロックする可能性のあるウイルス対策ソフトやセキュリティツールを一時的に無効にしてから、起動してみてください。
* 既存のインストールに上書きする形で、最新の Liberation ビルドを再インストールしてください。
* 上記のいずれでも解決しない場合は、詳細と、存在する場合は `logs` サブフォルダー内のクラッシュログを添えて、[**info@liberationlaser.com**](mailto:info@liberationlaser.com) までサポートにご連絡ください。

***

#### まとめ

1. バージョン付きの作業フォルダー内で `data/liberation/settings.json` を削除します。
2. Clip を編集中だった場合は、`data/liberation/clipEdit.json` をバックアップしてから削除します。
3. それでも開かない場合は、`1.0.0`（または使用中のバージョン）フォルダー全体をバックアップしてから削除します。
4. Step 3 で解決した場合（または解決しなかった場合も）、バックアップを zip に圧縮し、OS と Liberation のバージョンを添えて [**info@liberationlaser.com**](mailto:info@liberationlaser.com) までお送りください。
