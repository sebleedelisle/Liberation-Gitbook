---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicadores

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Crea un duplicado reflejado de todo el contenido. De forma predeterminada, el eje de simetría es una línea vertical en el centro.

* **angle** - el ángulo de la línea del eje de simetría.
* **offset position** - desplaza el eje de simetría (lo mueve perpendicularmente al eje).
* **delay** - retardo temporal del contenido reflejado. Ten en cuenta que solo tendrá efecto si el contenido tiene algún tipo de animación.

#### Opciones 3D (disponibles cuando 3D está seleccionado)

* **angle X / angle Y** - el eje de simetría pasa a ser un plano y puedes usar estos ajustes para rotarlo en 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplica el contenido en un patrón circular.

* **radius** - la distancia desde el punto central a la que se desplaza el contenido antes de rotarlo.
* **count** - el número de copias del objeto que se crearán.
* **use each objects pivot point** - cuando está seleccionado, cada elemento se desplazará y rotará alrededor de su propio punto central. (Solo tiene efecto cuando se duplican varios elementos)
* **delay** - añade un retardo temporal progresivamente mayor a cada elemento duplicado. Ten en cuenta que el contenido debe tener algún tipo de animación para que esto produzca un efecto visible.
* **rotation** - una rotación de desplazamiento añadida a los elementos.

#### Opciones 3D (disponibles cuando 3D está seleccionado)

* **rotation x / rotation y** - rota todo el patrón circular alrededor de los ejes x e y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplica el contenido en un patrón de cuadrícula con filas y columnas.

* **spacing** - la distancia entre los elementos.
* **count X**- el número de copias en horizontal (columnas).
* **count Y**- el número de copias en vertical (filas).
* **horizontal alignment** - el punto inicial de las columnas: LEFT, CENTRE o RIGHT.
* **vertical alignment** - el punto inicial de las filas: TOP, MIDDLE o BOTTOM.
* **delay** - añade un retardo temporal progresivamente mayor a cada elemento duplicado. Ten en cuenta que el contenido debe tener algún tipo de animación para que esto produzca un efecto visible.
