---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Nodes pro stylizaci

## &#x20;Randomise

Vytváří rozptýlené kopie příchozích prvků pomocí souvislého šumového pole. Jinými slovy kopíruje a posouvá vaše tvary a body kontrolovaným „zašuměným“ způsobem. Místo aby vše zůstalo úhledně na jednom místě, získáte více verzí, které se posouvají a rozprostírají, podobně jako částice pohybující se v proudu.

* **count** – počet kopií pro každý příchozí prvek (1–20). Při hodnotě 1 vznikne jedna lehce posunutá verze každého prvku. Vyšší hodnoty vytvoří více rozptýlených kopií.
* **noise offset** – prochází šumovým polem (0–100 %). Smyčka plynule navazuje, takže při animaci pomocí Oscillator Node vznikne hladký souvislý pohyb všech kopií najednou.
* **noise jitter** – určuje měřítko textury šumu. Nižší hodnoty vytvářejí široké, plynulé variace. Vyšší hodnoty vytvářejí těsnější a nepravidelnější rozmístění. Mění se tím vzor, ne síla efektu.
* **change between points** – určuje, jak moc se každá kopie liší od předchozí. Nízké hodnoty drží kopie u sebe a podobné. Vysoké hodnoty je více rozprostřou a přidají větší variaci.
* **face direction** – otočí každou kopii tak, aby směřovala ve směru pohybu v šumovém poli. Výsledkem jsou šipky nebo částice zarovnané podle proudu.
* **amount** – celková síla efektu (0–100 %). Škáluje posun i rotaci z Face direction.

{% hint style="info" %}
Node Randomise je základem efektu Randomise!
{% endhint %}

## &#x20;Trails

Vytváří ozvěny vašeho obsahu – za pohybujícím se originálem zanechává kopie, které postupně mizí nebo mění měřítko.

* **change render profile for trail** – pokud je zapnuto, všechny kopie trailu použijí vybraný **render profile**. _Viz_ [Render profile](../fundamentals/render-profile.md "mention").
* **render profile** – profil použitý pro kopie trailu, když je přepínač výše zapnutý. Často se používá, když je hlavní obsah nastavený na **DETAIL**, ale ozvěny se vykreslují jako **FAST**. Hlavní tvary tak zůstanou detailní, zatímco traily se vykreslují efektivněji.
* **delay** – nastavuje rozestup mezi kopiemi trailu v hudebním čase, měřený v **krocích po 1/64 noty**.\
  Pro orientaci:
  * 16 = 1/16 taktu (šestnáctinová nota)
  * 32 = 1/8 taktu (osminová nota)
  * 64 = 1/4 taktu (čtvrťová nota)
  * 128 = 1/2 taktu (půlová nota)
  * 256 = 1 takt
* **trail size** – kolik kopií trailu se vykreslí za aktuálním obsahem.
* **prefill trails** – vyplní historii stop hned při spuštění Clip, místo aby se ozvěny postupně vytvářely během prvních několika dob.
* **freeze trails** – změní plynule tekoucí traily na sekvenci zmrazených snímků. Hodí se pro vytváření staccatových trail efektů synchronizovaných s beatem.
* **brightness start / brightness end** – aplikuje jas napříč trailem od nejnovější kopie (**start**) po nejstarší kopii (**end**). Obvykle nastavte **brightness start** na 100 % a **brightness end** na 0 %, aby ozvěny postupně zmizely.
* **scale start / scale end** – aplikuje změnu měřítka napříč trailem od nejnovější kopie (start) po nejstarší kopii (end). Pro traily, které se mají zmenšit až do zmizení, nastavte **scale start** na 100 % a **scale end** na 0 %.

## &#x20;Shimmer

Přidává obsahu třpytivou variaci jasu, od jemného jiskření až po intenzivní strobování.

* **speed** – jak rychle se shimmer v čase mění. Vyšší hodnoty blikají rychleji; 0 efekt pozastaví.
* **separation** – jak moc se sousední body nebo prvky od sebe liší.
  * 0: vše se třpytí společně.
  * \>0: blízké body dostávají postupně odlišné fáze, takže se shimmer mění napříč tvarem.
  * <0: stejné jako výše, ale posun fáze běží opačným směrem.
* **threshold** – místo plynulého slábnutí se body podle svého jasu plně zapínají nebo vypínají. Jasnější prvky se rozsvěcují častěji, ale mějte na paměti, že prvky se 100% jasem jsou vždy zapnuté a prvky s 0% jasem jsou vždy vypnuté. Hodí se pro ostré třpytivé nebo hvězdné efekty.

{% hint style="info" %}
Zapnutí **threshold** je jedna z těch skvělých skrytých funkcí, které dokážou částice nebo obsah výrazně oživit. Místo plynulého slábnutí se body podle svého jasu rychle zapínají a vypínají. Protože se v daném okamžiku vykresluje méně bodů, výsledkem je jasnější výstup a plynulejší animace.

