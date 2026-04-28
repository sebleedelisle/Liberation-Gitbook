---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Opretter en spejlet kopi af alt indholdet. Som standard er spejlaksen en lodret linje i midten.

* **angle** - vinklen på spejlaksens linje.
* **offset position** - forskyder spejlaksen (flytter den vinkelret på aksen)
* **delay** - tidsforsinkelse for det spejlede indhold. Bemærk, at dette kun har en effekt, hvis indholdet har en form for animation.

#### 3D-indstillinger (tilgængelige, når 3D er valgt)

* **angle X / angle Y** - spejlaksen bliver til et plan, og du kan bruge disse indstillinger til at rotere planet i 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplikerer indhold i et cirkulært mønster.

* **radius** - afstanden fra midtpunktet, som indholdet forskydes, før det roteres.
* **count** - antallet af kopier af objektet, der skal oprettes.
* **use each objects pivot point** - når dette er valgt, forskydes og roteres hvert element omkring sit eget midtpunkt. (Har kun effekt, når flere elementer duplikeres)
* **delay** - tilføjer en gradvist længere tidsforsinkelse til hvert duplikeret element. Bemærk, at indholdet skal have en form for animation, før dette har en synlig effekt.
* **rotation** - en offset-rotation, der føjes til elementerne.

#### 3D-indstillinger (tilgængelige, når 3D er valgt)

* **rotation x / rotation y** - roterer hele det cirkulære mønster omkring x- og y-akserne.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplikerer indhold i et gittermønster med rækker og kolonner.

* **spacing** - afstanden mellem elementerne
* **count X**- antallet af kopier vandret (kolonner)
* **count Y**- antallet af kopier lodret (rækker)
* **horizontal alignment** - startpunktet for kolonnerne, LEFT, CENTRE eller RIGHT
* **vertical alignment** - startpunktet for rækkerne, TOP, MIDDLE eller BOTTOM
* **delay** - tilføjer en gradvist længere tidsforsinkelse til hvert duplikeret element. Bemærk, at indholdet skal have en form for animation, før dette har en synlig effekt.
