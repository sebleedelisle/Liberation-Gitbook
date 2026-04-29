---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Vremenski kod (timecode)

Liberation podržava sinkronizaciju s vanjskim SMPTE/LTC signalom vremenskog koda, koji se često koristi u glazbenim nastupima uživo kako bi svjetla, pirotehnika, video i prateće snimke ostali vremenski usklađeni.

{% hint style="info" %}
Što je SMPTE/LTC?

SMPTE je standard za vremenski kod, a LTC je taj vremenski kod pretvoren u audiosignal. Ako slušate taj audio, zvuči kao užasno visoko pištanje, ali za računala je to vremenska informacija visoke razlučivosti.

**Činjenice za geekove!**

Povijesno se SMPTE koristio za sinkronizaciju videa i zvuka. Kod sinkronizacije s analognom vrpcom, jedan bi zapis sadržavao snimljeni audio vremenskog koda, što se ponekad nazivalo „striping” vrpce. Taj zapis vremenskog koda mogao se koristiti za vremensko usklađivanje više magnetofona međusobno ili za sinkronizaciju MIDI sekvencera s vrpcom. (Tako MIDI instrumente nije trebalo snimati na vrpcu; sekvencer ih je mogao reproducirati uživo tijekom miksanja!)

SMPTE znači Society of Motion Picture and Television Engineers, organizacija koja je definirala standard. LTC znači _Linear TimeCode._
{% endhint %}

LTC signal vremenskog koda možete primati preko bilo kojeg zvučnog sučelja na računalu, ali preporučuje se profesionalno sučelje s barem jednim podesivim XLR ulazom i mogućnošću monitoringa.

Imam dobro iskustvo s uređajem [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) jer ima monitoring na slušalicama, 2 XLR ulaza i ne zahtijeva posebne upravljačke programe (barem na macOS-u). Ako ćete ga koristiti isključivo za vremenski kod, možete uzeti nešto jeftiniji [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (ima samo jedan ulaz i nema MIDI), ali iskreno, svako solidno zvučno sučelje trebalo bi raditi.

{% hint style="info" %}
LTC signali vremenskog koda obično se distribuiraju uravnoteženim XLR kabelima jer su dovoljno robusni za prijenos audio signala niske razine na velike udaljenosti. (XLR je cilindrični priključak koji se obično koristi s mikrofonima.)
{% endhint %}

### Hardversko povezivanje

Priključite XLR kabel sa signalom vremenskog koda u zvučno sučelje i provjerite dobivate li dobar signal. Podesite razinu na zvučnom sučelju dok signal ne bude jak, ali bez klipanja. Ako vaše zvučno sučelje ima izlaz za slušalice, možete poslušati vremenski kod i provjeriti da nema prekida ni previše šuma.

{% hint style="info" %}
Teoretski je moguće primiti signal preko jack priključka na MacBooku, ali za to bi bio potreban prilagođeni kabel. Ti su priključci obično 4-polni TRRS mini jackovi i iskreno nisam siguran koji se od tih kontakata može koristiti za audio ulaz, kao ni koju razinu napona može podnijeti (negdje sam pročitao da je to +/-1 V, ali koristite to na vlastitu odgovornost!)

Mislim da je bolje nabaviti jeftino USB zvučno sučelje nego pokušavati s ovim.
{% endhint %}

Ako vaše zvučno sučelje nema nikakav ulazni monitoring, možete provjeriti u postavkama sustava macOS (pod _Sound_) primate li signal. (Na Windowsu upotrijebite _Sound Control Panel_.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS prikazuje ulaznu razinu za svako zvučno sučelje u panelu postavki sustava Sound</p></figcaption></figure>

### Postavljanje u Liberation

1. Odaberite svoje zvučno sučelje i ispravan ulazni kanal u prozoru Timecode settings.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Imajte na umu da u padajućem izborniku postoje zasebne opcije za svaki ulazni kanal na vašem zvučnom sučelju.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Obratite pozornost na kvadrat s lijeve strane. Ako primate valjan signal vremenskog koda, postat će zelen. Ako ne, bit će crven.

2. Odaberite ispravan broj sličica u sekundi za dolazni vremenski kod. Osoba koja vam šalje vremenski kod trebala bi vam moći reći koji je frame rate. (Ako odaberete pogrešno, sinkronizacija će i dalje raditi, ali primijetit ćete mali „skok” svake sekunde.)
3. Otvorite postavke vremenskog koda za Timeline pomoću male ikone sata na traci Timeline i odaberite opciju SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Podesite početni pomak (u satima, minutama, sekundama i frameovima) tako da odgovara početku pjesme. Ako imate više Timeline stavki, ove opcije morate postaviti za svaku zasebno.

{% hint style="info" %}
U svijetu turneja uobičajena je praksa da svaka pjesma počinje u drugom satu, npr. 01:00:00:00 za prvu pjesmu, 02:00:00:00 za drugu pjesmu i tako dalje.

Liberation će se automatski prebaciti na Timeline ovisno o vremenskom kodu, tako da tijekom nastupa nikad ne morate ručno mijenjati Timeline.
{% endhint %}

Imajte na umu da je, za razliku od MIDI Clocka i Ableton Linka, SMPTE _apsolutni_ vremenski sustav, mjeren u satima, minutama, sekundama i frameovima. Osnovni vremenski sustav u Liberation temelji se na dobama i taktovima, pa će se pri primanju vremenskog koda koristiti tempo postavljen u Timeline. Morate provjeriti da je taj tempo sinkroniziran s glazbom koja je također sinkronizirana s vremenskim kodom.
