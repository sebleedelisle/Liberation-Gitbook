---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Učitavanje i spremanje

Liberation stalno sprema svoje stanje na disk, tako da u slučaju nestanka struje ili problema sa sustavom može nastaviti točno ondje gdje je stao. Ne biste trebali izgubiti svoje zones, vremenske crte ili drugi sadržaj.

Ipak, svoju konfiguraciju možete izvesti radi sigurnosne kopije ili prijenosa na drugo računalo.

### Uvoz/izvoz projekta

Datoteka projekta sprema gotovo sve iz vaše trenutačne konfiguracije, uključujući:

* Sve što je opisano u odjeljku [Uvoz/izvoz Laser Settings](loading-and-saving.md#laser-settings-import-export "mention") u nastavku
* Clips, efekte i postavke grupa
* Sve vaše vremenske crte (bez audio i video medija)
* Art-Net postavke
* Postavke slanja/primanja MIDI podataka
* Postavke tempa/sinkronizacije

Trenutačno ne sprema i ne učitava:

* Postavke zvučnog i MIDI ulaza koje se upotrebljavaju u node MIDI notes i Sound Input Oscillator (_sprema_ postavke slanja/primanja MIDI podataka, kao i zvučni ulaz za timecode)
* Skaliranje sučelja
* Medije za Canvas guide images
* Zvučne i video medije za vremenske crte
* Fontove koji se upotrebljavaju u node Text

{% hint style="danger" %}
Zvučne i videodatoteke na vremenskoj crti ne spremaju se s datotekama projekta, zato ih obavezno spremite zasebno ako ih želite prenijeti na drugo računalo. Pogledajte [Važna napomena o medijskim datotekama vremenske crte](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Uvoz/izvoz Laser Settings

* Laser Settings za svaki laser
* Beam zones
* Ciljna područja za Canvas
* DMX zones
* Dodjela za laser controller (i aliasi za sve controllers koje ste preimenovali)
* Postavke i preseti kalibracije skenera i boja lasera
* Postavke i preseti za 3D vizualizator

### Uvoz/izvoz Clip Deck

* Svi Clips i njihove dodjele na zones, postavke i parametri
* Sve postavke grupa, flash mode, vremena fade in/out itd.

Trenutačno ne sprema i ne učitava:

* Sve efekte te njihove parametre i postavke

{% hint style="info" %}
**Učitajte Clips iz datoteke projekta bez učitavanja cijelog projekta**

Da biste iz projekta uvezli samo Clips, odaberite _**Clips->Import Clip Deck**_, a zatim umjesto datoteke Clip Deck (.cpdk) odaberite datoteku projekta.
{% endhint %}

### Dodavanje Clip Deck

Možete dodati Clips iz izvezene datoteke Clip Deck u trenutačni projekt pomoću _Append Clip Deck_. Clips se dodaju na kraj trenutačnog Clip Deck, ali efekti i postavke grupa iz datoteke ne uvoze se.

### Izvoz odabranih Clips

Svi trenutačno odabrani Clips izvest će se u datoteku. Postavke grupa i efekti neće se spremiti, nego samo Clips. Imajte na umu da se trenutačno aktivni Clips ne izvoze osim ako su također odabrani.

{% hint style="info" %}
Za odabir Clips pritisnite Option/Alt - shift i kliknite na njih (ili upotrijebite laso). Odabrane Clips prepoznat ćete po debelom bijelom obrubu oko njih. Pogledajte [Pokretanje i zaustavljanje Clips](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Uvoz/izvoz efekata

Učitava i sprema sve efekte zajedno s njihovim postavkama grupa i parametrima.

{% hint style="info" %}
**Učitajte efekte iz datoteke projekta bez učitavanja cijelog projekta**

Da biste iz projekta uvezli samo efekte, odaberite _**Effects->Import Effects**_, a zatim umjesto datoteke efekata (.efts) odaberite datoteku projekta.
{% endhint %}

### Izvoz vremenske crte

Izvezite datoteku vremenske crte s jednom ili više vremenskih crta. Imajte na umu da je Clip Deck uvijek uključen u izvezene datoteke vremenske crte (iako možete odabrati koje ćete Clips ponovno uvesti; pogledajte [Uvoz vremenske crte](loading-and-saving.md#timeline-import "mention") u nastavku).

Ako u datoteci projekta imate više od jedne vremenske crte, otvorit će se panel u kojem možete odabrati koje vremenske crte želite izvesti.

{% hint style="danger" %}
Zvučne i videodatoteke na vremenskoj crti ne spremaju se s datotekama vremenske crte, zato ih obavezno spremite zasebno ako sadržaj želite prenijeti na drugo računalo. Pogledajte [Važna napomena o medijskim datotekama vremenske crte](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Uvoz vremenske crte

Uvezite jednu ili više vremenskih crta iz jedne datoteke vremenske crte. Nakon što odaberete datoteku vremenske crte, otvorit će se panel s više opcija uvoza.

Ako datoteka vremenske crte sadrži više od jedne vremenske crte, sve će biti navedene. Označite one koje želite uključiti.

* Replace existing timelines\
  Izbrisat će sve vaše trenutačne vremenske crte i zamijeniti ih uvezenima
* Import used clips only\
  Uvest će samo upotrijebljene Clips i rasporediti ih u grupe, po jednu za svaku vremensku crtu. Ako ova opcija nije odabrana, cijeli Clip Deck iz datoteke vremenske crte dodat će se vašim postojećim Clips.
* Replace existing clip deck\
  Zamjenjuje trenutačni Clip Deck sa Clips iz datoteke vremenske crte. Dostupno je samo ako je odabrano _Replace existing timelines_.

{% hint style="info" %}
**Učitajte vremenske crte iz datoteke projekta bez učitavanja cijelog projekta**

Da biste iz projekta uvezli samo vremenske crte, odaberite _**Timeline->Import Timeline(s)**_, a zatim umjesto datoteke vremenske crte (.ltml) odaberite datoteku projekta.
{% endhint %}

### Uvoz/izvoz DMX / Art-Net

Sprema i učitava Art-Net nodes, zajedno s njihovim IP adresama. Uključuje i DMX zones te sve vaše DMX presete.

### Važna napomena o medijskim datotekama vremenske crte

Zvučne i videodatoteke trenutačno se **ne izvoze** s datotekom vremenske crte, zato ih obavezno uključite ako sadržaj trebate premjestiti na drugo računalo.

{% hint style="info" %}
**Kako vremenska crta traži medijske datoteke**

Kada se vremenska crta učita, tražit će datoteke u istoj mapi u kojoj se nalazi datoteka vremenske crte (ili projekta), kao i u svim podmapama. Dakle, sve dok su datoteke u istoj mapi ili podmapi (kao što su _/videos_ ili _/sound_), pronaći će ih pri učitavanju.
{% endhint %}
