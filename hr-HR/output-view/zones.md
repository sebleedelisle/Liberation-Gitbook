---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Glavna vrsta koju ćete koristiti u većini projekata jest _Beam zone_. To je zone namijenjen atmosferskim beam efektima kroz zrak. Druga vrsta je _Canvas zone_ (pogledajte [Grafika i sustav Canvas](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**UPOZORENJE – Budite iznimno oprezni pri pomicanju zones dok laser radi** i smanjite svjetlinu na najnižu moguću razinu. Pogledajte [Postavljanje lasera](../setting-up/setting-up-lasers.md) za cjelovit vodič o sigurnom aktiviranju i zoniranju lasera.
{% endhint %}

Zones možete kliknuti i povlačiti mišem. Uključite test pattern kako biste vidjeli kamo taj zone ide.

{% hint style="info" %}
Tipkama sa strelicama možete **pomaknuti u malim koracima** trenutačno odabrani zone/točku. Pritisnite tipku `Shift` za pomicanje u većim koracima.
{% endhint %}

{% hint style="info" %}
Kratki savjet: postavke za zone možete brzo kopirati na više lasera! Pogledajte [Kopiranje Laser Settings](../setting-up/copy-laser-settings.md)
{% endhint %}

### Dodavanje novog Beam zone

Kliknite gumb _Add a new beam zone_ na vrhu alatne trake i pojavit će se novi zone. Imajte na umu da se Beam zone stavke sortiraju redoslijedom kojim ih dodajete, ali ih možete promijeniti. Pogledajte [Promjena redoslijeda za Beam zones](re-ordering-beam-zones.md)

### Dodavanje postojećeg Canvas zone

Kliknite gumb _Add existing canvas zone_ i vidjet ćete popis dostupnih Canvas zone stavki koje za ovaj laser možete uključiti ili isključiti. Pogledajte [Grafika i sustav Canvas](../graphics-and-the-canvas-system/)

### Vrste oblika za zone

Postoje 3 vrste oblika za zone:

* **Quad** – zadani pravokutni oblik za zone, koji može biti pravilan (poravnat s osima) ili izobličen. Najbolji je za veće pravokutne zone ili Canvas zone koji zahtijevaju korekciju perspektive.
* **Line/Curve** – zone definiran s dvije ili više točaka i debljinom. Idealan za tanke zone ili za završavanje projekcije na balkonima, mostovima ili drugim zakrivljenim oblicima.
* **Segmented** – zone koji se može podijeliti na manje četverokute. Idealan za arhitektonsko mapiranje.

Desnom tipkom miša kliknite bilo koji zone kako biste otvorili njegove postavke. Iz tog izbornika desnog klika možete:

* Preimenovati zone (to može pomoći pri prepoznavanju u Clip Deck, osobito ako imate mnogo zones!)
* Omogućiti/onemogućiti zone
* Zaključati njegov položaj
* Promijeniti vrstu oblika
* Vratiti ga na zadani položaj
* Pristupiti postavkama specifičnima za tu vrstu oblika
* Izbrisati ga
* Dodati _Alt Zone_ (pogledajte [Sustav Alt Zone](alt-zone-system.md))

{% hint style="danger" %}
**UPOZORENJE –** budite vrlo oprezni pri promjeni vrste za zone dok je laser aktivan. Zone će se vratiti na posljednji položaj/veličinu za taj oblik, pa se izlaz može naglo promijeniti. Najbolje je isključiti laser prije promjene vrste za zone.
{% endhint %}

### Oblik Quad zone

Svaki kut četverokuta možete pomicati mišem. Kliknite kut uz `Alt / Option` kako biste ga pomaknuli neovisno o ostalima i izobličili četverokut. Nakon što je četverokut izobličen, svi se kutovi mogu slobodno pomicati.

Izobličenje možete ukloniti i vratiti ga u pravokutnik poravnat s osima pomoću gumba _REMOVE DISTORTION_ u izborniku desnog klika.

#### Korekcija perspektive

Ova se opcija može postaviti pomoću preklopnog gumba u izborniku desnog klika i određuje metodu izobličenja. Za beams je najbolje ostaviti je isključenu, ali ako ovaj zone projicira grafiku na ravnu plohu, uključite je i izlaz će biti korigiran za perspektivu.

{% hint style="info" %}
Ako je _Perspective correction_ isključen, sadržaj se izobličuje pomoću _bilinearne interpolacije_. Drugim riječima, sadržaj je ravnomjerno raspoređen preko četverokuta. Zato je to najbolje za beams.

Kad je korekcija perspektive uključena, sadržaj se izobličuje perspektivnim preoblikovanjem koje kompenzira skraćenje zbog kuta gledanja. Dakle, ako grafiku projicirate na zid pod kosim kutom, ovom opcijom možete ispraviti izlaz i ukloniti izobličenje projekcije.
{% endhint %}

### Oblik Line / Curve zone

Oblik Line / Curve zone postao je moj najčešći izbor u novijim showovima, a moglo bi se reći i da bi trebao biti zadani za Beam zone.

Moji zones najčešće moraju biti tanki kako bi stali u nezgodne uske prostore na lokacijama ili između prozora na zgradama, a pokazalo se da podešavanje četiri kuta četverokuta može biti vrlo nezgodno kad su toliko blizu jedan drugome. Tako je nastao Line / Curve zone!

Za ravne linije potrebne su samo dvije točke, a zatim u izborniku desnog klika podesite _Zone thickness_. To je najbrži način za izradu jednostavnih zones.

Kliknite liniju uz `Alt / Option` kako biste stvorili dodatne točke. Te se točke automatski zaglađuju kako bi se dobio tečan oblik, a možete podesiti _Smooth level_ kako biste izravnali eventualne prijelome.

Kliknite točku uz `Alt / Option` kako biste je izbrisali.

Ako imate iskustva s aplikacijama za vektorsku grafiku (Inkscape, Illustrator itd.), možete upotrijebiti opciju _Manually adjust bezier curves_ za precizno podešavanje svih kontrolnih točaka.

### Oblik Segmented zone

Ovaj podijeljeni zone omogućuje iznimno detaljne korekcije i koristan je kad mapirate na složene oblike. Podjele možete dodavati ili uklanjati pomoću gumba + i - u izborniku desnog klika.

### Kako urediti zone koji je potpuno prekriven drugim zone

Desnom tipkom miša kliknite gornji zone i kliknite gumb s lokotom kako biste ga zaključali. Sada biste trebali moći urediti i podesiti zone ispod njega.

<br>

{% hint style="info" %}
Nakon što dodate Beam zone u svoj Output, bit će dostupan za dodavanje u Clip u Clip Deck.
{% endhint %}
