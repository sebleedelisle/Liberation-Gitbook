---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Svæði

Helsta gerð svæðis sem þú notar í flestum verkefnum er _Beam zone_. Þetta svæði er hannað fyrir geislaáhrif í lofti. Hin gerðin er _Canvas zone_ (Sjá [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**VIÐVÖRUN - Farðu mjög varlega þegar þú færir svæði á meðan laserinn er í gangi** og lækkaðu birtuna eins mikið og hægt er. Sjá [setting-up-lasers.md](../setting-up/setting-up-lasers.md) fyrir ítarlega leiðbeiningu um hvernig á að virkja lasera og skilgreina svæði á öruggan hátt.
{% endhint %}

Þú getur smellt á svæðin og dregið þau til með músinni. Kveiktu á test pattern til að sjá hvert svæðið fer.

{% hint style="info" %}
Notaðu örvatakkana til að **færa smám saman** valið svæði/punkt. Haltu `Shift` inni til að færa í stærri skrefum.
{% endhint %}

{% hint style="info" %}
Gott ráð: þú getur afritað stillingar svæða fljótt yfir á marga lasera! Sjá [copy-laser-settings.md](../setting-up/copy-laser-settings.md)
{% endhint %}

### Bæta við nýju beam zone

Smelltu á _Add a new beam zone_ hnappinn efst á tækjastikunni og nýtt svæði birtist. Athugaðu að beam zones raðast í þeirri röð sem þú bætir þeim við, en þú getur breytt röðinni. Sjá [re-ordering-beam-zones.md](re-ordering-beam-zones.md)

### Bæta við fyrirliggjandi canvas zone

Smelltu á _Add existing canvas zone_ hnappinn og þá sérðu lista yfir tiltæk canvas zones sem þú getur kveikt eða slökkt á fyrir þennan laser. Sjá [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/)

### Formgerðir svæða

Það eru 3 formgerðir svæða:

* **Quad** - sjálfgefna rétthyrnda svæðisformið, sem getur verið reglulegt (samhliða ásum) eða aflagað. Hentar best fyrir stærri rétthyrnd svæði eða canvas zones sem þurfa sjónarhornsleiðréttingu.
* **Line/Curve** - svæði skilgreint með 2 eða fleiri punktum og þykkt. Tilvalið fyrir mjó svæði eða til að enda á svölum, brúm eða öðrum bogadregnum formum.
* **Segmented** - svæði sem má skipta niður í minni quads. Tilvalið fyrir vörpun á arkitektúr.

Hægrismelltu á hvaða svæði sem er til að opna stillingar þess. Í þessari hægrismellsvalmynd geturðu:

* Endurnefnt svæðið (þetta getur hjálpað við að þekkja það í Clip Deck, sérstaklega ef þú ert með mörg svæði!)
* Kveikt eða slökkt á svæðinu
* Læst staðsetningu þess
* Breytt formgerð þess
* Endurstillt það á sjálfgefna staðsetningu
* Opnað stillingar sem eiga sérstaklega við formgerðina
* Eytt því
* Bætt við _Alt Zone_ (Sjá [alt-zone-system.md](alt-zone-system.md))

{% hint style="danger" %}
**VIÐVÖRUN -** farðu mjög varlega þegar þú breytir gerð svæðis á meðan laserinn er virkur. Svæðið fer aftur í síðustu staðsetningu / stærð fyrir það form, þannig að úttakið getur breyst skyndilega. Best er að slökkva á lasernum áður en þú breytir gerð svæðisins.
{% endhint %}

### Quad svæðisform

Þú getur fært hvert horn á quad með músinni. `Alt / Option`-smelltu á horn til að færa það óháð hinum og aflaga quad. Þegar quad hefur verið aflagað er hægt að færa öll hornin frjálslega.

Þú getur fjarlægt aflögunina og breytt því aftur í rétthyrning sem er samhliða ásum með _REMOVE DISTORTION_ hnappnum í hægrismellsvalmyndinni.

#### Sjónarhornsleiðrétting

Þennan valkost má stilla með rofanum í hægrismellsvalmyndinni og hann ákvarðar aðferðina við aflögun. Best er að hafa þetta slökkt fyrir geisla, en ef þetta svæði varpar grafík á flatan flöt skaltu kveikja á þessu og úttakið verður leiðrétt fyrir sjónarhorn.

{% hint style="info" %}
Ef slökkt er á _Perspective correction_ er efnið aflagað með _bi-linear interpolation_. Með öðrum orðum dreifist efnið jafnt yfir quad. Þess vegna hentar þetta best fyrir geisla.

Þegar kveikt er á perspective correction er efnið aflagað með sjónarhornsvörpun sem leiðréttir fyrir styttingu vegna sjónarhorns. Ef þú ert til dæmis að varpa grafík á vegg frá skáu horni geturðu notað þetta til að leiðrétta úttakið og laga vörpunaraflögunina.
{% endhint %}

### Line / Curve svæðisform

Line / Curve svæðisformið hefur orðið mitt helsta val í nýlegum sýningum, og það mætti færa rök fyrir því að þetta ætti að vera sjálfgefið fyrir beam zones.

Oftar en ekki þurfa svæðin mín að vera mjó til að passa í þröng og erfið rými á sýningarstöðum eða á milli glugga á byggingum. Ég komst að því að það gat verið mjög vandasamt að stilla fjögur horn á quad þegar þau eru svona nálægt hvert öðru. Þannig varð Line / Curve svæðið til!

Fyrir beinar línur þarftu aðeins tvo punkta og stillir svo _Zone thickness_ í hægrismellsvalmyndinni. Þetta er fljótlegasta leiðin til að búa til einföld svæði.

`Alt / Option`-smelltu á línuna til að búa til fleiri punkta. Þessir punktar eru sjálfkrafa mýktir til að mynda flæðandi form og þú getur stillt _Smooth level_ til að jafna út beygjur eða hnykki.

`Alt / Option`-smelltu á punkt til að eyða honum.

Ef þú hefur reynslu af vektorforritum (Inkscape, Illustrator o.s.frv.) geturðu líka notað _Manually adjust bezier curves_ valkostinn til að fá nákvæma stjórn á öllum stýripunktum.

### Segmented svæðisform

Þetta niðurskipta svæði gerir þér kleift að gera mjög nákvæmar leiðréttingar og nýtist vel þegar þú ert að varpa á flókin form. Þú getur bætt við eða fjarlægt undirskiptingar með + og - hnöppunum í hægrismellsvalmyndinni.

### Hvernig á að breyta svæði sem er alveg hulið af öðru svæði

Hægrismelltu á svæðið sem er ofan á og smelltu á hengiláshnappinn til að læsa því. Nú ættirðu að geta breytt og stillt svæðið fyrir neðan.

<br>

{% hint style="info" %}
Þegar þú bætir Beam zone við úttakið þitt verður það tiltækt til að bæta við Clip í Clip Deck.
{% endhint %}
