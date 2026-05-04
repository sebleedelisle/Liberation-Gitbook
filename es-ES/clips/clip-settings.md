---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Ajustes de Clip

### Panel Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>El panel de ajustes del clip</p></figcaption></figure>

Cambia el tamaño de salida del clip con _Scale X_ y _Scale Y_. Están vinculados entre sí salvo que pulses la tecla _SHIFT_.

Cambia la posición horizontal y vertical del clip con _Shift X_ y _Shift Y_.

_Zone Delay/Chase_ es una función tan divertida que tiene su propia sección. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Panel Parameters

El panel situado a la derecha del Clip Deck muestra ocho parámetros contextuales. Con un Clip seleccionado, los primeros controles son _Shift X_, _Shift Y_ y _Zone Delay_ del Clip seleccionado, seguidos de los controles globales _Spin_ y _Scale_.

Estos mismos parámetros se replican en los controladores MIDI compatibles. Si no hay ningún Clip seleccionado, los espacios específicos del Clip aparecen en blanco. Si mantienes pulsado un botón de grupo, los dos primeros controles cambian a los tiempos de fundido de entrada y fundido de salida de ese grupo.

### Bloquear clips

Si un clip está bloqueado, no se puede mover ni eliminar. Para bloquear un clip, usa la casilla _Locked_ del menú contextual. En el panel Clip settings tienes algunas opciones más.

* _UNLOCK ALL -_ desbloquea todos los clips del Clip Deck.
* _AUTO-LOCK_ - cuando _Auto-Lock_ está activado, cualquier clip que se reproduzca automáticamente (ya sea con la línea de tiempo o con el sistema de grabación/reproducción MIDI) quedará bloqueado. Esto resulta útil si has programado un show en Logic Pro (o similar) y no quieres editar accidentalmente los clips usados en el show.
* _LOCKED CLIPS ZONES_ - si está activado, no podrás cambiar las zonas de ningún clip bloqueado.
* _LOCKED CLIPS PARAMS_ - si está activado, no podrás cambiar los parámetros (escala, desplazamiento, etc.) de ningún clip bloqueado.

### Menú contextual

Si haces clic derecho en un Clip, aparece un menú con algunas de las opciones de ese Clip. Consulta [Introducción al Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Ajustes de Clip](clip-settings.md "mention") y [Grupos de Clip](groups.md "mention")para saber más sobre los primeros elementos de este menú.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

De forma predeterminada, los clips están configurados como _retrigger_. Esto significa que, pulses cuando pulses, el clip empezará a reproducirse desde ese momento. Así que, si lo lanzas tarde, la animación del clip irá ligeramente tarde y fuera de tiempo.

{% hint style="info" %}
Si usas _Tap Tempo_ mientras se está reproduciendo un clip con retrigger, el sistema “cuantizará” el clip para que quede a tiempo, aunque no lo hayas iniciado exactamente en el pulso.
{% endhint %}

Si _Retrigger_ no está activado, el clip siempre estará a tiempo: es como si el clip se hubiera iniciado justo al principio del reloj. Va bien cuando estás perfectamente sincronizado con la música mediante una señal de reloj externa.

{% hint style="info" %}
Los clips suelen estar diseñados para reproducirse en bucle indefinidamente, pero también puedes diseñarlos para que solo se reproduzcan una vez o unas pocas vueltas. Asegúrate de mantener esos clips con _retrigger_ activado, ¡o no se reiniciarán!
{% endhint %}

### Tiempo de entrada/salida de transición (fundido)

Los Clips se pueden configurar para que hagan fundido de entrada y salida con una duración medida en segundos. De forma predeterminada, el tiempo de fundido se hereda de los ajustes de su grupo (y se puede cambiar haciendo clic derecho en el botón del grupo).

Si quieres una duración de fundido distinta a la del grupo del clip, primero desactiva el botón _USE GROUP DEFAULT_ y después ajusta los deslizadores _In time_ y _Out time_ del clip.
