---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformaciones

## &#x20;Translate

Mueve todo el contenido a lo largo de los ejes x, y y/o z. Ten en cuenta que el sistema de coordenadas está centrado y se extiende hasta +/-200 en los ejes x e y. Consulta [Sistema de coordenadas](../fundamentals/co-ordinate-system.md "mention").

* **x** - la distancia que se mueve en el eje x (izquierda - derecha).
* **y** - la distancia que se mueve en el eje y (arriba - abajo).

#### Opciones 3D (disponibles cuando 3D está seleccionado)

* **z** - la distancia que se mueve en el eje z (hacia atrás y hacia delante dentro de la pantalla).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Rota todo el contenido. Los valores están en grados. Consulta [Sistema de coordenadas](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - la cantidad de rotación del contenido en sentido horario, en grados. Todo se rota alrededor del origen (0,0), el centro.
* **pivot point x / pivot point y** - usa estos valores para desplazar el origen de la rotación.

#### Opciones 3D (disponibles cuando 3D está seleccionado)

* **rotation x** - rotación alrededor del eje x (pitch).
* **rotation y** - rotación alrededor del eje y (yaw).
* **pivot point z** - posición de desplazamiento de la rotación en el eje z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Escala todo el contenido.

* **scale** - el porcentaje de escala.
* **scale x / scale y** - si quieres escalar horizontal y/o verticalmente, usa estas opciones.

{% hint style="warning" %}
¡Cuando algo se escala al 0 % en cualquier eje, desaparece!
{% endhint %}
