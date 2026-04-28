---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introducción

El 3D Visualiser de Liberation es una función increíblemente útil: puedes diseñar y ajustar tus shows sin necesitar ningún láser. Para mí ha demostrado ser una herramienta de enorme valor, especialmente en montajes complejos con un gran número de láseres.

### Navegar por el espacio 3D

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>La vista de 3D Visualiser</p></figcaption></figure>

* Haz clic y arrastra para rotar la vista alrededor del punto de órbita
* Usa la rueda del ratón para acercarte o alejarte del punto de órbita
* Haz clic y arrastra manteniendo pulsada la tecla shift para mover la cámara lateralmente (strafe) a izquierda, derecha, arriba y abajo a lo largo del plano XY
* Haz doble clic en cualquier punto del visualizador para restablecer la posición de la cámara

### Ajustes

Abre el panel _3D Visualiser Settings_ desde el menú _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>El panel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - cambia el tamaño del visualizador en relación con el resto de la app
* **Brightness Adjustment** - cambia el brillo con el que se muestran los láseres
* **Show laser numbers** - muestra el número correspondiente encima de cada láser
* **Show zone names** - muestra los nombres de zona correspondientes debajo de cada láser

### Ajustes de cámara

Estos ajustes están relacionados principalmente con la cámara virtual dentro del espacio 3D. Verás un desplegable con presets para estos ajustes, que puedes guardar y volver a cargar.

* **Camera distance -** La cámara siempre apunta a su _Orbit point_. La distancia de cámara indica lo lejos que está de ese punto. También puedes ajustar este valor con la rueda del ratón.
* **FOV -** Field of view: determina si la cámara tiene un ángulo más amplio o está más ampliada.
* **Orbit position** - describe la rotación actual alrededor del punto de órbita. El primer valor es la rotación alrededor del eje X (pitch) y el segundo valor es la rotación alrededor del eje Y (yaw).
* **Orbit centre point** - la posición del punto de órbita en el espacio 3D, x, y, z.
* **Grid height** - la altura de la cuadrícula desde el “suelo” (es decir, donde y = 0).

### Ajustes de contenido

Estos ajustes determinan dónde se colocan los láseres (y el Canvas) dentro del entorno 3D. Verás un desplegable con presets para estos ajustes, que puedes guardar y volver a cargar.

#### Láseres

Cada láser tiene su propio grupo de ajustes, que puedes desplegar usando el pequeño triángulo blanco.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Ajustes de láser del 3D Visualiser</p></figcaption></figure>

* **3D Position** - la posición x, y y z del láser.
* **3D Orientation** - la rotación del láser alrededor de cada uno de los ejes x, y y z.
* **Flip X / Flip Y** - invierte la salida virtual del láser. TEN EN CUENTA que esto no debería ser necesario; es mejor usar los ajustes de inversión/orientación del láser para corregir cualquier inconsistencia con tu hardware.
* **Output Range horizontal / vertical** - está relacionado con el ángulo máximo/mínimo de los scanners de tu láser. 60º es lo estándar, pero puedes ajustarlo si tus láseres son diferentes.

#### Canvas

Si utilizas el sistema de Canvas, también puedes incluir la imagen del Canvas dentro de la vista 3D. Activa la casilla para renderizar el Canvas dentro de la vista y usa los ajustes de posición, orientación y escala para definir cómo aparece en tu vista 3D.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Ajustes de Canvas del 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
¿Ves láseres “fantasma”? El 3D Visualiser es en cierto modo independiente de la configuración de láseres, y es posible tener más láseres dentro del visualizador que en Liberation. Cuando añades un láser a tu proyecto, también se añade un nuevo objeto de láser dentro del visualizador. Pero si eliminas un láser, seguirá quedando un objeto de láser “fantasma” en el visualizador.

Para eliminar todos los láseres fantasma, haz clic en el botón _Remove extra 3D laser objects_ (en la parte inferior del panel de ajustes de 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
