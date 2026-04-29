# ✅ Panel nastavení výstupu laseru

Panel nastavení _Laser output_ otevřete z nabídky _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Zobrazí se nastavení aktuálně vybraného laseru, které můžete změnit:

* tlačítkem s číslem v panelu _Laser overview_
* číselnou klávesou na klávesnici; klávesy 1 až 0 otevřou lasery 1–10
* klávesou `Tab` pro procházení laserů (`Shift + Tab` prochází opačným směrem).

V horní části tohoto panelu uvidíte:

* tlačítko s číslem – kliknutím tento laser aktivujete nebo deaktivujete. Když je laser aktivní, tlačítko je červené.
* posuvník _Brightness_ pouze pro tento laser. Toto nastavení se kombinuje s hodnotou Global Brightness.
* přepínač _Test Pattern_ a výběr vzoru. Umožní vybrat konkrétní testovací obrazec pouze pro tento laser. (Tyto ovládací prvky jsou zrcadlené také v nástrojové liště Output view.)

### Korekce orientace výstupu / zrcadlení

Následující prvky slouží ke korekci nastavení laseru tak, aby se v Liberation choval konzistentně.

* **Flip horizontal / vertical** – tyto volby umožňují opravit výstup laseru

{% hint style="info" %}
Nastavení horizontálního nebo vertikálního převrácení byste neměli potřebovat měnit, pokud laser není špatně zapojený nebo pokud nemá na zadní straně tlačítka pro převrácení X/Y, která nejsou správně nastavena. Pokud chcete převrátit výstup jen u konkrétního Clip, nastavte to přímo v něm.
{% endhint %}

* **Orientation** – pokud je laser zavěšený na boku nebo vzhůru nohama, můžete tímto nastavením opravit jeho natočení.
* **Fine position adjustments** – lze použít ke korekci velmi malých posunů nebo natočení. Je určené pro dorovnání driftu nebo sednutí, pokud byl laser ponechán přes noc nebo po delší dobu.

{% hint style="info" %}
Korekce orientace a zrcadlení nemění nic ve 3D Visualiser. Slouží k tomu, aby výstup skutečného laseru odpovídal tomu, co vidíte ve 3D Visualiser!
{% endhint %}

### Kopírování nastavení laseru

Viz [Kopírování nastavení laseru](./#copy-laser-settings).

### Nastavení skenerů

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Nastavení rychlosti určuje, jak rychle se skenery pohybují.

{% hint style="danger" %}
I když jsou výchozí hodnoty poměrně konzervativní, při příliš rychlém řízení můžete skenery stále poškodit. Postupujte opatrně, zejména při zvyšování rychlosti.
{% endhint %}

{% hint style="info" %}
Toto nastavení rychlosti nemění rychlost bodů. Místo toho upravuje, jak daleko jsou body od sebe rozmístěné. Další informace najdete v části [Jak Liberation generuje laserový obsah](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Paprsek při pohybu skenerů mění barvu a zapíná se a vypíná. Tyto dvě věci obvykle nejsou dokonale synchronizované. Tímto nastavením je můžete znovu sladit.

{% hint style="info" %}
Někdy se tomu říká _blank shift_, ale osobně dávám přednost označení _scanner sync_ – je o něco přesnější, protože upravuje časování všech změn barev vůči pohybu skenerů.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laserové „ocásky“ – Colour shift není správně nastavený</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Žádné laserové „ocásky“! Colour shift je nastavený správně!</p></figcaption></figure></div>

Pokud na výstupu laseru vidíte malé „ocásky“, pravděpodobně je potřeba upravit Scanner sync. Pokud se ocásky objevují bez ohledu na nastavení, nejspíš řídíte skenery nebo laserové drivery rychleji, než zvládnou. Zkuste snížit rychlost skenerů.

#### Předvolby skenerů

Pomocí této volby vyberete předem připravené nastavení skenerů. Výchozí volba je obvykle v pořádku, takže toto nastavení byste neměli potřebovat měnit, pokud nemáte výrazně horší (nebo lepší) skenery. Pokud chcete jít více do hloubky, podívejte se na [Předvolby skenerů](../../advanced/scanner-presets.md)

#### Kalibrace barev

Tento systém můžete použít ke korekci křivky jasu a vyvážení bílé vašeho laseru. Viz [Kalibrace barev](../../advanced/colour-calibration.md)

#### Pokročilá nastavení

S těmito nastaveními byste neměli potřebovat manipulovat, ale pokud vás zajímají podrobnosti, podívejte se na [Pokročilá nastavení laseru](../../advanced/advanced-laser-settings.md)
