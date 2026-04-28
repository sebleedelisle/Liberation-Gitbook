---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Ajustes de color y HSB

El color en Liberation se define como HSB en lugar de RGB. Puede que no te resulte familiar, pero me parece un sistema mucho más intuitivo cuando te acostumbras a él.

{% hint style="info" %}
Si prefieres usar RGB, puedes hacer clic en el cuadrado de color en cualquier ajuste de color. Esto abre el panel del editor de color, que te ofrece opciones para RGB y HSB.
{% endhint %}

### HSB - Hue, Saturation y Brightness

#### Hue

El tono de color va de 0 a 255. 0 es rojo y, a medida que aumentas el valor, pasarás por todos los tonos del arcoíris: naranja, amarillo, verde, cian, azul, morado, magenta y de nuevo rojo en 255.

Como es un bucle, puedes usar una onda triangular para recorrer todos los colores.

#### Saturation

Este ajuste modifica la saturación o viveza del color. En otras palabras, lo _colorido_ que es, y va de 0 a 255. Pon la saturación en 0 para obtener grises, y en 255 para colores de arcoíris a plena intensidad. Un valor intermedio te dará colores pastel más apagados.

{% hint style="info" %}
Disculpas a mis amigos de EE. UU. por la vocal adicional en la palabra inglesa colour. Liberation se crea en Inglaterra, así que el inglés británico es el idioma predeterminado. En el futuro espero ofrecer traducciones al francés, español, alemán, italiano, chino simplificado y sí, también al inglés de EE. UU. :innocent:
{% endhint %}

#### Brightness

Probablemente el más fácil de entender: 0 es completamente negro, 255 es brillo máximo.

### Ejemplos de uso

#### Ciclo de arcoíris:

Ajusta _Brightness_ y _Saturation_ a 255. Conecta un oscilador _Sawtooth_ a tu conector _Hue_ y ajusta su rango de 0 a 255.

#### Brillo pulsante:

Conecta un oscilador _Sawtooth_ a tu conector _Brightness_ y ajusta su rango de 255 a 0. También puedes ajustar los valores mínimo y máximo de clamp para controlar la duración del cambio. Después, usa las funciones de easing para refinar aún más la animación.

#### Flash duro / estrobo:

Selecciona un color usando _Hue_ y _Saturation_ o haciendo clic en el selector de color. Conecta un oscilador _Square Wave_ a tu conector _Brightness_ y ajusta su rango de 255 a 0.

#### Recorrer un rango personalizado de tonos:

Ajusta _Brightness_ y _Saturation_ a 255. Conecta un oscilador _Triangle Wave_ a tu conector _Hue_ y ajusta su rango:

* para ir de azul a cian, usa un rango de 70 a 128
* para ir de rojo a amarillo, usa un rango de 0 a 40
* para ir de rojo a magenta, usa un rango de 255 a 220
