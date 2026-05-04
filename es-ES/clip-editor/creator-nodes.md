---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Nodos Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Crea un único punto / haz.

* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - el color del punto. Consulta [Ajustes de color y HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Crea una línea / lámina.

* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **Size** - la longitud de la línea
* **Colour** - el color de la línea. Consulta [Ajustes de color y HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* **rotation** - el ángulo de la línea, en grados
* **resolution** - consulta [Resolución](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ determina el punto inicial y el centro de rotación de la línea
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Crea un círculo / cono.

* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **radius** - el radio del círculo
* **Colour** - el color del círculo. Consulta [Ajustes de color y HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* **resolution** - consulta [Resolución](fundamentals/resolution.md "mention")
* **Fill state** - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Crea un polígono equilátero: triángulo, cuadrado, pentágono, etc.

* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **size** - la distancia desde el centro hasta cada una de las esquinas
* **Colour** - el color del polígono. Consulta [Ajustes de color y HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* **rotation** - el ángulo de rotación de la forma, en grados
* **resolution** - consulta [Resolución](fundamentals/resolution.md "mention")
* **Fill state** - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Carga un archivo SVG para usar formas personalizadas.

{% hint style="warning" %}
Liberation es compatible con el formato _SVGTiny_. Se recomienda InkScape, aunque la mayoría de aplicaciones de gráficos vectoriales pueden exportar en este formato. Asegúrate de convertir cualquier texto en formas antes de exportar. Liberation renderizará los trazos y, opcionalmente, usará los rellenos como máscaras. Asegúrate de que tus líneas no sean negras, o no se verán sin un modificador de color.
{% endhint %}

* **Import SVG** - carga un archivo SVG desde el disco.

{% hint style="info" %}
Una vez cargado un SVG, el contenido se convierte y se guarda dentro del clip, así que no necesitas conservar una referencia al archivo, salvo que más adelante quieras cambiar los ajustes de máscara.
{% endhint %}

* **Use fills as masks** - procesa cualquier forma rellena como una máscara, es decir, rellenada en negro. Se activará automáticamente si tu SVG tiene alguna forma rellena. Si no tiene formas rellenas, se desactivará. Consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - si las formas de tu SVG no tienen contorno, no podremos dibujarlas. Esta opción añade un contorno (o _stroke_) a cualquier forma rellena. Si tu SVG no tiene ninguna forma con trazo, se activa automáticamente. Si no tiene ninguna forma rellena, se desactiva.
* **Invert black lines** - si todas las líneas de tu SVG son negras, no podrás verlas. Esta opción las vuelve blancas. Se activa automáticamente si tu SVG solo tiene formas negras, pero se desactiva si no tiene ninguna.
* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **scale** - ajusta el tamaño del SVG. Se calcula automáticamente al cargar el SVG (para asegurarse de que la imagen sea visible), pero después puedes editarlo manualmente.
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* **rotation** - el ángulo de rotación de la imagen, en grados
* **resolution** - consulta [Resolución](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Crea una animación a partir de una secuencia de archivos SVG.

* **Import SVG Sequence** - elige la carpeta que contiene todos los archivos SVG. Ten en cuenta que se cargan en orden alfanumérico.

{% hint style="info" %}
Una vez cargada la secuencia SVG, el contenido se convierte y se guarda dentro del clip, así que no necesitas conservar una referencia a los archivos, salvo que más adelante quieras cambiar los ajustes de máscara.
{% endhint %}

* **Use fills as masks** - procesa cualquier forma rellena como una máscara, es decir, rellenada en negro. Se activará automáticamente si alguno de tus SVG tiene formas rellenas. Si ninguno tiene formas rellenas, se desactivará. Consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - si las formas de tus SVG no tienen contornos, no podremos dibujarlas. Esta opción añade un contorno (o _stroke_) a cualquier forma rellena. Si tus SVG no tienen ninguna forma con trazo, se activa automáticamente. Si ninguno tiene formas rellenas, se desactiva.
* **Invert black lines** - si todas las líneas de tus SVG son negras, no podrás verlas. Esta opción las vuelve blancas. Se activa automáticamente si tus SVG solo tienen formas negras, pero se desactiva si no tienen ninguna.
* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **scale** - ajusta el tamaño de la imagen.
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* **rotation** - el ángulo de rotación de la imagen, en grados
* **resolution** - consulta [Resolución](fundamentals/resolution.md "mention")
* **speed** - la duración de la animación completa, en compases.
* **time per frame** - si está activado, la duración se aplica a cada fotograma en lugar de a la duración completa de la animación. Por tanto, si _speed_ está configurado en ¼, cada fotograma durará 1 beat.
* **animation direction** -
  * _FORWARDS_ - la animación avanza y luego vuelve al principio en bucle
  * _BACKWARDS_ - la animación retrocede y luego vuelve al final en bucle
  * _PINGPONG_ - la animación avanza y después retrocede en bucle
  * _MANUAL_ - el fotograma actual se define con el ajuste _position manual_
* **position manual** - define el fotograma actual: 0% es el primer fotograma y 100% es el último. Puedes ajustarlo manualmente o con un oscilador externo.
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Crea texto usando una fuente TrueType u OpenType.

* **Text** - escribe aquí el texto que quieras
* **Font** - elige la fuente que quieras

{% hint style="info" %}
Para añadir más fuentes a Liberation, copia los archivos .ttf u .otf en la carpeta `data/fonts` dentro de la carpeta de trabajo de Liberation y, después, reinicia Liberation.
{% endhint %}

* **Render profile** - consulta [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - elige _LEFT_, _CENTRE_ o _RIGHT_ para seleccionar la alineación del texto.
* **Fill state** - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - el tamaño del texto
* **monospace** - dibuja todos los caracteres con la misma anchura. Es útil para temporizadores y contadores, porque el texto no se desplaza lateralmente cuando cambian los números.
* **character spacing** - ajusta el espacio entre caracteres. Auméntalo para un espaciado más amplio o redúcelo para compactar el texto.
* **colour -** consulta [Ajustes de color y HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** y **y** position - consulta [Sistema de coordenadas](fundamentals/co-ordinate-system.md "mention")
* **rotation** - el ángulo de rotación de la imagen, en grados
* **resolution** - consulta [Resolución](fundamentals/resolution.md "mention")
* **reveal** - úsalo para revelar gradualmente el texto, carácter a carácter. Cuando esté entre 0 y 50%, el texto aparecerá gradualmente de izquierda a derecha. Cuando esté entre 50% y 100%, el texto desaparecerá de izquierda a derecha. Puedes conectar un oscilador a este socket para crear animaciones.
* **reveal by word** - si está activado, _reveal_ funcionará palabra a palabra en lugar de carácter a carácter.
* **countdown** - sustituye el texto escrito por una cuenta atrás. Cuando la cuenta atrás llega a cero, se muestra el valor normal de **Text**.
* **use seconds** - cuenta en segundos reales. Cuando está desactivado, la cuenta atrás se basa en beats: dos beats cuentan como un segundo, así que 120 bpm coincide con segundos reales.
* **show minutes/seconds** - muestra el tiempo restante en minutos y segundos. Si supera una hora, también incluye las horas.
* **countdown to date/time** - cuenta atrás hasta una fecha y hora UTC específicas, en lugar de contar hacia atrás desde un número.
* **countdown datetime** - define la fecha y hora UTC de destino cuando **countdown to date/time** está activado.
* **start number** - número inicial cuando **countdown to date/time** está desactivado.
* _MOVE TO FRONT / MOVE TO BACK_ - consulta [Rellenos, máscaras y ordenación por profundidad](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Si el menú desplegable de fuentes está abierto, las teclas de flecha arriba y abajo recorren las fuentes disponibles.
{% endhint %}
