---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Bevezetés

A Liberation 3D visualiser funkciója rendkívül hasznos: a show-kat akár lézerek nélkül is megtervezheted és finomhangolhatod. Számomra különösen értékes eszköznek bizonyult, főleg összetett, sok lézerből álló setupoknál.

### Navigálás a 3D térben

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>A 3D Visualiser nézete</p></figcaption></figure>

* Kattints és húzd az egeret a nézet forgatásához az orbit pont körül
* Az egérgörgővel közelíthetsz vagy távolíthatsz az orbit pont felé
* Kattints és húzd az egeret lenyomott shift billentyű mellett, hogy a kamerát oldalirányban (strafe) mozgasd balra, jobbra, fel és le az XY sík mentén
* Kattints duplán bárhol a visualiserben a kamera pozíciójának alaphelyzetbe állításához

### Beállítások

Nyisd meg a _3D Visualiser Settings_ panelt a _Window_ menüből.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>A 3D Visualiser Settings panel</p></figcaption></figure>

* **Visualiser size** - a visualiser méretét módosítja az alkalmazás többi részéhez képest
* **Brightness Adjustment** - a lézerek megjelenített fényerejét módosítja
* **Show laser numbers** - megjeleníti az adott számot minden lézer fölött
* **Show zone names** - megjeleníti az adott zone neveket minden lézer alatt

### Kamera beállításai

Ezek a beállítások főként a 3D térben lévő virtuális kamerára vonatkoznak. Látsz egy legördülő menüt is ezekhez a beállításokhoz tartozó presetekkel, amelyeket elmenthetsz és újra betölthetsz.

* **Camera distance -** A kamera mindig az _Orbit point_ felé néz. A camera distance azt adja meg, milyen messze van ettől a ponttól. Ezt a beállítást az egérgörgővel is módosíthatod.
* **FOV -** Field of view - meghatározza, mennyire nagylátószögű vagy ráközelített a kamera képe.
* **Orbit position** - az orbit pont körüli aktuális forgatást írja le. Az első érték az X tengely körüli forgatás (pitch), a második érték az Y tengely körüli forgatás (yaw).
* **Orbit centre point** - az orbit pont pozíciója a 3D térben: x, y, z.
* **Grid height** - a rács magassága a „talajhoz” képest (azaz ahol y = 0).

### Tartalombeállítások

Ezek a beállítások határozzák meg, hogy a lézerek (és a canvas) hol helyezkednek el a 3D környezetben. Látsz egy legördülő menüt is ezekhez a beállításokhoz tartozó presetekkel, amelyeket elmenthetsz és újra betölthetsz.

#### Lézerek

Minden lézerhez saját beállításcsoport tartozik, amelyet a kis fehér háromszöggel nyithatsz ki.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>3D visualiser lézerbeállítások</p></figcaption></figure>

* **3D Position** - a lézer x, y és z pozíciója.
* **3D Orientation** - a lézer forgatása az x, y és z tengelyek körül.
* **Flip X / Flip Y** - megfordítja a lézer virtuális outputját. MEGJEGYZÉS: erre általában nem kellene szükség legyen; jobb, ha a laser flip / orientation beállításokkal javítod a hardvered esetleges eltéréseit.
* **Output Range horizontal / vertical** - a lézer szkennereinek maximális / minimális szögéhez kapcsolódik. A 60º a szabványos érték, de módosíthatod, ha a lézereid ettől eltérnek.

#### Canvas

Ha a canvas rendszert használod, a canvas képet is megjelenítheted a 3D nézetben. Aktiváld a jelölőnégyzetet a canvas megjelenítéséhez, majd a position, orientation és scale beállításokkal határozd meg, hogyan jelenjen meg a 3D nézetben.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>3D visualiser canvas beállítások</p></figcaption></figure>

{% hint style="info" %}
„Szellem” lézereket látsz? A 3D Visualiser részben független a lézer setupjától, ezért előfordulhat, hogy több lézer van a visualiserben, mint a Liberation projektben. Amikor lézert adsz a projekthez, a visualiserben is létrejön egy új lézerobjektum. Ha viszont törölsz egy lézert, a visualiserben továbbra is megmarad egy „szellem” lézerobjektum.

Az összes szellem lézer eltávolításához kattints a _Remove extra 3D laser objects_ gombra (a 3D Visualiser settings panel alján).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
