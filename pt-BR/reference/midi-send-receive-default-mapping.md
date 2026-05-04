---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Mapeamento padrão de envio/recebimento MIDI

**Clip on e off são acionados por MIDI note on / off nos canais 1 a 14**

Os Clips têm uma posição horizontal (x) e vertical (y). Clique com o botão direito em um Clip para ver sua posição. O MIDI pode acionar Clips começando em 0,0.

{% hint style="info" %}
Observe que o controle de clipes com este sistema é absoluto, e as posições dos clipes não mudam quando você rola o Clip Deck.
{% endhint %}

No canal MIDI 1, a nota 1 corresponde ao Clip 0,0; a nota 2 ao Clip 0,1; a nota 3 ao Clip 0,2, descendo pelas linhas e avançando pelas colunas. Quando chega a 128, ele passa para o próximo canal e recomeça. Assim, você tem um total de 128 x 14 = 1792 Clips acessíveis via MIDI.

Nota MIDI para coordenadas de clipe:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nota : 1</td><td>Nota : 6</td><td>Nota : 11</td><td>Nota : 16</td><td>Nota : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nota : 2</td><td>Nota : 7</td><td>Nota : 12</td><td>Nota : 17</td><td>...etc</td></tr><tr><td><strong>y : 2</strong></td><td>Nota : 3</td><td>Nota : 8</td><td>Nota : 13</td><td>Nota : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nota : 4</td><td>Nota : 9</td><td>Nota : 14</td><td>Nota : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nota : 5</td><td>Nota : 10</td><td>Nota : 15</td><td>Nota : 20</td><td></td></tr></tbody></table>

Observe que um evento MIDI note on inicia o clipe, e o evento note off equivalente para o clipe. Isso independe do modo de acionamento do grupo. O sistema foi originalmente projetado para reprodução e gravação, então fazer as notas alternarem o estado de um clipe não seria desejável.

### **Efeitos**

Mensagens MIDI control change (CC) no **canal 15** ajustam os efeitos.\
O efeito 1 usa CC 0-3, valor 0-127\
O efeito 2 usa CC 4-7, valor 0-127\
O efeito 3 usa CC 8-11, valor 0-127\
… e assim por diante.

Cada grupo de quatro controla o nível e 3 parâmetros desse efeito:

<table><thead><tr><th width="164">Efeito :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Nível</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parâmetro 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...etc</td></tr><tr><td><strong>Parâmetro 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parâmetro 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Configurações globais**

Mensagens MIDI control change no **canal 16** alteram as configurações globais:\
CC 1 : Shift X (horizontal) 0 -127, 64 fica no centro\
CC 2 : Shift Y (vertical) 0 -127, 64 fica no centro\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

E, muito importante:\
CC 15 : Global brightness

Observe que este sistema foi originalmente projetado para gravação e reprodução, permitindo que você use Logic, Ableton ou outra DAW para criar animações em timeline. Embora você possa usá-lo para controle ao vivo, ele não foi otimizado para esse uso, e algumas funções de controle ao vivo estão ausentes em comparação com a configuração do APC40.
