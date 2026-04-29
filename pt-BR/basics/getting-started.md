# ✅ Guia de início rápido

## Introdução

Boas-vindas ao **Liberation** — a próxima geração de software para shows de laser.

O Liberation é um software moderno, poderoso e complexo; ele foi construído sobre fundamentos de usabilidade e confiabilidade para dar a você liberdade para expressar sua criatividade. Ele é rápido, eficiente e fluido; siga este _Guia de início rápido_ para começar a usar em pouco tempo!

### Gerenciamento de lasers

O Liberation é flexível o suficiente para você configurar lasers e visualizá-los sem ter nenhum laser real conectado. Depois, quando estiver tudo pronto, você pode atribuir cada Output a um laser controller de forma simples.

{% hint style="info" %}
Você pode configurar e visualizar quantos lasers quiser dentro do Liberation; os níveis de licença (Hobbyist, Pro etc.) limitam apenas o número de lasers que você pode colocar em _armed._ Isso significa que você pode criar shows de laser com 100 lasers mesmo com uma licença gratuita. Você só precisa fazer upgrade quando for realmente executar o show em lasers reais.
{% endhint %}

O padrão vem com 8 lasers distribuídos horizontalmente, mas você pode personalizar isso como quiser. Provavelmente é melhor manter esse padrão enquanto você está conhecendo o software e, depois, ajustar para corresponder à sua configuração de hardware. (Veja [Configuração do seu projeto](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Importante: antes de colocar qualquer laser em armed, entenda os riscos envolvidos e leia com atenção o capítulo [Configuração de lasers](../setting-up/setting-up-lasers.md).
{% endhint %}

## Visão geral do software

### Desligamento de segurança

Sempre que você estiver operando lasers, é obrigatório ter à mão um **botão físico de parada de emergência** (veja [Parada de emergência e interlocks](../hardware/emergency-stop-interlocks.md)). Mas, se você quiser colocar tudo em disarmed sem tanta urgência, use o botão _**DISARM ALL**_, a tecla `Escape` ou a tecla _**SESSION**_ no APC40. Você também pode reduzir o Global Brightness usando o controle deslizante na tela ou o fader principal no APC40.

### Controles deslizantes

Em todo o Liberation, há vários controles deslizantes e outros controles.

{% hint style="info" %}
Clique em um controle deslizante com `Cmd / Ctrl` pressionado para digitar um novo valor se precisar de mais controle do que o slider permite.
{% endhint %}

### Atalhos de teclado

Uma lista completa de atalhos de teclado pode ser encontrada aqui: [Atalhos de teclado](../reference/keyboard-shortcuts.md)

### Layout da tela

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Não sabe o que um botão específico faz? Passe o mouse sobre ele para ver uma descrição!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

O menu é onde você encontra todas as opções de importação/exportação de arquivos e abre painéis. Aqui também fica a opção para autorizar o computador com sua assinatura, em _Liberation -> Authorise/Deauthorise this computer_.

#### Barra de ícones

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Tarefas comuns ficam aqui, como colocar todos os lasers em armed/disarmed, ajustar o Global Brightness, ativar o test pattern e alternar entre as 3D, Canvas e Output views.

### Views

A grande área no canto superior esquerdo da tela pode mostrar uma das 3 views principais: **3D**, **CANVAS** e **OUTPUT.** Alterne entre elas usando os botões da barra de ícones ou use a tecla `Tab` para alternar entre as 3D e OUTPUT views e, em seguida, continuar passando por cada Output de laser em sequência.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D View

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

A 3D view mostra como seus lasers vão aparecer e pode ser configurada para corresponder à sua própria configuração de lasers. Clique e arraste para girar a câmera; use a roda do mouse para avançar e recuar. Você encontra várias outras opções no painel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Veja [Visualizador 3D](../setting-up/3d-visualiser.md).

#### Output View

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

A Output view é usada para configurar zones e masks para cada laser. (Observe o número enorme no canto superior esquerdo para você saber facilmente em qual laser está!)

Esta view representa todo o Output desse laser e mostra onde cada zone está posicionada dentro dele. Por padrão, existe apenas uma zone por laser, mas você pode adicionar tantas zones quanto for razoavelmente prático, e todas aparecerão nesta view.

{% hint style="info" %}
**O que é uma zone?**

Uma zone é um espaço dentro do Output de um laser para o qual você pode direcionar conteúdo de laser. E você pode ter mais de uma zone por laser. O tipo mais simples de zone é uma _beam_ zone, mas também existem _canvas_ zones e _DMX_ zones. Neste guia, vamos focar principalmente em beam zones, que normalmente são usadas para criar efeitos atmosféricos de feixes no ar.
{% endhint %}

Você pode selecionar o laser que quer editar de uma destas formas:

* usando os botões numerados na barra superior
* pressionando a tecla numérica do laser desejado _(teclas 1-9_ keys\_)\_
* usando a tecla `Tab` para percorrer de um laser para o próximo

Adicione um novo laser à configuração pressionando o botão _+_. (Também existe um botão _ADD LASER_ no painel _Laser Overview_)

Exclua um laser da configuração pressionando o botão vermelho ⊖ no painel _Laser Overview_.

Você pode aproximar e afastar usando a roda de rolagem do mouse e clicar e arrastar em qualquer área que não tenha uma zone para mover a view.

Clique em uma zone para selecioná-la e ajuste seus pontos de canto com o mouse. Use a tecla `Alt / Option` enquanto arrasta um canto para torná-lo não uniforme. Clique com o botão direito na zone para ver mais opções, incluindo alterar o tipo de zone.

À esquerda, há uma barra com uma série de botões de ícone; passe o mouse sobre qualquer botão para ver uma descrição do que ele faz. Os botões aqui permitem adicionar beam zones, canvas zones e masks. Também há opções para definir um test pattern apenas para este laser, além de configurações de grade e encaixe.

Para mais detalhes, veja [Visualização Output](../output-view/).

#### Canvas

O sistema Canvas é usado principalmente para gráficos e mapeamento arquitetônico. Você pode distribuir imagens complexas por vários lasers e corrigir a perspectiva de cada seção. Veja [Gráficos e o sistema Canvas](../graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Embora seja possível controlar o Liberation usando mouse e teclado, é muito melhor usar uma interface de controle MIDI APC40 (a Mark 2 é a melhor, mas a Mark 1 também funciona).

Veja também: [Referência do APC40](../reference/apc40-reference.md)

Agora também implementamos suporte para o APC Mini Mark 2 e o MIDI Fighter Twister, e mais controladores estão em desenvolvimento. Mas o APC40 Mark 2 é a melhor opção na maioria dos casos.&#x20;

### Clips e efeitos

{% hint style="info" %}
**O que é um Clip?**

Um Clip é um contêiner para qualquer conteúdo de laser dentro do Liberation. Clips podem conter beams ou animações gráficas e geralmente funcionam em loop. Eles podem ser direcionados para qualquer zone ou _área de destino do Canvas_ e são acionados usando os botões de Clip dentro do Clip Deck.
{% endhint %}

#### Visão geral do Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Esta grade é conhecida como _Clip Deck_ e é onde todos os Clips de laser ficam armazenados. Ela foi projetada para corresponder diretamente à grade de botões 8 x 5 do seu APC40.

**Navegação pelo Clip Deck.**

Você pode rolar o Clip Deck para a esquerda e para a direita usando:

* Teclas de seta para esquerda e direita. Adicione `Cmd / Ctrl` para rolar uma página inteira por vez.
* Trackpad: deslize
* Mouse: se o seu mouse tiver rolagem lateral, você pode usá-la enquanto o cursor estiver sobre o Clip Deck
* Knob de rolagem do APC40
* Botões _<- DEVICE ->_ do APC40

Para ajudar você a se orientar, há um minivisualizador do Clip Deck na parte superior. Veja também [Clips e Clip Deck](../clips/)

#### Iniciando e parando Clips

Pressione um botão de Clip, seja com o mouse ou com o APC40, para iniciar um Clip. Pressione novamente para pará-lo. Quando você inicia um Clip, todos os outros Clips da mesma cor param automaticamente, a menos que você segure _shift_.

Alguns Clips ficam em _Flash mode_ (por padrão, os vermelhos). Nesse caso, eles param assim que você solta o botão de Clip.

O botão _STOP_ para todos os Clips em execução no momento.

#### Definição das output zones do Clip

Abaixo dos botões de Clip, você verá os botões de zone, beam zones 1 a 8 por padrão (_BEAM 1_, _BEAM 2_ etc.). Os botões de zone acendem para indicar quais zones estão atribuídas ao Clip selecionado no momento.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Duas linhas abaixo dos botões de zone, você verá os botões de inversão X/Y; ative-os para inverter o Clip horizontal e verticalmente.

{% hint style="info" %}
Observe que essas alocações de zone e configurações de inversão X/Y estão ligadas ao próprio Clip; elas serão mantidas na próxima vez que você executar esse Clip. Elas não são uma configuração global.
{% endhint %}

Clique com o botão direito em um Clip para editar mais configurações dele. Veja também [Configurações de Clip](../clips/clip-settings.md)

### Grupos

Você vai notar que cada Clip tem um contorno colorido, e essa cor representa em qual _grupo_ ele está. Os botões de Clip do APC40 também acendem nessa cor.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Ciano</td></tr><tr><td>Group 2</td><td>Laranja</td></tr><tr><td>Group 3</td><td>Vermelho</td></tr><tr><td>Group 4</td><td>Índigo</td></tr><tr><td>Group 5</td><td>Verde</td></tr></tbody></table>

O sistema de grupos é muito flexível e permite que você:

* mantenha Clips de um grupo em execução enquanto alterna Clips de outro grupo
* atribua rapidamente zones e inversões X/Y a todos os Clips de um grupo
* defina _Flash mode_ para um Clip (o Group 3 vem configurado em _Flash mode_ por padrão)

Os grupos também têm configurações de transição de entrada/saída que podem ser herdadas pelos Clips ou sobrescritas.

Você pode atribuir o grupo de um Clip usando os botões no menu de clique direito ou, usando o APC40, pressionar o botão do grupo e, _enquanto ele ainda estiver pressionado,_ pressionar os botões de Clip.

Altere as configurações de zone de todos os Clips dentro de um grupo

Usando o APC40, pressione o botão do grupo e, _enquanto ele ainda estiver pressionado,_ use os botões de zone e X/Y para alternar as configurações de zone de todos os Clips desse grupo.

Veja também [Grupos de Clip](../clips/groups.md)

### Efeitos

O sistema de efeitos no Liberation é uma forma poderosa e versátil de alterar o Output do Clip em tempo real. Os botões de efeitos padrão 1-8 ficam abaixo dos botões de zone.

#### Aplicando um efeito

Pressione um botão de efeito para ativar ou desativar o efeito. Melhor ainda: use os sliders 1-8 do APC40 para fazer fade in e fade out dos efeitos.

#### Parâmetros de efeito

Use os rotary controllers 1-8\* para ajustar o _parâmetro_ de cada efeito. (Ou clique com o botão direito do mouse para ajustar o level e o parâmetro). A alteração do parâmetro faz coisas diferentes dependendo de como o efeito está configurado. Veja a lista abaixo para os efeitos padrão.

{% hint style="info" %}
Os números pequenos nos botões de efeito indicam o _level_ e o _parâmetro_ do efeito. O _level_ é controlado pelo fader no APC40, ou você pode clicar e arrastar no botão. O parâmetro é ajustado pelos rotaries no APC40, ou você pode clicar com o botão direito para ajustar com o mouse.
{% endhint %}

_\*Os rotary controllers 1-8 ficam na parte superior do APC40 Mk2 e no canto superior direito do Mk1. Veja também:_ [Referência do APC40](../reference/apc40-reference.md)

#### Os efeitos padrão

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Aplica um movimento caótico ao Output do Clip. O parâmetro ajusta a quantidade/velocidade do caos.
2. **Sine wave** :\
   Distorce todo o conteúdo ao longo de uma onda senoidal em movimento. O parâmetro ajusta o comprimento de onda.
3. **Rotation** :\
   Gira tudo. O parâmetro ajusta a velocidade de rotação.
4. **Horizontal flip** :\
   Comprime e estica tudo horizontalmente. O parâmetro ajusta a velocidade.
5. **Scale** :\
   Redimensiona tudo repetidamente de 100% até zero. O parâmetro ajusta a velocidade.
6. **Hue** :\
   Altera o matiz de tudo, mas não altera a saturação (ou seja, tudo que é branco continua branco). O parâmetro ajusta o matiz.
7. **Saturation and hue** :\
   Altera o matiz de tudo e também satura totalmente a cor (ou seja, tudo que é branco muda para a cor). O parâmetro ajusta o matiz.
8. **Flash** :\
   Faz o brilho de tudo piscar repetidamente de 100% até zero. O parâmetro ajusta a velocidade do flash.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Há mais 16 efeitos de cor na linha inferior para aplicar valores predefinidos de matiz e saturação.

Observe que estes são os efeitos padrão, mas eles podem ser editados para fazer quase qualquer coisa que você quiser!

#### O que é o _"Clip selecionado no momento"_?

Quando você inicia um Clip, ele acende para mostrar que está ativo. Ele também fica com um contorno branco, indicando que este é o Clip _selecionado_ no momento. Sempre que você alterna botões de zone ou ajusta as configurações do Clip, essas alterações são aplicadas ao _Clip selecionado no momento._

{% hint style="info" %}
Para selecionar um Clip sem acioná-lo, pressione a tecla `Alt / Option` antes de pressionar o botão de Clip. Essa é uma boa forma de ajustar suas zones e outras configurações sem executá-lo.
{% endhint %}

### Painel Clip Settings

Use o painel _Clip Settings_ para editar escala, posição X/Y e acessar o poderoso sistema de atraso por zone.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Painel Global Settings

Encontre o painel _Global Settings_ para ajustar configurações globais de Output que afetam todo o Output em todas as zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Ative AUTO RESET para redefinir automaticamente todas as _Global settings_ sempre que nenhum Clip estiver sendo reproduzido.&#x20;

### Timing

Quase todas as apresentações de laser têm algum tipo de trilha musical, então o sistema de timing do Liberation é baseado em um tempo em batidas por minuto. No _Tempo Panel_, você pode ver uma representação do tempo; cada quadrado representa uma batida, e você pode vê-los piscando no ritmo.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Há várias opções de sincronização, incluindo MIDI clock e Ableton Link. Se você souber o tempo da música, pode ajustá-lo manualmente usando o controle deslizante na tela ou o knob Tempo do APC40, mas também pode acompanhar o ritmo da música usando o sistema _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ é um termo comumente usado em aplicativos de música e permite que você marque o tempo tocando no ritmo da batida para definir o tempo enquanto a música está tocando. Você pode usar o botão na tela, embora seja recomendável usar a tecla _T_ ou o botão _Tap Tempo_ no APC40 (ou até um pedal, se preferir).

Pressione a tecla _R_ ou o botão _Metronome_ (APC40) para redefinir o tempo para o início do compasso.

Pressione a tecla _Y_ ou gire o knob _Tempo_ (APC40) para arredondar o tempo para um número inteiro. Isso pode ser útil para música eletrônica, que tende a ter um número inteiro de batidas por minuto.

### Organização do seu Clip Deck

Para mover um Clip no seu Clip Deck, clique e arraste-o para uma nova posição. Enquanto arrasta, você pode usar as teclas de seta ou a roda/botões de rolagem do APC40 para rolar para a esquerda e para a direita.

Pressione a tecla `Alt / Option` enquanto arrasta para fazer uma cópia.

Clique em um Clip com `Alt / Option` pressionado para selecioná-lo sem iniciá-lo.

Clique em um Clip com `Alt / Option + Shift` pressionado para selecionar vários, ou clique e arraste fora de um Clip para selecionar por "laço".&#x20;

Clicar e arrastar moverá TODOS os Clips selecionados.

Para excluir um ou mais Clips, arraste-os para fora do Clip Deck (um ícone de lixeira aparecerá) ou use o botão DELETE no menu de clique direito do Clip.

### Painel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

O painel _Laser Overview_ mostra rapidamente o status dos lasers em execução no momento. O quadrado verde à direita indica que o laser controller está funcionando bem. Se ficar laranja, há quedas ocasionais; se ficar vermelho, ele foi desconectado. Se estiver cinza, ele não está conectado a nenhum controller.&#x20;

O gráfico no meio mostra o histórico dos comprimentos de frame, e o número à direita é a taxa de frames atual. Quanto mais complexo for o conteúdo, menor será a taxa de frames (ou seja, mais tremido/instável ele parecerá). Qualquer coisa abaixo de cerca de 25 fps começará a parecer um pouco instável.&#x20;

### Conexão com lasers — painel Controller Assignment

Clique no botão _Assign Laser Controllers_ para abrir o painel _Controller Assignment_. (Esse painel também pode ser acessado pelo menu _View -> Controller Assignment_ na barra de menus).

Aqui você pode escolher quais Outputs de laser vão para quais laser controllers. Arraste e solte controllers da lista à direita para os slots à esquerda. Você pode renomear seus controllers para corresponder ao laser com o qual estão pareados usando o botão de ícone de caneta.

Leia o capítulo [Atribuição de controller](../setting-up/controller-assignment.md) para mais detalhes.

{% hint style="danger" %}
Antes de colocar qualquer laser em armed, leia o capítulo [Configuração de lasers](../setting-up/setting-up-lasers.md).
{% endhint %}

### Painel Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Este painel mostra as configurações do _laser selecionado no momento_ (representado pelo número na parte superior). Altere qual laser está selecionado usando a tecla _tab_, pressionando uma tecla numérica, clicando em um número de laser no painel _Laser Overview_ ou na _output view._

* **Number button** coloca o laser em armed ou disarmed; se estiver vermelho, o laser está armed.
* **Brightness** ajusta o brilho do laser independentemente dos outros lasers (e é combinado com a configuração de _global brightness_ — ou seja, se ambos estiverem em 50%, seu laser ficará em 25%).
* **Test Pattern** ativa um test pattern apenas para este laser (substitui a configuração global de test pattern)
* **Orientation** corrige lasers montados de lado ou de cabeça para baixo.
* **Flip Horizontal and Flip Vertical** inverte o Output do laser. Útil para correção de Output em lasers com fiação inconsistente.
* **Copy Laser Settings** abre um painel que permite copiar várias configurações deste laser para outros.

### Configurações de scanner

Lasers de show funcionam movendo um único feixe de laser em altíssima velocidade e ligando/desligando esse feixe para desenhar formas no ar. O que você vê como linhas, formas e imagens é, na verdade, o feixe traçando caminhos mais rápido do que seus olhos conseguem acompanhar.

Um fluxo de pontos é o conjunto de dados que informa ao laser para onde mover em seguida e quando o feixe deve ficar ligado ou desligado. No Liberation, Clips são convertidos para esse fluxo de pontos em tempo real enquanto são enviados aos lasers.

O Liberation oferece controle detalhado sobre como esse fluxo de pontos é gerado, permitindo equilibrar suavidade, brilho e desempenho para cada laser.

{% hint style="info" %}
Se você está acostumado com softwares de laser mais antigos que dependem de fluxos de pontos pré-calculados, essa abordagem pode parecer diferente no início. No entanto, a geração de pontos em tempo real permite que o mesmo conteúdo seja otimizado de formas diferentes para cada laser. Isso facilita trabalhar com vários lasers que têm velocidades ou qualidades de scanner diferentes, sem duplicar ou reconstruir conteúdo. Também mantém os arquivos de Clip muito pequenos, por isso todo o Clip Deck padrão do Liberation tem apenas alguns megabytes em vez de gigabytes.
{% endhint %}

As configurações básicas de scanner são:

* **Speed** é a velocidade do scanner, ou seja, a rapidez com que o laser se move para desenhar formas. Isso equivale a ajustar a taxa de pontos em softwares de laser tradicionais, mas no Liberation você pode alterar a velocidade de movimento do laser _independentemente da taxa de pontos._ Você não deve precisar ajustar isso.
* **Scanner sync** (às vezes conhecido como _blank shift, anteriormente Colour Shift_) Os scanners movem o laser muito rápido, mas geralmente a mudança de brilho e cor fica fora de sincronia com o movimento. Isso aparece como pequenas "caudas" de luz piscando nas bordas de beams e linhas. Use este ajuste para sincronizar o movimento e a cor. Veja [Configurações de laser](../setting-up/laser-settings/)

As outras configurações avançadas de scanner são abordadas no capítulo [Avançado](../advanced/).

### Zoning

Para um guia completo sobre configuração e zoning de lasers, veja: [Configuração de lasers](../setting-up/setting-up-lasers.md)
