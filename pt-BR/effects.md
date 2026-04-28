---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effects

O sistema de efeitos do Liberation é uma forma divertida e versátil de alterar a saída do Clip em tempo real. Os efeitos são totalmente flexíveis e podem ser usados para fazer tudo piscar, girar, mudar de cor ou até se mover aleatoriamente!

Tudo o que você pode fazer no editor de Clips pode ser usado como efeito. Na verdade, os efeitos são editados com exatamente o mesmo editor de nós usado para Clips! Consulte [#editing-effects](effects.md#editing-effects). As possibilidades criativas são praticamente infinitas.

Os botões de efeitos padrão 1-8 ficam abaixo dos botões de zona, e os efeitos 9-24 são os botões pequenos na parte inferior.

#### Aplicando um efeito

Pressione um botão de efeito para ativar/desativar o efeito ou, melhor ainda, use os sliders 1-8 do APC40 para fazer fade in e fade out dos efeitos. Para fazer fade in de um efeito sem um APC40, clique no botão e arraste para cima e para baixo. Ou clique com o botão direito no botão do efeito e ajuste o slider de nível.

{% hint style="warning" %}
Pressionar o botão do efeito ativará esse efeito imediatamente. No entanto, observe que, se o nível estiver em zero, nada acontecerá! Clique/arraste o botão para alterar o nível, clique com o botão direito e use o slider _level_, ou use os faders do APC40.
{% endhint %}

#### Efeitos e o atraso de zona do Clip

Os efeitos usam a configuração de atraso de zona de cada Clip em execução no momento. Então, se o seu Clip tem um atraso que se move da esquerda para a direita e você adiciona o efeito de piscar, o piscar também é atrasado da esquerda para a direita.

{% hint style="info" %}
A forma como o atraso de zona do Clip é herdado pelos efeitos é uma daquelas coisas extremamente difíceis de descrever, mas óbvias quando você testa!

Eu diria que é uma das ferramentas mais divertidas e criativas integradas ao Liberation. Experimente e você vai entender o que quero dizer!
{% endhint %}

#### Parâmetros de efeito

Adicione um parâmetro ao seu efeito com um nó _Parameter_. O sistema Parameter é uma forma de ajustar, de fora, várias configurações dentro do seu efeito. Consulte [parameter-control.md](clip-editor/oscillators/parameter-control.md) para mais informações.

Use os controles rotativos 1-8 para ajustar o _parameter_ de cada efeito. Ou clique com o botão direito no botão do efeito e ajuste o(s) slider(s) de parâmetro. A alteração do parâmetro faz coisas diferentes, dependendo de como o efeito foi configurado. Veja a lista abaixo com os efeitos padrão e o que os parâmetros deles fazem.

{% hint style="info" %}
Os controles rotativos 1-8 ficam na parte superior de um APC40 Mk2 e no canto superior direito no Mk1. Veja também: [apc40-reference.md](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Os números pequenos que você vê nos botões de efeito se referem ao _level_ e ao _parameter_ do efeito. O _level_ é controlado pelo fader no APC40, ou você pode clicar e arrastar no botão. O parâmetro é ajustado pelos rotativos do APC40, ou você pode clicar com o botão direito para ajustar com o mouse.
{% endhint %}

#### Os efeitos padrão

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Aplica um movimento caótico à saída do Clip. O parâmetro ajusta a quantidade/velocidade do caos.
2. **Sine wave** :\
   Distorce todo o conteúdo ao longo de uma onda senoidal em movimento. O parâmetro ajusta o comprimento de onda.
3. **Rotation** :\
   Faz tudo girar. O parâmetro ajusta a velocidade de rotação.
4. **Horizontal flip** :\
   Comprime e estica tudo horizontalmente. O parâmetro ajusta a velocidade.
5. **Scale** :\
   Redimensiona repetidamente tudo de tamanho máximo até zero. O parâmetro ajusta a velocidade.
6. **Hue** :\
   Altera o matiz de tudo, mas não altera a saturação (ou seja, qualquer coisa branca permanece branca). O parâmetro ajusta o matiz.
7. **Saturation and hue** :\
   Altera o matiz de tudo e também satura totalmente a cor (ou seja, qualquer coisa branca muda para a cor). O parâmetro ajusta o matiz.
8. **Flash** :\
   Faz o brilho de tudo piscar repetidamente de máximo até zero. O parâmetro ajusta a velocidade do flash.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Há mais 16 efeitos de cor na fileira inferior para aplicar valores predefinidos de matiz e saturação.

Observe que esses são os efeitos padrão, mas eles podem ser editados para fazer praticamente qualquer coisa que você quiser!

### Apply to groups

Você pode escolher quais grupos são afetados pelo efeito. Clique com o botão direito e marque/desmarque as caixas de seleção de grupo identificadas como _Apply to groups._

Eu uso principalmente essa configuração ao trabalhar separadamente com gráficos de Canvas e feixes de laser. Atribuo todos os Clips de Canvas ao grupo 5 e então excluo esse grupo dos efeitos que não quero que afetem esses Clips gráficos.

Você também poderia usar isso para aplicar ao vivo 2 mudanças de cor diferentes a 2 grupos de lasers ao mesmo tempo. Crie dois efeitos de mudança de cor e selecione a quais grupos de Clips cada um será aplicado.

### MX group

Abreviação de _Mutually Exclusive_, esta é uma forma de agrupar efeitos de modo que apenas um efeito do grupo possa estar ativo ao mesmo tempo. Observe que apenas um dos efeitos padrão de mudança de cor pode ficar ativo por vez. Isso acontece porque todos eles estão em MX Group 1.

Essa funcionalidade fica desativada se a configuração _MX Group_ estiver em 0.

### Editando efeitos

Clique com o botão direito em qualquer efeito e clique no botão _EDIT EFFECT_ para abrir o editor de efeitos. Observe que esse editor é idêntico ao editor de Clips!

Edite seu efeito da mesma forma que você editaria qualquer Clip. Consulte [clip-editor](clip-editor/).

Você precisa ter pelo menos um nó criador; pode ser qualquer coisa (linha, círculo, forma, até texto!), mas provavelmente é melhor escolher algo que faça mais sentido na pré-visualização do botão de efeito.

Quando os efeitos são aplicados, todos os nós criadores no efeito são substituídos pela saída dos Clips em execução no momento.

{% hint style="warning" %}
Por motivos técnicos extremamente tediosos, os nós "trails" não ficam habilitados dentro de um efeito. O mesmo vale para a configuração "delay" dentro dos nós de padrão (eles usam o mesmo sistema). Isso será corrigido em versões futuras.
{% endhint %}
