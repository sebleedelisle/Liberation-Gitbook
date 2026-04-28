---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

A Liberation támogatja a külső SMPTE/LTC timecode jellel történő szinkronizálást. Ezt gyakran használják élő zenei műsorokban, hogy a fények, pirotechnika, videó és kísérősávok időben együtt fussanak.

{% hint style="info" %}
Mi az az SMPTE/LTC?

Az SMPTE egy timecode szabvány, az LTC pedig ennek a timecode-nak hangjellé alakított változata. Ha belehallgatsz ebbe a hangba, kellemetlen, magas sípolásnak hallatszik, a számítógépek számára viszont nagy felbontású időzítési információ.

**Kocka tények!**

Az SMPTE-t hagyományosan videó és hang szinkronban tartására használták. Analóg szalagra történő szinkronizálásnál az egyik sávra rögzítették a timecode hangot; ezt néha a szalag „csíkozásának” nevezték. Ezt a timecode sávot használhattad arra, hogy több magnódecket egymáshoz igazítva tarts, vagy hogy egy MIDI szekvenszert a szalaggal szinkronban futtass. (Így nem kellett MIDI hangszereket szalagra rögzítened; elég volt, ha a szekvenszer élőben lejátszotta őket keverés közben!)

Az SMPTE a Society of Motion Picture and Television Engineers rövidítése; ők határozták meg a szabványt. Az LTC jelentése _Linear TimeCode._
{% endhint %}

LTC timecode jelet a számítógép bármely hanginterfészén keresztül fogadhatsz, de ajánlott professzionális interfészt használni, legalább egy állítható XLR bemenettel és monitorozási lehetőséggel.

Nekem jó tapasztalatom volt a [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) eszközzel: van rajta fejhallgatós monitorozás, 2 XLR bemenet, és nem igényel külön illesztőprogramot (legalábbis macOS-en). Ha csak timecode-hoz fogod használni, választhatod a valamivel olcsóbb [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) modellt is (ezen csak egy bemenet van, MIDI nincs), de őszintén szólva bármilyen korrekt hanginterfésznek működnie kell.

{% hint style="info" %}
Az LTC timecode jeleket jellemzően szimmetrikus XLR kábeleken továbbítják, mert ezek elég robusztusak ahhoz, hogy alacsony szintű hangjeleket nagy távolságon is megbízhatóan vigyenek át. (Az XLR az a hengeres csatlakozó, amelyet általában mikrofonokhoz használnak.)
{% endhint %}

### Hardveres csatlakozások

Csatlakoztasd a timecode jelet hordozó XLR kábelt a hanginterfészhez, és ellenőrizd, hogy megfelelő jelet kapsz-e. Állítsd be a szintet a hanginterfészen úgy, hogy a jel erős legyen, de ne vezérelje túl a bemenetet. Ha a hanginterfészeden van fejhallgató-kimenet, belehallgathatsz a timecode-ba, és ellenőrizheted, hogy nem akadozik-e, illetve nincs-e rajta túl sok zaj.

{% hint style="info" %}
Elméletileg lehetséges a jelet a MacBook jack aljzatán keresztül fogadni, de ehhez egyedi kábelre lenne szükség. Ezek az aljzatok jellemzően 4 pólusú TRRS mini jackek, és őszintén szólva nem vagyok biztos benne, hogy ezek közül melyik érintkező használható hangbemenetként. Abban sem vagyok biztos, milyen feszültségszintet képes kezelni (valahol azt olvastam, hogy +/-1V, de ezt csak saját felelősségre használd!).

Szerintem jobban jársz, ha inkább beszerzel egy olcsó USB-s hanginterfészt, mint hogy ezzel próbálkozz.
{% endhint %}

Ha a hanginterfészeden nincs semmilyen bemeneti monitorozás, macOS rendszerbeállításokban (_Sound_ alatt) ellenőrizheted, hogy érkezik-e jel. (Windows alatt használd a _Sound Control Panel_ panelt.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>A macOS a Sound rendszerbeállítási panelen megjeleníti bármely hanginterfész bemeneti szintjét</p></figcaption></figure>

### Beállítás a Liberationben

1. Válaszd ki a hanginterfészt és a megfelelő bemeneti csatornát a Timecode settings Window ablakban.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Figyeld meg, hogy a legördülő menüben külön opció található a hanginterfész minden bemeneti csatornájához.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Figyeld meg a bal oldali négyzetet: ha érvényes timecode jelet fogadsz, zöldre vált. Ha nem, piros marad.

2. Válaszd ki a bejövő timecode megfelelő képkockasebességét. Aki a timecode-ot biztosítja, meg kell tudja mondani, mi a frame rate. (Ha rosszul állítod be, a szinkronizálás továbbra is működik, de minden másodpercben észreveszel egy kis „ugrást”.)
3. Nyisd meg a Timeline timecode beállításait a timeline sávon lévő kis óra ikon segítségével, és válaszd az SMPTE(LTC) opciót.

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Állítsd be a start offset értéket (órában, percben, másodpercben, képkockában), hogy illeszkedjen a dal kezdetéhez. Ha több timeline-t használsz, ezeket az opciókat mindegyikhez külön be kell állítanod.

{% hint style="info" %}
A turnévilágban gyakori konvenció, hogy minden dal másik óránál kezdődik, például az első dal 01:00:00:00-nál, a második 02:00:00:00-nál, és így tovább.

A Liberation a timecode alapján automatikusan átvált a megfelelő timeline-ra, ezért egy műsor közben soha nem kell kézzel timeline-t váltanod.
{% endhint %}

Fontos, hogy a MIDI Clockkal és az Ableton Linkkel ellentétben az SMPTE _abszolút_ időrendszer, amely órában, percben, másodpercben és képkockában mér. A Liberation alapvető időrendszere ütemekre és taktusokra épül, ezért timecode fogadásakor a timeline-ban beállított tempót fogja használni. Győződj meg róla, hogy ez a tempó szinkronban van azzal a zenével, amely szintén a timecode-hoz van igazítva.
