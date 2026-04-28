---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Színbeállítások és HSB

A Liberationben a színeket nem RGB, hanem HSB alapján adjuk meg. Ez elsőre szokatlan lehet, de ha megszokod, sokkal intuitívabb rendszernek fogod érezni.

{% hint style="info" %}
Ha inkább RGB-t használnál, kattints bármelyik színbeállításnál a színes négyzetre. Ezzel megnyílik a színszerkesztő panel, ahol RGB és HSB beállításokat is találsz.
{% endhint %}

### HSB - Hue, Saturation és Brightness

#### Hue

A szín Hue értéke 0 és 255 között lehet. A 0 a piros, majd az érték növelésével végighaladsz a szivárvány összes árnyalatán: narancs, sárga, zöld, cián, kék, lila, magenta, majd 255-nél visszatérsz a piroshoz.

Mivel ez egy körkörös tartomány, egy háromszögjellel végigléptetheted az összes színt.

#### Saturation

Ez a beállítás a szín telítettségét, vagyis élénkségét szabályozza. Más szóval azt, hogy mennyire _színes_ a szín, 0 és 255 közötti tartományban. A Saturation értékét 0-ra állítva szürkeárnyalatokat kapsz, 255-nél pedig teljesen élénk, szivárványszerű színeket. A kettő között pasztelles, fakóbb színek jelennek meg.

{% hint style="info" %}
Elnézést amerikai barátaimtól a colour szó plusz magánhangzója miatt. A Liberation Angliában készül, ezért az alapértelmezett nyelv a brit angol. A jövőben szeretnék fordításokat biztosítani franciára, spanyolra, németre, olaszra, egyszerűsített kínaira, és igen, még amerikai angolra is. :innocent:
{% endhint %}

#### Brightness

Talán ezt a legegyszerűbb megérteni: a 0 teljesen fekete, a 255 teljes fényerő.

### Példák a használatra

#### Szivárvány-ciklus :

Állítsd a _Brightness_ és a _Saturation_ értékét 255-re. Csatlakoztass egy _Sawtooth_ oszcillátort a _Hue_ bemenethez, és állítsd a tartományát 0 és 255 közé.

#### Pulzáló fényerő :

Csatlakoztass egy _Sawtooth_ oszcillátort a _Brightness_ bemenethez, és állítsd a tartományát 255 és 0 közé. A változás időtartamának ellenőrzéséhez tovább finomíthatod a clamp min és max értékeket. Ezután az easing függvényekkel még pontosabban beállíthatod az animációt.

#### Erős villanás / stroboszkóp :

Válassz színt a _Hue_ és _Saturation_ használatával, vagy kattints a színválasztóra. Csatlakoztass egy _Square Wave_ oszcillátort a _Brightness_ bemenethez, és állítsd a tartományát 255 és 0 közé.

#### Ciklus egy egyéni színtartományon belül :

Állítsd a _Brightness_ és a _Saturation_ értékét 255-re. Csatlakoztass egy _Triangle Wave_ oszcillátort a _Hue_ bemenethez, és állítsd be a tartományát:

* kékből ciánba: 70 és 128 közötti tartomány
* pirosból sárgába: 0 és 40 közötti tartomány
* pirosból magentába: 255 és 220 közötti tartomány
