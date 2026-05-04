---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Guía de inicio rápido

## Introducción

Bienvenido a **Liberation**, la nueva generación de software para espectáculos láser.

Liberation es un software moderno, potente y complejo; está construido sobre principios de usabilidad y fiabilidad para darte la libertad de expresar tu creatividad. Es rápido, eficiente y fluido; sigue esta _Guía de inicio rápido_ para ponerte en marcha en muy poco tiempo.

### Gestión de láseres

Liberation es lo bastante flexible como para que puedas configurar láseres y visualizarlos sin tener ningún láser físico conectado. Después, cuando estés listo para empezar, puedes asignar cada salida a un controlador láser de forma fluida.

{% hint style="info" %}
Puedes configurar y visualizar tantos láseres como quieras dentro de Liberation; los niveles de licencia (Hobbyist, Pro, etc.) solo limitan el número de láseres que puedes _armar._ Esto significa que puedes diseñar espectáculos láser con 100 láseres incluso con una licencia gratuita. Solo necesitas actualizar la licencia cuando vayas a ejecutarlo realmente en láseres físicos.
{% endhint %}

La configuración predeterminada tiene 8 láseres distribuidos horizontalmente, pero puedes personalizarla como quieras. Probablemente sea mejor mantener este valor predeterminado mientras te familiarizas con el software y, más adelante, ajustarlo para que coincida con tu configuración de hardware. Consulta [Configurar tu proyecto](setting-up/setting-up-your-project.md "mention").

