---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

O Liberation oferece suporte à sincronização com um sinal externo de timecode SMPTE/LTC, comumente usado em shows de música ao vivo para manter luzes, pirotecnia, vídeo e trilhas de apoio sincronizados.

{% hint style="info" %}
O que é SMPTE/LTC?

SMPTE é um padrão de timecode, e LTC é esse timecode convertido em um sinal de áudio. Se você ouvir esse áudio, ele parece um chiado agudo horrível, mas para computadores ele é uma informação de temporização de alta resolução.

**Curiosidades nerd!**

Historicamente, SMPTE tem sido usado para manter vídeo e áudio em sincronia. Ao sincronizar com fita analógica, uma das trilhas tinha o áudio de timecode gravado nela, algo às vezes chamado de "striping" da fita. Você podia usar essa trilha de timecode para manter vários gravadores de fita sincronizados entre si, ou para manter um sequenciador MIDI sincronizado com a fita. (Assim você não precisava gravar instrumentos MIDI na fita; bastava deixar o sequenciador tocá-los ao vivo enquanto você mixava!)

SMPTE significa Society of Motion Picture and Television Engineers, a organização que definiu o padrão. LTC significa _Linear TimeCode._
{% endhint %}

Você pode receber um sinal de timecode LTC por qualquer interface de áudio no seu computador, mas é recomendado usar uma interface profissional com pelo menos uma entrada XLR ajustável e recurso de monitoração.

Tive uma boa experiência com a [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), pois ela tem monitoração por fones, 2 entradas XLR e não precisa de drivers especiais (pelo menos no macOS). Se você for usá-la apenas para timecode, pode comprar a [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html), que é um pouco mais barata (tem apenas uma entrada e não tem MIDI), mas, sinceramente, qualquer interface de áudio razoável deve funcionar.

{% hint style="info" %}
Sinais de timecode LTC normalmente são distribuídos por cabos XLR balanceados, pois eles são robustos o suficiente para transmitir sinais de áudio de baixo nível por longas distâncias. (XLR é o conector cilíndrico geralmente usado com microfones)
{% endhint %}

### Conexões de hardware

Conecte o cabo XLR do sinal de timecode à sua interface de áudio e verifique se você está recebendo um bom sinal. Ajuste o nível na interface de áudio até que o sinal fique forte, mas sem clipar. Se a sua interface de áudio tiver uma saída para fones, você pode ouvir o timecode e confirmar que ele não está falhando e não tem ruído em excesso.

{% hint style="info" %}
Em teoria, é possível receber o sinal pelo conector jack do seu MacBook, mas isso exigiria um cabo personalizado. Esses conectores normalmente são mini jacks TRRS de 4 polos, e sinceramente não tenho certeza de quais desses contatos podem ser usados como entrada de áudio. Também não tenho certeza de qual nível de tensão ele suporta (li em algum lugar que era +/-1V, mas use isso por sua conta e risco!)

Acho que é melhor simplesmente conseguir uma interface de áudio USB barata em vez de tentar fazer isso.
{% endhint %}

Se a sua interface de áudio não tiver nenhum tipo de monitoração de entrada, você pode verificar nos ajustes do sistema do macOS (em _Sound_) para confirmar que está recebendo um sinal. (No Windows, use o _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>O macOS mostra o nível de entrada de qualquer interface de áudio no painel de ajustes do sistema Sound</p></figcaption></figure>

### Configuração no Liberation

1. Selecione sua interface de áudio e o canal de entrada correto na janela Timecode settings Window.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Observe que há opções separadas no menu suspenso para cada canal de entrada da sua interface de áudio

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Observe o quadrado à esquerda: se você estiver recebendo um sinal de timecode válido, ele ficará verde. Caso contrário, ficará vermelho.

2. Selecione o framerate correto para o timecode de entrada. Quem estiver fornecendo o timecode deve conseguir informar qual é o frame rate. (Se você selecionar errado, ele ainda vai sincronizar, mas você perceberá um pequeno "pulo" a cada segundo)
3. Abra as configurações de timecode da Timeline usando o pequeno ícone de relógio na barra da timeline e escolha a opção SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Ajuste o start offset (em horas, minutos, segundos e frames) para corresponder ao início da música. Se você tiver várias timelines, precisará configurar essas opções separadamente para cada uma.

{% hint style="info" %}
É uma convenção comum no mundo das turnês fazer cada música começar em uma hora diferente, ou seja, 01:00:00:00 para a primeira música, 02:00:00:00 para a segunda música, e assim por diante.

O Liberation trocará automaticamente para a timeline correspondente ao timecode, então você nunca precisa mudar de timeline manualmente durante um show.
{% endhint %}

Observe que, ao contrário do MIDI Clock e do Ableton Link, SMPTE é um sistema de tempo _absoluto_, medido em horas, minutos, segundos e frames. O sistema de tempo central do Liberation é baseado em beats e bars, então, ao receber timecode, ele usará o tempo definido na timeline. Você precisa garantir que esse tempo esteja sincronizado com a música que também estiver sincronizada ao timecode.
