---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Este node substitui linhas e formas por pontos com espaçamento uniforme (os pontos existentes não são alterados).

* **Colour** – a cor dos pontos. Ignorado se _Inherit Colour_ estiver ativado; veja abaixo. _Veja também_ [Configurações de cor e HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – a distância entre os pontos, medida em pixels. Valores menores = mais pontos; valores maiores = menos pontos.
* **Offset** – desloca a posição inicial dos pontos como uma porcentagem do espaçamento. Pode ser animado (por exemplo, com um Oscillator Node em dente de serra) para criar efeitos de pontos "viajando".
* **Keep Original** – se ativado, as linhas/formas originais são mantidas e os pontos são desenhados por cima.
* **Render Profile** – escolhe a qualidade de renderização. _Veja_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – ajusta automaticamente o espaçamento para que o comprimento do caminho seja divisível de forma uniforme.
* **Fade Out Ends** – reduz gradualmente o brilho dos pontos em direção ao início e ao fim do caminho. Útil ao animar **Offset** com um Oscillator Node em dente de serra, para que os pontos apareçam/desapareçam suavemente conforme se movem até o fim da forma.

## &#x20;Trimmer

Este node corta o comprimento visível de linhas e formas, permitindo revelar, ocultar ou animá-las ao longo do tempo.

* **Offset** – controla onde a parte visível da forma começa. Mesmo com _Trim Size_ em 0%, animar Offset de 0% → 100% faz a forma ser desenhada, ficar totalmente visível em 50% e depois desaparecer novamente.
* **Trim Size** – define quanto da forma é mantido, como uma porcentagem do seu comprimento total.
* **Loop** – trata a forma como um loop contínuo, de modo que o final se conecta de volta ao início em vez de desaparecer.
* **All Shapes** – combina todas as formas de entrada e as corta como se fossem um único caminho. Se estiver desativado, cada forma é cortada individualmente.
* **Add Dot at Start / Add Dot at End** – adiciona um ponto da cor escolhida nos pontos de corte. (Se nenhum corte for aplicado, nenhum ponto será adicionado.)
* **Colour** – a cor dos pontos de corte. _Veja também_ [Configurações de cor e HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – escolhe o render profile dos pontos. _Veja_ [Render Profile](../fundamentals/render-profile.md)
