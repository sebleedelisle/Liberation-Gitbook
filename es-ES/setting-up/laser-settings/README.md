# ✅ Panel de ajustes de Laser output

Abre el panel de ajustes _Laser output_ desde el menú _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Esto te mostrará los ajustes del láser seleccionado en ese momento, que puedes cambiar:

* con su botón numérico en el panel _Laser overview_
* con una tecla numérica del teclado; las teclas 1 a 0 abren los láseres 1 - 10
* con la tecla `Tab` para recorrer los láseres (`Shift + Tab` va hacia atrás).

En la parte superior de este panel verás:

* un botón numérico: haz clic en él para armar/desarmar este láser. Se muestra en rojo cuando el láser está armado.
* un control deslizante _Brightness_ solo para este láser. Ten en cuenta que se combina con el brillo global.
* el conmutador _Test Pattern_ y el selector de patrón. Esto te permite elegir un patrón de prueba específico solo para este láser. (Estos controles están duplicados en la barra de herramientas de la vista Output).

### Orientación de la salida / corrección del reflejo

Los siguientes elementos sirven para corregir la configuración de tu láser, de modo que se comporte de forma coherente en Liberation.

* **Flip horizontal / vertical**: estas opciones te permiten corregir la salida de tu láser

{% hint style="info" %}
No deberías necesitar cambiar los ajustes de inversión horizontal / vertical a menos que tu láser esté cableado incorrectamente o tenga botones de inversión X/Y en la parte trasera que no estén configurados correctamente. Si quieres que la salida se invierta para un clip concreto, puedes hacerlo en el propio clip.
{% endhint %}

* **Orientation**: si tu láser se ha montado de lado o boca abajo, puedes corregir la rotación con este ajuste.
* **Fine position adjustments**: se pueden usar para corregir desplazamientos o rotaciones muy pequeños. Están pensados para corregir deriva/asentamiento si un láser se ha dejado encendido durante la noche o durante periodos largos.

{% hint style="info" %}
Ten en cuenta que las correcciones de orientación / reflejo no cambian nada en el 3D Visualiser; deben usarse para corregir la salida del láser real y hacer que coincida con lo que aparece en el 3D Visualiser.
{% endhint %}

### Copiar ajustes de láser

Consulta [#copy-laser-settings](./#copy-laser-settings "mention").

### Ajustes de scanner

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

El ajuste de velocidad determina lo rápido que se mueven los scanners.

{% hint style="danger" %}
Aunque los ajustes predeterminados son bastante conservadores, puedes dañar los scanners si los haces trabajar demasiado rápido. Ten cuidado, especialmente al aumentar la velocidad.
{% endhint %}

{% hint style="info" %}
Este ajuste de velocidad no cambia la tasa de puntos; en su lugar, ajusta lo separados que están esos puntos. Para más información, consulta [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

El haz cambia de color y se enciende y apaga mientras los scanners lo desplazan, y normalmente estas dos cosas no están perfectamente sincronizadas entre sí. Ajusta este valor para volver a alinearlas.

{% hint style="info" %}
A veces esto se conoce como _blank shift_, pero personalmente prefiero el término _scanner sync_: es un poco más preciso, ya que ajusta la temporización de todos los cambios de color con respecto al movimiento del scanner.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>“Colas” de láser: Colour shift no está ajustado correctamente</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>¡Sin “colas” de láser! ¡Colour shift está bien ajustado!</p></figcaption></figure></div>

Si ves pequeñas “colas” en la salida de tu láser, probablemente sea porque hay que ajustar la sincronización del scanner. Si las colas siguen apareciendo hagas lo que hagas, es probable que estés haciendo trabajar los scanners/controladores láser más rápido de lo que pueden soportar. Prueba a reducir la velocidad del scanner.

#### Presets de scanner

Usa esto para elegir un ajuste de scanner prediseñado. La opción predeterminada suele ir bien, así que no deberías necesitar cambiar este ajuste a menos que tengas scanners especialmente malos (o buenos). Si quieres profundizar más, consulta [scanner-presets.md](../../advanced/scanner-presets.md "mention")

#### Calibración de color

Puedes usar este sistema para corregir la curva de brillo y el balance de blancos de tu láser. Consulta [colour-calibration.md](../../advanced/colour-calibration.md "mention")

#### Ajustes avanzados

No deberías necesitar tocar estos ajustes, pero si tienes curiosidad, consulta [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md "mention")
