---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Nós Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Cria um único ponto / feixe.

* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **Colour** - a cor do ponto. Consulte [Configurações de cor e HSB](fundamentals/colour-settings-and-hsb.md)
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Cria uma linha / plano.

* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **Size** - o comprimento da linha
* **Colour** - a cor da linha. Consulte [Configurações de cor e HSB](fundamentals/colour-settings-and-hsb.md)
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* **rotation** - o ângulo da linha, em graus
* **resolution** - consulte [Resolução](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ determina o ponto inicial e o centro de rotação da linha
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Cria um círculo / cone.

* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **radius** - o raio do círculo
* **Colour** - a cor do círculo. Consulte [Configurações de cor e HSB](fundamentals/colour-settings-and-hsb.md)
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* **resolution** - consulte [Resolução](fundamentals/resolution.md)
* **Fill state** - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Cria um polígono equilátero: triângulo, quadrado, pentágono etc.

* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **size** - a distância do centro até cada um dos vértices
* **Colour** - a cor do polígono. Consulte [Configurações de cor e HSB](fundamentals/colour-settings-and-hsb.md)
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* **rotation** - o ângulo de rotação da forma, em graus
* **resolution** - consulte [Resolução](fundamentals/resolution.md)
* **Fill state** - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Carrega um arquivo SVG para formas personalizadas.

{% hint style="warning" %}
O Liberation é compatível com o formato _SVGTiny_. O InkScape é recomendado, mas a maioria dos aplicativos de gráficos vetoriais consegue exportar nesse formato. Converta qualquer texto em formas antes de exportar. O Liberation renderiza traços e, opcionalmente, usa preenchimentos como máscaras. Verifique se suas linhas não estão pretas, ou elas não aparecerão sem um modificador de cor!
{% endhint %}

* **Import SVG** - carrega um arquivo SVG do disco.

{% hint style="info" %}
Depois que um SVG é carregado, o conteúdo é convertido e salvo dentro do clip. Assim, você não precisa manter uma referência ao arquivo, a menos que queira alterar as configurações de máscara posteriormente.
{% endhint %}

* **Use fills as masks** - processa qualquer forma preenchida como uma máscara, ou seja, preenchida com preto. Isso será definido automaticamente se o SVG tiver alguma forma preenchida. Se ele não tiver formas preenchidas, a opção será desativada. Consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - se as formas no seu SVG não tiverem contorno, não será possível desenhá-las! Esta opção adiciona um contorno (ou _stroke_) a qualquer forma preenchida. Se o SVG não tiver nenhuma forma com traço, ela será definida automaticamente. Se ele não tiver formas preenchidas, ela será desativada.
* **Invert black lines** - se todas as linhas no seu SVG forem pretas, você não conseguirá vê-las! Esta opção as transforma em branco. Ela é definida automaticamente se o SVG tiver apenas formas pretas, mas fica desativada se não houver nenhuma.
* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **scale** - ajusta o tamanho do SVG. Isso é calculado automaticamente quando o SVG é carregado (para garantir que a imagem fique visível), mas pode ser editado manualmente depois.
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* **rotation** - o ângulo de rotação da imagem, em graus
* **resolution** - consulte [Resolução](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Cria uma animação a partir de uma sequência de arquivos SVG.

* **Import SVG Sequence** - escolha a pasta que contém todos os arquivos SVG. Observe que eles são carregados em ordem alfanumérica.

{% hint style="info" %}
Depois que a sequência de SVG é carregada, o conteúdo é convertido e salvo dentro do clip. Assim, você não precisa manter uma referência aos arquivos, a menos que queira alterar as configurações de máscara posteriormente.
{% endhint %}

* **Use fills as masks** - processa qualquer forma preenchida como uma máscara, ou seja, preenchida com preto. Isso será definido automaticamente se qualquer um dos seus SVGs tiver formas preenchidas. Se nenhum tiver formas preenchidas, a opção será desativada. Consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - se as formas nos seus SVGs não tiverem contorno, não será possível desenhá-las! Esta opção adiciona um contorno (ou _stroke_) a qualquer forma preenchida. Se os SVGs não tiverem nenhuma forma com traço, ela será definida automaticamente. Se nenhum tiver formas preenchidas, ela será desativada.
* **Invert black lines** - se todas as linhas nos seus SVGs forem pretas, você não conseguirá vê-las! Esta opção as transforma em branco. Ela é definida automaticamente se os SVGs tiverem apenas formas pretas, mas fica desativada se não houver nenhuma.
* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **scale** - ajusta o tamanho da imagem.
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* **rotation** - o ângulo de rotação da imagem, em graus
* **resolution** - consulte [Resolução](fundamentals/resolution.md)
* **speed** - a duração da animação inteira, em compassos.
* **time per frame** - se esta opção estiver ativada, a duração será por quadro, e não pela duração total da animação. Então, se _speed_ estiver definido como ¼, cada quadro terá 1 tempo.
* **animation direction** -
  * _FORWARDS_ - a animação avança e depois volta em loop para o início
  * _BACKWARDS_ - a animação retrocede e depois volta em loop para o final
  * _PINGPONG_ - a animação avança e depois retrocede em loop
  * _MANUAL_ - o quadro atual é definido pela configuração _position manual_
* **position manual** - define o quadro atual: 0% é o primeiro quadro, 100% é o último quadro. Isso pode ser definido manualmente ou com um oscilador externo.
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Cria texto usando uma fonte TrueType ou OpenType.

* **Text** - digite aqui o texto que você quer
* **Font** - escolha a fonte que você quer

{% hint style="info" %}
Para adicionar mais fontes ao Liberation, copie os arquivos .ttf ou .otf para a pasta data/resources/fonts.
{% endhint %}

* **Render profile** - consulte [Render Profile](fundamentals/render-profile.md)
* **horizontal alignment** - escolha _LEFT_, _CENTRE_ ou _RIGHT_ para selecionar o alinhamento do texto.
* **Fill state** - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - o tamanho do texto
* **colour -** consulte [Configurações de cor e HSB](fundamentals/colour-settings-and-hsb.md)
* posição **x** e **y** - consulte [Sistema de coordenadas](fundamentals/co-ordinate-system.md)
* **rotation** - o ângulo de rotação da imagem, em graus
* **resolution** - consulte [Resolução](fundamentals/resolution.md)
* **reveal** - use isto para revelar gradualmente o texto, um caractere por vez. Quando estiver entre 0 e 50%, o texto aparecerá gradualmente da esquerda para a direita. Quando estiver entre 50% e 100%, o texto desaparecerá da esquerda para a direita. Você pode conectar um oscilador a este socket para criar animações.
* **reveal by word** - quando ativado, _reveal_ funciona palavra por palavra, em vez de caractere por caractere.
* **countdown** - um sistema de contagem regressiva (implementado às pressas!). Ele muda a cada 2 tempos; se você quiser segundos, confirme que está em 120bpm.
* **countdown start** - o número a partir do qual você quer iniciar a contagem regressiva
* _MOVE TO FRONT / MOVE TO BACK_ - consulte [Preenchimentos, máscaras e ordenação por profundidade](fundamentals/fills-masks-and-depth-sorting.md)
