---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Preenchimentos, máscaras e ordenação por profundidade

### Traços, preenchimentos e máscaras

Você vai perceber que alguns nós Creator têm a opção _Fill state_; você pode desenhá-los com um traço (um contorno), como uma máscara (cobrindo o que está por baixo) ou ambos.

Quando você renderiza uma forma como máscara, é como se ela fosse preenchida com preto, e tudo que estiver por baixo dela será coberto.

{% hint style="info" %}
Desenhar uma linha (ou _stroke_) com um laser é simples: você escaneia o laser do início da linha até o fim da linha. Pronto, aí está a sua linha!

Formas preenchidas são mais difíceis; se você quiser uma forma preenchida com cor, poderia fazer hachuras manualmente desenhando linhas e preenchendo a área, mas o Liberation não consegue fazer isso automaticamente (ainda). E, mesmo que fizéssemos isso, você ainda veria outras linhas aparecendo por baixo.

Mas o que podemos fazer é preencher formas com _preto_. Por baixo dos panos, o Liberation faz todos os cálculos para remover o conteúdo que está sob a forma preenchida de preto. E pode acreditar: é trabalhoso!

Mas funciona muito bem e cria a ilusão de uma forma preenchida em preto.
{% endhint %}

### Ordenação por profundidade

Como algumas formas podem _cobrir_ outras formas, o Liberation precisa ordená-las pela profundidade. Por padrão, os elementos são ordenados por profundidade de acordo com a posição z. Se estiverem na mesma posição z, eles são ordenados pela posição de camada, que pode ser alterada usando os botões _MOVE TO FRONT_ e _MOVE TO BACK_ dentro de cada Creator.