Mějte ale na paměti, že pokud je váš obsah už na 100% jasu, nic se nestane!
{% endhint %}

* **use whole shape** – aplikuje jednu hodnotu shimmer rovnoměrně na celý tvar. Když je vypnuto, node rozdělí tvary tak, aby se různé části mohly třpytit nezávisle a vytvořily zrnitý vzhled.

## &#x20;Particles

Toto je experimentální efekt, který vytváří a animuje částice podle vašeho obsahu. Všechny bodové prvky na vstupu se berou jako pozice emitorů. Protože se dráhy částic předpočítávají, při změně vstupního obsahu může být nutné částice obnovit nebo přepočítat (stačí změnit libovolné nastavení).

**Obecné**

* **keep original** – pokud je zapnuto, původní obsah zůstane zachovaný a částice se přidají navrch. Hodí se, když chcete, aby body emitorů zůstaly viditelné.
* **number of particles** – kolik částic se vytvoří při každé emisi. Vyšší hodnoty vytvoří hustší efekty, nižší hodnoty působí střídměji.
* **emission period** – rozsah smyčky (v taktech), během kterého se částice emitují. Při 100 % jsou rovnoměrně rozložené napříč smyčkou; menší hodnoty je shlukují do krátkých výbuchů.
* **loop length** – jak dlouho trvá částicová smyčka, měřeno v hudebních taktech.
* **loop count** – kolikrát se smyčka zopakuje před resetem. Pokud je nastaveno 1, částice vždy poběží přesně podle stejné simulace, takže bude dokonale opakovatelná. Vyšší hodnoty přidají před resetem cyklu více variace.
* **delay** – posune začátek emise o určitý počet 1/64 not pro časovací efekty.

**Pohyb**

* **speed** – jak rychle se částice pohybují od emitoru.
* **speed variation** – přidá náhodnost, aby se všechny částice nepohybovaly stejnou rychlostí. Vytváří přirozenější rozptyl.
* **direction** – nastavuje základní směr, kterým jsou částice vystřelovány, definovaný pomocí **úhlů x, y, z**. Tyto úhly otáčejí vektor výstřelu ve 3D prostoru, takže můžete částice mířit přímo nahoru, do strany nebo libovolně šikmo. Kombinujte se **spread** pro širší kužely nebo chaotičtější výbuchy.

{% hint style="info" %}
**Eulerovy úhly**\
Liberation používá **Eulerovy úhly** k popisu orientace ve 3D prostoru. Jsou to jednoduše rotace kolem tří hlavních os:

* **X** – náklon dopředu/dozadu (jako když kýváte hlavou)
* **Y** – otočení doleva/doprava (jako když vrtíte hlavou „ne“)
* **Z** – rotace po/proti směru hodinových ručiček (jako když nakláníte hlavu do strany)

Úpravou těchto tří hodnot můžete částice nasměrovat libovolným směrem.
{% endhint %}

* **direction variation** – přidá náhodný rozptyl kolem daného směru. Hodí se pro vytváření kuželů, sprejů nebo explozí.
* **drag** – časem částice zpomaluje. Vyšší hodnoty působí těžším a línějším dojmem.
* **gravity** – táhne částice dolů (kladná hodnota) nebo je tlačí nahoru (záporná hodnota).
* **gravity variation** – přidá pro každou částici variaci gravitace, takže je pohyb chaotičtější.

**Životnost**

* **life duration** – jak dlouho částice existují (měřeno v jednotkách 1/64 noty). Při kratších hodnotách částice rychle mizí, při delších hodnotách zůstávají viditelné delší dobu.
* **life variation** – přidá náhodnost do životnosti částic, aby nezmizely všechny najednou.
* **start delay / start delay variation** – zpozdí okamžik, kdy se každá částice stane viditelnou (v krocích po 1/64 noty). Částice je během této doby už vytvořená a pohybuje se, ale její jas je držený na 0, takže zůstává neviditelná, dokud zpoždění neuplyne. Hodí se, když chcete, aby se opožděně objevily ohňostrojové „jiskry“.

**Barva a jas**

* **hue start** – počáteční barva částic.
* **hue variation** – přidá náhodnost, aby všechny částice nezačínaly stejnou barvou.
* **hue change** – posouvá odstín během životnosti částice a vytváří barevně se měnící traily.
* **brightness start / brightness end** – aplikuje jas napříč životností částice. Obvykle nastavte brightness start vysoko a brightness end nízko, aby částice přirozeně mizely.
* **brightness variation** – náhodně upravuje počáteční jas a vytváří dynamičtější vzhled.
* **saturation start / saturation end** – nastavuje, jak sytá je barva na začátku a na konci.
* **saturation variation** – náhodně mění sytost a vytváří variaci mezi částicemi.

**Simulace**

* **time adjustment** – zrychlí nebo zpomalí celou částicovou simulaci. Hodí se pro synchronizaci s různými tempy nebo pro zvýraznění pohybu.
