---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Atribuição de controladores

Depois de configurar os lasers no Liberation, você pode atribuir cada um deles a um controlador de laser no mundo real. (Consulte [lasers e controladores compatíveis](../hardware/compatible-lasers-and-controllers-dacs.md) para verificar quais hardwares você pode usar). Os controladores serão conectados por USB ou pela rede.

* Abra o painel _Controller Assignment_ pela opção de menu _View -> Controller Assignment_. (Como alternativa, você também pode usar o botão _ASSIGN LASER CONTROLLERS_ no painel _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Painel Controller Assignment"><figcaption></figcaption></figure>

* O painel é dividido em duas partes: uma lista de lasers à esquerda e a lista de controladores disponíveis à direita. Se você não vir seu controlador de laser na lista, pressione o botão _REFRESH_. Se continuar tendo problemas, consulte [solução de problemas](../troubleshooting/).
* Para atribuir um controlador a um laser, clique e arraste da direita para um slot de laser livre à esquerda. Isso informa ao Liberation qual controlador ele deve usar para cada laser. (Se mudar de ideia, você pode arrastar os controladores livremente para cima e para baixo, de um laser para outro.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Lista de controladores" width="375"><figcaption></figcaption></figure>

* Se você vir um quadrado verde ao lado do controlador, isso significa que o Liberation se conectou a ele com sucesso.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Um Ether Dream e um Helios DAC atribuídos aos lasers 2 e 3, respectivamente</p></figcaption></figure>

{% hint style="info" %}
Observe que sempre que você se conectar a um controlador, o laser será desarmado automaticamente.
{% endhint %}

* Um quadrado laranja 🟧 significa que o controlador está com problemas intermitentes de conexão. Isso geralmente é causado por um problema de rede; consulte [solução de problemas](../troubleshooting/).
* Um quadrado vermelho 🟥 significa que o controlador não pode ser acessado; consulte [solução de problemas](../troubleshooting/).
* O _disconnect button_ (X) desconecta o controlador, mas não remove a atribuição dele ao laser. Depois, você pode usar o _reconnect button_ (ícone de seta de atualização) para reconectá-lo ou clicar no _disconnect button_ novamente para remover a atribuição.
* _Recurso avançado:_ abra o painel de análise do controlador clicando no botão que parece um gráfico. Este é um recurso avançado que fornece informações detalhadas sobre o fluxo de dados e pode ajudar na solução de problemas. (Esta opção pode não estar disponível para alguns tipos de controlador.)
* Você pode usar o _rename button_ (lápis) para renomear este controlador como quiser. Faz sentido dar um nome que facilite associá-lo a um hardware específico. Se ele estiver integrado a um laser, você pode nomeá-lo de acordo, por exemplo _LaserCube Ultra #1_ ou _Triton T5 #3._ Esses nomes serão salvos na sua instalação do Liberation e aparecerão a partir de agora; isso pode ajudar bastante a identificar rapidamente seus lasers.

{% hint style="info" %}
Dica profissional: dê **dois cliques** em um controlador à direita para atribuí-lo automaticamente ao próximo laser disponível à esquerda. Isso pode economizar bastante tempo se você tiver muitos lasers para atribuir!
{% endhint %}

Você pode usar os botões _DISCONNECT ALL_ e _RECONNECT ALL_ para redefinir rapidamente todas as conexões. Isso é útil se você estiver com problemas de rede.
