# ✅ Guía de inicio rápido

## Introducción

Te damos la bienvenida a **Liberation**, la nueva generación de software para shows láser.

Liberation es un software moderno, potente y complejo; está construido sobre principios de usabilidad y fiabilidad para darte la libertad de expresar tu creatividad. Es rápido, eficiente y fluido; sigue esta _Guía de inicio rápido_ para empezar a trabajar en muy poco tiempo.

### Gestión de láseres

Liberation es lo bastante flexible como para que puedas configurar láseres y visualizarlos sin tener ningún láser físico conectado. Después, cuando estés listo para empezar, puedes asignar cada salida a un controlador láser de forma sencilla.

{% hint style="info" %}
Puedes configurar y visualizar tantos láseres como quieras dentro de Liberation; los niveles de licencia (Hobbyist, Pro, etc.) solo limitan el número de láseres que puedes _armar_. Esto significa que puedes diseñar shows láser con 100 láseres incluso con una licencia gratuita. Solo necesitas actualizar la licencia cuando vayas a ejecutarlo realmente en láseres físicos.
{% endhint %}

La configuración predeterminada tiene 8 láseres distribuidos horizontalmente, pero puedes personalizarla como quieras. Probablemente sea mejor mantener esta configuración mientras te familiarizas con el software, y más adelante ajustarla para que coincida con tu hardware. Consulta [Configurar tu proyecto](../setting-up/setting-up-your-project.md "mention").&#x20;

