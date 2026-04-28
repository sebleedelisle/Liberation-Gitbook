---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introduksjon

Liberations 3D Visualiser er en svært nyttig funksjon – du kan designe og finjustere showene dine uten å trenge lasere i det hele tatt! Den har vist seg å være et uvurderlig verktøy for meg, spesielt ved komplekse oppsett med mange lasere.

### Navigere i 3D-rommet

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>3D Visualiser-visningen</p></figcaption></figure>

* Klikk og dra for å rotere visningen rundt rotasjonspunktet
* Bruk musehjulet for å bevege deg bakover og fremover mot rotasjonspunktet
* Klikk og dra mens du holder Shift-tasten nede for å flytte kameraet sideveis (strafe) til venstre, høyre, opp og ned langs XY-planet
* Dobbeltklikk hvor som helst i visualisereren for å tilbakestille kameraposisjonen

### Innstillinger

Åpne _3D Visualiser Settings_-panelet via _Window_-menyen.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>3D Visualiser Settings-panelet</p></figcaption></figure>

* **Visualiser size** – endrer størrelsen på visualisereren i forhold til resten av appen
* **Brightness Adjustment** – endrer hvor lyse laserne ser ut
* **Show laser numbers** – viser det relevante nummeret over hver laser
* **Show zone names** – viser de relevante sonenavnene under hver laser

### Kamerainnstillinger

Disse innstillingene gjelder hovedsakelig det virtuelle kameraet i 3D-rommet. Du ser en rullegardinmeny med forhåndsinnstillinger for disse innstillingene, som du kan lagre og laste inn på nytt.

* **Camera distance -** Kameraet peker alltid mot rotasjonspunktet sitt. Kameraavstanden er hvor langt unna kameraet er fra dette punktet. Du kan også justere denne innstillingen med musehjulet.
* **FOV -** Field of view – bestemmer hvor vidvinklet eller innzoomet kameraet er.
* **Orbit position** – beskriver gjeldende rotasjon rundt rotasjonspunktet. Den første verdien er rotasjonen rundt X-aksen (pitch), og den andre verdien er rotasjonen rundt Y-aksen (yaw).
* **Orbit centre point** – posisjonen til rotasjonspunktet i 3D-rommet, x, y, z.
* **Grid height** – høyden på rutenettet fra «bakken» (altså der y = 0).

### Innholdsinnstillinger

Disse innstillingene bestemmer hvor laserne (og Canvas) plasseres i 3D-miljøet. Du ser en rullegardinmeny med forhåndsinnstillinger for disse innstillingene, som du kan lagre og laste inn på nytt.

#### Lasers

Hver laser har sin egen gruppe med innstillinger som du kan utvide med den lille hvite trekanten.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Laserinnstillinger for 3D Visualiser</p></figcaption></figure>

* **3D Position** – laserens x-, y- og z-posisjon.
* **3D Orientation** – laserens rotasjon rundt hver av x-, y- og z-aksene.
* **Flip X / Flip Y** – speilvender den virtuelle utgangen fra laseren – MERK at dette ikke skal være nødvendig. Det er bedre å bruke flip-/orienteringsinnstillingene for laseren for å korrigere eventuelle avvik i maskinvaren din.
* **Output Range horizontal / vertical** – gjelder maks-/min-vinkelen til skannerne i laseren din. 60º er standard, men du kan justere dette hvis laserne dine er annerledes.

#### Canvas

Hvis du bruker Canvas-systemet, kan du også velge å inkludere Canvas-bildet i 3D-visningen. Aktiver avkrysningsboksen for å vise Canvas i visualisereren, og bruk innstillingene for posisjon, orientering og skala for å bestemme hvordan det ser ut i 3D-visningen din.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Canvas-innstillinger for 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Ser du «spøkelseslasere»? 3D Visualiser er delvis uavhengig av laseroppsettet, og det er mulig å ha flere lasere i visualisereren enn du har i Liberation. Når du legger til en laser i prosjektet, legges det også til et nytt laserobjekt i visualisereren. Men hvis du sletter en laser, blir det fortsatt liggende igjen et «spøkelseslaser»-objekt i visualisereren.

For å fjerne alle spøkelseslaserne klikker du på _Remove extra 3D laser objects_-knappen (nederst i 3D Visualiser-innstillingspanelet).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
