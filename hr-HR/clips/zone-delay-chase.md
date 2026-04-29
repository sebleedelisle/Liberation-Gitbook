---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Svi se slažemo da više lasera znači više zabave, ali ako svi rade potpuno isto, propuštate kreativne mogućnosti.

Sustav zone delay jednostavan je, ali učinkovit način za uvođenje raznolikosti među zonama i može zaista dobro iskoristiti postavu s više lasera. Može se upotrijebiti i za izradu tradicionalnijeg chase efekta.

#### Kako funkcionira

_Zone delay_ dodaje kašnjenje u vremenski tijek za Clip kroz svaku zone, stvarajući neku vrstu prelaska preko zona.

Vrlo je učinkovito dodati zone delay na Clip koji već radi, a zatim odgovarajućom kontrolom na APC40 prilagoditi razinu i pattern. (Pogledajte [Referenca za APC40](../reference/apc40-reference.md)). Možete upotrijebiti i panel _Clip Settings_.

Postavke za zone delay:

* **Zone delay** - upravlja količinom kašnjenja primijenjenom na svaku zone, mjereno u šezdesetčetvrtinkama.
* **Pattern** - odabire redoslijed zona
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern radi na temelju brojeva zone i pretpostavlja da su vaše zone poredane slijeva nadesno. Zone delay pri izračunu patterna tretira canvas zones i DMX zones kao zasebne grupe.
{% endhint %}

* **Delay mode**
  1. No delay - upotrijebite ovo u chase mode
  2. Delay - zadani način rada; odgađa vremenski tijek svake zone
  3. Delay with re-trigger - vraća Clip na početak pri svakom koraku kroz pattern. Ovo je dobro u kombinaciji s _Chase mode_.
* **Chase mode** - kada je chase mode uključen, svaka zone uključuje se i isključuje poput tradicionalnog chase efekta. Izgled chase efekta prilagodite postavkama _Fade in, Hold,_ i _Fade out_. Te se postavke zadaju kao omjer vrijednosti zone delay, pa bi vrijednost 1 trajala jednako kao vrijeme zadano u vrijednosti _Zone delay_. Malo je teško objasniti, pa je moj savjet da sami isprobate.

{% hint style="info" %}
Zone delay primjenjuje se i na sve aktivne efekte. Na primjer, efekt treperenja također će se odgoditi kroz zone, jednako kao i animacija unutar samog Clip.
{% endhint %}

Kada Clip ima bilo koju vrstu _Zone delay_, u gornjem desnom kutu Clip vidjet ćete ikonu s tri točke. Te su točke animirane kako bi prikazale stil _Zone delay_ za taj Clip. Za više detalja pogledajte [Što znače male ikone na gumbima za Clips?](what-are-the-small-icons-on-the-clip-buttons.md).

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Simbol s tri točke koji označava da Clip ima zone delay i prikazuje njegov način rada</p></figcaption></figure>

{% hint style="info" %}
Zone delay je postavka koja pripada svakom Clip; nije globalna. Dio je kreativnog dizajna za Clip.
{% endhint %}
