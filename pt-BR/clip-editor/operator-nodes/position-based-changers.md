---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Modificadores baseados em posição

Esta família de nodes modifica o conteúdo de acordo com a posição. Por padrão, o efeito é aplicado ao longo de um eixo horizontal (da esquerda para a direita), mas você pode girar esse eixo para qualquer ângulo. Cada node também inclui um modo _radial_, em que o efeito é controlado pelo ângulo de cada ponto em relação ao centro.

* **Colour Changer by Position** – desloca as cores ao longo do eixo escolhido ou ao redor do ângulo radial.\
  \&#xNAN;_Exemplo: crie um gradiente arco-íris percorrendo uma linha, ou use o modo radial em um círculo para produzir um efeito de roda de cores._
* **Wave Shift by Position** – aplica uma distorção de onda senoidal, deslocando o conteúdo verticalmente (ou perpendicularmente ao eixo escolhido).\
  \&#xNAN;_Exemplo: faça uma linha ondular como água, ou use o modo radial para fazer um círculo pulsar para fora a partir do centro._
* **Noise Shift by Position** – aplica uma distorção de ruído simplex, deslocando o conteúdo verticalmente (ou perpendicularmente ao eixo escolhido).\
  \&#xNAN;_Exemplo: veja o exemplo de Wave Shift, mas com um caráter mais orgânico e aleatório, perfeito para adicionar variação natural._

## &#x20;Alteração de cor por posição

Este node aplica mudanças de cor ao seu conteúdo com base na posição. Por padrão, o eixo é horizontal (0°), mas você pode girá-lo ou alternar para o modo radial.

* **wavelength** – define o tamanho do ciclo de cores repetido.
  * _Modo Linear:_ em 100%, um ciclo completo ocupa toda a largura do conteúdo.
  * _Modo Radial:_ em 100%, um ciclo completo ocupa o círculo inteiro (360°). Os valores são porcentagens do círculo: por exemplo, 50% = meio círculo (180°).
* **offset** – desloca o ponto inicial do ciclo de cores, como uma porcentagem do wavelength. Você pode modular isso (por exemplo, com um oscilador dente de serra) para percorrer as cores de forma suave.
* **repeat** – quando ativado, o ciclo se repete pelo conteúdo. Se desativado, o gradiente é aplicado apenas uma vez: tudo antes do início recebe a cor inicial, e tudo depois do fim recebe a cor final.
* **pingpong** – quando ativado, cada repetição alterna de direção, criando um efeito espelhado. Se _Repeat_ estiver desativado, o gradiente vai para frente e depois volta uma vez. _Observação: no modo Pingpong, o wavelength cobre tanto a varredura de ida quanto a de volta._
* **linear angle** – gira o eixo do efeito. 0° = horizontal.
* **radial** – alterna para o modo radial, aplicando cores com base no ângulo a partir do centro.
* **radial smooth loop** – ajusta automaticamente o wavelength para que ele divida 100% do círculo de forma uniforme, evitando uma emenda visível onde o ciclo se fecha.

**Modos de cor**

Eles determinam quais aspectos dos ajustes de cor são aplicados ao conteúdo. Veja também: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md).

* **hue mode**
  * _OFF_ – o hue não é alterado.
  * _FIXED_ – o hue é forçado para um valor fixo.
  * _SHIFTED_ – o hue é deslocado pelo valor especificado (elementos com cores diferentes continuam distintos, mas são deslocados juntos ao redor da roda de cores).
* **saturation mode**
  * _OFF_ – a saturation não é alterada.
  * _FIXED_ – a saturation é definida para o valor especificado.
* **brightness mode**
  * _OFF_ – o brightness não é alterado.
  * _FIXED_ – o brightness é definido para o valor especificado.
  * _MULTIPLY_ – o brightness é escalado pelo valor especificado. Isso preserva a dinâmica (por exemplo, elementos piscando continuam piscando, mas dentro da faixa de brilho limitada).

**Valores iniciais / finais**

Estes sliders definem a faixa de cor aplicada ao longo do eixo escolhido (ou da varredura radial).

* **start hue** – o hue no início do gradiente.
* **end hue** – o hue no fim do gradiente.
* **start saturation** – a saturation no início.
* **end saturation** – a saturation no fim.
* **start brightness** – o brightness no início.
* **end brightness** – o brightness no fim.
* **blend** – mistura a alteração de cor com as cores originais. Em 100%, o efeito substitui totalmente as cores originais.

**Exemplo 1: gradiente arco-íris deslizante**

Começando com as configurações padrão:

