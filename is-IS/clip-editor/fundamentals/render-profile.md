---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

Hver _Creator_ node hefur stillinguna _Render Profile_, sem ákvarðar hvernig formin eru teiknuð (eða _renderuð)_ með leysunum.

**Fyrir flesta notkun hentar&#x20;**_**DEFAULT**_**&#x20;alveg ágætlega**. En ef þú ert að vinna með grafík eða flókið efni gætirðu viljað meiri stjórn á því hvernig hvert form er renderað.

{% hint style="info" %}
Ólíkt flestum laserhugbúnaði býr Liberation til punktastraum í rauntíma, rétt áður en hann er sendur til laser controller. Þetta sparar mikið diskpláss: hvert Clip er aðeins nokkur kB í stað MB af fyrirfram renderuðum punktastraumum.

Þetta þýðir líka að þú getur fínstillt sama efnið fyrir mismunandi skannagerðir, fyrir hvern leysi fyrir sig, án þess að þurfa að breyta Clip sjálfum.

Nánari upplýsingar eru í [Hvernig Liberation býr til laserefni](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Það eru þrjú forstillt _Render Profiles_: _DEFAULT_, _FAST_ og _DETAIL._

_**DEFAULT**_ – gott almennt snið sem hentar best í flestum tilvikum

_**FAST** –_ ef Clip inniheldur mikið efni og hluti af því er bara mjög einfaldir punktar og beinar línur geturðu fengið minna flökt með því að velja þennan valkost.

_**DETAIL**_ – ef þú ert að teikna eitthvað sem þarf skörp horn skaltu nota þennan valkost. Hafðu þó í huga að skannarnir hreyfast hægar, sem getur gert Output flöktandi.

{% hint style="info" %}
Í Clip Editor geturðu látið mismunandi Creator nota ólík Render Profile, en hver leysir vinnur úr þessum sniðum samkvæmt skannastillingunum sínum. Sjá [Forstillingar skanna](../../advanced/scanner-presets.md)
{% endhint %}
