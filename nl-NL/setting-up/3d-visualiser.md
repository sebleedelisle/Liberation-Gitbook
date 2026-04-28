---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Inleiding

De 3D Visualiser van Liberation is een ontzettend handige functie: je kunt je shows ontwerpen en verfijnen zonder dat je lasers nodig hebt. Voor mij is dit een onmisbaar hulpmiddel gebleken, vooral bij complexe opstellingen met grote aantallen lasers.

### Navigeren in de 3D-ruimte

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>De 3D Visualiser-weergave</p></figcaption></figure>

* Klik en sleep om de weergave rond het draaipunt te roteren
* Gebruik het muiswiel om naar voren en naar achteren te bewegen richting het draaipunt
* Houd Shift ingedrukt en klik en sleep om de camera zijwaarts te verplaatsen (strafe): links, rechts, omhoog en omlaag langs het XY-vlak
* Dubbelklik ergens in de visualiser om de camerapositie te resetten

### Instellingen

Open het _3D Visualiser Settings_-paneel via het _Window_-menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Het 3D Visualiser Settings-paneel</p></figcaption></figure>

* **Visualiser size** - wijzigt de grootte van de visualiser ten opzichte van de rest van de app
* **Brightness Adjustment** - wijzigt hoe helder de lasers worden weergegeven
* **Show laser numbers** - toont het bijbehorende nummer boven elke laser
* **Show zone names** - toont de bijbehorende zonenamen onder elke laser

### Camera-instellingen

Deze instellingen hebben vooral betrekking op de virtuele camera in de 3D-ruimte. Je ziet een dropdownmenu met presets voor deze instellingen, die je kunt opslaan en opnieuw kunt laden.

* **Camera distance -** De camera is altijd gericht op het _draaipunt_. De camera-afstand bepaalt hoe ver de camera van dit punt staat. Je kunt deze instelling ook aanpassen met het muiswiel.
* **FOV -** Field of view: bepaalt hoe groothoekig of ingezoomd de camera is.
* **Orbit position** - beschrijft de huidige rotatie rond het draaipunt. De eerste waarde is de rotatie rond de X-as (pitch) en de tweede waarde is de rotatie rond de Y-as (yaw).
* **Orbit centre point** - de positie van het draaipunt in de 3D-ruimte: x, y, z.
* **Grid height** - de hoogte van het raster vanaf de "grond" (oftewel waar y = 0).

### Content-instellingen

Deze instellingen bepalen waar de lasers (en Canvas) binnen de 3D-omgeving worden geplaatst. Je ziet een dropdownmenu met presets voor deze instellingen, die je kunt opslaan en opnieuw kunt laden.

#### Lasers

Elke laser heeft een eigen groep instellingen die je kunt uitklappen met het kleine witte driehoekje.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Laserinstellingen voor de 3D visualiser</p></figcaption></figure>

* **3D Position** - de x-, y- en z-positie van de laser.
* **3D Orientation** - de rotatie van de laser rond elk van de x-, y- en z-assen.
* **Flip X / Flip Y** - spiegelt de virtuele output van de laser. LET OP: dit zou niet nodig moeten zijn; je kunt beter de flip-/oriëntatie-instellingen van de laser gebruiken om eventuele inconsistenties met je hardware te corrigeren.
* **Output Range horizontal / vertical** - heeft betrekking op de maximale/minimale hoek van de scanners van je laser. 60º is standaard, maar je kunt dit aanpassen als je lasers hiervan afwijken.

#### Canvas

Als je het Canvas-systeem gebruikt, kun je er ook voor kiezen om de Canvas-afbeelding in de 3D-weergave op te nemen. Activeer het selectievakje om de Canvas weer te geven en gebruik de instellingen voor positie, oriëntatie en schaal om te bepalen hoe deze eruitziet in je 3D-weergave.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Canvas-instellingen voor de 3D visualiser</p></figcaption></figure>

{% hint style="info" %}
Zie je "ghost"-lasers? De 3D Visualiser staat enigszins los van de laseropstelling en het is mogelijk om meer lasers in de visualiser te hebben dan in Liberation. Wanneer je een laser aan je project toevoegt, wordt er ook een nieuw laserobject in de visualiser toegevoegd. Maar als je een laser verwijdert, blijft er nog steeds een "ghost"-laserobject in de visualiser achter.

Klik op de knop _Remove extra 3D laser objects_ (onderaan het 3D Visualiser settings-paneel) om alle ghost-lasers te verwijderen.

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
