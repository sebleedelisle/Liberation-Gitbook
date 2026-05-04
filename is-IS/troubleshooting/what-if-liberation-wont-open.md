---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Hvað ef Liberation opnast ekki?

Það gerist sjaldan, en stundum getur Liberation ekki ræst sig eða hrynur strax eftir opnun. Þetta stafar nær alltaf af því að ein af staðbundnu stillingaskránum hefur skemmst – yfirleitt eftir kerfishrun eða eitthvað óvænt í tölvunni.

Sem betur fer er auðvelt að laga þetta með því að endurstilla staðbundnu stillingarnar. Hér er hvernig þú gerir það í macOS og Windows.

> **Mikilvægt**
>
> * Lokaðu Liberation áður en þú gerir eitthvað annað.
> * Þessi skref hafa aðeins áhrif á staðbundnar stillingar, logs og skyndiminni. Leyfið þitt og aðgangurinn eru örugg.

***

#### Hvar finnurðu vinnumöppuna?

Hver útgáfa af Liberation hefur sína eigin vinnumöppu. Ef þú ert til dæmis að nota útgáfu 1.0.3 heitir mappan 1.0.3.

* **macOS**: `~/Library/Application Support/Liberation/1.0.3`
* **Windows**: `AppData\Local\Liberation\1.0.3`

**Fljótleg leið til að opna möppuna**

**macOS**

1. Í Finder skaltu ýta á **Shift + Cmd + G**.
2.  Límdu þessa slóð inn og ýttu á **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Opnaðu möppuna sem samsvarar útgáfunúmerinu þínu, til dæmis `1.0.3`.

**Windows**

1.  Ýttu á **Win + R**, límdu þetta inn og ýttu á **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Opnaðu möppuna sem samsvarar útgáfunúmerinu þínu, til dæmis `1.0.3`.

> **Ábending fyrir Windows**: Ef þú flettir í gegnum File Explorer í staðinn skaltu virkja falin atriði: **View > Show > Hidden items**.

***

#### Skref 1 – Endurstilltu stillingaskrána á öruggan hátt

Opnaðu eftirfarandi möppu inni í útgáfumöppunni þinni:

```
data/liberation/
```

Í liberation-möppunni ættirðu að finna skrá sem heitir `settings.json`. Eyddu þessari skrá.

* **Dæmi fyrir macOS**: `~/Library/Application Support/Liberation/1.0.3/data/liberation/settings.json`
* **Dæmi fyrir Windows**: `%LOCALAPPDATA%\Liberation\1.0.3\data\liberation\settings.json`

Reyndu nú að ræsa Liberation. Ef forritið opnast er þessu lokið.

***

#### Skref 2 – Athugaðu hvort vandamálið tengist tilteknu Clip

Ef Liberation hrundi á meðan þú varst að breyta Clip gæti eitthvað í skránni fyrir það Clip verið að valda vandanum.

Í sömu möppu og `settings.json` skráin ættirðu að finna skrá sem heitir `clipEdit.json`

Taktu afrit af þessari skrá á öruggum stað (til dæmis á Desktop) og eyddu henni síðan úr Liberation vinnumöppunni.

Reyndu að ræsa Liberation aftur. Ef forritið opnast nú eðlilega skaltu senda afritið af skránni í tölvupósti á [**info@liberationlaser.com**](mailto:info@liberationlaser.com) svo við getum skoðað hvað olli vandanum.

***

#### Skref 3 - Taktu afrit og eyddu síðan allri vinnumöppunni

Ef skref 1 og skref 2 hjálpuðu ekki:

1. **Taktu afrit** af allri útgáfumöppunni:
* macOS: Hægrismelltu á `1.0.3` möppuna og veldu **Compress** til að búa til zip-skrá, eða afritaðu hana á öruggan stað eins og Desktop.
* Windows: Hægrismelltu á `1.0.3` möppuna og veldu **Send to > Compressed (zipped) folder**, eða afritaðu hana á öruggan stað eins og Desktop.
2. Þegar afritið er tilbúið skaltu **eyða** upprunalegu `1.0.3` möppunni úr Liberation vinnusvæðinu.
3. Ræstu Liberation aftur. Forritið býr þá til nýja vinnumöppu.

Ef Liberation opnast nú skaltu halda áfram í skref 4.

***

#### Skref 4 - Sendu okkur afritið

Þetta hjálpar okkur að finna hvað olli vandanum svo við getum komið í veg fyrir hann í framtíðarútgáfum.

Þjappaðu **afritinu** úr skrefi 3 í zip-skrá ef þú hefur ekki þegar gert það og sendu það síðan í tölvupósti svo við getum greint orsökina.

* **Til**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Efni**: Liberation start-up fix - working folder backup
* **Meginmál**: Láttu eftirfarandi fylgja:
  * Stýrikerfi og útgáfu (t.d. macOS 14.6 eða Windows 11 23H2)
* Liberation útgáfu (t.d. 1.0.3)
  * Hvaða skref lagaði vandann, ef eitthvað þeirra gerði það (skref 1, skref 2 eða skref 3)
  * Stutta lýsingu á því hvað gerðist áður en vandinn kom upp
* **Viðhengi**: zip-skráin með afritinu af `1.0.3` vinnumöppunni þinni.

> Ef zip-skráin er of stór fyrir tölvupóst skaltu hlaða henni upp á skýjadrif og deila hlekk.

***

#### Opnast forritið enn ekki eftir skref 3?

Ef Liberation opnast enn ekki eftir að vinnumöppunni hefur verið eytt:

* Endurræstu tölvuna og reyndu aftur.
* Slökktu tímabundið á vírusvörn eða öryggisverkfærum sem gætu hindrað nýjar möppur og reyndu síðan að ræsa forritið.
* Settu nýjustu Liberation útgáfuna upp aftur yfir núverandi uppsetningu.
* Ef ekkert af þessu virkar skaltu hafa samband við þjónustuver á [**info@liberationlaser.com**](mailto:info@liberationlaser.com) með nánari upplýsingum og öllum hrunskrám úr `logs` undirmöppunni, ef hún er til staðar.

***

#### Samantekt

1. Eyddu `data/liberation/settings.json` í útgáfumerktu vinnumöppunni þinni.
2. Ef þú varst að breyta Clip skaltu taka afrit og eyða síðan `data/liberation/clipEdit.json`.
3. Ef forritið opnast enn ekki skaltu taka afrit og eyða síðan allri `1.0.3` möppunni (eða möppunni fyrir þína útgáfu).
4. Ef skref 3 lagar vandann (eða ef það lagar hann ekki), þjappaðu afritinu í zip-skrá og sendu hana á [**info@liberationlaser.com**](mailto:info@liberationlaser.com) ásamt stýrikerfi og Liberation útgáfu.
