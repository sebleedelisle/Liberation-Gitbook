---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Hvad hvis Liberation ikke vil åbne?

Det sker sjældent, men Liberation kan nogle gange fejle ved opstart eller crashe lige efter åbning. Det skyldes næsten altid, at en af de lokale konfigurationsfiler er blevet beskadiget - typisk efter et systemnedbrud eller noget uventet på din computer.

Heldigvis er det nemt at løse ved at nulstille dine lokale indstillinger. Her kan du se, hvordan du gør på macOS og Windows.

> **Vigtigt**
>
> * Luk Liberation, før du gør noget.
> * Disse trin påvirker kun lokale indstillinger, logs og caches. Din licens og konto er sikre.

***

#### Hvor finder du arbejdsmappen

Hver version af Liberation har sin egen arbejdsmappe. Hvis du for eksempel kører version 1.0.0, hedder mappen 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Sådan åbner du mappen hurtigt**

**macOS**

1. I Finder skal du trykke på **Shift + Cmd + G**.
2.  Indsæt denne sti, og tryk på **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Åbn den mappe, der matcher dit versionsnummer, for eksempel `1.0.0`.

**Windows**

1.  Tryk på **Win + R**, indsæt dette, og tryk på **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Åbn den mappe, der matcher dit versionsnummer, for eksempel `1.0.0`.

> **Tip til Windows**: Hvis du i stedet navigerer via File Explorer, skal du slå skjulte elementer til: **View > Show > Hidden items**.

***

#### Trin 1 – Nulstil din indstillingsfil sikkert

Åbn dette i din versionsmappe:

```
data/liberation/
```

I liberation-mappen bør du finde en fil kaldet se`ttings.json`. Slet denne fil.

* **macOS-eksempel**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows-eksempel**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Prøv nu at starte Liberation. Hvis programmet åbner, er du færdig.

***

#### Trin 2 – Tjek for en problematisk clip

Hvis Liberation crashede, mens du redigerede en clip, er det muligt, at noget i den clip-fil forårsager problemet.

I samme mappe som din settings.json-fil bør du finde en fil kaldet clipEdit`.json`

Lav en backup af denne fil et sikkert sted (for eksempel på Desktop), og slet den derefter fra Liberations arbejdsmappe.

Prøv at starte Liberation igen. Hvis programmet nu åbner normalt, bedes du sende den backup-fil til [**info@liberationlaser.com**](mailto:info@liberationlaser.com), så vi kan undersøge, hvad der forårsagede problemet.

***

#### Trin 3 - Lav en backup, og slet derefter hele arbejdsmappen

Hvis trin 1 og trin 2 ikke hjalp:

1. **Lav en backup** af hele versionsmappen:
   * macOS: Højreklik på mappen `1.0.0`, og vælg **Compress** for at lave en zip-fil, eller kopiér den til et sikkert sted, f.eks. Desktop.
   * Windows: Højreklik på mappen `1.0.0`, og vælg **Send to > Compressed (zipped) folder**, eller kopiér den til et sikkert sted, f.eks. Desktop.
2. Når du har lavet en backup, skal du **slette** den oprindelige `1.0.0`-mappe fra Liberations arbejdsplacering.
3. Start Liberation igen. Programmet opretter en ny, frisk arbejdsmappe.

Hvis Liberation nu åbner, skal du fortsætte til trin 4.

***

#### Trin 4 - Send os backuppen

Det hjælper os med at finde ud af, hvad der forårsagede problemet, så vi kan forhindre det i fremtidige versioner.

Zip din **backup** fra trin 3, hvis du ikke allerede har gjort det, og send den derefter via e-mail, så vi kan diagnosticere årsagen.

* **Til**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Emne**: Liberation-opstartsfix - backup af arbejdsmappe
* **Brødtekst**: Medtag venligst:
  * Operativsystem og version (f.eks. macOS 14.6 eller Windows 11 23H2)
  * Liberation-version (f.eks. 1.0.0)
  * Hvilket trin der løste det, hvis nogen (trin 1, trin 2 eller trin 3)
  * En kort beskrivelse af, hvad der skete, før problemet opstod
* **Vedhæftning**: den zippede backup af din `1.0.0`-arbejdsmappe.

> Hvis zip-filen er for stor til e-mail, kan du uploade den til et cloud-drev og dele et link.

***

#### Starter programmet stadig ikke efter trin 3?

Hvis Liberation stadig ikke vil åbne efter sletning af arbejdsmappen:

* Genstart computeren, og prøv igen.
* Deaktiver midlertidigt antivirus- eller sikkerhedsværktøjer, der kan blokere nye mapper, og prøv derefter at starte programmet.
* Installer den nyeste Liberation-build oven på din eksisterende installation.
* Hvis intet af ovenstående virker, skal du kontakte support på [**info@liberationlaser.com**](mailto:info@liberationlaser.com) med detaljer og eventuelle crash logs fra undermappen `logs`, hvis den findes.

***

#### Oversigt

1. Slet `data/liberation/settings.json` i din versionsopdelte arbejdsmappe.
2. Hvis du redigerede en clip, skal du lave en backup og derefter slette `data/liberation/clipEdit.json`.
3. Hvis programmet stadig ikke åbner, skal du lave en backup og derefter slette hele mappen `1.0.0` (eller din version).
4. Hvis trin 3 løser det (eller hvis det ikke gør), skal du zippe backuppen og sende den til [**info@liberationlaser.com**](mailto:info@liberationlaser.com) med dit OS og din Liberation-version.
