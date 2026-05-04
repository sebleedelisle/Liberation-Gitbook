---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Élő MIDI vezérlők

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 vezérlő**

Ez a Liberation alapértelmezett hardveres vezérlője; erősen ajánlott, és nyugodtan mondhatjuk, hogy a Liberationt kezdettől fogva ehhez a hardverhez tervezték. Amint csatlakoztatod az APC40-et, a Liberation automatikusan kapcsolódik hozzá.

{% hint style="warning" %}
_Jaj ne! Előadás közben félig kihúzódott az USB-csatlakozóm!_

Ne ess pánikba – csak dugd vissza, a Liberation automatikusan újracsatlakozik, minden különösebb teendő nélkül.
{% endhint %}

### APC40 Mark 1 vagy Mark 2?

Röviden: a Mark 2 ajánlott, mert teljes színű gombjai jobban illeszkednek a Liberation Clip Deck felületéhez. A Mark 1 verzió szükség esetén használható, de kissé zavaróbb lehet, mivel az elrendezése valamennyire eltér a képernyőn láthatótól, a gombjai pedig csak pirosan, narancssárgán vagy zölden tudnak világítani, így nem fognak egyezni a klipek színeivel.

{% hint style="info" %}
Az eredeti APC40 Mark 1 2009-ben jelent meg(!), és néhányan még ma is ezt kedvelik a fémháza és a masszív, konzolszerű kialakítása miatt. A frissített Mark 2 2014-ben jelent meg, és bár 2024-ben megszűnt a gyártása, a vizuális művészek (Resolume stb.) és a lézeres felhasználók igényei miatt 2025-ben újra gyártásba kerül.
{% endhint %}

Az APC40-en elérhető vezérlők teljes listáját lásd itt: [APC40 referencia](../reference/apc40-reference.md "mention")

### APC Mini

A Liberation 1.0.3 egy APC Mini profilt is tartalmaz. Ez leképezi a 8x5-ös Clip rácsot, a zone gombokat, a zone X/Y tükrözési vezérlőit, a csoportgombokat, az összes Clip leállítását, a Clip-oldalak léptetését, a zone-oldalak léptetését, a tap tempót, az ütemresetet és a tempó finomállítását. A faderek az effektszinteket vezérlik, a shiftelt faderek pedig az effektparamétereket. Az utolsó fader a globális fényerőt vezérli.

### MIDI Fighter Twister

A MIDI Fighter Twister profil inkább encoderközpontú vezérlésre készült, nem Clip indításra. Az encoderek egyik sora az 1–8. effekthely 1. paraméterét vezérli, egy másik sor pedig a Parameters panel nyolc kontextusfüggő vezérlőjét követi, beleértve a Clip eltolását, a zone késleltetését, a globális forgatást/méretezést és a csoportos fade-eket.
