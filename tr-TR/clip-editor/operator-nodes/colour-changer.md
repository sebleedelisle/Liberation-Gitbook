---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Renk değiştirme

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Renk değiştirme

Açıklama

* **hue, saturation, brightness** - renk değerleri; bkz. [Renk ayarları ve HSB](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - renk tonu değiştirilmez
  * FIXED - öğelerin renk tonu, hue değerine ayarlanır
  * SHIFT - öğelerin renk tonu bu değer kadar kaydırılır; böylece farklı renkteki öğeler farklı kalır, yalnızca renk tonu ekseninde kayar.
* **saturation mode** -
  * OFF - doygunluk değiştirilmez
  * FIXED - doygunluk belirtilen değere sabitlenir.
* **brightness mode** -
  * OFF - parlaklık değiştirilmez
  * FIXED - öğelerin parlaklığı brightness değerine ayarlanır
  * MULTIPLY - öğelerin parlaklığı brightness değeriyle ölçeklenir; yani yanıp sönüyorlarsa yine yanıp sönerler, ancak yalnızca burada belirtilen parlaklık seviyesine kadar çıkarlar.
* **blend** - renk değiştirmenin ne kadar güçlü uygulanacağını belirler. 0% hiç uygulanmaz, 100% tamamen uygulanır, 50% ise mevcut renk ile yeni değerlerin birleşimidir.
