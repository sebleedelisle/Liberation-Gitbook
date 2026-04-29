---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / sincronización

La sincronización con la música es un elemento fundamental de Liberation; cuando tienes el tempo y los beats alineados con la música, puedes tener la seguridad de que todo irá sincronizado. Si tienes la suerte de recibir MIDI clock (o Ableton Link), no tendrás que preocuparte por sincronizar manualmente. Pero si no es así, no pasa nada: puedes ajustarlo manualmente con la función de tempo _Live_.

Si tienes experiencia con software de música o iluminación, este proceso te resultará familiar. Si no, merece la pena dedicar algo de tiempo a familiarizarte con el sistema y practicar en casa antes de llegar a un directo.

## Panel Tempo

El panel _Tempo_ estará siempre en pantalla y contiene todos los ajustes de sincronización. En la parte superior verás el contador actual de compás/beat y un transporte con botones de reproducción/pausa y rebobinado/avance rápido.

Debajo verás el marcador de beat: cuatro cuadrados que “pulsán” al ritmo. Este _beat marker_ es una visualización extremadamente útil y lo consultarás constantemente mientras uses el sistema de tempo _Live_.

### Ajustar el tempo

Tienes varias opciones para ajustar el tempo:

* Haz clic y arrastra en el control deslizante _Tempo_
* Haz Shift-clic y arrastra en el control deslizante _Tempo_ para cambiar el tempo en incrementos de 0,1
* Haz doble clic en el control deslizante _Tempo_ y escribe el número manualmente
* Usa el knob _Tempo_ del APC40 (pulsa Shift para incrementos de 0,1)
* Tap Tempo

{% hint style="info" %}
El tempo se define en “beats por minuto” y el valor predeterminado tradicional suele ser 120.
{% endhint %}

## Tap Tempo

Ajusta el tempo automáticamente haciendo clic en el botón _TAP_ siguiendo el beat. Ajusta el inicio del compás con el botón _RESET_.

{% hint style="info" %}
El sistema Tap Tempo es lo bastante inteligente como para saber si has dejado de marcar durante un rato o si te has saltado un par de beats. Si empiezas a marcar al doble de velocidad, entenderá que quieres duplicar el tempo; lo mismo ocurre si marcas a medio tiempo.

También es capaz de detectar si hay dos personas marcando el tempo a la vez (por ejemplo, una con el teclado y otra con el APC40). Liberation hará una media de las pulsaciones dobles.
{% endhint %}

#### Comandos de teclado:

T - tap tempo\
R - reset the bar\
Y - redondear el tempo al beat por minuto más cercano.

{% hint style="info" %}
Como la mayor parte de la música actual se crea digitalmente, lo normal es que el tempo sea un número entero redondeado. Así que, si al marcar el tempo parece estar cerca, usa la tecla Y (o mueve el knob de tempo del APC40 un “tick”) para redondearlo a un número entero.
{% endhint %}

#### Controles del APC40:

El APC40 tiene un botón dedicado _TAP TEMPO_, o también puedes usar un pedal conectado para marcar el tempo con el pie.

Usa el knob _TEMPO_ para ajustar. Pulsa _SHIFT_ mientras usas el knob _TEMPO_ para hacer ajustes finos.

Usa el botón _METRONOME_ para **reset the bar**. (Ten en cuenta que el botón _METRONOME_ también se ilumina al ritmo del beat)

Gira el knob _TEMPO_ un “tick” a la derecha o a la izquierda para **redondear el tempo** hacia arriba o hacia abajo a un número entero de BPM.

Consulta también [Referencia de APC40](reference/apc40-reference.md "mention")

### Nudge tempo

Si estás seguro de que estás lo bastante cerca del tempo real pero notas que te vas desfasando, usa los botones _NUDGE_ para corregirlo.

Si el tempo de Liberation se está adelantando a la música, mantén pulsado _NUDGE -_ para ralentizarlo temporalmente hasta que vuelva a alinearse.

Si el tempo de Liberation se está quedando por detrás de la música, mantén pulsado _NUDGE +_ para acelerarlo temporalmente hasta que vuelva a alinearse.

{% hint style="info" %}
Puedes usar los botones NUDGE en pantalla o los botones dedicados del APC40.
{% endhint %}

### Medio tiempo / doble tiempo

Usa los botones _÷2_ y _x2_ para dividir el tempo a la mitad o duplicarlo de forma permanente. A diferencia del multiplicador de tempo, este es un cambio permanente del tempo actual.

## Tempo Multiplier

El sistema _Tempo Multiplier_ te permite ajustar temporalmente el tempo antes de volver al valor que tenía antes.

Activa o desactiva _Tempo Multiplier_ pulsando el botón _TEMPO MULTIPLIER_ o el botón _BANK_ del APC40. Ajusta el valor con el control deslizante en pantalla o usando el slider A-B del APC40. También puedes usar los botones de preset _25%, 50%, 100% 200%_.

## Fuentes de tempo externas

### MIDI Clock

Para sincronizar con una señal MIDI clock externa, selecciona el botón de opción _MIDI CLOCK_ y elige el dispositivo MIDI en el menú desplegable. Fíjate en la luz de estado de color situada junto a los menús desplegables:

* Verde: se está recibiendo una señal MIDI clock
* Naranja: puede conectarse al dispositivo MIDI, pero no hay señal de clock actualmente
* Rojo: no puede conectarse al dispositivo MIDI

{% hint style="info" %}
MIDI Clock emite una serie de frames (24 por negra), pero los mensajes no incluyen datos de posición. Esto significa que resulta útil para mantener el tempo, aunque puede que aún tengas que reiniciar el compás.

La fuente de tempo MIDI Clock de Liberation también responde a mensajes **MIDI Machine Control (MMC)**, así que, si tu fuente de clock los transmite, no tendrás que reiniciar el compás manualmente.
{% endhint %}



### Timeline

Cada timeline tiene su propio tempo, que puede ser un valor fijo o un _Tempo Map_. El _Tempo Map_ te permite ajustar el tempo en momentos concretos dentro de la timeline.

El tempo de la timeline se usará cuando _TIMELINE_ esté seleccionado como fuente de tempo.

{% hint style="info" %}
Puedes ejecutar una timeline junto con _cualquiera_ de las fuentes de tempo. Así que, si tienes una banda en directo que no toca con click, puedes iniciar la timeline manualmente y mantenerla sincronizada usando la fuente de tempo _LIVE_. O, si tienes una señal MIDI clock, también puedes usarla.
{% endhint %}
