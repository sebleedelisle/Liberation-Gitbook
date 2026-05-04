---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zonas

El tipo principal de zona que usarás en la mayoría de tus proyectos es la _Beam zone_. Es una zona diseñada para efectos de haces atmosféricos en el aire. El otro tipo de zona es una _Canvas zone_ (consulta [Gráficos y el sistema Canvas](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**ADVERTENCIA: ten muchísimo cuidado al mover zonas mientras el láser está en funcionamiento** y baja el brillo al mínimo posible. Consulta [Resumen del proceso de configuración de láseres](../setting-up/setting-up-lasers.md "mention") para ver una guía completa sobre cómo activar y zonificar láseres de forma segura.
{% endhint %}

Puedes hacer clic y arrastrar las zonas con el ratón. Activa un patrón de prueba para ver hacia dónde va esa zona.

{% hint style="info" %}
Usa las teclas de flecha para **desplazar ligeramente** la zona o el punto seleccionado. Pulsa la tecla `Shift` para desplazarlo en pasos más grandes.
{% endhint %}

{% hint style="info" %}
Consejo: puedes copiar rápidamente la configuración de zonas entre varios láseres. Consulta [Copiar ajustes entre láseres](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Añadir una nueva Beam zone

Haz clic en el botón _Add a new beam zone_ en la parte superior de la barra de herramientas y aparecerá una zona nueva. Ten en cuenta que las Beam zones se ordenan según el orden en que las añades, pero puedes reordenarlas. Consulta [Reordenar zonas de haz](re-ordering-beam-zones.md "mention")

### Añadir una Canvas zone existente

Haz clic en el botón _Add existing canvas zone_ y verás una lista de las Canvas zones disponibles; podrás activarlas o desactivarlas para este láser. Consulta [Gráficos y el sistema Canvas](../graphics-and-the-canvas-system/ "mention")

### Tipos de forma de zona

Hay 3 tipos de forma de zona:

* **Quad** - la forma de zona rectangular predeterminada, que puede ser uniforme (alineada a los ejes) o estar distorsionada. Es la mejor opción para zonas rectangulares grandes o Canvas zones que requieren corrección de perspectiva.
* **Line/Curve** - una zona definida por 2 o más puntos y un grosor. Ideal para zonas estrechas o para terminar en balcones, puentes u otras formas curvas.
* **Segmented** - una zona que puede subdividirse en quads más pequeños. Ideal para mapping arquitectónico.

Haz clic derecho en cualquier zona para abrir su configuración. Desde este menú contextual puedes:

* Cambiar el nombre de la zona (esto puede ayudarte a identificarla en el clip deck, especialmente si tienes muchas zonas).
* Activar/desactivar la zona.
* Bloquear su posición.
* Cambiar su tipo de forma.
* Restablecerla a la posición predeterminada.
* Acceder a ajustes específicos del tipo de forma.
* Eliminarla.
* Añadir una _Alt Zone_ (consulta [Sistema de zonas Alt](alt-zone-system.md "mention")).

{% hint style="danger" %}
**ADVERTENCIA:** ten mucho cuidado al cambiar el tipo de zona mientras el láser está activo. La zona volverá a la última posición/tamaño usados para esa forma, por lo que la salida podría cambiar de repente. Es mejor apagar el láser antes de cambiar el tipo de zona.
{% endhint %}

### Forma de zona Quad

Puedes mover cada esquina del quad con el ratón. Haz `Alt / Option`-clic en una esquina para moverla de forma independiente respecto a las demás y distorsionar el quad. Una vez que el quad está distorsionado, todas las esquinas pueden moverse libremente.

Puedes eliminar la distorsión y devolverla a un rectángulo alineado a los ejes usando el botón _REMOVE DISTORTION_ del menú contextual.

#### Corrección de perspectiva

Esta opción se puede ajustar con el botón de activación del menú contextual y determina el método de distorsión. Para haces, normalmente es mejor mantenerla desactivada, pero si esta zona proyecta gráficos sobre un plano, actívala y la salida se corregirá en perspectiva.

{% hint style="info" %}
Si _Perspective correction_ está desactivada, el contenido se distorsiona usando _interpolación bilineal_. En otras palabras, el contenido se distribuye de forma uniforme por todo el quad. Por eso es la mejor opción para haces.

Con la corrección de perspectiva activada, el contenido se distorsiona mediante una deformación de perspectiva que compensa el escorzo. Así, si proyectas gráficos sobre una pared con un ángulo oblicuo, puedes usar esta opción para desdistorsionar la salida y corregir la distorsión de la proyección.
{% endhint %}

### Forma de zona Line / Curve

La forma de zona Line / Curve se ha convertido en mi opción habitual en shows recientes, y se podría decir que debería ser la predeterminada para las Beam zones.

Muy a menudo, mis zonas tienen que ser estrechas para encajar en espacios complicados y finos en recintos o entre ventanas de edificios, y me di cuenta de que ajustar cuatro esquinas de un quad cuando están tan juntas podía ser muy delicado. ¡Así nació la zona Line / Curve!

Para líneas rectas, solo necesitas dos puntos y después ajustar _Zone thickness_ en el menú contextual. Es la forma más rápida de crear zonas sencillas.

Haz `Alt / Option`-clic en la línea para crear puntos adicionales. Estos puntos se suavizan automáticamente para crear una forma fluida, y puedes ajustar _Smooth level_ para eliminar cualquier irregularidad.

Haz `Alt / Option`-clic en un punto para eliminarlo.

O, si tienes experiencia con aplicaciones de gráficos vectoriales (Inkscape, Illustrator, etc.), puedes usar la opción _Manually adjust bezier curves_ para ajustar con precisión todos los puntos de control.

### Forma de zona Segmented

Esta zona subdividida te permite hacer correcciones extremadamente detalladas y resulta útil cuando haces mapping sobre formas complejas. Puedes añadir o eliminar subdivisiones con los botones + y - del menú contextual.

### Cómo editar una zona que está completamente cubierta por otra zona

Haz clic derecho en la zona superior y haz clic en el botón del candado para bloquearla. Ahora deberías poder editar y ajustar la zona que está debajo.

<br>

{% hint style="info" %}
Cuando añadas una Beam zone a tu salida, estará disponible para añadirla a un clip en el clip deck.
{% endhint %}
