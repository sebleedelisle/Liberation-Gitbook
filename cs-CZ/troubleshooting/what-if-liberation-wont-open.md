---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Co když se Liberation neotevře?

Je to vzácné, ale někdy se může stát, že se Liberation nespustí nebo spadne hned po otevření. Téměř vždy je příčinou poškozený některý z místních konfiguračních souborů – obvykle po pádu systému nebo jiné nečekané události v počítači.

Naštěstí se to dá snadno opravit resetováním místních nastavení. Níže najdete postup pro macOS a Windows.

> **Důležité**
>
> * Než začnete, zavřete Liberation.
> * Tyto kroky ovlivní pouze místní nastavení, logy a cache. Vaše licence a účet zůstanou v pořádku.

***

#### Kde najít pracovní složku

Každá verze Liberation má vlastní pracovní složku. Pokud například používáte verzi 1.0.0, název složky bude 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Jak složku rychle otevřít**

**macOS**

1. Ve Finderu stiskněte **Shift + Cmd + G**.
2.  Vložte tuto cestu a stiskněte **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Otevřete složku, která odpovídá číslu vaší verze, například `1.0.0`.

**Windows**

1.  Stiskněte **Win + R**, vložte následující cestu a stiskněte **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Otevřete složku, která odpovídá číslu vaší verze, například `1.0.0`.

> **Tip pro Windows**: Pokud složku procházíte přes Průzkumníka souborů, zapněte skryté položky: **Zobrazení > Zobrazit > Skryté položky**.

***

#### Krok 1 – Bezpečně resetujte soubor s nastavením

Ve složce své verze otevřete:

```
data/liberation/
```

Ve složce liberation by měl být soubor s názvem `settings.json`. Tento soubor smažte.

* **Příklad pro macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Příklad pro Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Teď zkuste Liberation spustit. Pokud se otevře, máte hotovo.

***

#### Krok 2 – Zkontrolujte problematický Clip

Pokud Liberation spadl ve chvíli, kdy jste upravovali některý Clip, může problém způsobovat něco v souboru tohoto Clip.

Ve stejné složce jako soubor settings.json byste měli najít soubor s názvem `clipEdit.json`

Zálohujte tento soubor na bezpečné místo (například na plochu) a potom ho smažte z pracovní složky Liberation.

Zkuste Liberation spustit znovu. Pokud se teď otevře normálně, pošlete nám prosím zálohovaný soubor e-mailem na [**info@liberationlaser.com**](mailto:info@liberationlaser.com), abychom mohli zjistit, co problém způsobilo.

***

#### Krok 3 – Zálohujte a potom smažte celou pracovní složku

Pokud Krok 1 ani Krok 2 nepomohl:

1. **Zálohujte** celou složku verze:
   * macOS: Klikněte pravým tlačítkem na složku `1.0.0` a zvolte **Compress**, čímž vytvoříte zip, nebo ji zkopírujte na bezpečné místo, například na plochu.
   * Windows: Klikněte pravým tlačítkem na složku `1.0.0` a zvolte **Send to > Compressed (zipped) folder**, nebo ji zkopírujte na bezpečné místo, například na plochu.
2. Po vytvoření zálohy **smažte** původní složku `1.0.0` z pracovního umístění Liberation.
3. Spusťte Liberation znovu. Vytvoří si novou čistou pracovní složku.

Pokud se Liberation teď otevře, pokračujte na Krok 4.

***

#### Krok 4 – Pošlete nám zálohu

Pomůže nám to zjistit, co problém způsobilo, abychom mu mohli v budoucích verzích předejít.

Pokud jste svou **zálohu** z Kroku 3 ještě nezazipovali, zazipujte ji a pošlete nám ji e-mailem, abychom mohli příčinu diagnostikovat.

* **Komu**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Předmět**: Oprava spuštění Liberation – záloha pracovní složky
* **Text zprávy**: Uveďte prosím:
  * Operační systém a verzi (např. macOS 14.6 nebo Windows 11 23H2)
  * Verzi Liberation (např. 1.0.0)
  * Který krok problém vyřešil, pokud některý (Krok 1, Krok 2 nebo Krok 3)
  * Stručný popis toho, co se stalo před začátkem problému
* **Příloha**: zazipovaná záloha vaší pracovní složky `1.0.0`.

> Pokud je zip pro e-mail příliš velký, nahrajte ho na cloudové úložiště a sdílejte odkaz.

***

#### Liberation se po Kroku 3 stále nespouští?

Pokud se Liberation po smazání pracovní složky stále neotevře:

* Restartujte počítač a zkuste to znovu.
* Dočasně vypněte antivirové nebo bezpečnostní nástroje, které by mohly blokovat vytváření nových složek, a potom zkuste program spustit.
* Přeinstalujte nejnovější sestavení Liberation přes stávající instalaci.
* Pokud nic z výše uvedeného nepomůže, kontaktujte podporu na [**info@liberationlaser.com**](mailto:info@liberationlaser.com) a přiložte podrobnosti i případné protokoly o pádu z podsložky `logs`, pokud existuje.

***

#### Shrnutí

1. Smažte `data/liberation/settings.json` ve své verzované pracovní složce.
2. Pokud jste upravovali některý Clip, zálohujte a potom smažte `data/liberation/clipEdit.json`.
3. Pokud se Liberation stále neotevře, zálohujte a potom smažte celou složku `1.0.0` (nebo složku své verze).
4. Pokud Krok 3 problém vyřeší (nebo i pokud ne), zazipujte zálohu a pošlete ji na [**info@liberationlaser.com**](mailto:info@liberationlaser.com) spolu s informací o operačním systému a verzi Liberation.
