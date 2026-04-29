---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Býr til einn punkt / geisla.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **Colour** - litur punktsins. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Býr til línu / flöt.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **Size** - lengd línunnar
* **Colour** - litur línunnar. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* **rotation** - horn línunnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ ákvarðar upphafspunkt og snúningsmiðju línunnar
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Býr til hring / keilu.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **radius** - radíus hringsins
* **Colour** - litur hringsins. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* **resolution** - sjá [Upplausn](fundamentals/resolution.md)
* **Fill state** - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Býr til reglulegan marghyrning, t.d. þríhyrning, ferning eða fimmhyrning.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **size** - fjarlægðin frá miðju að hverju horni
* **Colour** - litur marghyrningsins. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn formsins, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md)
* **Fill state** - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Hleður inn SVG-skrá fyrir sérsniðin form.

{% hint style="warning" %}
Liberation styður _SVGTiny_-sniðið. Mælt er með InkScape, en flest vektorforrit geta flutt út á þessu sniði. Gakktu úr skugga um að breyta öllum texta í form áður en þú flytur út. Liberation teiknar útlínur og getur valfrjálst notað fyllingar sem masks. Gakktu úr skugga um að línurnar séu ekki svartar, annars birtast þær ekki án colour modifier!
{% endhint %}

* **Import SVG** - hleður SVG-skrá af diski.

{% hint style="info" %}
Þegar SVG hefur verið hlaðið inn er efninu breytt og það vistað inni í Clip, þannig að þú þarft ekki að halda tengingu við skrána, nema þú viljir síðar breyta mask-stillingum.
{% endhint %}

* **Use fills as masks** - vinnur úr öllum fylltum formum sem mask, þ.e. fyllt með svörtu. Þetta er stillt sjálfkrafa ef SVG-skráin inniheldur fyllt form. Ef hún inniheldur engin fyllt form er þetta óvirkt. Sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - ef formin í SVG-skránni eru ekki með útlínu getum við ekki teiknað þau! Þessi valkostur bætir útlínu (eða _stroke_) við öll fyllt form. Ef SVG-skráin inniheldur engin stroked form er þetta stillt sjálfkrafa. Ef hún inniheldur engin fyllt form er þetta óvirkt.
* **Invert black lines** - ef allar línurnar í SVG-skránni eru svartar sérðu þær ekki! Þessi valkostur breytir þeim í hvítar. Hann er stilltur sjálfkrafa ef SVG-skráin inniheldur aðeins svört form, en er óvirkur ef engin slík eru til staðar.
* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **scale** - stillir stærð SVG-myndarinnar. Þetta er reiknað sjálfkrafa þegar SVG er hlaðið inn (til að tryggja að myndin sé sýnileg), en hægt er að breyta gildinu handvirkt eftir á.
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Býr til hreyfimynd úr röð SVG-skráa.

* **Import SVG Sequence** - veldu möppuna sem inniheldur allar SVG-skrárnar. Athugaðu að þær eru hlaðnar inn í bókstafa- og talnaröð.

{% hint style="info" %}
Þegar SVG-röðinni hefur verið hlaðið inn er efninu breytt og það vistað inni í Clip, þannig að þú þarft ekki að halda tengingu við skrárnar, nema þú viljir síðar breyta mask-stillingum.
{% endhint %}

* **Use fills as masks** - vinnur úr öllum fylltum formum sem mask, þ.e. fyllt með svörtu. Þetta er stillt sjálfkrafa ef einhver SVG-skránna inniheldur fyllt form. Ef engin þeirra inniheldur fyllt form er þetta óvirkt. Sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - ef formin í SVG-skránum eru ekki með neinar útlínur getum við ekki teiknað þau! Þessi valkostur bætir útlínu (eða _stroke_) við öll fyllt form. Ef SVG-skrárnar innihalda engin stroked form er þetta stillt sjálfkrafa. Ef engin þeirra inniheldur fyllt form er þetta óvirkt.
* **Invert black lines** - ef allar línurnar í SVG-skránum eru svartar sérðu þær ekki! Þessi valkostur breytir þeim í hvítar. Hann er stilltur sjálfkrafa ef SVG-skrárnar innihalda aðeins svört form, en er óvirkur ef engin slík eru til staðar.
* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **scale** - stillir stærð myndarinnar.
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md)
* **speed** - lengd allrar hreyfimyndarinnar, í bars.
* **time per frame** - ef þetta er stillt gildir lengdin fyrir hvern ramma, frekar en fyrir alla hreyfimyndina. Ef _speed_ er t.d. stillt á ¼ verður hver rammi 1 taktslag.
* **animation direction** -
  * _FORWARDS_ - hreyfimyndin spilar áfram og fer svo aftur í byrjun
  * _BACKWARDS_ - hreyfimyndin spilar afturábak og fer svo aftur á endann
  * _PINGPONG_ - hreyfimyndin spilar áfram og svo afturábak í lykkju
  * _MANUAL_ - núverandi rammi er stilltur með _position manual_
* **position manual** - stillir núverandi ramma; 0% er fyrsti ramminn og 100% er síðasti ramminn. Þetta er hægt að stilla handvirkt eða með ytri sveiflugjafa.
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Býr til texta með TrueType- eða OpenType-letri.

* **Text** - sláðu inn textann sem þú vilt nota hér
* **Font** - veldu letrið sem þú vilt nota

{% hint style="info" %}
Til að bæta fleiri leturgerðum við Liberation skaltu afrita .ttf- eða .otf-skrárnar í data/resources/fonts möppuna.
{% endhint %}

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md)
* **horizontal alignment** - veldu _LEFT_, _CENTRE_ eða _RIGHT_ til að stilla textajöfnun.
* **Fill state** - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - stærð textans
* **colour -** sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md)
* **reveal** - notaðu þetta til að birta textann smám saman, einn staf í einu. Þegar gildið er á milli 0 og 50% birtist textinn smám saman frá vinstri til hægri. Þegar gildið er á milli 50% og 100% hverfur textinn frá vinstri til hægri. Þú getur tengt sveiflugjafa við þennan socket til að búa til hreyfingar.
* **reveal by word** - þegar þetta er virkt vinnur _reveal_ orð fyrir orð í stað stafs fyrir staf.
* **countdown** - niðurtalningarkerfi (sett saman í flýti!). Breytist á 2 taktslaga fresti, þannig að ef þú vilt sekúndur skaltu ganga úr skugga um að tempóið sé 120 bpm.
* **countdown start** - talan sem þú vilt að niðurtalningin byrji á
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md)
