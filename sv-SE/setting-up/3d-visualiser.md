---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introduktion

Liberations 3D Visualiser är en otroligt användbar funktion – du kan designa och finjustera dina shower utan att behöva några lasrar alls! Den har visat sig vara ett ovärderligt verktyg för mig, särskilt vid mer komplexa riggar med många lasrar.

### Navigera i 3D-utrymmet

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Vyn 3D Visualiser</p></figcaption></figure>

* Klicka och dra för att rotera vyn runt omloppspunkten
* Använd mushjulet för att flytta bakåt och framåt mot omloppspunkten
* Klicka och dra medan du håller ned Shift-tangenten för att flytta kameran i sidled (strafe) åt vänster, höger, uppåt och nedåt längs XY-planet
* Dubbelklicka var som helst i visualiseraren för att återställa kamerapositionen

### Settings

Öppna panelen _3D Visualiser Settings_ via menyn _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Panelen 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - ändrar visualiserarens storlek i förhållande till resten av appen
* **Brightness Adjustment** - ändrar hur ljusa lasrarna visas
* **Show laser numbers** - visar det relevanta numret ovanför varje laser
* **Show zone names** - visar de relevanta zonnamnen under varje laser

### Kamerainställningar

De här inställningarna gäller främst den virtuella kameran i 3D-utrymmet. Du ser en rullgardinsmeny med förinställningar för dessa inställningar som du kan spara och läsa in igen.

* **Camera distance -** Kameran är alltid riktad mot sin _Orbit point_. Camera distance anger hur långt bort den är från denna punkt. Du kan också justera den här inställningen med mushjulet.
* **FOV -** Field of view – avgör hur vidvinklig eller inzoomad kameran är.
* **Orbit position** - beskriver den aktuella rotationen runt omloppspunkten. Det första värdet är rotationen runt X-axeln (pitch) och det andra värdet är rotationen runt Y-axeln (yaw).
* **Orbit centre point** - omloppspunktens position i 3D-utrymmet, x, y, z.
* **Grid height** - rutnätets höjd från "marken" (dvs. där y = 0).

### Innehållsinställningar

De här inställningarna avgör var lasrarna (och canvas) placeras i 3D-miljön. Du ser en rullgardinsmeny med förinställningar för dessa inställningar som du kan spara och läsa in igen.

#### Lasers

Varje laser har en egen grupp med inställningar som du kan expandera med den lilla vita triangeln.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Laserinställningar för 3D Visualiser</p></figcaption></figure>

* **3D Position** - laserns x-, y- och z-position.
* **3D Orientation** - laserns rotation runt var och en av x-, y- och z-axlarna.
* **Flip X / Flip Y** - vänder laserns virtuella output – OBS att detta inte bör behövas. Det är bättre att använda laserns flip-/orienteringsinställningar för att korrigera eventuella avvikelser i din hårdvara.
* **Output Range horizontal / vertical** - gäller max-/minvinkeln för laserns scanners. 60º är standard, men du kan justera detta om dina lasrar skiljer sig åt.

#### Canvas

Om du använder canvas-systemet kan du också välja att inkludera canvas-bilden i 3D-vyn. Aktivera kryssrutan för att rendera canvas i vyn och använd inställningarna för position, orientation och scale för att bestämma hur den ska se ut i din 3D-vy.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Canvas-inställningar för 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Ser du "spök"-lasrar? 3D Visualiser är till viss del oberoende av laseruppsättningen, och det är möjligt att ha fler lasrar i visualiseraren än du har i Liberation. När du lägger till en laser i ditt projekt läggs även ett nytt laserobjekt till i visualiseraren. Men om du tar bort en laser finns ett "spök"-laserobjekt fortfarande kvar i visualiseraren.

För att bli av med alla spök-lasrar klickar du på knappen _Remove extra 3D laser objects_ (längst ned i panelen 3D Visualiser Settings).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
