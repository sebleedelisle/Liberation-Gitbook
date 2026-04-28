---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Það er _Render Profile_ stilling í hverjum _Creator_ hnút og hún ákvarðar hvernig formin eru teiknuð (eða _rendered_) með leysunum.

**Fyrir flesta notkun hentar stillingin** _**DEFAULT**_ **fullkomlega**. En ef þú ert að vinna með grafík eða flókið efni gætirðu viljað hafa meiri stjórn á því hvernig hvert form er renderað.

{% hint style="info" %}
Ólíkt flestum leysihugbúnaði býr Liberation til punktastraum í rauntíma, rétt áður en hann er sendur til leysistýringanna. Þetta sparar mikið diskpláss; Clip eru aðeins nokkur kB í stað MB af forrenderuðum punktastraumum.

Það þýðir líka að þú getur fínstillt sama efni fyrir mismunandi skannagerðir, fyrir hvern leysi fyrir sig, án þess að þurfa að breyta Clip sjálfum.

Nánari upplýsingar eru í [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Það eru þrjú forstillt _Render Profiles_: _DEFAULT_, _FAST_ og _DETAIL._

_**DEFAULT**_ - góð almenn stilling sem hentar best fyrir flest

_**FAST** -_ ef Clip inniheldur mikið efni og hluti þess er bara mjög einfaldir punktar og beinar línur geturðu fengið minna flökt með því að velja þennan valkost.

_**DETAIL**_ - notaðu þennan valkost ef þú ert að teikna eitthvað sem þarf skörp horn. Hafðu þó í huga að skannarnir hreyfast hægar, sem getur valdið flökti í úttakinu.

{% hint style="info" %}
Í Clip editor geturðu úthlutað creators á mismunandi render profiles, en hver leysir vinnur úr þessum profiles eftir eigin skannastillingum. Sjá [scanner-presets.md](../../advanced/scanner-presets.md)
{% endhint %}
