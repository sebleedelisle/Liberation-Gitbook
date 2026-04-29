---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Uvod

Liberationova značajka 3D Visualiser iznimno je korisna — možete dizajnirati i dorađivati svoje showove bez ikakvih lasera! Meni se pokazala kao neprocjenjiv alat, posebno kod složenih postava s velikim brojem lasera.

### Kretanje kroz 3D prostor

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Prikaz 3D Visualiser</p></figcaption></figure>

* Kliknite i povucite za rotiranje prikaza oko točke orbitiranja
* Kotačićem miša pomičite se natrag i naprijed prema točki orbitiranja
* Kliknite i povucite uz pritisnutu tipku shift za bočno pomicanje kamere lijevo, desno, gore i dolje po XY ravnini
* Dvaput kliknite bilo gdje u prikazu 3D Visualiser za vraćanje položaja kamere na početne vrijednosti

### Postavke

Otvorite panel _3D Visualiser Settings_ putem izbornika _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Panel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - mijenja veličinu prikaza 3D Visualiser u odnosu na ostatak aplikacije
* **Brightness Adjustment** - mijenja koliko laseri izgledaju svijetlo
* **Show laser numbers** - prikazuje odgovarajući broj iznad svakog lasera
* **Show zone names** - prikazuje odgovarajuće nazive zone ispod svakog lasera

### Postavke kamere

Ove se postavke uglavnom odnose na virtualnu kameru u 3D prostoru. Dostupan je padajući izbornik s presetima za te postavke, koje možete spremiti i ponovno učitati.

* **Camera distance -** Kamera je uvijek usmjerena prema svojoj _točki orbitiranja_. Camera distance određuje koliko je kamera udaljena od te točke. Ovu postavku možete prilagoditi i kotačićem miša.
* **FOV -** Vidno polje — određuje koliko je širok kut kamere odnosno koliko je prikaz zumiran.
* **Orbit position** - opisuje trenutačnu rotaciju oko točke orbitiranja. Prva vrijednost je rotacija oko osi X (pitch), a druga vrijednost rotacija oko osi Y (yaw).
* **Orbit centre point** - položaj točke orbitiranja u 3D prostoru: x, y, z.
* **Grid height** - visina mreže od „tla” (tj. mjesta gdje je y = 0).

### Postavke sadržaja

Ove postavke određuju gdje su laseri (i Canvas) smješteni unutar 3D okruženja. Dostupan je padajući izbornik s presetima za te postavke, koje možete spremiti i ponovno učitati.

#### Laseri

Svaki laser ima vlastitu grupu postavki koju možete proširiti malim bijelim trokutićem.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Postavke lasera za 3D Visualiser</p></figcaption></figure>

* **3D Position** - položaj lasera po osima x, y i z.
* **3D Orientation** - rotacija lasera oko svake od osi x, y i z.
* **Flip X / Flip Y** - preokreće virtualni izlaz lasera — NAPOMENA: ovo ne bi trebalo biti potrebno. Bolje je koristiti postavke za preokretanje/orijentaciju lasera kako biste ispravili eventualne neusklađenosti s hardverom.
* **Output Range horizontal / vertical** - odnosi se na maksimalni/minimalni kut skenera vašeg lasera. 60º je standardno, ali to možete prilagoditi ako su vaši laseri drukčiji.

#### Canvas

Ako koristite sustav Canvas, možete uključiti i sliku Canvas unutar 3D view. Označite potvrdni okvir za prikaz Canvas i upotrijebite postavke položaja, orijentacije i mjerila kako biste odredili kako će izgledati u vašem 3D view.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Postavke Canvas za 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Vidite „duhove” lasera? 3D Visualiser donekle je neovisan o postavi lasera i moguće je da u prikazu 3D Visualiser imate više lasera nego u Liberation. Kada u projekt dodate laser, dodat će se i novi objekt lasera unutar prikaza 3D Visualiser. No ako izbrišete laser, u prikazu 3D Visualiser i dalje će ostati objekt lasera kao „duh”.

Da biste uklonili sve takve lasere, kliknite gumb _Remove extra 3D laser objects_ (pri dnu panela s postavkama 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