1. Deixe o node no modo **Linear** (ângulo de 0° = horizontal).
2. Deixe **wavelength** em 100% (ocupa toda a largura e deve ser o padrão).
3. Deixe os valores inicial e final como padrão.
4. Ative **repeat**.
5. Adicione um **Sawtooth Oscillator** à configuração **offset**, indo de 0% a 100%.

***

**Exemplo 2: gradiente preto–branco–preto (Pingpong)**

Começando com as configurações padrão:

1. Deixe o node no modo **Linear** (ângulo de 0° = horizontal).
2. Deixe **wavelength** em 100% (ocupa toda a largura e deve ser o padrão).
3. Desative **repeat**.
4. Defina **start brightness** como 0 (preto).
5. Defina **end brightness** como 100 (branco).
6. Defina **start saturation** e **end saturation** como 0 (converte para escala de cinza).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Ative **pingpong**.

_Resultado: o gradiente passa de preto para branco e depois volta para preto ao longo da largura._\
Observe que, se você quiser que o conteúdo mantenha seu hue e sua saturation, desative Saturation mode. \\

***

**Exemplo 3: roda arco-íris giratória (Radial)**

1. Ative o modo **radial**.
2. Defina **wavelength** como 100% (uma varredura completa de 360°).
3. Ative **repeat**.
4. Adicione um **Sawtooth Oscillator** à configuração **offset**, indo de 0% a 100%.

_Resultado: uma roda de cores contínua, sem emendas, que gira continuamente ao redor do círculo._

## &#x20;Deslocamento de onda por posição

Este node aplica uma distorção de onda ao seu conteúdo, deslocando pontos perpendicularmente ao eixo escolhido (ou radialmente a partir do centro).

* **Wavelength** – define o comprimento do ciclo da onda.
  * _Modo Linear:_ em 100%, um ciclo completo ocupa toda a largura do conteúdo.
  * _Modo Radial:_ em 100%, um ciclo completo ocupa os 360° completos. (Os valores são porcentagens do círculo: 50% = meia volta, 25% = um quarto de volta etc.)
* **Size** – controla a amplitude da onda (o quanto o conteúdo é deslocado).
* **Offset** – desloca a onda ao longo do eixo (ou ao redor do círculo no modo radial). Este valor é uma porcentagem do wavelength, então você pode animá-lo com um **Oscillator Node** para fazer a onda se mover.
* **Radial** – alterna do modo linear para o modo radial, fazendo com que o deslocamento seja baseado no ângulo a partir do centro.
* **Radial Smooth Loop** – ajusta o wavelength para que ele divida 100% do círculo de forma uniforme, evitando emendas visíveis no ponto de fechamento.
* **Triangle** – muda o formato de onda de seno para triângulo.
* **Absolute** – usa o valor absoluto da onda, criando apenas deslocamentos para cima (dobrando o lado negativo sobre o positivo).
* **Angle** – gira o eixo da onda. 0° = horizontal.

## &#x20;Deslocamento de ruído por posição

Este node distorce o conteúdo usando um campo de ruído (como turbulência), deslocando pontos perpendicularmente ao eixo escolhido (ou radialmente a partir do centro). Comparado ao _Wave Shift_, o resultado é mais orgânico e aleatório.

* **Detail** – controla o nível de detalhe do ruído. Valores mais altos = variação mais nítida e detalhada. Valores mais baixos = variação mais suave.
* **Wavelength** – define a escala do padrão de ruído.
  * _Modo Linear:_ em 100%, um ciclo completo de ruído ocupa a largura do conteúdo.
  * _Modo Radial:_ em 100%, um ciclo completo ocupa os 360° completos.
* **Size** – controla a quantidade de deslocamento (amplitude da distorção de ruído).
* **Offset** – desloca o padrão de ruído ao longo do eixo (ou ao redor do círculo). Este valor é uma porcentagem do wavelength, então você pode animá-lo com um **Oscillator Node** para fazer o ruído “fluir”.
* **Depth Offset** – percorre o campo de ruído 3D, criando variação ao longo do tempo. Isso é especialmente eficaz quando animado com um Oscillator Node.
* **Depth Detail** – controla o nível de detalhe da variação na dimensão de profundidade.
* **Absolute** – usa o valor absoluto do ruído, dobrando valores negativos para positivos (produzindo deslocamento em apenas um lado).
* **Radial** – alterna do modo linear para o modo radial, fazendo com que o deslocamento seja baseado no ângulo a partir do centro.
* **Radial Smooth Loop** – ajusta o wavelength para que ele divida 100% do círculo de forma uniforme, evitando emendas visíveis no modo radial.
