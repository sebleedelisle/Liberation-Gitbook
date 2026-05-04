---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Sú gerð zone sem þú notar í flestum verkefnum er _Beam zone_. Þetta er zone sem er hönnuð fyrir beam-áhrif í lofti. Hin gerðin er _Canvas zone_ (sjá [Grafík og Canvas-kerfið](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**VIÐVÖRUN - Farðu mjög varlega þegar þú færir zones á meðan leysirinn er í gangi** og lækkaðu birtustigið eins mikið og hægt er. Sjá [Uppsetning leysigeisla](../setting-up/setting-up-lasers.md "mention") fyrir ítarlega leiðbeiningu um hvernig á að virkja og stilla zones fyrir leysigeisla á öruggan hátt.
{% endhint %}

Þú getur smellt og dregið zones til með músinni. Kveiktu á test pattern til að sjá hvert viðkomandi zone fer.

{% hint style="info" %}
Notaðu örvatakkana til að **færa** valið zone eða punkt örlítið. Haltu `Shift` inni til að færa í stærri skrefum.
{% endhint %}

{% hint style="info" %}
Gott ráð: þú getur afritað zone-stillingar hratt yfir á marga leysigeisla! Sjá [Afrita Laser Settings](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Bæta við nýju beam zone

Smelltu á _Add a new beam zone_ hnappinn efst á tækjastikunni og nýtt zone birtist. Athugaðu að beam zones raðast í þeirri röð sem þú bætir þeim við, en þú getur breytt röðinni. Sjá [Endurraða beam zones](re-ordering-beam-zones.md "mention")

### Bæta við fyrirliggjandi canvas zone

Smelltu á _Add existing canvas zone_ hnappinn og þá sérðu lista yfir tiltæk canvas zones. Þar geturðu kveikt og slökkt á þeim fyrir þennan leysi. Sjá [Grafík og Canvas-kerfið](../graphics-and-the-canvas-system/ "mention")

### Gerðir zone-forma

Það eru 3 gerðir zone-forma:

* **Quad** - sjálfgefna ferhyrnda zone-formið, sem getur verið reglulegt (samhliða ásum) eða afmyndað. Best fyrir stærri ferhyrnd zones eða canvas zones sem þurfa leiðréttingu á sjónarhorni.
* **Line/Curve** - zone sem er skilgreind með 2 eða fleiri punktum og þykkt. Hentar vel fyrir mjó zones eða til að afmarka á svölum, brúm eða öðrum bognum formum.
* **Segmented** - zone sem má skipta niður í smærri quads. Hentar vel fyrir architectural mapping.

Hægrismelltu á hvaða zone sem er til að opna stillingarnar. Í þessari hægrismellsvalmynd geturðu:

* Endurnefnt zone-ið (þetta getur hjálpað til við að þekkja það í Clip Deck, sérstaklega ef þú ert með mörg zones!)
* Virkjað/slökkt á zone-inu
* Læst staðsetningu þess
* Breytt formgerð þess
* Endurstillt það í sjálfgefna staðsetningu
* Opnað stillingar sem eiga sérstaklega við formgerðina
* Eytt því
* Bætt við _Alt Zone_ (sjá [Alt Zone-kerfið](alt-zone-system.md "mention"))

{% hint style="danger" %}
**VIÐVÖRUN -** farðu mjög varlega þegar þú breytir zone-gerð á meðan leysirinn er virkur. Zone-ið fer aftur í síðustu staðsetningu/stærð fyrir það form, þannig að úttakið gæti breyst skyndilega. Best er að slökkva á leysinum áður en þú breytir zone-gerðinni.
{% endhint %}

### Quad zone-form

Þú getur fært hvert horn í quad með músinni. `Alt / Option`-smelltu á horn til að færa það óháð hinum hornunum og afmynda quad. Þegar quad hefur verið afmyndað er hægt að færa öll hornin frjálst.

Þú getur fjarlægt afmyndunina og sett formið aftur í rétthyrning sem er samsíða ásum með _REMOVE DISTORTION_ hnappinum í hægrismellsvalmyndinni.

#### Leiðrétting á sjónarhorni

Þessi valkostur er stilltur með rofanum í hægrismellsvalmyndinni og hann ræður afmyndunaraðferðinni. Best er að hafa þetta slökkt fyrir beams, en ef þetta zone varpar grafík á flatan flöt skaltu kveikja á þessu svo úttakið verði leiðrétt fyrir sjónarhorni.

{% hint style="info" %}
Ef slökkt er á _Perspective correction_ er efni afmyndað með _bi-linear interpolation_. Með öðrum orðum er efni dreift jafnt yfir quad. Þess vegna hentar þetta best fyrir beams.

Þegar kveikt er á perspective correction er efni afmyndað með perspective warping, sem leiðréttir fyrir styttingu vegna sjónarhorns. Ef þú ert til dæmis að varpa grafík á vegg undir skáhorni geturðu notað þetta til að leiðrétta úttakið og laga afmyndunina í vörpuninni.
{% endhint %}

### Line / Curve zone-form

Line / Curve zone-formið hefur orðið það sem ég nota helst í nýlegum sýningum, og það má alveg færa rök fyrir því að þetta ætti að vera sjálfgefið fyrir beam zones.

Oftast þurfa zones hjá mér að vera mjó til að passa inn í erfið, mjó rými á viðburðastöðum eða á milli glugga á byggingum. Mér fannst geta verið mjög vandasamt að stilla fjögur horn á quad þegar þau eru svona þétt saman. Þannig varð Line / Curve zone til!

Fyrir beinar línur þarftu bara tvo punkta og stillir síðan _Zone thickness_ í hægrismellsvalmyndinni. Þetta er fljótlegasta leiðin til að búa til einföld zones.

`Alt / Option`-smelltu á línuna til að búa til fleiri punkta. Þessir punktar eru sjálfkrafa mýktir til að búa til flæðandi form og þú getur stillt _Smooth level_ til að slétta út ójöfnur.

`Alt / Option`-smelltu á punkt til að eyða honum.

Ef þú hefur reynslu af vektorforritum (Inkscape, Illustrator o.s.frv.) geturðu líka notað _Manually adjust bezier curves_ til að fá nákvæma stjórn á öllum stýripunktum.

### Segmented zone-form

Þetta niðurskipta zone gerir þér kleift að gera mjög nákvæmar leiðréttingar og nýtist vel þegar þú ert að map-a á flókin form. Þú getur bætt við eða fjarlægt skiptingar með + og - hnöppunum í hægrismellsvalmyndinni.

### Hvernig á að breyta zone sem er alveg hulið af öðru zone

Hægrismelltu á zone-ið sem er ofan á og smelltu á hengiláshnappinn til að læsa því. Þá ættirðu að geta breytt og stillt zone-ið sem er undir.

<br>

{% hint style="info" %}
Þegar þú bætir Beam zone við Output verður það tiltækt til að bæta við Clip í Clip Deck.
{% endhint %}
