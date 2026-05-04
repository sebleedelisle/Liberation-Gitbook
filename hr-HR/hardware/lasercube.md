---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Promotivna slika uređaja LaserCube, ljubaznošću Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) tvrtke Wicked Lasers iznimno je kompaktna laserska jedinica s baterijskim napajanjem, dostupna u više konfiguracija snage. Popularna je među hobistima zbog jednostavne aplikacije za pametni telefon, ali noviji modeli dovoljno su sposobni i za upotrebu u profesionalnim nastupima.

Aplikacija za telefon (zove se LaserOS, a dostupna je i za stolna računala) može se besplatno preuzeti, vrlo je zabavna za isprobavanje i dovoljno dobra za većinu korisnika. No ako radite veće nastupe s više lasera, treba vam nešto specijaliziranije i snažnije — tu na scenu dolazi Liberation.

### Povezivanje s uređajem LaserCube

Rani modeli LaserCube upravljaju se putem USB-a, ali svi trenutačni modeli imaju ugrađen mrežni kontroler. Te mrežno upravljane jedinice poznate su kao „LaserCube Wifi”. Liberation podržava obje vrste LaserCube\* uređaja, bilo da su povezani putem USB-a ili preko mreže.

\*(Podrška za mrežni protokol LaserCube uvedena je u verziji 0.7.3)

### USB LaserCube

Povežite LaserCube s računalom pomoću micro USB kabela, a zatim ga potražite u panelu _Controller Assignment_ (pogledajte [Dodjela kontrolera](../setting-up/controller-assignment.md "mention")). Ako se ne prikaže automatski, pritisnite gumb _REFRESH_.

### Mrežni LaserCube „Wifi”

{% hint style="danger" %}
Iako su „Wifi” jedinice zamišljene za rad preko bežične mreže, to se ne preporučuje jer ćete vjerojatno imati prekide i smetnje. Umjesto toga upotrijebite RJ45 priključak i povežite LaserCube na žičanu mrežu, kao što biste učinili s uređajem Ether Dream.
{% endhint %}

Povežite LaserCube sa svojom žičanom mrežom.

Postavite LaserCube u način rada „LAN Client” i provjerite postoji li usmjerivač u mreži. LaserCube će dobiti IP adresu od usmjerivača i zatim bi se trebao prikazati u panelu _Controller Assignment_. (Pogledajte [Dodjela kontrolera](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Moguće je postaviti mrežu bez usmjerivača i svim uređajima dodijeliti fiksne IP adrese, što je vrlo uobičajeno u industriji događanja. Osobno radije dodajem usmjerivač u mrežu i tu opciju preporučujem svima koji imaju manje iskustva s mrežama.

Usmjerivač dinamički dodjeljuje IP adresu svemu na mreži; smatram da je to jednostavnije i manje sklono pogreškama.
{% endhint %}

{% hint style="danger" %}
Za razliku od Ether Dreama, _**LaserCube NE GASI LASERSKI IZLAZ**_ ako dođe do pražnjenja međuspremnika, izgubljenog paketa ili drugih oštećenih/neispravnih podataka.

Umjesto toga, jednostavno nastavlja od mjesta gdje je stao, a u nekim slučajevima to može uzrokovati da aktivna zraka prijeđe preko područja koja nisu unutar zones te, još gore, presiječe softverske masks.

Razgovaram s dizajnerima/programerima uređaja LaserCube i nadam se da će to riješiti u budućnosti ažuriranjem firmvera. U međuvremenu morate fizički maskirati sva mjesta na koja ne želite da laser dođe.

Iskreno, to biste ionako vjerojatno trebali raditi, ali ja osobno koristim softverske masks za zaštitu kamera i projektora. Zato imajte na umu da je to opasnije kada se koristi mrežni protokol LaserCube nego s uređajem Ether Dream (koji ulazi u sigurnosni zaustavni način rada čim dođe do bilo kakve pogreške ili nedostajućih podataka).

Također, već sam to rekao, ali **koristite žičanu vezu s uređajem LaserCube**. Wifi neće biti dovoljan i samo će dodatno pogoršati ovaj problem.
{% endhint %}
