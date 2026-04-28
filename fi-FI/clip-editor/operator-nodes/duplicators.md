---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Luo kaikesta sisällöstä peilikuvakopion. Oletuksena peilausakseli on pystysuora viiva keskellä.

* **angle** - peilausakselin kulma.
* **offset position** - siirtää peilausakselia (kohtisuoraan akseliin nähden)
* **delay** - peilatun sisällön aikaviive. Huomaa, että tällä on vaikutusta vain, jos sisällössä on jonkinlaista animaatiota.

#### 3D-asetukset (käytettävissä, kun 3D on valittuna)

* **angle X / angle Y** - peilausakselista tulee taso, ja näillä asetuksilla voit kiertää tasoa 3D-tilassa.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Monistaa sisällön ympyräkuvioksi.

* **radius** - etäisyys keskipisteestä, johon sisältö siirretään ennen kiertoa.
* **count** - luotavien objektikopioiden määrä.
* **use each objects pivot point** - kun tämä on valittuna, jokainen elementti siirretään ja kierretään oman keskipisteensä ympäri. (Vaikuttaa vain, kun monistettavia elementtejä on useita)
* **delay** - lisää jokaiseen monistettuun elementtiin asteittain kasvavan aikaviiveen. Huomaa, että sisällössä täytyy olla jonkinlaista animaatiota, jotta vaikutus näkyy selvästi.
* **rotation** - elementteihin lisättävä kierron siirtymä.

#### 3D-asetukset (käytettävissä, kun 3D on valittuna)

* **rotation x / rotation y** - kiertää koko ympyräkuviota x- ja y-akselien ympäri.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Monistaa sisällön ruudukoksi, jossa on rivejä ja sarakkeita.

* **spacing** - elementtien välinen etäisyys
* **count X**- kopioiden määrä vaakasuunnassa (sarakkeet)
* **count Y**- kopioiden määrä pystysuunnassa (rivit)
* **horizontal alignment** - sarakkeiden aloituskohta, LEFT, CENTRE tai RIGHT
* **vertical alignment** - rivien aloituskohta, TOP, MIDDLE tai BOTTOM
* **delay** - lisää jokaiseen monistettuun elementtiin asteittain kasvavan aikaviiveen. Huomaa, että sisällössä täytyy olla jonkinlaista animaatiota, jotta vaikutus näkyy selvästi.
