---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ コントローラーの割り当て

Liberation 内でレーザーの設定が完了したら、次に各レーザーを実際のレーザーコントローラーに割り当てます。（使用できるハードウェアについては、[compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md) を参照してください）。コントローラーは、USB またはネットワーク経由で接続されます。

* _View -> Controller Assignment_ メニューから _Controller Assignment_ パネルを開きます。（または、_Laser Overview_ パネルの _ASSIGN LASER CONTROLLERS_ ボタンを使用することもできます。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment panel"><figcaption></figcaption></figure>

* パネルは 2 つに分かれており、左側にレーザーの一覧、右側に利用可能なコントローラーの一覧が表示されます。レーザーコントローラーが一覧に表示されない場合は、_REFRESH_ ボタンを押してください。それでも問題が解決しない場合は、[troubleshooting](../troubleshooting/) を参照してください。
* コントローラーをレーザーに割り当てるには、右側から左側の空いているレーザースロットへクリックしてドラッグします。これにより、どのコントローラーをどのレーザーに使用するかを Liberation に指定できます。（後で変更したい場合は、コントローラーをレーザー間で自由に上下へドラッグできます。）

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="List of controllers" width="375"><figcaption></figcaption></figure>

* コントローラーの横に緑の四角が表示されている場合、Liberation がそのコントローラーに正常に接続できていることを示します。

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream と Helios DAC が、それぞれレーザー 2 と 3 に割り当てられています</p></figcaption></figure>

{% hint style="info" %}
コントローラーに接続すると、レーザーは自動的にアーム解除されます。
{% endhint %}

* オレンジの四角 🟧 は、コントローラーで断続的な接続問題が発生していることを示します。通常はネットワークの問題が原因です。[troubleshooting](../troubleshooting/) を参照してください。
* 赤の四角 🟥 は、コントローラーに到達できないことを示します。[troubleshooting](../troubleshooting/) を参照してください。
* _disconnect button_（X）は、コントローラーとの接続を切断しますが、レーザーへの割り当ては解除しません。その後、_reconnect button_（更新矢印アイコン）を使用して再接続するか、もう一度 _disconnect button_ をクリックして割り当てを解除できます。
* _高度な機能：_ グラフのようなアイコンのボタンをクリックすると、コントローラー分析パネルを開けます。これは高度な機能で、データストリームに関する詳細情報を確認でき、問題のトラブルシューティングに役立ちます。（このオプションは、一部のコントローラータイプでは利用できない場合があります。）
* _rename button_（鉛筆）を使用して、このコントローラーに任意の名前を付けることができます。特定のハードウェアと簡単に関連付けられる名前にすると便利です。レーザーに内蔵されている場合は、_LaserCube Ultra #1_ や _Triton T5 #3_ のように、それが分かる名前にするとよいでしょう。これらの名前は Liberation のインストール環境に保存され、今後表示されます。レーザーをすばやく識別するのに非常に役立ちます。

{% hint style="info" %}
プロ向けヒント - 右側のコントローラーを **ダブルクリック** すると、左側の次に利用可能なレーザーへ自動的に割り当てられます。割り当てるレーザーが多い場合は、大きな時間短縮になります。
{% endhint %}

_DISABLE ALL_ ではなく、_DISCONNECT ALL_ と _RECONNECT ALL_ ボタンを使用すると、すべての接続をすばやくリセットできます。ネットワークの問題が発生している場合に便利です。
