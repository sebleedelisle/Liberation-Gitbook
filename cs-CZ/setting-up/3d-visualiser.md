---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Úvod

3D Visualiser v Liberation je mimořádně užitečná funkce – můžete navrhovat a ladit show, aniž byste potřebovali jakékoli lasery. Pro mě je to neocenitelný nástroj, zvlášť u složitějších instalací s velkým počtem laserů.

### Pohyb ve 3D prostoru

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Zobrazení 3D Visualiser</p></figcaption></figure>

* Kliknutím a tažením otáčíte pohled kolem orbitálního bodu
* Kolečkem myši se posouváte dopředu a dozadu směrem k orbitálnímu bodu
* Kliknutím a tažením se stisknutou klávesou Shift posouváte kameru do stran (strafe) vlevo, vpravo, nahoru a dolů v rovině XY
* Dvojitým kliknutím kamkoli ve vizualizéru obnovíte pozici kamery

### Nastavení

Panel _3D Visualiser Settings_ otevřete z nabídky _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Panel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** – mění velikost vizualizéru vůči zbytku aplikace
* **Brightness Adjustment** – mění, jak jasně se lasery zobrazují
* **Show laser numbers** – zobrazí příslušné číslo nad každým laserem
* **Show zone names** – zobrazí příslušné názvy zone pod každým laserem

### Nastavení kamery

Tato nastavení se většinou týkají virtuální kamery ve 3D prostoru. K dispozici je rozbalovací nabídka s presety pro tato nastavení, které můžete ukládat a znovu načítat.

* **Camera distance -** Kamera vždy míří na svůj _Orbit point_. Vzdálenost kamery určuje, jak daleko je od tohoto bodu. Toto nastavení můžete upravit také kolečkem myši.
* **FOV -** Zorné pole – určuje, jak širokoúhlý nebo přiblížený je pohled kamery.
* **Orbit position** – popisuje aktuální natočení kolem orbitálního bodu. První hodnota je natočení kolem osy X (pitch) a druhá hodnota je natočení kolem osy Y (yaw).
* **Orbit centre point** – pozice orbitálního bodu ve 3D prostoru: x, y, z.
* **Grid height** – výška mřížky od „země“ (tj. místa, kde y = 0).

### Nastavení obsahu

Tato nastavení určují, kde jsou lasery (a Canvas) umístěné ve 3D prostředí. K dispozici je rozbalovací nabídka s presety pro tato nastavení, které můžete ukládat a znovu načítat.

#### Lasery

Každý laser má vlastní skupinu nastavení, kterou můžete rozbalit pomocí malého bílého trojúhelníku.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Nastavení laserů ve 3D Visualiser</p></figcaption></figure>

* **3D Position** – pozice laseru v osách x, y a z.
* **3D Orientation** – natočení laseru kolem os x, y a z.
* **Flip X / Flip Y** – převrátí virtuální výstup laseru. POZNÁMKA: nemělo by to být nutné – pro opravu nesrovnalostí v hardwaru je lepší použít nastavení převrácení/orientace laseru.
* **Output Range horizontal / vertical** – souvisí s maximálním/minimálním úhlem skenerů vašeho laseru. Standardně je to 60º, ale pokud se vaše lasery liší, můžete hodnotu upravit.

#### Canvas

Pokud používáte systém Canvas, můžete do 3D view zahrnout také obraz Canvas. Zaškrtnutím příslušného políčka zapnete vykreslení Canvas a pomocí nastavení pozice, orientace a měřítka určíte, jak bude ve vašem 3D view vypadat.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Nastavení Canvas ve 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Vidíte „duchové“ lasery? 3D Visualiser je do určité míry nezávislý na nastavení laserů a je možné mít ve vizualizéru více laserů, než máte v Liberation. Když do projektu přidáte laser, přidá se také nový laserový objekt ve vizualizéru. Když ale laser smažete, ve vizualizéru stále zůstane jeho „duch“.

Chcete-li odstranit všechny tyto „duchové“ lasery, klikněte na tlačítko _Remove extra 3D laser objects_ (dole v panelu 3D Visualiser Settings).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
