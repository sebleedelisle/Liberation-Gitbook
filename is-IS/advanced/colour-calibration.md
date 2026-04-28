---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Litkvörðun

Litkvörðun tryggir að rauðir, grænir og bláir leysar skjávarpans gefi frá sér ljós á mjúkan og fyrirsjáanlegan hátt á öllum birtustigum. Mismunandi skjávarpar geta haft ólínulegar birtukúrfur, sem þýðir að 50% rautt getur virst mun bjartara eða daufara en helmingurinn af styrk 100% rauðs. Kvörðun leiðréttir þetta svo litir blandist hreint, litstiglar verði mjúkir og hvítur litur sé í jafnvægi.

#### Að hita skjávarpann upp

Leysidíóður breyta hegðun sinni þegar þær hitna. Leyfðu skjávarpanum alltaf að ná stöðugleika áður en þú kvarðar:

* Varpaðu björtum ramma, til dæmis **White rectangle test pattern (11)**, í að minnsta kosti **15–20 mínútur**.
* Þetta tryggir að litajafnvægið sem þú stillir haldist stöðugt meðan á sýningu stendur.

#### Hvernig kvörðunarprófið virkar

Notaðu prófmynstrin fyrir kvörðun (sjá [test-patterns.md](../output-view/test-patterns.md))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Hvert þeirra sýnir fjórar hreyfanlegar línur:

* **Efsta lína** – 100% birta á fullum hraða
* **Önnur lína** – 75% birta á 75% hraða
* **Þriðja lína** – 50% birta á 50% hraða
* **Fjórða lína** – 25% birta á 25% hraða

Þar sem bæði birta _og hraði_ eru sköluð saman ættu allar línurnar að virðast jafn bjartar. Ef ein virðist ljósari eða dekkri skaltu stilla samsvarandi sleða þar til þær passa saman.

Hvert prófmynstur hefur einnig fimmtu línu við **0% birtu** sem ætti ekki að sjást. Þetta er notað til að leiðrétta leysigeisla sem gefa ekkert ljós frá sér við mjög lágt stig. Ef leysigeislinn þinn er enn ósýnilegur við lága birtu skaltu hækka **0% setting** smám saman þar til línan rétt sést, og lækka síðan örlítið þar til hún hverfur aftur. Markmiðið er að finna þröskuldinn þar sem leysigeislinn byrjar að lýsa, og vera svo rétt fyrir neðan hann - þannig byrja dofnanir eðlilega án þess að neðsti hluti sviðsins sé skorinn af.

#### Að nota Colour Calibration panel

Spjaldið gefur þér sjálfstæðar stýringar fyrir hverja rás (rauða, græna, bláa) við 100, 75, 50, 25 og 0% stig.

1. **Veldu prófmynstur** (byrjaðu á rauðu).
2. **Stilltu sleðana** þannig að 100, 75, 50 og 25% línurnar virðist jafn bjartar.
3. **Fínstilltu 0% sleðann** ef „slökkt“ línan sést enn mjög dauft.
4. **Endurtaktu fyrir grænt og blátt.**
5. Skiptu yfir í **White test pattern (8)**. Allar fjórar línurnar ættu að virðast jafnar og hvíti liturinn ætti að vera hlutlaus (ekki litaður).

#### Að stilla hvítjöfnun

Þú getur einnig notað þetta kerfi til að stilla **hvítjöfnun**. Eftir að hafa kvarðað hverja rás fyrir sig skaltu skipta yfir í **White test pattern (8)**. Ef úttakið virðist litað (til dæmis of grænt eða of blátt) skaltu stilla hlutfallsleg stig rauðu, grænu og bláu rásanna þar til línurnar virðast hlutlausar hvítar. Jafnvel þótt aflstyrkur leysigeislanna sé nokkuð misjafn hjálpar kvörðun samt við að færa þá nær hver öðrum og skila hreinni og betur jafnaðri litablöndu.

#### Að vista kvörðunina

* Notaðu **Store** til að skrifa yfir núverandi forstillingu.
* Notaðu **Store As** til að búa til nýja forstillingu (gagnlegt ef þú vinnur með marga leysigeisla).
