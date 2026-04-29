---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Описание

* **hue, saturation, brightness** — значения цвета, см. [Настройки цвета и HSB](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** —
  * OFF — тон не изменяется
  * FIXED — тон элементов устанавливается на значение hue
  * SHIFT — тон элементов смещается на указанное значение, поэтому элементы разных цветов останутся разными, но будут сдвинуты по шкале тона.
* **saturation mode** —
  * OFF — насыщенность не изменяется
  * FIXED — насыщенность фиксируется на указанном значении.
* **brightness mode** —
  * OFF — яркость не изменяется
  * FIXED — яркость элементов устанавливается на значение brightness
  * MULTIPLY — яркость элементов комбинируется со значением brightness, поэтому если они мигают, они продолжат мигать, но только до яркости, указанной здесь.
* **blend** — насколько сильно применяется Colour change: 0% — совсем не применяется, 100% — применяется полностью, а 50% — это сочетание существующего цвета и новых значений.
