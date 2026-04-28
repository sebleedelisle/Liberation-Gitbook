---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

各 _Creator_ ノードには _Render Profile_ 設定があり、レーザーでシェイプをどのように描画（_render_）するかを決定します。

**ほとんどの用途では、**_**DEFAULT**_** 設定でまったく問題ありません**。ただし、グラフィックや複雑なコンテンツを扱う場合は、各シェイプの描画方法をより細かく制御したくなることがあります。

{% hint style="info" %}
多くのレーザーソフトウェアとは異なり、Liberation はレーザーコントローラーへ渡す直前に、リアルタイムでポイントストリームを生成します。これにより、ディスク容量を大幅に節約できます。クリップは、事前レンダリングされたポイントストリームのように MB 単位ではなく、数 kB 程度です。

また、クリップ自体を変更せずに、同じコンテンツをレーザーごとに異なるスキャナータイプへ合わせて調整できます。

詳しくは [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention") を参照してください。
{% endhint %}

プリセットの _Render Profiles_ には、_DEFAULT_、_FAST_、_DETAIL_ の 3 つがあります。

_**DEFAULT**_ - ほとんどの用途に適した、汎用性の高いプロファイルです。

_**FAST** -_ クリップに多くのコンテンツが含まれていて、その一部が非常にシンプルな点や直線だけの場合、このオプションを選ぶとちらつきが少なくなることがあります。

_**DETAIL**_ - 鋭い角が必要な図形を描画する場合は、このオプションを使用します。ただし、スキャナーの動きが遅くなるため、出力がちらつきやすくなる点に注意してください。

{% hint style="info" %}
Clip editor 内では、Creator を異なる Render Profile に割り当てられますが、各レーザーはスキャナー設定に応じてこれらのプロファイルを処理します。詳しくは [scanner-presets.md](../../advanced/scanner-presets.md "mention") を参照してください。
{% endhint %}
