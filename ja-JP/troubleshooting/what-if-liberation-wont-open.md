---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Liberation が開かない場合は？

まれに、Liberation が起動しなかったり、開いた直後にクラッシュしたりすることがあります。ほとんどの場合、ローカル設定ファイルのいずれかが破損したことが原因です。通常は、システムクラッシュやコンピューター上での予期しない問題の後に発生します。

幸い、ローカル設定をリセットすることで簡単に修正できます。macOS と Windows での手順は以下のとおりです。

> **重要**
>
> * 作業を始める前に Liberation を終了してください。
> * これらの手順で影響を受けるのは、ローカル設定、ログ、キャッシュのみです。ライセンスとアカウントは安全です。

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
3. 使用しているバージョン番号に一致するフォルダーを開きます。例: `1.0.0`

**Windows**

1.  **Win + R** を押し、次を貼り付けて **Enter** を押します。

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. 使用しているバージョン番号に一致するフォルダーを開きます。例: `1.0.0`

> **Windows のヒント**: File Explorer で参照する場合は、隠し項目を有効にしてください: **View > Show > Hidden items**。

***

#### 手順 1 – 設定ファイルを安全にリセットする

バージョンフォルダー内で、次を開きます。

```
data/liberation/
```

liberation フォルダー内に、se`ttings.json` というファイルがあるはずです。このファイルを削除します。

* **macOS の例**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows の例**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

次に Liberation を起動してみてください。開く場合は、これで完了です。

***

#### 手順 2 – 問題のある Clip がないか確認する

Clip を編集中に Liberation がクラッシュした場合、その Clip ファイルに関する何かが問題の原因になっている可能性があります。

settings.json ファイルと同じフォルダー内に、clipEdit`.json` というファイルがあるはずです。

このファイルを安全な場所（たとえば Desktop）にバックアップしてから、Liberation の作業フォルダーから削除します。

Liberation をもう一度起動してみてください。正常に開くようになった場合は、原因を調査できるよう、バックアップしたファイルを [**info@liberationlaser.com**](mailto:info@liberationlaser.com) までメールでお送りください。

***

#### 手順 3 - バックアップしてから、作業フォルダー全体を削除する

手順 1 と手順 2 で解決しなかった場合:

1. バージョンフォルダー全体を**バックアップ**します。
   * macOS: `1.0.0` フォルダーを右クリックして **Compress** を選択し zip を作成するか、Desktop などの安全な場所にコピーします。
   * Windows: `1.0.0` フォルダーを右クリックして **Send to > Compressed (zipped) folder** を選択するか、Desktop などの安全な場所にコピーします。
2. バックアップ後、Liberation の作業場所から元の `1.0.0` フォルダーを**削除**します。
3. Liberation をもう一度起動します。新しい作業フォルダーが再作成されます。

これで Liberation が開くようになった場合は、手順 4 に進んでください。

***

#### 手順 4 - バックアップを送信する

これにより、問題の原因を特定し、今後のバージョンで再発を防ぐための参考にできます。

手順 3 の**バックアップ**をまだ zip 化していない場合は zip 化し、原因を診断できるようメールでお送りください。

* **宛先**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **件名**: Liberation start-up fix - working folder backup
* **本文**: 次の内容を含めてください。
  * オペレーティングシステムとバージョン（例: macOS 14.6 または Windows 11 23H2）
  * Liberation のバージョン（例: 1.0.0）
  * 解決した手順がある場合は、その手順（手順 1、手順 2、または手順 3）
  * 問題が始まる前に何が起きたかの簡単な説明
* **添付ファイル**: `1.0.0` 作業フォルダーの zip 化したバックアップ。

> zip がメールに添付するには大きすぎる場合は、クラウドドライブにアップロードしてリンクを共有してください。

***

#### 手順 3 の後も起動しない場合

作業フォルダーを削除しても Liberation が開かない場合:

* コンピューターを再起動して、もう一度試してください。
* 新しいフォルダーの作成をブロックする可能性があるウイルス対策ソフトやセキュリティツールを一時的に無効にしてから、起動してみてください。
* 既存のインストールに上書きする形で、最新の Liberation ビルドを再インストールしてください。
* 上記のどれでも解決しない場合は、詳細と、存在する場合は `logs` サブフォルダー内のクラッシュログを添えて、[**info@liberationlaser.com**](mailto:info@liberationlaser.com) までサポートにお問い合わせください。

***

#### まとめ

1. バージョン別の作業フォルダー内にある `data/liberation/settings.json` を削除します。
2. Clip を編集中だった場合は、`data/liberation/clipEdit.json` をバックアップしてから削除します。
3. それでも開かない場合は、`1.0.0`（または使用しているバージョン）のフォルダー全体をバックアップしてから削除します。
4. 手順 3 で解決した場合（または解決しなかった場合）も、バックアップを zip 化し、OS と Liberation のバージョンを添えて [**info@liberationlaser.com**](mailto:info@liberationlaser.com) までお送りください。
