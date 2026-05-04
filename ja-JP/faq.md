---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## ハードウェア

#### **Liberation は Windows で動作しますか？**

はい。Liberation は **Windows 10 および 11（64-bit）**を完全にサポートしており、Mac 版とまったく同じ機能を利用できます。すべてのリリースは両プラットフォーム向けに同時に提供されます。

#### **Liberation は Mac で動作しますか？**

はい。Liberation は **Mac（macOS 12 Monterey 以降）**を完全にサポートしており、Windows 版と同じ機能を利用できます。すべてのアップデートは同時にリリースされます。

#### **必要な最小スペックはどの程度ですか？**

制御したいレーザーの台数によって異なります。数台のレーザーだけを使う場合は、低スペックのマシンでも問題ありません。Apple Silicon Mac はどれも非常に良好に動作し、最大 100 台程度のレーザーを制御できるはずです。重要度の高い複雑なショーを実行する場合は、予算内でできるだけ高性能なマシンをおすすめします。

#### **Liberation で何台のレーザーを制御できますか？**

Liberation は 1 台のコンピューターで多数のレーザーを動作できます。100 台を超えるレーザーコントローラーでテスト済みですが、実際の台数は次の要素によって決まります。

* コンピューターの CPU
* ネットワーク速度
* サブスクリプションの種類

#### **どの MIDI コントローラーを使用できますか？**

Liberation は、人気の APC40 Mk2 MIDI コントローラーを中心に設計・最適化されています。APC40 Mk1 でも動作します。詳しくは [APC40でのライブコントロール](midi-control/live-control-with-the-apc40.md "mention") を参照してください。

Liberation は APC Mini と MIDI Fighter Twister にも対応しています。APC40 Mk2 は、現在も最も機能が揃ったリファレンスコントローラーです。

追加の MIDI 制御を行うための MIDI Send/Receive システムもあります。詳しくは [MIDI Send/Receive](midi-control/midi-send-receive.md "mention") を参照してください。

詳細については [MIDI コントロール](midi-control/ "mention") を参照してください。

#### **任意の MIDI コントローラーを使用できますか？**

