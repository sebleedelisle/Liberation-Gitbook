---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Canvas target areas

Vi vet hur du får in delar av canvasen i zoner inom varje laser, men för att få in innehåll i canvasen från början behöver du de (förvirrande men korrekt namngivna) _Canvas target areas._

_Canvas target areas_ är sektioner av canvasen som du kan rita clips in i, och de visas i _CANVAS_-vyn som blå rektanglar med kontur.

Ofta behöver du kanske bara en canvas target area och delar sedan upp den i flera zoner som skickas till olika lasrar.

Ibland kan du vilja ha flera canvas target areas för olika delar av en byggnad, eller för att utnyttja zone delay mellan dem. (Ja! Zone delay fungerar fortfarande mellan canvas target areas!).

### Skicka clips till canvas target areas

Om du tittar i Clip Deck, bredvid knapparna för beam zone, ser du knapparna för canvas target area. Du kan behöva bläddra bland utgångsknapparna för att se dem. Använd `Shift + Left / Right Arrow`, eller ZONE PAGE-knapparna på skärmen, eller APC40-knapparna (se [APC40-referens](../reference/apc40-reference.md "mention"))

Tilldela clips till canvas target areas genom att slå på eller av de här knapparna på exakt samma sätt som du gör med knapparna för beam zone.

### Lägga till/redigera canvas target areas

Välj _View -> Canvas Target Areas_ i den övre menyraden. Där ser du alla inställningar för varje canvas target area som finns i ditt projekt.

Längst upp finns knappen _ADD CANVAS TARGET AREA_.

Ta bort en canvas target area med den röda knappen med ett minustecken.

Justera storlek och position med reglagen. Dubbelklicka på ett reglage för att skriva in ett värde.

### Scale mode

* **FIT TO AREA** – förminskar innehållet så att det får plats helt inom canvas target area, samtidigt som bildförhållandet behålls. (Detta är standardinställningen)
* **FILL AREA** – skalar innehållet så att det fyller canvas target area, samtidigt som bildförhållandet behålls. Innehåll kan beskäras vid kanterna.
* **STRETCH TO FIT** – sträcker ut innehållet så att det fyller hela canvas target area, utan att ta hänsyn till bildförhållandet.
