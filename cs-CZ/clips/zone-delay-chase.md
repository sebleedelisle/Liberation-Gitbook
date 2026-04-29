---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Všichni se shodneme, že více laserů znamená více zábavy. Pokud ale všechny dělají přesně totéž, přicházíte o kreativní možnosti.

Systém Zone delay je jednoduchý, ale účinný způsob, jak přidat mezi zones více rozmanitosti a opravdu využít sestavu s více lasery. Dá se použít také k vytvoření tradičnějšího chase efektu.

#### Jak to funguje

_Zone delay_ přidává zpoždění do časování Clip pro každou zone a vytváří tak určitý průběh napříč zones.

Zone delay je velmi účinné přidat do již běžícího Clip. Pomocí příslušného ovládacího prvku na APC40 upravte úroveň a pattern. (Viz [Referenční přehled APC40](../reference/apc40-reference.md)). Nebo můžete použít panel _Clip Settings_.

Nastavení Zone delay:

* **Zone delay** – určuje velikost zpoždění použitého pro každou zone, měřeno v 1/64 notách.
* **Pattern** – vyberte pořadí zones
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern pracuje s čísly zone a předpokládá, že vaše zones jsou seřazené zleva doprava. Při výpočtu pattern bere Zone delay canvas zone a DMX zone jako samostatné skupiny.
{% endhint %}

* **Delay mode**
  1. No delay – použijte v režimu Chase mode
  2. Delay – výchozí režim, zpožďuje časování každé zone
  3. Delay with re-trigger – při každém průchodu pattern vrátí Clip zpět na začátek. Dobře funguje s _Chase mode_.
* **Chase mode** – při zapnutém Chase mode se každá zone zapíná a vypíná jako u tradičního chase efektu. Vzhled chase upravíte pomocí nastavení _Fade in, Hold,_ a _Fade out_. Tato nastavení jsou určena jako poměr k hodnotě Zone delay, takže hodnota 1 odpovídá stejnému času, jaký je zadaný v hodnotě _Zone delay_. Vysvětluje se to trochu obtížně, takže nejlepší rada je vyzkoušet si to.

{% hint style="info" %}
Zone delay se použije také na všechny aktivní efekty. Například blikající efekt bude zpožděný napříč zones stejně jako animace uvnitř samotného Clip.
{% endhint %}

Když má Clip jakýkoli typ _Zone delay_, v pravém horním rohu Clip uvidíte ikonu se třemi tečkami. Tyto tečky jsou animované a ukazují styl _Zone delay_ pro daný Clip. Další informace najdete v části [Co znamenají malé ikony na tlačítkách Clip](what-are-the-small-icons-on-the-clip-buttons.md).

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Symbol se třemi tečkami, který označuje, že Clip má Zone delay, a ukazuje jeho režim</p></figcaption></figure>

{% hint style="info" %}
Zone delay je nastavení, které patří ke každému Clip. Není globální; je součástí kreativního návrhu Clip.
{% endhint %}
