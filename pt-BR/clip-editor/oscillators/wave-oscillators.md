---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Osciladores de onda

## Nesta página:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Onda dente de serra](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Onda triangular](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Onda senoidal](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Onda quadrada](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Configurações dos osciladores de onda

Todos os osciladores de onda têm as seguintes configurações:

* **range min / range max** - determina o intervalo de valores da propriedade controlada pelo oscilador. A propriedade é definida como _range min_ quando a forma de onda está na parte inferior, e como _range max_ quando a forma de onda está na parte superior.

{% hint style="info" %}
Por exemplo, se você quiser que um ponto se mova para a esquerda e para a direita entre -100 e 100, conecte o oscilador ao _x property socket_, defina _min range_ como -100 e _max range_ como 100.
{% endhint %}

* **duration** - o tempo que um ciclo completo, ou _loop_, leva para terminar. Isso é relativo ao andamento em compassos. Então ¼ é um único tempo. 1 é um compasso completo, e assim por diante.
* **duration multiplier** - escala a duração base por um fator escolhido. Por exemplo, se duration estiver definido como uma semínima e o multiplicador for 3, o oscilador durará três semínimas, ou seja, uma mínima pontuada. Multiplicadores fracionários também são aceitos — segure _SHIFT_ enquanto arrasta o controle deslizante para definir números não inteiros, o que é útil para efeitos de defasagem ou para criar deslocamentos sutis de tempo.
* **offset** - o deslocamento inicial da onda como porcentagem da duração. Se você quiser que a onda comece a um quarto do caminho, defina isso como 25%.
* **repeat count** - o número de vezes que o loop roda antes de parar. O padrão é _FOREVER_, mas você pode alterar isso se não quiser que o oscilador rode indefinidamente. Depois que ele parar, a propriedade será definida para o valor no final da onda.
* **delay count** - o atraso em tempos antes de o oscilador começar a rodar. Antes de começar, a propriedade será definida para o valor no início da onda.

{% hint style="info" %}
Com um uso cuidadoso de _repeat count_ e _delay count_, você pode criar animações bem complexas, quase como uma timeline própria!
{% endhint %}

## Configurações comuns

* **steps** - divide o movimento em um número de etapas discretas. Bom para quando você quer que as propriedades "saltem" para valores em vez de se moverem suavemente.

{% hint style="info" %}
Observe que as etapas são divididas por tempo, não por valor. Então, para uma onda dividida em 4 etapas com duração de 1 compasso, a propriedade mudará instantaneamente a cada tempo.
{% endhint %}

* **clamp min / clamp max -** aumenta a escala da onda além de seus valores mínimos ou máximos e limita o resultado.

{% hint style="info" %}
O conceito de _clamp_ é um pouco difícil de explicar, mas imagine a forma de onda saindo pela parte superior ou inferior do gráfico e depois sendo limitada às bordas. Recomendo que você experimente essas opções! Elas são muito úteis se você quiser que uma onda dente de serra comece mais tarde ou termine mais cedo.
{% endhint %}

* **ease function** - as ondas dente de serra e triangular também têm uma função de easing, que altera sutilmente a curva da animação e pode deixar suas animações muito mais expressivas!
  * **LINEAR** - o padrão, sem easing; apenas se move de forma linear entre os valores mínimo e máximo.
  * **EASE OUT** - começa rápido e depois desacelera ao chegar ao final. Muito bom para simular física, por exemplo, desacelerar até parar.
  * **EASE IN** - começa devagar e acelera gradualmente. Bom para simular ganho de impulso.
  * **EASE IN/OUT** - uma combinação dos dois, gerando um movimento bem orgânico.

{% hint style="warning" %}
**Easing -** Eu evitaria a animação linear padrão sempre que puder, a menos que você queira especificamente algo com aparência robótica. O easing pode deixar suas animações muito mais fluidas e orgânicas!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Onda dente de serra

Também é conhecida às vezes como _forma de onda em rampa_, porque sobe em rampa e depois cai bruscamente no final do ciclo. Provavelmente é o oscilador de onda mais comum, pois cria um loop para alternar propriedades como _hue_ ou _rotation._

