---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / sinkronizacija

Sinkronizacija s glazbom temeljni je dio Liberationa; kada uskladite tempo i dobe s glazbom, možete biti sigurni da će sve biti sinkronizirano. Ako imate sreće i dobijete MIDI clock (ili Ableton Link), ne morate se uopće brinuti o ručnoj sinkronizaciji. Ako ga nemate, nema problema — možete se ručno uskladiti pomoću značajke _Live_ tempo.

Ako imate iskustva s glazbenim ili rasvjetnim softverom, ovaj će vam postupak biti poznat. Ako nemate, vrijedi odvojiti malo vremena za upoznavanje sa sustavom i vježbanje kod kuće prije nastupa uživo.

## Panel Tempo

Panel _Tempo_ uvijek je prikazan na zaslonu i sadrži sve postavke sinkronizacije. Na vrhu ćete vidjeti trenutačni brojač takta/dobe i transport s gumbima za reprodukciju/pauzu te premotavanje natrag/unaprijed.

Ispod toga nalazi se indikator dobe; četiri kvadrata koja „pulsiraju” u ritmu. Ovaj _beat marker_ iznimno je korisna vizualizacija i stalno ćete ga pratiti dok koristite sustav _Live_ tempo.

### Postavljanje tempa

Tempo možete postaviti na više načina:

* Kliknite i povucite klizač _Tempo_
* Shift-kliknite i povucite klizač _Tempo_ za promjenu tempa u koracima od 0,1
* Dvaput kliknite klizač _Tempo_ i ručno upišite broj
* Upotrijebite gumb _Tempo_ na APC40 (pritisnite shift za korake od 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo je definiran u „dobama u minuti”, a uobičajena tradicionalna početna vrijednost najčešće je 120.
{% endhint %}

## Tap Tempo

Automatski postavite tempo klikom na gumb _TAP_ u ritmu s dobom. Početak takta postavite gumbom _RESET_.

{% hint style="info" %}
Sustav Tap Tempo dovoljno je pametan da prepozna ako ste nakratko prestali tapkati ili ako ste propustili nekoliko doba. Ako počnete tapkati u dvostrukom tempu, razumjet će da želite udvostručiti tempo; isto vrijedi i ako tapkate u pola tempa.

Također može prepoznati ako dvije osobe istodobno tapkaju tempo (npr. jedna na tipkovnici, a druga na APC40). Liberation će izračunati prosjek dvostrukih tapova.
{% endhint %}

#### Tipkovničke naredbe:

T - tap tempo\
R - reset takta\
Y - zaokruživanje tempa na najbližu dobu u minuti.

{% hint style="info" %}
Budući da se većina današnje glazbe stvara digitalno, tempo je vrlo vjerojatno zaokružen cijeli broj. Ako se čini da je tapkani tempo blizu, pritisnite tipku Y (ili pomaknite gumb za tempo na APC40 za jedan „klik”) kako biste ga zaokružili na cijeli broj.
{% endhint %}

#### Kontrole na APC40:

APC40 ima namjenski gumb _TAP TEMPO_, a možete upotrijebiti i spojeni nožni prekidač kako biste tapkali nogom!

Za podešavanje upotrijebite gumb _TEMPO_. Držite _SHIFT_ dok koristite gumb _TEMPO_ za fino podešavanje.

Upotrijebite gumb _METRONOME_ za **reset takta**. (Imajte na umu da gumb _METRONOME_ također svijetli u ritmu dobe.)

Okrenite gumb _TEMPO_ za jedan „klik” udesno ili ulijevo kako biste **zaokružili tempo** gore ili dolje na cijeli BPM broj.

Pogledajte i [Referenca za APC40](reference/apc40-reference.md "mention")

### Nudge tempo

Ako ste sigurni da ste dovoljno blizu stvarnom tempu, ali primijetite da polako izlazite iz ritma, upotrijebite gumbe _NUDGE_ za korekciju.

Ako tempo u Liberationu ide ispred glazbe, pritisnite i držite _NUDGE -_ kako biste ga privremeno usporili dok se ponovno ne poravna.

Ako tempo u Liberationu zaostaje za glazbom, pritisnite i držite _NUDGE +_ kako biste ga privremeno ubrzali dok se ponovno ne poravna.

{% hint style="info" %}
Možete koristiti gumbe NUDGE na zaslonu ili namjenske gumbe na APC40.
{% endhint %}

### Pola tempa / dvostruki tempo

Upotrijebite gumbe _÷2_ i _x2_ za trajno prepolavljanje ili udvostručavanje tempa. Za razliku od množitelja tempa, ovo je trajna promjena trenutačnog tempa.

## Tempo Multiplier

Sustav _Tempo Multiplier_ omogućuje vam privremenu prilagodbu tempa prije povratka na prethodnu vrijednost.

Uključite ili isključite _Tempo Multiplier_ pritiskom na gumb _TEMPO MULTIPLIER_ ili gumb _BANK_ na APC40. Podesite ga pomoću klizača na zaslonu ili pomoću APC40 A-B klizača. Možete upotrijebiti i preset gumbe _25%, 50%, 100% 200%_.

## Vanjski izvori tempa

### MIDI Clock

Za sinkronizaciju s vanjskim MIDI clock signalom odaberite opcijski gumb _MIDI CLOCK_ i odaberite MIDI uređaj iz padajućeg izbornika. Obratite pozornost na obojeno statusno svjetlo pokraj padajućih izbornika:

* Zeleno - prima se MIDI clock signal
* Narančasto - moguće je povezati se s MIDI uređajem, ali trenutačno nema clock signala
* Crveno - nije moguće povezati se s MIDI uređajem

{% hint style="info" %}
MIDI Clock emitira niz okvira (24 po četvrtinki), ali poruke ne sadrže podatke o poziciji. To znači da je koristan za održavanje tempa, ali možda ćete i dalje morati resetirati takt.

Izvor tempa MIDI Clock u Liberationu također reagira na poruke **MIDI Machine Control (MMC)**, pa ako ih vaš izvor clock signala šalje, nećete morati ručno resetirati takt.
{% endhint %}



### Ableton Link

Za sinkronizaciju s Ableton Link odaberite _ABLETON LINK_ kao izvor tempa. Liberation se pridružuje Link sesiji na vašoj lokalnoj mreži i prati zajednički tempo i fazu dobe iz drugih aplikacija koje podržavaju Link.

Ableton Link ne upotrebljava MIDI priključak i ne prenosi apsolutnu poziciju u pjesmi. Upotrijebite kontrole za resetiranje takta ako početak takta u Liberation treba uskladiti s određenim trenutkom u showu.

### Vremenska linija

Svaka vremenska linija ima vlastiti tempo, koji može biti fiksna vrijednost ili _Tempo Map_. _Tempo Map_ omogućuje prilagodbu tempa u određenim trenucima unutar vremenske linije.

Tempo vremenske linije koristit će se kada je _TIMELINE_ odabran kao izvor tempa.

{% hint style="info" %}
Vremensku liniju možete pokrenuti s _bilo kojim_ izvorom tempa! Dakle, ako imate bend uživo koji ne svira uz click, možete ručno pokrenuti vremensku liniju i održavati je sinkroniziranom pomoću izvora tempa _LIVE_. Ili, ako imate MIDI clock signal, možete koristiti njega!
{% endhint %}
