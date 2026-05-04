---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Cambia los colores de todo el contenido entrante. Puedes definir valores HSB fijos, o cambiar al sistema de degradado y tomar colores de muestra de un degradado personalizado.

* **hue, saturation, brightness** - los valores de color; consulta [Ajustes de color y HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - no se cambia el matiz
  * FIXED - el matiz de los elementos se establece en el valor de matiz
  * SHIFT - el matiz de los elementos se desplaza según el valor, de modo que los elementos con colores distintos seguirán siendo distintos, pero desplazados a lo largo del valor de matiz.
* **saturation mode** -
  * OFF - no se cambia la saturación
  * FIXED - la saturación se fija en el valor especificado.
* **brightness mode** -
  * OFF - no se cambia el brillo
  * FIXED - el brillo de los elementos se establece en el valor de brillo
  * MULTIPLY - el brillo de los elementos se combina con el valor de brillo, de modo que, si están parpadeando, seguirán parpadeando, pero solo hasta el brillo especificado aquí.
* **gradient mode** - cambia de los deslizadores HSB fijos al editor de degradado. El node toma un color de muestra del degradado y lo aplica usando los modos de tono, saturación y brillo anteriores.
* **gradient position** - elige qué punto del degradado se toma como muestra. Anímalo de 0 % a 100 % con un Sawtooth Oscillator para recorrer el degradado con el tiempo.
* **blend** - la intensidad con la que se aplica el cambiador de color: 0% no lo aplica en absoluto, 100% lo aplica por completo y 50% es una combinación del color existente y los nuevos valores.

{% hint style="info" %}
El node Colour Change toma un único color de muestra del degradado para toda la entrada. Si quieres que el degradado se aplique a lo largo de la forma según la posición, usa [modificadores basados en posición](position-based-changers.md "mention") en su lugar.
{% endhint %}

### Editor de degradado

Cuando **gradient mode** está activado, el editor de degradado aparece debajo de los controles principales.

* Haz clic en la barra de degradado para añadir una parada de color.
* Haz clic izquierdo en una parada para seleccionarla y arrástrala lateralmente para moverla.
* Arrastra una parada seleccionada hacia abajo, alejándola de la barra, o pulsa Delete/Backspace para eliminarla. Un degradado siempre mantiene al menos dos paradas.
* Haz clic derecho en una parada para editarla con el selector de color.
* Usa **Position**, **Hue**, **Saturation** y **Brightness** para editar con precisión la parada seleccionada.
* **interpolation** elige cómo se mezclan los colores entre paradas:
* **HSB** - mezcla tono, saturación y brillo. Es la mejor opción para movimientos suaves tipo arcoíris alrededor de la rueda de color.
* **RGB** - mezcla directamente los valores de rojo, verde y azul. A menudo se percibe más como un fundido de color de una pantalla o una consola de iluminación.
* **NONE** - salta de una parada a la siguiente sin mezcla.
* **hue direction** está disponible en la interpolación HSB:
* **AUTO** - toma la ruta más corta alrededor de la rueda de tono.
* **FORWARDS** - siempre avanza a través de los valores de tono.
* **BACKWARDS** - siempre retrocede a través de los valores de tono.
