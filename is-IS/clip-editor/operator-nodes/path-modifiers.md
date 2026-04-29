---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Breytingar á slóðum

## &#x20;Dotter

Þessi node skiptir út línum og formum fyrir jafndreifða punkta (punktar sem eru þegar til staðar breytast ekki).

* **Colour** – litur punktanna. Hunsað ef _Inherit Colour_ er virkt, sjá hér að neðan. _Sjá einnig_ [litastillingar og HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – fjarlægðin milli punkta, mæld í pixlum. Lægri gildi = fleiri punktar, hærri gildi = færri punktar.
* **Offset** – færir upphafsstöðu punktanna sem prósentu af bilinu. Hægt er að hreyfa þetta með animation, t.d. með Oscillator Node sem notar sagtannarbylgju, til að búa til punktaáhrif sem „ferðast“ eftir forminu.
* **Keep Original** – ef þetta er virkt eru upprunalegu línurnar/formin varðveitt og punktarnir teiknaðir ofan á.
* **Render Profile** – velur gæði rendering. _Sjá_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – stillir bilið sjálfkrafa þannig að lengd slóðarinnar skiptist jafnt.
* **Fade Out Ends** – dregur smám saman úr birtu punktanna við upphaf og enda slóðarinnar. Gagnlegt þegar **Offset** er hreyft með Oscillator Node sem notar sagtannarbylgju, svo punktarnir dofni mjúklega inn/út þegar þeir færast að enda formsins.

## &#x20;Trimmer

Þessi node klippir sýnilega lengd lína og forma, þannig að þú getur látið þau birtast, falið þau eða hreyft þau með tímanum.

* **Offset** – stýrir hvar sýnilegi hluti formsins byrjar. Jafnvel þótt _Trim Size_ sé 0% lætur animation á Offset frá 0% → 100% formið teiknast inn, verða alveg sýnilegt við 50% og hverfa svo aftur.
* **Trim Size** – stillir hversu stórum hluta formsins er haldið, sem prósentu af heildarlengd þess.
* **Loop** – meðhöndlar formið sem samfellda lykkju, þannig að endinn tengist aftur við upphafið í stað þess að hverfa.
* **All Shapes** – sameinar öll input form og klippir þau eins og þau væru ein slóð. Ef þetta er óvirkt er hvert form klippt sérstaklega.
* **Add Dot at Start / Add Dot at End** – bætir við punkti í völdum lit á klippipunktunum. (Ef engin klipping er notuð er engum punktum bætt við.)
* **Colour** – litur klippipunktanna. _Sjá einnig_ [litastillingar og HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – velur render profile fyrir punktana. _Sjá_ [Render Profile](../fundamentals/render-profile.md)
