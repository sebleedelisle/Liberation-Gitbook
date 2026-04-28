---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardware

#### **¿Liberation funciona en Windows?**

Sí. Liberation es totalmente compatible con **Windows 10 y 11 (64 bits)**, con exactamente las mismas funciones que la versión para Mac. Cada versión se publica simultáneamente para ambas plataformas.

#### **¿Liberation funciona en Mac?**

Sí. Liberation es totalmente compatible con **Mac (macOS 12 Monterey y posteriores)**, con las mismas funciones que la versión para Windows. Todas las actualizaciones se publican a la vez.

#### **¿Cuál es el equipo mínimo necesario?**

Depende de cuántos láseres quieras controlar. Si solo vas a usar unos pocos láseres, te bastará con un equipo de especificaciones modestas. Cualquier Mac con Apple Silicon funciona muy bien y debería poder controlar hasta 100 láseres. Si vas a ejecutar shows complejos donde todo debe salir perfecto, te recomendamos usar el mejor equipo que puedas permitirte.

#### **¿Cuántos láseres puedo controlar con Liberation?**

Liberation puede controlar muchos láseres desde un solo ordenador. Se ha probado con más de 100 controladores láser, así que la respuesta depende de:

* la CPU de tu ordenador
* la velocidad de la red
* tu tipo de suscripción

#### **¿Qué controladores MIDI puedo usar?**

Liberation se ha diseñado y optimizado alrededor del popular controlador MIDI APC40 Mk2. También funciona con el APC40 Mk1. Consulta [live-control-with-the-apc40.md](midi-control/live-control-with-the-apc40.md "mention")

Estamos añadiendo poco a poco más controladores MIDI y actualmente también son compatibles el APC Mini Mk2 y el MIDI Fighter Twister.

También existe el sistema MIDI Send/Receive, que ofrece control MIDI adicional. Consulta [midi-send-receive.md](midi-control/midi-send-receive.md "mention")

Consulta [midi-control](midi-control/ "mention")para obtener más información.

#### **¿Puedo usarlo con cualquier controlador MIDI?**

