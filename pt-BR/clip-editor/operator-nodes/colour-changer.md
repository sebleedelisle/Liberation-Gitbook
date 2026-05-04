---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Altera as cores de todo o conteúdo de entrada. Você pode definir valores HSB fixos ou mudar para o sistema de gradiente e amostrar cores de um gradiente personalizado.

* **hue, saturation, brightness** - os valores de cor; consulte [Configurações de cor e HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - o matiz não é alterado
  * FIXED - o matiz dos elementos é definido pelo valor de hue
  * SHIFT - o matiz dos elementos é deslocado pelo valor definido; assim, elementos de cores diferentes continuam diferentes, mas são apenas deslocados ao longo do valor de matiz.
* **saturation mode** -
  * OFF - a saturação não é alterada
  * FIXED - a saturação é fixada no valor especificado.
* **brightness mode** -
  * OFF - o brilho não é alterado
  * FIXED - o brilho dos elementos é definido pelo valor de brightness
  * MULTIPLY - o brilho dos elementos é combinado com o valor de brightness; assim, se eles estiverem piscando, continuarão piscando, mas somente até o brilho especificado aqui.
* **gradient mode** - muda dos controles deslizantes HSB fixos para o editor de gradiente. O node amostra uma cor do gradiente e depois a aplica usando os modos de matiz, saturação e brilho acima.
* **gradient position** - escolhe qual ponto do gradiente será amostrado. Anime isto de 0% a 100% com um Sawtooth Oscillator para percorrer o gradiente ao longo do tempo.
* **blend** - define com que intensidade o Colour change é aplicado: 0% significa nenhuma aplicação, 100% significa aplicação total, e 50% é uma combinação da cor existente com os novos valores.

{% hint style="info" %}
O node Colour Change amostra uma cor do gradiente para toda a entrada. Se você quiser que o gradiente percorra a forma por posição, use [alteradores baseados em posição](position-based-changers.md "mention") em vez disso.
{% endhint %}

### Editor de gradiente

Quando **gradient mode** está ativado, o editor de gradiente aparece abaixo dos controles principais.

* Clique na barra de gradiente para adicionar um ponto de cor.
* Clique com o botão esquerdo em um ponto para selecioná-lo e arraste-o para os lados para movê-lo.
* Arraste um ponto selecionado para baixo, afastando-o da barra, ou pressione Delete/Backspace, para removê-lo. Um gradiente sempre mantém pelo menos dois pontos.
* Clique com o botão direito em um ponto para editá-lo com o seletor de cores.
* Use **Position**, **Hue**, **Saturation** e **Brightness** para editar o ponto selecionado com precisão.
* **interpolation** escolhe como as cores são mescladas entre os pontos:
* **HSB** - mescla matiz, saturação e brilho. Isso é ideal para movimentos suaves em estilo arco-íris ao redor da roda de cores.
* **RGB** - mescla diretamente os valores de vermelho, verde e azul. Isso costuma parecer mais com uma transição de cor de tela ou de console de iluminação.
* **NONE** - salta de um ponto para o próximo sem mesclagem.
* **hue direction** está disponível na interpolação HSB:
* **AUTO** - usa o caminho mais curto ao redor da roda de matiz.
* **FORWARDS** - sempre avança pelos valores de matiz.
* **BACKWARDS** - sempre retrocede pelos valores de matiz.
