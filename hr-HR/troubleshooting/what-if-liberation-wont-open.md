---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Što ako se Liberation ne otvara?

Rijetko se događa, ali Liberation se ponekad možda neće pokrenuti ili se može srušiti odmah nakon otvaranja. To se gotovo uvijek dogodi zato što je neka lokalna konfiguracijska datoteka oštećena - obično nakon rušenja sustava ili nečeg neočekivanog na vašem računalu.

Srećom, to se lako može popraviti resetiranjem lokalnih postavki. Evo kako to učiniti na macOS i Windows sustavu.

> **Važno**
>
> * Zatvorite Liberation prije bilo kakvih promjena.
> * Ovi koraci utječu samo na lokalne postavke, zapisnike i predmemorije. Vaša licenca i korisnički račun su sigurni.

***

#### Gdje pronaći radnu mapu

Svaka verzija aplikacije Liberation ima vlastitu radnu mapu. Na primjer, ako koristite verziju 1.0.0, naziv mape bit će 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Kako brzo otvoriti mapu**

**macOS**

1. U Finderu pritisnite **Shift + Cmd + G**.
2.  Zalijepite ovu putanju i pritisnite **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Otvorite mapu koja odgovara broju vaše verzije, na primjer `1.0.0`.

**Windows**

1.  Pritisnite **Win + R**, zalijepite ovo i pritisnite **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Otvorite mapu koja odgovara broju vaše verzije, na primjer `1.0.0`.

> **Savjet za Windows**: Ako mapu pregledavate putem Eksplorera za datoteke, uključite prikaz skrivenih stavki: **Prikaz > Prikaži > Skrivene stavke**.

***

#### Korak 1 – Sigurno resetirajte datoteku s postavkama

Unutar mape svoje verzije otvorite:

```
data/liberation/
```

U mapi liberation trebali biste pronaći datoteku pod nazivom `settings.json`. Izbrišite tu datoteku.

* **Primjer za macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Primjer za Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Sada pokušajte pokrenuti Liberation. Ako se otvori, završili ste.

***

#### Korak 2 – Provjerite postoji li problematičan Clip

Ako se Liberation srušio dok ste uređivali Clip, moguće je da nešto u toj Clip datoteci uzrokuje problem.

U istoj mapi u kojoj se nalazi datoteka settings.json trebali biste pronaći datoteku pod nazivom `clipEdit.json`

Izradite sigurnosnu kopiju te datoteke na sigurno mjesto (na primjer, na radnu površinu), zatim je izbrišite iz radne mape aplikacije Liberation.

Ponovno pokušajte pokrenuti Liberation. Ako se sada otvara normalno, pošaljite sigurnosnu kopiju datoteke e-poštom na [**info@liberationlaser.com**](mailto:info@liberationlaser.com) kako bismo mogli istražiti što je uzrokovalo problem.

***

#### Korak 3 - Izradite sigurnosnu kopiju, zatim izbrišite cijelu radnu mapu

Ako Korak 1 i Korak 2 nisu pomogli:

1. **Izradite sigurnosnu kopiju** cijele mape verzije:
   * macOS: Desnom tipkom kliknite mapu `1.0.0` i odaberite **Compress** kako biste napravili zip datoteku, ili je kopirajte na sigurno mjesto, primjerice na radnu površinu.
   * Windows: Desnom tipkom kliknite mapu `1.0.0` i odaberite **Send to > Compressed (zipped) folder**, ili je kopirajte na sigurno mjesto, primjerice na radnu površinu.
2. Nakon izrade sigurnosne kopije **izbrišite** izvornu mapu `1.0.0` s radne lokacije aplikacije Liberation.
3. Ponovno pokrenite Liberation. Aplikacija će ponovno stvoriti svježu radnu mapu.

Ako se Liberation sada otvara, prijeđite na Korak 4.

***

#### Korak 4 - Pošaljite nam sigurnosnu kopiju

To nam pomaže utvrditi što je uzrokovalo problem kako bismo ga mogli spriječiti u budućim verzijama.

Ako to već niste učinili, zapakirajte svoju **sigurnosnu kopiju** iz Koraka 3 u zip datoteku, zatim nam je pošaljite e-poštom kako bismo mogli dijagnosticirati uzrok.

* **Prima**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Predmet**: Popravak pokretanja Liberation - sigurnosna kopija radne mape
* **Poruka**: Uključite sljedeće:
  * Operacijski sustav i verziju (npr. macOS 14.6 ili Windows 11 23H2)
  * Verziju aplikacije Liberation (npr. 1.0.0)
  * Koji je korak riješio problem, ako jest (Korak 1, Korak 2 ili Korak 3)
  * Kratak opis onoga što se dogodilo prije nego što je problem počeo
* **Privitak**: zip sigurnosne kopije vaše radne mape `1.0.0`.

> Ako je zip datoteka prevelika za e-poštu, prenesite je na cloud disk i podijelite poveznicu.

***

#### I dalje se ne pokreće nakon Koraka 3?

Ako se Liberation i dalje ne otvara nakon brisanja radne mape:

* Ponovno pokrenite računalo i pokušajte ponovno.
* Privremeno onemogućite antivirusni ili sigurnosni alat koji bi mogao blokirati nove mape, zatim pokušajte pokrenuti aplikaciju.
* Ponovno instalirajte najnoviju verziju aplikacije Liberation preko postojeće instalacije.
* Ako ništa od navedenog ne uspije, kontaktirajte podršku na [**info@liberationlaser.com**](mailto:info@liberationlaser.com) s pojedinostima i svim zapisnicima o rušenju iz podmape `logs`, ako postoje.

***

#### Sažetak

1. Izbrišite `data/liberation/settings.json` u radnoj mapi svoje verzije.
2. Ako ste uređivali Clip, izradite sigurnosnu kopiju, zatim izbrišite `data/liberation/clipEdit.json`.
3. Ako se i dalje ne otvara, izradite sigurnosnu kopiju, zatim izbrišite cijelu mapu `1.0.0` (ili mapu svoje verzije).
4. Ako Korak 3 riješi problem (ili ako ga ne riješi), zapakirajte sigurnosnu kopiju u zip datoteku i pošaljite je na [**info@liberationlaser.com**](mailto:info@liberationlaser.com) uz svoj OS i verziju aplikacije Liberation.
