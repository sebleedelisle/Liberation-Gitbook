---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Promjene na temelju položaja

Ova skupina node elemenata mijenja sadržaj prema položaju. Prema zadanim postavkama efekt se primjenjuje duž vodoravne osi (slijeva nadesno), ali tu os možete rotirati na bilo koji kut. Svaki node uključuje i _radial_ način rada, u kojem efekt ovisi o kutu svake točke u odnosu na središte.

* **Colour Changer by Position** – primjenjuje gradijent duž odabrane osi ili oko radijalnog kuta.\
  \&#xNAN;_Primjer: stvorite dugin gradijent koji prelazi preko linije ili upotrijebite radial način na krugu za efekt kotača boja._
* **Wave Shift by Position** – primjenjuje izobličenje sinusnim valom, pomičući sadržaj okomito (ili okomito na odabranu os).\
  \&#xNAN;_Primjer: neka linija valovito titra poput vode ili upotrijebite radial način kako bi krug pulsirao prema van iz središta._
* **Noise Shift by Position** – primjenjuje izobličenje simplex šumom, pomičući sadržaj okomito (ili okomito na odabranu os).\
  \&#xNAN;_Primjer: kao u primjeru za Wave Shift, ali s organskijim i nasumičnijim karakterom, idealno za dodavanje prirodne varijacije._

## &#x20;Promjena boje prema položaju

Ovaj node primjenjuje promjene boje na sadržaj prema položaju. Prema zadanim postavkama os je vodoravna (0°), ali možete je rotirati ili prijeći u radial način rada.

* **wavelength** – postavlja veličinu ponavljajućeg ciklusa boja.
  * _Linear način:_ pri 100% jedan puni ciklus obuhvaća punu širinu sadržaja.
  * _Radial način:_ pri 100% jedan puni ciklus obuhvaća cijeli krug (360°). Vrijednosti su postoci kruga: npr. 50% = pola kruga (180°).
* **offset** – pomiče početnu točku ciklusa boja, kao postotak wavelength vrijednosti. Možete ga modulirati (npr. pilastim oscilatorom) za glatko kruženje kroz boje.
* **repeat** – kada je omogućeno, ciklus se ponavlja preko sadržaja. Ako je onemogućeno, gradijent se primjenjuje samo jednom: sve prije početka ima početnu boju, a sve nakon kraja završnu boju.
* **pingpong** – kada je omogućeno, svako ponavljanje mijenja smjer, stvarajući zrcalni efekt. Ako je _Repeat_ onemogućen, gradijent ide naprijed pa jednom natrag. _Napomena: u Pingpong načinu wavelength obuhvaća i pomak naprijed i povratni pomak._
* **linear angle** – rotira os efekta. 0° = vodoravno.
* **radial** – prebacuje u radial način, primjenjujući boje prema kutu od središta.
* **radial smooth loop** – automatski prilagođava wavelength tako da se ravnomjerno dijeli u 100% kruga, čime se sprječava vidljiv spoj na mjestu gdje se ciklus zatvara.
* **legacy mode** – vraća se na starije početne/završne HSB klizače. Ostavite ovu opciju isključenu za upotrebu novijeg uređivača gradijenta.

**Načini boje**

