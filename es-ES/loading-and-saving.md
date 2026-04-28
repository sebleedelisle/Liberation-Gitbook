---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Cargar y guardar

Liberation guarda constantemente su estado en el disco para que, si hay un corte de corriente o un problema del sistema, pueda arrancar justo donde se quedó. No deberías perder nunca tus zonas, líneas de tiempo ni otros contenidos.

Aun así, puedes exportar tu configuración para hacer copias de seguridad o transferirla a otro ordenador.

### Importación/exportación de proyecto

El archivo de proyecto almacena casi todo lo que hay en tu configuración actual, incluyendo:

* Todo lo detallado en [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export "mention") más abajo
* Clips, efectos y ajustes de grupo
* Todas tus líneas de tiempo (sin incluir medios de audio y vídeo)
* Configuración de Artnet
* Ajustes de envío/recepción MIDI
* Ajustes de tempo / sincronización

Actualmente no guarda ni carga:

* Ajustes de entrada de sonido y MIDI usados en el nodo MIDI notes y en Sound Input Oscillator (sí guarda los ajustes de envío/recepción MIDI, así como la entrada de sonido de timecode)
* Escalado de la interfaz
* Medios para imágenes guía de Canvas
* Medios de sonido y vídeo para líneas de tiempo
* Fuentes usadas en el nodo Text

{% hint style="danger" %}
Los archivos de sonido y vídeo de la línea de tiempo no se guardan con los archivos de proyecto, así que asegúrate de guardarlos por separado si quieres transferirlos a otro ordenador. Consulta [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Importación/exportación de ajustes láser

* Ajustes láser de cada láser
* Zonas de haz
* Áreas de destino de Canvas
* Zonas DMX
* Asignación de controladores láser (y alias de cualquier controlador que hayas renombrado)
* Ajustes y presets de calibración de escáner láser y color
* Ajustes y presets de 3D Visualiser

### Importación/exportación de Clip Deck

* Todos los clips y sus asignaciones de zona, ajustes y parámetros
* Todos los ajustes de grupo, modo flash, tiempos de fundido de entrada/salida, etc.

Actualmente no guarda ni carga:

* Todos los efectos y sus parámetros y ajustes

{% hint style="info" %}
**Cargar clips desde un archivo de proyecto sin cargar todo el proyecto**

Para importar solo los clips de un proyecto, selecciona _**Clips->Import Clip Deck**_ y, en lugar de seleccionar un archivo de Clip Deck (.cpdk), elige un archivo de proyecto.
{% endhint %}

### Append Clip Deck

Puedes añadir clips desde un archivo de Clip Deck exportado a tu proyecto actual usando _Append Clip Deck_. Los clips se añaden al final de tu Clip Deck actual, pero no se importan los efectos ni los ajustes de grupo incluidos en el archivo.

### Export Selected Clips

Los clips seleccionados actualmente se exportarán a un archivo. Los ajustes de grupo y los efectos no se guardarán; solo los clips. Ten en cuenta que los clips activos que se estén ejecutando no se exportan salvo que también estén seleccionados.

{% hint style="info" %}
Opción/Alt - Mayús - clic en los clips para seleccionarlos (o usa el lazo). Puedes identificar qué clips están seleccionados por el contorno blanco grueso que los rodea. Consulta [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Importación/exportación de efectos

Carga y guarda todos los efectos junto con sus ajustes de grupo y parámetros.

{% hint style="info" %}
**Cargar efectos desde un archivo de proyecto sin cargar todo el proyecto**

Para importar solo los efectos de un proyecto, selecciona _**Effects->Import Effects**_ y, en lugar de seleccionar un archivo de efectos (.efts), elige un archivo de proyecto.
{% endhint %}

### Exportación de línea de tiempo

Exporta un archivo de línea de tiempo con una o más líneas de tiempo. Ten en cuenta que el Clip Deck siempre se incluye con los archivos de línea de tiempo exportados (aunque puedes elegir qué clips vuelves a importar; consulta [#timeline-import](loading-and-saving.md#timeline-import "mention") más abajo).

Si tienes más de una línea de tiempo en tu archivo de proyecto, se abrirá un panel que te permitirá seleccionar qué líneas de tiempo quieres exportar.

{% hint style="danger" %}
Los archivos de sonido y vídeo de la línea de tiempo no se guardan con los archivos de línea de tiempo, así que asegúrate de guardarlos por separado si quieres transferir tu contenido a otro ordenador. Consulta [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Importación de línea de tiempo

Importa una o más líneas de tiempo desde un único archivo de línea de tiempo. Después de seleccionar tu archivo de línea de tiempo, se abrirá un panel con varias opciones de importación.

Si el archivo de línea de tiempo contiene más de una línea de tiempo, se mostrarán todas. Marca las que quieras incluir.

* Replace existing timelines\
  Eliminará todas tus líneas de tiempo actuales y las sustituirá por las importadas
* Import used clips only\
  Importará solo los clips utilizados y los organizará en grupos, uno por cada línea de tiempo. Si esta opción no está seleccionada, todo el Clip Deck del archivo de línea de tiempo se añadirá a tus clips existentes.
* Replace existing clip deck\
  Sustituye tu Clip Deck actual por los clips del archivo de línea de tiempo. Solo está disponible si _Replace existing timelines_ está seleccionado.

{% hint style="info" %}
**Cargar líneas de tiempo desde un archivo de proyecto sin cargar todo el proyecto**

Para importar solo las líneas de tiempo de un proyecto, selecciona _**Timeline->Import Timeline(s)**_ y, en lugar de seleccionar un archivo de línea de tiempo (.ltml), elige un archivo de proyecto.
{% endhint %}

### Importación/exportación de DMX / Artnet

Guarda y carga los nodos Artnet junto con sus direcciones IP. También incluye las zonas DMX y todos tus presets DMX.

### Nota importante sobre los archivos multimedia de la línea de tiempo

Los archivos de sonido y vídeo **no** se exportan actualmente con el archivo de línea de tiempo, así que, si necesitas mover contenido a otro ordenador, asegúrate de incluirlos.

{% hint style="info" %}
**Cómo busca una línea de tiempo los archivos multimedia**

Cuando se carga la línea de tiempo, buscará en la misma carpeta que el archivo de línea de tiempo (o de proyecto) y también dentro de esa carpeta y de cualquier subcarpeta. Por tanto, siempre que los archivos estén en la misma carpeta o en una subcarpeta (como _/videos_ o _/sound_), los encontrará al cargar.
{% endhint %}
