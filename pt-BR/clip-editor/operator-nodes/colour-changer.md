---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Descrição

* **hue, saturation, brightness** - os valores de cor; consulte [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - o matiz não é alterado
  * FIXED - o matiz dos elementos é definido pelo valor de hue
  * SHIFT - o matiz dos elementos é deslocado pelo valor definido; assim, elementos de cores diferentes continuam diferentes, mas são apenas deslocados ao longo do valor de matiz.
* **saturation mode** -
  * OFF - a saturação não é alterada
  * FIXED - a saturação é fixada no valor especificado.
* **brightness mode** -
  * OFF - o brilho não é alterado
  * FIXED - o brilho dos elementos é definido pelo valor de brightness
  * MULTIPLY - o brilho dos elementos é combinado com o valor de brightness; assim, se eles estiverem piscando, continuarão piscando, mas somente até o brilho especificado aqui.
* **blend** - define com que intensidade o Colour change é aplicado: 0% significa nenhuma aplicação, 100% significa aplicação total, e 50% é uma combinação da cor existente com os novos valores.
