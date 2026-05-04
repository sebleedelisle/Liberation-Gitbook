---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Staðsetningarbundnir breytar

Þessi flokkur inniheldur node sem breyta efni út frá staðsetningu. Sjálfgefið er áhrifinu beitt eftir láréttum ási, frá vinstri til hægri, en þú getur snúið ásnum í hvaða horn sem er. Hver node er líka með _radial_ stillingu, þar sem áhrifin ráðast af horni hvers punkts miðað við miðju.

* **Colour Changer by Position** – beitir stigli eftir völdum ási eða í kringum radial hornið.\
  \&#xNAN;_Dæmi: Búðu til regnbogastigul sem fer yfir línu, eða notaðu radial stillingu á hring til að fá litahringsáhrif._
* **Wave Shift by Position** – beitir sinusbylgju-aflögun og hliðrar efninu lóðrétt, eða hornrétt á valinn ás.\
  \&#xNAN;_Dæmi: Láttu línu gára eins og vatn, eða notaðu radial stillingu til að láta hring púlsa út frá miðjunni._
* **Noise Shift by Position** – beitir simplex noise aflögun og hliðrar efninu lóðrétt, eða hornrétt á valinn ás.\
  \&#xNAN;_Dæmi: svipað og Wave Shift dæmið, en með lífrænni og tilviljanakenndari áferð, sem hentar vel til að bæta við náttúrulegum breytileika._

## &#x20;Litabreyting eftir staðsetningu

Þessi node beitir litabreytingum á efnið út frá staðsetningu. Sjálfgefið er ásinn láréttur (0°), en þú getur snúið honum eða skipt yfir í radial stillingu.

* **wavelength** – stillir stærð endurtekinnar litalotu.
  * _Linear mode:_ við 100% nær ein heil lota yfir alla breidd efnisins.
  * _Radial mode:_ við 100% nær ein heil lota allan hringinn (360°). Gildi eru prósentur af hringnum: t.d. 50% = hálfur hringur (180°).
* **offset** – hliðrar upphafspunkti litalotunnar, sem prósentu af wavelength. Þú getur mótað þetta, t.d. með sawtooth oscillator, til að fara mjúklega í gegnum litina.
* **repeat** – þegar þetta er virkt endurtekur lotan sig yfir efnið. Ef þetta er óvirkt er stigullinn aðeins notaður einu sinni: allt fyrir upphafið fær upphafslitinn og allt eftir endann fær endalitinn.
* **pingpong** – þegar þetta er virkt skiptir hver endurtekning um stefnu og býr til spegluð áhrif. Ef _Repeat_ er óvirkt fer stigullinn einu sinni áfram og síðan til baka. _Athugaðu: í Pingpong mode nær wavelength bæði yfir ferðina áfram og ferðina til baka._
* **linear angle** – snýr ási áhrifanna. 0° = lárétt.
* **radial** – skiptir yfir í radial stillingu og beitir litum út frá horni frá miðju.
* **radial smooth loop** – lagar wavelength sjálfkrafa þannig að hún gangi jafnt upp í 100% af hringnum og kemur í veg fyrir sýnilega samskeytalínu þar sem lotan vefst um.
* **legacy mode** – skiptir aftur yfir í eldri HSB-rennana fyrir upphaf og enda. Hafðu þetta slökkt til að nota nýrri stigulritilinn.

**Litastillingar**

