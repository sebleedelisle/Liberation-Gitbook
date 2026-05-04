---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Býr til einn punkt / geisla.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - litur punktsins. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Býr til línu / flöt.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **Size** - lengd línunnar
* **Colour** - litur línunnar. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - horn línunnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ ákvarðar upphafspunkt og snúningsmiðju línunnar
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Býr til hring / keilu.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **radius** - radíus hringsins
* **Colour** - litur hringsins. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* **resolution** - sjá [Upplausn](fundamentals/resolution.md "mention")
* **Fill state** - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Býr til reglulegan marghyrning, t.d. þríhyrning, ferning eða fimmhyrning.

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **size** - fjarlægðin frá miðju að hverju horni
* **Colour** - litur marghyrningsins. Sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - snúningshorn formsins, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md "mention")
* **Fill state** - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Hleður inn SVG-skrá fyrir sérsniðin form.

{% hint style="warning" %}
Liberation styður _SVGTiny_-sniðið. Mælt er með InkScape, en flest vektorforrit geta flutt út á þessu sniði. Gakktu úr skugga um að breyta öllum texta í form áður en þú flytur út. Liberation teiknar útlínur og getur valfrjálst notað fyllingar sem masks. Gakktu úr skugga um að línurnar séu ekki svartar, annars birtast þær ekki án colour modifier!
{% endhint %}

* **Import SVG** - hleður SVG-skrá af diski.

{% hint style="info" %}
Þegar SVG hefur verið hlaðið inn er efninu breytt og það vistað inni í Clip, þannig að þú þarft ekki að halda tengingu við skrána, nema þú viljir síðar breyta mask-stillingum.
{% endhint %}

* **Use fills as masks** - vinnur úr öllum fylltum formum sem mask, þ.e. fyllt með svörtu. Þetta er stillt sjálfkrafa ef SVG-skráin inniheldur fyllt form. Ef hún inniheldur engin fyllt form er þetta óvirkt. Sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - ef formin í SVG-skránni eru ekki með útlínu getum við ekki teiknað þau! Þessi valkostur bætir útlínu (eða _stroke_) við öll fyllt form. Ef SVG-skráin inniheldur engin stroked form er þetta stillt sjálfkrafa. Ef hún inniheldur engin fyllt form er þetta óvirkt.
* **Invert black lines** - ef allar línurnar í SVG-skránni eru svartar sérðu þær ekki! Þessi valkostur breytir þeim í hvítar. Hann er stilltur sjálfkrafa ef SVG-skráin inniheldur aðeins svört form, en er óvirkur ef engin slík eru til staðar.
* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **scale** - stillir stærð SVG-myndarinnar. Þetta er reiknað sjálfkrafa þegar SVG er hlaðið inn (til að tryggja að myndin sé sýnileg), en hægt er að breyta gildinu handvirkt eftir á.
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Býr til hreyfimynd úr röð SVG-skráa.

* **Import SVG Sequence** - veldu möppuna sem inniheldur allar SVG-skrárnar. Athugaðu að þær eru hlaðnar inn í bókstafa- og talnaröð.

{% hint style="info" %}
Þegar SVG-röðinni hefur verið hlaðið inn er efninu breytt og það vistað inni í Clip, þannig að þú þarft ekki að halda tengingu við skrárnar, nema þú viljir síðar breyta mask-stillingum.
{% endhint %}

