---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Wat als Liberation niet opent?

Het komt zelden voor, maar soms start Liberation niet op of crasht het direct na het openen. Dit gebeurt bijna altijd doordat een van de lokale configuratiebestanden beschadigd is geraakt - meestal na een systeemcrash of iets onverwachts op je computer.

Gelukkig is dit eenvoudig op te lossen door je lokale instellingen te resetten. Hieronder lees je hoe je dat doet op macOS en Windows.

> **Belangrijk**
>
> * Sluit Liberation voordat je iets doet.
> * Deze stappen hebben alleen invloed op lokale instellingen, logs en caches. Je licentie en account blijven veilig.

***

#### Waar je de werkmap vindt

Elke versie van Liberation heeft een eigen werkmap. Als je bijvoorbeeld versie 1.0.0 gebruikt, heet de map 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**De map snel openen**

**macOS**

1. Druk in Finder op **Shift + Cmd + G**.
2.  Plak dit pad en druk op **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Open de map die overeenkomt met je versienummer, bijvoorbeeld `1.0.0`.

**Windows**

1.  Druk op **Win + R**, plak dit en druk op **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Open de map die overeenkomt met je versienummer, bijvoorbeeld `1.0.0`.

> **Tip voor Windows**: Als je via File Explorer bladert, schakel dan verborgen items in: **View > Show > Hidden items**.

***

#### Stap 1 – Reset je instellingenbestand veilig

Open in je versiemap:

```
data/liberation/
```

In de map liberation vind je als het goed is een bestand met de naam `settings.json`. Verwijder dit bestand.

* **macOS-voorbeeld**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Windows-voorbeeld**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Probeer Liberation nu te starten. Als het opent, ben je klaar.

***

#### Stap 2 – Controleer op een problematische clip

Als Liberation crashte terwijl je een clip aan het bewerken was, kan iets in dat clipbestand het probleem veroorzaken.

In dezelfde map als je settings.json-bestand vind je als het goed is een bestand met de naam `clipEdit.json`

Maak een back-up van dit bestand op een veilige plek (bijvoorbeeld je Desktop) en verwijder het daarna uit de Liberation-werkmap.

Probeer Liberation opnieuw te starten. Als het nu normaal opent, mail het back-upbestand dan naar [**info@liberationlaser.com**](mailto:info@liberationlaser.com), zodat we kunnen onderzoeken wat het probleem heeft veroorzaakt.

***

#### Stap 3 - Maak een back-up en verwijder daarna de hele werkmap

Als Stap 1 en Stap 2 niet hebben geholpen:

1. Maak een **back-up** van de volledige versiemap:
   * macOS: Klik met de rechtermuisknop op de map `1.0.0` en kies **Compress** om een zipbestand te maken, of kopieer de map naar een veilige plek zoals Desktop.
   * Windows: Klik met de rechtermuisknop op de map `1.0.0` en kies **Send to > Compressed (zipped) folder**, of kopieer de map naar een veilige plek zoals Desktop.
2. Verwijder na het maken van de back-up de oorspronkelijke map `1.0.0` uit de Liberation-werklocatie.
3. Start Liberation opnieuw. Er wordt automatisch een nieuwe, schone werkmap aangemaakt.

Als Liberation nu opent, ga dan door naar Stap 4.

***

#### Stap 4 - Stuur ons de back-up

Dit helpt ons te achterhalen wat het probleem heeft veroorzaakt, zodat we dit in toekomstige versies kunnen voorkomen.

Zip je **back-up** uit Stap 3 als je dat nog niet had gedaan en mail deze naar ons, zodat we de oorzaak kunnen onderzoeken.

* **Aan**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Onderwerp**: Liberation opstartfix - back-up van werkmap
* **Bericht**: Vermeld het volgende:
  * Besturingssysteem en versie (bijv. macOS 14.6 of Windows 11 23H2)
  * Liberation-versie (bijv. 1.0.0)
  * Welke stap het probleem heeft opgelost, als dat zo is (Stap 1, Stap 2 of Stap 3)
  * Een korte beschrijving van wat er gebeurde voordat het probleem begon
* **Bijlage**: de gezipte back-up van je `1.0.0`-werkmap.

> Als het zipbestand te groot is voor e-mail, upload het dan naar een clouddrive en deel een link.

***

#### Start Liberation nog steeds niet na Stap 3?

Als Liberation nog steeds niet opent nadat je de werkmap hebt verwijderd:

* Start je computer opnieuw op en probeer het nog een keer.
* Schakel antivirus- of beveiligingstools die nieuwe mappen kunnen blokkeren tijdelijk uit en probeer Liberation daarna te starten.
* Installeer de nieuwste Liberation-build over je bestaande installatie heen.
* Als geen van bovenstaande stappen werkt, neem dan contact op met support via [**info@liberationlaser.com**](mailto:info@liberationlaser.com) met details en eventuele crashlogs uit de submap `logs`, als die aanwezig is.

***

#### Samenvatting

1. Verwijder `data/liberation/settings.json` in je versiegebonden werkmap.
2. Als je een clip aan het bewerken was, maak dan een back-up van `data/liberation/clipEdit.json` en verwijder het daarna.
3. Als Liberation nog steeds niet opent, maak dan een back-up van de hele map `1.0.0` (of jouw versie) en verwijder die daarna.
4. Als Stap 3 het oplost (of ook als dat niet zo is), zip de back-up en stuur deze naar [**info@liberationlaser.com**](mailto:info@liberationlaser.com) met je besturingssysteem en Liberation-versie.
