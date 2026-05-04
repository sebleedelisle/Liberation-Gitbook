---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Bølgeoscillatorer

## På denne siden :

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sagtannbølge](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Trekantbølge](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sinusbølge](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Firkantbølge](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Innstillinger for bølgeoscillator

Alle Wave-oscillatorer har følgende innstillinger :

* **range min / range max** - bestemmer verdiområdet for egenskapen oscillatoren styrer. Egenskapen settes til _range min_ når bølgeformen er nederst, og til _range max_ når bølgeformen er øverst.

{% hint style="info" %}
Hvis du for eksempel vil at en prikk skal bevege seg til venstre og høyre mellom -100 og 100, kobler du oscillatoren til _x property socket_, setter _min range_ til -100 og _max range_ til 100.
{% endhint %}

* **duration** - hvor lang tid én full syklus (eller _loop_) tar å fullføre. Dette er relativt til tempoet i takter. Så ¼ er ett enkelt slag. 1 er en hel takt, osv.
* **duration multiplier** - skalerer grunnvarigheten med en valgt faktor. Hvis duration for eksempel er satt til en firedelsnote og multiplier er 3, varer oscillatoren i tre firedelsnoter (en punktert halvnote). Desimale multiplikatorer støttes også — hold _SHIFT_ mens du drar i glidebryteren for å angi ikke-hele tall. Dette er nyttig for faseeffekter eller for å lage små tidsforskyvninger.
* **offset** - startforskyvningen for bølgen, som prosent av varigheten. Hvis du vil at bølgen skal starte en fjerdedel inn i forløpet, setter du denne til 25%.
* **repeat count** - antall ganger loopen kjøres før den stopper. Standardverdien er _FOREVER_, men du kan endre den hvis du ikke vil at oscillatoren skal kjøre uendelig. Når den stopper, settes egenskapen til verdien ved slutten av bølgen.
* **delay count** - forsinkelsen i slag før oscillatoren begynner å kjøre. Før den starter, settes egenskapen til verdien ved starten av bølgen.

{% hint style="info" %}
Med bevisst bruk av _repeat count_ og _delay count_ kan du lage svært kompliserte animasjoner, nesten som en egen tidslinje!
{% endhint %}

## Felles innstillinger

* **steps** - deler bevegelsen inn i et antall diskrete trinn. Nyttig når du vil at egenskaper skal "hoppe" til verdier i stedet for å bevege seg jevnt.

{% hint style="info" %}
Merk at trinnene deles inn etter tid, ikke verdi. For en bølge delt inn i 4 trinn med en varighet på 1 takt, vil egenskapen derfor endres momentant på hvert slag.
{% endhint %}

* **clamp min / clamp max -** øker skalaen på bølgen utover minimums- eller maksimumsverdiene og clampler resultatet.

{% hint style="info" %}
_clamp_-konseptet er litt vanskelig å forklare, men se for deg at bølgeformen går over toppen eller bunnen av grafen og deretter blir klemt fast mot kantene. Jeg anbefaler at du eksperimenterer med disse! De er veldig nyttige hvis du vil at en sagtannbølge skal starte sent eller slutte tidlig.
{% endhint %}

* **ease function** - Sawtooth- og Triangle-bølgene har også en ease function som subtilt endrer animasjonskurven, og kan gjøre animasjonene dine svært uttrykksfulle!
  * **LINEAR** - standardvalget, ingen easing, bare lineær bevegelse mellom min- og maksverdiene.
* **EASE OUT** - starter raskt og bremser ned mot slutten. Veldig nyttig for å simulere fysikk, dvs. å bremse ned til stopp.
  * **EASE IN** - starter langsomt og øker gradvis i hastighet. Nyttig for å simulere at momentum bygger seg opp.
  * **EASE IN/OUT** - en kombinasjon av begge, og gir en svært organisk bevegelse.

{% hint style="warning" %}
**Easing -** Jeg ville unngått standard lineær animasjon når du kan, med mindre du spesifikt vil ha noe som ser robotaktig ut. Easing kan gjøre animasjonene dine mye mer flytende og organiske!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sagtannbølge

Kalles også noen ganger en _rampebølgeform_, fordi den ramper oppover og deretter faller brått på slutten av syklusen. Dette er sannsynligvis den vanligste bølgeoscillatoren, fordi den lager en loop for sykliske egenskaper som _hue_ eller _rotation._

Se avsnittene over for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Spesifikt for sagtannbølge :

* **cycle range compensation** - tilgjengelig når **steps** er satt, og er nyttig for sykliske verdier, for eksempel en rotasjon fra 0 til 360. Når denne ikke er satt, vil start- og sluttverdiene være like, noe som kan føre til at bevegelsen henger ved startpunktet (fordi 0 og 360 er samme vinkel). Slå dette på, så reduseres maksimumsområdet for å korrigere trinnposisjonene.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Trekantbølge

I motsetning til _sagtannbølgen_, som hopper tilbake til starten for hver syklus, beveger _trekantbølgen_ seg lineært fremover og deretter bakover.

Se avsnittene over for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sinusbølge

Den jevneste bølgeformen! Oscillerer mykt mellom to verdier, som en pendel.

Se avsnittene over for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Firkantbølge

Den enkleste bølgeformen - den veksler bare mellom to verdier, frem og tilbake!

Se avsnittene over for :

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Spesifikt for firkantbølge :

* **pulse width** - hvor lenge bølgen ligger på maksimumsverdien i forhold til den totale varigheten. 50% er standard, som er nøyaktig halvparten av tiden. Hvis du bare vil at den skal være "på" en fjerdedel av tiden, setter du den til 25%. Du kan justere når denne pulsen skjer ved å bruke _offset_-verdien.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

En av styrkene til Liberation er at det kan generere tilfeldige, men repeterbare effekter. _noise_-oscillatoren kan brukes til å lage en organisk, loopende tilfeldig bevegelse med så mye detalj/jitter som du ønsker.

Se avsnittene over for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Spesifikt for Noise :

* **noise type** - algoritmen som brukes til å generere støyen.
  * **SIMPLEX** - standardvalget, en bølgende verdi som stiger og faller, og gjentas i en loop.
  * **RANDOM** - bruker en mer tradisjonell algoritme for tilfeldige tall, helt støyete og kaotisk.

{% hint style="info" %}
**Simplex noise** ble utviklet av Ken Perlin i 2001 som en forbedring av hans "Perlin noise"-algoritme, som han utviklet i 1983 som en del av arbeidet sitt på filmen _Tron_ (som han vant en Oscar for!)

Denne såkalte "gradient"-støyen oppsto fra frustrasjonen hans over tidligere "maskinaktige" datagenererte bilder. I CGI-verdenen er den spesielt god til å rendere skyer, vannflater eller til og med høydekart for realistisk terreng.

Men i Liberation er den nyttig for tilsynelatende uforutsigbar bevegelse som fortsatt er jevn og organisk.
{% endhint %}

* **seed** - verdien som brukes til å lage støyen. Hvis du ikke liker hvordan noise-bølgen ser ut, kan du prøve å endre denne verdien.

{% hint style="info" %}
Morsomt nerdefaktum! For å få perfekt loopende simplex noise itererer jeg rundt en sirkel på et 2D-støyplan. Og når seed-verdien endres, flyttes dette planet gjennom en tredje dimensjon!
{% endhint %}

* **simplex detail** - endrer hvor detaljert eller jittery støyen er. Hvis du vil at det repeterende mønsteret skal være mindre tydelig, øker du duration og øker denne verdien.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Lager en helt egendefinert bølgeform. Dette er svært nyttig for å lage komplekse animasjoner.

Se avsnittene over for :

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Under dette finner du en liste med posisjoner og verdier. Varigheten deles inn i 64 trinn, og du kan plassere en verdi på hvilket som helst av disse punktene.

Hvert trinn har følgende innstillinger :

* **Step** - tidstrinnet innenfor varigheten. 0 er i starten, og 64 er ved slutten.
* **Level** - bølgens nivå ved dette tidstrinnet. Nivået går fra 0 til 1.
* **Animation type** - nedtrekksmenyen lar deg velge hvordan du vil bevege deg mot dette nivået fra forrige trinn.
  * **None** - ingen overgang, bare hopp rett til dette nivået på det angitte tidspunktet.
  * **Linear** - en helt lineær bevegelse fra forrige nivå til dette.
  * **Ease in / Ease out / Ease in/out** - easer mellom forrige nivå og dette. Se _ease function_ over for en beskrivelse av animasjonstypene.

***