他のコントローラーでは、MIDI Send/Receive システムを使用するか、Liberation のデフォルト MIDI メッセージを送信できる MIDI トランスレーターを使用してください。この設定については [forum](https://forum.liberationlaser.com) で情報を探せますが、現実的には、ほとんどのライブショーでは APC40 Mk2 が最適な選択肢です。

## レーザーコントローラー

#### **Liberation と互換性のあるレーザーコントローラーはどれですか？**

* [Ether Dream（推奨）](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system)（ファームウェアの更新が必要な場合があります）
* LaserCube USB（および LaserDock）
* LaserCube ネットワークプロトコル（有線接続）
* [LASollinger lasers](https://laseranimation.com/en/) で使用される AVB（現在 macOS のみ、テスト中）

詳細については [対応レーザーとコントローラー（DAC）](hardware/compatible-lasers-and-controllers-dacs.md "mention") を参照してください。

#### **なぜ \[他社ブランドの] レーザーコントローラーをサポートしないのですか？**

ソフトウェアとハードウェア間の相互運用性を高めるため、Liberation は通信プロトコルが公開されている DAC のみをサポートします。これはレーザー業界にとって最善の方向だと考えています。

#### **自分のレーザーが Liberation で使えるかどうかは、どう確認できますか？**

お使いのレーザーに次のいずれかがある場合、Liberation で使用できます。

* 外部 **ILDA 入力** — 25 ピン D コネクター。対応する外部コントローラーと組み合わせて使用します。
* 内蔵 **Ether Dream**。
* 任意の **LaserCube**（USB と Wi-Fi LaserCube の両方で動作します）。
* **Mercury system 内蔵の X-Laser ユニット**（Ether Dream モード）。
* **AVB 内蔵の LaserAnimation Sollinger projector**（macOS のみ、AVB 対応ネットワーク機器が必要、現在テスト中）。

詳細については [対応レーザーとコントローラー（DAC）](hardware/compatible-lasers-and-controllers-dacs.md "mention") を参照してください。

#### **Liberation を LaserCube と一緒に使用できますか？**

はい。Liberation は任意の LaserCube と直接動作します。詳しくは [LaserCube](hardware/lasercube.md "mention") を参照してください。

## ライセンス

#### **ライセンスの価格はいくらですか？**

現在の価格については [shop](https://liberationlaser.com/shop) ページを参照してください。

#### **ライセンスティア間の制限は何ですか？**

現在のライセンスオプションについては [shop](https://liberationlaser.com/shop) ページを参照してください。

無料ティアを含む**すべて**のティアで、任意の台数のレーザーを使ってセットアップ、プレビュー、ショー設計を行えます。制限は、_arm_ できるレーザーの台数のみです。それ以外の Liberation の機能はすべて、全ユーザーが利用できます。

#### **新しいティアにアップグレードできますか？**

上位ティアにはいつでもアップグレードできます。現在のライセンスの残り期間分は一部返金され、新しいプランはすぐに開始されます。詳しくは [ライセンスのアップグレード / ダウングレード](installation/upgrade-downgrade-your-license.md "mention") を参照してください。

#### **ライセンスをダウングレードできますか？**

いつでもダウングレードできますが、変更は現在のライセンス期間の終了時に適用されます。詳しくは [ライセンスのアップグレード / ダウングレード](installation/upgrade-downgrade-your-license.md "mention") を参照してください。

#### **ライセンスでコンピューターを認証するにはどうすればよいですか？**

ライセンスを購入すると、Liberation ソフトウェア内でコンピューターを認証できます。_About_ 画面に _Authorise_ ボタンが表示され、クリックすると Web サイトへのログインを求められます。画面の指示に従って認証プロセスを完了してください。詳しくは [認証と認証解除](installation/authorising-and-de-authorising.md "mention") を参照してください。

#### **コンピューターをどのくらいの頻度でインターネットに接続する必要がありますか？**

ライセンスが更新されるたびに、Liberation をインターネットに接続して内部ライセンスを更新する必要があります。月額の自動更新支払いの場合は、毎月接続する必要があります。

#### **更新後にコンピューターをインターネットに接続できない場合はどうなりますか？**

ライセンス更新後、Liberation は内部ライセンスを更新するための 7 日間の猶予期間を提供します。その期間を過ぎると、Liberation は _Free_ モードに戻ります。

#### **クレジットカードの有効期限が切れた場合はどうなりますか？**

決済プロバイダーからメール通知が届きます。その後、支払い方法を更新する必要があります。Web サイトにログインし、サブスクリプションページの _Update payment details_ リンクを使用してください。

#### **定期更新ライセンスをキャンセルするにはどうすればよいですか？**

Web サイトにログインし、_Your subscriptions_ ページを開き、キャンセルしたいサブスクリプションを選択して、_Cancel Subscription_ リンクをクリックします。ライセンス期間の残りの間は、Liberation を引き続き使用できます。

#### **Liberation は何台のコンピューターにインストールできますか？**

Liberation は好きな台数のコンピューターにインストールできます。ライセンス認証が必要なのは laser / DMX output を有効にする場合のみで、同時に output 用として認証できるコンピューターの台数はライセンスティアによって決まります。詳しくは [ライセンスの仕組み](installation/how-licensing-works.md "mention") を参照してください。

#### **ライセンスを別のコンピューターに移すにはどうすればよいですか？**

* もう使用しないコンピューターで Liberation を開きます。
* インターネットに接続されていることを確認し、_About_ 画面の _De-authorise this computer_ ボタンをクリックします。
* 次に、新しいコンピューターで Liberation を開きます。
* _About_ 画面の _Authorise this computer_ ボタンをクリックします。
* Web サイトが開くので、ログインして画面の指示に従い、認証を完了します。

アクセスできなくなったコンピューターをリモートで認証解除することもできます（一部制限があります）。詳しくは [認証と認証解除](installation/authorising-and-de-authorising.md "mention") を参照してください。

#### **紛失または盗難にあったコンピューター上の Liberation を認証解除できますか？**

Web サイトからコンピューターを認証解除できます。前回の更新以降、その Liberation インストールがオンラインになっていない場合は、すぐに実行できます。

そうでない場合、認証解除はサブスクリプション更新時、またはそのコンピューターがインターネットに接続した時点の、どちらか早い方で有効になります。新しいコンピューターを至急再認証する必要がある場合は、サポートに連絡してください。

### Liberation の使用

#### デフォルト設定にはレーザーが 8 台あります。これを変更するにはどうすればよいですか？

[プロジェクトの設定](setting-up/setting-up-your-project.md "mention") と [レーザーの追加 / 削除](setting-up/adding-removing-lasers.md "mention") を参照してください。

#### あるレーザーのゾーン設定を他のレーザーにコピーできますか？

はい。詳しくは [レーザー間でゾーンをコピーする](output-view/copy-zones-between-lasers.md "mention") を参照してください。

#### スライダーの代わりに数値を入力できますか？

はい。スライダーを `Cmd / Ctrl`-クリックすると、キーボードで値を入力できます。

#### **Liberation を音楽に同期するにはどうすればよいですか？**

期待どおりに動作するインテリジェントな "tap tempo" システムがありますが、外部 MIDI clock または Ableton Link も使用できます。詳しくは [テンポ / 同期](tempo-synchronisation.md "mention") を参照してください。タイムラインは、任意のオーディオインターフェイス経由で入力される LTC/SMPTE timecode に同期できます。詳しくは [Timecode](timecode.md "mention") を参照してください。

#### レーザーから最適な出力を得るには、どの設定を調整すればよいですか？

主な設定は _Colour Shift_ です。これは、ミラーの動きとレーザーの明るさの変化の間にあるわずかな遅延を補正します。レーザードットやビームに小さな「尾」がある場合は、この設定を調整する必要があります。（「尾」の例は [Laser output 設定パネル](setting-up/laser-settings.md "mention") ページの写真を参照してください）

scanner speed を変更してみることもできます。スキャナーが基本的なものなら遅めに、高性能なものなら速めに設定します。ただし、**過度に駆動するとスキャナーを損傷する可能性があるため、注意して使用してください。**

プリセットの scanner settings もいくつか用意されています。デフォルトオプションは控えめな設定で、ほとんどのレーザービーム用途に適しています。ただし、より高性能なスキャナー向けのプリセットや、グラフィックス向けに調整されたプリセットもあります。

詳細については [Laser output 設定パネル](setting-up/laser-settings.md "mention") を参照してください。独自のプリセットを作成する方法については [◼️ Scanner プリセットとレンダープロファイル](advanced/scanner-presets.md "mention")（上級者向け、作成中）を参照してください。

_Colour calibration_ 設定を使ってカラーバランスを補正することもできます。詳しくは [カラーキャリブレーション](advanced/colour-calibration.md "mention")（上級テクニック）を参照してください。

#### _Latency(ms)_ 設定は何をしますか？

これはフレームレイテンシー、つまりフレームが生成されてからレーザーへ送信されるまでの最大時間です。通常は調整する必要はありませんが、ネットワークの問題がある場合は値を大きくしてみることができます。詳細は [レイテンシー設定](setting-up/latency-setting.md "mention") を参照してください。

### Clips

#### クリップを実行せずに、そのゾーンや設定を調整するにはどうすればよいですか？

`Alt / Option`-クリックすると、アクティブ化せずに _現在選択されている Clip_ にできます。あわせて [クリップの開始／停止](clips/starting-stopping-clips.md "mention") も参照してください。

#### クリップをコピーするにはどうすればよいですか？

`Alt / Option` キーを押したままクリックしてドラッグします。あわせて [Clip Deckを整理する](clips/organising-your-clip-deck.md "mention") も参照してください。

#### クリップを削除するにはどうすればよいですか？

クリップをクリックして clip deck の外へドラッグします。あわせて [Clip Deckを整理する](clips/organising-your-clip-deck.md "mention") も参照してください。

#### 複数選択、削除、clip deck の結合などはどうすればよいですか？

[Clip Deckを整理する](clips/organising-your-clip-deck.md "mention") を参照してください。

#### クリップ上の小さなマイクの記号やその他のアイコンは何を示していますか？

これらは、そのクリップが音声または MIDI 入力を受け取ることを示しています。また、3 つの点は zone delay があることを示します。詳しくは [Clipボタンに表示される小さなアイコンは何ですか？](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention") を参照してください。
