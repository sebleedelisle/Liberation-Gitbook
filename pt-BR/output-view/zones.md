---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zonas

O principal tipo de zona que você vai usar na maioria dos seus projetos é a _Beam zone_. Essa zona foi criada para efeitos de feixes atmosféricos no ar. O outro tipo de zona é a _Canvas zone_ (veja [Gráficos e o sistema Canvas](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**AVISO — Tenha extremo cuidado ao mover zonas enquanto o laser estiver em funcionamento** e reduza o brilho para o menor nível possível. Veja [Visão geral do processo de configuração de lasers](../setting-up/setting-up-lasers.md) para um guia completo sobre como ativar e zonear lasers com segurança.
{% endhint %}

Você pode clicar e arrastar as zonas com o mouse. Ative um padrão de teste para ver para onde essa zona está indo.

{% hint style="info" %}
Use as teclas de seta para **deslocar levemente** a zona/ponto selecionado no momento. Pressione a tecla `Shift` para deslocar em passos maiores.
{% endhint %}

{% hint style="info" %}
Dica rápida: você pode copiar rapidamente as configurações de zona entre vários lasers! Veja [Copiar configurações entre lasers](../setting-up/copy-laser-settings.md)
{% endhint %}

### Adicionando uma nova beam zone

Clique no botão _Add a new beam zone_ na parte superior da barra de ferramentas e uma nova zona aparecerá. Observe que as beam zones são ordenadas na sequência em que você as adiciona, mas você pode reordená-las. Veja [Reordenando zonas de feixe](re-ordering-beam-zones.md)

### Adicionando uma canvas zone existente

Clique no botão _Add existing canvas zone_ e você verá uma lista das canvas zones disponíveis, podendo ativá-las ou desativá-las para este laser. Veja [Gráficos e o sistema Canvas](../graphics-and-the-canvas-system/)

### Tipos de formato de zona

Há 3 tipos de formato de zona:

* **Quad** — o formato padrão de zona retangular, que pode ser uniforme (alinhado aos eixos) ou distorcido. Ideal para zonas retangulares maiores ou canvas zones que exigem correção de perspectiva.
* **Line/Curve** — uma zona definida por 2 ou mais pontos e uma espessura. Ideal para zonas estreitas ou para terminar em sacadas, pontes ou outras formas curvas.
* **Segmented** — uma zona que pode ser subdividida em quads menores. Ideal para mapeamento arquitetônico.

Clique com o botão direito em qualquer zona para abrir suas configurações. Nesse menu de clique direito, você pode:

* Renomear a zona (isso pode ajudar a identificá-la no Clip Deck, especialmente se você tiver muitas zonas!)
* Ativar/desativar a zona
* Bloquear sua posição
* Alterar seu tipo de formato
* Redefini-la para a posição padrão
* Acessar configurações específicas do tipo de formato
* Excluí-la
* Adicionar uma _Alt Zone_ (veja [Sistema de zonas Alt](alt-zone-system.md))

{% hint style="danger" %}
**AVISO —** tenha muito cuidado ao alterar o tipo de zona enquanto o laser estiver ativo. A zona voltará para a última posição/tamanho usado para esse formato, então a saída pode mudar de repente. O ideal é desligar o laser antes de alterar o tipo de zona.
{% endhint %}

### Formato de zona Quad

Você pode mover cada canto do quad com o mouse. Clique com `Alt / Option` em um canto para movê-lo independentemente dos outros e distorcer o quad. Depois que o quad estiver distorcido, todos os cantos poderão ser movidos livremente.

Você pode remover a distorção e voltar para um retângulo alinhado aos eixos usando o botão _REMOVE DISTORTION_ no menu de clique direito.

#### Correção de perspectiva

Essa opção pode ser configurada usando o botão de alternância no menu de clique direito e determina o método de distorção. Para feixes, é melhor deixá-la desativada, mas se essa zona estiver projetando gráficos em um plano plano, ative-a para aplicar correção de perspectiva à saída.

{% hint style="info" %}
Se _Perspective correction_ estiver desativado, o conteúdo será distorcido usando _interpolação bilinear_. Em outras palavras, o conteúdo é espaçado uniformemente ao longo do quad. É por isso que essa opção é melhor para feixes.

Com a correção de perspectiva ativada, o conteúdo é distorcido usando deformação por perspectiva, que ajusta o encurtamento por perspectiva. Então, se você estiver projetando gráficos em uma parede em um ângulo oblíquo, poderá usar isso para corrigir a saída e compensar a distorção da projeção.
{% endhint %}

### Formato de zona Line / Curve

O formato de zona Line / Curve se tornou minha opção preferida em shows recentes, e dá para argumentar que ele deveria ser o padrão para beam zones.

Na maioria das vezes, minhas zonas precisam ser estreitas para caber em espaços apertados nos locais ou entre janelas de edifícios, e percebi que podia ser muito trabalhoso ajustar quatro cantos de um quad quando eles estão tão próximos. E assim nasceu a zona Line / Curve!

Para linhas retas, você só precisa de dois pontos e depois ajustar o _Zone thickness_ no menu de clique direito. É a forma mais rápida de criar zonas simples.

Clique com `Alt / Option` na linha para criar pontos adicionais. Esses pontos são suavizados automaticamente para criar uma forma fluida, e você pode ajustar o _Smooth level_ para eliminar qualquer dobra.

Clique com `Alt / Option` em um ponto para excluí-lo.

Ou, se você tem experiência com aplicativos de gráficos vetoriais (Inkscape, Illustrator etc.), pode usar a opção _Manually adjust bezier curves_ para ter ajuste fino de todos os pontos de controle.

### Formato de zona Segmented

Essa zona subdividida permite fazer correções extremamente detalhadas e é útil quando você está mapeando em formas complexas. Você pode adicionar ou remover subdivisões usando os botões + e - no menu de clique direito.

### Como editar uma zona que está totalmente coberta por outra zona

Clique com o botão direito na zona de cima e clique no botão de cadeado para bloqueá-la. Agora você deverá conseguir editar e ajustar a zona que está por baixo.

<br>

{% hint style="info" %}
Depois de adicionar uma Beam zone ao seu Output, ela ficará disponível para ser adicionada a um Clip no Clip Deck.
{% endhint %}
