---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Cria uma cópia espelhada de todo o conteúdo. Por padrão, o eixo de espelhamento é uma linha vertical no centro.

* **angle** - o ângulo da linha do eixo de espelhamento.
* **offset position** - desloca o eixo de espelhamento (move perpendicularmente ao eixo)
* **delay** - atraso de tempo do conteúdo espelhado. Observe que isso só terá efeito se o conteúdo tiver algum tipo de animação.

#### Opções 3D (disponíveis quando 3D está selecionado)

* **angle X / angle Y** - o eixo de espelhamento se torna um plano, e você pode usar essas configurações para girar o plano em 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplica o conteúdo em um padrão circular.

* **radius** - a distância a partir do ponto central pela qual o conteúdo é deslocado antes da rotação.
* **count** - o número de cópias do objeto a serem criadas.
* **use each objects pivot point** - quando selecionado, cada elemento será deslocado e girado em torno do seu próprio ponto central. (Só tem efeito quando há vários elementos sendo duplicados)
* **delay** - adiciona um atraso de tempo progressivamente maior a cada elemento duplicado. Observe que o conteúdo precisa ter algum tipo de animação para que isso tenha um efeito perceptível.
* **rotation** - uma rotação de deslocamento adicionada aos elementos.

#### Opções 3D (disponíveis quando 3D está selecionado)

* **rotation x / rotation y** - gira todo o padrão circular em torno dos eixos x e y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplica o conteúdo em um padrão de grade com linhas e colunas.

* **spacing** - a distância entre os elementos
* **count X**- o número de cópias na horizontal (colunas)
* **count Y**- o número de cópias na vertical (linhas)
* **horizontal alignment** - o ponto inicial das colunas, LEFT, CENTRE ou RIGHT
* **vertical alignment** - o ponto inicial das linhas, TOP, MIDDLE ou BOTTOM
* **delay** - adiciona um atraso de tempo progressivamente maior a cada elemento duplicado. Observe que o conteúdo precisa ter algum tipo de animação para que isso tenha um efeito perceptível.
