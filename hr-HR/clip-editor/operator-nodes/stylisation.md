---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Stylisation nodes

## &#x20;Randomise

Stvara raspršene kopije dolaznih elemenata pomoću koherentnog polja šuma. Drugim riječima, kopira i pomiče vaše oblike i točke na kontroliran, „šumovit” način. Umjesto da sve uredno stoji na jednom mjestu, dobivate više verzija koje se pomiču i šire, poput čestica koje se kreću u toku.

* **count** – broj kopija po dolaznom elementu (1–20). Uz vrijednost 1 dobivate jednu pomaknutu verziju svakog elementa. Veće vrijednosti stvaraju više raspršenih kopija.
* **noise offset** – prolazi kroz polje šuma (0–100%). Besprijekorno se ponavlja, pa animiranje ove postavke pomoću Oscillator Node daje glatko, kontinuirano zajedničko kretanje svih kopija.
* **noise jitter** – upravlja skalom teksture šuma. Niže vrijednosti daju široku, glatku varijaciju. Više vrijednosti daju zbijeniji i nepravilniji raspored. Time se mijenja uzorak, ne jačina.
* **change between points** – upravlja time koliko se svaka kopija razlikuje od prethodne. Niske vrijednosti drže kopije grupiranima i sličnima. Visoke vrijednosti ih više razmiču i uvode veću varijaciju.
* **face direction** – rotira svaku kopiju tako da bude okrenuta u smjeru kretanja u polju šuma, što stvara strelice/čestice poravnate s tokom.
* **amount** – ukupna jačina efekta (0–100%). Skalira i pomak i rotaciju iz postavke Face direction.

{% hint style="info" %}
Randomise node je u središtu efekta Randomise!
{% endhint %}

## &#x20;Trails

Stvara odjeke vašeg sadržaja, ostavljajući iza izvornika kopije koje postupno blijede ili mijenjaju mjerilo dok se izvornik kreće.

* **change render profile for trail** – ako je uključeno, sve kopije traga koriste odabrani **render profile**. _Pogledajte_ [render profile](../fundamentals/render-profile.md "mention").
* **render profile** – profil koji se koristi za kopije traga kada je gornji prekidač uključen. Često se koristi kada je glavni sadržaj postavljen na **DETAIL**, a odjeci se renderiraju kao **FAST**. Tako dobivate jasan detalj na glavnim oblicima, dok se tragovi renderiraju učinkovitije.
* **delay** – postavlja razmak između kopija traga u glazbenom vremenu, mjereno u **koracima od 1/64 note**.\
  Za referencu:
  * 16 = 1/16 takta (šesnaestinka)
  * 32 = 1/8 takta (osminka)
  * 64 = 1/4 takta (četvrtinka)
  * 128 = 1/2 takta (polovinka)
  * 256 = 1 takt
* **trail size** – koliko se kopija traga crta iza aktivnog sadržaja.
* **prefill trails** – odmah popunjava povijest tragova kada Clip počne, umjesto da čeka da se odjeci izgrade tijekom prvih nekoliko beatova.
* **freeze trails** – pretvara glatko tekuće tragove u niz zamrznutih snimaka. Korisno za stvaranje staccato efekata traga sinkroniziranih s beatom.
* **brightness start / brightness end** – primjenjuje svjetlinu duž traga, od najnovije kopije (**start**) do najstarije kopije (**end**). Obično postavite **brightness start** na 100%, a **brightness end** na 0% i odjeci će postupno izblijedjeti.
* **scale start / scale end** – primjenjuje skaliranje duž traga, od najnovije kopije (start) do najstarije kopije (end). Za tragove koji se smanjuju do nestanka postavite **scale start** na 100%, a **scale end** na 0%.

## &#x20;Shimmer

Dodaje varijaciju svjetline nalik treperenju, od suptilnog iskrenja do intenzivnog strobiranja.

* **speed** – koliko se brzo shimmer mijenja tijekom vremena. Više vrijednosti brže trepere; 0 pauzira efekt.
* **separation** – koliko se susjedne točke/elementi međusobno razlikuju.
  * 0: sve treperi zajedno.
  * \>0: obližnje točke dobivaju postupno različite faze, pa se shimmer mijenja preko oblika.
  * <0: isto kao gore, ali napredovanje faze ide u suprotnom smjeru.
* **threshold** – umjesto glatkog blijeđenja, točke sada potpuno bljeskaju uključeno ili isključeno ovisno o svojoj svjetlini. Svjetliji elementi pale se češće, ali imajte na umu da su elementi na 100% svjetline uvijek uključeni, dok su elementi na 0% svjetline uvijek isključeni. Korisno za oštre efekte svjetlucanja ili zvjezdane svjetlosti.

{% hint style="info" %}
Uključivanje postavke **threshold** jedna je od onih sjajnih skrivenih mogućnosti koje zaista mogu oživjeti vaše čestice ili sadržaj. Umjesto blijeđenja, točke se brzo uključuju i isključuju na temelju svoje svjetline. Budući da se u bilo kojem trenutku crta manje točaka, rezultat je svjetliji izlaz i glađa animacija.

