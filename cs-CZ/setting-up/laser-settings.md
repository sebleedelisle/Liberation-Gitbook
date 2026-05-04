---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Panel nastavení laserového výstupu

Panel nastavení _Laser output_ otevřete z nabídky _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Zobrazí se nastavení aktuálně vybraného laseru, které můžete změnit:

* pomocí jeho číselného tlačítka v panelu _Laser Overview_
* číselnou klávesou na klávesnici; klávesy 1 až 0 otevírají lasery 1–10
* klávesou `Tab`, kterou postupně procházíte lasery (`Shift + Tab` prochází opačným směrem).

V horní části tohoto panelu najdete:

* číselné tlačítko – kliknutím tento laser aktivujete nebo deaktivujete. Když je laser aktivovaný, tlačítko je červené.
* posuvník _Brightness_ pouze pro tento laser. Pamatujte, že se kombinuje s nastavením _Global Brightness_.
* přepínač _Test Pattern_ a výběr obrazce. Umožní vybrat konkrétní testovací obrazec pouze pro tento laser. (Stejné ovládací prvky jsou také na panelu nástrojů v Output view.)

### Orientace výstupu / korekce zrcadlení

Následující prvky slouží ke korekci nastavení laseru tak, aby se v Liberation choval konzistentně.

* **Flip horizontal / vertical** – tyto volby umožňují opravit výstup laseru

{% hint style="info" %}
Nastavení převrácení vodorovně / svisle byste neměli potřebovat měnit, pokud laser není nesprávně zapojený nebo pokud na zadní straně nemá tlačítka pro převrácení X/Y, která nejsou správně nastavena. Pokud chcete převrátit výstup jen u konkrétního Clip, nastavte to přímo v daném Clip.
{% endhint %}

* **Orientation** – pokud je laser zavěšený na boku nebo vzhůru nohama, můžete tímto nastavením opravit jeho natočení.
* **Fine position adjustments** – slouží k opravě velmi malého posunu nebo natočení. Jsou určené ke korekci driftu nebo sednutí sestavy, pokud byl laser ponechán přes noc nebo delší dobu bez zásahu.

{% hint style="info" %}
Korekce orientace / zrcadlení nemění nic ve 3D Visualiser. Použijte je k tomu, aby výstup skutečného laseru odpovídal tomu, co vidíte ve 3D Visualiser!
{% endhint %}

### Kopírování nastavení laseru

Viz [Kopírování nastavení laseru](laser-settings.md#copy-laser-settings "mention").

### Nastavení skenerů

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Nastavení rychlosti určuje, jak rychle se skenery pohybují.

{% hint style="danger" %}
I když jsou výchozí nastavení poměrně konzervativní, příliš vysokou rychlostí můžete skenery poškodit. Postupujte opatrně, zejména při zvyšování rychlosti.
{% endhint %}

{% hint style="info" %}
Toto nastavení rychlosti nemění počet bodů za sekundu. Místo toho upravuje, jak daleko jsou jednotlivé body od sebe. Další informace najdete v části [Jak Liberation generuje laserový obsah](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Paprsek při pohybu skenerů mění barvu a zapíná se a vypíná. Tyto dvě věci obvykle nejsou navzájem dokonale synchronní. Tímto nastavením je znovu srovnáte.

{% hint style="info" %}
Někdy se tomu říká _blank shift_, ale osobně dávám přednost názvu _scanner sync_ – je o něco přesnější, protože upravuje časování všech změn barev vůči pohybu skenerů.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laserové „ocásky“ – Colour shift není správně nastavený</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Žádné laserové „ocásky“! Colour shift je nastavený dobře!</p></figcaption></figure></div>

Pokud na výstupu laseru vidíte malé „ocásky“, pravděpodobně je potřeba upravit synchronizaci skenerů. Pokud se ocásky objevují bez ohledu na nastavení, nejspíš řídíte skenery nebo laserové drivery rychleji, než zvládnou. Zkuste snížit rychlost skenerů.

#### Předvolby skenerů

Tímto nastavením vyberete předpřipravené nastavení skenerů. Výchozí volba je obvykle v pořádku, takže ji většinou nemusíte měnit, pokud nemáte mimořádně špatné (nebo dobré) skenery. Pokud se chcete podívat podrobněji, viz [Předvolby skenerů](../advanced/scanner-presets.md "mention")

#### Kalibrace barev

Tento systém můžete použít ke korekci křivky jasu a vyvážení bílé u laseru. Viz [Kalibrace barev](../advanced/colour-calibration.md "mention")

#### Pokročilá nastavení

Tato nastavení byste neměli potřebovat měnit, ale pokud vás zajímají podrobnosti, viz [Pokročilá nastavení laseru](../advanced/advanced-laser-settings.md "mention")
