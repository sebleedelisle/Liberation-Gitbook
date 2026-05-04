---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Panel postavki za izlaz lasera

Otvorite panel postavki _Laser output_ putem izbornika _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Prikazat će se postavke trenutačno odabranog lasera, koje možete promijeniti:

* putem gumba s njegovim brojem u panelu _Laser overview_
* brojčanom tipkom na tipkovnici; tipke 1 do 0 otvaraju lasere 1 – 10
* tipkom `Tab` za kruženje kroz lasere (`Shift + Tab` ide unatrag).

Na vrhu ovog panela vidjet ćete:

* gumb s brojem — kliknite ga da biste aktivirali/deaktivirali ovaj laser. Crven je kada je laser aktiviran.
* klizač _Brightness_ samo za ovaj laser. Imajte na umu da se kombinira s globalnom svjetlinom.
* prekidač _Test Pattern_ i odabir uzorka. To vam omogućuje odabir određenog testnog uzorka samo za ovaj laser. (Ove kontrole zrcale se u alatnoj traci Output view.)

### Ispravak orijentacije izlaza / zrcaljenja

Sljedeći elementi služe za ispravljanje postavljanja lasera kako bi se u Liberation ponašao dosljedno.

* **Flip horizontal / vertical** — ove opcije omogućuju ispravak izlaza vašeg lasera

{% hint style="info" %}
Postavke za horizontalno/vertikalno okretanje ne biste trebali mijenjati osim ako je laser neispravno ožičen ili na stražnjoj strani ima X/Y gumbe za okretanje koji nisu pravilno postavljeni. Ako želite okrenuti izlaz za određeni Clip, to možete napraviti na samom Clipu.
{% endhint %}

* **Orientation** — ako je laser montiran bočno ili naopako, ovom postavkom možete ispraviti rotaciju.
* **Fine position adjustments** — mogu se upotrijebiti za ispravljanje vrlo malih pomaka/rotacije. Namijenjeno za ispravak pomaka ili slijeganja ako je laser ostavljen preko noći ili dulje vrijeme.

{% hint style="info" %}
Imajte na umu da ispravci orijentacije/zrcaljenja ne mijenjaju ništa u 3D Visualiseru; trebaju se koristiti za usklađivanje izlaza stvarnog lasera s onim što je prikazano u 3D Visualiseru!
{% endhint %}

### Kopiranje postavki lasera

Pogledajte [Kopiranje postavki lasera](laser-settings.md#copy-laser-settings "mention").

### Postavke skenera

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Postavka Speed određuje koliko se brzo skeneri pomiču.

{% hint style="danger" %}
Iako su zadane postavke prilično konzervativne, skenere i dalje možete oštetiti ako ih pokrećete prebrzo. Budite oprezni, osobito pri povećavanju brzine.
{% endhint %}

{% hint style="info" %}
Ova postavka brzine ne mijenja učestalost točaka, nego podešava koliko su te točke razmaknute. Za više informacija pogledajte [Kako Liberation generira laserski sadržaj](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (pomak boje / blank shift)**

Snop mijenja boju te se uključuje i isključuje dok ga skeneri pomiču, a te dvije stvari obično nisu savršeno sinkronizirane. Podesite ovu postavku kako biste ih ponovno uskladili.

{% hint style="info" %}
Ovo se ponekad naziva _blank shift_, ali osobno više volim izraz _scanner sync_ — malo je precizniji jer podešava vremensko usklađivanje svih promjena boje u odnosu na kretanje skenera.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laserski „repovi” — pomak boje nije pravilno podešen</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Nema laserskih „repova”! Pomak boje je dobar!</p></figcaption></figure></div>

Ako na izlazu lasera vidite male „repove”, vjerojatno je potrebno podesiti scanner sync. Ako se repovi i dalje pojavljuju bez obzira na podešavanje, vjerojatno skenere ili upravljačke sklopove lasera pokrećete brže nego što mogu podnijeti. Pokušajte smanjiti brzinu skenera.

#### Unaprijed definirane postavke skenera

Ovdje odaberite unaprijed pripremljenu postavku skenera. Zadana opcija obično je u redu, pa ovu postavku ne biste trebali mijenjati osim ako imate posebno loše (ili dobre) skenere. Ako želite ići dublje, pogledajte [Unaprijed definirane postavke skenera](../advanced/scanner-presets.md "mention")

#### Kalibracija boja

Ovim sustavom možete ispraviti krivulju svjetline i balans bijele boje vašeg lasera. Pogledajte [Kalibracija boja](../advanced/colour-calibration.md "mention")

#### Napredne postavke

Ne biste se trebali morati baviti ovim postavkama, ali ako vas zanima, pogledajte [Napredne postavke lasera](../advanced/advanced-laser-settings.md "mention")
