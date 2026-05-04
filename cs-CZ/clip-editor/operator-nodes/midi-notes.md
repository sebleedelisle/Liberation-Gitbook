---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Vytváří efekty ve stylu „laserové harfy“, kde příchozí MIDI noty spouštějí paprsky nebo tvary v určitém rozsahu. Tento node použije obsah, který do něj pošlete, jako _zdroj_ pro každou notu – pošlete do něj tečku a dostanete řadu teček. Pošlete do něj tvar, například kruh, a dostanete řadu kruhů. Složitější tvary se zreplikují stejným způsobem.

MIDI rozhraní, kterému má Liberation naslouchat, vyberete v **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **MIDI channel** – MIDI kanál, kterému se má naslouchat (0 = všechny kanály, 1–16 = konkrétní kanál)
* **width** – celková šířka, přes kterou se noty rozprostřou.
* **MIDI note min / max** – nejnižší a nejvyšší hodnota MIDI noty v rozsahu.
* **ignore out of range notes** – odfiltruje všechny noty mimo nastavený rozsah. Pokud je vypnuto, noty mimo rozsah se „omezí“ na nejbližší dostupnou notu (vysoké noty spustí horní část rozsahu, nízké noty spodní část).
* **auto extend range** – automaticky rozšíří rozsah, pokud zahrajete noty mimo něj.

{% hint style="info" %}
Nejste si jistí, jaký rozsah not dostáváte? Zapněte **auto extend range**, nastavte **MIDI note min** opravdu vysoko a **MIDI note max** opravdu nízko a potom své noty zahrajte. Systém je všechny zachytí a rozsah vám rozšíří. Jakmile máte vše nastavené, stačí **auto extend range** vypnout a rozsah tím uzamknout.
{% endhint %}

* **leave all notes visible** – vytvoří paprsky nebo tvary pro všechny noty v rozsahu bez ohledu na to, jestli právě hrají. Tím vznikne efekt „laserové harfy“.
* **hit colour** – barva, která se zobrazí při spuštění noty.
* **hit colour hold time** – jak dlouho zůstane barva zásahu na plném jasu, než začne slábnout. Hodnota je v sekundách (0–1). _100 % = 1 sekunda._
* **hit colour decay time** – jak dlouho trvá, než se barva zásahu po době podržení vrátí zpět. Hodnota je v sekundách (0–1). _100 % = 1 sekunda._

{% hint style="info" %}
Pokud je váš obsah už čistě bílý, nastavení barvy zásahu na bílou nic nezmění. Nejlepších výsledků dosáhnete tak, že pro obsah použijete sytou barvu a **hit colour** nastavíte na bílou – při spuštění not tak vznikne velmi pěkný záblesk.
{% endhint %}

* **note off fade out time** – jak dlouho trvá, než nota po uvolnění zeslábne. Hodnota je v sekundách (0–1). _100 % = 1 sekunda._
* **hit scale factor** – o kolik se nota při spuštění zvětší (např. 2 = dvojnásobná velikost).
* **hit scale hold time** – jak dlouho zůstane nota zvětšená, než se začne zmenšovat zpět. Hodnota je v sekundách (0–1). _100 % = 1 sekunda._
* **hit scale decay time** – jak dlouho trvá, než se nota vrátí na původní velikost. Hodnota je v sekundách (0–1). _100 % = 1 sekunda._
* **note off shrink time** – jak dlouho trvá zmenšení zpět na původní velikost po uvolnění noty. Hodnota je v sekundách (0–1). _100 % = 1 sekunda._ (Nemá žádný efekt, když je zapnuté **leave all notes visible**.)

{% hint style="info" %}
Změna měřítka – pokud je vaším obsahem jediná tečka, změna měřítka nebude mít žádný efekt!
{% endhint %}
