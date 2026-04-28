---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Resumen de Canvas

El sistema Canvas de Liberation es relativamente sencillo, pero al principio puede resultar confuso. Aquí tienes una explicación conceptual para empezar.

{% hint style="info" %}
**Un momento, ¿necesito el sistema Canvas?**

¡Quizá no! Si solo vas a proyectar un único gráfico en un único láser, puedes hacerlo fácilmente con una zona de haces (aunque, por defecto, el contenido de las zonas de haces se invierte horizontalmente, así que tendrás que invertir el clip en X).

Pero si quieres repartir contenido gráfico entre varios láseres, o dividirlo en distintas secciones para mapearlo sobre arquitectura, entonces el sistema Canvas te vendrá perfecto.
{% endhint %}

### Canvas

En primer lugar, está el propio Canvas. Es lo que ves en la vista _CANVAS_ y representa, como su nombre indica, un gran lienzo donde puedes dibujar contenido en cualquier punto de ese espacio.

### Áreas de destino de Canvas

Se muestran como rectángulos con contorno azul en la vista Canvas, y son áreas a las que puedes enviar contenido. Envías el contenido de un clip a un área de destino de Canvas del mismo modo que enviarías un clip a una zona de haces. Verás los botones de las áreas de destino de Canvas a la derecha de los botones de las zonas de haces en el Clip Deck.

{% hint style="info" %}
Si no ves los botones de Canvas en el Clip Deck, prueba a desplazarte por los botones de zonas de haces con `Shift + Left / Right Arrow`. Deberías ver un botón para cada área de destino de Canvas con la etiqueta _CANVAS 1, CANVAS 2_, etc.
{% endhint %}

### Zonas de Canvas

Las zonas de Canvas son áreas dentro del Canvas que eliges enviar a un láser. Se representan como rectángulos con contorno rosa en la vista Canvas. Puedes hacer clic derecho en cada zona y seleccionar los láseres a los que quieres asignarla. Si ahora cambias a la vista _OUTPUT_ de ese láser, verás que ha aparecido una zona nueva.

{% hint style="danger" %}
ADVERTENCIA: si el láser está armado, podrías empezar a proyectar contenido de repente en una zona de Canvas predeterminada. Es mejor desarmar el láser antes de asignarle zonas de Canvas.
{% endhint %}

{% hint style="info" %}
También puedes asignar una zona de Canvas a un láser haciendo clic en el botón _add canvas zone_ en la vista _OUTPUT_. Consulta [zones.md](../output-view/zones.md "mention").
{% endhint %}

### Imágenes guía

Puedes añadir una imagen guía al Canvas y usarla como plantilla para tus gráficos. Es recomendable ajustar el tinte de color de la imagen guía (menú de clic derecho) y oscurecerla para poder ver tu contenido encima con más facilidad.

{% hint style="info" %}
Para mapping arquitectónico, me ha resultado útil crear una visualización «desplegada» del edificio que represente todas sus superficies como una imagen plana sin distorsión. La corrección de perspectiva de las distintas secciones se puede hacer usando la zona de Canvas en la vista _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Una imagen guía «aplanada» de Saltwell Hall en Gateshead, Reino Unido</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Las zonas de Canvas en una versión embrionaria de Liberation (¡c. 2017!). Observa que los rectángulos rosas eligen qué parte del Canvas se muestra, y que las vistas de salida de abajo muestran a qué parte de cada láser van esas zonas.</p></figcaption></figure>

### Canvas en el 3D visualiser

Recrear tu complejo sistema de proyección multiláser en el 3D visualiser probablemente sería, como mínimo, laborioso. Así que, en su lugar, tienes la opción de colocar tu Canvas dentro del espacio 3D. Activa la casilla _Show canvas_ en el panel _3D visualiser settings_. (Cualquier imagen guía que tengas en el Canvas también aparecerá en el visualiser).

{% hint style="info" %}
Ten en cuenta que el visualiser seguirá mostrando las proyecciones del Canvas como efectos atmosféricos procedentes de los láseres. Puedes simplemente apartarlos de la vista o, si quieres ir un paso más allá, alinearlos con el Canvas.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>¡Puede ser extremadamente satisfactorio alinear los haces del láser con la imagen del Canvas en el 3D visualiser!</p></figcaption></figure>
