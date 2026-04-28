---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ A Preset rendszer

A Preset rendszer a Liberation több pontján is használatos, amikor több, egy _preset_ listából kiválasztható beállítást kell tárolni.

A rendszer jelenleg ezekhez használható:

* Scanner settings
* Colour calibration settings
* 3D visualiser camera settings
* 3D visualiser laser settings
* DMX profiles

Ha tehát beállítod a scanner settings értékeit az új CT6210 scannereidhez, elmentheted presetként, például "CT6210" néven. Ezután bármikor elérhető lesz a preset listában, amikor később szükséged van rá, és megjelenik a legördülő menüben.

Minden preset a projekteddel (vagy a lézerbeállításokkal) együtt mentődik, függetlenül attól, hogy éppen használod-e őket. Ezért amikor betöltesz egy ilyen fájlt, a benne lévő összes preset hozzáadódik a meglévő presetjeidhez. Ha valamelyik betöltött preset neve megegyezik egy már meglévő preset nevével, akkor felülírja a meglévőt.

Preset fájlokat külön is importálhatsz és exportálhatsz a preset legördülő lista melletti load/save gombbal (floppy ikon). Ez egy felugró ablakot nyit meg, amelyben import/export gombok találhatók, valamint lehetőség van egy vagy több preset törlésére is.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>A felugró menü, amely a load/save ikonra kattintva nyílik meg</p></figcaption></figure>

Ha szerkesztesz egy presetet, például a _Default_ nevű scanner settinget, vedd figyelembe, hogy a többi lézer nem frissül automatikusan. Ehelyett mindegyik scanner settings címkéje _Default(edited)_ lesz. Ha ezt az új _Default_ presetre szeretnéd frissíteni, válaszd ki újra a legördülő listából.

{% hint style="info" %}
Ha sok lézered van, és mindegyik scanner settings értékét frissíteni szeretnéd, használd a _COPY LASER SETTINGS_ rendszert. Lásd: [copy-laser-settings.md](../setting-up/copy-laser-settings.md)
{% endhint %}

Ha törölsz egy máshol használt presetet, a beállítás nem veszik el, hanem _(deleted)_ címkével jelenik meg.
