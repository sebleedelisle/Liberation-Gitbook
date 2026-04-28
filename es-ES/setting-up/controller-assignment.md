---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Asignación de controladores

Una vez que hayas configurado los láseres en Liberation, puedes asignar cada uno a un controlador láser del mundo real. (Consulta [compatible-lasers-and-controllers-dacs.md](../hardware/compatible-lasers-and-controllers-dacs.md "mention") para comprobar qué hardware puedes usar). Los controladores estarán conectados por USB o a través de la red.

* Abre el panel _Controller Assignment_ desde la opción de menú _View -> Controller Assignment_. (También puedes usar el botón _ASSIGN LASER CONTROLLERS_ del panel _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Panel Controller Assignment"><figcaption></figcaption></figure>

* El panel está dividido en dos partes: a la izquierda hay una lista de láseres y a la derecha la lista de controladores disponibles. Si no ves tu controlador láser en la lista, pulsa el botón _REFRESH_. Si sigues teniendo problemas, consulta [troubleshooting](../troubleshooting/ "mention").
* Para asignar un controlador a un láser, haz clic y arrastra desde la derecha hasta una ranura de láser libre en la izquierda. Esto le indica a Liberation qué controlador debe usar para cada láser. (Si cambias de opinión, puedes arrastrar los controladores libremente hacia arriba o hacia abajo de un láser a otro.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Lista de controladores" width="375"><figcaption></figcaption></figure>

* Si ves un cuadrado verde junto al controlador, significa que Liberation se ha conectado a él correctamente.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Un Ether Dream y un Helios DAC asignados a los láseres 2 y 3, respectivamente</p></figcaption></figure>

{% hint style="info" %}
Ten en cuenta que, cada vez que te conectes a un controlador, el láser se desarmará automáticamente.
{% endhint %}

* Un cuadrado naranja 🟧 significa que el controlador tiene problemas de conexión intermitentes. Normalmente se debe a un problema de red; consulta [troubleshooting](../troubleshooting/ "mention").
* Un cuadrado rojo 🟥 significa que no se puede acceder al controlador; consulta [troubleshooting](../troubleshooting/ "mention").
* El _botón de desconexión_ (X) desconecta el controlador, pero no lo elimina de la asignación del láser. Después puedes usar el _botón de reconexión_ (icono de flecha de actualización) para volver a conectarlo, o hacer clic de nuevo en el _botón de desconexión_ para borrar la asignación.
* _Función avanzada:_ abre el panel de análisis del controlador haciendo clic en el botón con aspecto de gráfica. Es una función avanzada que proporciona información detallada sobre el flujo de datos y puede ayudarte a solucionar problemas. (Es posible que esta opción no esté disponible para algunos tipos de controlador.)
* Puedes usar el _botón de renombrar_ (lápiz) para cambiar el nombre de este controlador por el que quieras. Tiene sentido ponerle un nombre que te ayude a asociarlo fácilmente con un hardware concreto. Si está integrado en un láser, quizá quieras nombrarlo en consecuencia, por ejemplo _LaserCube Ultra #1_ o _Triton T5 #3._ Estos nombres se guardarán con tu instalación de Liberation y aparecerán a partir de ahora; pueden resultarte muy útiles para identificar rápidamente tus láseres.

{% hint style="info" %}
Consejo pro: haz **doble clic** en un controlador de la derecha para asignarlo automáticamente al siguiente láser disponible de la izquierda. ¡Puede ahorrarte mucho tiempo si tienes muchos láseres que asignar!
{% endhint %}

Puedes usar los botones _DISCONNECT ALL_ y _RECONNECT ALL_ para restablecer rápidamente todas las conexiones. Esto resulta útil si tienes problemas de red.
