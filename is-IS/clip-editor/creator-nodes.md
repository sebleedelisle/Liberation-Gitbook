---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator-hnútar

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Býr til einn punkt / geisla.

* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **Colour** - litur punktsins. Sjá [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Býr til línu / flöt.

* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **Size** - lengd línunnar
* **Colour** - litur línunnar. Sjá [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - horn línunnar, í gráðum
* **resolution** - sjá [resolution.md](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ ákvarðar upphafspunkt og snúningsmiðju línunnar
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Býr til hring / keilu.

* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **radius** - radíus hringsins
* **Colour** - litur hringsins. Sjá [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **resolution** - sjá [resolution.md](fundamentals/resolution.md)
* **Fill state** - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Býr til reglulegan marghyrning, þríhyrning, ferning, fimmhyrning o.s.frv.

* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **size** - fjarlægðin frá miðju að hverju horni
* **Colour** - litur marghyrningsins. Sjá [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn formsins, í gráðum
* **resolution** - sjá [resolution.md](fundamentals/resolution.md)
* **Fill state** - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Hleður inn SVG-skrá fyrir sérsniðin form.

{% hint style="warning" %}
Liberation er samhæft við _SVGTiny_ sniðið. Mælt er með InkScape, en flest vektorforrit geta flutt út á þessu sniði. Gakktu úr skugga um að breyta öllum texta í form áður en þú flytur út. Liberation birtir útlínur (strokes) og getur valkvætt notað fyllingar sem maska. Gakktu úr skugga um að línurnar þínar séu ekki svartar, annars sjást þær ekki án litabreytis!
{% endhint %}

* **Import SVG** - hlaða SVG-skrá af diski.

{% hint style="info" %}
Þegar SVG hefur verið hlaðið inn er efninu umbreytt og það vistað inni í clipinu, svo þú þarft ekki að halda tengingu við skrána, nema þú viljir síðar breyta maskastillingunum.
{% endhint %}

* **Use fills as masks** - vinnur úr öllum fylltum formum sem möskum, þ.e. fylltum með svörtu. Þetta er stillt sjálfkrafa ef SVG-skráin þín inniheldur einhver fyllt form. Ef hún inniheldur engin fyllt form er þetta óvirkt. Sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - ef formin í SVG-skránni þinni eru ekki með útlínu getum við ekki teiknað þau! Þessi valkostur bætir útlínu (eða _stroke_) við öll fyllt form. Ef SVG-skráin þín er ekki með nein form með stroke er þetta stillt sjálfkrafa. Ef hún inniheldur engin fyllt form er þetta óvirkt.
* **Invert black lines** - ef allar línurnar í SVG-skránni þinni eru svartar sérðu þær ekki! Þessi valkostur breytir þeim í hvítar. Hann er stilltur sjálfkrafa ef SVG-skráin þín inniheldur aðeins svört form, en er óvirkur ef hún inniheldur engin slík.
* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **scale** - stillir stærð SVG-myndarinnar. Þetta er reiknað sjálfkrafa þegar SVG er hlaðið inn (til að tryggja að myndin sjáist), en hægt er að breyta því handvirkt síðar.
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [resolution.md](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Býr til hreyfimynd úr röð SVG-skráa.

* **Import SVG Sequence** - veldu möppuna sem inniheldur allar SVG-skrárnar. Athugaðu að þær eru hlaðnar inn í alfanúmerískri röð.

{% hint style="info" %}
Þegar SVG-röðinni hefur verið hlaðið inn er efninu umbreytt og það vistað inni í clipinu, svo þú þarft ekki að halda tengingu við skrárnar, nema þú viljir síðar breyta maskastillingunum.
{% endhint %}

* **Use fills as masks** - vinnur úr öllum fylltum formum sem möskum, þ.e. fylltum með svörtu. Þetta er stillt sjálfkrafa ef einhver SVG-skránna þinna inniheldur fyllt form. Ef engin þeirra inniheldur fyllt form er þetta óvirkt. Sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - ef formin í SVG-skránum þínum eru ekki með neinar útlínur getum við ekki teiknað þau! Þessi valkostur bætir útlínu (eða _stroke_) við öll fyllt form. Ef SVG-skrárnar þínar eru ekki með nein form með stroke er þetta stillt sjálfkrafa. Ef engin þeirra inniheldur fyllt form er þetta óvirkt.
* **Invert black lines** - ef allar línurnar í SVG-skránum þínum eru svartar sérðu þær ekki! Þessi valkostur breytir þeim í hvítar. Hann er stilltur sjálfkrafa ef SVG-skrárnar þínar innihalda aðeins svört form, en er óvirkur ef þær innihalda engin slík.
* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **scale** - stillir stærð myndarinnar.
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [resolution.md](fundamentals/resolution.md)
* **speed** - lengd allrar hreyfimyndarinnar, í töktum.
* **time per frame** - ef þetta er stillt gildir lengdin fyrir hvern ramma í stað allrar hreyfimyndarinnar. Ef _speed_ er stillt á ¼ verður hver rammi 1 slag.
* **animation direction** -
  * _FORWARDS_ - hreyfimyndin keyrir áfram og fer síðan aftur í byrjun
  * _BACKWARDS_ - hreyfimyndin keyrir afturábak og fer síðan aftur á endann
  * _PINGPONG_ - hreyfimyndin keyrir áfram og síðan afturábak í lykkju
  * _MANUAL_ - núverandi rammi er stilltur með _position manual_ stillingunni
* **position manual** - stillir núverandi ramma; 0% er fyrsti ramminn og 100% er síðasti ramminn. Hægt er að stilla þetta handvirkt eða með ytri sveiflugjafa.
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Býr til texta með TrueType- eða OpenType-letri.

* **Text** - sláðu inn textann sem þú vilt nota hér
* **Font** - veldu letrið sem þú vilt nota

{% hint style="info" %}
Til að bæta fleiri letrum við Liberation skaltu afrita .ttf- eða .otf-skrárnar í data/resources/fonts möppuna.
{% endhint %}

* **Render profile** - sjá [render-profile.md](fundamentals/render-profile.md)
* **horizontal alignment** - veldu _LEFT_, _CENTRE_ eða _RIGHT_ til að stilla textajöfnunina.
* **Fill state** - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - textastærðin
* **colour -** sjá [colour-settings-and-hsb.md](fundamentals/colour-settings-and-hsb.md)
* **x** og **y** position - sjá [co-ordinate-system.md](fundamentals/co-ordinate-system.md)
* **rotation** - snúningshorn myndarinnar, í gráðum
* **resolution** - sjá [resolution.md](fundamentals/resolution.md)
* **reveal** - notaðu þetta til að sýna textann smám saman, einn staf í einu. Þegar þetta er á milli 0 og 50% birtist textinn smám saman frá vinstri til hægri. Þegar þetta er á milli 50% og 100% hverfur textinn frá vinstri til hægri. Þú getur tengt sveiflugjafa við þennan tengipunkt til að búa til hreyfingar.
* **reveal by word** - þegar þetta er virkt vinnur _reveal_ orð fyrir orð í stað stafs fyrir staf.
* **countdown** - niðurtalningarkerfi (sett saman í flýti!). Breytist á tveggja slaga fresti, þannig að ef þú vilt sekúndur skaltu ganga úr skugga um að þú sért á 120 bpm.
* **countdown start** - talan sem þú vilt að niðurtalningin byrji á
* _MOVE TO FRONT / MOVE TO BACK_ - sjá [fills-masks-and-depth-sorting.md](fundamentals/fills-masks-and-depth-sorting.md)