{% hint style="warning" %}
Importante: antes de armar cualquier láser, asegúrate de comprender los riesgos implicados y revisa detenidamente el capítulo [Resumen del proceso de configuración de láseres](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Vista general del software

### Apagado de seguridad

Siempre que estés usando láseres debes tener a mano un **botón físico de parada de emergencia**; consulta [Parada de emergencia / enclavamientos](../hardware/emergency-stop-interlocks.md "mention"). Si quieres desarmarlo todo sin tanta urgencia, puedes usar el botón _**DISARM ALL**_, la tecla `Escape` o la tecla _**SESSION**_ del APC40. También puedes reducir el brillo global con el deslizador en pantalla o con el fader principal del APC40.

### Elementos deslizantes

En Liberation encontrarás varios deslizadores y controles.

{% hint style="info" %}
Haz clic en un deslizador con `Cmd / Ctrl` para escribir un valor nuevo si necesitas más control del que permite el propio deslizador.
{% endhint %}

### Atajos de teclado

Puedes encontrar una lista completa de atajos de teclado aquí: [Atajos de teclado](../reference/keyboard-shortcuts.md "mention")

### Distribución de la pantalla

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
¿No sabes qué hace un botón concreto? Pasa el ratón por encima para ver una descripción.
{% endhint %}

#### Menú

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

En el menú encontrarás todas las opciones de importación y exportación de archivos, además de las opciones para abrir paneles. También encontrarás aquí la opción para autorizar el ordenador con tu suscripción, en _Liberation -> Authorise/Deauthorise this computer_.

#### Barra de iconos

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Aquí encontrarás tareas habituales, como armar o desarmar todos los láseres, el brillo global, el patrón de prueba y el cambio entre las vistas 3D, Canvas y Output.

### Vistas

La zona grande de la parte superior izquierda de la pantalla puede mostrar una de las 3 vistas principales: **3D**, **CANVAS** y **OUTPUT**. Cambia entre ellas con los botones de la barra de iconos, o usa la tecla `Tab` para alternar entre las vistas 3D y OUTPUT y seguir pasando por cada salida láser por turnos.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Vista 3D

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

La vista 3D muestra cómo se verán tus láseres y puede configurarse para coincidir con tu propia instalación. Haz clic y arrastra para rotar la cámara; usa la rueda del ratón para avanzar y retroceder. Encontrarás muchas otras opciones en el panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Consulta [3D Visualiser](../setting-up/3d-visualiser.md "mention").

#### Vista Output

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

La vista Output se usa para configurar zonas y máscaras de cada láser. Observa el número grande en la esquina superior izquierda: te permite ver fácilmente en qué láser estás.

Esta vista representa toda la salida de ese láser y muestra dónde se sitúa cada zona dentro de ella. De forma predeterminada solo hay una zona por láser, pero puedes añadir tantas zonas como sea razonablemente práctico, y las verás todas en esta vista.

{% hint style="info" %}
**¿Qué es una zona?**

Una zona es un espacio dentro de la salida de un láser al que puedes dirigir contenido láser. Puedes tener más de una zona por láser. El tipo de zona más sencillo es una zona de _beam_, pero también existen zonas _canvas_ y zonas _DMX_. En esta guía nos centraremos principalmente en las zonas de beam, que suelen utilizarse para crear efectos atmosféricos de haces en el aire.
{% endhint %}

Puedes seleccionar el láser que quieres editar usando cualquiera de estas opciones:

* los botones numerados de la barra superior
* pulsando la tecla numérica del láser que quieras, teclas _1-9_
* la tecla `Tab` para avanzar de uno al siguiente

Añade un nuevo láser a la configuración pulsando el botón _+_. También hay un botón _ADD LASER_ en el panel _Laser Overview_.

Elimina un láser de la configuración pulsando el botón rojo ⊖ en el panel _Laser Overview_.

Puedes acercar y alejar la vista con la rueda del ratón, y hacer clic y arrastrar en cualquier punto donde no haya una zona para mover la vista.

Haz clic en una zona para seleccionarla y después ajusta sus puntos de esquina con el ratón. Usa la tecla `Alt / Option` mientras arrastras una esquina para hacer que el ajuste no sea uniforme. Haz clic derecho en la zona para ver más opciones, incluida la posibilidad de cambiar el tipo de zona.

A la izquierda hay una barra con una serie de botones de icono; pasa el ratón por encima de cualquier botón para ver una descripción de lo que hace. Los botones de esta barra te permiten añadir zonas beam, zonas canvas y máscaras. También hay opciones para activar un patrón de prueba solo para este láser, además de ajustes de cuadrícula y ajuste por imán.

Para más detalles, consulta [Vista Output](../output-view/ "mention").

#### Canvas

El sistema Canvas se usa principalmente para gráficos y mapping arquitectónico. Puedes distribuir imágenes complejas entre varios láseres y corregir la perspectiva de cada sección. Consulta [Gráficos y el sistema Canvas](../graphics-and-the-canvas-system/ "mention").

### Controlador MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Aunque es posible controlar Liberation con el ratón y el teclado, es mucho mejor usar una superficie de control MIDI APC40. Mark 2 es la mejor opción, aunque Mark 1 también funciona.

Consulta también: [Referencia de APC40](../reference/apc40-reference.md "mention")

También hemos implementado ya compatibilidad con APC Mini Mark 2 y MIDI Fighter Twister, y hay más controladores en desarrollo. Aun así, APC40 Mark 2 es la mejor opción en la mayoría de los casos.&#x20;

### Clips y efectos

{% hint style="info" %}
**¿Qué es un clip?**

Un clip es un contenedor para cualquier contenido láser dentro de Liberation. Los clips pueden contener beams o animaciones gráficas y normalmente funcionan como un ciclo en bucle. Pueden dirigirse a cualquier zona, o _Canvas target area_, y se disparan usando los botones de clip dentro del Clip Deck.
{% endhint %}

#### Vista general del Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Esta cuadrícula se conoce como _Clip Deck_ y es donde se almacenan todos los clips láser. Está diseñada para corresponderse directamente con la cuadrícula de botones 8 x 5 de tu APC40.

**Navegación por el Clip Deck.**

Puedes desplazar el Clip Deck a izquierda y derecha usando:

* Teclas de flecha izquierda y derecha. Añade `Cmd / Ctrl` para desplazarte una página completa cada vez.
* Trackpad: deslizar
* Ratón: si tu ratón tiene desplazamiento lateral, puedes usarlo mientras el cursor está sobre el Clip Deck
* Rueda de desplazamiento del APC40
* Botones _<- DEVICE ->_ del APC40

Para ayudarte a orientarte, hay un mini visualizador del Clip Deck en la parte superior. Consulta también [Clips y Clip deck](../clips/ "mention").

#### Iniciar y detener clips

Pulsa un botón de clip, ya sea con el ratón o con el APC40, para iniciar un clip. Púlsalo de nuevo para detenerlo. Cuando inicias un clip, todos los demás clips del mismo color se detienen automáticamente salvo que mantengas pulsado _shift_.

Algunos clips estarán en _Flash mode_ —de forma predeterminada, los rojos—, en cuyo caso se detendrán en cuanto sueltes el botón de clip.

El botón _STOP_ detiene todos los clips que se estén ejecutando en ese momento.

#### Configurar zonas de salida para el clip

Debajo de los botones de clip verás los botones de zona, zonas beam 1 a 8 de forma predeterminada (_BEAM 1_, _BEAM 2_, etc.). Los botones de zona se iluminan para indicar qué zonas están asignadas al clip seleccionado actualmente.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dos filas por debajo de los botones de zona verás los botones de inversión X/Y; actívalos o desactívalos para voltear el clip horizontal y verticalmente.

{% hint style="info" %}
Ten en cuenta que estas asignaciones de zona y los ajustes de inversión X/Y están vinculados al propio clip; se conservarán la próxima vez que ejecutes ese clip. No son un ajuste global.
{% endhint %}

Haz clic derecho en un clip para editar más ajustes del clip. Consulta también [Ajustes de Clip](../clips/clip-settings.md "mention").

### Grupos

Verás que cada clip tiene un contorno de color, y ese color representa a qué _grupo_ pertenece. Los botones de clip del APC40 también se iluminan con ese color.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cian</td></tr><tr><td>Group 2</td><td>Naranja</td></tr><tr><td>Group 3</td><td>Rojo</td></tr><tr><td>Group 4</td><td>Índigo</td></tr><tr><td>Group 5</td><td>Verde</td></tr></tbody></table>

El sistema de grupos es muy flexible y te permite:

* Mantener los clips de un grupo en marcha mientras activas o desactivas grupos en otro
* Asignar rápidamente zonas e inversiones X/Y a todos los clips de un grupo
* Activar _Flash mode_ para un clip; Group 3 está configurado en _Flash mode_ de forma predeterminada

Los grupos también tienen ajustes de transición de entrada y salida que pueden heredar sus clips, o sobrescribirse.

Puedes asignar el grupo de un clip usando los botones del menú de clic derecho o, con el APC40, pulsando el botón de grupo y, _mientras lo mantienes pulsado_, pulsando los botones de clip.

Cambiar los ajustes de zona de todos los clips de un grupo

Con el APC40, pulsa el botón de grupo y, _mientras lo mantienes pulsado_, usa los botones de zona y X/Y para activar o desactivar los ajustes de zona de todos los clips de ese grupo.

Consulta también [Grupos de Clip](../clips/groups.md "mention").

### Efectos

El sistema de efectos de Liberation es una forma potente y versátil de modificar la salida del clip en tiempo real. Los botones de efectos predeterminados 1-8 están debajo de los botones de zona.

#### Aplicar un efecto

Pulsa un botón de efecto para activar o desactivar el efecto o, mejor aún, usa los deslizadores 1-8 del APC40 para fundir los efectos de entrada y salida.

#### Parámetros de efecto

Usa los controles giratorios 1-8\* para ajustar el _parámetro_ de cada efecto. También puedes hacer clic derecho con el ratón para ajustar el nivel y el parámetro. El cambio de parámetro hace cosas distintas según cómo esté configurado el efecto. Consulta la lista siguiente para ver los efectos predeterminados.

{% hint style="info" %}
Los números pequeños que ves en los botones de efectos hacen referencia al _level_ y al _parameter_ del efecto. El _level_ se controla con el fader del APC40 o haciendo clic y arrastrando sobre el botón. El parámetro se ajusta con los controles giratorios del APC40, o puedes hacer clic derecho para ajustarlo con el ratón.
{% endhint %}

_\*Los controles giratorios 1-8 están en la parte superior de un APC40 Mk2 y en la parte superior derecha en el Mk1. Consulta también:_ [Referencia de APC40](../reference/apc40-reference.md "mention")

#### Efectos predeterminados

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**:\
   Aplica un movimiento caótico a la salida del clip. El parámetro ajusta la cantidad o velocidad del caos.
2. **Sine wave**:\
   Deforma todo el contenido sobre una onda sinusoidal en movimiento. El parámetro ajusta la longitud de onda.
3. **Rotation**:\
   Hace girar todo el contenido. El parámetro ajusta la velocidad de giro.
4. **Horizontal flip**:\
   Comprime y estira todo horizontalmente. El parámetro ajusta la velocidad.
5. **Scale**:\
   Escala repetidamente todo el contenido desde tamaño completo hasta cero. El parámetro ajusta la velocidad.
6. **Hue**:\
   Cambia el tono de todo el contenido, pero no cambia la saturación; es decir, todo lo que sea blanco sigue siendo blanco. El parámetro ajusta el tono.
7. **Saturation and hue**:\
   Cambia el tono de todo el contenido y además satura completamente el color; es decir, todo lo que sea blanco cambia al color. El parámetro ajusta el tono.
8. **Flash**:\
   Hace parpadear repetidamente el brillo de todo el contenido desde máximo hasta cero. El parámetro ajusta la velocidad del parpadeo.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Hay otros 16 efectos de color en la fila inferior para aplicar valores predefinidos de tono y saturación.

Ten en cuenta que estos son los efectos predeterminados, pero se pueden editar para hacer prácticamente lo que quieras.

#### ¿Qué es el _“clip seleccionado actualmente”_?

Cuando inicias un clip, se ilumina para indicar que está activo. También tiene un contorno blanco alrededor, que indica que este es el clip _seleccionado_ actualmente. Cada vez que activas o desactivas botones de zona o ajustas la configuración del clip, esos cambios se aplican al _clip seleccionado actualmente_.

{% hint style="info" %}
Para seleccionar un clip sin dispararlo, pulsa la tecla `Alt / Option` antes de pulsar el botón de clip. Es una buena forma de ajustar sus zonas y otros ajustes sin ejecutarlo.
{% endhint %}

### Panel Clip Settings

Usa el panel _Clip Settings_ para editar la escala, la posición X/Y y acceder al potente sistema de retardo de zonas.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

Busca el panel _Global Settings_ para ajustar opciones globales de salida que afectan a toda la salida de todas las zonas.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Activa AUTO RESET para restablecer automáticamente todos los _Global settings_ cuando no haya clips reproduciéndose.&#x20;

### Sincronización

Casi todas las proyecciones láser tienen algún tipo de banda sonora, así que el sistema de sincronización de Liberation se basa en un tempo en pulsaciones por minuto. En el _Tempo Panel_ puedes ver una representación del tiempo; cada cuadrado representa un pulso y puedes ver cómo parpadean a tiempo.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Hay varias opciones de sincronización, incluidas MIDI clock y Ableton Link. Si conoces el tempo de la música, puedes ajustarlo manualmente con el deslizador en pantalla o con el mando Tempo del APC40, pero también puedes mantenerte a tiempo con la música usando el sistema _Tap Tempo_\_ .\_

#### Tap Tempo

_Tap Tempo_ es un término habitual en aplicaciones musicales y te permite marcar el tempo siguiendo el pulso mientras suena la música. Puedes usar el botón en pantalla, aunque se recomienda usar la tecla _T_ o el botón _Tap Tempo_ del APC40, o incluso un pedal si lo prefieres.

Pulsa la tecla _R_ o el botón _Metronome_ del APC40 para reiniciar el tempo al principio del compás.

Pulsa la tecla _Y_ o gira el mando _Tempo_ del APC40 para redondear el tempo a un número entero. Esto puede ser útil para música electrónica, que suele tener un número entero de pulsaciones por minuto.

### Organizar tu Clip Deck

Para mover un clip en tu Clip Deck, haz clic y arrástralo a una nueva posición. Mientras arrastras, puedes usar las teclas de cursor, o la rueda/botones de desplazamiento de tu APC40, para desplazarte a izquierda y derecha.

Pulsa la tecla `Alt / Option` mientras arrastras para hacer una copia.

Haz clic en un clip con `Alt / Option` para seleccionarlo sin iniciarlo.

Haz clic en un clip con `Alt / Option + Shift` para seleccionar varios, o haz clic y arrastra fuera de un clip para seleccionar con “lazo”.&#x20;

Al hacer clic y arrastrar, se arrastrarán TODOS los clips seleccionados.

Para eliminar uno o varios clips, arrástralos fuera del Clip Deck —aparecerá un icono de papelera— o usa el botón DELETE del menú de clic derecho del clip.

### Panel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

El panel _Laser Overview_ te ofrece una vista rápida del estado de los láseres que se están ejecutando actualmente. El cuadrado verde de la derecha indica que el controlador láser está funcionando correctamente. Si pasa a naranja, hay pérdidas ocasionales; si pasa a rojo, se ha desconectado. Si está gris, no está conectado a ningún controlador.&#x20;

El gráfico central muestra un historial de la duración de los frames, y el número de la derecha es la frecuencia de frames actual. Cuanto más complejo sea el contenido, menor será la frecuencia de frames; es decir, más parpadeante se verá. Todo lo que esté por debajo de unos 25 fps empezará a verse algo parpadeante.&#x20;

### Conexión a láseres: panel Controller Assignment

Haz clic en el botón _Assign Laser Controllers_ para abrir el panel _Controller Assignment_. También puedes acceder a este panel desde _View -> Controller Assignment_ en la barra de menús.

Aquí puedes elegir qué salidas láser van a qué controladores láser. Arrastra y suelta controladores desde la lista de la derecha hasta las ranuras de la izquierda. Puedes cambiar el nombre de tus controladores para que coincida con el láser al que están asociados; usa el botón con el icono de lápiz.

Lee el capítulo [Asignación de controladores](../setting-up/controller-assignment.md "mention") para más detalles.

{% hint style="danger" %}
Antes de armar cualquier láser, asegúrate de revisar el capítulo [Resumen del proceso de configuración de láseres](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panel Laser Output

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Este panel muestra los ajustes del _láser seleccionado actualmente_, representado por el número de la parte superior. Cambia el láser seleccionado actualmente usando la tecla _tab_, pulsando una tecla numérica, haciendo clic en un número de láser en el panel _Laser Overview_ o en la _vista Output_.

* **Number button** arma y desarma el láser; si está rojo, el láser está armado.
* **Brightness** ajusta el brillo del láser independientemente de los demás láseres. Se combina con el ajuste de _global brightness_; es decir, si ambos están al 50 %, tu láser estará al 25 %.
* **Test Pattern** activa un patrón de prueba solo para este láser; anula el ajuste de patrón de prueba global.
* **Orientation** corrige láseres montados de lado o boca abajo.
* **Flip Horizontal and Flip Vertical** invierte la salida del láser. Resulta útil para corregir la salida en láseres con cableado no uniforme.
* **Copy Laser Settings** abre un panel que te permite copiar varios ajustes de este láser a otros.

### Ajustes de scanner

Los láseres de display funcionan moviendo un único haz láser extremadamente rápido y encendiéndolo y apagándolo para dibujar formas en el aire. Lo que ves como líneas, formas e imágenes es en realidad el haz trazando recorridos más rápido de lo que tus ojos pueden seguir.

Un flujo de puntos es el conjunto de datos que indica al láser adónde moverse a continuación y cuándo debe encenderse o apagarse el haz. En Liberation, los clips se convierten en este flujo de puntos en tiempo real a medida que se envían a los láseres.

Liberation te ofrece un control detallado sobre cómo se genera este flujo de puntos, lo que te permite equilibrar suavidad, brillo y rendimiento para cada láser.

{% hint style="info" %}
Si estás acostumbrado a software láser más antiguo que depende de flujos de puntos precalculados, este enfoque puede parecerte diferente al principio. Sin embargo, la generación de puntos en tiempo real permite optimizar el mismo contenido de forma distinta para cada láser. Esto facilita trabajar con varios láseres que tienen distintas velocidades o calidades de scanner, sin duplicar ni reconstruir contenido. También mantiene los archivos de clip muy pequeños; por eso todo el Clip Deck predeterminado de Liberation ocupa solo unos pocos megabytes en lugar de gigabytes.
{% endhint %}

Los ajustes básicos de scanner son:

* **Speed** es la velocidad del scanner, es decir, lo rápido que se mueve el láser para dibujar formas. Equivale a ajustar la tasa de puntos en software láser tradicional, pero en Liberation puedes cambiar la velocidad a la que se mueve el láser _independientemente de la tasa de puntos_. No deberías necesitar ajustar esto.
* **Scanner sync** —a veces conocido como _blank shift_, anteriormente Colour Shift—. Los scanners mueven el láser muy rápido, pero normalmente el cambio de brillo y color no está sincronizado con el movimiento. Esto aparece como pequeñas “colas” de luz parpadeantes en el borde de haces y líneas. Usa este ajuste para sincronizar el movimiento y el color entre sí. Consulta [Panel de ajustes de Laser output](../setting-up/laser-settings/ "mention")

Los demás ajustes avanzados de scanner se tratan en el capítulo [Avanzado](../advanced/ "mention").

### Zoning

Para ver una guía completa sobre cómo configurar y zonificar láseres, consulta: [Resumen del proceso de configuración de láseres](../setting-up/setting-up-lasers.md "mention")
