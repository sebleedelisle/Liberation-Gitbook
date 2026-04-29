---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / sincronização

A sincronização com a música é um elemento fundamental do Liberation. Depois que você ajusta o tempo e os beats para acompanhar a música, pode ter certeza de que tudo ficará sincronizado. Se você tiver a sorte de receber MIDI clock (ou Ableton Link), não precisa se preocupar com sincronização manual. Mas, se não tiver, tudo bem: você pode fazer o ajuste manualmente usando o recurso de tempo _Live_.

Se você tem experiência com softwares de música ou iluminação, esse processo será familiar. Se não tiver, vale a pena dedicar algum tempo para se familiarizar com o sistema e praticar em casa antes de chegar a um show ao vivo.

## Painel Tempo

O painel _Tempo_ fica sempre visível na tela e contém todas as configurações de sincronização. Na parte superior, você verá o contador atual de compasso/beat e um transporte com botões de play/pause e rewind/fastforward.

Abaixo, você verá o marcador de beat: quatro quadrados que “pulsam” no beat. Esse _beat marker_ é uma visualização extremamente útil, e você o consultará constantemente ao usar o sistema de tempo _Live_.

### Definindo o tempo

Você tem algumas opções para definir o tempo:

* Clique e arraste o controle deslizante _Tempo_
* Shift-clique e arraste o controle deslizante _Tempo_ para alterar o tempo em incrementos de 0,1
* Clique duas vezes no controle deslizante _Tempo_ e digite o número manualmente
* Use o knob _Tempo_ no APC40 (pressione shift para incrementos de 0,1)
* Tap Tempo

{% hint style="info" %}
O tempo é definido em “beats por minuto”, e o padrão tradicional geralmente é 120.
{% endhint %}

## Tap Tempo

Defina o tempo automaticamente clicando no botão _TAP_ no ritmo do beat. Defina o início do compasso com o botão _RESET_.

{% hint style="info" %}
O sistema Tap Tempo é inteligente o suficiente para saber se você ficou um tempo sem tocar ou se perdeu alguns beats. Se você começar a tocar em double time, ele entenderá que você quer dobrar o tempo; o mesmo vale se você tocar em half time.

Ele também é inteligente o suficiente para identificar se há duas pessoas tocando o tempo ao mesmo tempo (por exemplo, uma no teclado e outra no APC40). O Liberation fará a média dos toques duplicados.
{% endhint %}

#### Comandos de teclado:

T - tap tempo\
R - reset the bar\
Y - arredonda o tempo para o beat por minuto mais próximo.

{% hint style="info" %}
Como a maior parte da música hoje em dia é criada digitalmente, é provável que o tempo seja um número inteiro arredondado. Então, se o tempo marcado no tap estiver próximo, use a tecla Y (ou mova o knob de tempo do APC40 um “tick”) para arredondar para um número inteiro.
{% endhint %}

#### Controles do APC40:

O APC40 tem um botão dedicado _TAP TEMPO_, ou você também pode usar um footswitch conectado para marcar o tempo com o pé!

Use o knob _TEMPO_ para ajustar. Pressione _SHIFT_ enquanto usa o knob _TEMPO_ para ajustes finos.

Use o botão _METRONOME_ para **reset the bar**. (Observe que o botão _METRONOME_ também acende no ritmo do beat)

Gire o knob _TEMPO_ um “tick” para a direita ou para a esquerda para **round the tempo** para cima ou para baixo até um valor inteiro de BPM.

Veja também [Referência do APC40](reference/apc40-reference.md)

### Nudge tempo

Se você tiver certeza de que está perto o suficiente do tempo real, mas perceber que está saindo do sincronismo, use os botões _NUDGE_ para corrigir.

Se o tempo do Liberation estiver adiantando em relação à música, mantenha pressionado _NUDGE -_ para desacelerar temporariamente até realinhar.

Se o tempo do Liberation estiver atrasando em relação à música, mantenha pressionado _NUDGE +_ para acelerar temporariamente até realinhar.

{% hint style="info" %}
Você pode usar os botões NUDGE na tela ou os botões dedicados no APC40.
{% endhint %}

### Half time / double time

Use os botões _÷2_ e _x2_ para reduzir pela metade ou dobrar o tempo permanentemente. Diferente do multiplicador de tempo, essa é uma alteração permanente no tempo atual.

## Tempo Multiplier

O sistema _Tempo Multiplier_ permite ajustar temporariamente o tempo antes de voltar ao valor anterior.

Ative ou desative o _Tempo Multiplier_ pressionando o botão _TEMPO MULTIPLIER_ ou o botão _BANK_ no APC40. Ajuste usando o controle deslizante na tela ou o slider A-B do APC40. Ou use os botões de preset _25%, 50%, 100% 200%_.

## Fontes externas de tempo

### MIDI Clock

Para sincronizar com um sinal externo de MIDI clock, selecione o botão de opção _MIDI CLOCK_ e escolha o dispositivo MIDI no menu suspenso. Observe a luz de status colorida ao lado dos menus suspensos:

* Verde - recebendo um sinal de MIDI clock
* Laranja - consegue se conectar ao dispositivo MIDI, mas não há sinal de clock no momento
* Vermelho - não consegue se conectar ao dispositivo MIDI

{% hint style="info" %}
O MIDI Clock transmite uma série de frames (24 por semínima), mas não há dados de posição nas mensagens. Isso significa que ele ajuda a manter o tempo, mas talvez você ainda precise resetar o compasso.

A fonte de tempo MIDI Clock do Liberation também responde a mensagens **MIDI Machine Control (MMC)**, portanto, se a sua fonte de clock transmitir essas mensagens, você não precisará resetar o compasso manualmente.
{% endhint %}



### Timeline

Cada timeline tem seu próprio tempo, que pode ser um valor fixo ou um _Tempo Map_. O _Tempo Map_ permite ajustar o tempo em momentos específicos dentro da timeline.

O tempo da timeline será usado quando _TIMELINE_ estiver selecionado como fonte de tempo.

{% hint style="info" %}
Você pode executar uma timeline junto com _qualquer_ uma das fontes de tempo! Então, se você tiver uma banda ao vivo que não toca com click, pode iniciar a timeline manualmente e mantê-la sincronizada usando a fonte de tempo _LIVE_. Ou, se você tiver um sinal de MIDI clock, pode usar esse sinal!
{% endhint %}
