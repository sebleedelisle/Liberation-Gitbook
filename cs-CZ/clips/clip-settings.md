---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Nastavení Clip

### Panel Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Panel Clip settings</p></figcaption></figure>

Velikost výstupu pro Clip změníte pomocí _Scale X_ a _Scale Y_. Tyto hodnoty jsou svázané, pokud nestisknete klávesu _SHIFT_.

Vodorovnou a svislou pozici Clip změníte pomocí _Shift X_ a _Shift Y_.

_Zone Delay/Chase_ je tak zábavná funkce, že má vlastní část. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Panel Parameters

Panel napravo od Clip Deck zobrazuje osm kontextových parametrů. Když je vybraný Clip, první ovládací prvky jsou _Shift X_, _Shift Y_ a _Zone Delay_ pro vybraný Clip, za nimi následují globální ovládací prvky _Spin_ a _Scale_.

Tyto stejné parametry se zrcadlí i na podporované MIDI kontrolery. Pokud není vybraný žádný Clip, pozice určené pro konkrétní Clip zůstanou prázdné. Pokud podržíte tlačítko skupiny, první dva ovládací prvky se změní na časy náběhu a doběhu dané skupiny.

### Zamykání Clip

Když je Clip zamčený, nelze ho přesunout ani smazat. Clip zamknete pomocí zaškrtávacího políčka _Locked_ v nabídce po kliknutí pravým tlačítkem. V panelu Clip settings najdete několik dalších možností.

* _UNLOCK ALL -_ odemkne každý Clip v Clip Deck.
* _AUTO-LOCK_ - když je _Auto-Lock_ zapnuté, každý Clip, který se spustí automaticky (buď pomocí časové osy, nebo systému pro záznam a přehrávání MIDI), se zamkne. To se hodí, pokud jste si naprogramovali show v Logic Pro (nebo podobném programu) a nechcete omylem upravit Clips použité v show.
* _LOCKED CLIPS ZONES_ - pokud je tato možnost zapnutá, nemůžete u žádného zamčeného Clip měnit zones.
* _LOCKED CLIPS PARAMS_ - pokud je tato možnost zapnutá, nemůžete u žádného zamčeného Clip měnit parametry (měřítko, posun atd.).

### Nabídka po kliknutí pravým tlačítkem

Když na Clip kliknete pravým tlačítkem, zobrazí se nabídka s některými možnostmi pro daný Clip. Více k prvním položkám v této nabídce najdete v částech [Úvod do Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Nastavení Clip](clip-settings.md "mention") a [Skupiny Clips](groups.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Každý Clip má ve výchozím nastavení zapnutý _retrigger_. To znamená, že ať ho spustíte kdykoli, Clip začne běžet od tohoto okamžiku. Pokud ho tedy spustíte pozdě, animace Clip bude mírně opožděná a mimo rytmus.

{% hint style="info" %}
Pokud během běhu Clip se zapnutým _retrigger_ použijete _Tap Tempo_, systém Clip „kvantizuje“ do rytmu, i když jste ho nespustili přesně na dobu.
{% endhint %}

Pokud _Retrigger_ není zapnutý, Clip bude vždy v rytmu – jako by byl spuštěn hned na úplném začátku časování. Hodí se to ve chvíli, kdy jste dokonale synchronizovaní s hudbou pomocí externího hodinového signálu.

{% hint style="info" %}
Clips jsou často navržené tak, aby se opakovaly donekonečna, ale můžete je navrhnout i tak, aby proběhly jen jednou nebo několikrát. U takových nechte zapnutý _retrigger_, jinak se znovu nespustí!
{% endhint %}

### Doba fade-in/fade-out

Pro Clip lze nastavit náběh a doběh s délkou v sekundách. Ve výchozím stavu se doba fade dědí z nastavení skupiny, do které Clip patří (a lze ji změnit kliknutím pravým tlačítkem na tlačítko skupiny).

Pokud chcete použít jinou dobu fade než u skupiny, do které Clip patří, nejprve vypněte tlačítko _USE GROUP DEFAULT_ a potom upravte posuvníky _In time_ a _Out time_ pro daný Clip.