{% hint style="warning" %}
Importante: antes de armar cualquier láser, asegúrate de entender los riesgos implicados y revisa cuidadosamente el capítulo [Resumen del proceso de configuración de láseres](setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Vista general del software

### Parada de seguridad

Siempre que trabajes con láseres debes tener a mano un **botón físico de parada de emergencia** (consulta [Parada de emergencia / enclavamientos](hardware/emergency-stop-interlocks.md "mention")), pero si quieres desarmarlo todo sin tanta urgencia puedes usar el botón _**DISARM ALL**_ o la tecla `Escape` (o la tecla _**SESSION**_ en el APC40). También puedes reducir el brillo global usando el deslizador en pantalla o el fader principal del APC40.

### Elementos deslizantes

En Liberation encontrarás varios deslizadores y controles.

{% hint style="info" %}
Haz `Cmd / Ctrl`-clic en un deslizador para escribir un valor nuevo si necesitas más control del que te permite el deslizador.
{% endhint %}

### Atajos de teclado

Puedes encontrar una lista completa de atajos de teclado aquí: [Atajos de teclado](reference/keyboard-shortcuts.md "mention")

### Distribución de la pantalla

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
¿No tienes claro qué hace un botón concreto? Pasa el ratón por encima para ver una descripción.
{% endhint %}

#### Menú

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

En el menú encontrarás todas las opciones de importación/exportación de archivos y la apertura de paneles. También encontrarás aquí la opción para autorizar el ordenador con tu suscripción, en _Liberation -> Authorise/Deauthorise this computer_.

#### Barra de iconos

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Aquí encontrarás tareas habituales, como armar/desarmar todos los láseres, el brillo global, el patrón de prueba y el cambio entre las vistas 3D, Canvas y Output.

### Vistas

La zona grande situada en la parte superior izquierda de la pantalla puede mostrar una de las 3 vistas principales: **3D**, **CANVAS** y **OUTPUT.** Cambia entre ellas usando los botones de la barra de iconos (o usa la tecla `Tab` para alternar entre las vistas 3D y OUTPUT, y luego seguir pasando por cada salida láser una a una).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Vista 3D

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

La vista 3D te muestra cómo se verán tus láseres y puede configurarse para que coincida con tu propia instalación. Haz clic y arrastra para girar la cámara; usa la rueda del ratón para avanzar y retroceder. Encontrarás muchas otras opciones en el panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Consulta [3D Visualiser](setting-up/3d-visualiser.md "mention").

#### Vista Output

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

La vista Output se usa para configurar zonas y máscaras para cada láser. Fíjate en el número enorme de la esquina superior izquierda: así puedes ver fácilmente en qué láser estás.

Esta vista es una representación de toda la salida de este láser y de dónde se sitúa cada zona dentro de ella. De forma predeterminada solo hay una zona por láser, pero puedes añadir tantas zonas como sea razonablemente práctico, y las verás todas en esta vista.

{% hint style="info" %}
**¿Qué es una zona?**

Una zona es un espacio dentro de la salida de un láser al que puedes dirigir contenido láser. Puedes tener más de una zona por láser. El tipo de zona más sencillo es una zona _beam_, pero también existen zonas _canvas_ y zonas _DMX_. En esta guía nos centraremos sobre todo en las zonas beam, que normalmente se usan para crear efectos atmosféricos de haces en el aire.
{% endhint %}

Puedes seleccionar el láser que quieres editar usando cualquiera de estas opciones:

* los botones numerados de la barra superior
* pulsando la tecla numérica del láser que quieras (_teclas 1-9_)
* la tecla `Tab` para recorrerlos uno tras otro

Añade un nuevo láser a la configuración pulsando el botón _+_. También hay un botón _ADD LASER_ en el panel _Laser Overview_.

Elimina un láser de la configuración pulsando el botón rojo ⊖ en el panel _Laser Overview_.

Puedes acercar y alejar la vista con la rueda de desplazamiento del ratón, y hacer clic y arrastrar en cualquier zona donde no haya una zona definida para mover la vista.

Haz clic en una zona para seleccionarla y ajusta sus puntos de esquina con el ratón. Usa la tecla `Alt / Option` mientras arrastras una esquina para hacer que el ajuste no sea uniforme. Haz clic derecho en la zona para ver más opciones, incluido el cambio de tipo de zona.

A la izquierda hay una barra con una serie de botones de icono; pasa el ratón sobre cualquier botón para obtener una descripción de lo que hace. Estos botones te permiten añadir zonas beam, zonas canvas y máscaras. También hay opciones para definir un patrón de prueba solo para este láser, junto con ajustes de cuadrícula y ajuste magnético.

Para más detalles, consulta [Vista Output](output-view/ "mention").

#### Canvas

El sistema Canvas se usa principalmente para gráficos y mapeado arquitectónico. Puedes distribuir imágenes complejas entre varios láseres y corregir la perspectiva de cada sección. Consulta [Gráficos y el sistema Canvas](graphics-and-the-canvas-system/ "mention").

### Controlador MIDI APC40

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Aunque es posible controlar Liberation con ratón y teclado, es mucho mejor usar una interfaz de control MIDI APC40 (Mark 2 es la mejor opción, pero Mark 1 también funciona).

Consulta también: [Referencia de APC40](reference/apc40-reference.md "mention")

Liberation también es compatible con APC Mini y MIDI Fighter Twister. APC40 Mark 2 sigue siendo la mejor opción en la mayoría de los casos.

### Clips y efectos

{% hint style="info" %}
**¿Qué es un clip?**

Un clip es un contenedor para cualquier contenido láser dentro de Liberation. Los clips pueden contener haces o animaciones gráficas, y normalmente son ciclos en bucle. Pueden dirigirse a cualquier zona (o _Canvas target area_) y se lanzan usando los botones de clip dentro del clip deck.
{% endhint %}

#### Vista general del clip deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Esta cuadrícula se conoce como _clip deck_ y es donde se almacenan todos los clips láser. Está diseñada para mapearse directamente con la cuadrícula de botones 8 x 5 de tu APC40.

**Navegación por el clip deck.**

Puedes desplazar el clip deck a izquierda y derecha usando:

* Teclas de flecha izquierda y derecha. Añade `Cmd / Ctrl` para desplazarte una página completa cada vez.
* Trackpad: deslizar
* Ratón: si tu ratón tiene desplazamiento lateral, puedes usarlo mientras el cursor está sobre el clip deck
* Rueda de desplazamiento del APC40
* Botones _<- DEVICE ->_ del APC40

Para ayudarte a orientarte, hay un minivisualizador del clip deck en la parte superior. Consulta también [Clips y Clip deck](clips/ "mention").

#### Iniciar y detener clips

Pulsa un botón de clip (con el ratón o con el APC40) para iniciar un clip. Vuelve a pulsarlo para detenerlo. Cuando inicias un clip, todos los demás clips del mismo color se detendrán automáticamente salvo que mantengas pulsado _shift_.

Algunos clips estarán en _Flash mode_ (de forma predeterminada, los rojos); en ese caso, se detendrán en cuanto sueltes el botón de clip.

El botón _STOP_ detiene todos los clips que se estén ejecutando en ese momento.

#### Configurar zonas de salida para el clip

Debajo de los botones de clip verás los botones de zona, beam zones 1 a 8 de forma predeterminada (_BEAM 1_, _BEAM 2_, etc.). Los botones de zona se iluminan para indicar qué zonas están asignadas al clip seleccionado actualmente.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dos filas por debajo de los botones de zona verás los botones de inversión X/Y; actívalos para invertir el clip horizontal y verticalmente.

{% hint style="info" %}
Ten en cuenta que estas asignaciones de zona y los ajustes de inversión X/Y están conectados al propio clip; se conservan la próxima vez que ejecutes ese clip. No son un ajuste global.
{% endhint %}

Haz clic derecho en un clip para editar más ajustes del clip. Consulta también [Ajustes de Clip](clips/clip-settings.md "mention").

### Grupos

Verás que cada clip tiene un contorno de color, y ese color representa a qué _grupo_ pertenece. Los botones de clip del APC40 también se iluminan con este color.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grupo 1</td><td>Cian</td></tr><tr><td>Grupo 2</td><td>Naranja</td></tr><tr><td>Grupo 3</td><td>Rojo</td></tr><tr><td>Grupo 4</td><td>Índigo</td></tr><tr><td>Grupo 5</td><td>Verde</td></tr></tbody></table>

El sistema de grupos es muy flexible y te permite:

* Mantener en marcha clips de un grupo mientras activas y desactivas clips de otro
* Asignar rápidamente zonas e inversiones X/Y a todos los clips de un grupo
* Definir _Flash mode_ para un clip (el Grupo 3 está configurado en _Flash mode_ de forma predeterminada)

Los grupos también tienen ajustes de transición de entrada/salida que sus clips pueden heredar o sobrescribir.

Puedes asignar el grupo del clip usando los botones del menú de clic derecho, o con el APC40 pulsando el botón de grupo y, _mientras lo mantienes pulsado,_ pulsando los botones de clip.

Cambiar los ajustes de zona para todos los clips de un grupo

Con el APC40, pulsa el botón de grupo y, _mientras lo mantienes pulsado,_ usa los botones de zona y X/Y para activar o desactivar los ajustes de zona de todos los clips de ese grupo.

Consulta también [Grupos de Clip](clips/groups.md "mention").

### Efectos

El sistema de efectos de Liberation es una forma potente y versátil de modificar la salida del clip en tiempo real. Los botones de efectos predeterminados 1-8 están debajo de los botones de zona.

#### Aplicar un efecto

Pulsa un botón de efecto para activarlo o desactivarlo; mejor aún, usa los deslizadores 1-8 del APC40 para hacer entrar y salir los efectos progresivamente.

#### Parámetros de efecto

Usa los controladores rotatorios 1-8\* para ajustar el _parámetro_ de cada efecto. También puedes hacer clic derecho con el ratón para ajustar el nivel y el parámetro. El cambio de parámetro hace cosas distintas según cómo esté configurado el efecto. Consulta la lista siguiente para ver los efectos predeterminados.

{% hint style="info" %}
Los números pequeños que ves en los botones de efecto hacen referencia al _level_ y al _parameter_ del efecto. El _level_ se controla con el fader del APC40, o puedes hacer clic y arrastrar sobre el botón. El parámetro se ajusta con los rotatorios del APC40, o puedes hacer clic derecho para ajustarlo con el ratón.
{% endhint %}

_\*Los controladores rotatorios 1-8 están en la parte superior del APC40 Mk2 y en la parte superior derecha del Mk1. Consulta también:_ [Referencia de APC40](reference/apc40-reference.md "mention")

#### Efectos predeterminados

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Aplica un movimiento caótico a la salida del clip. El parámetro ajusta la cantidad/velocidad del caos.
2. **Sine wave** :\
   Deforma todo el contenido a lo largo de una onda sinusoidal en movimiento. El parámetro ajusta la longitud de onda.
3. **Rotation** :\
   Hace girar todo el contenido. El parámetro ajusta la velocidad de giro.
4. **Horizontal flip** :\
   Comprime y estira todo horizontalmente. El parámetro ajusta la velocidad.
5. **Scale** :\
   Escala repetidamente todo desde tamaño completo hasta cero. El parámetro ajusta la velocidad.
6. **Hue** :\
Cambia el tono de todo, pero no cambia la saturación (es decir, cualquier elemento blanco sigue siendo blanco). El parámetro ajusta el tono.
7. **Saturation and hue** :\
Cambia el tono de todo y también satura completamente el color (es decir, cualquier elemento blanco cambia a ese color). El parámetro ajusta el tono.
8. **Flash** :\
   Hace parpadear repetidamente el brillo de todo desde el máximo hasta cero. El parámetro ajusta la velocidad del parpadeo.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Hay otros 16 efectos de color en la fila inferior para aplicar valores predefinidos de tono y saturación.

Ten en cuenta que estos son los efectos predeterminados, pero pueden editarse para hacer casi cualquier cosa que quieras.

#### ¿Qué es el _"currently selected clip"_?

Cuando inicias un clip, se ilumina para mostrar que está activo. También tiene un contorno blanco alrededor, que indica que este es el clip actualmente _seleccionado_. Siempre que actives botones de zona o ajustes la configuración del clip, esos cambios se aplican al _clip seleccionado actualmente._

{% hint style="info" %}
Para seleccionar un clip sin dispararlo, pulsa la tecla `Alt / Option` antes de pulsar el botón de clip. Es una buena forma de ajustar sus zonas y otros parámetros sin ejecutarlo.
{% endhint %}

### Panel Clip Settings

Usa el panel _Clip Settings_ para editar la escala, la posición X/Y y acceder al potente sistema de retardo por zonas.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

Busca el panel _Global Settings_ para ajustar opciones globales de salida que afectan a toda la salida en todas las zonas.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Activa AUTO RESET para restablecer automáticamente todos los _Global settings_ cuando no haya clips reproduciéndose.

### Temporización

Casi todos los espectáculos láser tienen algún tipo de banda sonora musical, así que el sistema de temporización de Liberation se basa en un tempo en pulsos por minuto. En el _Tempo Panel_ puedes ver una representación del tiempo; cada cuadrado representa un pulso y verás cómo parpadean al ritmo.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Hay varias opciones de sincronización, incluyendo MIDI clock y Ableton Link. Si conoces el tempo de la música, puedes ajustarlo manualmente con el deslizador en pantalla o con el mando Tempo del APC40, pero también puedes mantenerte al ritmo de la música usando el sistema _Tap Tempo_.

#### Tap Tempo

_Tap Tempo_ es un término muy usado en aplicaciones musicales y te permite marcar el ritmo con pulsaciones para definir el tempo mientras suena la música. Puedes usar el botón en pantalla, aunque se recomienda usar la tecla _T_ o el botón _Tap Tempo_ del APC40 (o incluso un pedal si lo prefieres).

Pulsa la tecla _R_ o el botón _Metronome_ (APC40) para reiniciar el tempo al principio del compás.

Pulsa la tecla _Y_ o gira el mando _Tempo_ (APC40) para redondear el tempo a un número entero. Esto puede ser útil para música electrónica, que suele tener un número entero de pulsos por minuto.

### Organizar tu clip deck

Para mover un clip en tu clip deck, haz clic y arrástralo a una nueva posición. Mientras arrastras, puedes usar las teclas de cursor (o la rueda/botones de desplazamiento de tu APC40) para desplazarte a izquierda y derecha.

Pulsa la tecla `Alt / Option` mientras arrastras para hacer una copia.

Haz `Alt / Option`-clic en un clip para seleccionarlo sin iniciarlo.

Haz `Alt / Option + Shift`-clic en un clip para multiseleccionar, o haz clic y arrastra fuera de un clip para seleccionar con "lazo".

Hacer clic y arrastrar arrastrará TODOS los clips seleccionados.

Para eliminar uno o varios clips, arrástralos fuera del clip deck (aparecerá un icono de papelera) o usa el botón DELETE del menú de clic derecho del clip.

### Panel Laser Overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

El panel _Laser overview panel_ te ofrece una vista rápida del estado de los láseres que se están ejecutando actualmente. El cuadrado verde de la derecha indica que el controlador láser está funcionando correctamente. Si se vuelve naranja, hay pérdidas ocasionales; si se vuelve rojo, se ha desconectado. Si está gris, no está conectado a ningún controlador.

El gráfico central es un historial de duraciones de fotograma, y el número de la derecha es la frecuencia de fotogramas actual. Cuanto más complejo sea el contenido, más lenta será la frecuencia de fotogramas (es decir, más parpadeo). Cualquier valor por debajo de unos 25 fps empezará a verse algo parpadeante.

### Conectar láseres: panel Controller Assignment

Haz clic en el botón _Assign Laser Controllers_ para abrir el panel _Controller Assignment_. También puedes acceder a este panel desde _View -> Controller Assignment_ en la barra de menús.

Aquí puedes elegir qué salidas láser van a qué controladores láser. Arrastra y suelta controladores desde la lista de la derecha a las ranuras de la izquierda. Puedes renombrar tus controladores para que coincidan con el láser al que están asociados (usa el botón con el icono de lápiz).

Lee el capítulo [Asignación de controladores](setting-up/controller-assignment.md "mention") para obtener más detalles.

{% hint style="danger" %}
Antes de armar cualquier láser, asegúrate de revisar el capítulo [Resumen del proceso de configuración de láseres](setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panel Laser Output

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Este panel muestra los ajustes del _láser seleccionado actualmente_ (representado por el número de la parte superior). Cambia el láser seleccionado usando la tecla _tab_, pulsando una tecla numérica, haciendo clic en un número de láser en el panel _Laser Overview_ o en la _output view._

* **Number button** arma y desarma el láser; si está rojo, el láser está armado.
* **Brightness** ajusta el brillo del láser de forma independiente al resto de láseres (y se combina con el ajuste de _global brightness_; es decir, si ambos están al 50 %, tu láser estará al 25 %).
* **Test Pattern** activa un patrón de prueba solo para este láser (anula el ajuste global de patrón de prueba).
* **Orientation** corrige láseres montados de lado o boca abajo.
* **Flip Horizontal and Flip Vertical** invierte la salida del láser. Es útil para corregir la salida en láseres con cableado inconsistente.
* **Copy Laser Settings** abre un panel que te permite copiar varios ajustes de este láser a otros.

### Ajustes de escáner

Los láseres de exhibición funcionan moviendo un único haz láser a una velocidad extremadamente alta y encendiéndolo y apagándolo para dibujar formas en el aire. Lo que ves como líneas, formas e imágenes es en realidad el haz trazando recorridos más rápido de lo que tus ojos pueden seguir.

Un flujo de puntos es el conjunto de datos que indica al láser adónde moverse a continuación y cuándo debe encenderse o apagarse el haz. En Liberation, los clips se convierten en este flujo de puntos en tiempo real mientras se envían a los láseres.

Liberation te da un control detallado sobre cómo se genera este flujo de puntos, permitiéndote equilibrar suavidad, brillo y rendimiento para cada láser.

{% hint style="info" %}
Si estás acostumbrado a software láser más antiguo que depende de flujos de puntos precalculados, este enfoque puede resultarte diferente al principio. Sin embargo, la generación de puntos en tiempo real permite optimizar el mismo contenido de forma distinta para cada láser. Esto facilita trabajar con varios láseres que tienen velocidades o calidades de escáner diferentes, sin duplicar ni reconstruir contenido. También mantiene los archivos de clip muy pequeños, por eso todo el clip deck predeterminado de Liberation ocupa solo unos pocos megabytes en lugar de gigabytes.
{% endhint %}

Los ajustes básicos de escáner son:

* **Speed** es la velocidad del escáner, es decir, lo rápido que se mueve el láser para dibujar formas. Equivale a ajustar la tasa de puntos en software láser tradicional, pero en Liberation puedes cambiar la velocidad a la que se mueve el láser _independientemente de la tasa de puntos._ No deberías necesitar ajustarlo.
* **Scanner sync** (a veces conocido como _blank shift_, antes Colour Shift) Los escáneres mueven el láser muy rápido, pero normalmente el cambio de brillo y color no está sincronizado con el movimiento. Esto aparece como pequeñas "colas" de luz parpadeantes en el borde de haces y líneas. Usa este ajuste para sincronizar el movimiento y el color entre sí. Consulta [Panel de ajustes de Laser output](setting-up/laser-settings.md "mention")

Los demás ajustes avanzados de escáner se tratan en el capítulo [Avanzado](advanced/ "mention").

### Zonificación

Para una guía completa sobre cómo configurar y zonificar láseres, consulta: [Resumen del proceso de configuración de láseres](setting-up/setting-up-lasers.md "mention")
