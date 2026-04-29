---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Systém MIDI Send/Receive je oddělený od ovládání APC40 a slouží k přenosu MIDI dat do Liberation i z něj. Funkce jako spouštění a zastavování Clips, úprava globálních nastavení, efektů a parametrů Clip mají přiřazený vlastní MIDI příkaz.

{% hint style="info" %}
Systém MIDI Send/Receive vznikl původně ještě předtím, než Liberation měl jakoukoli funkci Timeline. Byl to náhradní způsob, jak nahrát show do hudebního softwaru, jako je Logic Pro nebo Cubase, a z něj ji pak přehrávat.

Poskytuje přímé ovládání Clips, efektů a nastavení bez ohledu na zobrazení a pozici posunu v Clip Deck. Pokročilejší systémové možnosti živého ovládání, jako je tap tempo, přiřazování zones nebo arm/disarm, nejsou implementovány.
{% endhint %}

### Nastavení MIDI Send/Receive

Otevřete panel _MIDI Send/Receive_ pomocí nabídky _View -> MIDI Send/Receive_. Uvidíte možnosti _SEND, RECEIVE_ a _BOTH_ pro odesílání a příjem, stejně jako možnost vybrat, která MIDI rozhraní chcete používat.

{% hint style="danger" %}
Nastavení _BOTH_ používejte opatrně. MIDI zařízení a software mohou být nakonfigurovány tak, aby posílaly zpět data, která přijmou. To může způsobit zpětnovazební smyčku MIDI dat, což není dobré.
{% endhint %}

### MIDI mapování

Viz [Výchozí mapování odesílání a příjmu MIDI](../reference/midi-send-receive-default-mapping.md)

Do budoucna plánuji přidat mnohem lépe přizpůsobitelné MIDI mapování. Mezitím ale můžete použít aplikace jako [BOME](https://www.bome.com/products/miditranslator) a [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) k převodu mezi Liberation a vaším vlastním hardwarem.
