---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/installation/transfer-your-content-when-upgrading-to-a-new-version
---

# 🟩 新しいバージョンへアップグレードするときにコンテンツを移行する

Liberation はコンテンツを作業フォルダーに保存します（[working folder の場所](../troubleshooting/where-to-find-the-working-folder.md) を参照）。この作業フォルダーは、新しいバージョンがリリースされるたびに変わります。古いバージョンの作業ファイルを新しいバージョンでも使いたい場合は、次の手順を行います。&#x20;

1. 元のバージョンの Liberation を開きます
2. _File->Project->Export Project_ を使用します。これにより、Liberation 内のすべて（レーザー設定、タイムライン、Clip Deck など）が保存されます。&#x20;
3. このバージョンを閉じてから、新しいバージョンの Liberation を開きます
4. _File->Project->Import Project_ を使用し、手順 2 でエクスポートしたプロジェクトファイルを選択します。&#x20;

これで、すべてのコンテンツが新しいバージョンに移行されているはずです。

#### Liberation の複数バージョンを保持する

新しいバージョンをインストールする前に、古いバージョンの名前を変更してください。通常はバージョン番号を使い、例として Liberation103.app（Windows では .exe）とします。Liberation は必要な数だけ保持できますが、同時に実行できるのは 1 つだけです。 <br>

#### 古いバージョンの Liberation を新しいバージョンで上書きしてしまった場合

最も確実な方法は、古いバージョンの Liberation を再インストールし、その後、上記の手順を実行することです。&#x20;

別の方法として、作業フォルダーをコピーし、新しいバージョン番号に合わせて名前を変更することもできます。&#x20;
