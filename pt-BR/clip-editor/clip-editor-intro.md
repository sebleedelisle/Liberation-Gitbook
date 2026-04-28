---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introdução ao Clip Editor

O clip editor é uma forma versátil de criar conteúdo laser e está no centro do Liberation. É fácil criar coisas simples e, ao mesmo tempo, ele é flexível o suficiente para criar efeitos incrivelmente sofisticados e complexos.

{% hint style="info" %}
O editor baseado em nós foi a primeira parte do Liberation a ser criada! Ele nasceu de uma conversa com Rob Stanley em um encontro de laser no Reino Unido em 2018, sobre como seria um designer de conteúdo laser "orientado a objetos".

Embora pareça simples, é um sistema bastante complexo de construir, mas no início de 2019 eu já tinha uma demonstração funcional que comprovava o conceito — e foi isso que deu início a toda esta jornada!
{% endhint %}

É um editor visual baseado em nós (ou [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), que será familiar se você já usou produtos como TouchDesigner, MaxMSP ou VVVV. Embora o clip editor seja um pouco diferente e um pouco mais simples, pois foi projetado especificamente para gráficos vetoriais.

Você pode abrir o Clip Editor clicando com o botão direito no botão do clip e selecionando _EDIT CLIP_. Ou clique com o botão direito em um botão de clip vazio e selecione _CREATE AND EDIT CLIP_.

### Visão geral

O que você verá no clip editor:

* Os botões de nós **Creator** e **Operator** na parte superior
* Os botões de nós **Oscillator** à esquerda
* Uma prévia do conteúdo em um painel à direita e, se você clicar em um nó, verá uma segunda prévia que mostra o conteúdo no próprio nó.
* Todos os nós e conexões do clip que você está editando (se for um clip novo, isso estará vazio)
* O painel Clip Editor com várias opções

Enquanto você estiver editando, também verá a aparência do clip no 3D visualiser em segundo plano.

{% hint style="info" %}
Se você não vir nenhuma saída no 3D visualiser, talvez seja necessário usar os botões de zone para ativar as zones desejadas. Você também precisa garantir que _Preview to lasers_ esteja ativado; veja [#clip-editor-panel](clip-editor-intro.md#clip-editor-panel) abaixo.
{% endhint %}

### Criando um clip

Normalmente, você começa com um ou mais [nós Creator](creator-nodes.md) e conecta [Operators](operator-nodes/) da esquerda para a direita para processar o conteúdo. Ao mover Creators e/ou Operators próximos uns dos outros, você perceberá que eles se conectam automaticamente. E você pode arrastá-los para longe para desconectá-los novamente.

### Adicionando nós ao seu clip

Clique e arraste de um dos botões de nó na parte superior ou à esquerda para um espaço vazio dentro do clip editor.

### Ajustando as configurações de um nó

Clique no botão com ícone de engrenagem (no canto superior direito do nó) para abrir o painel de propriedades desse nó.

### Ativando e desativando um nó

Clique no botão com ícone de energia (no canto superior esquerdo do nó) para ativar e desativar o nó. O nó ficará esmaecido para indicar que não está ativo no momento. Observe que o conteúdo ainda passa por um Operator mesmo quando ele está desativado, mas o nó não afeta o conteúdo.

### Conectando nós entre si

O conteúdo é criado com um nó Creator e passa pelos nós da esquerda para a direita; cada Operator afeta o conteúdo de alguma forma e o passa para o próximo Operator. O que restar no fim do caminho será o conteúdo do clip. Creators e Operators são conectados automaticamente entre si quando você os aproxima. Para separá-los, arraste-os para longe novamente.

{% hint style="info" %}
Você pode conectar mais de um nó à entrada do próximo nó. Isso é útil para combinar várias partes de conteúdo
{% endhint %}

### Propriedades e sockets dos nós

Cada nó tem uma série de sockets na parte inferior, e cada um representa uma propriedade dentro do nó, como brilho, posição, escala, rotação etc.

[Nós Oscillator](oscillators/) podem ser conectados a esses sockets por baixo e usados para animar essas configurações. Nós Oscillator têm uma saída na parte superior; clique e arraste para puxar a conexão e soltá-la em um dos sockets de propriedade dos outros nós.

### Nós Oscillator

Nós Oscillator são usados para alterar propriedades ao longo do tempo. Normalmente, eles representam formas de onda, como dente de serra ou senoide, mas alguns nós Oscillator usam entradas externas (como o nível de entrada do microfone) como fonte.

{% hint style="info" %}
Se você já usou um sintetizador analógico, estará familiarizado com o conceito de osciladores, que são comumente usados para criar formas de onda ou ajustar o som ao longo do tempo. Os osciladores no Liberation fazem um trabalho parecido.

**Curiosidade:** o nome _Liberation_ foi inspirado no Moog Liberation, um sintetizador "keytar" lançado em 1980 e tornado famoso por Herbie Hancock, Jean-Michel Jarre e até James Brown!
{% endhint %}

Oscillators sempre têm configurações de _range_ que controlam o valor mínimo e máximo da propriedade a ser ajustada. E _Wave Oscillators_ sempre têm uma configuração de _duration_ que determina a velocidade com que o oscilador altera o valor. Veja [wave-oscillators.md](oscillators/wave-oscillators.md) para mais informações.

### Painel Clip Editor

* Timer — na parte superior do painel, você verá o tempo atual do clip à medida que ele avança
* _RETRIGGER_ — reinicia o clip desde o início; especialmente útil se o seu clip não estiver em loop
* _Preview to lasers_ — quando esta opção estiver marcada, você verá o 3D visualiser ser atualizado enquanto edita este clip. Se você desativá-la, verá quaisquer clips que estejam sendo executados fora do editor. Esta é uma configuração global, não por clip.
* _UNDO/REDO_ — para o próprio clip editor. Também mapeado para `Cmd / Ctrl + Z` e `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ — salva suas edições, mas avisa sobre sobrescrever
* _SAVE AS A COPY_ — salva seu clip no próximo slot disponível no clip deck. Essa passa a ser a nova posição do seu clip, e todos os salvamentos posteriores serão feitos nesse novo local.
* _EXIT EDITOR_ — fecha o clip editor. Se houver alterações não salvas, você verá um painel de confirmação.
