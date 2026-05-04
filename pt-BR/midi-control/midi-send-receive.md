---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

O sistema MIDI Send/Receive é separado dos controles do APC40 e é uma forma de enviar e receber dados MIDI no Liberation. Funções como iniciar e parar clips, ajustar configurações globais, efeitos e parâmetros de clip têm, cada uma, um comando MIDI associado.

{% hint style="info" %}
O sistema MIDI Send/Receive foi criado inicialmente antes de o Liberation ter qualquer funcionalidade de Timeline; era uma solução alternativa que você podia usar para gravar e reproduzir um show em softwares de música como Logic Pro ou Cubase.

Ele dá controle direto sobre clips, efeitos e configurações, independentemente da posição de rolagem da tela e do Clip Deck. Recursos mais sistêmicos de controle ao vivo, como tap tempo, atribuição de zones e armar/desarmar, não estão implementados.
{% endhint %}

### Configurações de MIDI Send/Receive

Abra o painel _MIDI Send/Receive_ (pelo menu _View -> MIDI Send/Receive_). Você verá que há opções para _SEND, RECEIVE,_ ou _BOTH_ enviar e receber, além da possibilidade de escolher quais interfaces MIDI deseja usar.

{% hint style="danger" %}
Use a configuração _BOTH_ com cuidado. Dispositivos e softwares MIDI podem ser configurados para reenviar os dados que recebem; isso pode causar um loop de feedback de dados MIDI, e isso não é nada bom!
{% endhint %}

### Mapeamento MIDI

Consulte [Mapeamento padrão de envio/recebimento MIDI](../reference/midi-send-receive-default-mapping.md "mention")

Planejo adicionar um mapeamento MIDI muito mais personalizável no futuro, mas, enquanto isso, você pode usar apps como [BOME](https://www.bome.com/products/miditranslator) e [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) para traduzir entre o Liberation e seu hardware personalizado.
