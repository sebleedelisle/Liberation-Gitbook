---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Färgkalibrering

Färgkalibrering ser till att projektorns röda, gröna och blå lasrar avger ljus på ett jämnt och förutsägbart sätt vid alla ljusstyrkor. Olika projektorer kan ha icke-linjära ljusstyrkekurvor, vilket innebär att 50 % rött kan se mycket starkare eller svagare ut än halva intensiteten av 100 % rött. Kalibreringen korrigerar detta så att färger blandas rent, gradienter blir jämna och vitt blir balanserat.

#### Värm upp projektorn

Laserdioder ändrar beteende när de värms upp. Låt alltid projektorn stabiliseras före kalibrering:

* Projicera en ljusstark bildruta, till exempel **White rectangle test pattern (11)**, i minst **15–20 minuter**.
* Detta gör att färgbalansen du ställer in håller sig konsekvent under en show.

#### Så fungerar kalibreringstestet

Använd testmönstren för kalibrering (se [Testmönster](../output-view/test-patterns.md "mention"))

* **5** – Röd
* **6** – Grön
* **7** – Blå
* **8** – Vit

Varje testmönster visar fyra rörliga linjer. Ljusstyrkan i ett lasersystem påverkas inte bara av effektnivån, utan också av hur länge strålen stannar på en plats. När skannrarna rör sig snabbare stannar strålen kortare tid på varje punkt och upplevs som svagare.

För att ta hänsyn till detta skalar testmönstren både ljusstyrka och hastighet tillsammans:

* **Översta linjen** – 100 % ljusstyrka vid full hastighet
* **Andra linjen** – 75 % ljusstyrka vid 75 % hastighet
* **Tredje linjen** – 50 % ljusstyrka vid 50 % hastighet
* **Fjärde linjen** – 25 % ljusstyrka vid 25 % hastighet

Eftersom både ljusstyrka _och hastighet_ skalas tillsammans ska alla linjer se lika ljusstarka ut. Om en linje ser ljusare eller svagare ut justerar du motsvarande reglage tills de matchar.

Varje testmönster har också en femte linje vid **0 % ljusstyrka**, som inte ska synas. Den används för att korrigera lasrar som inte avger något ljus alls vid mycket låga nivåer. Om lasern fortfarande är osynlig vid låg ljusstyrka ökar du gradvis **0% setting** tills linjen precis syns, och sänker sedan något tills den försvinner igen. Målet är att hitta tröskeln där lasern börjar lysa, och sedan ligga precis under den – så att toningar startar naturligt utan att den nedre delen av området kapas.

#### Använda panelen Colour Calibration

Panelen ger dig separata kontroller för varje kanal (röd, grön, blå) vid nivåerna 100, 75, 50, 25 och 0 %.

1. **Välj ett testmönster** (börja med rött).
2. **Justera reglagen** så att linjerna för 100, 75, 50 och 25 % ser lika ljusstarka ut.
3. **Finjustera reglaget för 0 %** om ”off”-linjen fortfarande syns svagt.
4. **Upprepa för grönt och blått.**
5. Växla till **White test pattern (8)**. Alla fyra linjer ska se likvärdiga ut, och det vita ska upplevas neutralt (inte färgtonat).

#### Justera vitbalansen

Du kan också använda det här systemet för att justera **vitbalans**. När du har kalibrerat varje kanal separat växlar du till **White test pattern (8)**. Om output ser färgtonad ut (till exempel för grön eller för blå) justerar du de relativa nivåerna för de röda, gröna och blå kanalerna tills linjerna ser neutralt vita ut. Även om lasrarnas effekt skiljer sig mycket åt hjälper kalibreringen till att föra dem närmare varandra och ge en renare, mer balanserad färgblandning.

#### Spara kalibreringen

* Använd **Store** för att skriva över den aktuella preseten.
* Använd **Store As** för att skapa en ny preset (praktiskt om du arbetar med flera lasrar).
