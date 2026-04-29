---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Modifikatori putanje

## &#x20;Dotter

Ovaj node zamjenjuje sadržaj linija i oblika ravnomjerno raspoređenim točkama (postojeće točke ostaju nepromijenjene).

* **Colour** – boja točaka. Zanemaruje se ako je uključeno _Inherit Colour_, pogledajte dolje. _Pogledajte i_ [Postavke boje i HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – udaljenost između točaka, mjerena u pikselima. Manje vrijednosti = više točaka, veće vrijednosti = manje točaka.
* **Offset** – pomiče početni položaj točaka kao postotak razmaka. Može se animirati (npr. sawtooth Oscillator Node) za stvaranje efekata „putujućih” točaka.
* **Keep Original** – ako je uključeno, izvorne linije/oblici ostaju zadržani, a točke se iscrtavaju preko njih.
* **Render Profile** – odabire kvalitetu renderiranja. _Pogledajte_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – automatski prilagođava razmak tako da se duljina putanje ravnomjerno dijeli.
* **Fade Out Ends** – postupno smanjuje svjetlinu točaka prema početku i kraju putanje. Korisno pri animiranju **Offset** pomoću sawtooth Oscillator Node, kako bi se točke glatko pojavljivale/nestajale dok se pomiču prema kraju oblika.

## &#x20;Trimmer

Ovaj node skraćuje vidljivu duljinu linija i oblika, tako da ih možete postupno otkrivati, skrivati ili animirati kroz vrijeme.

* **Offset** – određuje gdje počinje vidljivi dio oblika. Čak i kada je _Trim Size_ na 0%, animiranje Offset od 0% → 100% čini da se oblik iscrta, postane potpuno vidljiv na 50%, a zatim ponovno nestane.
* **Trim Size** – određuje koliki se dio oblika zadržava, kao postotak njegove ukupne duljine.
* **Loop** – tretira oblik kao neprekinutu petlju, tako da se kraj spaja natrag na početak umjesto da nestane.
* **All Shapes** – kombinira sve ulazne oblike i skraćuje ih kao da su jedna putanja. Ako je isključeno, svaki se oblik skraćuje pojedinačno.
* **Add Dot at Start / Add Dot at End** – dodaje točku odabrane boje na mjestima skraćivanja. (Ako skraćivanje nije primijenjeno, točke se ne dodaju.)
* **Colour** – boja točaka skraćivanja. _Pogledajte i_ [Postavke boje i HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – odabire render profile za točke. _Pogledajte_ [Render Profile](../fundamentals/render-profile.md)