Actualmente estamos trabajando en un sistema MIDI configurable que lo permitirá en el futuro. Mientras tanto, algunos usuarios han conseguido hacerlo usando un intérprete MIDI que puede convertir cualquier mensaje MIDI para el sistema MIDI Send/Receive, pero es un proceso avanzado y algo laborioso. Busca consejos sobre esta configuración en el [forum](https://forum.liberationlaser.com), aunque siendo realistas el APC40 es la mejor opción.

## Laser controllers

#### **¿Qué controladores láser son compatibles con Liberation?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (puede que tengas que actualizar el firmware)
* LaserCube USB (y LaserDock)
* Protocolo de red LaserCube (con una conexión cableada)
* AVB, como el que usan los láseres [LASollinger lasers](https://laseranimation.com/en/) (actualmente solo macOS, en pruebas)

Consulta [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") para obtener más información

#### **¿Por qué no dais soporte a \[otra marca de] controlador láser?**

Para fomentar una mayor interoperabilidad entre software y hardware, Liberation solo dará soporte a DACs que tengan un protocolo de comunicación publicado. Creo que esta es la mejor vía para el sector del láser.

#### **¿Cómo puedo saber si mi láser se puede usar con Liberation?**

Si tu láser tiene una de las siguientes opciones, puedes usarlo con Liberation:

* Una **entrada ILDA externa**: un conector D de 25 pines, usado con un controlador externo compatible.
* Un **Ether Dream** instalado internamente.
* Cualquier **LaserCube** (funciona tanto con LaserCube USB como con LaserCube Wi-Fi).
* Una **unidad X-Laser con sistema Mercury integrado** (en modo Ether Dream).
* Un **proyector LaserAnimation Sollinger con AVB integrado** (solo macOS, requiere dispositivos de red compatibles con AVB, actualmente en pruebas).

Consulta [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md "mention") para obtener más información

#### **¿Puedo usar Liberation con mi LaserCube?**

Sí, Liberation funciona directamente con cualquier LaserCube. Consulta [lasercube.md](hardware/lasercube.md "mention")

## Licences

#### **¿Cuál es el precio de una licencia?**

Consulta la página de la [shop](https://liberationlaser.com/shop) para ver los precios actuales.

#### **¿Qué limitaciones hay entre los niveles de licencia?**

Consulta la página de la [shop](https://liberationlaser.com/shop) para ver las opciones de licencia actuales.

Ten en cuenta que puedes configurar, previsualizar y diseñar shows con tantos láseres como quieras en **todos** los niveles, incluso en el gratuito, y no hay ninguna otra limitación aparte del número de láseres que puedes _arm_. Todas las demás funciones de Liberation están disponibles para todos.

#### **¿Puedo subir a un nivel superior?**

Puedes subir a un nivel superior en cualquier momento. Recibirás un reembolso parcial por el tiempo restante de tu licencia actual y tu nuevo plan empezará inmediatamente. Consulta [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **¿Puedo bajar mi licencia de nivel?**

Puedes bajar de nivel en cualquier momento, pero el cambio se aplicará al final del periodo de licencia actual. Consulta [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md "mention")

#### **¿Cómo autorizo mi ordenador con mi licencia?**

Una vez que hayas comprado una licencia, puedes autorizar el ordenador desde el propio software Liberation. Verás un botón _Authorise_ en la pantalla _About_ que te pedirá iniciar sesión en el sitio web. Sigue las instrucciones en pantalla para completar el proceso de autorización. Consulta [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **¿Cada cuánto tengo que conectar mi ordenador a internet?**

Cada vez que se renueve la licencia, tendrás que conectar Liberation a internet para actualizar su licencia interna. Con un pago recurrente mensual, tendrás que conectarlo cada mes.

#### **¿Qué ocurre si no puedo conectar mi ordenador a internet después de la renovación?**

Liberation te dará un periodo de gracia de 7 días después de que se renueve tu licencia para conectarlo a internet y actualizar su licencia interna. Pasado ese periodo, Liberation volverá al modo _Free_.

#### **¿Qué ocurre si caduca mi tarjeta de crédito?**

Recibirás una notificación por correo electrónico de nuestro proveedor de pagos y tendrás que actualizar tu método de pago. Inicia sesión en el sitio web y usa el enlace _Update payment details_ en la página de suscripciones.

#### **¿Cómo cancelo mi licencia recurrente?**

Inicia sesión en el sitio web, abre la página _Your subscriptions_, selecciona la suscripción que quieres cancelar y haz clic en el enlace _Cancel Subscription_. Puedes seguir usando Liberation durante el resto del periodo de licencia.

#### **¿En cuántos ordenadores puedo instalar Liberation?**

Puedes instalar Liberation en tantos ordenadores como quieras. Las autorizaciones de licencia solo son necesarias para activar la salida láser / DMX, y tu nivel de licencia determina cuántos ordenadores pueden estar autorizados para salida al mismo tiempo. Consulta [how-licensing-works.md](installation/how-licensing-works.md "mention")

#### **¿Cómo traslado mi licencia de un ordenador a otro?**

* Abre Liberation en el ordenador que ya no quieres usar
* Asegúrate de que está conectado a internet y haz clic en el botón _De-authorise this computer_ en la pantalla _About_
* Ahora abre Liberation en el nuevo ordenador
* Haz clic en el botón _Authorise this computer_ en la pantalla _About_.
* Se abrirá el sitio web; inicia sesión y sigue las instrucciones en pantalla para completar la autorización

También puedes desautorizar de forma remota un ordenador al que ya no tienes acceso (con algunas limitaciones). Consulta [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md "mention")

#### **¿Puedo desautorizar Liberation en un ordenador que se ha perdido o ha sido robado?**

Puedes desautorizar el ordenador desde el sitio web. Si la instalación de Liberation no ha estado en línea desde tu última renovación, esto puede hacerse inmediatamente.

Si no, la desautorización se aplicará cuando se renueve la suscripción o cuando el ordenador se conecte a internet, lo que ocurra primero. Si necesitas reautorizar un nuevo ordenador con urgencia, ponte en contacto con soporte.

### Using Liberation

#### La configuración por defecto tiene 8 láseres. ¿Cómo cambio esto?

Consulta [setting-up-your-project.md](setting-up/setting-up-your-project.md "mention") y [adding-removing-lasers.md](setting-up/adding-removing-lasers.md "mention")

#### ¿Puedo copiar la configuración de zonas de un láser a los demás?

Sí. Consulta [copy-zones-between-lasers.md](output-view/copy-zones-between-lasers.md "mention")

#### ¿Puedo escribir un número en vez de usar un deslizador?

Sí. Haz `Cmd / Ctrl`-clic en el deslizador y podrás introducir el valor con el teclado.

#### **¿Cómo sincronizo Liberation con la música?**

Tiene un sistema inteligente de "tap tempo" que funciona como esperarías, pero también puedes usar un reloj MIDI externo o Ableton Link. Consulta [tempo-synchronisation.md](tempo-synchronisation.md "mention"). La línea de tiempo puede sincronizarse con timecode LTC/SMPTE entrante a través de cualquier interfaz de audio. Consulta [timecode.md](timecode.md "mention").

#### ¿Qué ajustes tengo que cambiar para obtener la mejor salida del láser?

El ajuste principal es _Colour Shift_, que compensa el pequeño retraso entre el movimiento de los espejos y el cambio de brillo de los láseres. Si los puntos o haces de tu láser tienen pequeñas "colas", tendrás que ajustar esto. (Consulta las fotos de la página [laser-settings.md](setting-up/laser-settings.md "mention") para ver un ejemplo de "colas")

También puedes probar a cambiar la velocidad del escáner: más lenta si tus escáneres son básicos, o más rápida si son buenos. Pero **úsalo con cuidado, ya que puedes dañar los escáneres si los fuerzas demasiado.**

También hay algunos presets de escáner. La opción por defecto es conservadora y adecuada para la mayoría de necesidades de haces láser. Pero hay otros presets para escáneres mejores, y también presets ajustados para gráficos.

Para obtener más información, consulta [laser-settings.md](setting-up/laser-settings.md "mention"); y para saber cómo crear tus propios presets, consulta [scanner-presets.md](advanced/scanner-presets.md "mention") (avanzado, en curso)

También puedes corregir el balance de color usando los ajustes de _Colour calibration_. Consulta [colour-calibration.md](advanced/colour-calibration.md "mention")(técnica avanzada)

#### ¿Qué hace el ajuste _Latency(ms)_?

Es la latencia de fotogramas, es decir, la cantidad máxima de tiempo entre que se genera un fotograma y se envía posteriormente a un láser. No deberías necesitar ajustarla, pero si tienes problemas de red puedes probar a aumentarla. Consulta [latency-setting.md](setting-up/latency-setting.md "mention") para obtener más detalles.

### Clips

#### ¿Cómo ajusto las zonas y la configuración de un clip sin ejecutarlo?

Haz `Alt / Option`-clic para convertirlo en el _currently selected clip_, pero sin activarlo. Consulta también [starting-stopping-clips.md](clips/starting-stopping-clips.md "mention")

#### ¿Cómo copio clips?

Haz clic y arrastra manteniendo pulsada la tecla `Alt / Option`. Consulta también [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### ¿Cómo elimino clips?

Haz clic en ellos y arrástralos fuera del clip deck. Consulta también [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### ¿Cómo hago selección múltiple, elimino, combino clip decks, etc.?

Consulta [organising-your-clip-deck.md](clips/organising-your-clip-deck.md "mention")

#### ¿Qué indican el pequeño símbolo de micrófono y otros iconos del clip?

Sirven para mostrarte que un clip recibe entrada de sonido o MIDI, y los 3 puntos indican que hay un retardo de zona. Consulta [what-are-the-small-icons-on-the-clip-buttons.md](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
