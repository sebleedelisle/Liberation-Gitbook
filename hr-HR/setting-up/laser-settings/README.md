# ✅ Ploča s postavkama laserskog izlaza

Otvorite ploču s postavkama _Laser output_ putem izbornika _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Prikazat će se postavke trenutačno odabranog lasera, koje možete mijenjati:

* preko gumba s njegovim brojem u ploči _Laser Overview_
* tipkom s brojem na tipkovnici; tipke 1 do 0 otvaraju lasere 1 - 10
* tipkom `Tab` za kruženje kroz lasere (`Shift + Tab` ide unatrag).

Na vrhu ove ploče vidjet ćete:

* gumb s brojem - kliknite ga da biste omogućili ili onemogućili izlaz ovog lasera. Gumb je crven kada je izlaz lasera omogućen.
* klizač _Brightness_ samo za ovaj laser. Imajte na umu da se ta vrijednost kombinira s postavkom Global Brightness.
* prekidač _Test Pattern_ i birač uzorka. Time možete odabrati poseban testni uzorak samo za ovaj laser. (Te su kontrole zrcaljene u alatnoj traci Output view.)

### Korekcija orijentacije izlaza / zrcaljenja

Sljedeći elementi služe za ispravljanje podešenja lasera kako bi se dosljedno ponašao u Liberation.

* **Flip horizontal / vertical** - ove opcije omogućuju korekciju izlaza lasera

{% hint style="info" %}
Ne biste trebali mijenjati postavke Flip horizontal / vertical osim ako je laser pogrešno ožičen ili na stražnjoj strani ima gumbe za X/Y zrcaljenje koji nisu pravilno postavljeni. Ako za određeni Clip želite zrcaljen izlaz, to možete podesiti izravno na tom elementu.
{% endhint %}

* **Orientation** - ako je laser montiran bočno ili naopako, ovom postavkom možete ispraviti rotaciju.
* **Fine position adjustments** - mogu se koristiti za korekciju vrlo malih pomaka ili rotacije. Namijenjeno za korekciju pomaka ili slijeganja ako je laser ostavljen preko noći ili dulje vrijeme.

{% hint style="info" %}
Imajte na umu da korekcije orijentacije i zrcaljenja ne mijenjaju ništa u prikazu 3D Visualiser. Treba ih koristiti za usklađivanje izlaza stvarnog lasera s onime što se prikazuje u 3D Visualiser!
{% endhint %}

### Kopiranje postavki lasera

Pogledajte [Kopiranje postavki lasera](./#copy-laser-settings).

### Postavke skenera

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Postavka Speed određuje koliko se brzo skeneri pomiču.

{% hint style="danger" %}
Iako su zadane postavke prilično konzervativne, skenere i dalje možete oštetiti ako ih pogonite prebrzo. Budite oprezni, posebno pri povećavanju brzine.
{% endhint %}

{% hint style="info" %}
Ova postavka brzine ne mijenja frekvenciju točaka, nego podešava koliko su te točke razmaknute. Za više informacija pogledajte [Kako Liberation generira laserski sadržaj](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Snop mijenja boju te se uključuje i isključuje dok ga skeneri pomiču, a te dvije stvari obično nisu savršeno sinkronizirane. Podesite ovu postavku kako biste ih ponovno uskladili.

{% hint style="info" %}
Ovo se ponekad naziva _blank shift_, ali osobno mi je draži naziv _scanner sync_ - malo je točniji jer podešava vremensko usklađenje svih promjena boje u odnosu na kretanje skenera.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laserski „repovi” - Colour shift nije pravilno podešen</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Nema laserskih „repova”! Colour shift je dobro podešen!</p></figcaption></figure></div>

Ako na laserskom izlazu vidite male „repove”, vjerojatno treba podesiti scanner sync. Ako se repovi i dalje pojavljuju bez obzira na postavku, vjerojatno pogonite skenere ili upravljačke sklopove lasera brže nego što mogu podnijeti. Pokušajte smanjiti brzinu skenera.

#### Preseti skenera

Ovom postavkom odaberite unaprijed pripremljenu postavku skenera. Zadana opcija obično je sasvim u redu, pa ovu postavku ne biste trebali mijenjati osim ako imate posebno loše (ili dobre) skenere. Ako želite detaljnije istražiti, pogledajte [Preseti skenera](../../advanced/scanner-presets.md)

#### Kalibracija boja

Ovaj sustav možete koristiti za korekciju krivulje svjetline i balansa bijele boje lasera. Pogledajte [Kalibracija boja](../../advanced/colour-calibration.md)

#### Napredne postavke

Ne biste trebali mijenjati ove postavke, ali ako vas zanima više, pogledajte [Napredne postavke lasera](../../advanced/advanced-laser-settings.md)
