---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Breytarar eftir staðsetningu

Þessi hnútafjölskylda breytir efni út frá staðsetningu. Sjálfgefið er áhrifinu beitt eftir láréttum ási (frá vinstri til hægri), en þú getur snúið ásnum í hvaða horn sem er. Hver hnútur inniheldur einnig _radial_ stillingu, þar sem áhrifinu er stýrt af horni hvers punkts miðað við miðjuna.

* **Colour Changer by Position** – færir liti eftir völdum ási eða umhverfis geislahornið.\
  \&#xNAN;_Dæmi: Búðu til regnbogalitstigul sem fer yfir línu, eða notaðu radial stillingu á hring til að búa til litahjólsáhrif._
* **Wave Shift by Position** – beitir sínusbylgjubjögun og hliðrar efninu lóðrétt (eða hornrétt á valinn ás).\
  \&#xNAN;_Dæmi: Láttu línu gára eins og vatn, eða notaðu radial stillingu til að láta hring púlsa út frá miðjunni._
* **Noise Shift by Position** – beitir simplex noise bjögun og hliðrar efninu lóðrétt (eða hornrétt á valinn ás).\
  \&#xNAN;_Dæmi: sjá dæmið fyrir Wave Shift, en með lífrænni og tilviljanakenndari áferð, tilvalið til að bæta við náttúrulegum breytileika._

## &#x20;Litabreyting eftir staðsetningu

Þessi hnútur beitir litabreytingum á efnið út frá staðsetningu. Sjálfgefið er ásinn láréttur (0°), en þú getur snúið honum eða skipt yfir í radial stillingu.

* **wavelength** – stillir stærð endurtekinnar litalotu.
  * _Linear mode:_ við 100% nær ein heil lota yfir alla breidd efnisins.
  * _Radial mode:_ við 100% nær ein heil lota yfir allan hringinn (360°). Gildi eru prósentur af hringnum: t.d. 50% = hálfur hringur (180°).
* **offset** – hliðrar upphafspunkti litalotunnar sem prósentu af wavelength. Þú getur mótað þetta (t.d. með sawtooth oscillator) til að renna mjúklega í gegnum litina.
* **repeat** – þegar þetta er virkt endurtekur lotan sig yfir efnið. Ef slökkt er á þessu er litstigullinn aðeins notaður einu sinni: allt fyrir upphafið fær upphafslitinn og allt eftir endann fær endalitinn.
* **pingpong** – þegar þetta er virkt skiptir hver endurtekning um stefnu og býr til speglað áhrif. Ef slökkt er á _Repeat_ fer litstigullinn fram og svo til baka einu sinni. _Athugaðu: í Pingpong mode nær wavelength yfir bæði fram- og tilbakasveipið._
* **linear angle** – snýr ási áhrifanna. 0° = lárétt.
* **radial** – skiptir yfir í radial stillingu og beitir litum út frá horninu frá miðjunni.
* **radial smooth loop** – aðlagar wavelength sjálfkrafa þannig að hún gangi jafnt upp í 100% af hringnum og kemur þannig í veg fyrir sýnilegan saum þar sem lotan vefst aftur að upphafi.

**Colour Modes**

Þessar stillingar ákvarða hvaða þættir litabreytinganna eru notaðir á efnið. Sjá einnig: [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md).

* **hue mode**
  * _OFF_ – hue helst óbreytt.
  * _FIXED_ – hue er fest við ákveðið gildi.
  * _SHIFTED_ – hue er hliðrað um tilgreint gildi (mismunandi lituð atriði halda aðgreiningu sinni, en færast saman um litahjólið).
* **saturation mode**
  * _OFF_ – saturation helst óbreytt.
  * _FIXED_ – saturation er stillt á tilgreint gildi.
* **brightness mode**
  * _OFF_ – brightness helst óbreytt.
  * _FIXED_ – brightness er stillt á tilgreint gildi.
  * _MULTIPLY_ – brightness er margfaldað með tilgreindu gildi. Þetta varðveitir dýnamík (t.d. halda blikkandi atriði áfram að blikka, en innan takmarkaðs birtusviðs).

**Start / End Values**

Þessir sleðar skilgreina litasviðið sem er beitt eftir völdum ási (eða radial sweep).

* **start hue** – hue í upphafi litstigulsins.
* **end hue** – hue í enda litstigulsins.
* **start saturation** – saturation í upphafi.
* **end saturation** – saturation í enda.
* **start brightness** – brightness í upphafi.
* **end brightness** – brightness í enda.
* **blend** – blandar litabreytingunni við upprunalegu litina. Við 100% kemur áhrifin alveg í stað upprunalegu litanna.

**Dæmi 1: Rennandi regnbogalitstigull**

Byrjaðu með sjálfgefnum stillingum:

1. Láttu hnútinn vera í **Linear** mode (0° angle = horizontal).
2. Láttu **wavelength** vera 100% (nær yfir alla breiddina og ætti að vera sjálfgefið).
3. Láttu upphafs- og endagildin vera sjálfgefin.
4. Kveiktu á **repeat**.
5. Bættu **Sawtooth Oscillator** við **offset** stillinguna sem fer frá 0% til 100%.

***

**Dæmi 2: Svart–hvítt–svart litstigull (Pingpong)**

Byrjaðu með sjálfgefnum stillingum:

1. Láttu hnútinn vera í **Linear** mode (0° angle = horizontal).
2. Láttu **wavelength** vera 100% (nær yfir alla breiddina og ætti að vera sjálfgefið).
3. Slökktu á **repeat**.
4. Stilltu **start brightness** á 0 (svart).
5. Stilltu **end brightness** á 100 (hvítt).
6. Stilltu **start saturation** og **end saturation** á 0 (breytir í grátóna).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Kveiktu á **pingpong**.

_Niðurstaða: litstigullinn dofnar úr svörtu yfir í hvítt og svo aftur yfir í svart yfir breiddina._\
Athugaðu að ef þú vilt að efnið haldi hue og saturation skaltu slökkva á Saturation mode. \\

***

**Dæmi 3: Snúnings-regnbogahjól (Radial)**

1. Kveiktu á **radial** mode.
2. Stilltu **wavelength** á 100% (heil 360° sveifla).
3. Kveiktu á **repeat**.
4. Bættu **Sawtooth Oscillator** við **offset** stillinguna sem fer frá 0% til 100%.

_Niðurstaða: saumlaust litahjól sem snýst stöðugt umhverfis hringinn._

## &#x20;Bylgjuhliðrun eftir staðsetningu

Þessi hnútur beitir bylgjubjögun á efnið og hliðrar punktum hornrétt á valinn ás (eða geislalægt frá miðjunni).

* **Wavelength** – stillir lengd bylgjulotunnar.
  * _Linear mode:_ við 100% nær ein heil lota yfir alla breidd efnisins.
  * _Radial mode:_ við 100% nær ein heil lota yfir öll 360°. (Gildi eru prósentur af hringnum: 50% = hálfur snúningur, 25% = fjórðungssnúningur o.s.frv.)
* **Size** – stýrir útslagi bylgjunnar (hversu langt efnið færist).
* **Offset** – hliðrar bylgjunni eftir ásnum (eða umhverfis hringinn í radial mode). Þetta er prósenta af wavelength, svo þú getur hreyft þetta með **Oscillator Node** til að láta bylgjuna ferðast.
* **Radial** – skiptir úr linear yfir í radial mode, þannig að hliðrunin byggist á horninu frá miðjunni.
* **Radial Smooth Loop** – aðlagar wavelength þannig að hún gangi jafnt upp í 100% af hringnum og kemur í veg fyrir sýnilega sauma við vafninginn.
* **Triangle** – breytir bylgjuforminu úr sínus í þríhyrningsbylgju.
* **Absolute** – tekur algildi bylgjunnar og býr aðeins til hliðrun upp á við (neikvæða hliðin er felld yfir á þá jákvæðu).
* **Angle** – snýr ási bylgjunnar. 0° = lárétt.

## &#x20;Noise-hliðrun eftir staðsetningu

Þessi hnútur bjagar efni með noise-sviði (eins og ókyrrð) og hliðrar punktum hornrétt á valinn ás (eða geislalægt frá miðjunni). Í samanburði við _Wave Shift_ verður útkoman lífrænni og tilviljanakenndari.

* **Detail** – stýrir hversu fínkornað noise er. Hærri gildi = skarpari og ítarlegri breytileiki. Lægri gildi = mýkri breytileiki.
* **Wavelength** – stillir skala noise-mynstursins.
  * _Linear mode:_ við 100% nær ein heil noise-lota yfir breidd efnisins.
  * _Radial mode:_ við 100% nær ein heil lota yfir öll 360°.
* **Size** – stýrir magni hliðrunar (útslagi noise-bjögunarinnar).
* **Offset** – hliðrar noise-mynstrinu eftir ásnum (eða umhverfis hringinn). Þetta er prósenta af wavelength, svo þú getur hreyft þetta með **Oscillator Node** til að láta noise “flæða.”
* **Depth Offset** – færir sig í gegnum 3D noise-sviðið og býr til breytileika yfir tíma. Þetta er sérstaklega áhrifaríkt þegar það er hreyft með Oscillator Node.
* **Depth Detail** – stýrir hversu ítarlegur breytileikinn er eftir dýptarvíddinni.
* **Absolute** – tekur algildi noise og fellir neikvæð gildi yfir í jákvæð (býr aðeins til einhliða hliðrun).
* **Radial** – skiptir úr linear yfir í radial mode, þannig að hliðrunin byggist á horninu frá miðjunni.
* **Radial Smooth Loop** – aðlagar wavelength þannig að hún gangi jafnt upp í 100% af hringnum og kemur í veg fyrir sýnilega sauma í radial mode.
