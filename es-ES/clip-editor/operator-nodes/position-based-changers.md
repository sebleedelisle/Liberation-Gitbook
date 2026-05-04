---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Cambiadores basados en la posición

Esta familia de nodos modifica el contenido según la posición. De forma predeterminada, el efecto se aplica a lo largo de un eje horizontal (de izquierda a derecha), pero puedes girar este eje a cualquier ángulo. Cada nodo también incluye un modo _radial_, en el que el efecto depende del ángulo de cada punto respecto al centro.

* **Colour Changer by Position** – aplica un degradado a lo largo del eje elegido o alrededor del ángulo radial.\
  \&#xNAN;_Ejemplo: crea un degradado arcoíris que recorra una línea, o usa el modo radial sobre un círculo para producir un efecto de rueda de color._
* **Wave Shift by Position** – aplica una distorsión de onda sinusoidal, desplazando el contenido verticalmente (o en perpendicular al eje elegido).\
  \&#xNAN;_Ejemplo: haz que una línea ondule como el agua, o usa el modo radial para hacer que un círculo pulse hacia fuera desde el centro._
* **Noise Shift by Position** – aplica una distorsión de ruido simplex, desplazando el contenido verticalmente (o en perpendicular al eje elegido).\
  \&#xNAN;_Ejemplo: consulta el ejemplo de Wave Shift, pero con un carácter más orgánico y aleatorio, perfecto para añadir variación natural._

## &#x20;Cambio de color por posición

Este nodo aplica cambios de color al contenido según la posición. De forma predeterminada, el eje es horizontal (0°), pero puedes girarlo o cambiar al modo radial.

* **wavelength** – define el tamaño del ciclo de color repetido.
  * _Modo lineal:_ al 100%, un ciclo completo abarca todo el ancho del contenido.
  * _Modo radial:_ al 100%, un ciclo completo abarca todo el círculo (360°). Los valores son porcentajes del círculo: por ejemplo, 50% = medio círculo (180°).
* **offset** – desplaza el punto inicial del ciclo de color, como porcentaje de la wavelength. Puedes modularlo (por ejemplo, con un oscilador de diente de sierra) para recorrer los colores de forma suave.
* **repeat** – si está activado, el ciclo se repite a lo largo del contenido. Si está desactivado, el degradado se aplica solo una vez: todo lo anterior al inicio usa el color inicial, y todo lo posterior al final usa el color final.
* **pingpong** – si está activado, cada repetición alterna la dirección, creando un efecto espejado. Si _Repeat_ está desactivado, el degradado avanza y luego retrocede una vez. _Nota: en modo Pingpong, la wavelength cubre tanto el barrido de ida como el de vuelta._
* **linear angle** – gira el eje del efecto. 0° = horizontal.
* **radial** – cambia al modo radial, aplicando colores según el ángulo desde el centro.
* **radial smooth loop** – ajusta automáticamente la wavelength para que divida de forma exacta el 100% del círculo, evitando una costura visible donde se cierra el ciclo.
* **legacy mode** – vuelve a los controles antiguos de HSB de inicio/fin. Déjalo desactivado para usar el editor de degradados nuevo.

**Colour Modes**

