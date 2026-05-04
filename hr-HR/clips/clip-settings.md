---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Postavke za Clip

### Panel s postavkama za Clip

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Panel s postavkama za Clip</p></figcaption></figure>

Promijenite veličinu izlaza za Clip pomoću _Scale X_ i _Scale Y_. Te su vrijednosti povezane, osim ako pritisnete tipku _SHIFT_.

Promijenite vodoravni i okomiti položaj za Clip pomoću _Shift X_ i _Shift Y_.

_Zone Delay/Chase_ toliko je zabavna značajka da ima vlastiti odjeljak. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Panel Parameters

Panel desno od Clip Deck prikazuje osam kontekstualnih parametara. Kada je odabran Clip, prve kontrole su _Shift X_, _Shift Y_ i _Zone Delay_ odabranog Clip, nakon čega slijede globalne kontrole _Spin_ i _Scale_.

Ti isti parametri preslikavaju se na podržane MIDI kontrolere. Ako nije odabran nijedan Clip, mjesta specifična za Clip ostaju prazna. Ako držite pritisnut gumb grupe, prve dvije kontrole mijenjaju se u vremena fade in i fade out za tu grupu.

### Zaključavanje Clips

Ako je Clip zaključan, ne može se premjestiti ni izbrisati. Da biste zaključali Clip, upotrijebite potvrdni okvir _Locked_ u izborniku desnog klika. U panelu s postavkama za Clip dostupno je još nekoliko opcija.

* _UNLOCK ALL -_ otključava svaki Clip u Clip Deck.
* _AUTO-LOCK_ - kada je _Auto-Lock_ uključen, svaki Clip koji se automatski reproducira (bilo putem timelinea ili sustava za MIDI snimanje/reprodukciju) bit će zaključan. To je korisno ako ste programirali show u Logic Pro (ili sličnom programu) i ne želite slučajno urediti Clips koji se koriste u showu.
* _LOCKED CLIPS ZONES_ - ako je ovo uključeno, ne možete mijenjati zones ni za jedan zaključani Clip.
* _LOCKED CLIPS PARAMS_ - ako je ovo uključeno, ne možete mijenjati parametre (scale, shift itd.) ni za jedan zaključani Clip.

### Izbornik desnog klika

Ako desnom tipkom miša kliknete Clip, prikazat će se izbornik s nekim opcijama za taj Clip. Pogledajte [Uvod u Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Postavke za Clip](clip-settings.md "mention") i [Clip grupe](groups.md "mention") za više informacija o prvih nekoliko stavki u ovom izborniku.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Clips su prema zadanim postavkama postavljeni na _retrigger_. To znači da će se Clip početi izvoditi od tog trenutka, bez obzira na to kada ga pritisnete. Dakle, ako ga pokrenete kasno, animacija za Clip bit će malo zakašnjela i izvan ritma.

{% hint style="info" %}
Ako upotrijebite _Tap Tempo_ dok se izvodi Clip s uključenim retriggerom, sustav će “kvantizirati” Clip tako da bude u ritmu, čak i ako ga niste pokrenuli točno na dobu.
{% endhint %}

Ako _Retrigger_ nije omogućen, Clip će uvijek biti u ritmu — kao da je pokrenut na samom početku sata. To je korisno kada ste savršeno sinkronizirani s glazbom putem vanjskog signala sata.

{% hint style="info" %}
Clips su često dizajnirani da se ponavljaju beskonačno, ali možete ih dizajnirati i tako da se izvedu samo jednom ili nekoliko puta. Pazite da za takve Clips ostavite uključen _retrigger_, inače se neće ponovno pokrenuti!
{% endhint %}

### Vrijeme prijelaza za ulaz/izlaz (fade)

Clips se mogu postaviti tako da se postupno pojavljuju i nestaju, s trajanjem mjerenim u sekundama. Prema zadanim postavkama, vrijeme fadea nasljeđuje se iz postavki grupe (a može se promijeniti desnim klikom na gumb grupe).

Ako želite drukčije trajanje fadea od onog u grupi kojoj Clip pripada, najprije isključite gumb _USE GROUP DEFAULT_, a zatim prilagodite klizače _In time_ i _Out time_ za Clip.
