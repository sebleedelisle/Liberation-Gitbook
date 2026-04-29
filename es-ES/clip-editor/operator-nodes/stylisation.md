---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Nodos de Stylisation

## &#x20;Randomise

Crea copias dispersas de los elementos de entrada usando un campo de ruido coherente. Dicho de otro modo, copia y desplaza tus formas y puntos de una manera controlada y “ruidosa”. En lugar de tenerlo todo colocado ordenadamente en un solo sitio, obtienes varias versiones que se desplazan y se reparten, como partículas moviéndose en un flujo.

* **count** – número de copias por cada elemento de entrada (1–20). Con 1, obtienes una única versión con ligera variación de cada elemento. Los valores más altos crean varias copias dispersas.
* **noise offset** – recorre el campo de ruido (0–100%). Hace un bucle sin cortes, así que si lo animas con un Oscillator Node obtendrás un movimiento suave y continuo de todas las copias a la vez.
* **noise jitter** – controla la escala de textura del ruido. Los valores bajos producen variaciones amplias y suaves. Los valores altos generan colocaciones más cerradas y erráticas. Esto cambia el patrón, no la intensidad.
* **change between points** – controla cuánto se diferencia cada copia de la anterior. Los valores bajos mantienen las copias agrupadas y parecidas. Los valores altos las separan más y añaden mayor variación.
* **face direction** – rota cada copia para que mire en la dirección de desplazamiento dentro del campo de ruido, creando flechas/partículas alineadas con el flujo.
* **amount** – intensidad global del efecto (0–100%). Escala tanto el desplazamiento como la rotación de Face direction.

{% hint style="info" %}
¡El nodo randomise es la base del efecto Randomise!
{% endhint %}

## &#x20;Trails

Crea ecos de tu contenido, dejando copias que se desvanecen o cambian de escala detrás del original a medida que se mueve.

* **change render profile for trail** – si está activado, todas las copias del rastro usan el **render profile** seleccionado. _Consulta_ [Render profile](../fundamentals/render-profile.md "mention").
* **render profile** – perfil que se usa para las copias del rastro cuando el interruptor anterior está activado. Se suele usar cuando el contenido principal está configurado en **DETAIL**, pero los ecos se renderizan como **FAST**; así mantienes buen detalle en las formas principales y renderizas los rastros de forma más eficiente.
* **delay** – define el espaciado entre copias del rastro en tiempo musical, medido en **pasos de 1/64 de nota**.\
  Como referencia:
  * 16 = 1/16 de compás (semicorchea)
  * 32 = 1/8 de compás (corchea)
  * 64 = 1/4 de compás (negra)
  * 128 = 1/2 compás (blanca)
  * 256 = 1 compás
* **trail size** – cuántas copias de rastro se dibujan detrás del contenido en vivo.
* **freeze trails** – convierte rastros de movimiento fluido en una secuencia de instantáneas congeladas. Útil para crear efectos de rastro staccato sincronizados al ritmo.
* **brightness start / brightness end** – aplica brillo a lo largo del rastro, desde la copia más reciente (**start**) hasta la más antigua (**end**). Normalmente, si ajustas **brightness start** al 100% y **brightness end** al 0%, los ecos se desvanecerán.
* **scale start / scale end** – aplica escala a lo largo del rastro, desde la copia más reciente (start) hasta la más antigua (end). Para rastros que se encogen hasta desaparecer, ajusta **scale start** al 100% y **scale end** al 0%.

## &#x20;Shimmer

Añade una variación de brillo parpadeante a tu contenido, desde un destello suave hasta un estroboscopio intenso.

* **speed** – rapidez con la que cambia el shimmer con el tiempo. Los valores más altos parpadean más rápido; 0 pausa el efecto.
* **separation** – cuánto se diferencian entre sí los puntos/elementos vecinos.
  * 0: todo parpadea a la vez.
  * \>0: los puntos cercanos reciben fases progresivamente distintas, así que el shimmer varía a lo largo de la forma.
  * <0: igual que lo anterior, pero la progresión de fase va en sentido contrario.
* **threshold** – en lugar de desvanecerse suavemente, los puntos se encienden o se apagan por completo según su brillo. Los elementos más brillantes se iluminan con más frecuencia, pero ten en cuenta que los elementos al 100% de brillo están siempre encendidos, mientras que los elementos al 0% están siempre apagados. Útil para efectos de purpurina nítida o luz de estrellas.

{% hint style="info" %}
Activar **threshold** es una de esas funciones ocultas excelentes que pueden dar mucha vida a tus partículas o a tu contenido. En lugar de desvanecerse, los puntos se encienden y apagan rápidamente según su brillo. Como se dibujan menos puntos en cada momento, el resultado es una salida más brillante y una animación más suave.

