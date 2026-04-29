---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Farvekalibrering

Farvekalibrering sikrer, at projektorens røde, grønne og blå lasere udsender lys på en jævn og forudsigelig måde ved alle lysstyrkeniveauer. Forskellige projektorer kan have ikke-lineære lysstyrkekurver, hvilket betyder, at 50 % rød kan se langt lysere eller mørkere ud end halvdelen af intensiteten ved 100 % rød. Kalibrering retter dette, så farver blandes rent, gradueringer ser jævne ud, og hvid er balanceret.

#### Opvarmning af projektoren

Laserdioder ændrer adfærd, når de varmer op. Lad altid projektoren stabilisere sig før kalibrering:

* Projicér en lys frame, f.eks. **White rectangle test pattern (11)**, i mindst **15–20 minutter**.
* Det sikrer, at den farvebalance, du indstiller, forbliver stabil under et show.

#### Sådan fungerer kalibreringstesten

Brug testmønstrene til kalibrering (se [Testmønstre](../output-view/test-patterns.md "mention"))

* **5** – Rød
* **6** – Grøn
* **7** – Blå
* **8** – Hvid

Hvert af disse viser fire bevægelige linjer:

* **Øverste linje** – 100 % lysstyrke ved fuld hastighed
* **Anden linje** – 75 % lysstyrke ved 75 % hastighed
* **Tredje linje** – 50 % lysstyrke ved 50 % hastighed
* **Fjerde linje** – 25 % lysstyrke ved 25 % hastighed

Fordi både lysstyrke _og hastighed_ skaleres sammen, bør alle linjerne se ud til at have samme lysstyrke. Hvis en linje ser lysere eller mørkere ud, skal du justere den tilsvarende skyder, indtil de matcher.

Hvert testmønster har også en femte linje ved **0 % lysstyrke**, som ikke bør være synlig. Den bruges til at korrigere for lasere, der ikke udsender lys ved meget lave niveauer. Hvis din laser forbliver usynlig ved lav lysstyrke, skal du gradvist øge **0% setting**, indtil linjen lige akkurat bliver synlig, og derefter sænke den lidt igen, indtil den forsvinder. Målet er at finde tærsklen, hvor laseren begynder at lyse, og derefter holde sig lige under den – så dine fades starter naturligt uden at afskære det nederste område.

#### Brug af Colour Calibration-panelet

Panelet giver dig uafhængig kontrol for hver kanal (rød, grøn, blå) ved niveauerne 100, 75, 50, 25 og 0 %.

1. **Vælg et testmønster** (start med rød).
2. **Juster skyderne**, så linjerne ved 100, 75, 50 og 25 % ser ud til at have samme lysstyrke.
3. **Finjustér 0%-skyderen**, hvis “off”-linjen stadig er svagt synlig.
4. **Gentag for grøn og blå.**
5. Skift til **White test pattern (8)**. Alle fire linjer bør se ens ud, og den hvide farve bør fremstå neutral (uden farvestik).

#### Justering af hvidbalance

Du kan også bruge dette system til at justere **hvidbalance**. Når du har kalibreret hver kanal individuelt, skal du skifte til **White test pattern (8)**. Hvis outputtet ser farvet ud (f.eks. for grønt eller for blåt), skal du justere de relative niveauer for de røde, grønne og blå kanaler, indtil linjerne fremstår neutralt hvide. Selv hvis dine lasere har ret forskellig effekt, vil kalibrering stadig hjælpe med at bringe dem tættere på hinanden og give en renere, mere balanceret farveblanding.

#### Gem din kalibrering

* Brug **Store** til at overskrive den aktuelle preset.
* Brug **Store As** til at oprette en ny preset (nyttigt, hvis du arbejder med flere lasere).
