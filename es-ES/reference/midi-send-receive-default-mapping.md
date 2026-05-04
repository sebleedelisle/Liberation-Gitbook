---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Asignación predeterminada de envío/recepción MIDI

**Los clips se activan y desactivan mediante MIDI note on / off en los canales 1 a 14**

Los Clips tienen una posición horizontal (x) y vertical (y). Haz clic derecho en un Clip y verás su posición. MIDI puede disparar Clips empezando en 0,0.

{% hint style="info" %}
Ten en cuenta que el control de clips con este sistema es absoluto y que las posiciones de los clips no cambian al desplazarte por el Clip Deck.
{% endhint %}

El canal MIDI 1, nota 1 corresponde al Clip 0,0; la nota 2 al Clip 0,1; la nota 3 al Clip 0,2, avanzando hacia abajo por filas y a lo largo por columnas. Cuando llega a 128, pasa al siguiente canal y vuelve a empezar. Por tanto, tienes un total de 128 x 14 = 1792 Clips accesibles mediante MIDI.

Nota MIDI para coordenadas de clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Nota : 1</td><td>Nota : 6</td><td>Nota : 11</td><td>Nota : 16</td><td>Nota : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Nota : 2</td><td>Nota : 7</td><td>Nota : 12</td><td>Nota : 17</td><td>...etc.</td></tr><tr><td><strong>y : 2</strong></td><td>Nota : 3</td><td>Nota : 8</td><td>Nota : 13</td><td>Nota : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Nota : 4</td><td>Nota : 9</td><td>Nota : 14</td><td>Nota : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Nota : 5</td><td>Nota : 10</td><td>Nota : 15</td><td>Nota : 20</td><td></td></tr></tbody></table>

Ten en cuenta que un evento MIDI note on inicia el clip, y el evento note off equivalente lo detiene. Esto ocurre independientemente del modo de disparo del grupo. El sistema se diseñó originalmente para reproducción y grabación, por lo que no era deseable que las notas alternasen el estado de un clip.

### **Effects**

Los mensajes MIDI control change (CC) en el **canal 15** ajustan los efectos.\
El efecto 1 usa CC 0-3, valor 0-127\
El efecto 2 usa CC 4-7, valor 0-127\
El efecto 3 usa CC 8-11, valor 0-127\
… y así sucesivamente.

Cada grupo de cuatro controla el nivel y 3 parámetros de ese efecto:

<table><thead><tr><th width="164">Efecto :</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Nivel</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Parámetro 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...etc.</td></tr><tr><td><strong>Parámetro 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Parámetro 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Global settings**

Los mensajes MIDI control change en el **canal 16** cambian los ajustes globales:\
CC 1 : Shift X (horizontal) 0 -127, 64 está en el centro\
CC 2 : Shift Y (vertical) 0 -127, 64 está en el centro\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Y, algo importante:\
CC 15 : Global brightness

Ten en cuenta que este sistema se diseñó originalmente para grabación y reproducción, permitiéndote usar Logic, Ableton u otros DAW para crear animaciones en línea de tiempo. Aunque puedes usarlo para control en directo, no se ha optimizado para ese uso, y faltan algunas funciones de control en directo en comparación con la configuración de APC40.
