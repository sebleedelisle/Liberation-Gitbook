---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Hvad hvis Liberation ikke vil åbne?

Det sker sjældent, men nogle gange kan Liberation ikke starte, eller også lukker programmet ned lige efter åbning. Det skyldes næsten altid, at en af de lokale konfigurationsfiler er blevet beskadiget - typisk efter et systemnedbrud eller noget uventet på din computer.

Heldigvis er det nemt at løse ved at nulstille dine lokale indstillinger. Sådan gør du på macOS og Windows.

> **Vigtigt**
>
> * Luk Liberation, før du gør noget.
> * Disse trin påvirker kun lokale indstillinger, logfiler og cachefiler. Din licens og konto er i sikkerhed.

***

#### Hvor finder du arbejdsmappen?

Hver version af Liberation har sin egen arbejdsmappe. Hvis du f.eks. kører version 1.0.3, hedder mappen 1.0.3.

* **macOS**: `~/Library/Application Support/Liberation/1.0.3`
* **Windows**: `AppData\Local\Liberation\1.0.3`

**Sådan åbner du mappen hurtigt**

**macOS**

1. Tryk på **Shift + Cmd + G** i Finder.
2.  Indsæt denne sti, og tryk på **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Åbn den mappe, der svarer til dit versionsnummer, f.eks. `1.0.3`.

**Windows**

1.  Tryk på **Win + R**, indsæt dette, og tryk på **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Åbn den mappe, der svarer til dit versionsnummer, f.eks. `1.0.3`.

> **Tip til Windows**: Hvis du i stedet finder mappen via File Explorer, skal du slå skjulte elementer til: **View > Show > Hidden items**.

***

#### Trin 1 – Nulstil din indstillingsfil på en sikker måde

Åbn dette inde i din versionsmappe:

```
data/liberation/
```

I liberation-mappen bør du finde en fil, der hedder `settings.json`. Slet denne fil.

* **macOS-eksempel**: `~/Library/Application Support/Liberation/1.0.3/data/liberation/settings.json`
* **Windows-eksempel**: `%LOCALAPPDATA%\Liberation\1.0.3\data\liberation\settings.json`

Prøv nu at starte Liberation. Hvis programmet åbner, er du færdig.

***

#### Trin 2 – Tjek, om en Clip giver problemer

Hvis Liberation lukkede ned, mens du redigerede en Clip, kan noget i filen for den pågældende Clip være årsagen til problemet.

I samme mappe som din settings.json-fil bør du finde en fil, der hedder `clipEdit.json`

Lav en sikkerhedskopi af denne fil et sikkert sted (f.eks. på skrivebordet), og slet den derefter fra Liberations arbejdsmappe.

Prøv at starte Liberation igen. Hvis programmet nu åbner normalt, må du meget gerne sende den sikkerhedskopierede fil til [**info@liberationlaser.com**](mailto:info@liberationlaser.com), så vi kan undersøge, hvad der forårsagede problemet.

***

#### Trin 3 - Lav en sikkerhedskopi, og slet derefter hele arbejdsmappen

Hvis trin 1 og trin 2 ikke hjalp:

1. Lav en **sikkerhedskopi** af hele versionsmappen:
* macOS: Højreklik på mappen `1.0.3`, og vælg **Compress** for at lave en zip-fil, eller kopiér den til et sikkert sted, f.eks. skrivebordet.
* Windows: Højreklik på mappen `1.0.3`, og vælg **Send to > Compressed (zipped) folder**, eller kopiér den til et sikkert sted, f.eks. skrivebordet.
2. Når du har lavet sikkerhedskopien, skal du **slette** den oprindelige `1.0.3`-mappe fra Liberations arbejdsplacering.
3. Start Liberation igen. Programmet opretter en ny arbejdsmappe.

Hvis Liberation nu åbner, skal du fortsætte til trin 4.

***

#### Trin 4 - Send os sikkerhedskopien

Det hjælper os med at finde årsagen til problemet, så vi kan forhindre det i fremtidige versioner.

Pak din **sikkerhedskopi** fra trin 3 som zip, hvis du ikke allerede har gjort det, og send den derefter til os, så vi kan diagnosticere årsagen.

* **Til**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Emne**: Liberation start-up fix - working folder backup
* **Besked**: Medtag venligst:
  * Operativsystem og version (f.eks. macOS 14.6 eller Windows 11 23H2)
* Liberation-version (f.eks. 1.0.3)
  * Hvilket trin der løste problemet, hvis nogen (trin 1, trin 2 eller trin 3)
  * En kort beskrivelse af, hvad der skete, før problemet opstod
* **Vedhæftet fil**: den zippede sikkerhedskopi af din `1.0.3`-arbejdsmappe.

> Hvis zip-filen er for stor til e-mail, kan du uploade den til et cloud-drev og dele et link.

***

#### Starter programmet stadig ikke efter trin 3?

Hvis Liberation stadig ikke vil åbne, efter at du har slettet arbejdsmappen:

* Genstart computeren, og prøv igen.
* Deaktivér midlertidigt antivirus- eller sikkerhedsværktøjer, der kan blokere nye mapper, og prøv derefter at starte programmet.
* Geninstaller den nyeste Liberation-build oven i din eksisterende installation.
* Hvis intet af ovenstående virker, skal du kontakte support på [**info@liberationlaser.com**](mailto:info@liberationlaser.com) med detaljer og eventuelle crash-logs fra undermappen `logs`, hvis den findes.

***

#### Oversigt

1. Slet `data/liberation/settings.json` i din versionsopdelte arbejdsmappe.
2. Hvis du redigerede en Clip, skal du lave en sikkerhedskopi og derefter slette `data/liberation/clipEdit.json`.
3. Hvis programmet stadig ikke åbner, skal du lave en sikkerhedskopi og derefter slette hele mappen `1.0.3` (eller din versionsmappe).
4. Hvis trin 3 løser problemet (eller hvis det ikke gør), skal du zippe sikkerhedskopien og sende den til [**info@liberationlaser.com**](mailto:info@liberationlaser.com) sammen med dit operativsystem og din Liberation-version.
