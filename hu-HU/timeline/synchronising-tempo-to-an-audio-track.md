---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Tempó szinkronizálása hangsávhoz

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchronising tempo to an audio track" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

A Liberation idővonala fix és változó tempókkal is tud dolgozni, de a megbízható szinkron mindig a tempó meghatározásával és a hang megfelelő igazításával kezdődik. Ez a szakasz az ajánlott munkafolyamatot ismerteti.

#### 1. Az első hangsúlyos ütem igazítása

Add hozzá a hangsávot az idővonalhoz, és ügyelj rá, hogy ütemhez legyen illesztve, vagyis a sáv **első zenei hangsúlyos üteme** pontosan egy ütemvonal elejére essen.

Ez a lépés kritikus.

Ha a hanganyag természetes módon nem hangsúlyos ütemen indul, két lehetőséged van:

* **A clip késleltetésének beállítása**\
  Kattints jobb gombbal az audio clipre, és állítsd a Delay értéket, amíg az első hangsúlyos ütem egy beat- vagy bar jelölőhöz nem igazodik.
* **A hanganyag külső vágása**\
  Szerkeszd a hangfájlt egy külső szerkesztőben, például Audacityben, hogy a fájl pontosan az első hangsúlyos ütemen induljon, majd importáld újra.

{% hint style="info" %}
**Fontos:**\
Ha a hanganyag kezdete nincs beathez vagy barhoz igazítva, a zene érzékelt kezdőpozíciója a tempó módosításakor előre-hátra el fog tolódni. Ez rendkívül megnehezíti a pontos tempóillesztést.
{% endhint %}

#### 2. Kezdeti tempó beállítása

Ha nagyjából tudod a BPM értéket, írd be az idővonal tempóvezérlőjébe, majd indítsd el a lejátszást az elejéről.

A sáv lejátszása közben figyeld meg alaposan a beat és bar jelölőket.

* Ha a jelölők a zene elé sodródnak, kissé csökkentsd a tempót.
* Ha lemaradnak mögötte, kissé növeld a tempót.
* Állítsd le a lejátszást, módosítsd a tempót, majd próbáld újra.

A legtöbb modern zenénél a tempó fix, egész számú BPM. Ha megtaláltad a helyes értéket, annak a teljes sávon végig szinkronban kell maradnia.

#### 3. A hullámforma használata vizuális támpontként

Az audio hullámforma hasznos referencia a tempó illesztéséhez.

* A tranziens pontoknak és csúcsoknak a függőleges bar jelölőkhöz kell igazodniuk.
* Nagyíts rá, és több baron keresztül ellenőrizd az igazítást.

**Tipp:**\
Az idővonal nagyításához használd az egérgörgőt vagy a trackpad gesztust. A vízszintes görgővel vagy gesztussal balra és jobbra mozoghatsz. Ránagyítva sokkal könnyebb a finom beállítás.

#### 4. Nem egész BPM értékű sávok

Ha a sáv nem egész számú BPM-et használ, az elcsúszás fokozatosabb lesz.

* Nagyíts rá még jobban.
* Kisebb tempómódosításokat használj.
* Ne csak az első néhány baron, hanem a sáv hosszabb szakaszain ellenőrizd az igazítást.

#### 5. Tempóváltásokat tartalmazó zene

Ha a zene gyorsul vagy lassul, használd a Tempo Map funkciót:

* Játszd le a sávot, és figyeld a beat jelölőket.
* Amikor az elcsúszás észrevehetővé válik, adj hozzá egy tempóváltást ezen a ponton.
* Állítsd be az új szakasz tempóját, amíg ismét szinkronba nem kerül.

Ismételd meg ezt a folyamatot a zene minden tempóváltásánál.

#### 6. Külső tempóelemzés (opcionális)

Végső megoldásként elemezheted a sávot egy DAW-ban, például Logic Próban, és automatikusan generálhatsz tempótérképet. Vedd figyelembe, hogy ez gyakran nagyon sok tempóváltást eredményez, néha baronként egyet, ami a legtöbb show-hoz részletesebb lehet a szükségesnél.
