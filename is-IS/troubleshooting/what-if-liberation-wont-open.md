---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Hvað ef Liberation opnast ekki?

Það gerist sjaldan, en stundum getur Liberation ekki ræst eða hrunnið strax eftir að það opnast. Þetta stafar næstum alltaf af því að ein af staðbundnu stillingaskránum hefur skemmst - yfirleitt eftir kerfishrun eða eitthvað óvænt í tölvunni þinni.

Sem betur fer er auðvelt að laga þetta með því að endurstilla staðbundnu stillingarnar. Hér er hvernig þú gerir það á macOS og Windows.

> **Mikilvægt**
>
> * Lokaðu Liberation áður en þú gerir nokkuð.
> * Þessi skref hafa aðeins áhrif á staðbundnar stillingar, annála og skyndiminni. Leyfið þitt og reikningurinn eru örugg.

***

#### Hvar finnurðu vinnumöppuna?

Hver útgáfa af Liberation hefur sína eigin vinnumöppu. Ef þú ert til dæmis að keyra útgáfu 1.0.0 heitir mappan 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Hvernig opnarðu möppuna fljótt?**

**macOS**

1. Í Finder skaltu ýta á **Shift + Cmd + G**.
2.  Límdu þessa slóð inn og ýttu á **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Opnaðu möppuna sem samsvarar útgáfunúmerinu þínu, til dæmis `1.0.0`.

**Windows**

1.  Ýttu á **Win + R**, límdu þetta inn og ýttu á **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Opnaðu möppuna sem samsvarar útgáfunúmerinu þínu, til dæmis `1.0.0`.

> **Ábending fyrir Windows**: Ef þú ferð í gegnum File Explorer í staðinn skaltu virkja falda hluti: **View > Show > Hidden items**.

***

#### Skref 1 – Endurstilla stillingaskrána á öruggan hátt

Inni í útgáfumöppunni þinni skaltu opna:

```
data/liberation/
```

Inni í liberation-möppunni ættirðu að finna skrá sem heitir se`ttings.json`. Eyddu þessari skrá.

* **Dæmi fyrir macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Dæmi fyrir Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Reyndu nú að ræsa Liberation. Ef það opnast ertu búin(n).

***

#### Skref 2 – Athuga hvort clip valdi vandanum

Ef Liberation hrundi á meðan þú varst að breyta clip getur verið að eitthvað í þeirri clip-skrá sé að valda vandanum.

Í sömu möppu og settings.json skráin ættirðu að finna skrá sem heitir clipEdit`.json`

Taktu afrit af þessari skrá á öruggan stað (til dæmis á Desktop) og eyddu henni svo úr vinnumöppu Liberation.

Reyndu að ræsa Liberation aftur. Ef það opnast núna eðlilega skaltu senda afrituðu skrána með tölvupósti á [**info@liberationlaser.com**](mailto:info@liberationlaser.com) svo við getum rannsakað hvað olli vandanum.

***

#### Skref 3 - Taktu afrit og eyddu svo allri vinnumöppunni

Ef Skref 1 og Skref 2 hjálpuðu ekki:

1. **Taktu afrit** af allri útgáfumöppunni:
   * macOS: Hægrismelltu á `1.0.0` möppuna og veldu **Compress** til að búa til zip-skrá, eða afritaðu hana á öruggan stað eins og Desktop.
   * Windows: Hægrismelltu á `1.0.0` möppuna og veldu **Send to > Compressed (zipped) folder**, eða afritaðu hana á öruggan stað eins og Desktop.
2. Þegar þú hefur tekið afrit skaltu **eyða** upprunalegu `1.0.0` möppunni úr vinnusvæði Liberation.
3. Ræstu Liberation aftur. Það býr til nýja hreina vinnumöppu.

Ef Liberation opnast núna skaltu halda áfram í Skref 4.

***

#### Skref 4 - Sendu okkur afritið

Þetta hjálpar okkur að finna hvað olli vandanum svo við getum komið í veg fyrir hann í framtíðarútgáfum.

Þjappaðu **afritinu** úr Skrefi 3 í zip-skrá ef þú hefur ekki þegar gert það og sendu það svo með tölvupósti svo við getum greint orsökina.

* **Til**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Efni**: Liberation start-up fix - working folder backup
* **Texti**: Láttu fylgja:
  * Stýrikerfi og útgáfu (t.d. macOS 14.6 eða Windows 11 23H2)
  * Liberation útgáfu (t.d. 1.0.0)
  * Hvaða skref lagaði vandann, ef eitthvað þeirra (Skref 1, Skref 2 eða Skref 3)
  * Stutta lýsingu á því hvað gerðist áður en vandinn byrjaði
* **Viðhengi**: zip-afritið af `1.0.0` vinnumöppunni þinni.

> Ef zip-skráin er of stór fyrir tölvupóst skaltu hlaða henni upp á skýjadrif og deila tengli.

***

#### Opnast það enn ekki eftir Skref 3?

Ef Liberation opnast enn ekki eftir að vinnumöppunni hefur verið eytt:

* Endurræstu tölvuna og reyndu aftur.
* Slökktu tímabundið á vírusvörn eða öryggisverkfærum sem gætu lokað á nýjar möppur og reyndu svo að ræsa.
* Settu upp nýjustu Liberation-útgáfuna yfir núverandi uppsetningu.
* Ef ekkert af þessu virkar skaltu hafa samband við þjónustuver í [**info@liberationlaser.com**](mailto:info@liberationlaser.com) með nánari upplýsingum og hrunannálum úr `logs` undirmöppunni ef hún er til staðar.

***

#### Samantekt

1. Eyddu `data/liberation/settings.json` í útgáfumerktu vinnumöppunni þinni.
2. Ef þú varst að breyta clip skaltu taka afrit af `data/liberation/clipEdit.json` og eyða henni síðan.
3. Ef það opnast enn ekki skaltu taka afrit af allri `1.0.0` möppunni (eða möppunni fyrir þína útgáfu) og eyða henni síðan.
4. Ef Skref 3 lagar vandann (eða ef það gerir það ekki), þjappaðu afritinu í zip-skrá og sendu það á [**info@liberationlaser.com**](mailto:info@liberationlaser.com) ásamt stýrikerfi þínu og Liberation-útgáfu.
