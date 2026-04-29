---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Přerušovaný / blikající výstup

Otevřete panel _Laser Overview_ a podívejte se na indikátor připojení vedle laseru, se kterým máte problém.

**Pokud indikátor připojení NESVÍTÍ trvale zeleně:**\
Pravděpodobně máte problém se sítí nebo s výkonem CPU:

**Výkon sítě –**

* Ujistěte se, že nejste připojeni k Wi‑Fi síti. Vždy používejte kabelové připojení. Zkontrolujte, že operační systém upřednostňuje kabelovou síť před Wi‑Fi, nebo Wi‑Fi vypněte, pokud si nejste jistí.
* Zkontrolujte síťový adaptér – a zkuste jiný adaptér USB-C.
* Uživatelé Windows – zkontrolujte nebo aktualizujte ovladače síťové karty a spusťte vhodné nástroje pro testování sítě.
* Zkontrolujte veškerou kabeláž, switche a routery. Systematicky vyměňte a otestujte každý kabel.
* Restartujte všechna síťová zařízení, včetně switchů, routerů a každého Ether Dream.

**Výkon CPU**

Pokud máte starý nebo méně výkonný počítač, může být pro běh Liberation příliš pomalý. Zkontrolujte indikátor snímkové frekvence na pravé straně lišty ikon.

Jsou tam dvě hodnoty – aktuální snímková frekvence a cílová snímková frekvence. Pokud aktuální snímková frekvence klesne pod 30, mohou nastat problémy.

Pomoci mohou následující kroky:

* Odstraňte nepoužívané lasery, tedy pokud máte připojený pouze jeden laser, smažte ostatní.
* Přepněte do Output view nebo Canvas view.
* Zavřete všechny ostatní programy, zkontrolujte nastavení síťového firewallu, vypněte antivirus, Dropbox apod.
* Snižte rozlišení displeje a zmenšete okno Liberation.

Pokud nic z toho nepomůže, zvažte upgrade počítače.

***

**Pokud indikátor připojení SVÍTÍ trvale zeleně:**

Pak půjde pravděpodobně o hardwarový problém. To je mimo rozsah této příručky, ale můžete zkusit následující kroky:

* Vypněte systém SFS (Scan Fail Safety). Některé lasery mají funkci, která vypne výstup, pokud se skenery přestanou pohybovat, tedy pokud by vznikl silný statický paprsek. Tyto systémy mohou být někdy příliš opatrné nebo nespolehlivé.

{% hint style="danger" %}
Při vypínání systému scan fail safety postupujte mimořádně opatrně. Silné statické paprsky mohou způsobit popálení! Mějte po ruce nouzové stop tlačítko a hasicí přístroj.
{% endhint %}

* Zkontrolujte kabely a systémy bezpečnostního blokování.
* Zkontrolujte veškerou kabeláž mezi kontrolérem a laserem.

[ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) může být neocenitelným nástrojem při řešení problémů s lasery.
