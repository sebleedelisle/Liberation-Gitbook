---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Sincronizando o andamento com uma faixa de áudio

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Sincronizando o andamento com uma faixa de áudio" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

A timeline do Liberation foi criada para trabalhar com andamentos fixos ou variáveis, mas uma sincronização confiável sempre começa encontrando o andamento e alinhando o áudio corretamente. Esta seção descreve o fluxo de trabalho recomendado.

#### 1. Alinhe o primeiro tempo forte

Adicione sua faixa de áudio à timeline e verifique se ela está ajustada a uma batida, de modo que o **primeiro tempo forte musical** da faixa fique alinhado exatamente com o início de um compasso.

Esta etapa é essencial.

Se o áudio não começar naturalmente em um tempo forte, você tem duas opções:

* **Ajustar o atraso do clip**\
  Clique com o botão direito no clip de áudio e ajuste o valor de Delay até que o primeiro tempo forte fique alinhado com um marcador de batida ou de compasso.
* **Cortar o áudio externamente**\
  Edite o arquivo de áudio em um editor externo, como o Audacity, para que o arquivo comece exatamente no primeiro tempo forte. Depois, importe-o novamente.

{% hint style="info" %}
**Importante:**\
Se o início do áudio não estiver alinhado a uma batida ou a um compasso, a posição inicial percebida da música vai se deslocar para trás e para frente conforme você altera o andamento. Isso torna muito difícil fazer uma correspondência precisa de andamento.
{% endhint %}

#### 2. Defina um andamento inicial

Se você tiver uma ideia aproximada do BPM, insira esse valor no controle de andamento da timeline e inicie a reprodução desde o começo.

Observe com atenção os marcadores de batida e de compasso enquanto a faixa toca.

* Se os marcadores se adiantarem em relação à música, reduza um pouco o andamento.
* Se eles ficarem para trás, aumente um pouco o andamento.
* Pare a reprodução, ajuste o andamento e tente novamente.

Na maioria das músicas modernas, o andamento é um BPM inteiro fixo. Depois de encontrar o valor correto, ele deve permanecer sincronizado durante toda a faixa.

#### 3. Use a forma de onda como referência visual

A forma de onda do áudio é uma referência útil ao ajustar o andamento.

* Transientes e picos devem ficar alinhados com os marcadores verticais de compasso.
* Aproxime bastante o zoom para verificar o alinhamento ao longo de vários compassos.

**Dica:**\
Use a roda do mouse ou o gesto no trackpad para aplicar zoom na timeline. Use a roda de rolagem horizontal ou o gesto correspondente para mover para a esquerda e para a direita. Trabalhar com zoom aproximado facilita muito os pequenos ajustes.

#### 4. Faixas com BPM não inteiro

Se a faixa não usar um BPM inteiro, o desvio será mais gradual.

* Aproxime mais o zoom.
* Use ajustes menores de andamento.
* Verifique o alinhamento em seções mais longas da faixa, não apenas nos primeiros compassos.

#### 5. Músicas com mudanças de andamento

Se a música acelerar ou desacelerar, use o Tempo Map:

* Reproduza a faixa e observe os marcadores de batida.
* Quando o desvio ficar perceptível, adicione uma mudança de andamento nesse ponto.
* Ajuste o andamento da nova seção até que ela fique sincronizada novamente.

Repita esse processo para cada mudança de andamento na música.

#### 6. Análise externa de andamento (opcional)

Como último recurso, você pode analisar a faixa em uma DAW, como o Logic Pro, e gerar um mapa de andamento automaticamente. Tenha em mente que isso costuma produzir um grande número de mudanças de andamento, às vezes uma por compasso, o que pode ser mais detalhado do que o necessário para a maioria dos shows.
