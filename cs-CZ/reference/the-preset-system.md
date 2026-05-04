---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Systém presetů

Systém presetů se v Liberation používá na různých místech, kdykoli je potřeba uložit více volitelných nastavení do seznamu _presetů_.

Tento systém se aktuálně používá pro:

* nastavení skenerů
* nastavení kalibrace barev
* nastavení kamery 3D vizualizéru
* nastavení laserů ve 3D vizualizéru
* profily DMX

Pokud tedy vyladíte nastavení skenerů pro své nové skenery CT6210, můžete je uložit jako preset, pojmenovat ho „CT6210“ a od té chvíle bude dostupný v seznamu presetů, kdykoli ho budete v budoucnu potřebovat, a také v rozbalovací nabídce.

Všechny presety se ukládají spolu s projektem (nebo nastavením laseru), bez ohledu na to, zda je právě používáte. Kdykoli tedy některý z těchto souborů načtete, všechny presety uvnitř se přidají k vašim stávajícím presetům. Pokud má některý z načtených presetů stejný název jako některý z vašich stávajících presetů, stávající preset se přepíše.

Soubory presetů můžete také importovat a exportovat pomocí tlačítka pro načtení/uložení (ikona diskety) vedle rozbalovacího seznamu presetů. Otevře se vyskakovací okno s tlačítky pro import/export a také s možností odstranit jeden nebo více presetů.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>The pop-up menu that opens when you click the load/save icon</p></figcaption></figure>

Pokud upravíte preset, například nastavení skenerů s názvem _Default_, mějte na paměti, že ostatní lasery se automaticky neaktualizují. Místo toho bude každé jejich nastavení skenerů označeno jako _Default(edited)_. Chcete-li ho aktualizovat na nový preset _Default_, znovu ho vyberte v rozbalovacím seznamu.

{% hint style="info" %}
Pokud máte hodně laserů a chcete aktualizovat nastavení skenerů u všech, použijte systém _COPY LASER SETTINGS_. Viz [Kopírování nastavení laserů](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Pokud odstraníte preset, který se používá jinde, o dané nastavení nepřijdete. Uvidíte ho pouze označené jako _(deleted)._
