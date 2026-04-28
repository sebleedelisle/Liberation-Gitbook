---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Configurações de cor e HSB

No Liberation, a cor é definida como HSB, e não como RGB. Isso pode ser novidade para você, mas considero esse sistema muito mais intuitivo depois que você se acostuma.

{% hint style="info" %}
Se você preferir usar RGB, pode clicar no quadrado de cor em qualquer configuração de cor. Isso abre o painel do editor de cores, que oferece opções para RGB e HSB.
{% endhint %}

### HSB - Hue, Saturation e Brightness

#### Hue

O matiz da cor varia de 0 a 255. 0 é vermelho e, conforme você aumenta o valor, passa por todos os matizes do arco-íris: laranja, amarelo, verde, ciano, azul, roxo, magenta e depois volta para vermelho em 255.

Como isso é um loop, você pode usar uma onda triangular para percorrer todas as cores.

#### Saturation

Esta configuração ajusta a saturação, ou vivacidade, da cor. Em outras palavras, o quanto ela é _colorida_, variando de 0 a 255. Defina a saturação como 0 para tons de cinza e 255 para cores completas do arco-íris. Valores intermediários produzem cores pastel, mais lavadas.

{% hint style="info" %}
Peço desculpas aos meus amigos dos EUA pela vogal extra na palavra colour. O Liberation é feito na Inglaterra, então o inglês britânico é o padrão. No futuro, espero oferecer traduções para francês, espanhol, alemão, italiano, chinês simplificado e, sim, até inglês dos EUA. :innocent:
{% endhint %}

#### Brightness

Provavelmente a mais simples de entender: 0 é completamente preto, 255 é brilho total.

### Exemplo de uso

#### Ciclo de arco-íris :

Defina _Brightness_ e _Saturation_ como 255. Conecte um oscilador _Sawtooth_ ao soquete _Hue_ e ajuste o intervalo de 0 a 255.

#### Brilho pulsante :

Conecte um oscilador _Sawtooth_ ao soquete _Brightness_ e ajuste o intervalo de 255 a 0. Você também pode ajustar os valores mínimo e máximo do clamp para controlar a duração da mudança. Depois, use as funções de easing para refinar ainda mais a animação.

#### Flash forte / strobe :

Selecione uma cor usando _Hue_ e _Saturation_ ou clicando no seletor de cores. Conecte um oscilador _Square Wave_ ao soquete _Brightness_ e ajuste o intervalo de 255 a 0.

#### Percorrer um intervalo personalizado de matizes :

Defina _Brightness_ e _Saturation_ como 255. Conecte um oscilador _Triangle Wave_ ao soquete _Hue_ e ajuste o intervalo :

* para azul a ciano, use um intervalo de 70 a 128
* para vermelho a amarelo, use um intervalo de 0 a 40
* para vermelho a magenta, use um intervalo de 255 a 220