Ove postavke određuju koji se aspekti prilagodbi boje primjenjuju na sadržaj. Vidi također: [Postavke boje i HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – nijansa se ne mijenja.
  * _FIXED_ – nijansa se prisilno postavlja na fiksnu vrijednost.
  * _SHIFTED_ – nijansa se pomiče za zadani iznos (elementi različitih boja ostaju međusobno različiti, ali se zajedno pomiču oko kotača boja).
* **saturation mode**
  * _OFF_ – zasićenost se ne mijenja.
  * _FIXED_ – zasićenost se postavlja na zadanu vrijednost.
* **brightness mode**
  * _OFF_ – svjetlina se ne mijenja.
  * _FIXED_ – svjetlina se postavlja na zadanu vrijednost.
  * _MULTIPLY_ – svjetlina se skalira prema zadanoj vrijednosti. Time se zadržava dinamika (npr. elementi koji bljeskaju i dalje bljeskaju, ali unutar ograničenog raspona svjetline).

**Uređivač gradijenta**

Koristi isti uređivač gradijenta kao [Colour change](colour-changer.md "mention"), ali mapira gradijent preko sadržaja prema položaju.

* Kliknite traku gradijenta za dodavanje točke boje.
* Lijevim klikom odaberite točku, zatim je povucite bočno za pomicanje.
* Povucite odabranu točku prema dolje, dalje od trake, ili pritisnite Delete/Backspace da biste je uklonili. Gradijent uvijek zadržava najmanje dvije točke.
* Desnom tipkom miša kliknite točku da biste je uredili pomoću birača boje.
* Upotrijebite **Position**, **Hue**, **Saturation** i **Brightness** za precizno uređivanje odabrane točke.
* **interpolation** odabire kako se boje stapaju između točaka:
* **HSB** – stapa nijansu, zasićenost i svjetlinu. To je najbolje za glatko kretanje u stilu duge oko kotača boja.
* **RGB** – izravno stapa vrijednosti crvene, zelene i plave. To često djeluje sličnije prijelazu boja na zaslonu ili rasvjetnoj konzoli.
* **NONE** – skače s jedne točke na sljedeću bez stapanja.
* **hue direction** dostupno je pri HSB interpolaciji:
* **AUTO** – bira najkraći put oko kotača nijansi.
* **FORWARDS** – uvijek se kreće prema naprijed kroz vrijednosti nijanse.
* **BACKWARDS** – uvijek se kreće prema natrag kroz vrijednosti nijanse.
* **blend** – miješa promjenu boje s izvornim bojama. Pri 100% efekt potpuno zamjenjuje izvorne boje.

**Naslijeđene početne / završne vrijednosti**

Ako je **legacy mode** uključen, uređivač gradijenta zamjenjuje se starijim kontrolama:

* **start hue / end hue** – nijansa na početku i kraju raspona.
* **start saturation / end saturation** – zasićenost na početku i kraju raspona.
* **start brightness / end brightness** – svjetlina na početku i kraju raspona.

**Primjer 1: Klizni dugin gradijent**

Počevši od zadanih postavki:

1. Ostavite node u **Linear** načinu (kut 0° = vodoravno).
2. Ostavite **wavelength** na 100% (obuhvaća punu širinu i to bi trebala biti zadana vrijednost).
3. Ostavite zadani gradijent.
4. Omogućite **repeat**.
5. Dodajte **Sawtooth Oscillator** na postavku **offset**, s rasponom od 0% do 100%.

***

**Primjer 2: Crno–bijelo–crni gradijent (Pingpong)**

Počevši od zadanih postavki:

1. Ostavite node u **Linear** načinu (kut 0° = vodoravno).
2. Ostavite **wavelength** na 100% (obuhvaća punu širinu i to bi trebala biti zadana vrijednost).
3. Isključite **repeat**.
4. Postavite prvu točku gradijenta na crnu.
5. Postavite završnu točku gradijenta na bijelu.
6. Postavite **hue mode** na OFF.
7. Postavite **saturation mode** na FIXED ako želite prisiliti rezultat na nijanse sive.
8. Postavite **brightness mode** na FIXED.
9. Omogućite **pingpong**.

_Rezultat: gradijent prelazi iz crne u bijelu, zatim natrag u crnu preko širine._\
Imajte na umu da, ako želite da sadržaj zadrži svoju nijansu i zasićenost, isključite Saturation mode. \\

***

**Primjer 3: Rotirajući kotač duginih boja (Radial)**

1. Omogućite **radial** način.
2. Postavite **wavelength** na 100% (puni pomak od 360°).
3. Uključite **repeat**.
4. Dodajte **Sawtooth Oscillator** na postavku **offset**, s rasponom od 0% do 100%.

_Rezultat: bešavni kotač boja koji se neprekidno rotira oko kruga._

## &#x20;Wave Shift prema položaju

Ovaj node primjenjuje valno izobličenje preko sadržaja, pomičući točke okomito na odabranu os (ili radijalno od središta).

* **Wavelength** – postavlja duljinu ciklusa vala.
  * _Linear način:_ pri 100% jedan puni ciklus obuhvaća punu širinu sadržaja.
  * _Radial način:_ pri 100% jedan puni ciklus obuhvaća punih 360°. (Vrijednosti su postoci kruga: 50% = pola okreta, 25% = četvrt okreta itd.)
* **Size** – kontrolira amplitudu vala (koliko se sadržaj pomiče).
* **Offset** – pomiče val duž osi (ili oko kruga u radial načinu). To je postotak wavelength vrijednosti, pa ga možete animirati s **Oscillator Node** kako bi se val kretao.
* **Radial** – prebacuje iz linear na radial način, tako da se pomak temelji na kutu od središta.
* **Radial Smooth Loop** – prilagođava wavelength tako da se ravnomjerno dijeli u 100% kruga, čime se sprječavaju vidljivi spojevi na mjestu zatvaranja.
* **Triangle** – mijenja oblik vala iz sinusnog u trokutasti.
* **Absolute** – uzima apsolutnu vrijednost vala, stvarajući samo pomake prema gore (presavija negativnu stranu preko pozitivne).
* **Angle** – rotira os vala. 0° = vodoravno.

## &#x20;Noise Shift prema položaju

Ovaj node izobličuje sadržaj pomoću polja šuma (poput turbulencije), pomičući točke okomito na odabranu os (ili radijalno od središta). U usporedbi s _Wave Shift_, rezultat je organskiji i nasumičniji.

* **Detail** – kontrolira finoću šuma. Veće vrijednosti = oštrije i detaljnije varijacije. Niže vrijednosti = glađe varijacije.
* **Wavelength** – postavlja skalu uzorka šuma.
  * _Linear način:_ pri 100% jedan puni ciklus šuma obuhvaća širinu sadržaja.
  * _Radial način:_ pri 100% jedan puni ciklus obuhvaća punih 360°.
* **Size** – kontrolira iznos pomaka (amplitudu izobličenja šumom).
* **Offset** – pomiče uzorak šuma duž osi (ili oko kruga). To je postotak wavelength vrijednosti, pa ga možete animirati s **Oscillator Node** kako bi šum “tekao”.
* **Depth Offset** – pomiče kroz 3D polje šuma, stvarajući varijacije tijekom vremena. To je posebno učinkovito kada se animira s Oscillator Node.
* **Depth Detail** – kontrolira koliko je detaljna varijacija kroz dimenziju dubine.
* **Absolute** – uzima apsolutnu vrijednost šuma, presavijajući negativne vrijednosti u pozitivne (stvara samo jednostrani pomak).
* **Angle** – rotira os šuma u linearnom načinu rada. 0° = vodoravno.
* **Radial** – prebacuje iz linear na radial način, tako da se pomak temelji na kutu od središta.
* **Radial Smooth Loop** – prilagođava wavelength tako da se ravnomjerno dijeli u 100% kruga, čime se sprječavaju vidljivi spojevi u radial načinu.
