---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introdução

Liberation inclui um sistema DMX flexível e poderoso que permite criar efeitos de iluminação e controlar lasers compatíveis com DMX via Art-Net. Ele foi projetado para facilitar a sincronização da iluminação com o seu show de laser — sem precisar de uma mesa de luz separada.

{% hint style="info" %}
**O que é Art-Net e qual é a relação dele com DMX?**

**DMX** é um sistema usado há anos para controlar luzes, lasers, máquinas de fumaça e outros efeitos de palco. Ele envia sinais de controle por cabos especiais, geralmente com conectores XLR, e cada equipamento responde a um conjunto específico de canais para saber o que fazer.

**Art-Net** é uma forma mais recente de enviar esses mesmos dados DMX por uma rede de computadores comum. Em vez de usar cabos especiais, ele envia tudo por Ethernet, como o tráfego de internet ou de rede local.

No Liberation, toda a saída DMX é enviada usando Art-Net. Você pode usá-lo para controlar dispositivos compatíveis com Art-Net diretamente, ou pode conectar um **Art-Net node** — uma pequena caixa que converte Art-Net de volta para DMX padrão. Isso significa que você ainda pode controlar luzes e efeitos DMX tradicionais, mesmo que eles não tenham suporte a Art-Net.
{% endhint %}

Você também pode usá-lo para controlar diversos tipos de equipamentos de palco, como máquinas de fumaça, hazers, jatos de CO₂, máquinas de faísca fria e muito mais. Se o equipamento tiver suporte a DMX, você pode configurá-lo como uma zona DMX e acioná-lo diretamente pelo Liberation, junto com o seu conteúdo de laser.

Os equipamentos DMX são adicionados como **zonas DMX**, que aparecem na lista de zonas junto com suas zonas de feixes de laser e áreas de destino do Canvas. Cada zona DMX usa um **preset DMX**, que informa ao Liberation como mapear propriedades dos seus clips de laser — como posição, cor e brilho — para valores de canais DMX.

Quando você envia um clip para uma zona DMX, o Liberation analisa o primeiro elemento do clip e converte suas propriedades com base no preset. Isso facilita controlar luzes e efeitos DMX diretamente a partir dos mesmos clips que você já usa para lasers.

#### Liberation no Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

O primeiro teste real do sistema DMX do Liberation foi no Glastonbury 2023, onde a Reach Lasers instalou um total de 90 fontes de feixe como parte do palco “spider” da Arcadia.

18 lasers foram controlados com Ether Dreams internos, e outras 12 barras de feixes com 6 cabeças foram controladas via Art-Net e DMX.
