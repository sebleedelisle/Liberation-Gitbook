---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Calibração de cores

A calibração de cores garante que os lasers vermelho, verde e azul do seu projetor emitam luz de forma suave e previsível em todos os níveis de brilho. Projetores diferentes podem ter curvas de brilho não lineares, ou seja, 50% de vermelho pode parecer muito mais claro ou mais escuro do que metade da intensidade de 100% de vermelho. A calibração corrige isso para que as cores se misturem melhor, os gradientes fiquem suaves e os brancos fiquem equilibrados.

#### Aquecendo o projetor

Os diodos laser mudam de comportamento conforme aquecem. Sempre deixe o projetor estabilizar antes da calibração:

* Projete um quadro brilhante, como o **White rectangle test pattern (11)**, por pelo menos **15–20 minutos**.
* Isso garante que o equilíbrio de cores definido permaneça consistente durante um show.

#### Como o teste de calibração funciona

Use os padrões de teste para calibração (veja [test-patterns.md](../output-view/test-patterns.md))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Cada um deles mostra quatro linhas em movimento:

* **Linha superior** – 100% de brilho em velocidade total
* **Segunda linha** – 75% de brilho a 75% da velocidade
* **Terceira linha** – 50% de brilho a 50% da velocidade
* **Quarta linha** – 25% de brilho a 25% da velocidade

Como o brilho _e a velocidade_ são ajustados juntos, todas as linhas devem parecer ter o mesmo brilho. Se uma parecer mais clara ou mais escura, ajuste o controle deslizante correspondente até que elas fiquem iguais.

Cada padrão de teste também tem uma quinta linha em **0% de brilho**, que não deve ficar visível. Ela é usada para corrigir lasers que não emitem nenhuma luz em níveis muito baixos. Se o laser continuar invisível em baixo brilho, aumente gradualmente o **0% setting** até que a linha fique apenas visível e, em seguida, reduza um pouco até ela desaparecer novamente. O objetivo é encontrar o limite em que o laser começa a acender e ficar logo abaixo dele, para que os fades comecem de forma natural sem cortar a parte inferior da faixa.

#### Usando o painel Colour Calibration

O painel oferece controles independentes para cada canal (vermelho, verde, azul) nos níveis de 100, 75, 50, 25 e 0%.

1. **Selecione um padrão de teste** (comece com vermelho).
2. **Ajuste os controles deslizantes** para que as linhas de 100, 75, 50 e 25% pareçam ter o mesmo brilho.
3. **Ajuste o controle deslizante de 0%** se a linha “desligada” ainda estiver levemente visível.
4. **Repita para verde e azul.**
5. Mude para o **White test pattern (8)**. Todas as quatro linhas devem parecer iguais, e o branco deve parecer neutro (sem tonalidade colorida).

#### Ajustando o balanço de branco

Você também pode usar este sistema para ajustar o **balanço de branco**. Depois de calibrar cada canal individualmente, mude para o **White test pattern (8)**. Se a saída parecer com alguma tonalidade colorida (por exemplo, verde demais ou azul demais), ajuste os níveis relativos dos canais vermelho, verde e azul até que as linhas pareçam um branco neutro. Mesmo que seus lasers tenham potências bem diferentes, a calibração ainda ajuda a aproximá-los e a produzir uma mistura de cores mais limpa e equilibrada.

#### Salvando a calibração

* Use **Store** para sobrescrever o preset atual.
* Use **Store As** para criar um novo preset (útil se você trabalha com vários lasers).
