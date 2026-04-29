---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Calibración de color

La calibración de color garantiza que los láseres rojo, verde y azul de tu proyector emitan luz de forma suave y predecible en todos los niveles de brillo. Cada proyector puede tener curvas de brillo no lineales; por ejemplo, un rojo al 50% puede verse mucho más brillante o más tenue que la mitad de la intensidad de un rojo al 100%. La calibración corrige esto para que los colores se mezclen bien, los degradados se vean suaves y los blancos queden equilibrados.

#### Calentar el proyector

Los diodos láser cambian su comportamiento a medida que se calientan. Deja siempre que el proyector se estabilice antes de calibrarlo:

* Proyecta un frame brillante, como el **White rectangle test pattern (11)**, durante al menos **15–20 minutos**.
* Así te aseguras de que el balance de color que ajustes se mantenga constante durante un show.

#### Cómo funciona la prueba de calibración

Usa los patrones de prueba para la calibración (consulta [Patrones de prueba](../output-view/test-patterns.md "mention"))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Cada uno muestra cuatro líneas en movimiento:

* **Línea superior** – 100% de brillo a velocidad completa
* **Segunda línea** – 75% de brillo al 75% de velocidad
* **Tercera línea** – 50% de brillo al 50% de velocidad
* **Cuarta línea** – 25% de brillo al 25% de velocidad

Como se escalan a la vez el brillo _y la velocidad_, todas las líneas deberían verse con el mismo brillo. Si alguna se ve más clara o más oscura, ajusta el deslizador correspondiente hasta que coincidan.

Cada patrón de prueba también tiene una quinta línea al **0% de brillo**, que no debería ser visible. Sirve para corregir láseres que no emiten luz en niveles muy bajos. Si tu láser sigue sin verse con un brillo bajo, aumenta gradualmente el **ajuste de 0%** hasta que la línea sea apenas visible y, después, bájalo un poco hasta que vuelva a desaparecer. El objetivo es encontrar el umbral en el que el láser empieza a encenderse y quedarse justo por debajo, para que los fundidos empiecen de forma natural sin recortar la parte inferior del rango.

#### Usar el panel Colour Calibration

El panel te ofrece controles independientes para cada canal (rojo, verde y azul) en los niveles 100, 75, 50, 25 y 0%.

1. **Selecciona un patrón de prueba** (empieza por el rojo).
2. **Ajusta los deslizadores** para que las líneas de 100, 75, 50 y 25% se vean con el mismo brillo.
3. **Ajusta ligeramente el deslizador de 0%** si la línea “apagada” sigue siendo visible de forma tenue.
4. **Repite el proceso con el verde y el azul.**
5. Cambia al **White test pattern (8)**. Las cuatro líneas deberían verse iguales y el blanco debería parecer neutro, sin dominantes de color.

#### Ajustar el balance de blancos

También puedes usar este sistema para ajustar el **balance de blancos**. Después de calibrar cada canal por separado, cambia al **White test pattern (8)**. Si la salida se ve con una dominante de color (por ejemplo, demasiado verde o demasiado azul), ajusta los niveles relativos de los canales rojo, verde y azul hasta que las líneas se vean de un blanco neutro. Aunque tus láseres tengan potencias bastante descompensadas, la calibración ayudará a acercarlos entre sí y a conseguir una mezcla de colores más limpia y equilibrada.

#### Guardar la calibración

* Usa **Store** para sobrescribir el preset actual.
* Usa **Store As** para crear un preset nuevo, útil si trabajas con varios láseres.
