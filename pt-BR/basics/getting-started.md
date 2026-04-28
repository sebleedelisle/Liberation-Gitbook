# ✅ Guia de início rápido

## Introdução

Bem-vindo ao **Liberation** — a próxima geração de software para shows de laser.

O Liberation é um software moderno, poderoso e complexo; ele foi criado com base em princípios de usabilidade e confiabilidade para dar a você liberdade para expressar sua criatividade. Ele é rápido, eficiente e fluido; siga este _Guia de início rápido_ para começar a usar em poucos minutos!

### Gerenciamento de lasers

O Liberation é flexível o suficiente para você configurar e visualizar lasers mesmo sem nenhum laser real conectado. Depois, quando estiver tudo pronto, você pode atribuir cada saída a um controlador de laser de forma integrada.

{% hint style="info" %}
Você pode configurar e visualizar quantos lasers quiser dentro do Liberation. Os níveis de licença (Hobbyist, Pro etc.) limitam apenas o número de lasers que você pode _armar_. Isso significa que você pode criar shows de laser com 100 lasers mesmo usando uma licença gratuita. Você só precisa fazer upgrade quando for realmente executar o show em lasers reais.
{% endhint %}

Por padrão, há 8 lasers distribuídos horizontalmente, mas você pode personalizar isso como quiser. Provavelmente é melhor manter esse padrão enquanto você se familiariza com o software e, depois, ajustá-lo para corresponder à sua configuração de hardware. (Veja [setting-up-your-project.md](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Importante: antes de armar qualquer laser, entenda os riscos envolvidos e leia com atenção o capítulo [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

## Visão geral do software

### Desligamento de segurança

Sempre que você estiver operando lasers, deve ter um **botão físico de parada de emergência** à mão (veja [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md)). Mas, se quiser desarmar tudo com menos urgência, você pode usar o botão _**DISARM ALL**_ ou a tecla `Escape` (ou a tecla _**SESSION**_ no APC40). Você também pode reduzir o brilho global usando o controle deslizante na tela ou o fader principal no APC40.

### Controles deslizantes

Em todo o Liberation há vários controles deslizantes e controles.

{% hint style="info" %}
Clique com `Cmd / Ctrl` em um controle deslizante para digitar um novo valor se precisar de mais controle do que o slider oferece.
{% endhint %}

### Atalhos de teclado

Uma lista completa de atalhos de teclado pode ser encontrada aqui: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md)

### Layout da tela

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Não tem certeza do que um botão específico faz? Passe o mouse sobre ele para ver uma descrição!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

O menu é onde você encontra todas as opções de importação/exportação de arquivos e abre painéis. Você também encontra aqui a opção para autorizar o computador com sua assinatura (em _Liberation -> Authorise/Deauthorise this computer_).

#### Barra de ícones

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Tarefas comuns ficam aqui, como armar/desarmar todos os lasers, ajustar o brilho global, ativar o test pattern e alternar entre as visualizações 3D, Canvas e Output.

### Visualizações

A grande área no canto superior esquerdo da tela pode mostrar uma de 3 visualizações principais: **3D**, **CANVAS** e **OUTPUT.** Alterne entre elas usando os botões da barra de ícones (ou use a tecla `Tab` para alternar entre as visualizações 3D e OUTPUT e, em seguida, continuar alternando por cada saída de laser em sequência).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Visualização 3D

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

A visualização 3D mostra como seus lasers vão aparecer e pode ser configurada para corresponder à sua própria montagem de lasers. Clique e arraste para girar a câmera; use a roda do mouse para avançar e recuar. Você encontra muitas outras opções no painel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Veja [3d-visualiser.md](../setting-up/3d-visualiser.md).

#### Visualização Output

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

A visualização Output é usada para configurar zonas e máscaras para cada laser. (Observe o número enorme no canto superior esquerdo para você ver facilmente em qual laser está!)

Esta visualização representa toda a saída desse laser e onde cada zona fica dentro dela. Por padrão, há apenas uma zona por laser, mas você pode adicionar quantas zonas forem razoavelmente práticas, e verá todas elas nesta visualização.

{% hint style="info" %}
**O que é uma zona?**

Uma zona é um espaço dentro da saída de um laser para o qual você pode direcionar conteúdo de laser. Você pode ter mais de uma zona por laser. O tipo mais simples de zona é uma zona de _beam_, mas também existem zonas de _canvas_ e zonas de _DMX_. Neste guia, vamos nos concentrar principalmente nas zonas de beam, que geralmente são usadas para criar efeitos atmosféricos de feixes no ar.
{% endhint %}

Você pode selecionar o laser que deseja editar usando:

* os botões numerados na barra superior
* pressionando a tecla numérica do laser desejado _(teclas 1-9)_
* a tecla `Tab` para percorrer um laser após o outro

Adicione um novo laser à configuração pressionando o botão _+_. (Também há um botão _ADD LASER_ no painel _Laser Overview_)

Exclua um laser da configuração pressionando o botão vermelho ⊖ no painel _Laser Overview_.

Você pode ampliar e reduzir usando a roda de rolagem do mouse, além de clicar e arrastar em qualquer área onde não haja uma zona para mover a visualização.

Clique em uma zona para selecioná-la e então ajuste seus pontos de canto com o mouse. Use a tecla `Alt / Option` enquanto arrasta um canto para torná-lo não uniforme. Clique com o botão direito na zona para ver mais opções, incluindo alterar o tipo de zona.

À esquerda há uma barra com uma série de botões de ícones; passe o mouse sobre qualquer botão para ver uma descrição do que ele faz. Os botões aqui permitem adicionar zonas de beam, zonas de canvas e máscaras. Também há opções para definir um test pattern apenas para este laser, junto com configurações de grade e encaixe.

Para mais detalhes, veja [output-view](../output-view/).

#### Canvas

O sistema Canvas é usado principalmente para gráficos e mapeamento arquitetônico. Você pode distribuir imagens complexas por vários lasers e corrigir a perspectiva de cada seção. Veja [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/).

### Controlador MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Embora seja possível controlar o Liberation usando mouse e teclado, é muito melhor usar uma interface de controle MIDI APC40 (a Mark 2 é a melhor, mas a Mark 1 também funciona).

Veja também: [apc40-reference.md](../reference/apc40-reference.md)

Agora também implementamos suporte ao APC Mini Mark 2 e ao MIDI Fighter Twister, e há outros em desenvolvimento. Mas o APC40 Mark 2 é a melhor opção na maioria dos casos.&#x20;

### Clips e efeitos

{% hint style="info" %}
**O que é um clip?**

Um clip é um contêiner para qualquer conteúdo de laser dentro do Liberation. Clips podem conter beams ou animações gráficas e geralmente são um ciclo em loop. Eles podem ser direcionados para qualquer zona (ou _Canvas target area_) e são disparados usando os botões de clip dentro do clip deck.
{% endhint %}

#### Visão geral do clip deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Esta grade é conhecida como _clip deck_ e é onde todos os clips de laser ficam armazenados. Ela foi projetada para corresponder diretamente à grade de botões 8 x 5 do seu APC40.

**Navegação no clip deck.**

Você pode rolar o clip deck para a esquerda e para a direita usando:

* Teclas de seta esquerda e direita. Adicione `Cmd / Ctrl` para rolar uma página inteira por vez.
* Trackpad: deslize
* Mouse: se o seu mouse tiver rolagem lateral, você pode usá-la enquanto o ponteiro estiver sobre o clip deck
* Knob de rolagem do APC40
* Botões APC40 _<- DEVICE ->_

Para ajudar você a se orientar, há um mini visualizador do clip deck na parte superior. Veja também [clips](../clips/)

#### Iniciando e parando clips

Pressione um botão de clip (com o mouse ou com o APC40) para iniciar um clip. Pressione novamente para pará-lo. Quando você inicia um clip, todos os outros clips da mesma cor param automaticamente, a menos que você segure _shift_.

Alguns clips estarão em _Flash mode_ (por padrão, os vermelhos); nesse caso, eles param assim que você solta o botão do clip.

O botão _STOP_ para todos os clips em execução no momento.

#### Definindo zonas de saída para o clip

Abaixo dos botões de clip, você verá os botões de zona, zonas de beam 1 a 8 por padrão (_BEAM 1_, _BEAM 2_ etc.). Os botões de zona acendem para indicar quais zonas estão atribuídas ao clip selecionado no momento.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Duas linhas abaixo dos botões de zona, você verá os botões de inversão X/Y; alterne esses botões para inverter o clip horizontal e verticalmente.

{% hint style="info" %}
Observe que essas alocações de zona e configurações de inversão X/Y estão conectadas ao próprio clip; elas são mantidas na próxima vez que você executar esse clip. Elas não são uma configuração global.
{% endhint %}

Clique com o botão direito em um clip para editar mais configurações do clip. Veja também [clip-settings.md](../clips/clip-settings.md)

### Grupos

Você perceberá que cada clip tem um contorno colorido, e essa cor representa a qual _grupo_ ele pertence. Os botões de clip do APC40 também acendem nessa cor.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grupo 1</td><td>Ciano</td></tr><tr><td>Grupo 2</td><td>Laranja</td></tr><tr><td>Grupo 3</td><td>Vermelho</td></tr><tr><td>Grupo 4</td><td>Índigo</td></tr><tr><td>Grupo 5</td><td>Verde</td></tr></tbody></table>

O sistema de grupos é muito flexível e permite que você:

* Mantenha clips de um grupo em execução enquanto alterna clips de outro grupo
* Atribua rapidamente zonas e inversões X/Y a todos os clips dentro de um grupo
* Defina _Flash mode_ para um clip (o Grupo 3 vem configurado em _Flash mode_ por padrão)

Os grupos também têm configurações de transição de entrada/saída que podem ser herdadas pelos clips ou substituídas.

Você pode atribuir o grupo do clip usando os botões no menu de clique direito ou, usando o APC40, pode pressionar o botão do grupo e, _enquanto ele ainda estiver pressionado_, pressionar os botões de clip.

Alterar configurações de zona para todos os clips dentro de um grupo

Usando o APC40, pressione o botão do grupo e, _enquanto ele ainda estiver pressionado_, use os botões de zona e X/Y para alternar as configurações de zona de todos os clips desse grupo.

Veja também [groups.md](../clips/groups.md)

### Efeitos

O sistema de efeitos do Liberation é uma forma poderosa e versátil de alterar a saída do clip em tempo real. Os botões de efeitos padrão 1-8 ficam abaixo dos botões de zona.

#### Aplicando um efeito

Pressione um botão de efeito para alternar o efeito ou, melhor ainda, use os sliders 1-8 do APC40 para fazer fade dos efeitos para dentro e para fora.

#### Parâmetros de efeito

Use os controladores rotativos 1-8\* para ajustar o _parâmetro_ de cada efeito. (Ou você pode clicar com o botão direito com o mouse para ajustar o nível e o parâmetro). A alteração do parâmetro faz coisas diferentes dependendo de como o efeito está configurado. Veja a lista abaixo para os efeitos padrão.

{% hint style="info" %}
Os números pequenos que você vê nos botões de efeito se referem ao _nível_ e ao _parâmetro_ do efeito. O _nível_ é controlado pelo fader no APC40, ou você pode clicar e arrastar no botão. O parâmetro é ajustado pelos rotativos no APC40, ou você pode clicar com o botão direito para ajustar com o mouse.
{% endhint %}

_\*Os controladores rotativos 1-8 ficam na parte superior de um APC40 Mk2 e no canto superior direito no Mk1. Veja também:_ [apc40-reference.md](../reference/apc40-reference.md)

#### Os efeitos padrão

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Aplica um movimento caótico à saída do clip. O parâmetro ajusta a quantidade/velocidade do caos.
2. **Sine wave** :\
   Distorce todo o conteúdo em uma onda senoidal em movimento. O parâmetro ajusta o comprimento de onda.
3. **Rotation** :\
   Gira tudo. O parâmetro ajusta a velocidade de rotação.
4. **Horizontal flip** :\
   Comprime e estica tudo horizontalmente. O parâmetro ajusta a velocidade.
5. **Scale** :\
   Redimensiona tudo repetidamente de tamanho máximo até zero. O parâmetro ajusta a velocidade.
6. **Hue** :\
   Altera o matiz de tudo, mas não altera a saturação (ou seja, qualquer coisa branca continua branca). O parâmetro ajusta o matiz.
7. **Saturation and hue** :\
   Altera o matiz de tudo e também satura totalmente a cor (ou seja, qualquer coisa branca muda para a cor). O parâmetro ajusta o matiz.
8. **Flash** :\
   Faz o brilho de tudo piscar repetidamente de máximo até zero. O parâmetro ajusta a velocidade do flash.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Há mais 16 efeitos de cor na linha inferior para aplicar valores predefinidos de matiz e saturação.

Observe que estes são os efeitos padrão, mas eles podem ser editados para fazer praticamente o que você quiser!

#### O que é o _"currently selected clip"_?

Quando você inicia um clip, ele acende para mostrar que está ativo. Ele também fica com um contorno branco ao redor, indicando que este é o clip _selecionado_ no momento. Sempre que você alterna botões de zona ou ajusta as configurações do clip, essas alterações são aplicadas ao _clip selecionado no momento._

{% hint style="info" %}
Para selecionar um clip sem dispará-lo, pressione a tecla `Alt / Option` antes de pressionar o botão do clip. Esta é uma boa forma de ajustar suas zonas e outras configurações sem executá-lo.
{% endhint %}

### Painel Clip Settings

Use o painel _Clip Settings_ para editar escala, posição X/Y e acessar o poderoso sistema de atraso de zonas.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Painel Global Settings

Encontre o painel _Global Settings_ para ajustar configurações globais de saída que afetam toda a saída em todas as zonas.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Ative AUTO RESET para redefinir automaticamente todas as _Global settings_ sempre que nenhum clip estiver em execução.&#x20;

### Tempo

Quase todas as apresentações de laser têm algum tipo de trilha musical, então o sistema de tempo do Liberation é baseado em um andamento em batidas por minuto. No _Tempo Panel_, você pode ver uma representação do tempo; cada quadrado representa uma batida e você pode vê-los piscando no ritmo.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Há várias opções de sincronização, incluindo MIDI clock e Ableton Link. Se você souber o tempo da música, pode ajustá-lo manualmente usando o controle deslizante na tela ou o knob Tempo do APC40, mas também pode acompanhar a música usando o sistema _Tap Tempo_\_:\_

#### Tap Tempo

_Tap Tempo_ é um termo muito usado em aplicativos de música e permite que você marque o tempo junto com a batida para definir o andamento enquanto a música toca. Você pode usar o botão na tela, embora seja recomendado usar a tecla _T_ ou o botão _Tap Tempo_ no APC40 (ou até mesmo um pedal, se preferir).

Pressione a tecla _R_ ou o botão _Metronome_ (APC40) para reiniciar o tempo no início do compasso.

Pressione a tecla _Y_ ou gire o knob _Tempo_ (APC40) para arredondar o tempo para um número inteiro. Isso pode ser útil para música eletrônica, que tende a ter um número inteiro de batidas por minuto.

### Organizando seu clip deck

Para mover um clip no seu clip deck, clique e arraste-o para uma nova posição. Enquanto arrasta, você pode usar as teclas de cursor (ou a roda/botões de rolagem no seu APC40) para rolar para a esquerda e para a direita.

Pressione a tecla `Alt / Option` enquanto arrasta para fazer uma cópia.

Clique com `Alt / Option` em um clip para selecioná-lo sem iniciá-lo.

Clique com `Alt / Option + Shift` em um clip para multisselecionar, ou clique e arraste fora de um clip para fazer uma seleção por "laço".&#x20;

Clicar e arrastar vai arrastar TODOS os clips selecionados.

Para excluir um ou mais clips, arraste-os para fora do clip deck (um ícone de lixeira aparecerá) ou use o botão DELETE no menu de clique direito do clip.

### Painel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

O painel _Laser Overview_ oferece uma visão rápida do status dos lasers em execução no momento. O quadrado verde à direita mostra que o controlador de laser está funcionando corretamente. Se ficar laranja, há quedas ocasionais; se ficar vermelho, ele foi desconectado. Se ficar cinza, então não está conectado a nenhum controlador.&#x20;

O gráfico no meio mostra o histórico de duração dos frames, e o número à direita é a taxa de frames atual. Quanto mais complexo for o conteúdo, menor será a taxa de frames (ou seja, mais tremulação). Qualquer valor abaixo de cerca de 25fps começará a parecer um pouco tremido.&#x20;

### Conectando a lasers — painel Controller Assignment

Clique no botão _Assign Laser Controllers_ para abrir o painel _Controller Assignment_. (Esse painel também pode ser acessado por _View -> Controller Assignment_ na barra de menu).

Aqui você pode escolher quais saídas de laser vão para quais controladores de laser. Arraste e solte controladores da lista à direita para os slots à esquerda. Você pode renomear seus controladores para corresponder ao laser com o qual estão pareados (use o botão com ícone de caneta).

Leia o capítulo [controller-assignment.md](../setting-up/controller-assignment.md) para mais detalhes.

{% hint style="danger" %}
Antes de armar qualquer laser, leia o capítulo [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

### Painel Laser Output

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Este painel mostra as configurações do _laser selecionado no momento_ (representado pelo número na parte superior). Altere qual laser está selecionado usando a tecla _tab_, pressionando uma tecla numérica, clicando em um número de laser no painel _Laser Overview_ ou na _visualização Output._

* **Number button** arma e desarma o laser; se estiver vermelho, o laser está armado.
* **Brightness** ajusta o brilho do laser independentemente dos outros lasers (e é combinado com a configuração de _global brightness_ — ou seja, se ambos estiverem em 50%, seu laser ficará em 25%).
* **Test Pattern** ativa um test pattern apenas para este laser (sobrepõe a configuração global de test pattern)
* **Orientation** corrige lasers montados de lado ou de cabeça para baixo.
* **Flip Horizontal and Flip Vertical** inverte a saída do laser. Útil para correção de saída em lasers com fiação inconsistente.
* **Copy Laser Settings** abre um painel que permite copiar várias configurações deste laser para outros.

### Configurações de scanner

Lasers de show funcionam movendo um único feixe de laser extremamente rápido e ligando/desligando esse feixe para desenhar formas no ar. O que você vê como linhas, formas e imagens é, na verdade, o feixe traçando caminhos mais rápido do que seus olhos conseguem acompanhar.

Um fluxo de pontos é o conjunto de dados que informa ao laser para onde se mover em seguida e quando o feixe deve estar ligado ou desligado. No Liberation, os clips são convertidos nesse fluxo de pontos em tempo real à medida que são enviados para os lasers.

O Liberation oferece controle detalhado sobre como esse fluxo de pontos é gerado, permitindo equilibrar suavidade, brilho e desempenho para cada laser.

{% hint style="info" %}
Se você está acostumado com softwares de laser mais antigos que dependem de fluxos de pontos pré-calculados, essa abordagem pode parecer diferente no início. Porém, a geração de pontos em tempo real permite que o mesmo conteúdo seja otimizado de formas diferentes para cada laser. Isso facilita trabalhar com vários lasers que tenham velocidades ou qualidades de scanner diferentes, sem duplicar ou reconstruir conteúdo. Também mantém os arquivos de clip muito pequenos, por isso todo o clip deck padrão do Liberation tem apenas alguns megabytes, em vez de gigabytes.
{% endhint %}

As configurações básicas de scanner são:

* **Speed** é a velocidade do scanner, ou seja, a rapidez com que o laser se move para desenhar formas. Isso equivale a ajustar a taxa de pontos em softwares de laser tradicionais, mas no Liberation você pode alterar a velocidade de movimento do laser _independentemente da taxa de pontos._ Você não deve precisar ajustar isso.
* **Scanner sync** (às vezes conhecido como _blank shift_, anteriormente Colour Shift) Os scanners movem o laser muito rápido, mas normalmente a mudança de brilho e cor fica fora de sincronia com o movimento. Isso aparece como pequenas "caudas" tremulantes de luz na borda de beams e linhas. Use este ajuste para sincronizar movimento e cor entre si. Veja [laser-settings](../setting-up/laser-settings/)

As outras configurações avançadas de scanner são abordadas no capítulo [advanced](../advanced/).

### Zoning

Para um guia completo sobre configuração e zoning de lasers, veja: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
