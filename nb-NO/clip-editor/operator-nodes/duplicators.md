---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Lager en speilvendt duplikat av alt innholdet. Som standard er speilaksen en vertikal linje i midten.

* **angle** - vinkelen på linjen for speilaksen.
* **offset position** - forskyver speilaksen (flytter den vinkelrett på aksen)
* **delay** - tidsforsinkelse for det speilvendte innholdet. Merk at dette bare har effekt hvis innholdet har en form for animasjon.

#### 3D-alternativer (tilgjengelig når 3D er valgt)

* **angle X / angle Y** - speilaksen blir et plan, og du kan bruke disse innstillingene til å rotere planet i 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Dupliserer innhold i et sirkulært mønster.

* **radius** - avstanden fra midtpunktet som innholdet forskyves før det roteres.
* **count** - antall kopier som skal lages av objektet.
* **use each objects pivot point** - når dette er valgt, forskyves og roteres hvert element rundt sitt eget midtpunkt. (Har bare effekt når flere elementer dupliseres)
* **delay** - legger til en gradvis lengre tidsforsinkelse for hvert dupliserte element. Merk at innholdet må ha en form for animasjon for at dette skal gi en merkbar effekt.
* **rotation** - en forskjøvet rotasjon som legges til elementene.

#### 3D-alternativer (tilgjengelig når 3D er valgt)

* **rotation x / rotation y** - roterer hele det sirkulære mønsteret rundt x- og y-aksene.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Dupliserer innhold i et rutenettmønster med rader og kolonner.

* **spacing** - avstanden mellom elementene
* **count X**- antall kopier horisontalt (kolonner)
* **count Y**- antall kopier vertikalt (rader)
* **horizontal alignment** - startpunktet for kolonnene, LEFT, CENTRE eller RIGHT
* **vertical alignment** - startpunktet for radene, TOP, MIDDLE eller BOTTOM
* **delay** - legger til en gradvis lengre tidsforsinkelse for hvert dupliserte element. Merk at innholdet må ha en form for animasjon for at dette skal gi en merkbar effekt.
