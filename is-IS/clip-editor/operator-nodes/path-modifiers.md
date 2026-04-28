---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Path Modifiers

## &#x20;Dotter

Þessi hnútur skiptir línum og formum út fyrir punkta með jöfnu millibili (punktar sem eru þegar til staðar breytast ekki).

* **Colour** – litur punktanna. Þetta er hunsað ef _Inherit Colour_ er virkt, sjá hér að neðan. _Sjá einnig_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – fjarlægðin á milli punkta, mæld í pixlum. Lægri gildi = fleiri punktar, hærri gildi = færri.
* **Offset** – hliðrar upphafsstað punktanna sem hlutfalli af bilinu. Hægt er að hreyfistýra þessu (t.d. með sawtooth Oscillator Node) til að búa til punkta sem „ferðast“ eftir forminu.
* **Keep Original** – ef þetta er virkt eru upprunalegu línurnar/formin varðveitt og punktarnir teiknaðir ofan á.
* **Render Profile** – velur myndgæði við teiknun. _Sjá_ [render-profile.md](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – stillir bilið sjálfkrafa þannig að lengd ferilsins deilist jafnt.
* **Fade Out Ends** – dregur smám saman úr birtu punktanna í átt að upphafi og enda ferilsins. Þetta er gagnlegt þegar **Offset** er hreyfistýrt með sawtooth Oscillator Node, þannig að punktarnir dofni mjúklega inn/út þegar þeir færast að enda formsins.

## &#x20;Trimmer

Þessi hnútur klippir sýnilega lengd lína og forma, svo þú getir látið þau birtast, hverfa eða hreyfistýrt þeim yfir tíma.

* **Offset** – stýrir hvar sýnilegi hluti formsins byrjar. Jafnvel þegar _Trim Size_ er 0% lætur hreyfistýring á Offset frá 0% → 100% formið teiknast inn, verða alveg sýnilegt við 50% og hverfa svo aftur.
* **Trim Size** – stillir hversu stórum hluta formsins er haldið eftir, sem prósentu af heildarlengd þess.
* **Loop** – meðhöndlar formið sem samfellda lykkju, þannig að endinn tengist aftur við byrjunina í stað þess að hverfa.
* **All Shapes** – sameinar öll inntaksform og klippir þau eins og þau væru einn ferill. Ef slökkt er á þessu er hvert form klippt sérstaklega.
* **Add Dot at Start / Add Dot at End** – bætir við punkti í völdum lit á klippipunktunum. (Ef engin klipping er notuð er engum punktum bætt við.)
* **Colour** – litur klippipunktanna. _Sjá einnig_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – velur render profile fyrir punktana. _Sjá_ [render-profile.md](../fundamentals/render-profile.md)