Pero ten en cuenta que, si tu contenido ya está al 100% de brillo, ¡no hará nada!
{% endhint %}

* **use whole shape** – aplica un único valor de shimmer de forma uniforme a toda la forma. Cuando está desactivado, el nodo subdivide las formas para que distintas partes puedan parpadear de manera independiente y crear un aspecto moteado.

## &#x20;Particles

Este es un efecto experimental que genera y anima partículas a partir de tu contenido. Cualquier elemento basado en puntos que entre se tratará como posición de emisor. Como las trayectorias de las partículas se precalculan, si cambia el contenido de entrada puede que tengas que actualizar/recalcular para actualizar las partículas (basta con cambiar cualquiera de los ajustes).

**General**

* **keep original** – si está activado, se conserva el contenido original y las partículas se añaden por encima. Útil cuando quieres que los puntos emisores sigan siendo visibles.
* **number of particles** – cuántas partículas se crean por emisión. Los valores más altos producen efectos más densos; los valores más bajos, resultados más minimalistas.
* **emission period** – duración del bucle (en compases) durante la cual se emiten partículas. Al 100% se reparten uniformemente por el bucle; los valores más pequeños las agrupan para crear ráfagas.
* **loop length** – cuánto dura el bucle de partículas, medido en compases musicales.
* **loop count** – cuántas veces se repite el bucle antes de reiniciarse. Si se ajusta a 1, las partículas seguirán siempre exactamente la misma simulación cada vez, por lo que será perfectamente repetible. Los valores más altos introducen más variación antes de que el ciclo se reinicie.
* **delay** – desplaza el inicio de la emisión un número de notas de 1/64, para crear efectos de temporización.

**Motion**

* **speed** – rapidez con la que las partículas se alejan del emisor.
* **speed variation** – añade aleatoriedad para que las partículas no se muevan todas a la misma velocidad. Crea una dispersión más natural.
* **direction** – define la dirección base en la que se disparan las partículas, mediante **ángulos x, y, z**. Estos ángulos rotan el vector de disparo en el espacio 3D, de modo que puedes orientar las partículas hacia arriba, hacia los lados o en cualquier diagonal. Combínalo con **spread** para crear conos más amplios o ráfagas más caóticas.

{% hint style="info" %}
**Ángulos de Euler**\
Liberation usa **ángulos de Euler** para describir la orientación en el espacio 3D. Son simplemente rotaciones alrededor de los tres ejes principales:

* **X** – inclinación hacia delante/atrás (como asentir con la cabeza)
* **Y** – giro izquierda/derecha (como negar con la cabeza)
* **Z** – rotación en sentido horario/antihorario (como inclinar la cabeza hacia un lado)

Ajustando estos tres valores puedes apuntar las partículas en cualquier dirección.
{% endhint %}

* **direction variation** – añade dispersión aleatoria alrededor de esa dirección. Útil para crear conos, chorros o explosiones.
* **drag** – ralentiza las partículas con el tiempo. Los valores más altos hacen que parezcan más pesadas y lentas.
* **gravity** – atrae las partículas hacia abajo (positivo) o las empuja hacia arriba (negativo).
* **gravity variation** – añade variación a la gravedad por partícula, haciendo que el movimiento sea más caótico.

**Life**

* **life duration** – cuánto tiempo existen las partículas (medido en unidades de nota de 1/64). Con valores más cortos, las partículas desaparecen rápidamente; con valores más largos, permanecen visibles durante más tiempo.
* **life variation** – añade aleatoriedad a la duración de vida de las partículas para que no desaparezcan todas a la vez.
* **start delay / start delay variation** – retrasa el momento en que cada partícula se hace visible (en pasos de nota de 1/64). La partícula ya se ha generado y se está moviendo durante este periodo, pero su brillo se mantiene en 0, así que permanece invisible hasta que termina el retraso. Es útil si quieres que aparezcan “destellos” de fuegos artificiales con retraso.

**Colour & brightness**

* **hue start** – color inicial de las partículas.
* **hue variation** – añade aleatoriedad para que las partículas no empiecen todas con el mismo color.
* **hue change** – desplaza el tono a lo largo de la vida de la partícula, creando rastros que cambian de color.
* **brightness start / brightness end** – aplica brillo a lo largo de la vida de la partícula. Normalmente se ajusta brightness start alto y brightness end bajo para que se desvanezcan de forma natural.
* **brightness variation** – aleatoriza el brillo inicial para crear un aspecto más dinámico.
* **saturation start / saturation end** – define lo vivo que es el color al inicio y al final.
* **saturation variation** – aleatoriza la saturación para introducir variación entre partículas.

**Simulation**

* **time adjustment** – acelera o ralentiza toda la simulación de partículas. Útil para sincronizar con distintos tempos o exagerar el movimiento.
