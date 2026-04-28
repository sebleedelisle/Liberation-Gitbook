---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Hva om Liberation ikke åpnes?

Det er sjeldent, men noen ganger kan Liberation ikke starte, eller krasje rett etter åpning. Dette skjer nesten alltid fordi en av de lokale konfigurasjonsfilene har blitt skadet – vanligvis etter et systemkrasj eller noe uventet på datamaskinen.

Heldigvis er det enkelt å fikse ved å tilbakestille de lokale innstillingene. Slik gjør du det på macOS og Windows.

> **Viktig**
>
> * Lukk Liberation før du gjør noe annet.
> * Disse trinnene påvirker bare lokale innstillinger, logger og hurtigbuffer. Lisensen og kontoen din er trygge.

***

#### Hvor du finner arbeidsmappen

Hver versjon av Liberation har sin egen arbeidsmappe. Hvis du for eksempel kjører versjon 1.0.0, heter mappen 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Slik åpner du mappen raskt**

**macOS**

1. I Finder trykker du **Shift + Cmd + G**.
2.  Lim inn denne banen og trykk **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Åpne mappen som samsvarer med versjonsnummeret ditt, for eksempel `1.0.0`.

**Windows**

1.  Trykk **Win + R**, lim inn dette og trykk **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Åpne mappen som samsvarer med versjonsnummeret ditt, for eksempel `1.0.0`.

> **Tips for Windows**: Hvis du blar via File Explorer i stedet, slår du på skjulte elementer: **View > Show > Hidden items**.

***

#### Trinn 1 – Tilbakestill innstillingsfilen på en trygg måte

Inne i versjonsmappen åpner du:

```
data/liberation/
```

I liberation-mappen skal du finne en fil som heter se`ttings.json`. Slett denne filen.

* **macOS-eksempel**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows-eksempel**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Prøv nå å starte Liberation. Hvis programmet åpnes, er du ferdig.

***

#### Trinn 2 – Se etter en problematisk clip

Hvis Liberation krasjet mens du redigerte en clip, kan det hende at noe med den clip-filen forårsaker problemet.

I samme mappe som settings.json-filen skal du finne en fil som heter clipEdit`.json`

Ta en sikkerhetskopi av denne filen et trygt sted (for eksempel på skrivebordet), og slett den deretter fra Liberation-arbeidsmappen.

Prøv å starte Liberation igjen. Hvis programmet nå åpnes normalt, kan du sende den sikkerhetskopierte filen på e-post til [**info@liberationlaser.com**](mailto:info@liberationlaser.com), slik at vi kan undersøke hva som forårsaket problemet.

***

#### Trinn 3 - Sikkerhetskopier, og slett deretter hele arbeidsmappen

Hvis Trinn 1 og Trinn 2 ikke hjalp:

1. **Sikkerhetskopier** hele versjonsmappen:
   * macOS: Høyreklikk på `1.0.0`-mappen og velg **Compress** for å lage en zip-fil, eller kopier den til et trygt sted, for eksempel skrivebordet.
   * Windows: Høyreklikk på `1.0.0`-mappen og velg **Send to > Compressed (zipped) folder**, eller kopier den til et trygt sted, for eksempel skrivebordet.
2. Etter at du har sikkerhetskopiert, **sletter** du den opprinnelige `1.0.0`-mappen fra Liberation-arbeidsplasseringen.
3. Start Liberation igjen. Programmet oppretter en ny arbeidsmappe automatisk.

Hvis Liberation nå åpnes, går du videre til Trinn 4.

***

#### Trinn 4 - Send oss sikkerhetskopien

Dette hjelper oss med å finne ut hva som forårsaket problemet, slik at vi kan forhindre det i fremtidige versjoner.

Pakk **sikkerhetskopien** fra Trinn 3 som zip hvis du ikke allerede har gjort det, og send den deretter på e-post slik at vi kan diagnostisere årsaken.

* **To**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Subject**: Liberation start-up fix - working folder backup
* **Body**: Ta med:
  * Operativsystem og versjon (f.eks. macOS 14.6 eller Windows 11 23H2)
  * Liberation-versjon (f.eks. 1.0.0)
  * Hvilket trinn som løste problemet, hvis noe gjorde det (Trinn 1, Trinn 2 eller Trinn 3)
  * En kort beskrivelse av hva som skjedde før problemet startet
* **Attachment**: den zippede sikkerhetskopien av `1.0.0`-arbeidsmappen.

> Hvis zip-filen er for stor for e-post, laster du den opp til en skytjeneste og deler en lenke.

***

#### Starter fortsatt ikke etter Trinn 3?

Hvis Liberation fortsatt ikke åpnes etter at du har slettet arbeidsmappen:

* Start datamaskinen på nytt og prøv igjen.
* Deaktiver midlertidig antivirus- eller sikkerhetsverktøy som kan blokkere nye mapper, og prøv deretter å starte programmet.
* Installer den nyeste Liberation-builden på nytt over den eksisterende installasjonen.
* Hvis ingen av punktene ovenfor fungerer, kontakter du support på [**info@liberationlaser.com**](mailto:info@liberationlaser.com) med detaljer og eventuelle krasjlogger fra undermappen `logs`, hvis den finnes.

***

#### Oppsummering

1. Slett `data/liberation/settings.json` i den versjonerte arbeidsmappen.
2. Hvis du redigerte en clip, sikkerhetskopierer du og sletter deretter `data/liberation/clipEdit.json`.
3. Hvis programmet fortsatt ikke åpnes, sikkerhetskopierer du og sletter deretter hele `1.0.0`-mappen (eller mappen for din versjon).
4. Hvis Trinn 3 løser problemet (eller hvis det ikke gjør det), zipper du sikkerhetskopien og sender den til [**info@liberationlaser.com**](mailto:info@liberationlaser.com) sammen med operativsystem og Liberation-versjon.