No imajte na umu da, ako je vaš sadržaj već na 100% svjetline, neće se dogoditi ništa!
{% endhint %}

* **use whole shape** – primjenjuje jednu vrijednost shimmera jednoliko na cijeli oblik. Kada je isključeno, node dijeli oblike tako da različiti dijelovi mogu treperiti neovisno, za točkasti izgled.

## &#x20;Particles

Ovo je eksperimentalni efekt koji stvara i animira čestice na temelju vašeg sadržaja. Svi elementi temeljeni na točkama koji ulaze u efekt tretiraju se kao položaji emitera. Budući da se putanje čestica unaprijed izračunavaju, ako se ulazni sadržaj promijeni možda ćete trebati osvježiti/ponovno izračunati čestice kako bi se ažurirale (samo promijenite bilo koju od postavki).

**General**

* **keep original** – ako je uključeno, izvorni sadržaj se zadržava i čestice se dodaju povrh njega. Korisno kada želite da točke emitera ostanu vidljive.
* **number of particles** – koliko se čestica stvara po emisiji. Više vrijednosti daju gušće efekte, niže vrijednosti daju minimalniji izgled.
* **emission period** – raspon petlje (u taktovima) tijekom kojeg se čestice emitiraju. Na 100% ravnomjerno su raspoređene kroz petlju; manje vrijednosti ih zbijaju u skupine za burst efekte.
* **loop length** – koliko dugo traje petlja čestica, mjereno u glazbenim taktovima.
* **loop count** – koliko se puta petlja ponavlja prije resetiranja. Ako je postavljeno na 1, čestice će svaki put pratiti potpuno istu simulaciju, pa je rezultat savršeno ponovljiv. Veće vrijednosti uvode više varijacije prije resetiranja ciklusa.
* **delay** – pomiče vrijeme početka emisije za određeni broj 1/64 nota, za vremenske efekte.

**Motion**

* **speed** – koliko se brzo čestice udaljavaju od emitera.
* **speed variation** – dodaje nasumičnost tako da se čestice ne kreću sve istom brzinom. Stvara prirodnije širenje.
* **direction** – postavlja osnovni smjer u kojem se čestice ispaljuju, definiran pomoću **x, y, z kutova**. Ti kutovi rotiraju vektor ispaljivanja u 3D prostoru, tako da čestice možete usmjeriti ravno gore, u stranu ili po bilo kojoj dijagonali. Kombinirajte s postavkom **spread** za šire stošce ili kaotičnije burst efekte.

{% hint style="info" %}
**Eulerovi kutovi**\
Liberation koristi **Eulerove kutove** za opis orijentacije u 3D prostoru. To su jednostavno rotacije oko tri glavne osi:

* **X** – nagib naprijed/natrag (kao kimanje glavom)
* **Y** – okret lijevo/desno (kao odmahivanje glavom za „ne”)
* **Z** – zakret u smjeru kazaljke na satu / suprotno od smjera kazaljke na satu (kao naginjanje glave u stranu)

Podešavanjem ove tri vrijednosti možete usmjeriti čestice u bilo kojem smjeru.
{% endhint %}

* **direction variation** – dodaje nasumično širenje oko tog smjera. Korisno za stvaranje stožaca, mlazova ili eksplozija.
* **drag** – usporava čestice tijekom vremena. Više vrijednosti čine ih težima i tromijima.
* **gravity** – vuče čestice prema dolje (pozitivno) ili ih gura prema gore (negativno).
* **gravity variation** – dodaje varijaciju gravitacije po čestici, čineći kretanje kaotičnijim.

**Life**

* **life duration** – koliko dugo čestice postoje (mjereno u jedinicama od 1/64 note). S kraćim vrijednostima čestice brzo nestaju, dok s duljim vrijednostima ostaju vidljive dulje vrijeme.
* **life variation** – dodaje nasumičnost trajanju čestica tako da ne nestanu sve odjednom.
* **start delay / start delay variation** – odgađa trenutak kada svaka čestica postaje vidljiva (u koracima od 1/64 note). Čestica je već stvorena i kreće se tijekom tog razdoblja, ali joj se svjetlina drži na 0, pa ostaje nevidljiva dok odgoda ne istekne. Korisno je ako želite da se odgođene vatrometne „iskrice” pojave kasnije.

**Colour & brightness**

* **hue start** – početna boja čestica.
* **hue variation** – dodaje nasumičnost tako da sve čestice ne počinju istom bojom.
* **hue change** – pomiče nijansu tijekom životnog vijeka čestice, stvarajući tragove koji mijenjaju boju.
* **brightness start / brightness end** – primjenjuje svjetlinu kroz životni vijek čestice. Obično postavite brightness start visoko, a brightness end nisko kako bi prirodno izblijedjele.
* **brightness variation** – nasumično mijenja početnu svjetlinu za dinamičniji izgled.
* **saturation start / saturation end** – postavlja koliko je boja živa na početku i na kraju.
* **saturation variation** – nasumično mijenja zasićenost radi varijacije među česticama.

**Simulation**

* **time adjustment** – ubrzava ili usporava cijelu simulaciju čestica. Korisno za sinkronizaciju s različitim tempima ili za naglašavanje kretanja.
