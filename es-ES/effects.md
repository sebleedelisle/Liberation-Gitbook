---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Efectos

El sistema de efectos de Liberation es una forma divertida y versátil de modificar la salida del clip en tiempo real. Los efectos son totalmente flexibles y pueden servir para hacer que todo parpadee, gire, cambie de color o incluso se mueva de forma aleatoria.

Todo lo que puedes hacer en el editor de clips puede usarse como efecto. De hecho, los efectos se editan con exactamente el mismo editor de nodos que los clips. Consulta [Efectos](effects.md#editing-effects "mention"). Las posibilidades creativas son prácticamente infinitas.

Los botones de efectos predeterminados 1-8 están debajo de los botones de zona, y los efectos 9-24 son los botones pequeños de la parte inferior.

#### Aplicar un efecto

Pulsa un botón de efecto para activar o desactivar el efecto o, mejor aún, usa los sliders 1-8 del APC40 para hacer fundidos de entrada y salida de los efectos. Para hacer aparecer un efecto sin un APC40, haz clic y arrastra arriba y abajo sobre el botón. También puedes hacer clic derecho en el botón del efecto y ajustar el slider de nivel.

{% hint style="warning" %}
Al pulsar el botón del efecto, ese efecto se activará inmediatamente. Sin embargo, ten en cuenta que si el nivel está a cero, no pasará nada. Haz clic y arrastra sobre el botón para cambiar el nivel, haz clic derecho y usa el slider _level_, o utiliza los faders del APC40.
{% endhint %}

#### Efectos y retardo de zona del clip

Los efectos toman el ajuste de retardo de zona de cada clip que se esté ejecutando en ese momento. Así que, si tu clip tiene un retardo que se mueve de izquierda a derecha y añades el efecto de parpadeo, el parpadeo también se retrasa de izquierda a derecha.

{% hint style="info" %}
La forma en que los efectos heredan el retardo de zona del clip es una de esas cosas que resulta muy difícil de describir, pero que se entiende al instante cuando la pruebas.

Diría que es una de las herramientas más divertidas y creativas integradas en Liberation. Pruébala y verás a qué me refiero.
{% endhint %}

#### Parámetros de efecto

Añade un parámetro a tu efecto con un _Parameter node._ El sistema de parámetros permite ajustar desde fuera varios ajustes dentro de tu efecto. Consulta [Parameter Control](clip-editor/oscillators/parameter-control.md "mention") para obtener más información.

Usa los controles giratorios 1-8 para ajustar el _parameter_ de cada efecto. O haz clic derecho en el botón del efecto y ajusta el slider o sliders de parámetro. El cambio de parámetro hace cosas distintas según cómo esté configurado el efecto. Consulta la lista siguiente para ver los efectos predeterminados y qué hacen sus parámetros.

{% hint style="info" %}
Los controles giratorios 1-8 están en la parte superior de un APC40 Mk2 y en la parte superior derecha en el Mk1. Consulta también: [Referencia de APC40](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
Los números pequeños que ves en los botones de efectos se refieren al _level_ y al _parameter_ del efecto. El _level_ se controla con el fader del APC40, o puedes hacer clic y arrastrar sobre el botón. El parámetro se ajusta con los controles giratorios del APC40, o puedes hacer clic derecho para ajustarlo con el ratón.
{% endhint %}

#### Los efectos predeterminados

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Aplica un movimiento caótico a la salida del clip. El parámetro ajusta la cantidad/velocidad del caos.
2. **Sine wave** :\
   Deforma todo el contenido sobre una onda sinusoidal en movimiento. El parámetro ajusta la longitud de onda.
3. **Rotation** :\
   Hace girar todo. El parámetro ajusta la velocidad de giro.
4. **Horizontal flip** :\
   Comprime y estira todo horizontalmente. El parámetro ajusta la velocidad.
5. **Scale** :\
   Escala repetidamente todo desde tamaño completo hasta cero. El parámetro ajusta la velocidad.
6. **Hue** :\
Cambia el tono de todo, pero no cambia la saturación (es decir, todo lo que sea blanco sigue siendo blanco). El parámetro ajusta el tono.
7. **Saturation and hue** :\
Cambia el tono de todo y también satura completamente el color (es decir, todo lo que sea blanco cambia al color). El parámetro ajusta el tono.
8. **Flash** :\
   Hace parpadear repetidamente el brillo de todo desde máximo hasta cero. El parámetro ajusta la velocidad de parpadeo.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Hay otros 16 efectos de color en la fila inferior para aplicar valores predefinidos de tono y saturación.

Ten en cuenta que estos son los efectos predeterminados, pero se pueden editar para que hagan casi cualquier cosa que quieras.

### Apply to groups

Puedes elegir a qué grupos afecta el efecto. Haz clic derecho y activa o desactiva las casillas de grupo etiquetadas como _Apply to groups._

Uso esta configuración principalmente cuando trabajo con gráficos de Canvas y haces láser por separado. Asigno todos los clips de Canvas al grupo 5 y luego excluyo este grupo de los efectos que no quiero que afecten a esos clips gráficos.

También podrías usarlo en directo para aplicar 2 cambios de color distintos a 2 grupos de láseres a la vez. Crea dos efectos de cambio de color y selecciona a qué grupos de clips se aplica cada uno.

### MX group

Abreviatura de _Mutually Exclusive_, es una forma de agrupar efectos de manera que solo un efecto del grupo pueda estar activo al mismo tiempo. Fíjate en que solo uno de los efectos de cambio de color predeterminados puede estar activo a la vez. Esto se debe a que todos están en MX Group 1.

Esta función está desactivada si el ajuste _MX Group_ está en 0.

### Editar efectos

Haz clic derecho en cualquier efecto y pulsa el botón _EDIT EFFECT_ para abrir el editor de efectos. Verás que este editor es idéntico al editor de clips.

Edita tu efecto del mismo modo que editarías cualquier clip. Consulta [El Clip Editor](clip-editor/ "mention").

Necesitas tener al menos un nodo creador; puede ser cualquier cosa (línea, círculo, forma, incluso texto), pero probablemente deberías elegir algo que tenga sentido en la vista previa del botón de efecto.

Cuando se aplican los efectos, todos los nodos creadores del efecto se sustituyen por la salida de los clips que se estén ejecutando en ese momento.

{% hint style="warning" %}
Por motivos técnicos extremadamente tediosos, los nodes "trails" no están habilitados dentro de un efecto. Lo mismo ocurre con el ajuste "delay" dentro de los nodes de patrón (usan el mismo sistema). Esto se corregirá en futuras revisiones.
{% endhint %}
