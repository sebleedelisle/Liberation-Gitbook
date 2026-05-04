---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Visão geral do Canvas

O sistema Canvas do Liberation é relativamente simples, mas pode parecer confuso no início. Aqui está uma visão geral conceitual para você começar.

{% hint style="info" %}
**Espere, eu preciso do sistema Canvas?**

Talvez não! Se você está apenas projetando um único gráfico em um único laser, é fácil fazer isso com uma beam zone (embora, por padrão, o conteúdo da beam zone seja espelhado horizontalmente, então você vai precisar aplicar X flip no clip).

Mas, se você quiser distribuir conteúdo gráfico entre mais de um laser, ou dividi-lo em seções diferentes para mapear em arquitetura, então o sistema Canvas resolve isso para você!
{% endhint %}

### Canvas

Antes de tudo, existe o Canvas em si. É o que você vê na visualização _CANVAS_ e representa um grande, bem, Canvas, onde você pode desenhar conteúdo em qualquer lugar dentro desse espaço.

### Áreas-alvo do Canvas

Elas aparecem como retângulos com contorno azul na visualização do Canvas e são áreas para as quais você pode enviar conteúdo. Você envia o conteúdo de um clip para uma área-alvo do Canvas da mesma forma que enviaria um clip para uma beam zone. Você verá os botões das áreas-alvo do Canvas à direita dos botões de beam zone no clip deck.

{% hint style="info" %}
Se você não conseguir ver os botões do Canvas no clip deck, tente rolar os botões de beam zone com `Shift + Left / Right Arrow`. Você deve ver um botão para cada área-alvo do Canvas, rotulado como _CANVAS 1, CANVAS 2_ etc.
{% endhint %}

### Zonas do Canvas

As zonas do Canvas são áreas dentro do Canvas que você escolhe enviar para um laser. Elas são representadas como retângulos com contorno rosa na visualização do Canvas. Você pode clicar com o botão direito em cada zona e selecionar os lasers aos quais ela deve ser atribuída. Se agora você mudar para a visualização _OUTPUT_ desse laser, verá que uma nova zona apareceu.

{% hint style="danger" %}
AVISO: se o laser estiver armado, você pode começar a projetar conteúdo de repente em uma zona padrão do Canvas. É melhor desarmar o laser antes de atribuir zonas do Canvas a ele.
{% endhint %}

{% hint style="info" %}
Você também pode atribuir uma zona do Canvas a um laser clicando no botão _add canvas zone_ na visualização _OUTPUT_. Consulte [Zonas](../output-view/zones.md "mention").
{% endhint %}

### Imagens-guia

Você pode adicionar uma imagem-guia ao Canvas e usá-la como modelo para seus gráficos. É recomendável ajustar a tonalidade de cor da imagem-guia (menu de clique direito) e escurecê-la para conseguir ver seu conteúdo sobre ela com mais facilidade.

{% hint style="info" %}
Para mapeamento arquitetônico, achei útil produzir um visual "desdobrado" do prédio, que representa todas as superfícies do edifício como uma imagem plana e sem distorção. A correção de perspectiva das várias seções pode ser feita usando a zona do Canvas na visualização _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Uma imagem-guia "achatada" do Saltwell Hall em Gateshead, Reino Unido</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>As zonas do Canvas em uma versão embrionária do Liberation (c2017!) Observe que os retângulos rosa escolhem qual parte do Canvas será exibida, e as visualizações de saída abaixo mostram para qual parte de cada laser essas zonas vão.</p></figcaption></figure>

### Canvas no 3D visualiser

Provavelmente seria trabalhoso (para dizer o mínimo) recriar seu sistema complicado de projeção com vários lasers no visualizador 3D! Então, em vez disso, você tem a opção de posicionar seu Canvas dentro do espaço 3D. Ative a caixa de seleção _Show canvas_ no painel _3D visualiser settings_. (Qualquer imagem-guia que você tenha no Canvas também aparecerá no visualizador.)

{% hint style="info" %}
Observe que o visualiser ainda mostrará as projeções do Canvas como efeitos atmosféricos vindos dos lasers. Você pode simplesmente movê-las para fora da visualização ou, se quiser caprichar, alinhá-las com o Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Pode ser extremamente satisfatório quando você alinha os feixes do laser com a imagem do Canvas no 3D visualiser!</p></figcaption></figure>
