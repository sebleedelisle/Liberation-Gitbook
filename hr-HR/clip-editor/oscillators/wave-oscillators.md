---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Valni oscilatori

## Na ovoj stranici:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Pilasti val](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Trokutasti val](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sinusni val](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Kvadratni val](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Šum](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Prilagođeni oscilator](wave-oscillators.md#custom-oscillator-1)

## Postavke valnog oscilatora

Svi valni oscilatori imaju sljedeće postavke:

* **range min / range max** - određuje raspon vrijednosti za svojstvo kojim oscilator upravlja. Svojstvo se postavlja na _range min_ kada je valni oblik na dnu, a na _range max_ kada je valni oblik na vrhu.

{% hint style="info" %}
Na primjer, ako želite da se točka pomiče lijevo-desno između -100 i 100, spojite oscilator na _x property socket_, postavite _min range_ na -100 i _max range_ na 100.
{% endhint %}

* **duration** - vrijeme potrebno da se završi jedan puni ciklus (ili _loop_). Vrijednost je relativna u odnosu na tempo u taktovima. Dakle, ¼ je jedan beat. 1 je cijeli takt itd.
* **duration multiplier** - skalira osnovno trajanje odabranim faktorom. Na primjer, ako je duration postavljen na četvrtinku, a multiplier na 3, oscilator će trajati tri četvrtinke (točkastu polovinku). Podržani su i razlomljeni množitelji — držite _SHIFT_ dok povlačite klizač kako biste postavili necjelobrojne vrijednosti, što je korisno za fazne efekte ili stvaranje suptilnih pomaka u tajmingu.
* **offset** - početni pomak vala kao postotak trajanja. Ako želite da val počne od četvrtine svog trajanja, postavite ovo na 25%.
* **repeat count** - broj ponavljanja loopa prije nego što se zaustavi. Zadana vrijednost je _FOREVER_, ali možete je promijeniti ako ne želite da oscilator radi neograničeno. Nakon zaustavljanja, svojstvo će se postaviti na vrijednost na kraju vala.
* **delay count** - odgoda u beatovima prije nego što se oscilator pokrene. Prije pokretanja, svojstvo će biti postavljeno na vrijednost na početku vala.

{% hint style="info" %}
Pažljivom upotrebom _repeat count_ i _delay count_ možete izraditi vrlo složene animacije, gotovo kao vlastiti timeline!
{% endhint %}

## Zajedničke postavke

* **steps** - dijeli kretanje na određeni broj diskretnih koraka. Korisno kada želite da svojstva „skaču” na vrijednosti umjesto da se glatko kreću.

{% hint style="info" %}
Imajte na umu da se koraci dijele po vremenu, a ne po vrijednosti. Dakle, za val podijeljen na 4 koraka s trajanjem od 1 takta, svojstvo će se trenutačno promijeniti na svaki beat.
{% endhint %}

* **clamp min / clamp max -** povećava skalu vala izvan njegovih minimalnih ili maksimalnih vrijednosti i ograničava rezultat.

{% hint style="info" %}
Koncept _clamp_ prilično je teško objasniti, ali zamislite da valni oblik izlazi izvan vrha ili dna grafa, a zatim se „prikvači” na rubove. Preporučujem da eksperimentirate s tim postavkama! Vrlo su korisne ako želite da pilasti val počne kasnije ili završi ranije.
{% endhint %}

* **ease function** - pilasti i trokutasti val također imaju ease function, koja suptilno mijenja krivulju animacije i može animacije učiniti mnogo izražajnijima!
  * **LINEAR** - zadano, bez easing efekta; samo se linearno pomiče između minimalne i maksimalne vrijednosti.
* **EASE OUT** - počinje brzo, a zatim usporava kako se približava kraju. Vrlo dobro za simulaciju fizike, npr. usporavanje do zaustavljanja.
  * **EASE IN** - počinje polako i postupno ubrzava. Dobro za simulaciju nakupljanja zamaha.
  * **EASE IN/OUT** - kombinacija oba pristupa, s vrlo organskim kretanjem.

{% hint style="warning" %}
**Easing -** Preporučujem da izbjegavate zadanu linearnu animaciju kad god možete, osim ako posebno želite robotski izgled. Easing može učiniti animacije mnogo fluidnijima i organskijima!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Pilasti val

Ponekad se naziva i _ramp waveform_ jer se penje prema gore, a zatim naglo pada na kraju ciklusa. Vjerojatno je najčešći valni oscilator jer stvara loop za kruženje svojstava poput _hue_ ili _rotation_.

