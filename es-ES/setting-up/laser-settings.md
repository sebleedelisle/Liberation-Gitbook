---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Panel de ajustes de Laser output

Abre el panel de ajustes _Laser output_ desde el menú _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Esto mostrará los ajustes del láser seleccionado actualmente, que puedes cambiar:

* mediante su botón numérico en el panel _Laser overview_
* con una tecla numérica del teclado; las teclas 1 a 0 abren los láseres 1 - 10
* con la tecla `Tab` para recorrer los láseres (`Shift + Tab` va hacia atrás).

En la parte superior de este panel verás:

* un botón numérico: haz clic en él para armar/desarmar este láser. Está en rojo cuando el láser está armado.
* un control deslizante _Brightness_ solo para este láser. Ten en cuenta que se combina con el brillo global.
* un conmutador _Test Pattern_ y un selector de patrón. Esto te permite elegir un patrón de prueba específico solo para este láser. (Estos controles también aparecen en la barra de herramientas de la vista Output).

### Corrección de orientación de salida / espejado

Los siguientes elementos sirven para corregir la configuración de tu láser, de modo que se comporte de forma coherente en Liberation.

* **Flip horizontal / vertical**: estas opciones te permiten corregir la salida de tu láser

{% hint style="info" %}
No deberías necesitar cambiar los ajustes de Flip horizontal / vertical a menos que tu láser esté cableado de forma incorrecta o tenga botones de inversión X/Y en la parte trasera que no estén configurados correctamente. Si quieres que la salida se voltee para un clip concreto, puedes hacerlo en el propio clip.
{% endhint %}

* **Orientation**: si tu láser se ha montado de lado o boca abajo, puedes corregir la rotación con este ajuste.
* **Fine position adjustments**: se puede usar para corregir desplazamientos o rotaciones muy pequeños. Está diseñado para corregir derivas o asentamientos si un láser se ha dejado durante la noche o durante periodos largos.

{% hint style="info" %}
Ten en cuenta que las correcciones de orientación / espejado no cambian nada en el 3D Visualiser. Deben usarse para corregir la salida del láser real y hacer que coincida con lo que aparece en el 3D Visualiser.
{% endhint %}

### Copy laser settings

Consulta [#copy-laser-settings](laser-settings.md#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

El ajuste Speed determina a qué velocidad se mueven los scanners.

{% hint style="danger" %}
Aunque los ajustes predeterminados son bastante conservadores, puedes dañar los scanners si los haces trabajar demasiado rápido. Ten cuidado, especialmente al aumentar la velocidad.
{% endhint %}

{% hint style="info" %}
Este ajuste de velocidad no cambia la tasa de puntos; en su lugar, ajusta cuánto se separan esos puntos entre sí. Para más información, consulta [◼️ Cómo genera Liberation contenido láser](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

El haz cambia de color y se enciende y apaga mientras los scanners lo desplazan, y estas dos cosas no suelen estar perfectamente sincronizadas entre sí. Ajusta este parámetro para volver a alinearlas.

{% hint style="info" %}
A veces se conoce como _blank shift_, pero personalmente prefiero el término _scanner sync_: es un poco más preciso, ya que ajusta la temporización de todos los cambios de color respecto al movimiento de los scanners.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>«Colas» de láser: Colour shift no está ajustado correctamente</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>¡Sin «colas» de láser! ¡Colour shift correcto!</p></figcaption></figure></div>

Si ves pequeñas «colas» en la salida del láser, probablemente sea porque Scanner sync necesita ajuste. Si las colas siguen apareciendo hagas lo que hagas, es probable que estés haciendo trabajar los scanners o los controladores del láser más rápido de lo que pueden soportar. Prueba a reducir la velocidad de los scanners.

#### Scanner presets

Usa esto para elegir un ajuste de scanner prediseñado. La opción predeterminada suele ir bien, así que no deberías necesitar cambiar este ajuste a menos que tengas scanners especialmente malos (o buenos). Si quieres profundizar más, consulta [◼️ Preajustes de escáner y perfiles de renderizado](../advanced/scanner-presets.md "mention")

#### Colour calibration

Puedes usar este sistema para corregir la curva de brillo y el balance de blancos de tu láser. Consulta [Calibración de color](../advanced/colour-calibration.md "mention")

#### Advanced settings

No deberías necesitar tocar estos ajustes, pero si tienes curiosidad, consulta [◼️ Ajustes avanzados de láser](../advanced/advanced-laser-settings.md "mention")
