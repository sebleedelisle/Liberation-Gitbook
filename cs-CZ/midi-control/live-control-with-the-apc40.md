---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Živé MIDI kontrolery

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

Toto je výchozí hardwarový controller pro Liberation; důrazně ho doporučujeme a dá se říct, že Liberation byl od začátku navrhován právě kolem tohoto hardwaru. Jakmile APC40 připojíte, Liberation se k němu okamžitě automaticky připojí.

{% hint style="warning" %}
_Ale ne! Uprostřed show se mi vytáhl USB konektor!_

Žádná panika – jednoduše ho znovu zapojte. Liberation se automaticky znovu připojí, bez zbytečných komplikací.
{% endhint %}

### APC40 Mark 1, nebo Mark 2?

Stručně řečeno doporučujeme Mark 2, protože má plnobarevná tlačítka, která lépe odpovídají rozhraní Clip Deck v Liberation. Verze Mark 1 v nouzi fungovat bude, ale bude o něco méně přehledná, protože její rozložení se mírně liší od toho, co vidíte na obrazovce, a tlačítka mohou svítit pouze červeně, oranžově nebo zeleně, takže nebudou odpovídat barvám Clips.

{% hint style="info" %}
Původní APC40 Mark 1 vyšel v roce 2009 (!) a někteří lidé ho stále preferují kvůli kovovému tělu a robustnímu konzolovému provedení. Aktualizovaný Mark 2 vyšel v roce 2014, a přestože byla jeho výroba v roce 2024 ukončena, v roce 2025 se kvůli poptávce ze strany vizuálních umělců (Resolume apod.) a laseristů vrací do výroby.
{% endhint %}

Úplný seznam ovládacích prvků dostupných na APC40 najdete v části [Referenční přehled APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 obsahuje také profil pro APC Mini. Mapuje mřížku Clips 8×5, tlačítka zone, ovládání převrácení zone v osách X/Y, tlačítka skupin, zastavení všech Clips, přepínání stránek Clips, přepínání stránek zone, tap tempo, reset taktu a jemné posunutí tempa. Jeho fadery ovládají úrovně efektů a fadery se Shiftem ovládají parametry efektů. Poslední fader ovládá globální jas.

### MIDI Fighter Twister

Profil MIDI Fighter Twister je určený spíše pro ovládání s důrazem na enkodéry než pro spouštění Clips. Jedna řada enkodérů ovládá parametr 1 pro sloty efektů 1–8 a další řada sleduje osm kontextových ovládacích prvků v panelu Parameters, včetně posunu Clip, zpoždění zone, globální rotace/změny měřítka a prolnutí skupin.
