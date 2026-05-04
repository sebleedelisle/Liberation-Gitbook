---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Áreas-alvo do Canvas

Já vimos como levar partes do Canvas para zonas dentro de cada laser, mas, para colocar conteúdo no Canvas em primeiro lugar, você precisa das _Canvas target areas_ (um nome um pouco confuso, mas preciso).

_As Canvas target areas_ são seções do Canvas nas quais você pode desenhar clips, e elas aparecem na visualização _CANVAS_ como retângulos com contorno azul.

Na maior parte do tempo, talvez você só precise de uma Canvas target area e depois dividi-la em várias zonas enviadas para lasers diferentes.

Às vezes, você pode querer várias Canvas target areas para diferentes partes de um prédio, ou para aproveitar o atraso de zona entre elas. (Sim! O atraso de zona ainda funciona entre Canvas target areas!).

### Enviando clips para Canvas target areas

Se você olhar no Clip Deck, ao lado dos botões de beam zone, verá os botões das Canvas target areas. Talvez seja necessário rolar os botões de Output para vê-los; use `Shift + Left / Right Arrow`, os botões ZONE PAGE na tela ou os botões do APC40 (veja [Referência do APC40](../reference/apc40-reference.md "mention")).

Atribua clips às Canvas target areas ativando esses botões exatamente da mesma forma que você faria com os botões de zona de feixe.

### Adicionando / editando Canvas target areas

Na barra de menu superior, selecione _View -> Canvas Target Areas_ — você verá todas as configurações de cada Canvas target area que existe no seu projeto.

E, na parte superior, há o botão _ADD CANVAS TARGET AREA_.

Exclua uma Canvas target area usando o botão vermelho com um sinal de menos.

Ajuste o tamanho e a posição usando os controles deslizantes. Clique duas vezes em um controle deslizante para digitar um valor.

### Modo de escala

* **FIT TO AREA** - reduz o conteúdo para que ele caiba completamente dentro da Canvas target area, mantendo a proporção. (Esta é a configuração padrão)
* **FILL AREA** - estica o conteúdo para preencher a Canvas target area, mantendo a proporção. O conteúdo pode ser cortado nas bordas.
* **STRETCH TO FIT** - estica o conteúdo para preencher toda a Canvas target area, ignorando a proporção.