Þessar stillingar ákvarða hvaða þættir litabreytinganna eru notaðir á efnið. Sjá einnig: [Litastillingar og HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – litblær helst óbreyttur.
  * _FIXED_ – litblær er þvingaður í fast gildi.
  * _SHIFTED_ – litblæ er hliðrað um tilgreint magn. Einingar með ólíka liti haldast aðgreindar, en færast saman um litahringinn.
* **saturation mode**
  * _OFF_ – mettun helst óbreytt.
  * _FIXED_ – mettun er stillt á tilgreint gildi.
* **brightness mode**
  * _OFF_ – birta helst óbreytt.
  * _FIXED_ – birta er stillt á tilgreint gildi.
  * _MULTIPLY_ – birta er sköluð með tilgreindu gildi. Þetta varðveitir hreyfingu í birtu, t.d. halda blikkandi einingar áfram að blikka, en innan takmarkaðra birtumarka.

**Stigulritill**

Notar sama stigulritil og [Colour Changer](colour-changer.md "mention"), en varpar stiglinum yfir efnið eftir staðsetningu.

* Smelltu á stigulstikuna til að bæta við litastoppi.
* Vinstrismelltu á stopp til að velja það og dragðu það síðan til hliðar til að færa það.
* Dragðu valið stopp niður frá stikunni, eða ýttu á Delete/Backspace, til að fjarlægja það. Stigull heldur alltaf að minnsta kosti tveimur stoppum.
* Hægrismelltu á stopp til að breyta því með litavalinu.
* Notaðu **Position**, **Hue**, **Saturation** og **Brightness** til að breyta völdu stoppi nákvæmlega.
* **interpolation** velur hvernig litir blandast milli stoppa:
* **HSB** – blandar litblæ, mettun og birtu. Þetta hentar best fyrir mjúka regnbogalíka hreyfingu um litahjólið.
* **RGB** – blandar rauðum, grænum og bláum gildum beint. Þetta minnir oft meira á litaflökt á skjá eða ljósaborði.
* **NONE** – hoppar frá einu stoppi í það næsta án blöndunar.
* **hue direction** er í boði í HSB-blöndun:
* **AUTO** – fer stystu leiðina um litblæshjólið.
* **FORWARDS** – fer alltaf áfram í gegnum litblæsgildin.
* **BACKWARDS** – fer alltaf afturábak í gegnum litblæsgildin.
* **blend** – blandar litabreytingunni við upprunalegu litina. Við 100% kemur áhrifin alveg í stað upprunalegu litanna.

**Eldri upphafs- og endagildi**

Ef **legacy mode** er kveikt kemur eldri stýring í stað stigulritilsins:

* **start hue / end hue** – litblær við upphaf og enda sviðsins.
* **start saturation / end saturation** – mettun við upphaf og enda sviðsins.
* **start brightness / end brightness** – birta við upphaf og enda sviðsins.

**Dæmi 1: Rennandi regnbogastigull**

Byrjaðu með sjálfgefnum stillingum:

1. Hafðu node áfram í **Linear** mode (0° angle = lárétt).
2. Hafðu **wavelength** á 100% (nær yfir alla breiddina og ætti að vera sjálfgefið).
3. Láttu sjálfgefna stigulinn vera óbreyttan.
4. Virkjaðu **repeat**.
5. Bættu **Sawtooth Oscillator** við **offset** stillinguna sem fer frá 0% til 100%.

***

**Dæmi 2: Svart–hvítt–svart stigull (Pingpong)**

Byrjaðu með sjálfgefnum stillingum:

1. Hafðu node áfram í **Linear** mode (0° angle = lárétt).
2. Hafðu **wavelength** á 100% (nær yfir alla breiddina og ætti að vera sjálfgefið).
3. Slökktu á **repeat**.
4. Stilltu fyrsta stopp stigulsins á svart.
5. Stilltu síðasta stopp stigulsins á hvítt.
6. Slökktu á **hue mode**.
7. Stilltu **saturation mode** á FIXED ef þú vilt þvinga niðurstöðuna í grátóna.
8. Stilltu **brightness mode** á FIXED.
9. Kveiktu á **pingpong**.

_Niðurstaða: stigullinn dofnar frá svörtu yfir í hvítt og síðan aftur yfir í svart yfir breiddina._\
Athugaðu að ef þú vilt að efnið haldi litblæ og mettun skaltu slökkva á Saturation mode. \\

***

**Dæmi 3: Snúandi regnbogahjól (Radial)**

1. Virkjaðu **radial** mode.
2. Stilltu **wavelength** á 100% (heilt 360° sveip).
3. Kveiktu á **repeat**.
4. Bættu **Sawtooth Oscillator** við **offset** stillinguna sem fer frá 0% til 100%.

_Niðurstaða: saumlaust litahjól sem snýst stöðugt í kringum hringinn._

## &#x20;Bylgjuhliðrun eftir staðsetningu

Þessi node beitir bylgjuaflögun á efnið og hliðrar punktum hornrétt á valinn ás, eða út frá miðjunni í radial stillingu.

* **Wavelength** – stillir lengd bylgjulotunnar.
  * _Linear mode:_ við 100% nær ein heil lota yfir alla breidd efnisins.
  * _Radial mode:_ við 100% nær ein heil lota yfir öll 360°. (Gildi eru prósentur af hringnum: 50% = hálfur snúningur, 25% = fjórðungssnúningur o.s.frv.)
* **Size** – stjórnar útslagi bylgjunnar, þ.e. hversu langt efnið færist.
* **Offset** – hliðrar bylgjunni eftir ásnum, eða í kringum hringinn í radial stillingu. Þetta er prósenta af wavelength, þannig að þú getur hreyft það með **Oscillator Node** til að láta bylgjuna ferðast.
* **Radial** – skiptir úr linear yfir í radial stillingu, þannig að tilfærslan byggist á horninu frá miðju.
* **Radial Smooth Loop** – lagar wavelength þannig að hún gangi jafnt upp í 100% af hringnum og kemur í veg fyrir sýnileg samskeyti þar sem sveipurinn vefst um.
* **Triangle** – breytir bylgjulöguninni úr sinus í þríhyrningsbylgju.
* **Absolute** – notar algildi bylgjunnar og býr aðeins til tilfærslur upp á við, með því að fella neikvæðu hliðina yfir á þá jákvæðu.
* **Angle** – snýr ási bylgjunnar. 0° = lárétt.

## &#x20;Noise hliðrun eftir staðsetningu

Þessi node aflagar efni með noise sviði, svipað og ókyrrð, og hliðrar punktum hornrétt á valinn ás, eða út frá miðjunni í radial stillingu. Í samanburði við _Wave Shift_ verður útkoman lífrænni og tilviljanakenndari.

* **Detail** – stjórnar hversu fíngert noise er. Hærri gildi gefa skarpari og ítarlegri breytileika. Lægri gildi gefa mýkri breytileika.
* **Wavelength** – stillir skala noise mynstrsins.
  * _Linear mode:_ við 100% nær ein heil noise lota yfir breidd efnisins.
  * _Radial mode:_ við 100% nær ein heil lota yfir öll 360°.
* **Size** – stjórnar magni tilfærslu, þ.e. útslagi noise aflögunarinnar.
* **Offset** – hliðrar noise mynstrinu eftir ásnum, eða í kringum hringinn. Þetta er prósenta af wavelength, þannig að þú getur hreyft það með **Oscillator Node** til að láta noise “flæða.”
* **Depth Offset** – færist í gegnum 3D noise sviðið og býr til breytileika yfir tíma. Þetta er sérstaklega áhrifaríkt þegar það er hreyft með Oscillator Node.
* **Depth Detail** – stjórnar hversu ítarlegur breytileikinn er eftir dýptarvíddinni.
* **Absolute** – notar algildi noise og fellir neikvæð gildi yfir í jákvæð gildi, sem skapar aðeins einhliða tilfærslu.
* **Angle** – snýr ás suðsins í linear mode. 0° = lárétt.
* **Radial** – skiptir úr linear yfir í radial stillingu, þannig að tilfærslan byggist á horninu frá miðju.
* **Radial Smooth Loop** – lagar wavelength þannig að hún gangi jafnt upp í 100% af hringnum og kemur í veg fyrir sýnileg samskeyti í radial stillingu.