Estos modos determinan qué aspectos de los ajustes de color se aplican al contenido. Consulta también: [Ajustes de color y HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – el hue no cambia.
  * _FIXED_ – el hue se fuerza a un valor fijo.
  * _SHIFTED_ – el hue se desplaza según la cantidad especificada (los elementos con distintos colores siguen siendo distintos, pero se desplazan juntos alrededor de la rueda de color).
* **saturation mode**
  * _OFF_ – la saturation no cambia.
  * _FIXED_ – la saturation se fija en el valor especificado.
* **brightness mode**
  * _OFF_ – el brightness no cambia.
  * _FIXED_ – el brightness se fija en el valor especificado.
  * _MULTIPLY_ – el brightness se escala según el valor especificado. Esto conserva la dinámica (por ejemplo, los elementos que parpadean siguen parpadeando, pero dentro del rango de brillo limitado).

**Gradient editor**

Usa el mismo editor de degradados que [Colour Changer](colour-changer.md "mention"), pero asigna el degradado al contenido según la posición.

* Haz clic en la barra de degradado para añadir un punto de color.
* Haz clic izquierdo en un punto para seleccionarlo y arrástralo lateralmente para moverlo.
* Arrastra un punto seleccionado hacia abajo, alejándolo de la barra, o pulsa Delete/Backspace para eliminarlo. Un degradado siempre conserva al menos dos puntos.
* Haz clic derecho en un punto para editarlo con el selector de color.
* Usa **Position**, **Hue**, **Saturation** y **Brightness** para editar con precisión el punto seleccionado.
* **interpolation** elige cómo se mezclan los colores entre puntos:
* **HSB** – mezcla hue, saturation y brightness. Es la mejor opción para movimientos suaves de tipo arcoíris alrededor de la rueda de color.
* **RGB** – mezcla directamente los valores de rojo, verde y azul. A menudo se parece más a un fundido de color en una pantalla o una consola de iluminación.
* **NONE** – salta de un punto al siguiente sin mezcla.
* **hue direction** está disponible con interpolación HSB:
* **AUTO** – toma la ruta más corta alrededor de la rueda de hue.
* **FORWARDS** – avanza siempre por los valores de hue.
* **BACKWARDS** – retrocede siempre por los valores de hue.
* **blend** – mezcla el cambio de color con los colores originales. Al 100%, el efecto sustituye por completo los colores originales.

**Valores de inicio/fin heredados**

Si **legacy mode** está activado, el editor de degradados se sustituye por los controles antiguos:

* **start hue / end hue** – hue al inicio y al final del rango.
* **start saturation / end saturation** – saturation al inicio y al final del rango.
* **start brightness / end brightness** – brightness al inicio y al final del rango.

**Ejemplo 1: degradado arcoíris deslizante**

Partiendo de los ajustes predeterminados:

1. Deja el nodo en modo **Linear** (ángulo de 0° = horizontal).
2. Deja **wavelength** al 100% (abarca todo el ancho y debería ser el valor predeterminado).
3. Deja el degradado predeterminado como está.
4. Activa **repeat**.
5. Añade un **Sawtooth Oscillator** al ajuste **offset** que vaya del 0% al 100%.

***

**Ejemplo 2: degradado negro–blanco–negro (Pingpong)**

Partiendo de los ajustes predeterminados:

1. Deja el nodo en modo **Linear** (ángulo de 0° = horizontal).
2. Deja **wavelength** al 100% (abarca todo el ancho y debería ser el valor predeterminado).
3. Desactiva **repeat**.
4. Ajusta el primer punto del degradado a negro.
5. Ajusta el último punto del degradado a blanco.
6. Ajusta **hue mode** a OFF.
7. Ajusta **saturation mode** a FIXED si quieres forzar el resultado a escala de grises.
8. Ajusta **brightness mode** a FIXED.
9. Activa **pingpong**.

_Resultado: el degradado pasa de negro a blanco y luego vuelve a negro a lo largo del ancho._\
Ten en cuenta que, si quieres que el contenido mantenga su hue y saturation, debes poner Saturation mode en OFF. \\

***

**Ejemplo 3: rueda arcoíris giratoria (radial)**

1. Activa el modo **radial**.
2. Ajusta **wavelength** al 100% (un barrido completo de 360°).
3. Activa **repeat**.
4. Añade un **Sawtooth Oscillator** al ajuste **offset** que vaya del 0% al 100%.

_Resultado: una rueda de color continua que gira sin costuras alrededor del círculo._

## &#x20;Desplazamiento de onda por posición

Este nodo aplica una distorsión de onda al contenido, desplazando los puntos en perpendicular al eje elegido (o radialmente desde el centro).

* **Wavelength** – define la longitud del ciclo de la onda.
  * _Modo lineal:_ al 100%, un ciclo completo abarca todo el ancho del contenido.
  * _Modo radial:_ al 100%, un ciclo completo abarca los 360°. (Los valores son porcentajes del círculo: 50% = media vuelta, 25% = un cuarto de vuelta, etc.)
* **Size** – controla la amplitud de la onda (cuánto se desplaza el contenido).
* **Offset** – desplaza la onda a lo largo del eje (o alrededor del círculo en modo radial). Es un porcentaje de la wavelength, así que puedes animarlo con un **Oscillator Node** para hacer que la onda viaje.
* **Radial** – cambia del modo lineal al modo radial, de modo que el desplazamiento se basa en el ángulo desde el centro.
* **Radial Smooth Loop** – ajusta la wavelength para que divida de forma exacta el 100% del círculo, evitando costuras visibles en el punto de cierre.
* **Triangle** – cambia la forma de onda de sinusoidal a triangular.
* **Absolute** – toma el valor absoluto de la onda, creando solo desplazamientos hacia arriba (plegando la parte negativa sobre la positiva).
* **Angle** – gira el eje de la onda. 0° = horizontal.

## &#x20;Desplazamiento de ruido por posición

Este nodo distorsiona el contenido usando un campo de ruido (como turbulencia), desplazando los puntos en perpendicular al eje elegido (o radialmente desde el centro). En comparación con _Wave Shift_, el resultado es más orgánico y aleatorio.

* **Detail** – controla lo fino que es el ruido. Los valores más altos generan variaciones más nítidas y detalladas. Los valores más bajos generan variaciones más suaves.
* **Wavelength** – define la escala del patrón de ruido.
  * _Modo lineal:_ al 100%, un ciclo completo de ruido abarca el ancho del contenido.
  * _Modo radial:_ al 100%, un ciclo completo abarca los 360°.
* **Size** – controla la cantidad de desplazamiento (amplitud de la distorsión de ruido).
* **Offset** – desplaza el patrón de ruido a lo largo del eje (o alrededor del círculo). Es un porcentaje de la wavelength, así que puedes animarlo con un **Oscillator Node** para hacer que el ruido “fluya”.
* **Depth Offset** – se desplaza a través del campo de ruido 3D, creando variación con el tiempo. Es especialmente eficaz cuando se anima con un Oscillator Node.
* **Depth Detail** – controla el nivel de detalle de la variación en la dimensión de profundidad.
* **Absolute** – toma el valor absoluto del ruido, plegando los valores negativos en positivos (produciendo desplazamiento solo hacia un lado).
* **Angle** – rota el eje del ruido en modo lineal. 0° = horizontal.
* **Radial** – cambia del modo lineal al modo radial, de modo que el desplazamiento se basa en el ángulo desde el centro.
* **Radial Smooth Loop** – ajusta la wavelength para que divida de forma exacta el 100% del círculo, evitando costuras visibles en modo radial.
