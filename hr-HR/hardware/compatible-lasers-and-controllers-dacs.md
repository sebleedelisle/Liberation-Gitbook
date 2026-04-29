---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatibilni laseri i kontroleri (DAC-ovi)

### Koji su laseri kompatibilni s Liberation?

Ako vaš laser ima standardni ILDA ulaz, možete ga koristiti s Liberation, uz kompatibilan laserski kontroler kao što je Ether Dream ili Helios DAC - [pogledajte cijeli popis u nastavku](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - najpovoljnija opcija za kućnu upotrebu</p></figcaption></figure>

Ne trebate vanjski kontroler ni ILDA ulaz ako:

* Vaš laser ima ugrađen Ether Dream, ili;
* Imate LaserCube tvrtke Wicked Lasers, ili;
* Imate X-Laser uređaj s ugrađenim Mercury sustavom, ili;
* Imate Laser Animation Sollinger laser s ugrađenim AVB kontrolerom (trenutačno u testiranju samo na macOS)

{% hint style="info" %}
**Što je laserski kontroler?**

Laserski kontroler (ili DAC) hardverski je uređaj koji može preuzeti digitalne podatke iz Liberation i pretvoriti ih u analogne signale potrebne za upravljanje skenerima i izlazom vašeg lasera. (Otuda DAC: Digital to Analog Converter, odnosno digitalno-analogni pretvarač.)

Kontroler se povezuje s računalom putem USB-a ili preko standardne računalne mreže; može biti vanjski uređaj ili ugrađen u laser.

Ako je vanjski, povezuje se s laserom putem ILDA priključka. ILDA je industrijski standard koji koristi stari 25-pinski „D” konektor. Nabavite ILDA kabel, jedan kraj priključite u kontroler, a drugi u laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>ILDA izlaz na vanjskom Ether Dream kontroleru</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Stražnja ploča lasera s različitim priključcima, uključujući ILDA ulaz</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Standardni ILDA kabel</p></figcaption></figure>

### Koji je kontroler najbolji za mene?

Ako ste kućni korisnik ili izvodite manje showove s najviše 4 lasera koji su blizu računala, USB kontroleri kao što je **Helios DAC** **najpovoljnija** su opcija.

Mrežni DAC-ovi kao što je **Ether Dream** **najbolja su opcija za profesionalne** operatere lasera koji su spremni postaviti mrežu i žele upravljati velikim brojem lasera; svi veliki showovi izvedeni s Liberation do sada su koristili Ether Dream kontrolere.

Ako imate **LaserCube**, ne trebate zaseban laserski kontroler - Liberation je kompatibilan sa svim LaserCube uređajima. Raniji modeli povezuju se USB kabelom, a noviji modeli preko mreže.

Ako ste profesionalni korisnik i tražite najjednostavniju opciju, razmotrite X-Laser uređaje s ugrađenim Mercury sustavom ili Laser Animation Sollinger lasere koji koriste AVB.

### Kompatibilni laserski kontroleri

#### Ether Dream (mreža)

[Ether Dream](https://ether-dream.com) postoji više od deset godina i trenutačno je u verziji 4 (iako Liberation radi i s Ether Dream verzijama 1, 2 i 3). Izuzetno su pouzdani.

S njima se povezujete preko standardne mreže. Mogu se kupiti kao samostalne jedinice ili, još bolje, mogu se ugraditi u lasere.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) najbolja je opcija za početnike i jeftiniji je od Ether Dream kontrolera, ali budući da se povezuje putem USB-a, ne preporučuje se za duge kabelske trase. Također, možete naići na probleme s USB podacima i upravljačkim programima kada povežete više od 4 uređaja (osobito na Windows).

Ali ako kod kuće želite pokrenuti samo nekoliko lasera, to je najjeftinija i najjednostavnija opcija.

#### Mercury (ugrađen u X-Laser uređaje)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) moćan je DMX sustav za upravljanje laserima tvrtke X-Laser, namijenjen dizajnerima rasvjete koji žele upravljati laserima izravno s tradicionalne rasvjetne konzole. S najnovijim ažuriranjem firmvera, Mercury uključuje i **emulaciju Ether Dream kontrolera**, što znači da sada besprijekorno radi s Liberation - kao i sa svim drugim softverom koji podržava Ether Dream.

#### AVB (ugrađen u Laser Animation Sollinger uređaje)

**AVB** je otvoreni mrežni protokol za visokoučinkoviti audio i podatkovni streaming s malom latencijom. Mnogi LaserAnimation Sollinger projektori uključuju AVB podršku izravno u hardveru, što omogućuje da se Liberation poveže s njima preko mreže bez potrebe za vanjskim DAC-ovima. AVB podrška u Liberation trenutačno je **samo za macOS i u fazi testiranja**, a zahtijeva **kompatibilne mrežne uređaje s podrškom za AVB**. Kada je pravilno postavljen, nudi jednostavniji tijek rada, manje vanjskih uređaja i robusnu pouzdanost za profesionalne showove.

#### Kontroleri koji će biti podržani u budućnosti:

* [IDN](http://www.ilda-digital.com) (otvoreni mrežni protokol organizacije ILDA, može ga implementirati bilo koji proizvođač)

### Preporuke za kabele

Za optimalne performanse držite USB DAC-ove blizu računala i povežite ih s laserima duljim ILDA kabelima. (Ipak, pripazite jer se ILDA kabeli tijekom raspremanja mogu ponašati kao kuka za hvatanje!)

Ako koristite Ether Dream kontrolere, i dalje ih možete držati sve zajedno i povezati ih s laserima dugim ILDA kabelima, ili ih možete postaviti blizu lasera i koristiti dulje mrežne kabele.

Idealna je konfiguracija da Ether Dream kontroleri (ili drugi kontroleri) budu ugrađeni izravno u vaše lasere (Rob iz Stanwax Laser može to napraviti za vas u Ujedinjenom Kraljevstvu).
