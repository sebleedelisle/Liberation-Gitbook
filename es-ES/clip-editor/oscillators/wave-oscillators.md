---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Osciladores de onda

## En esta página:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Onda de diente de sierra](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Onda triangular](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Onda sinusoidal](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Onda cuadrada](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Osciladores de onda](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Ajustes de los osciladores de onda

Todos los osciladores de onda tienen los siguientes ajustes:

* **range min / range max** - determina el rango de valores de la propiedad que controla el oscilador. La propiedad se establece en _range min_ cuando la forma de onda está en la parte inferior, y en _range max_ cuando la forma de onda está en la parte superior.

{% hint style="info" %}
Por ejemplo, si quieres que un punto se mueva a izquierda y derecha entre -100 y 100, conecta el oscilador al _x property socket_, ajusta _min range_ a -100 y _max range_ a 100.
{% endhint %}

* **duration** - el tiempo que tarda en completarse un ciclo completo (o _loop_). Es relativo al tempo en compases. Por tanto, ¼ es un solo pulso. 1 es un compás completo, etc.
* **duration multiplier** - escala la duración base por un factor elegido. Por ejemplo, si duration está ajustado a una negra y el multiplicador es 3, el oscilador durará tres negras (una blanca con puntillo). También se admiten multiplicadores fraccionarios: mantén pulsado _SHIFT_ mientras arrastras el deslizador para definir números no enteros, algo útil para efectos de fase o para crear pequeños desplazamientos de temporización.
* **offset** - el desplazamiento inicial de la onda como porcentaje de la duración. Si quieres que la onda empiece a un cuarto de su recorrido, ajústalo al 25%.
* **repeat count** - el número de veces que se ejecuta el loop antes de detenerse. El valor predeterminado es _FOREVER_, pero puedes cambiarlo si no quieres que el oscilador se ejecute indefinidamente. Cuando se detiene, la propiedad se establece en el valor del final de la onda.
* **delay count** - el retardo en pulsos antes de que el oscilador empiece a ejecutarse. Antes de empezar, la propiedad se establece en el valor del inicio de la onda.

{% hint style="info" %}
Con un uso cuidadoso de _repeat count_ y _delay count_ puedes crear animaciones muy complejas, casi como si fuera su propia línea de tiempo.
{% endhint %}

## Ajustes comunes

* **steps** - divide el movimiento en un número de pasos discretos. Es útil cuando quieres que las propiedades “salten” entre valores en lugar de moverse suavemente.

{% hint style="info" %}
Ten en cuenta que los pasos se dividen por tiempo, no por valor. Así que, en una onda dividida en 4 pasos con una duración de 1 compás, la propiedad cambiará instantáneamente en cada pulso.
{% endhint %}

* **clamp min / clamp max -** aumenta la escala de la onda más allá de sus valores mínimo o máximo y limita el resultado.

{% hint style="info" %}
El concepto de _clamp_ es un poco difícil de explicar, pero imagina que la forma de onda se sale por arriba o por abajo del gráfico y luego queda limitada a los bordes. Te recomiendo que experimentes con estos ajustes. Son muy útiles si quieres que un diente de sierra empiece tarde o termine pronto.
{% endhint %}

* **ease function** - las ondas Sawtooth y Triangle también tienen una función de suavizado que cambia sutilmente la curva de animación y puede hacer que tus animaciones sean mucho más expresivas.
  * **LINEAR** - el valor predeterminado, sin suavizado; simplemente se mueve de forma lineal entre los valores mínimo y máximo.
* **EASE OUT** - empieza rápido y luego reduce la velocidad al acercarse al final. Muy útil para simular física, por ejemplo, una desaceleración hasta detenerse.
  * **EASE IN** - empieza despacio y acelera gradualmente. Útil para simular acumulación de impulso.
  * **EASE IN/OUT** - una combinación de ambos, con un movimiento muy orgánico.

{% hint style="warning" %}
**Easing -** te recomiendo evitar la animación lineal predeterminada siempre que puedas, salvo que busques específicamente algo con aspecto robótico. El suavizado puede hacer que tus animaciones sean mucho más fluidas y orgánicas.
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Onda de diente de sierra

