---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX ゾーン

DMX zone は、レーザーポイントの代わりに Art-Net/DMX を送信する Liberation の Output zone です。beam zone や canvas zone と並んで表示されるため、同じ zone セレクターのワークフローで Clip を割り当てられます。

管理するには、メニューから **DMX Zones** を開くか、Laser Overview の DMX セクションを使用します。

* **ADD DMX ZONE** - 新しい DMX zone を作成します。
* **ARM** - その zone の DMX 出力を有効にします。有効化されていない DMX zone は、マッピングされたチャンネルをゼロにクリアします。
* **Node** - Art-Net の node 番号を選択します。
* **Universe** - Art-Net の universe を選択します。表示値は 1 始まりなので、Universe 1 が最初の universe です。
* **Address** - フィクスチャーの開始アドレスを設定します。表示値も 1 始まりです。
* **Preset** - Clip の内容を DMX チャンネルにマッピングする DMX プリセットを選択します。
* **Edit DMX zone settings**（鉛筆アイコン）- 手動の zone 転送やフィクスチャーの向きなど、zone 設定を開きます。
* **Edit DMX profile/channel mapping**（スライダーアイコン）- DMX プリセット／チャンネルエディターを開きます。
* **Delete** - DMX zone を削除します。

### 有効化できる数の上限

同時に有効化できる DMX zone の数は、ライセンス階層によって異なります。お使いの階層で DMX 出力が許可されていない場合、またはすでに上限数の DMX zone を有効化している場合、追加の zone の **ARM** ボタンは無効になり、ホバーすると進入禁止アイコンが表示されます。

さらに zone を有効化する前に、別の DMX zone を無効化するか、DMX の上限がより高いライセンス階層を使用してください。
