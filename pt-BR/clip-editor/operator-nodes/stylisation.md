---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Nós de Stylisation

## &#x20;Randomise

Cria cópias dispersas dos elementos de entrada usando um campo de ruído coerente. Em outras palavras, ele copia e move suas formas e pontos de maneira controlada e “ruidosa”. Em vez de tudo ficar organizado em um só lugar, você obtém várias versões que se deslocam e se espalham, como partículas se movendo em um fluxo.

* **count** – número de cópias por elemento de entrada (1–20). Com 1, você obtém uma única versão deslocada de cada elemento. Valores mais altos criam várias cópias dispersas.
* **noise offset** – percorre o campo de ruído (0–100%). Ele faz loop de forma contínua, então animar isso com um Oscillator Node gera um movimento suave e contínuo de todas as cópias juntas.
* **noise jitter** – controla a escala da textura do ruído. Valores mais baixos geram variações amplas e suaves. Valores mais altos geram posicionamentos mais fechados e irregulares. Isso altera o padrão, não a intensidade.
* **change between points** – controla o quanto cada cópia é diferente da anterior. Valores baixos mantêm as cópias agrupadas e parecidas. Valores altos espalham as cópias com maior variação.
* **face direction** – rotaciona cada cópia para que ela aponte na direção do movimento no campo de ruído, produzindo setas/partículas alinhadas ao fluxo.
* **amount** – intensidade geral do efeito (0–100%). Escala tanto o deslocamento quanto a rotação de Face direction.

{% hint style="info" %}
O nó Randomise está no centro do efeito Randomise!
{% endhint %}

## &#x20;Trails

Cria ecos do seu conteúdo, deixando cópias que desaparecem ou mudam de escala atrás do original conforme ele se move.

* **change render profile for trail** – se estiver ativado, todas as cópias da trilha usam o **render profile** selecionado. _Consulte_ [Render Profile](../fundamentals/render-profile.md).
* **render profile** – o perfil usado para as cópias da trilha quando a opção acima está ativada. É comum usar isso quando o conteúdo principal está definido como **DETAIL**, mas os ecos são renderizados como **FAST**, o que mantém detalhes nítidos nas formas principais enquanto renderiza as trilhas com mais eficiência.
* **delay** – define o espaçamento entre as cópias da trilha em tempo musical, medido em **passos de nota de 1/64**.\
  Para referência:
  * 16 = 1/16 de compasso (semicolcheia)
  * 32 = 1/8 de compasso (colcheia)
  * 64 = 1/4 de compasso (semínima)
  * 128 = 1/2 compasso (mínima)
  * 256 = 1 compasso
* **trail size** – quantas cópias de trilha serão desenhadas atrás do conteúdo ao vivo.
* **freeze trails** – transforma trilhas de fluxo suave em uma sequência de instantâneos congelados. Útil para criar efeitos de trilha em staccato, sincronizados com a batida.
* **brightness start / brightness end** – aplica brilho ao longo da trilha, da cópia mais recente (**start**) até a cópia mais antiga (**end**). Normalmente, defina **brightness start** em 100% e **brightness end** em 0% para que os ecos desapareçam.
* **scale start / scale end** – aplica escala ao longo da trilha, da cópia mais recente (start) até a cópia mais antiga (end). Para trilhas que encolhem até desaparecer, defina **scale start** em 100% e **scale end** em 0%.

## &#x20;Shimmer

Adiciona uma variação cintilante de brilho ao seu conteúdo, indo de um brilho sutil até um strobe intenso.

* **speed** – a velocidade com que o shimmer muda ao longo do tempo. Valores mais altos piscam mais rápido; 0 pausa o efeito.
* **separation** – o quanto pontos/elementos vizinhos são diferentes entre si.
  * 0: tudo cintila junto.
  * \>0: pontos próximos recebem fases progressivamente diferentes, então o shimmer varia ao longo da forma.
  * <0: igual ao acima, mas a progressão de fase ocorre no sentido oposto.
* **threshold** – em vez de desaparecer suavemente, os pontos agora piscam totalmente ligados ou desligados conforme o brilho. Elementos mais brilhantes acendem com mais frequência, mas observe que elementos com 100% de brilho ficam sempre ligados, enquanto elementos com 0% de brilho ficam sempre desligados. Útil para efeitos nítidos de glitter ou luz de estrelas.

{% hint style="info" %}
Ativar **threshold** é um daqueles ótimos recursos escondidos que podem dar muito mais vida às suas partículas ou ao seu conteúdo. Em vez de desaparecerem gradualmente, os pontos são ligados e desligados rapidamente com base no brilho. Como menos pontos são desenhados em um determinado momento, o resultado é uma saída mais brilhante e uma animação mais suave.