Pogledajte gornje odjeljke za:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Specifično za pilasti val:

* **cycle range compensation** - dostupno kada je postavljen **steps** i korisno je za kruženje vrijednosti, primjerice rotaciju od 0 do 360. Kada ovo nije uključeno, početna i završna vrijednost bit će iste, što može uzrokovati zastajkivanje na početnoj točki (jer su 0 i 360 isti kut). Uključite ovu opciju i maksimalni raspon bit će smanjen kako bi se ispravili položaji koraka.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Trokutasti val

Za razliku od _pilastog vala_, koji se svakim ciklusom vraća skokom na početak, _trokutasti val_ kreće se linearno naprijed, a zatim natrag.

Pogledajte gornje odjeljke za:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sinusni val

Najglađi valni oblik! Nježno oscilira između dvije vrijednosti poput njihala.

Pogledajte gornje odjeljke za:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Kvadratni val

Najjednostavniji valni oblik - samo se prebacuje između dvije vrijednosti, naprijed-natrag!

Pogledajte gornje odjeljke za:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Specifično za kvadratni val:

* **pulse width** - vrijeme tijekom kojeg je val na maksimalnoj vrijednosti u odnosu na ukupno trajanje. 50% je zadano, što je točno pola-pola. Ako želite da bude „uključen” samo četvrtinu vremena, postavite na 25%. Kada se taj puls događa možete prilagoditi pomoću vrijednosti _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Šum

Jedna od prednosti Liberationa jest to što može generirati nasumične, ali ponovljive efekte. Oscilator _noise_ može se upotrijebiti za stvaranje organskog, loopanog nasumičnog kretanja s onoliko detalja/treperenja koliko želite.

Pogledajte gornje odjeljke za:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Specifično za šum:

* **noise type** - algoritam koji se koristi za generiranje šuma.
  * **SIMPLEX** - zadano, valovita vrijednost koja raste i opada te se ponavlja u loopu.
  * **RANDOM** - koristi tradicionalniji algoritam nasumičnih brojeva; potpuno šumno i kaotično.

{% hint style="info" %}
**Simplex noise** osmislio je Ken Perlin 2001. godine kao poboljšanje svojeg algoritma „Perlin noise”, koji je razvio 1983. kao dio rada na filmu _Tron_ (za koji je osvojio Oscar!)

Taj takozvani „gradijentni” šum nastao je iz njegove frustracije dotadašnjim, „strojolikim” računalno generiranim slikama. U svijetu CGI-ja posebno je dobar za renderiranje oblaka, vodenih površina ili čak visinskih mapa za realističan teren.

No u Liberationu je koristan za naizgled nepredvidljivo kretanje koje je i dalje glatko i organsko.
{% endhint %}

* **seed** - vrijednost koja se koristi za stvaranje šuma. Ako vam se ne sviđa izgled vala šuma koji imate, pokušajte promijeniti ovu vrijednost.

{% hint style="info" %}
Zabavna štreberska činjenica! Kako bih dobio savršeno loopani simplex noise, iteriram oko kruga na 2D ravnini šuma. A promjena vrijednosti seed pomiče tu ravninu kroz treću dimenziju!
{% endhint %}

* **simplex detail** - mijenja koliko je šum detaljan ili treperav. Ako želite da ponavljajući uzorak bude manje očit, povećajte duration i ovu vrijednost.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Prilagođeni oscilator

Stvara potpuno prilagođene valne oblike. To je vrlo korisno za izradu složenih animacija.

Pogledajte gornje odjeljke za:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Ispod toga nalazi se popis položaja i vrijednosti. Trajanje je podijeljeno na 64 koraka i vrijednost možete postaviti na bilo koju od tih točaka.

Svaki korak ima sljedeće postavke:

* **Step** - vremenski korak unutar trajanja. 0 je na početku, a 64 je na kraju.
* **Level** - razina vala u tom vremenskom koraku. Razina je u rasponu od 0 do 1.
* **Animation type** - padajući izbornik omogućuje odabir načina na koji se želite kretati prema ovoj razini iz prethodnog koraka.
  * **None** - bez prijelaza; samo izravno skoči na ovu razinu u zadanom trenutku.
  * **Linear** - potpuno linearno kretanje s prethodne razine na ovu.
  * **Ease in / Ease out / Ease in/out** - primjenjuje easing između prethodne razine i ove. Pogledajte gore opis _ease function_ za objašnjenje vrsta animacije.

***
