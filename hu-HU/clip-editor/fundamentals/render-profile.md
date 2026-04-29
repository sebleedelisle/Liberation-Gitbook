---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

Minden _Creator_ csomópontban található egy _Render Profile_ beállítás. Ez határozza meg, hogyan rajzolódnak ki (vagyis hogyan történik a _renderelésük_) a lézerekkel.

**A legtöbb felhasználásnál a&#x20;**_**DEFAULT**_**&#x20;beállítás teljesen megfelelő**. Ha azonban grafikákkal vagy összetett tartalommal dolgozol, érdemes lehet részletesebben szabályozni, hogyan renderelődjön az egyes alakzatok kirajzolása.

{% hint style="info" %}
A legtöbb lézerszoftverrel ellentétben a Liberation valós időben generálja a pontfolyamot, közvetlenül azelőtt, hogy az a lézervezérlőkhöz kerülne. Ez sok lemezterületet takarít meg: a Clip-ek csak néhány kB méretűek, nem pedig előre renderelt, több MB-os pontfolyamok.

Ez azt is jelenti, hogy ugyanazt a tartalmat lézerenként különböző szkennertípusokhoz hangolhatod, anélkül hogy magukat a Clip-eket módosítanod kellene.

További részletekért lásd: [◼️ Hogyan generál a Liberation lézeres tartalmat](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Három előre beállított _Render Profile_ érhető el: _DEFAULT_, _FAST_ és _DETAIL._

_**DEFAULT**_ – jó általános profil, a legtöbb esetben ez a legjobb választás

_**FAST** -_ ha a Clip sok tartalmat tartalmaz, és ezek egy része csak nagyon egyszerű pontokból és egyenes vonalakból áll, ezzel a beállítással csökkenthető a villódzás.

_**DETAIL**_ – ha olyan tartalmat rajzolsz, amelynél éles sarkokra van szükség, ezt a beállítást használd. Vedd figyelembe, hogy a szkennerek lassabban fognak mozogni, ezért a kimenet villódzóbb lehet.

{% hint style="info" %}
A clip editorben a Creator csomópontokat különböző renderprofilokhoz rendelheted, de az egyes lézerek ezeket a profilokat a saját scanner beállításaik alapján dolgozzák fel. Lásd: [◼️ Scanner presets és renderprofilok](../../advanced/scanner-presets.md)
{% endhint %}