* **Use fills as masks** - vinnur úr öllum fylltum formum sem mask, þ.e. fyllt með svörtu. Þetta er stillt sjálfkrafa ef einhver SVG-skránna inniheldur fyllt form. Ef engin þeirra inniheldur fyllt form er þetta óvirkt. Sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - ef formin í SVG-skránum eru ekki með neinar útlínur getum við ekki teiknað þau! Þessi valkostur bætir útlínu (eða _stroke_) við öll fyllt form. Ef SVG-skrárnar innihalda engin stroked form er þetta stillt sjálfkrafa. Ef engin þeirra inniheldur fyllt form er þetta óvirkt.
* **Invert black lines** - ef allar línurnar í SVG-skránum eru svartar sérðu þær ekki! Þessi valkostur breytir þeim í hvítar. Hann er stilltur sjálfkrafa ef SVG-skrárnar innihalda aðeins svört form, en er óvirkur ef engin slík eru til staðar.
* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **scale** - stillir stærð myndarinnar.
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md "mention")
* **speed** - lengd allrar hreyfimyndarinnar, í bars.
* **time per frame** - ef þetta er stillt gildir lengdin fyrir hvern ramma, frekar en fyrir alla hreyfimyndina. Ef _speed_ er t.d. stillt á ¼ verður hver rammi 1 taktslag.
* **animation direction** -
  * _FORWARDS_ - hreyfimyndin spilar áfram og fer svo aftur í byrjun
  * _BACKWARDS_ - hreyfimyndin spilar afturábak og fer svo aftur á endann
  * _PINGPONG_ - hreyfimyndin spilar áfram og svo afturábak í lykkju
  * _MANUAL_ - núverandi rammi er stilltur með _position manual_
* **position manual** - stillir núverandi ramma; 0% er fyrsti ramminn og 100% er síðasti ramminn. Þetta er hægt að stilla handvirkt eða með ytri sveiflugjafa.
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Býr til texta með TrueType- eða OpenType-letri.

* **Text** - sláðu inn textann sem þú vilt nota hér
* **Font** - veldu letrið sem þú vilt nota

{% hint style="info" %}
Til að bæta fleiri leturgerðum við Liberation skaltu afrita .ttf- eða .otf-skrárnar í `data/fonts` möppuna inni í vinnumöppu Liberation og endurræsa síðan Liberation.
{% endhint %}

* **Render profile** - sjá [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - veldu _LEFT_, _CENTRE_ eða _RIGHT_ til að stilla textajöfnun.
* **Fill state** - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - stærð textans
* **monospace** - teiknar alla stafi með sömu breidd. Þetta er gagnlegt fyrir tímamæla og teljara, því textinn færist ekki til hliðar þegar tölurnar breytast.
* **character spacing** - stillir bilið á milli stafa. Hækkaðu gildið til að auka stafabil, eða lækkaðu það til að þétta textann.
* **colour -** sjá [Litastillingar og HSB](fundamentals/colour-settings-and-hsb.md "mention")
* **x** og **y** position - sjá [Hnitakerfi](fundamentals/co-ordinate-system.md "mention")
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [Upplausn](fundamentals/resolution.md "mention")
* **reveal** - notaðu þetta til að birta textann smám saman, einn staf í einu. Þegar gildið er á milli 0 og 50% birtist textinn smám saman frá vinstri til hægri. Þegar gildið er á milli 50% og 100% hverfur textinn frá vinstri til hægri. Þú getur tengt sveiflugjafa við þennan socket til að búa til hreyfingar.
* **reveal by word** - þegar þetta er virkt vinnur _reveal_ orð fyrir orð í stað stafs fyrir staf.
* **countdown** - skiptir innslögðum texta út fyrir niðurtalningu. Þegar niðurtalningin nær núlli birtist venjulega **Text** gildið.
* **use seconds** - telur í raunverulegum sekúndum. Þegar slökkt er á þessu byggist niðurtalningin á taktslögum: tvö taktslög teljast sem ein sekúnda, þannig að 120 bpm samsvarar raunverulegum sekúndum.
* **show minutes/seconds** - sýnir tímann sem eftir er í mínútum og sekúndum. Ef hann er yfir klukkustund eru klukkustundir einnig sýndar.
* **countdown to date/time** - telur niður að tiltekinni UTC-dagsetningu og -tíma í stað þess að telja niður frá tölu.
* **countdown datetime** - stillir UTC-markdagsetningu og -tíma þegar kveikt er á **countdown to date/time**.
* **start number** - upphafstalan þegar slökkt er á **countdown to date/time**.
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [Fyllingar, masks og dýptarröðun](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Ef fellivalmynd leturgerða er opin fara upp- og niðurörvatakkarnir í gegnum tiltækar leturgerðir.
{% endhint %}
