---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Skapar en spegelvänd kopia av allt innehåll. Som standard är spegelaxeln en vertikal linje i mitten.

* **angle** - spegelaxelns vinkel.
* **offset position** - förskjuter spegelaxeln (flyttar den vinkelrätt mot axeln)
* **delay** - tidsfördröjning för det speglade innehållet. Observera att detta bara får effekt om innehållet har någon form av animation.

#### 3D-alternativ (tillgängliga när 3D är valt)

* **angle X / angle Y** - spegelaxeln blir ett plan och du kan använda dessa inställningar för att rotera planet i 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplicerar innehåll i ett cirkulärt mönster.

* **radius** - avståndet från mittpunkten som innehållet förskjuts innan det roteras.
* **count** - antalet kopior av objektet som ska skapas.
* **use each objects pivot point** - när detta är valt förskjuts och roteras varje element runt sin egen mittpunkt. (Har bara effekt när flera element dupliceras)
* **delay** - lägger till en successivt längre tidsfördröjning för varje duplicerat element. Observera att innehållet behöver ha någon form av animation för att detta ska ge en märkbar effekt.
* **rotation** - en extra rotationsförskjutning som läggs till på elementen.

#### 3D-alternativ (tillgängliga när 3D är valt)

* **rotation x / rotation y** - roterar hela det cirkulära mönstret runt x- och y-axlarna.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplicerar innehåll i ett rutnätsmönster med rader och kolumner.

* **spacing** - avståndet mellan elementen
* **count X**- antalet kopior horisontellt (kolumner)
* **count Y**- antalet kopior vertikalt (rader)
* **horizontal alignment** - startpunkten för kolumnerna, LEFT, CENTRE eller RIGHT
* **vertical alignment** - startpunkten för raderna, TOP, MIDDLE eller BOTTOM
* **delay** - lägger till en successivt längre tidsfördröjning för varje duplicerat element. Observera att innehållet behöver ha någon form av animation för att detta ska ge en märkbar effekt.
