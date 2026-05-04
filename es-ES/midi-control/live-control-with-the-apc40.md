---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Controladores MIDI en directo

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **Controlador APC40**

Este es el controlador hardware predeterminado para Liberation; es muy recomendable y puede decirse que Liberation se ha diseñado en torno a este hardware desde el principio. En cuanto conectas el APC40, Liberation se conecta automáticamente a él.

{% hint style="warning" %}
_¡Oh, no! ¡Se me ha desconectado el USB en mitad de un show!_

No te preocupes: vuelve a conectarlo y Liberation se reconectará automáticamente, sin complicaciones.
{% endhint %}

### ¿APC40 Mark 1 o Mark 2?

En resumen, se recomienda el Mark 2 porque tiene botones a todo color que coinciden mejor con la interfaz del Clip Deck de Liberation. La versión Mark 1 puede servir en caso de apuro, pero resultará algo más confusa, ya que la distribución es ligeramente distinta a la que aparece en pantalla, y los botones solo pueden iluminarse en rojo, naranja o verde, por lo que no coincidirán con los colores de los clips.

{% hint style="info" %}
El APC40 Mark 1 original salió en 2009 (!) y algunas personas todavía lo prefieren por su construcción con cuerpo metálico y su formato robusto, similar al de una consola. El Mark 2 actualizado salió en 2014 y, aunque se dejó de fabricar en 2024, volverá a producirse en 2025 debido a la demanda de artistas visuales (Resolume, etc.) y laseristas.
{% endhint %}

Para ver la lista completa de controles disponibles en el APC40, consulta [Referencia de APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 también incluye un perfil para APC Mini. Asigna la cuadrícula de Clips 8x5, los botones de zone, los controles de inversión X/Y de zone, los botones de grupo, la detención de todos los Clips, el desplazamiento de página de Clips, el desplazamiento de página de zone, tap tempo, el reinicio de compás y el ajuste fino de tempo. Sus faders controlan los niveles de efecto, y los faders con Shift controlan los parámetros de efecto. El último fader controla el brillo global.

### MIDI Fighter Twister

El perfil MIDI Fighter Twister está pensado para un control centrado en encoders, más que para lanzar Clips. Una fila de encoders controla el parámetro 1 de los slots de efecto 1-8, y otra fila sigue los ocho controles contextuales del panel Parameters, incluidos el desplazamiento de Clip, el retardo de zone, el giro/escala global y los fundidos de grupo.
