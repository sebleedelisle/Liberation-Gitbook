---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Preguntas frecuentes

## Hardware

#### **¿Liberation funciona en Windows?**

Sí. Liberation es totalmente compatible con **Windows 10 y 11 (64 bits)**, con exactamente las mismas funciones que la versión para Mac. Cada versión se publica simultáneamente para ambas plataformas.

#### **¿Liberation funciona en Mac?**

Sí. Liberation es totalmente compatible con **Mac (macOS 12 Monterey y versiones posteriores)**, con plena paridad de funciones respecto a la versión para Windows. Todas las actualizaciones se publican a la vez.

#### **¿Cuál es el equipo mínimo necesario?**

Depende de cuántos láseres quieras controlar. Si solo vas a usar unos pocos láseres, te bastará con un equipo de especificaciones modestas. Cualquier Mac con Apple Silicon funciona muy bien y debería poder controlar hasta 100 láseres. Si vas a ejecutar shows complejos con mucho en juego, te recomendamos usar el mejor equipo que puedas permitirte.

#### **¿Cuántos láseres puedo controlar con Liberation?**

Liberation puede ejecutar muchos láseres en un solo ordenador. Se ha probado con más de 100 controladores láser, así que la respuesta depende de:

* la CPU de tu ordenador
* la velocidad de la red
* el nivel de tu licencia

#### **¿Qué controladores MIDI puedo usar?**

Liberation se ha diseñado y optimizado en torno al popular controlador MIDI APC40 Mk2. También funciona con el APC40 Mk1. Consulta [Controladores MIDI en directo](midi-control/live-control-with-the-apc40.md "mention")

Liberation también es compatible con APC Mini y MIDI Fighter Twister. El APC40 Mk2 sigue siendo el controlador de referencia más completo.

