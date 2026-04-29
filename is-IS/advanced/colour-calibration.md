---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Litkvörðun

Litkvörðun tryggir að rauðir, grænir og bláir leysar í skjávarpanum gefi frá sér ljós á mjúkan og fyrirsjáanlegan hátt á öllum birtustigum. Mismunandi skjávarpar geta haft ólínulegar birtukúrfur, sem þýðir að 50% rautt getur virst mun bjartara eða dekkra en helmingur af styrk 100% rauðs. Kvörðun leiðréttir þetta svo litir blandist hreint, litaskalar verði mjúkir og hvítur litur haldist í jafnvægi.

#### Að hita upp skjávarpann

Leysisdíóður breyta hegðun sinni þegar þær hitna. Láttu skjávarpann alltaf ná stöðugu ástandi áður en þú kvarðar:

* Varpaðu björtum ramma, til dæmis **White rectangle test pattern (11)**, í að minnsta kosti **15–20 mínútur**.
* Þannig helst litajafnvægið sem þú stillir stöðugt meðan á sýningu stendur.

#### Hvernig kvörðunarprófið virkar

Notaðu test pattern fyrir kvörðun (sjá [Test patterns](../output-view/test-patterns.md))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Hvert þeirra sýnir fjórar hreyfanlegar línur:

* **Efsta lína** – 100% birta á fullum hraða
* **Önnur lína** – 75% birta á 75% hraða
* **Þriðja lína** – 50% birta á 50% hraða
* **Fjórða lína** – 25% birta á 25% hraða

Þar sem bæði birta _og hraði_ eru sköluð saman ættu allar línurnar að virðast jafn bjartar. Ef ein þeirra virðist ljósari eða dekkri skaltu stilla samsvarandi sleða þar til þær passa saman.

Hvert test pattern hefur einnig fimmtu línu við **0% birtu** sem ætti ekki að sjást. Hún er notuð til að leiðrétta leysa sem gefa ekki frá sér neitt ljós við mjög lágt stig. Ef leysirinn sést ekki við lága birtu skaltu hækka **0% stillinguna** smám saman þar til línan rétt sést, og lækka hana svo örlítið þar til hún hverfur aftur. Markmiðið er að finna þröskuldinn þar sem leysirinn byrjar að lýsa og vera rétt fyrir neðan hann — svo dofnanir byrji eðlilega án þess að neðsta sviðið klippist af.

#### Notkun Colour Calibration spjaldsins

Spjaldið gefur þér sjálfstæðar stillingar fyrir hverja rás (rauða, græna og bláa) við 100, 75, 50, 25 og 0% stig.

1. **Veldu test pattern** (byrjaðu á rauðu).
2. **Stilltu sleðana** þannig að 100, 75, 50 og 25% línurnar virðist jafn bjartar.
3. **Fínstilltu 0% sleðann** ef “off” línan sést ennþá mjög dauft.
4. **Endurtaktu fyrir grænt og blátt.**
5. Skiptu yfir í **White test pattern (8)**. Allar fjórar línurnar ættu að virðast jafnar og hvíti liturinn ætti að vera hlutlaus (ekki litaður).

#### Að stilla hvítjöfnun

Þú getur líka notað þetta kerfi til að stilla **hvítjöfnun**. Þegar þú hefur kvarðað hverja rás fyrir sig skaltu skipta yfir í **White test pattern (8)**. Ef úttakið virðist litað (til dæmis of grænt eða of blátt) skaltu stilla hlutfallsleg stig rauðu, grænu og bláu rásanna þar til línurnar virðast hlutlaust hvítar. Jafnvel þó leysarnir séu mjög ólíkir að afli hjálpar kvörðunin samt til við að færa þá nær hver öðrum og búa til hreinni og betur jafnvægta litablöndu.

#### Að vista kvörðunina

* Notaðu **Store** til að skrifa yfir núverandi preset.
* Notaðu **Store As** til að búa til nýtt preset (gagnlegt ef þú vinnur með marga leysa).
