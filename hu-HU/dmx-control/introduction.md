---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Bevezetés

A Liberation rugalmas és hatékony DMX-rendszert tartalmaz, amellyel fényhatásokat hozhatsz létre, és DMX-kompatibilis lézereket vezérelhetsz Art-Neten keresztül. Úgy készült, hogy a világítást könnyen szinkronban tarthasd a lézershow-val – külön fényvezérlő pult nélkül.

{% hint style="info" %}
**Mi az Art-Net, és hogyan kapcsolódik a DMX-hez?**

A **DMX** egy régóta használt rendszer lámpák, lézerek, füstgépek és más színpadi effektek vezérlésére. Vezérlőjeleket küld speciális kábeleken keresztül (általában XLR-csatlakozókkal), és minden eszköz egy adott csatornatartományt figyel, hogy tudja, mit kell tennie.

Az **Art-Net** ugyanezeknek a DMX-adatoknak az átvitelére szolgál, de hagyományos számítógépes hálózaton. Speciális kábelek helyett Etherneten küldi az adatokat, ugyanúgy, mint az internetes vagy helyi hálózati forgalom.

A Liberationben minden DMX-kimenet Art-Net használatával történik. Ezzel közvetlenül vezérelhetsz Art-Net-kompatibilis eszközöket, vagy csatlakoztathatsz egy **Art-Net node** eszközt – egy kis dobozt, amely az Art-Net jelet visszaalakítja szabványos DMX-jellé. Így a hagyományos DMX-lámpákat és effekteket is vezérelheted, akkor is, ha azok önmagukban nem támogatják az Art-Netet.
{% endhint %}

A rendszerrel különféle színpadi eszközöket is vezérelhetsz, például füstgépeket, hazereket, CO₂-jeteket, hidegszikra-gépeket és egyebeket. Ha támogatja a DMX-et, beállíthatod DMX-zónaként, és közvetlenül a Liberationből indíthatod, a lézertartalom mellett.

A DMX-eszközök **DMX zones** formájában kerülnek hozzáadásra, és a zónalistában a lézersugár-zónák és a canvas célterületek mellett jelennek meg. Minden DMX zone egy **DMX preset** beállítást használ, amely megadja a Liberation számára, hogyan képezze le a lézerklipek tulajdonságait – például a pozíciót, a színt és a fényerőt – DMX-csatornaértékekre.

Amikor egy klipet DMX zone-ra küldesz, a Liberation a klip első elemét veszi alapul, és annak tulajdonságait a preset szerint alakítja át. Így ugyanazokkal a klipekkel, amelyeket már a lézerekhez használsz, közvetlenül vezérelhetsz lámpákat és DMX-effekteket is.

#### Liberation a Glastonburyn

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

A Liberation DMX-rendszer első éles próbája a Glastonbury 2023 fesztiválon volt, ahol a Reach Lasers összesen 90 sugárforrást telepített az Arcadia „spider” színpad részeként.

18 lézert belső Ether Dream eszközökkel vezéreltek, további 12 darab 6 fejes beam bart pedig Art-Neten és DMX-en keresztül.
