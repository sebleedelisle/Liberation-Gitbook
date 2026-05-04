---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Vista general del control MIDI

Liberation usa MIDI de varias formas:

* Como controlador en directo. El APC40 Mk1/Mk2, el APC Mini y el MIDI Fighter Twister pueden conectarse automáticamente cuando el dispositivo correspondiente está disponible. Consulta [Controladores MIDI en directo](live-control-with-the-apc40.md "mention").
* Como fuente de sincronización de reloj, usando mensajes de MIDI clock y de posición de canción MIDI. Consulta [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Como entrada interactiva en el node MIDI notes para crear efectos de tipo “arpa láser”. Consulta [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Como sistema de entrada/salida más general mediante el sistema MIDI Send/Receive. Consulta [MIDI Send/Receive](midi-send-receive.md "mention")

Los controladores en directo compatibles siguen el estado mostrado en pantalla por Liberation: los botones de Clips se iluminan con los colores de sus grupos, los botones de zone muestran el estado de cada zone, y los knobs o encoders mapeados siguen los controles actuales del efecto o del panel Parameters.
