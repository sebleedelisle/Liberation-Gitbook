---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Modificadores de trazado

## &#x20;Dotter

Este nodo sustituye el contenido de líneas y formas por puntos espaciados de manera uniforme (los puntos existentes no cambian).

* **Colour** – el color de los puntos. Se ignora si _Inherit Colour_ está activado; consulta más abajo. _Consulta también_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Spacing** – la distancia entre puntos, medida en píxeles. Valores más bajos = más puntos; valores más altos = menos.
* **Offset** – desplaza la posición inicial de los puntos como porcentaje del espaciado. Se puede animar (por ejemplo, con un Oscillator Node de diente de sierra) para crear efectos de puntos “en movimiento”.
* **Keep Original** – si está activado, se conservan las líneas/formas originales y los puntos se dibujan encima.
* **Render Profile** – elige la calidad de renderizado. _Consulta_ [render-profile.md](../fundamentals/render-profile.md "mention")
* **Length Auto Divisible by Spacing** – ajusta automáticamente el espaciado para que la longitud del trazado se divida de forma uniforme.
* **Fade Out Ends** – reduce gradualmente el brillo de los puntos hacia el inicio y el final del trazado. Es útil al animar **Offset** con un Oscillator Node de diente de sierra, para que los puntos aparezcan y desaparezcan suavemente al moverse hasta el final de la forma.

## &#x20;Trimmer

Este nodo recorta la longitud visible de líneas y formas, lo que te permite mostrarlas, ocultarlas o animarlas con el tiempo.

* **Offset** – controla dónde empieza la parte visible de la forma. Incluso con _Trim Size_ al 0 %, al animar Offset de 0 % → 100 %, la forma se dibuja, queda totalmente visible al 50 % y después vuelve a desaparecer.
* **Trim Size** – define qué parte de la forma se conserva, como porcentaje de su longitud total.
* **Loop** – trata la forma como un bucle continuo, de modo que el final se conecta de nuevo con el principio en lugar de desaparecer.
* **All Shapes** – combina todas las formas de entrada y las recorta como si fueran un único trazado. Si está desactivado, cada forma se recorta por separado.
* **Add Dot at Start / Add Dot at End** – añade un punto del color elegido en los puntos de recorte. (Si no se aplica ningún recorte, no se añaden puntos.)
* **Colour** – el color de los puntos de recorte. _Consulta también_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md "mention")
* **Render Profile** – elige el perfil de renderizado para los puntos. _Consulta_ [render-profile.md](../fundamentals/render-profile.md "mention")
