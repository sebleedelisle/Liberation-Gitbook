---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Controller Assignment

Jakmile v Liberation nastavíte lasery, můžete každý z nich přiřadit ke skutečnému laserovému kontroléru. (V části [Kompatibilní lasery a kontroléry (DAC)](../hardware/compatible-lasers-and-controllers-dacs.md) najdete přehled hardwaru, který můžete použít.) Kontroléry budou připojené buď přes USB, nebo přes síť.

* Otevřete panel _Controller Assignment_ přes nabídku _View -> Controller Assignment_. (Případně můžete použít tlačítko _ASSIGN LASER CONTROLLERS_ v panelu _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Panel Controller Assignment"><figcaption></figcaption></figure>

* Panel je rozdělený na dvě části: vlevo je seznam laserů a vpravo seznam dostupných kontrolérů. Pokud svůj laserový kontrolér v seznamu nevidíte, stiskněte tlačítko _REFRESH_. Pokud potíže přetrvávají, podívejte se na [Řešení potíží](../troubleshooting/).
* Chcete-li kontrolér přiřadit k laseru, klikněte na něj vpravo a přetáhněte ho na volnou pozici laseru vlevo. Tím Liberation určíte, který kontrolér má použít pro který laser. (Pokud si to rozmyslíte, můžete kontroléry libovolně přetahovat mezi jednotlivými lasery.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Seznam kontrolérů" width="375"><figcaption></figcaption></figure>

* Pokud vedle kontroléru vidíte zelený čtverec, znamená to, že se k němu Liberation úspěšně připojil.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream a Helios DAC přiřazené k laserům 2 a 3</p></figcaption></figure>

{% hint style="info" %}
Upozornění: kdykoli se připojíte ke kontroléru, laser se automaticky deaktivuje.
{% endhint %}

* Oranžový čtverec 🟧 znamená, že kontrolér má přerušované potíže s připojením. Obvykle je způsobuje problém se sítí; viz [Řešení potíží](../troubleshooting/).
* Červený čtverec 🟥 znamená, že kontrolér není dostupný; viz [Řešení potíží](../troubleshooting/).
* Tlačítko pro odpojení (X) kontrolér odpojí, ale neodebere ho z přiřazení k laseru. Poté ho můžete znovu připojit pomocí tlačítka pro opětovné připojení (ikona obnovovací šipky), nebo znovu kliknout na tlačítko pro odpojení a přiřazení tím zrušit.
* _Pokročilá funkce:_ Kliknutím na tlačítko, které vypadá jako graf, otevřete panel analýzy kontroléru. Jde o pokročilou funkci, která poskytuje podrobné informace o datovém toku a může pomoci při řešení problémů. (Tato možnost nemusí být u některých typů kontrolérů dostupná.)
* Pomocí tlačítka pro přejmenování (tužka) můžete kontrolér pojmenovat libovolně podle potřeby. Je praktické zvolit název tak, aby bylo snadné ho spojit s konkrétním hardwarem. Pokud je kontrolér zabudovaný v laseru, můžete ho pojmenovat například _LaserCube Ultra #1_ nebo _Triton T5 #3_. Tyto názvy se uloží ve vaší instalaci Liberation a budou se od této chvíle zobrazovat; může vám to výrazně usnadnit rychlou identifikaci laserů.

{% hint style="info" %}
Tip pro rychlejší práci – **dvojitým kliknutím** na kontrolér vpravo ho automaticky přiřadíte k dalšímu volnému laseru vlevo. Pokud přiřazujete větší počet laserů, může to ušetřit hodně času.
{% endhint %}

Pomocí tlačítek _DISCONNECT ALL_ a _RECONNECT ALL_ můžete rychle resetovat všechna připojení. To se hodí při potížích se sítí.
