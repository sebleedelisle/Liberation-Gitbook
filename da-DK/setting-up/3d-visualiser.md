---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introduktion

Liberations 3D Visualiser er en utrolig nyttig funktion – du kan designe og finjustere dine shows uden overhovedet at have brug for lasere! Den har vist sig at være et uvurderligt værktøj for mig, især ved særligt komplekse opsætninger med mange lasere.

### Navigation i 3D-rummet

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Visningen 3D Visualiser</p></figcaption></figure>

* Klik og træk for at rotere visningen omkring orbitpunktet
* Brug musehjulet til at bevæge dig tilbage og frem mod orbitpunktet
* Klik og træk, mens du holder Shift-tasten nede, for at flytte kameraet sideværts til venstre, højre, op og ned langs XY-planet
* Dobbeltklik hvor som helst i visualiseringen for at nulstille kameraets position

### Indstillinger

Åbn panelet _3D Visualiser Settings_ via menuen _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Panelet 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - ændrer visualiseringens størrelse i forhold til resten af appen
* **Brightness Adjustment** - ændrer, hvor kraftigt laserne vises
* **Show laser numbers** - viser det relevante nummer over hver laser
* **Show zone names** - viser de relevante zonenavne under hver laser

### Kameraindstillinger

Disse indstillinger handler primært om det virtuelle kamera i 3D-rummet. Du kan se en rullemenu med forudindstillinger for disse indstillinger, som du kan gemme og indlæse igen.

* **Camera distance -** Kameraet peger altid mod sit _Orbit point_. Kameraafstanden er, hvor langt det er fra dette punkt. Du kan også justere denne indstilling med musehjulet.
* **FOV -** Field of view – bestemmer, hvor vidvinklet eller indzoomet kameraet er.
* **Orbit position** - beskriver den aktuelle rotation omkring orbitpunktet. Den første værdi er rotationen omkring X-aksen (pitch), og den anden værdi er rotationen omkring Y-aksen (yaw).
* **Orbit centre point** - orbitpunktets position i 3D-rummet, x, y, z.
* **Grid height** - gitterets højde fra "jorden" (dvs. hvor y = 0).

### Indholdsindstillinger

Disse indstillinger bestemmer, hvor laserne (og Canvas) placeres i 3D-miljøet. Du kan se en rullemenu med forudindstillinger for disse indstillinger, som du kan gemme og indlæse igen.

#### Lasere

Hver laser har sin egen gruppe indstillinger, som du kan folde ud med den lille hvide trekant.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Laserindstillinger for 3D Visualiser</p></figcaption></figure>

* **3D Position** - laserens x-, y- og z-position.
* **3D Orientation** - laserens rotation omkring hver af x-, y- og z-akserne.
* **Flip X / Flip Y** - spejlvender laserens virtuelle output – BEMÆRK, at dette normalt ikke bør være nødvendigt. Det er bedre at bruge laserens flip-/orienteringsindstillinger til at rette eventuelle uoverensstemmelser med din hardware.
* **Output Range horizontal / vertical** - relaterer til maks.-/min.-vinklen for laserens scannere. 60º er standard, men du kan justere dette, hvis dine lasere er anderledes.

#### Canvas

Hvis du bruger Canvas-systemet, kan du også vælge at inkludere Canvas-billedet i 3D-visningen. Aktivér afkrydsningsfeltet for at vise Canvas i visningen, og brug indstillingerne for position, orientering og skalering til at bestemme, hvordan det ser ud i din 3D-visning.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Canvas-indstillinger for 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Ser du "spøgelseslasere"? 3D Visualiser er til en vis grad uafhængig af laseropsætningen, og det er muligt at have flere lasere i visualiseringen, end du har i Liberation. Når du føjer en laser til dit projekt, bliver der også tilføjet et nyt laserobjekt i visualiseringen. Men hvis du sletter en laser, vil der stadig være et "spøgelses"-laserobjekt tilbage i visualiseringen.

Klik på knappen _Remove extra 3D laser objects_ for at fjerne alle spøgelseslasere (nederst i panelet 3D Visualiser Settings).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