Consulte as seções acima para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Específico da onda dente de serra:

* **cycle range compensation** - disponível quando **steps** está definido, e é útil para valores cíclicos, como uma rotação de 0 a 360. Quando isso não está definido, os valores inicial e final serão iguais, o que pode causar uma travada no ponto inicial, porque 0 e 360 são o mesmo ângulo. Ative isso e o intervalo máximo será reduzido para corrigir as posições das etapas.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Onda triangular

Ao contrário da _onda dente de serra_, que salta de volta para o início a cada ciclo, a _onda triangular_ se move linearmente para a frente e depois para trás.

Consulte as seções acima para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Onda senoidal

A forma de onda mais suave! Oscila suavemente entre dois valores, como um pêndulo.

Consulte as seções acima para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Onda quadrada

A forma de onda mais simples: ela apenas alterna entre dois valores, indo e voltando!

Consulte as seções acima para:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Específico da onda quadrada:

* **pulse width** - o tempo em que a onda fica no valor máximo em relação à duração total. 50% é o padrão, exatamente metade do tempo em cada estado. Se você quiser que ela fique "ligada" por apenas um quarto do tempo, defina como 25%. Você pode ajustar quando esse pulso acontece usando o valor de _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Um dos pontos fortes do Liberation é que ele consegue gerar efeitos aleatórios, mas repetíveis. O oscilador _noise_ pode ser usado para criar um movimento aleatório em loop, orgânico, com tanto detalhe ou tremulação quanto você quiser.

Consulte as seções acima para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Específico de Noise:

* **noise type** - o algoritmo usado para gerar o noise.
  * **SIMPLEX** - o padrão, um valor ondulante que sobe e desce suavemente e se repete em loop.
  * **RANDOM** - usa um algoritmo de números aleatórios mais tradicional, totalmente ruidoso e caótico.

{% hint style="info" %}
**Simplex noise** foi criado por Ken Perlin em 2001 como uma melhoria do algoritmo "Perlin noise", que ele desenvolveu em 1983 como parte do trabalho no filme _Tron_ — trabalho pelo qual ele ganhou um Oscar!

Esse chamado ruído de "gradiente" nasceu da frustração dele com imagens geradas por computador que antes pareciam muito "mecânicas". No mundo do CGI, ele é especialmente bom para renderizar nuvens, superfícies de água ou até mapas de altura para terrenos realistas.

Mas, no Liberation, ele é bom para criar movimentos aparentemente imprevisíveis que ainda assim são suaves e orgânicos.
{% endhint %}

* **seed** - o valor usado para criar o noise. Se você não gostar da aparência da onda de noise, tente alterar esse valor.

{% hint style="info" %}
Curiosidade nerd! Para obter um simplex noise em loop perfeito, estou iterando ao redor de um círculo em um plano de noise 2D. E alterar o valor de seed move esse plano por uma 3ª dimensão!
{% endhint %}

* **simplex detail** - altera o nível de detalhe ou tremulação do noise. Se você quiser que o padrão repetido fique menos óbvio, aumente a duration e aumente esse valor.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Cria uma forma de onda completamente personalizada. Isso é muito útil para criar animações complexas.

Consulte as seções acima para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Abaixo disso há uma lista de posições e valores. A duration é dividida em 64 etapas e você pode colocar um valor em qualquer um desses pontos.

Cada etapa tem as seguintes configurações:

* **Step** - a etapa de tempo dentro da duration. 0 fica no início e 64 fica no final.
* **Level** - o nível da onda naquele passo de tempo. O nível varia entre 0 e 1.
* **Animation type** - o menu suspenso permite escolher como você quer se mover do passo anterior até este nível.
  * **None** - sem transição; apenas salta diretamente para este nível no tempo indicado.
  * **Linear** - um movimento completamente linear do nível anterior até este.
  * **Ease in / Ease out / Ease in/out** - aplica easing entre o nível anterior e este. Veja _ease function_ acima para uma descrição dos tipos de animação.

***
