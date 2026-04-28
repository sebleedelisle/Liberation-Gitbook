---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformações

## &#x20;Translate

Move todo o conteúdo ao longo dos eixos x, y e/ou z. Observe que o sistema de coordenadas é centralizado e se estende até +/-200 nos eixos x e y. Consulte [co-ordinate-system.md](../fundamentals/co-ordinate-system.md).

* **x** - a distância para mover ao longo do eixo x (esquerda - direita).
* **y** - a distância para mover ao longo do eixo y (cima - baixo).

#### Opções 3D (disponíveis quando 3D está selecionado)

* **z** - a distância para mover ao longo do eixo z (para trás e para frente, entrando na tela).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Gira todo o conteúdo. Os valores são em graus. Consulte [co-ordinate-system.md](../fundamentals/co-ordinate-system.md).

* **rotation** - a quantidade de rotação do conteúdo no sentido horário, em graus. Tudo é girado em torno da origem (0,0), o centro.
* **pivot point x / pivot point y** - use esses valores para deslocar a origem da rotação.

#### Opções 3D (disponíveis quando 3D está selecionado)

* **rotation x** - rotação em torno do eixo x (pitch).
* **rotation y** - rotação em torno do eixo y (yaw).
* **pivot point z** - posição de deslocamento da rotação no eixo z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Redimensiona todo o conteúdo.

* **scale** - a porcentagem de escala.
* **scale x / scale y** - se você quiser redimensionar horizontalmente e/ou verticalmente, use estas opções.

{% hint style="warning" %}
Sempre que algo é redimensionado para 0% em qualquer eixo, ele desaparece!
{% endhint %}
