---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

El sistema MIDI Send/Receive es independiente de los controles APC40 y sirve para enviar datos MIDI hacia Liberation y recibirlos desde Liberation. Funciones como iniciar y detener clips, ajustar opciones globales, efectos y parámetros de clips tienen todas un comando MIDI asociado.

{% hint style="info" %}
El sistema MIDI Send/Receive se creó inicialmente antes de que Liberation tuviera funcionalidad de Timeline; era una solución alternativa que podías usar para grabar y reproducir un show en software musical como Logic Pro o Cubase.

Te ofrece control directo sobre clips, efectos y ajustes, independientemente de la visualización y de la posición de desplazamiento del Clip Deck. No están implementadas capacidades de control en directo más generales, como tap tempo, asignación de zonas y armado/desarmado.
{% endhint %}

### Ajustes de MIDI Send/Receive

Abre el panel _MIDI Send/Receive_ con el menú _View -> MIDI Send/Receive_. Verás que tienes opciones para _SEND, RECEIVE,_ o _BOTH_ enviar y recibir, además de poder elegir qué interfaces MIDI quieres usar.

{% hint style="danger" %}
Usa el ajuste _BOTH_ con precaución. Los dispositivos y el software MIDI pueden configurarse para devolver los datos que reciben; esto podría provocar un bucle de realimentación de datos MIDI, ¡y eso no es nada recomendable!
{% endhint %}

### Mapeo MIDI

Consulta [Asignación predeterminada de envío/recepción MIDI](../reference/midi-send-receive-default-mapping.md "mention")

Tengo previsto añadir un mapeo MIDI mucho más personalizable en el futuro, pero mientras tanto puedes usar aplicaciones como [BOME](https://www.bome.com/products/miditranslator) y [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) para traducir entre Liberation y tu hardware personalizado.
