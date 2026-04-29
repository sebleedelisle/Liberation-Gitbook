---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Povremeni / treperavi izlaz

Otvorite panel _Laser Overview_ i pogledajte indikator veze pokraj lasera s kojim imate poteškoće.

**Ako indikator veze NIJE stalno zelen:**\
Tada vjerojatno imate problem s mrežom ili performansama CPU-a:

**Performanse mreže -**

* Provjerite da niste spojeni na Wi-Fi mrežu. Uvijek trebate koristiti žičanu vezu. Provjerite daje li vaš operacijski sustav prednost žičanoj mreži u odnosu na Wi-Fi ili, ako niste sigurni, isključite Wi-Fi.
* provjerite mrežni adapter i pokušajte s drugim USB-C adapterom
* korisnici Windowsa - provjerite / nadogradite mrežne upravljačke programe i pokrenite odgovarajuće alate za testiranje mreže
* provjerite sve kabele, switcheve i routere. Metodično zamijenite i testirajte svaki kabel.
* ponovno pokrenite svu mrežnu opremu, uključujući switcheve, routere i svaki Ether Dream.

**Performanse CPU-a**

Ako imate starije ili slabije računalo, možda je presporo za pokretanje Liberation. Provjerite indikator broja sličica u sekundi na desnoj strani trake s ikonama.

Tamo se nalaze dvije vrijednosti - stvarni broj sličica u sekundi i ciljni broj sličica u sekundi. Ako stvarni broj sličica u sekundi padne ispod 30, mogu se pojaviti problemi.

Sljedeće radnje mogu pomoći:

* uklonite lasere koje ne koristite, npr. ako imate spojen samo jedan laser, izbrišite ostale.
* Prebacite se na Output view ili Canvas view
* Zatvorite sve ostale programe, provjerite postavke mrežnog vatrozida, zatvorite antivirus, Dropbox itd.
* Smanjite razlučivost zaslona i smanjite prozor Liberation

Ako ništa od ovoga ne pomogne, razmislite o nadogradnji računala.

***

**Ako je indikator veze stalno zelen:**

Tada je vjerojatno riječ o hardverskom problemu. To je izvan opsega ovog priručnika, ali možete pokušati sljedeće:

* Onemogućite sustav SFS (Scan Fail Safety). Neki laseri imaju funkciju koja onemogućuje izlaz ako se skeneri prestanu kretati, tj. ako proizvode snažnu statičnu zraku. Takvi sustavi mogu biti pomalo preosjetljivi / nepouzdani.

{% hint style="danger" %}
Budite iznimno oprezni kada onemogućujete sustav zaštite od zaustavljanja skenera. Snažne statične zrake mogu izazvati zapaljenje! Pobrinite se da pri ruci imate tipku za zaustavljanje i aparat za gašenje požara.
{% endhint %}

* Provjerite kabele i sustave sigurnosnih blokada
* Provjerite sve kabele između kontrolera i lasera.

[ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) može biti neprocjenjiv alat za rješavanje problema s laserima.