Mas lembre-se de que, se o seu conteúdo já estiver com 100% de brilho, isso não fará nada!
{% endhint %}

* **use whole shape** – aplica um único valor de shimmer uniformemente à forma inteira. Quando desativado, o nó subdivide as formas para que partes diferentes possam cintilar de forma independente, criando um visual pontilhado.

## &#x20;Particles

Este é um efeito experimental que gera e anima partículas com base no seu conteúdo. Qualquer elemento baseado em pontos que entrar será tratado como posição de emissor. Como os caminhos das partículas são pré-calculados, se o conteúdo de entrada mudar, talvez você precise atualizar/recalcular para atualizar as partículas (basta alterar qualquer uma das configurações)

**General**

* **keep original** – se ativado, o conteúdo original é mantido e as partículas são adicionadas por cima. Útil quando você quer que os pontos emissores continuem visíveis.
* **number of particles** – quantas partículas são criadas por emissão. Valores mais altos geram efeitos mais densos; valores mais baixos ficam mais minimalistas.
* **emission period** – a duração do loop (em compassos) durante a qual as partículas são emitidas. Em 100%, elas são distribuídas uniformemente ao longo do loop; valores menores as agrupam para criar rajadas.
* **loop length** – quanto tempo o loop de partículas dura, medido em compassos musicais.
* **loop count** – quantas vezes o loop se repete antes de reiniciar. Se definido como 1, as partículas sempre seguirão exatamente a mesma simulação a cada vez, tornando o resultado perfeitamente repetível. Valores mais altos introduzem mais variação antes que o ciclo reinicie.
* **delay** – desloca o tempo de início da emissão por um número de notas de 1/64, para efeitos de temporização.

**Motion**

* **speed** – a velocidade com que as partículas se afastam do emissor.
* **speed variation** – adiciona aleatoriedade para que as partículas não se movam todas na mesma velocidade. Cria uma dispersão mais natural.
* **direction** – define a direção base em que as partículas são disparadas, definida pelos **ângulos x, y, z**. Esses ângulos rotacionam o vetor de disparo no espaço 3D, então você pode apontar as partículas diretamente para cima, para os lados ou para qualquer diagonal. Combine com **spread** para cones mais largos ou rajadas mais caóticas.

{% hint style="info" %}
**Ângulos de Euler**\
Liberation usa **ângulos de Euler** para descrever orientação no espaço 3D. Eles são simplesmente rotações em torno dos três eixos principais:

* **X** – inclinação para frente/trás (como balançar a cabeça em “sim”)
* **Y** – virar para a esquerda/direita (como balançar a cabeça em “não”)
* **Z** – rolar no sentido horário/anti-horário (como inclinar a cabeça para o lado)

Ao ajustar esses três valores, você pode apontar as partículas em qualquer direção.
{% endhint %}

* **direction variation** – adiciona dispersão aleatória em torno dessa direção. Útil para criar cones, sprays ou explosões.
* **drag** – desacelera as partículas ao longo do tempo. Valores mais altos fazem com que elas pareçam mais pesadas e lentas.
* **gravity** – puxa as partículas para baixo (positivo) ou as empurra para cima (negativo).
* **gravity variation** – adiciona variação de gravidade por partícula, tornando o movimento mais caótico.

**Life**

* **life duration** – por quanto tempo as partículas existem (medido em unidades de nota de 1/64). Com valores mais curtos, as partículas desaparecem rapidamente; com valores mais longos, elas permanecem visíveis por mais tempo.
* **life variation** – adiciona aleatoriedade à duração das partículas para que elas não desapareçam todas ao mesmo tempo.
* **start delay / start delay variation** – atrasa o momento em que cada partícula fica visível (em passos de nota de 1/64). A partícula já foi gerada e está se movendo durante esse período, mas seu brilho é mantido em 0, então ela permanece invisível até o atraso terminar. É útil se você quiser que "brilhos" atrasados de fogos de artifício apareçam.

**Colour & brightness**

* **hue start** – cor inicial das partículas.
* **hue variation** – adiciona aleatoriedade para que as partículas não comecem todas com a mesma cor.
* **hue change** – desloca o matiz ao longo da vida da partícula, criando trilhas que mudam de cor.
* **brightness start / brightness end** – aplica brilho ao longo da vida da partícula. Normalmente, defina brightness start alto e brightness end baixo para que elas desapareçam naturalmente.
* **brightness variation** – randomiza o brilho inicial para um visual mais dinâmico.
* **saturation start / saturation end** – define o quão vívida a cor é no início e no fim.
* **saturation variation** – randomiza a saturação para criar variação entre partículas.

**Simulation**

* **time adjustment** – acelera ou desacelera toda a simulação de partículas. Útil para sincronizar com diferentes tempos ou exagerar o movimento.