También se conoce a veces como _forma de onda de rampa_, porque asciende en rampa y luego cae bruscamente al final de su ciclo. Probablemente es el oscilador de onda más habitual, porque crea un loop para recorrer propiedades como _hue_ o _rotation_.

Consulta las secciones anteriores para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Específico de Sawtooth:

* **cycle range compensation** - disponible cuando **steps** está activado, y útil para recorrer valores, por ejemplo una rotación de 0 a 360. Cuando no está activado, los valores inicial y final son iguales, lo que puede provocar que se quede enganchado en el punto inicial (porque 0 y 360 son el mismo ángulo). Actívalo y el rango máximo se reducirá para corregir las posiciones de los pasos.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Onda triangular

A diferencia de la _onda de diente de sierra_, que vuelve al principio en cada ciclo, la _onda triangular_ se mueve linealmente hacia delante y luego hacia atrás.

Consulta las secciones anteriores para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Onda sinusoidal

La forma de onda más suave. Oscila suavemente entre dos valores, como un péndulo.

Consulta las secciones anteriores para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Onda cuadrada

La forma de onda más sencilla: simplemente alterna entre dos valores, de un lado a otro.

Consulta las secciones anteriores para:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Específico de Square wave:

* **pulse width** - el tiempo durante el cual la onda permanece en su valor máximo en relación con la duración total. El valor predeterminado es 50%, exactamente mitad y mitad. Si solo quieres que esté “encendida” durante una cuarta parte del tiempo, ajústalo al 25%. Puedes ajustar cuándo ocurre este pulso usando el valor _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Ruido

Uno de los puntos fuertes de Liberation es que puede generar efectos aleatorios, pero repetibles. El oscilador _noise_ puede usarse para crear un movimiento aleatorio orgánico en loop con tanto detalle o vibración como quieras.

Consulta las secciones anteriores para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Específico de Noise:

* **noise type** - el algoritmo usado para generar el ruido.
  * **SIMPLEX** - el valor predeterminado, un valor ondulante que sube y baja suavemente, y se repite en loop.
  * **RANDOM** - usa un algoritmo de números aleatorios más tradicional, totalmente ruidoso y caótico.

{% hint style="info" %}
**Simplex noise** fue diseñado por Ken Perlin en 2001 como mejora de su algoritmo “Perlin noise”, que desarrolló en 1983 como parte de su trabajo en la película _Tron_ (¡por el que ganó un Óscar!).

Este llamado ruido de “gradiente” nació de su frustración con las imágenes generadas por ordenador que hasta entonces tenían un aspecto demasiado “de máquina”. En el mundo del CGI, es especialmente útil para renderizar nubes, superficies de agua o incluso mapas de altura para terrenos realistas.

Pero en Liberation es útil para crear movimientos aparentemente impredecibles que siguen siendo suaves y orgánicos.
{% endhint %}

* **seed** - el valor usado para crear el ruido. Si no te gusta el aspecto de la onda de ruido que tienes, prueba a cambiar este valor.

{% hint style="info" %}
¡Dato friki! Para conseguir un simplex noise que forme un loop perfecto, recorro un círculo sobre un plano de ruido 2D. Y al cambiar el valor de seed, este plano se mueve a través de una tercera dimensión.
{% endhint %}

* **simplex detail** - cambia el nivel de detalle o vibración del ruido. Si quieres que el patrón repetido sea menos evidente, aumenta la duración y sube este valor.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Crea formas de onda completamente personalizadas. Es muy útil para crear animaciones complejas.

Consulta las secciones anteriores para:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Debajo hay una lista de posiciones y valores. La duración se divide en 64 pasos y puedes colocar un valor en cualquiera de estos puntos.

Cada paso tiene los siguientes ajustes:

* **Step** - el paso temporal dentro de la duración. 0 está al principio y 64 al final.
* **Level** - el nivel de la onda en ese paso temporal. El nivel va de 0 a 1.
* **Animation type** - el menú desplegable te permite elegir cómo quieres moverte hacia este nivel desde el paso anterior.
  * **None** - sin transición; salta directamente a este nivel en el momento indicado.
  * **Linear** - un movimiento completamente lineal desde el nivel anterior hasta este.
  * **Ease in / Ease out / Ease in/out** - suaviza el movimiento entre el nivel anterior y este. Consulta _ease function_ más arriba para ver una descripción de los tipos de animación.

***
