---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 DMXゾーンの作成

1. Art-Net nodeを接続し、[Art-Net nodeへの接続](../connecting-to-an-artnet-node.md "mention")の手順に従って設定します。
2. **DMX Zones** を開き、**ADD DMX ZONE** をクリックします。
3. zoneの **Node**、**Universe**、**Address** を、フィクスチャーに合わせて設定します。
4. フィクスチャー用の **Preset** を選択します。プリセットでは、どのDMXチャンネルが固定値、コンテンツのオン/オフ値、RGBカラー、X/Y位置、明るさ、または明示的なDMX Value入力を受け取るかを定義します。
5. **Edit DMX profile/channel mapping**（スライダーアイコン）をクリックして、チャンネルマッピングを編集します。デフォルトのプリセットは、コンテンツのオン/オフチャンネルとRGBカラーチャンネルから始まります。
6. beam zoneやcanvas zoneに割り当てる場合と同じ方法で、ClipをDMX zoneに割り当てます。
7. zoneからDMXを出力する準備ができたら、**ARM** を押します。

{% hint style="warning" %}
アームされたDMX zoneだけがライブ値を送信します。アームされていないDMX zoneは、マッピングされたチャンネルをゼロにクリアします。これはフィクスチャーの設定中により安全です。
{% endhint %}

DMX出力は、ライセンス階層によっても制限されます。**ARM** ボタンが無効になっている場合は、お使いの階層にDMX出力が含まれているか、またはアーム可能なDMX zoneの最大数にすでに達していないかを確認してください。
