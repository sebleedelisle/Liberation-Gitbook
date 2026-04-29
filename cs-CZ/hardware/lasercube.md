---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Propagační obrázek LaserCube se svolením Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) od Wicked Lasers je extrémně kompaktní laserová jednotka napájená z baterie, dostupná v několika výkonových konfiguracích. Mezi hobby uživateli je oblíbená díky snadno použitelné aplikaci pro chytré telefony, ale novější modely už jsou dostatečně schopné i pro profesionální show.

Telefonní aplikace, která se jmenuje LaserOS a je dostupná i pro desktop, je zdarma ke stažení, je zábavná na vyzkoušení a většině uživatelů bude stačit. Pokud ale provozujete větší show s více lasery, potřebujete specializovanější a výkonnější řešení – a tady přichází na řadu Liberation.

### Připojení k LaserCube

První LaserCube se ovládaly přes USB, ale současné modely mají vestavěný síťový řadič. Tyto síťově ovládané jednotky se označují jako „LaserCube Wifi“. Liberation podporuje oba typy LaserCube\*, ať už jsou připojené přes USB, nebo přes síť.

\*(Podpora síťového protokolu LaserCube byla přidána ve verzi 0.7.3)

### USB LaserCube

Připojte LaserCube k počítači pomocí micro USB kabelu a potom jej vyhledejte v panelu _Controller Assignment_ (viz [Controller Assignment](../setting-up/controller-assignment.md)). Pokud se nezobrazí automaticky, klikněte na tlačítko _REFRESH_.

### Síťový LaserCube „Wifi“

{% hint style="danger" %}
I když jsou jednotky „Wifi“ navržené pro provoz přes bezdrátovou síť, nedoporučuje se to. Pravděpodobně by docházelo k výpadkům a chybám. Místo toho připojte LaserCube do kabelové sítě přes konektor RJ45, stejně jako u Ether Dream.
{% endhint %}

Připojte LaserCube ke své kabelové síti.

Přepněte LaserCube do režimu „LAN Client“ a ujistěte se, že je v síti router. LaserCube získá IP adresu z routeru a poté by se měl zobrazit v panelu _Controller Assignment_ (viz [Controller Assignment](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Je možné nastavit síť bez routeru a přiřadit všem zařízením pevné IP adresy. V eventovém průmyslu je to velmi běžné. Osobně ale dávám přednost přidání routeru do sítě a tuto možnost doporučuji každému, kdo nemá se sítěmi tolik zkušeností.

Router dynamicky přidělí IP adresu všem zařízením. Podle mě je to jednodušší a méně náchylné k chybám.
{% endhint %}

{% hint style="danger" %}
Na rozdíl od Ether Dream jednotky LaserCube při podtečení bufferu, ztraceném paketu nebo jiných poškozených či nesprávných datech _**NEZHASNOU LASEROVÝ VÝSTUP**_.

Místo toho prostě pokračují od místa, kde skončily. V některých případech to může způsobit, že aktivní paprsek projde oblastmi, které nejsou uvnitř nastavených zones, a co je ještě horší, může projít i přes ochranu nastavenou pomocí software masks.

Mluvím o tom s návrháři a vývojáři LaserCube a doufám, že to v budoucnu vyřeší aktualizací firmwaru. Mezitím ale musíte zajistit fyzické maskování všech míst, kam se laser nemá dostat.

Upřímně řečeno byste to pravděpodobně měli dělat vždy, ale já sám používám software masks k ochraně kamer a projektorů. Berte tedy na vědomí, že při použití síťového protokolu LaserCube je to nebezpečnější než u Ether Dream, který při jakékoli chybě nebo chybějících datech přejde do bezpečnostního stop režimu.

A už jsem to říkal, ale **pro LaserCube používejte kabelové připojení**. Wifi na to nebude stačit a celý problém ještě zhorší.
{% endhint %}
