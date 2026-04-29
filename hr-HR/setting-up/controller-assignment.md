---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Dodjela kontrolera

Nakon što postavite lasere u Liberation, svaki od njih možete dodijeliti stvarnom laserskom kontroleru. (Pogledajte [kompatibilne lasere i kontrolere (DAC-ove)](../hardware/compatible-lasers-and-controllers-dacs.md) kako biste provjerili koji hardver možete koristiti). Kontroleri će biti povezani putem USB-a ili preko mreže.

* Otvorite panel _Controller Assignment_ putem opcije izbornika _View -> Controller Assignment_. (Možete upotrijebiti i gumb _ASSIGN LASER CONTROLLERS_ u panelu _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Panel Controller Assignment"><figcaption></figcaption></figure>

* Panel je podijeljen na dva dijela: popis lasera nalazi se lijevo, a popis dostupnih kontrolera desno. Ako na popisu ne vidite svoj laserski kontroler, pritisnite gumb _REFRESH_. Ako i dalje imate poteškoća, pogledajte [rješavanje problema](../troubleshooting/).
* Da biste kontroler dodijelili laseru, kliknite ga na desnoj strani i povucite u slobodan utor za laser na lijevoj strani. Time Liberation zna koji kontroler treba koristiti za koji laser. (Ako se predomislite, kontrolere možete slobodno povlačiti gore-dolje s jednog lasera na drugi.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Popis kontrolera" width="375"><figcaption></figcaption></figure>

* Ako pored kontrolera vidite zeleni kvadrat, to znači da se Liberation uspješno povezao s njim.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream i Helios DAC dodijeljeni su laserima 2 i 3</p></figcaption></figure>

{% hint style="info" %}
Imajte na umu da će se laser automatski deaktivirati svaki put kada se povežete s kontrolerom.
{% endhint %}

* Narančasti kvadrat 🟧 znači da kontroler ima povremene probleme s vezom. To je obično uzrokovano mrežnim problemom; pogledajte [rješavanje problema](../troubleshooting/).
* Crveni kvadrat 🟥 znači da kontroler nije dostupan; pogledajte [rješavanje problema](../troubleshooting/).
* _Gumb za prekid veze_ (X) prekida vezu s kontrolerom, ali ga ne uklanja iz dodjele laseru. Zatim možete upotrijebiti _gumb za ponovno povezivanje_ (ikona strelice za osvježavanje) kako biste ga ponovno povezali ili ponovno kliknuti _gumb za prekid veze_ kako biste uklonili dodjelu.
* _Napredna značajka:_ Otvorite panel za analitiku kontrolera klikom na gumb koji izgleda kao grafikon. To je napredna značajka koja vam daje detaljne informacije o toku podataka i može pomoći pri rješavanju problema. (Ova opcija možda nije dostupna za neke vrste kontrolera.)
* Možete upotrijebiti _gumb za preimenovanje_ (olovka) kako biste ovom kontroleru dali bilo koji naziv. Ima smisla nazvati ga tako da ga lako možete povezati s određenim hardverom. Ako je ugrađen u laser, možda ćete ga htjeti tako i nazvati, npr. _LaserCube Ultra #1_ ili _Triton T5 #3._ Ti će se nazivi spremiti u vašu instalaciju Liberation i ubuduće će se prikazivati; to vam može znatno pomoći da brzo prepoznate svoje lasere.

{% hint style="info" %}
Profesionalni savjet — **dvaput kliknite** kontroler na desnoj strani kako biste ga automatski dodijelili sljedećem dostupnom laseru na lijevoj strani. To može stvarno uštedjeti vrijeme ako trebate dodijeliti mnogo lasera!
{% endhint %}

Gumbe _DISCONNECT ALL_ i _RECONNECT ALL_ možete upotrijebiti za brzo ponovno postavljanje svih veza. To je korisno ako imate mrežnih problema.
