---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Ciljna područja Canvas

Već znamo kako dijelove Canvas proslijediti u zones unutar svakog lasera, ali da biste sadržaj uopće doveli na Canvas, trebat će vam (zbunjujuće, ali točno nazvana) _ciljna područja Canvas_.

_Ciljna područja Canvas_ dijelovi su Canvas u koje možete crtati Clips, a u prikazu _CANVAS_ prikazana su kao plavi obrubljeni pravokutnici.

Često će vam trebati samo jedno ciljno područje Canvas, koje zatim možete podijeliti u više zones koje se šalju različitim laserima.

Ponekad ćete možda htjeti više ciljnih područja Canvas za različite dijelove zgrade ili kako biste iskoristili zone delay između njih. (Da! Zone delay i dalje radi između ciljnih područja Canvas!)

### Slanje Clips u ciljna područja Canvas

Ako pogledate u Clip Deck, uz gumbe za beam zone vidjet ćete i gumbe za ciljna područja Canvas. Možda ćete morati pomaknuti gumbe Output kako biste ih vidjeli; upotrijebite `Shift + Left / Right Arrow`, gumbe ZONE PAGE na zaslonu ili gumbe na APC40 (pogledajte [APC40 referenca](../reference/apc40-reference.md "mention"))

Dodijelite Clips ciljnim područjima Canvas uključivanjem ili isključivanjem ovih gumba na potpuno isti način kao i kod gumba za beam zone.

### Dodavanje / uređivanje ciljnih područja Canvas

U gornjoj traci izbornika odaberite _View -> Canvas Target Areas_ — vidjet ćete sve postavke za svako ciljno područje Canvas u svojem projektu.

Na vrhu se nalazi gumb _ADD CANVAS TARGET AREA_.

Ciljno područje Canvas izbrišite crvenim gumbom sa znakom minus.

Veličinu i položaj prilagodite klizačima. Dvaput kliknite klizač da biste upisali vrijednost.

### Način skaliranja

* **FIT TO AREA** — smanjuje sadržaj tako da u cijelosti stane unutar ciljnog područja Canvas, uz zadržavanje omjera širine i visine. (Ovo je zadana postavka)
* **FILL AREA** — rasteže sadržaj tako da ispuni ciljno područje Canvas, uz zadržavanje omjera širine i visine. Sadržaj može biti odrezan na rubovima.
* **STRETCH TO FIT** — rasteže sadržaj tako da ispuni cijelo ciljno područje Canvas, bez obzira na omjer širine i visine.
