---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Cambio colore

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Cambio colore

Descrizione

* **hue, saturation, brightness** - i valori del colore, vedi [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - la tonalità non viene modificata
  * FIXED - la tonalità degli elementi viene impostata sul valore di hue
  * SHIFT - la tonalità degli elementi viene spostata del valore indicato, quindi elementi di colori diversi resteranno diversi, ma verranno semplicemente spostati lungo il valore di tonalità.
* **saturation mode** -
  * OFF - la saturazione non viene modificata
  * FIXED - la saturazione viene fissata al valore specificato.
* **brightness mode** -
  * OFF - la luminosità non viene modificata
  * FIXED - la luminosità degli elementi viene impostata sul valore di brightness
  * MULTIPLY - la luminosità degli elementi viene combinata con il valore di brightness, quindi se stanno lampeggiando continueranno a lampeggiare, ma solo fino alla luminosità specificata qui.
* **blend** - quanto viene applicato il modificatore di colore: 0% significa per niente, 100% completamente, e 50% è una combinazione tra il colore esistente e i nuovi valori.
