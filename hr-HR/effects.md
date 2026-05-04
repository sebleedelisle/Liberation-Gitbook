---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Efekti

Sustav efekata u aplikaciji Liberation zabavan je i svestran način za promjenu izlaza Clip sadržaja u stvarnom vremenu. Efekti su potpuno fleksibilni i mogu se koristiti za bljeskanje, uključivanje i isključivanje, vrtnju, promjenu boja ili čak nasumično kretanje!

Sve što možete napraviti u Clip Editor može se koristiti kao efekt. Zapravo, efekti se uređuju istim node editorom kao i Clips! Pogledajte [Uređivanje efekata](effects.md#editing-effects "mention"). Kreativne mogućnosti praktički su beskonačne.

Zadani gumbi za efekte 1–8 nalaze se ispod gumba za zone, a efekti 9–24 mali su gumbi pri dnu.

#### Primjena efekta

Pritisnite gumb efekta da biste ga uključili ili isključili, ili još bolje, koristite APC40 klizače 1–8 za postupno pojačavanje i smanjivanje efekata. Za postupno uvođenje efekta bez APC40, kliknite gumb i povlačite gore-dolje. Možete i kliknuti desnom tipkom miša na gumb efekta i podesiti klizač razine.

{% hint style="warning" %}
Pritiskom na gumb efekta taj će se efekt odmah aktivirati. Međutim, imajte na umu da se ništa neće dogoditi ako je razina postavljena na nulu! Kliknite i povucite gumb za promjenu razine, kliknite desnom tipkom miša i upotrijebite klizač _level_ ili upotrijebite APC40 fadere.
{% endhint %}

#### Efekti i odgoda za zone u Clip

Efekti preuzimaju postavku odgode za zone za svaki Clip koji je trenutačno pokrenut. Dakle, ako vaš Clip ima odgodu koja se kreće slijeva nadesno, a dodate efekt bljeskanja, i bljeskanje će biti odgođeno slijeva nadesno.

{% hint style="info" %}
Način na koji efekti nasljeđuju odgodu za zone iz Clip jedna je od onih stvari koje je iznimno teško opisati, ali postanu očite čim ih isprobate!

Rekao bih da je to jedan od najzabavnijih i najkreativnijih alata ugrađenih u Liberation. Isprobajte i vidjet ćete na što mislim!
{% endhint %}

#### Parametri efekta

Dodajte parametar svojem efektu pomoću _Parameter node_. Sustav Parameter način je za podešavanje više postavki unutar efekta izvana. Pogledajte [Upravljanje parametrima](clip-editor/oscillators/parameter-control.md "mention") za više informacija.

Upotrijebite rotacijske kontrolere 1–8 za podešavanje _parameter_ za svaki efekt. Možete i kliknuti desnom tipkom miša na gumb efekta i podesiti klizač ili klizače parametara. Promjena parametra radi različite stvari, ovisno o tome kako je efekt postavljen. U nastavku je popis zadanih efekata i objašnjenje što rade njihovi parametri.

{% hint style="info" %}
Rotacijski kontroleri 1–8 nalaze se uz gornji rub APC40 Mk2, a na Mk1 gore desno. Pogledajte i: [APC40 referenca](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
Mali brojevi koje vidite na gumbima efekata odnose se na _level_ i _parameter_ efekta. _level_ se kontrolira faderom na APC40 ili možete kliknuti i povlačiti po gumbu. Parametar se podešava rotacijskim kontrolerima na APC40 ili desnim klikom za podešavanje mišem.
{% endhint %}

#### Zadani efekti

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Primjenjuje kaotično kretanje na izlaz Clip sadržaja. Parametar podešava količinu/brzinu kaosa.
2. **Sine wave** :\
   Izobličuje sav sadržaj kroz pokretni sinusni val. Parametar podešava valnu duljinu.
3. **Rotation** :\
   Vrti sve elemente. Parametar podešava brzinu vrtnje.
4. **Horizontal flip** :\
   Vodoravno sabija i rasteže sve elemente. Parametar podešava brzinu.
5. **Scale** :\
   Neprestano skalira sve elemente od pune veličine do nule. Parametar podešava brzinu.
6. **Hue** :\
Mijenja nijansu svega, ali ne mijenja zasićenje (tj. sve što je bijelo ostaje bijelo). Parametar podešava nijansu.
7. **Saturation and hue** :\
Mijenja nijansu svega i također potpuno zasićuje boju (tj. sve što je bijelo mijenja se u tu boju). Parametar podešava nijansu.
8. **Flash** :\
   Neprestano bljeska svjetlinom svega od pune vrijednosti do nule. Parametar podešava brzinu bljeskanja.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

U donjem redu nalazi se još 16 efekata boje za primjenu unaprijed zadanih vrijednosti nijanse i zasićenja.

Imajte na umu da su to zadani efekti, ali možete ih urediti tako da rade gotovo što god želite!

### Apply to groups

Možete odabrati na koje grupe efekt utječe. Kliknite desnom tipkom miša i uključite ili isključite potvrdne okvire grupa označene _Apply to groups._

Ovu postavu najčešće koristim kada odvojeno radim s Canvas grafikom i laserskim zrakama. Sav Canvas sadržaj tipa Clip dodjeljujem grupi 5, a zatim tu grupu isključujem iz efekata za koje ne želim da utječu na taj grafički Clip sadržaj.

Možete je koristiti i za primjenu dviju različitih promjena boje uživo na dvije grupe lasera odjednom. Izradite dva efekta za promjenu boje i odaberite na koje se grupe Clip sadržaja svaki od njih primjenjuje.

### MX group

Kratica za _Mutually Exclusive_, ovo je način grupiranja efekata tako da samo jedan efekt u grupi može biti aktivan u isto vrijeme. Primijetite da samo jedan od zadanih efekata za promjenu boje može biti aktivan odjednom. To je zato što su svi u MX Group 1.

Ova je funkcionalnost onemogućena ako je postavka _MX Group_ postavljena na 0.

### Uređivanje efekata

Kliknite desnom tipkom miša na bilo koji efekt i kliknite gumb _EDIT EFFECT_ da biste otvorili editor efekta. Primijetite da je ovaj editor isti kao Clip Editor!

Uređujte efekt na isti način na koji biste uređivali bilo koji Clip. Pogledajte [Clip Editor](clip-editor/ "mention").

Morate imati barem jedan node tipa Creator; to može biti bilo što (linija, krug, oblik, čak i tekst!), ali vjerojatno biste trebali odabrati nešto što ima najviše smisla u pretpregledu gumba efekta.

Kada se efekti primijene, svi node tipa Creator u efektu zamjenjuju se izlazom trenutačno pokrenutih Clips.

{% hint style="warning" %}
Zbog iznimno zamornih tehničkih razloga, "trails" nodes nisu omogućeni unutar efekta. Isto vrijedi za postavku "delay" unutar node tipa pattern (koriste isti sustav). To će biti ispravljeno u budućim revizijama.
{% endhint %}
