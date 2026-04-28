---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Jokaisessa _Creator_-solmussa on _Render Profile_ -asetus. Se määrittää, miten muodot piirretään (eli _renderöidään_) lasereilla.

**Useimpiin tarkoituksiin&#x20;**_**DEFAULT**_**&#x20;-asetus riittää erinomaisesti**. Jos kuitenkin työskentelet grafiikan tai monimutkaisen sisällön kanssa, saatat haluta tarkempaa hallintaa siihen, miten kukin muoto renderöidään.

{% hint style="info" %}
Toisin kuin useimmat laseröhjelmistot, Liberation luo pistevirran reaaliajassa juuri ennen sen lähettämistä laserohjaimille. Tämä säästää paljon levytilaa: klipit ovat vain muutaman kilotavun kokoisia sen sijaan, että ne olisivat megatavujen kokoisia esirenderöityjä pistevirtoja.

Se tarkoittaa myös, että voit säätää saman sisällön eri skannerityypeille laserkohtaisesti ilman, että itse klippejä tarvitsee muuttaa.

Lisätietoja: [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Valmiita _Render Profile_ -profiileja on kolme: _DEFAULT_, _FAST_ ja _DETAIL._

_**DEFAULT**_ – hyvä yleisprofiili, paras useimpiin tilanteisiin

_**FAST** -_ jos klipissäsi on paljon sisältöä ja osa siitä on hyvin yksinkertaisia pisteitä ja suoria viivoja, tämä vaihtoehto voi vähentää välkkymistä.

_**DETAIL**_ – käytä tätä vaihtoehtoa, jos piirrät sisältöä, joka tarvitsee teräviä kulmia. Huomaa kuitenkin, että skannerit liikkuvat hitaammin, jolloin ulostulo voi välkkyä enemmän.

{% hint style="info" %}
Clip editorissa voit määrittää creatorit eri renderöintiprofiileihin, mutta jokainen laser käsittelee näitä profiileja omien skanneriasetustensa mukaan. Katso [scanner-presets.md](../../advanced/scanner-presets.md)
{% endhint %}
