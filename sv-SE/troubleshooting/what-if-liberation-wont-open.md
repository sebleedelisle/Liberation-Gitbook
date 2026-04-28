---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Vad gör jag om Liberation inte öppnas?

Det är ovanligt, men ibland kan Liberation misslyckas med att starta eller krascha direkt efter att det har öppnats. Det beror nästan alltid på att en av de lokala konfigurationsfilerna har blivit skadad – oftast efter en systemkrasch eller något annat oväntat på datorn.

Som tur är är det enkelt att åtgärda genom att återställa dina lokala inställningar. Så här gör du på macOS och Windows.

> **Viktigt**
>
> * Stäng Liberation innan du gör något.
> * De här stegen påverkar bara lokala inställningar, loggar och cachefiler. Din licens och ditt konto påverkas inte.

***

#### Var du hittar arbetsmappen

Varje version av Liberation har en egen arbetsmapp. Om du till exempel kör version 1.0.0 heter mappen 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Så öppnar du mappen snabbt**

**macOS**

1. Tryck på **Shift + Cmd + G** i Finder.
2.  Klistra in den här sökvägen och tryck på **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Öppna mappen som motsvarar ditt versionsnummer, till exempel `1.0.0`.

**Windows**

1.  Tryck på **Win + R**, klistra in detta och tryck på **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Öppna mappen som motsvarar ditt versionsnummer, till exempel `1.0.0`.

> **Tips för Windows**: Om du bläddrar via File Explorer i stället, aktivera dolda objekt: **View > Show > Hidden items**.

***

#### Steg 1 – Återställ inställningsfilen på ett säkert sätt

Öppna följande i din versionsmapp:

```
data/liberation/
```

I liberation-mappen bör du hitta en fil som heter se`ttings.json`. Ta bort den här filen.

* **Exempel för macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Exempel för Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Försök nu starta Liberation. Om det öppnas är du klar.

***

#### Steg 2 – Kontrollera om en Clip orsakar problem

Om Liberation kraschade medan du redigerade en Clip kan något i den Clip-filen orsaka problemet.

I samma mapp som filen settings.json bör du hitta en fil som heter clipEdit`.json`

Säkerhetskopiera filen till en säker plats (till exempel skrivbordet) och ta sedan bort den från Liberations arbetsmapp.

Försök starta Liberation igen. Om det nu öppnas normalt ber vi dig mejla den säkerhetskopierade filen till [**info@liberationlaser.com**](mailto:info@liberationlaser.com) så att vi kan undersöka vad som orsakade problemet.

***

#### Steg 3 - Säkerhetskopiera och ta sedan bort hela arbetsmappen

Om Steg 1 och Steg 2 inte hjälpte:

1. **Säkerhetskopiera** hela versionsmappen:
   * macOS: Högerklicka på mappen `1.0.0` och välj **Compress** för att skapa en zip-fil, eller kopiera den till en säker plats som skrivbordet.
   * Windows: Högerklicka på mappen `1.0.0` och välj **Send to > Compressed (zipped) folder**, eller kopiera den till en säker plats som skrivbordet.
2. När du har säkerhetskopierat, **ta bort** den ursprungliga mappen `1.0.0` från Liberations arbetsplats.
3. Starta Liberation igen. Programmet återskapar en ny arbetsmapp.

Om Liberation nu öppnas, fortsätt till Steg 4.

***

#### Steg 4 - Skicka säkerhetskopian till oss

Det hjälper oss att identifiera vad som orsakade problemet så att vi kan förhindra det i framtida versioner.

Zippa din **säkerhetskopia** från Steg 3 om du inte redan har gjort det, och mejla den sedan till oss så att vi kan diagnostisera orsaken.

* **Till**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Ämne**: Liberation start-up fix - working folder backup
* **Meddelande**: Inkludera:
  * Operativsystem och version (t.ex. macOS 14.6 eller Windows 11 23H2)
  * Liberation-version (t.ex. 1.0.0)
  * Vilket steg som löste problemet, om något (Steg 1, Steg 2 eller Steg 3)
  * En kort beskrivning av vad som hände innan problemet började
* **Bilaga**: den zippade säkerhetskopian av din `1.0.0`-arbetsmapp.

> Om zip-filen är för stor för e-post, ladda upp den till en molntjänst och dela en länk.

***

#### Startar det fortfarande inte efter Steg 3?

Om Liberation fortfarande inte öppnas efter att du har tagit bort arbetsmappen:

* Starta om datorn och försök igen.
* Inaktivera tillfälligt antivirus- eller säkerhetsverktyg som kan blockera nya mappar, och försök sedan starta programmet.
* Installera om den senaste Liberation-versionen ovanpå din befintliga installation.
* Om inget av ovanstående fungerar, kontakta support på [**info@liberationlaser.com**](mailto:info@liberationlaser.com) med information och eventuella kraschloggar från undermappen `logs`, om den finns.

***

#### Sammanfattning

1. Ta bort `data/liberation/settings.json` i din versionsspecifika arbetsmapp.
2. Om du redigerade en Clip, säkerhetskopiera och ta sedan bort `data/liberation/clipEdit.json`.
3. Om det fortfarande inte öppnas, säkerhetskopiera och ta sedan bort hela mappen `1.0.0` (eller din version).
4. Om Steg 3 löser problemet (eller om det inte gör det), zippa säkerhetskopian och skicka den till [**info@liberationlaser.com**](mailto:info@liberationlaser.com) tillsammans med ditt operativsystem och din Liberation-version.
