---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Sustav preseta

Sustav preseta koristi se na raznim mjestima u Liberationu kad god je potrebno spremiti više postavki koje se mogu odabrati s popisa _preseta_.

Taj se sustav trenutačno koristi za:

* Postavke skenera
* Postavke kalibracije boja
* Postavke kamere 3D vizualizatora
* Postavke lasera 3D vizualizatora
* DMX profile

Dakle, ako podesite postavke skenera za svoje nove CT6210 skenere, možete ih spremiti kao preset, nazvati ga „CT6210” i on će vam ubuduće biti dostupan na popisu preseta i u padajućem izborniku kad god vam zatreba.

Svi presetovi spremaju se zajedno s vašim projektom (ili postavkama lasera), bez obzira na to koristite li ih ili ne. Zato će se svaki put kad učitate jednu od tih datoteka svi presetovi iz nje dodati vašim postojećim presetovima. Ako jedan od učitanih preseta ima isti naziv kao neki od postojećih, prebrisat će postojeći preset.

Preset datoteke možete i uvoziti i izvoziti pomoću gumba za učitavanje/spremanje (ikona diskete) pokraj padajućeg popisa preseta. Time se otvara skočni prozor s gumbima za uvoz/izvoz, kao i mogućnošću brisanja jednog ili više preseta.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>The pop-up menu that opens when you click the load/save icon</p></figcaption></figure>

Ako uredite preset, recimo postavku skenera pod nazivom _Default_, imajte na umu da se ostali laseri neće automatski ažurirati. Umjesto toga, njihove će postavke skenera sada imati oznaku _Default(edited)_. Da biste ih ažurirali na novi preset _Default_, ponovno ga odaberite s padajućeg popisa.

{% hint style="info" %}
Ako imate mnogo lasera i želite ažurirati postavke skenera za sve njih, upotrijebite sustav _COPY LASER SETTINGS_. Pogledajte [Kopiranje postavki lasera](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Ako izbrišete preset koji se koristi drugdje, nećete izgubiti postavku, nego će se prikazati s oznakom _(deleted)._
