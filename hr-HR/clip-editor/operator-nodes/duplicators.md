---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Stvara zrcaljenu kopiju cijelog sadržaja. Prema zadanim postavkama os zrcaljenja je okomita linija u sredini.

* **angle** - kut linije osi zrcaljenja.
* **offset position** - pomiče os zrcaljenja (pomak je okomit na os)
* **delay** - vremensko kašnjenje zrcaljenog sadržaja. Imajte na umu da će ovo imati učinka samo ako sadržaj ima neku vrstu animacije.

#### 3D opcije (dostupno kada je odabrano 3D)

* **angle X / angle Y** - os zrcaljenja postaje ravnina, a ovim postavkama možete rotirati ravninu u 3D prostoru.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplicira sadržaj u kružnom uzorku.

* **radius** - udaljenost od središnje točke za koju se sadržaj pomiče prije rotacije.
* **count** - broj kopija objekta koje će se izraditi.
* **use each objects pivot point** - kada je odabrano, svaki će se element pomaknuti i rotirati oko vlastite središnje točke. (Ima učinka samo kada se duplicira više elemenata)
* **delay** - dodaje postupno sve dulje vremensko kašnjenje svakom dupliciranom elementu. Imajte na umu da sadržaj mora imati neku vrstu animacije kako bi učinak bio primjetan.
* **rotation** - dodatna rotacija koja se primjenjuje na elemente.

#### 3D opcije (dostupno kada je odabrano 3D)

* **rotation x / rotation y** - rotira cijeli kružni uzorak oko osi x i y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplicira sadržaj u rešetkastom uzorku redaka i stupaca.

* **spacing** - udaljenost između elemenata
* **count X**- broj kopija vodoravno (stupci)
* **count Y**- broj kopija okomito (redci)
* **horizontal alignment** - početna točka stupaca, LEFT, CENTRE ili RIGHT
* **vertical alignment** - početna točka redaka, TOP, MIDDLE ili BOTTOM
* **delay** - dodaje postupno sve dulje vremensko kašnjenje svakom dupliciranom elementu. Imajte na umu da sadržaj mora imati neku vrstu animacije kako bi učinak bio primjetan.
