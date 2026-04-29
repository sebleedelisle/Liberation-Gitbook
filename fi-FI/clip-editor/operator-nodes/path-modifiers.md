---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Tämä solmu korvaa viivojen ja muotojen sisällön tasavälein sijoitetuilla pisteillä (olemassa olevat pisteet pysyvät ennallaan).

* **Colour** – pisteiden väri. Ohitetaan, jos _Inherit Colour_ on käytössä, katso alla. _Katso myös_ [Väriasetukset ja HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – pisteiden välinen etäisyys pikseleinä. Pienemmät arvot = enemmän pisteitä, suuremmat arvot = vähemmän.
* **Offset** – siirtää pisteiden aloituskohtaa prosenttiosuutena pistevälistä. Voidaan animoida (esim. sahahammasmuotoisella Oscillator Node -solmulla) liikkuvien piste-efektien luomiseksi.
* **Keep Original** – jos käytössä, alkuperäiset viivat/muodot säilytetään ja pisteet piirretään niiden päälle.
* **Render Profile** – valitsee renderöinnin laadun. _Katso_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – säätää pisteväliä automaattisesti niin, että polun pituus jakautuu tasan.
* **Fade Out Ends** – vähentää pisteiden kirkkautta asteittain polun alku- ja loppupäätä kohti. Hyödyllinen, kun **Offset** animoidaan sahahammasmuotoisella Oscillator Node -solmulla, jolloin pisteet häipyvät pehmeästi sisään/ulos liikkuessaan muodon loppuun.

## &#x20;Trimmer

Tämä solmu rajaa viivojen ja muotojen näkyvää pituutta, jolloin voit paljastaa, piilottaa tai animoida niitä ajan kuluessa.

* **Offset** – määrittää, mistä kohdasta muodon näkyvä osa alkaa. Vaikka _Trim Size_ olisi 0 %, Offset-arvon animointi välillä 0 % → 100 % saa muodon piirtymään esiin, näkymään kokonaan 50 % kohdalla ja katoamaan sitten uudelleen.
* **Trim Size** – määrittää, kuinka suuri osa muodosta säilytetään, prosenttiosuutena sen kokonaispituudesta.
* **Loop** – käsittelee muotoa jatkuvana silmukkana, jolloin loppu yhdistyy takaisin alkuun katoamisen sijaan.
* **All Shapes** – yhdistää kaikki syötemuodot ja rajaa ne kuin ne olisivat yksi polku. Jos asetus ei ole käytössä, jokainen muoto rajataan erikseen.
* **Add Dot at Start / Add Dot at End** – lisää valitun värisen pisteen rajauskohtiin. (Jos rajausta ei käytetä, pisteitä ei lisätä.)
* **Colour** – rajauspisteiden väri. _Katso myös_ [Väriasetukset ja HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – valitsee pisteiden renderöintiprofiilin. _Katso_ [Render Profile](../fundamentals/render-profile.md)
