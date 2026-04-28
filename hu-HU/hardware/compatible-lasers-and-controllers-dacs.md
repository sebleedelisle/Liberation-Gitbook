---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatibilis lézerek és vezérlők (DAC-ok)

### Mely lézerek kompatibilisek a Liberationnel?

Ha a lézered rendelkezik szabványos ILDA bemenettel, akkor használhatod a Liberationnel, egy kompatibilis lézervezérlővel együtt, például Ether Dream vagy Helios DAC használatával - [a teljes listát lásd alább](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>A Helios DAC - a legolcsóbb megoldás otthoni használatra</p></figcaption></figure>

Nincs szükséged külső vezérlőre vagy ILDA bemenetre, ha:

* A lézeredbe Ether Dream van beépítve, vagy;
* Wicked Lasers LaserCube-od van, vagy;
* Olyan X-Laser eszközöd van, amelybe Mercury van beépítve, vagy;
* Olyan Laser Animation Sollinger lézered van, amelybe AVB vezérlő van beépítve (jelenleg csak macOS-en tesztelés alatt)

{% hint style="info" %}
**Mi az a lézervezérlő?**

A lézervezérlő (vagy DAC) olyan hardvereszköz, amely a Liberationből érkező digitális adatokat a lézer szkennereinek és kimenetének vezérléséhez szükséges analóg jelekké alakítja. (Innen a DAC név: Digital to Analog Converter, azaz digitális-analóg átalakító.)

A vezérlő USB-n vagy szabványos számítógépes hálózaton keresztül csatlakozik a számítógépedhez; lehet külső eszköz, vagy a lézerbe beépítve is.

Ha külső eszköz, akkor ILDA csatlakozáson keresztül kötöd össze a lézerrel. Az ILDA iparági szabvány, amely egy régi típusú, 25 pólusú „D” csatlakozót használ. Szerezz be egy ILDA kábelt, csatlakoztasd az egyik végét a vezérlőhöz, a másikat pedig a lézerhez.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>Az ILDA kimenet egy külső Ether Dream eszközön</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Egy lézer hátlapja a különböző csatlakozásokkal, köztük az ILDA bemenettel</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Egy szabványos ILDA kábel</p></figcaption></figure>

### Melyik vezérlő a legjobb számomra?

Ha otthoni felhasználó vagy, vagy kisebb show-kat futtatsz legfeljebb 4 lézerrel, amelyek közel vannak a számítógéphez, akkor az USB-s vezérlők, például a **Helios DAC**, a **legkedvezőbb árú** megoldások.

Az olyan hálózati DAC-ok, mint az **Ether Dream**, a **legjobb választást jelentik professzionális** lézershow-szakembereknek, akik szívesen beállítanak egy hálózatot, és sok lézert szeretnének vezérelni; eddig minden nagyobb Liberation show Ether Dream eszközökkel futott.

Ha **LaserCube**-od van, akkor egyáltalán nincs szükséged külön lézervezérlőre - a Liberation minden LaserCube-bal kompatibilis. A korábbi modellek USB kábellel csatlakoznak, az újabb modellek pedig hálózaton keresztül.

Ha professzionális felhasználóként a legegyszerűbb megoldást keresed, érdemes megfontolni a beépített Mercuryval rendelkező X-Laser egységeket, vagy az AVB-t használó Laser Animation Sollinger lézereket.

### Kompatibilis lézervezérlők

#### Ether Dream (hálózati)

Az [Ether Dream](https://ether-dream.com) több mint tíz éve létezik, és jelenleg a 4-es verziónál tart (bár a Liberation az Ether Dream 1-es, 2-es és 3-as verziójával is működik). Rendkívül megbízható eszközök.

Szabványos hálózaton keresztül csatlakozol hozzájuk. Megvásárolhatók önálló egységként, de még jobb, ha közvetlenül a lézerekbe vannak beépítve.

#### Helios (USB)

A [Helios](https://bitlasers.com/helios-laser-dac/) a legjobb választás kezdőknek, és olcsóbb, mint az Ether Dream, de mivel USB-n keresztül csatlakozik, hosszú kábelezéshez nem ajánlott. Emellett 4-nél több eszköz csatlakoztatása után USB adatátviteli és illesztőprogram-problémák is előfordulhatnak, különösen Windows alatt.

Ha viszont csak néhány lézert szeretnél otthon használni, ez a legolcsóbb és legegyszerűbb megoldás.

#### Mercury (X-Laser egységekbe beépítve)

A [**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) az X-Laser nagy teljesítményű DMX lézervezérlő rendszere, amelyet olyan világítástervezőknek készítettek, akik a lézereket közvetlenül hagyományos világításpultról szeretnék vezérelni. A legújabb firmware-frissítéssel a Mercury **Ether Dream-emulációt** is tartalmaz, ami azt jelenti, hogy most már zökkenőmentesen működik a Liberationnel - valamint minden más, Ether Dreamet támogató szoftverrel is.

#### AVB (Laser Animation Sollinger egységekbe beépítve)

Az **AVB** egy nyílt, hálózatalapú protokoll nagy teljesítményű, alacsony késleltetésű audió- és adatstreameléshez. Sok LaserAnimation Sollinger projektor közvetlenül a hardverben támogatja az AVB-t, így a Liberation külső DAC-ok nélkül, hálózaton keresztül tud csatlakozni hozzájuk. A Liberation AVB-támogatása jelenleg **csak macOS-en érhető el, és tesztelés alatt áll**, valamint **kompatibilis, AVB-képes hálózati eszközöket** igényel. Megfelelő beállítás esetén egyszerűbb munkafolyamatot, kevesebb külső eszközt és robusztus megbízhatóságot kínál professzionális show-khoz. I

#### A jövőben támogatott vezérlők:

* [IDN](http://www.ilda-digital.com) (az ILDA nyílt hálózati protokollja, amelyet bármely gyártó implementálhat)

### Kábelezési javaslatok

Az optimális teljesítmény érdekében tartsd az USB-s DAC-okat a számítógép közelében, és hosszabb ILDA kábelekkel csatlakoztasd őket a lézerekhez. (Arra viszont figyelj, hogy az ILDA kábelek bontáskor könnyen beakadhatnak, mint egy kampó!)

Ha Ether Dream eszközöket használsz, továbbra is tarthatod őket egy helyen, és hosszú ILDA kábelekkel kötheted őket a lézerekhez, vagy felszerelheted őket a lézerek közelében, és használhatsz hosszabb hálózati kábeleket.

Az ideális megoldás az, ha az Ether Dream eszközök (vagy más vezérlők) közvetlenül a lézerekbe vannak beépítve (az Egyesült Királyságban Rob a Stanwax Lasernél ezt el tudja végezni neked).