También existe el sistema MIDI Send/Receive, que ofrece control MIDI adicional. Consulta [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Consulta [Control MIDI](midi-control/ "mention") para obtener más información.

#### **¿Puedo usarlo con cualquier controlador MIDI?**

Para otros controladores, usa el sistema MIDI Send/Receive o un traductor MIDI que pueda enviar los mensajes MIDI predeterminados de Liberation. Busca consejos sobre esta configuración en el [foro](https://forum.liberationlaser.com), aunque, siendo realistas, el APC40 Mk2 sigue siendo la mejor opción para la mayoría de shows en directo.

## Controladores láser

#### **¿Qué controladores láser son compatibles con Liberation?**

* [Ether Dream (recomendado)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury de X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (puede que tengas que actualizar el firmware)
* LaserCube USB (y LaserDock)
* protocolo de red LaserCube (con conexión por cable)
* AVB, como se usa en los [láseres LASollinger](https://laseranimation.com/en/) (actualmente solo en macOS y en pruebas)

Consulta [Láseres y controladores compatibles (DAC)](hardware/compatible-lasers-and-controllers-dacs.md "mention") para obtener más información.

#### **¿Por qué no dais soporte a \[otra marca de] controlador láser?**

Para fomentar una mayor interoperabilidad entre software y hardware, Liberation solo dará soporte a DAC que tengan un protocolo de comunicación publicado. Creo que esta es la mejor vía de avance para la industria del láser.

#### **¿Cómo puedo saber si mi láser se puede usar con Liberation?**

Si tu láser tiene alguno de los siguientes elementos, puedes usarlo con Liberation:

* Una **entrada ILDA** externa: un conector D de 25 pines, usado con un controlador externo compatible.
* Un **Ether Dream** instalado internamente.
* Cualquier **LaserCube** (funciona tanto con LaserCube USB como con Wi-Fi).
* Una **unidad X-Laser con sistema Mercury integrado** (en modo Ether Dream).
* Un **proyector LaserAnimation Sollinger con AVB integrado** (solo macOS, requiere dispositivos de red compatibles con AVB; actualmente en pruebas).

Consulta [Láseres y controladores compatibles (DAC)](hardware/compatible-lasers-and-controllers-dacs.md "mention") para obtener más información.

#### **¿Puedo usar Liberation con mi LaserCube?**

Sí, Liberation funciona directamente con cualquier LaserCube. Consulta [LaserCube](hardware/lasercube.md "mention")

## Licencias

#### **¿Cuál es el precio de una licencia?**

Consulta la página de la [tienda](https://liberationlaser.com/shop) para ver los precios actuales.

#### **¿Qué limitaciones hay entre los niveles de licencia?**

Consulta la página de la [tienda](https://liberationlaser.com/shop) para ver las opciones de licencia actuales.

Ten en cuenta que puedes configurar, previsualizar y diseñar shows con tantos láseres como quieras en **todos** los niveles, incluso el gratuito, y no hay ninguna otra limitación aparte del número de láseres que puedes _armar_. Todas las demás funciones de Liberation están disponibles para todos los usuarios.

#### **¿Puedo pasar a un nivel superior?**

Puedes cambiar a un nivel superior en cualquier momento. Recibirás un reembolso parcial por el tiempo restante de tu periodo de pago actual, y tu nuevo nivel de licencia empezará inmediatamente. Consulta [Subir o bajar el nivel de tu licencia](installation/upgrade-downgrade-your-license.md "mention")

#### **¿Puedo bajar el nivel de mi licencia?**

Puedes bajar de nivel en cualquier momento, pero el cambio se aplicará al final de tu periodo de pago actual. Consulta [Subir o bajar el nivel de tu licencia](installation/upgrade-downgrade-your-license.md "mention")

#### **¿Puedo pausar los pagos de mi licencia?**

Sí. La licencia se puede pausar en la siguiente fecha de suscripción y reactivar en cualquier momento. Esto resulta útil si empiezas y dejas de usarla periódicamente, y no tendrás que volver a introducir los datos de tu tarjeta. Consulta [Pausar o cancelar pagos](installation/cancel-your-subscription.md "mention")

#### **¿Cómo cancelo mi licencia definitivamente?**

Puedes cancelar tu licencia recurrente en cualquier momento, y se desactivará automáticamente al final del periodo de pago actual. Consulta [Pausar o cancelar pagos](installation/cancel-your-subscription.md "mention")

#### **¿Cómo autorizo mi ordenador con mi licencia?**

Una vez que hayas comprado una licencia, puedes autorizar el ordenador desde el propio software Liberation. Verás un botón _Authorise_ en la pantalla _About_ que te pedirá que inicies sesión en el sitio web. Sigue las instrucciones en pantalla para completar el proceso de autorización. Consulta [Autorizar y desautorizar](installation/authorising-and-de-authorising.md "mention")

#### **¿Con qué frecuencia tengo que conectar mi ordenador a internet?**

Cada vez que una licencia de pago recurrente se renueve correctamente, tendrás que conectar Liberation a internet para actualizar su licencia interna. Por tanto, si tienes una licencia mensual con renovación automática, tendrás que conectarte cada mes.

#### **¿Qué ocurre si no puedo conectar mi ordenador a internet después del siguiente pago?**

Para las licencias de pago recurrentes mensuales, Liberation normalmente te da un periodo de gracia de 7 días después de que se renueve tu licencia de pago para conectarte a internet y actualizar su licencia interna. Pasado ese periodo, Liberation volverá al modo _Free_.

#### **¿Qué ocurre si caduca mi tarjeta de crédito?**

Recibirás una notificación por correo electrónico de nuestro proveedor de pagos, y tendrás que actualizar los datos de tu tarjeta. Inicia sesión en el sitio web y usa _UPDATE CARD DETAILS_ en la página de la licencia, o _Update_ en _Billing and payments_. Debes hacerlo dentro del periodo de gracia para evitar perder el acceso a las funciones de pago.

#### **¿En cuántos ordenadores puedo instalar Liberation?**

Puedes instalar Liberation en tantos ordenadores como quieras. Las autorizaciones de licencia solo son necesarias para activar la salida láser / DMX, y tu nivel de licencia determina cuántos ordenadores pueden estar autorizados para salida al mismo tiempo. Consulta [Cómo funciona el sistema de licencias](installation/how-licensing-works.md "mention")

#### **¿Cómo muevo mi licencia de un ordenador a otro?**

* Abre Liberation en el ordenador que ya no quieras usar
* Asegúrate de estar conectado a internet y haz clic en el botón _De-authorise this computer_ de la pantalla _About_
* Ahora abre Liberation en el ordenador nuevo
* Haz clic en el botón _Authorise this computer_ de la pantalla _About_.
* Se abrirá el sitio web; inicia sesión y sigue las instrucciones en pantalla para completar la autorización

También puedes desautorizar de forma remota un ordenador al que ya no tengas acceso (con algunas limitaciones). Consulta [Autorizar y desautorizar](installation/authorising-and-de-authorising.md "mention")

#### **¿Puedo desautorizar Liberation en un ordenador que se ha perdido o robado?**

Puedes desautorizar el ordenador desde el sitio web. Si la instalación de Liberation no se ha conectado a internet desde su última actualización de licencia, esto puede hacerse inmediatamente.

Si no, la desautorización tendrá efecto cuando la licencia se actualice de nuevo o cuando el ordenador se conecte a internet, lo que ocurra primero. Si necesitas volver a autorizar un ordenador nuevo con urgencia, ponte en contacto con soporte.

### Uso de Liberation

#### La configuración predeterminada tiene 8 láseres. ¿Cómo lo cambio?

Consulta [Configurar tu proyecto](setting-up/setting-up-your-project.md "mention") y [Añadir / quitar láseres](setting-up/adding-removing-lasers.md "mention")

#### ¿Puedo copiar los ajustes de zones de un láser a los demás?

Sí. Consulta [Copiar zones entre láseres](output-view/copy-zones-between-lasers.md "mention")

#### ¿Puedo escribir un número en vez de usar un deslizador?

Sí. Haz clic en el deslizador con `Cmd / Ctrl` pulsado y podrás introducir el valor con el teclado.

#### **¿Cómo sincronizo Liberation con música?**

Tiene un sistema inteligente de "tap tempo" que funciona como esperarías, pero también puedes usar un reloj MIDI externo o Ableton Link. Consulta [Tempo / sincronización](tempo-synchronisation.md "mention"). La timeline se puede sincronizar con timecode LTC/SMPTE entrante a través de cualquier interfaz de audio. Consulta [Timecode](timecode.md "mention").

#### ¿Qué ajustes tengo que modificar para obtener la mejor salida del láser?

El ajuste principal es _Scanner Sync_, que compensa el pequeño retardo entre el movimiento de los espejos y el cambio de brillo de los láseres. Si los puntos o haces de tu láser tienen pequeñas “colas”, tendrás que ajustar esto. (Consulta las fotos de la página [Panel de ajustes de salida láser](setting-up/laser-settings.md "mention") para ver un ejemplo de “colas”).

También puedes probar a cambiar la velocidad del escáner: más lenta si tus escáneres son básicos, o más rápida si son buenos. Pero **úsalo con precaución, ya que puedes dañar los escáneres si los fuerzas demasiado.**

También hay algunos ajustes de escáner predefinidos. La opción predeterminada es conservadora y adecuada para la mayoría de necesidades de haces láser. Pero hay otros presets si tienes escáneres mejores, y también hay presets ajustados para gráficos.

Para obtener más información, consulta [Panel de ajustes de salida láser](setting-up/laser-settings.md "mention"); y para saber cómo crear tus propios presets, consulta [◼️ Presets de escáner y perfiles de renderizado](advanced/scanner-presets.md "mention") (avanzado, en curso)

También puedes corregir el balance de color con los ajustes de _Colour calibration_. Consulta [Calibración de color](advanced/colour-calibration.md "mention") (técnica avanzada)

#### ¿Qué hace el ajuste _Latency(ms)_?

Es la latencia de fotogramas, o la cantidad máxima de tiempo entre que se genera un fotograma y se envía posteriormente a un láser. No deberías necesitar ajustarlo, pero si tienes problemas de red puedes probar a aumentarlo. Consulta [Ajuste de latencia](setting-up/latency-setting.md "mention") para más detalles.

### Clips

#### ¿Cómo ajusto las zones y los ajustes de un Clip sin ejecutarlo?

Haz clic con `Alt / Option` para convertirlo en el _Clip seleccionado actualmente_, pero sin activarlo. Consulta también [Iniciar / detener Clips](clips/starting-stopping-clips.md "mention")

#### ¿Cómo copio Clips?

Haz clic y arrastra mientras mantienes pulsada la tecla `Alt / Option`. Consulta también [Organizar tu Clip Deck](clips/organising-your-clip-deck.md "mention")

#### ¿Cómo elimino Clips?

Haz clic y arrástralos fuera del Clip Deck. Consulta también [Organizar tu Clip Deck](clips/organising-your-clip-deck.md "mention")

#### ¿Cómo hago selección múltiple, elimino, combino Clip Decks, etc.?

Consulta [Organizar tu Clip Deck](clips/organising-your-clip-deck.md "mention")

#### ¿Qué indican el pequeño símbolo de micrófono y otros iconos del Clip?

Sirven para mostrar que un Clip recibe entrada de sonido o MIDI, y los 3 puntos indican que hay un retardo de zone. Consulta [¿Qué son los iconos pequeños de los botones de Clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
