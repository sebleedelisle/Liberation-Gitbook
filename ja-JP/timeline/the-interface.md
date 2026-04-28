---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/the-interface
---

# 🟧 インターフェース

### Timeline インターフェース

音楽制作ソフトや動画編集ソフトを使ったことがあれば、Timeline の考え方はなじみやすいはずです。Timeline は、時間が左から右へ進む横方向のグリッドで、その上に Clip を配置して「いつ何を再生するか」を決めます。

Timeline が初めての場合は、楽譜や舞台のキューシートのようなものだと考えてください。各ブロックは、特定のタイミングでトリガーされるコンテンツの一部です。レーザーショーが時間に沿ってどのように展開するかを設計するための、構造化された方法です。

***

#### Timeline Bar Controls

**Enable Button**

Timeline を操作する前に、有効にする必要があります。**ENABLE** トグル（有効時はオレンジ）をクリックして、編集と再生に使用する Timeline を有効にします。

**Timeline Name**

現在の Timeline 名が Enable Button の横に表示されます（デフォルトは **“Timeline”**）。クリックすると名前を変更できます。複数の曲やセグメントを管理するときに便利です。

**Timeline List (Three Bars Icon)**

クリックすると Timeline リストが開きます。ここから Timeline を切り替えたり、ショーに追加・削除したりできます。

**Lock Button**

Timeline を誤操作による変更から保護します。有効にすると、ロックを解除するまで編集できません。

**Add Clips Button**

Clip Deck で現在選択されているすべての Clip を、現在の再生ヘッド位置に追加します。ライブ演奏や準備済みの選択内容から Timeline を組み立てるときに便利です。

**Insert Audio File**

Timeline の先頭に挿入するオーディオファイルを選択するためのファイルダイアログを開きます。対応形式：WAV、MP3、OGG、FLAC。Timeline を音楽に同期させるときに便利です。

**Default Clip Duration**

ドラッグまたは + ボタンで Timeline に新しい Clip を追加するときのデフォルトの長さ（小節単位）を設定します。シーケンス作成時の作業を効率化できます。

**Volume**

Timeline 上のすべてのオーディオ Clip の再生音量を調整します。レーザー出力には影響しません。

***

#### Transport and Playback

**Transport Controls**

移動と再生に使う標準的なトランスポートボタンです。

* Forward / back（1 小節ずつ移動）
* Stop / Rewind to start
* Play / pause
* Record

**Bar / Beat / Step Display**

現在の Timeline 位置を bars:beats:frames 形式で表示します。再生の進行に合わせてリアルタイムに更新されます。

***

#### Sync and Timing

**Tempo Map Button**

テンポマッピングを有効にします。有効にすると、Timeline の上部に新しい行が表示され、右クリックでテンポ変更を追加できます。テンポが変化するトラックやテンポランプを含むトラックに適しています。

**Timecode Panel**

タイムコード設定パネルを開きます。ここでは、外部システムと正確に同期するために、Liberation を LTC、MIDI Clock、Ableton Link に同期する設定を行えます。

**SNAP Toggle**

有効にすると、Clip と編集操作がグリッドにスナップします。正確な位置合わせが簡単になります。自由に配置したい場合は無効にします。

**Snap Size**

グリッド解像度を bars、beats、steps から設定します。細かな編集や素早い再配置を行うときに便利です。

***

#### View and Playback Behavior

**Auto Scroll (Skater Icon)**

有効にすると、再生中に Timeline が自動でスクロールし、再生ヘッドを追従します。

**Scrub Mode (Light Bulb Icon)**

有効にすると、再生ヘッドを手動で動かしている間もレーザーがライブ出力されます。特定のフレームをプレビューするのに便利ですが、特に高出力のプロジェクターでは注意して使用してください。

**Loop Playback**

Timeline の先頭から設定された Timeline 長までをループ再生します。特定のセクションを作業するときや、背景ビジュアルを流し続けるときに便利です。

**Timeline Length**

Timeline 全体の長さを小節単位で設定します。ドラッグして調整するか、ダブルクリックして数値を直接入力します。
