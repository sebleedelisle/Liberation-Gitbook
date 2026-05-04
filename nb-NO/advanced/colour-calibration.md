---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Fargekalibrering

Fargekalibrering sørger for at projektorens røde, grønne og blå lasere gir lys på en jevn og forutsigbar måte ved alle lysstyrkenivåer. Ulike projektorer kan ha ikke-lineære lysstyrkekurver, som betyr at 50 % rødt kan se mye lysere eller svakere ut enn halvparten av intensiteten til 100 % rødt. Kalibrering korrigerer dette, slik at fargene blandes rent, graderinger ser jevne ut, og hvitt blir balansert.

#### Varme opp projektoren

Laserdioder endrer oppførsel etter hvert som de varmes opp. La alltid projektoren stabilisere seg før kalibrering:

* Projiser en lys ramme, for eksempel **White rectangle test pattern (11)**, i minst **15–20 minutter**.
* Dette sikrer at fargebalansen du angir, holder seg stabil under et show.

#### Slik fungerer kalibreringstesten

Bruk testmønstrene for kalibrering (se [Testmønstre](../output-view/test-patterns.md "mention"))

* **5** – Rød
* **6** – Grønn
* **7** – Blå
* **8** – Hvit

Hvert av disse viser fire bevegelige linjer. Lysstyrken i et lasersystem påvirkes ikke bare av effektnivået, men også av hvor lenge strålen blir værende på ett sted. Når scannerne beveger seg raskere, bruker strålen mindre tid på hvert punkt og ser svakere ut.

For å ta høyde for dette skalerer testmønstrene både lysstyrke og hastighet samtidig:

* **Øverste linje** – 100 % lysstyrke ved full hastighet
* **Andre linje** – 75 % lysstyrke ved 75 % hastighet
* **Tredje linje** – 50 % lysstyrke ved 50 % hastighet
* **Fjerde linje** – 25 % lysstyrke ved 25 % hastighet

Fordi både lysstyrke _og hastighet_ skaleres samtidig, skal alle linjene se ut til å ha samme lysstyrke. Hvis én linje ser lysere eller svakere ut, justerer du den tilhørende skyveknappen til de samsvarer.

Hvert testmønster har også en femte linje ved **0 % lysstyrke**, som ikke skal være synlig. Denne brukes til å korrigere for lasere som ikke sender ut noe lys ved svært lave nivåer. Hvis laseren fortsatt er usynlig ved lav lysstyrke, øker du **0% setting** gradvis til linjen så vidt blir synlig. Deretter senker du den litt til linjen forsvinner igjen. Målet er å finne terskelen der laseren begynner å lyse, og deretter ligge rett under den – slik at fading starter naturlig uten å kutte bort det nederste området.

#### Bruke Colour Calibration-panelet

Panelet gir deg uavhengige kontroller for hver kanal (rød, grønn, blå) ved nivåene 100, 75, 50, 25 og 0 %.

1. **Velg et testmønster** (start med rødt).
2. **Juster skyveknappene** slik at linjene på 100, 75, 50 og 25 % ser ut til å ha samme lysstyrke.
3. **Finjuster 0 %-skyveknappen** hvis «av»-linjen fortsatt er svakt synlig.
4. **Gjenta for grønn og blå.**
5. Bytt til **White test pattern (8)**. Alle fire linjene skal se like ut, og hvitt skal fremstå nøytralt (uten fargestikk).

#### Justere hvitbalansen

Du kan også bruke dette systemet til å justere **hvitbalanse**. Etter at du har kalibrert hver kanal enkeltvis, bytter du til **White test pattern (8)**. Hvis utgangen ser farget ut (for eksempel for grønn eller for blå), justerer du de relative nivåene for de røde, grønne og blå kanalene til linjene fremstår som nøytralt hvite. Selv om laserne har ganske ulik effekt, vil kalibreringen likevel bidra til å bringe dem nærmere hverandre og gi en renere, mer balansert fargeblanding.

#### Lagre kalibreringen

* Bruk **Store** for å overskrive gjeldende forhåndsinnstilling.
* Bruk **Store As** for å opprette en ny forhåndsinnstilling (nyttig hvis du arbeider med flere lasere).
