---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas-kohdealueet

Tiedämme jo, miten Canvasin osia saadaan kunkin laserin zone-alueisiin, mutta jotta sisältö saadaan alun perin Canvasiin, tarvitset hieman hämmentävästi mutta täsmällisesti nimetyt _Canvas-kohdealueet_.

_Canvas-kohdealueet_ ovat Canvasin osia, joihin voit piirtää clippejä. _CANVAS_-näkymässä ne näkyvät sinisinä ääriviivasuorakulmioina.

Usein tarvitset ehkä vain yhden Canvas-kohdealueen, jonka jaat useisiin eri lasereille lähetettäviin zone-alueisiin.

Joskus taas saatat haluta useita Canvas-kohdealueita rakennuksen eri osia varten tai hyödyntää zone delay -viivettä niiden välillä. (Kyllä! Zone delay toimii myös Canvas-kohdealueiden välillä!).

### Clippien lähettäminen Canvas-kohdealueisiin

Clip deckissä beam zone -painikkeiden vieressä näkyvät Canvas-kohdealueiden painikkeet. Saatat joutua vierittämään output-painikkeita nähdäksesi ne. Käytä `Shift + Left / Right Arrow` -näppäimiä, näytön ZONE PAGE -painikkeita tai APC40-painikkeita (katso [APC40-viite](../reference/apc40-reference.md))

Määritä clipit Canvas-kohdealueisiin kytkemällä nämä painikkeet päälle tai pois täsmälleen samalla tavalla kuin beam zone -painikkeiden kanssa.

### Canvas-kohdealueiden lisääminen ja muokkaaminen

Valitse ylävalikkopalkista _View -> Canvas Target Areas_ – näet kaikki projektisi Canvas-kohdealueiden asetukset.

Yläreunassa on _ADD CANVAS TARGET AREA_ -painike.

Poista Canvas-kohdealue punaisella miinusmerkkipainikkeella.

Säädä kokoa ja sijaintia liukusäätimillä. Kaksoisnapsauta liukusäädintä, jos haluat kirjoittaa arvon.

### Scale mode

* **FIT TO AREA** – pienentää sisällön niin, että se mahtuu kokonaan Canvas-kohdealueen sisään ja säilyttää kuvasuhteen. (Tämä on oletusasetus)
* **FILL AREA** – venyttää sisällön täyttämään Canvas-kohdealueen ja säilyttää kuvasuhteen. Sisältö voi leikkautua reunoilta.
* **STRETCH TO FIT** – venyttää sisällön täyttämään koko Canvas-kohdealueen kuvasuhteesta välittämättä.
