---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Pregled sustava Canvas

Sustav Canvas u Liberation relativno je jednostavan, ali u početku može biti zbunjujuć. Ovo je konceptualni pregled koji će vam pomoći da krenete.

{% hint style="info" %}
**Čekajte, trebam li uopće sustav Canvas?**

Možda ne! Ako samo projicirate jednu grafiku na jedan laser, to možete jednostavno napraviti pomoću beam zone (iako je sadržaj u beam zone prema zadanim postavkama zrcaljen vodoravno, pa ćete na Clip morati primijeniti X flip).

No ako želite rasporediti grafički sadržaj na više od jednog lasera ili ga podijeliti u različite dijelove za mapiranje na arhitekturu, sustav Canvas je pravo rješenje.
{% endhint %}

### Canvas

Prije svega, tu je sam Canvas. To je ono što vidite u prikazu _CANVAS_ i predstavlja veliko, pa, platno na kojem možete crtati sadržaj bilo gdje unutar tog prostora.

### Ciljna područja Canvas

Ona su u Canvas view prikazana kao plavi obrisi pravokutnika, a predstavljaju područja u koja možete slati sadržaj. Sadržaj iz Clip šaljete u ciljno područje Canvas na isti način na koji biste Clip poslali u beam zone. Gumbe za ciljna područja Canvas vidjet ćete desno od gumba za beam zone u Clip Deck.

{% hint style="info" %}
Ako u Clip Deck ne vidite gumbe za Canvas, pokušajte pomicati gumbe za beam zone pomoću `Shift + Left / Right Arrow`. Trebali biste vidjeti po jedan gumb za svako ciljno područje Canvas, označen kao _CANVAS 1, CANVAS 2_ itd.
{% endhint %}

### Canvas zones

Canvas zones su područja unutar Canvas koja odaberete za slanje na laser. U Canvas view prikazane su kao ružičasti obrisi pravokutnika. Na svaku zone možete kliknuti desnom tipkom miša i odabrati lasere kojima je želite dodijeliti. Ako se zatim prebacite na prikaz _OUTPUT_ za taj laser, vidjet ćete da se pojavila nova zone.

{% hint style="danger" %}
UPOZORENJE - ako je laser u stanju armed, mogli biste iznenada početi projicirati sadržaj u zadanoj canvas zone. Najbolje je da laser bude disarmed prije nego što mu dodijelite canvas zones.
{% endhint %}

{% hint style="info" %}
Canvas zone možete dodijeliti laseru i klikom na gumb _add canvas zone_ u prikazu _OUTPUT_. Pogledajte [zones](../output-view/zones.md).
{% endhint %}

### Referentne slike

U Canvas možete dodati referentnu sliku i koristiti je kao predložak za svoju grafiku. Preporučuje se prilagoditi nijansu boje referentne slike (izbornik desnog klika) i potamniti je kako biste lakše vidjeli svoj sadržaj preko nje.

{% hint style="info" %}
Kod arhitektonskog mapiranja korisnim se pokazalo izraditi „razmotani” prikaz zgrade koji sve površine zgrade prikazuje kao ravnu, nedeformiranu sliku. Korekcija perspektive za pojedine dijelove može se napraviti pomoću canvas zone u prikazu _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>„Spljoštena” referentna slika za Saltwell Hall u Gatesheadu, UK</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas zones u ranoj verziji Liberation (oko 2017.!) Obratite pozornost na to da ružičasti pravokutnici određuju koji se dio Canvas prikazuje, a prikazi Output ispod pokazuju na koji dio svakog lasera te zone odlaze.</p></figcaption></figure>

### Canvas u 3D vizualizatoru

Vjerojatno bi bilo prilično nezgodno (blago rečeno) ponovno izraditi složen sustav projekcije s više lasera u 3D vizualizatoru. Zato umjesto toga imate opciju postaviti svoj Canvas unutar 3D prostora. Aktivirajte potvrdni okvir _Show canvas_ u panelu _3D visualiser settings_. (Sve referentne slike koje imate u Canvas također će se prikazati u vizualizatoru.)

{% hint style="info" %}
Imajte na umu da će vizualizator i dalje prikazivati projekcije Canvas kao atmosferske efekte koji dolaze iz lasera. Možete ih jednostavno pomaknuti izvan prikaza ili ih, ako želite biti precizni, poravnati s Canvas.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Može biti iznimno zadovoljavajuće kada zrake iz lasera poravnate sa slikom Canvas u 3D vizualizatoru!</p></figcaption></figure>
