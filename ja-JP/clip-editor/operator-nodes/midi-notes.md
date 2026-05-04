---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

入力された MIDI ノートで、一定範囲にビームやシェイプをトリガーする「レーザーハープ」風のエフェクトを作成します。このノードは、渡されたコンテンツを各ノートの _ソース_ として使用します。ドットを入力すればドットの列になり、円のようなシェイプを入力すれば円の列になります。より複雑なシェイプも同じように複製されます。

Liberation がリッスンする MIDI インターフェースは、**Liberation → Settings**（`Cmd / Ctrl + ,`）で選択できます。

* **MIDI channel** – リッスンする MIDI チャンネル（0 = すべてのチャンネル、1–16 = 特定のチャンネル）。
* **width** – ノートが広がる全体の幅。
* **MIDI note min / max** – 範囲内の最低および最高 MIDI ノート値。
* **ignore out of range notes** – 設定範囲外のノートを除外します。無効にすると、範囲外のノートは最も近い使用可能なノートに「クランプ」されます（高いノートは範囲の上端を、低いノートは範囲の下端をトリガーします）。
* **auto extend range** – 範囲外のノートが演奏された場合、自動的に範囲を広げます。

{% hint style="info" %}
受信しているノート範囲が分からない場合は、**auto extend range** をオンにし、**MIDI note min** をかなり高く、**MIDI note max** をかなり低く設定してから、ノートを一通り演奏してください。システムがすべてのノートを検出し、範囲を自動で拡張します。すべて取得できたら、**auto extend range** をオフにして範囲を固定します。
{% endhint %}

* **leave all notes visible** – 演奏中かどうかにかかわらず、範囲内のすべてのノートに対してビームまたはシェイプを作成し、「レーザーハープ」風の効果にします。
* **hit colour** – ノートがトリガーされたときに表示される色。
* **hit colour hold time** – hit colour が最大輝度のまま保持される時間。値は秒単位です（0–1）。_100% = 1 秒。_
* **hit colour decay time** – 保持時間後に hit colour が元に戻るまでの時間。値は秒単位です（0–1）。_100% = 1 秒。_

{% hint style="info" %}
コンテンツがすでに純白の場合、hit colour を白に設定しても変化はありません。最良の結果を得るには、コンテンツに彩度の高い色を使い、hit colour を白に設定してください。ノートがトリガーされたときに、きれいなフラッシュ効果が得られます。
{% endhint %}

* **note off fade out time** – ノートをリリースした後、フェードするまでの時間。値は秒単位です（0–1）。_100% = 1 秒。_
* **hit scale factor** – ノートがトリガーされたときにどれだけ拡大されるか（例：2 = 2 倍のサイズ）。
* **hit scale hold time** – ノートが拡大された状態を保ってから元に戻り始めるまでの時間。値は秒単位です（0–1）。_100% = 1 秒。_
* **hit scale decay time** – ノートが元のサイズに戻るまでの時間。値は秒単位です（0–1）。_100% = 1 秒。_
* **note off shrink time** – ノートをリリースした後、元のサイズに縮小して戻るまでの時間。値は秒単位です（0–1）。_100% = 1 秒。_（**leave all notes visible** が有効な場合は効果がありません。）

{% hint style="info" %}
スケーリング - コンテンツが単一のドットの場合、スケーリングは効果がありません。
{% endhint %}
