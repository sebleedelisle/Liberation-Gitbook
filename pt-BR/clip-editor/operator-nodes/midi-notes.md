---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Cria efeitos no estilo “harpa laser”, em que notas MIDI recebidas disparam feixes ou formas ao longo de um intervalo. O node usa qualquer conteúdo que você enviar para ele como a _fonte_ de cada nota — envie um ponto e você terá uma fileira de pontos. Envie uma forma, como um círculo, e você terá uma fileira de círculos; formas mais complexas serão replicadas da mesma maneira.

Você pode escolher qual interface MIDI o Liberation deve escutar em **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – qual canal MIDI escutar (0 = todos os canais, 1–16 = canal específico)
* **width** – largura total ao longo da qual as notas se distribuem.
* **midi note min / max** – os valores da nota MIDI mais baixa e mais alta no intervalo.
* **ignore out of range notes** – filtra qualquer nota fora do intervalo definido. Se desativado, notas fora do intervalo são “limitadas” à nota disponível mais próxima (notas altas disparam o topo do intervalo, notas baixas disparam a base).
* **auto extend range** – amplia automaticamente o intervalo se forem tocadas notas fora dele.

{% hint style="info" %}
Não tem certeza de qual intervalo de notas você está recebendo? Ative **auto extend range**, defina **midi note min** bem alto e **midi note max** bem baixo e então toque suas notas. O sistema vai capturar todas elas e expandir o intervalo para você. Depois que tiver tudo, basta desativar **auto extend range** para fixar o intervalo.
{% endhint %}

* **leave all notes visible** – cria feixes ou formas para todas as notas no intervalo, estejam elas tocando ou não, gerando um efeito de “harpa laser”.
* **hit colour** – a cor que aparece quando uma nota é acionada.
* **hit colour hold time** – por quanto tempo a cor de acionamento permanece com brilho total antes de começar a desaparecer. O valor é em segundos (0–1). _100% = 1 segundo._
* **hit colour decay time** – quanto tempo a cor de acionamento leva para voltar ao estado anterior após o tempo de sustentação. O valor é em segundos (0–1). _100% = 1 segundo._

{% hint style="info" %}
Se o seu conteúdo já for branco puro, definir a cor de acionamento como branco não fará diferença. Para obter melhores resultados, use uma cor saturada no seu conteúdo e defina **hit colour** como branco — isso cria um efeito de flash muito bom quando as notas são acionadas.
{% endhint %}

* **note off fade out time** – quanto tempo a nota leva para desaparecer depois de ser solta. O valor é em segundos (0–1). _100% = 1 segundo._
* **hit scale factor** – quanto a nota aumenta de escala quando é acionada (por exemplo, 2 = o dobro do tamanho).
* **hit scale hold time** – por quanto tempo a nota permanece aumentada antes de voltar ao tamanho normal. O valor é em segundos (0–1). _100% = 1 segundo._
* **hit scale decay time** – quanto tempo a nota leva para voltar ao tamanho original. O valor é em segundos (0–1). _100% = 1 segundo._
* **note off shrink time** – quanto tempo leva para encolher de volta ao tamanho original depois que a nota é solta. O valor é em segundos (0–1). _100% = 1 segundo._ (Não tem efeito quando **leave all notes visible** está ativado.)

{% hint style="info" %}
Escala — observe que, se o seu conteúdo for um único ponto, a escala não terá efeito!
{% endhint %}
