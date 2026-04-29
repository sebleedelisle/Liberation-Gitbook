---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Introducción al Clip Editor

El Clip Editor es una forma versátil de crear contenido láser y está en el centro de Liberation. Es fácil crear elementos sencillos, pero también es lo bastante flexible como para hacer efectos increíblemente sofisticados y complejos.

{% hint style="info" %}
¡El editor basado en nodos fue la primera parte de Liberation que se creó! Nació de una conversación con Rob Stanley en un encuentro de láser en Reino Unido en 2018 sobre cómo sería un diseñador de contenido láser "orientado a objetos".

Aunque parece sencillo, es un sistema bastante complejo de construir, pero a principios de 2019 ya tenía una demo funcional que demostraba el concepto, ¡y ahí empezó todo este viaje!
{% endhint %}

Es un editor visual basado en nodos (o [arquitectura de grafo de nodos](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) que te resultará familiar si has usado productos como TouchDesigner, MaxMSP o VVVV. Aun así, el Clip Editor es un poco diferente y algo más sencillo, ya que se ha diseñado específicamente para gráficos vectoriales.

Puedes abrir el Clip Editor haciendo clic derecho en el botón de Clip y seleccionando _EDIT CLIP_. También puedes hacer clic derecho en un botón de Clip vacío y seleccionar _CREATE AND EDIT CLIP_.

### Vista general

Lo que verás en el Clip Editor:

* Los botones de nodos **Creator** y **Operator** en la parte superior
* Los botones de nodos **Oscillator** en la parte izquierda
* Una previsualización del contenido en un panel a la derecha; si haces clic en un nodo, verás una segunda previsualización que muestra el contenido en ese nodo concreto.
* Todos los nodos y conexiones del Clip que estás editando (si es un Clip nuevo, estará vacío)
* El panel Clip Editor con varias opciones

Mientras editas, también verás cómo queda el Clip en el 3D Visualiser, en segundo plano.

{% hint style="info" %}
Si no ves ninguna salida en el 3D Visualiser, puede que tengas que usar los botones de zona para activar las zonas que quieres. También tendrás que asegurarte de que _Preview to lasers_ esté activado; consulta [Introducción al Clip Editor](clip-editor-intro.md#clip-editor-panel "mention") más abajo.
{% endhint %}

### Crear un Clip

Normalmente empezarás con uno o varios [nodos Creator](creator-nodes.md) y conectarás [Nodos de operador](operator-nodes/) de izquierda a derecha para procesar el contenido. Al acercar Creator y/o Operator entre sí, verás que se conectan automáticamente. También puedes arrastrarlos para separarlos y desconectarlos de nuevo.

### Añadir nodos a tu Clip

Haz clic y arrastra desde uno de los botones de nodo de la parte superior o izquierda hasta un espacio vacío dentro del Clip Editor.

### Ajustar la configuración de un nodo

Haz clic en el botón con el icono de engranaje (en la parte superior derecha del nodo) para abrir el panel de propiedades de ese nodo.

### Activar y desactivar un nodo

Haz clic en el botón con el icono de encendido (en la parte superior izquierda del nodo) para activar y desactivar el nodo. El nodo se atenuará para indicar que no está activo en ese momento. Ten en cuenta que el contenido sigue pasando por un Operator aunque esté desactivado, pero el nodo no afecta al contenido.

### Conectar nodos entre sí

El contenido se crea con un nodo Creator y pasa por los nodos de izquierda a derecha; cada Operator afecta al contenido de alguna forma y lo envía al siguiente Operator. Lo que queda al final de la ruta es el contenido del Clip. Los Creator y Operator se conectan automáticamente entre sí cuando los acercas. Para separarlos, vuelve a arrastrarlos para alejarlos.

{% hint style="info" %}
Puedes conectar más de un nodo a la entrada del siguiente nodo. Esto resulta útil para combinar varias piezas de contenido.
{% endhint %}

### Propiedades y conectores de los nodos

Cada nodo tiene una serie de conectores en la parte inferior, y cada uno representa una propiedad dentro del nodo, como brillo, posición, escala, rotación, etc.

Los [nodos Oscillator](oscillators/) se pueden conectar a estos conectores desde abajo y se usan para animar estos ajustes. Los nodos Oscillator tienen una salida en la parte superior: haz clic y arrastra para sacar la conexión y soltarla en uno de los conectores de propiedades de los otros nodos.

### Nodos Oscillator

Los nodos Oscillator se usan para cambiar propiedades con el tiempo. Normalmente representan formas de onda, como una onda de diente de sierra o una onda sinusoidal, aunque algunos nodos Oscillator utilizan entradas externas (como el nivel de entrada del micrófono) como fuente.

{% hint style="info" %}
Si alguna vez has usado un sintetizador analógico, te resultará familiar el concepto de osciladores, que suelen utilizarse para crear formas de onda o ajustar el sonido con el tiempo. Los osciladores en Liberation cumplen una función similar.

**Dato curioso:** el nombre _Liberation_ se inspiró en el Moog Liberation, un sintetizador "keytar" lanzado en 1980 y hecho famoso por Herbie Hancock, Jean-Michel Jarre e incluso James Brown.
{% endhint %}

Los osciladores siempre tienen ajustes de _range_ que controlan el valor mínimo y máximo de la propiedad que se va a ajustar. Además, los _Wave Oscillators_ siempre tienen un ajuste de _duration_ que determina la velocidad con la que el oscilador cambia el valor. Consulta [Osciladores de onda](oscillators/wave-oscillators.md "mention") para obtener más información.

### Panel Clip Editor

* Timer - en la parte superior del panel verás el tiempo actual del Clip mientras avanza
* _RETRIGGER_ - reinicia el Clip desde el principio; es especialmente útil si tu Clip no se reproduce en bucle
* _Preview to lasers_ - cuando está marcado, verás cómo se actualiza el 3D Visualiser mientras editas este Clip. Si lo desactivas, verás los Clips que se estén ejecutando fuera del editor. Es un ajuste global, no por Clip.
* _UNDO/REDO_ - para el propio Clip Editor. También asignado a `Cmd / Ctrl + Z` y `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - guarda tus cambios, pero te avisa antes de sobrescribir
* _SAVE AS A COPY_ - guarda tu Clip en el siguiente espacio disponible del Clip Deck. Esta pasa a ser la nueva posición de tu Clip y todos los guardados posteriores se harán en esta nueva ubicación.
* _EXIT EDITOR_ - cierra el Clip Editor. Si tienes cambios sin guardar, aparecerá un panel de confirmación.
