---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Visão geral do controle MIDI

Há várias formas de usar MIDI no Liberation:

* Como controlador ao vivo. O APC40 Mk1/Mk2, APC Mini e MIDI Fighter Twister podem se conectar automaticamente quando o dispositivo correspondente estiver disponível. Veja [Controladores MIDI ao vivo](live-control-with-the-apc40.md "mention").
* Como fonte de sincronização de clock, usando mensagens de MIDI clock e MIDI song position. Veja [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Como entrada interativa no node MIDI notes para criar efeitos no estilo “harpa laser”. Veja [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Como um sistema mais geral de entrada/saída usando o sistema MIDI Send/Receive. Veja [MIDI Send/Receive](midi-send-receive.md "mention")

Controladores ao vivo compatíveis seguem o estado exibido na tela do Liberation: botões de Clip acendem com as cores dos respectivos grupos, botões de zone mostram o estado da zone, e knobs ou encoders mapeados acompanham o efeito atual ou os controles do painel Parameters.
