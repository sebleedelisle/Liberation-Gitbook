---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Effekter

Effektsystemet i Liberation är ett roligt och flexibelt sätt att ändra clip-output i realtid. Effekter är helt flexibla och kan användas för att få allt att blinka av och på, rotera, byta färg eller till och med flyga runt slumpmässigt!

Allt du kan göra i clip-editorn kan användas som en effekt. Effekter redigeras faktiskt med exakt samma nodeditor som clips! Se [Effekter](effects.md#editing-effects "mention"). De kreativa möjligheterna är i princip oändliga.

Standardknapparna för effekter 1–8 finns under zonknapparna, och effekterna 9–24 är de små knapparna längst ned.

#### Använda en effekt

Tryck på en effektknapp för att slå på eller av effekten, eller ännu bättre: använd APC40-reglagen 1–8 för att tona effekter in och ut. För att tona in en effekt utan en APC40 klickar du på knappen och drar uppåt eller nedåt. Du kan också högerklicka på effektknappen och justera nivåreglaget.

{% hint style="warning" %}
När du trycker på effektknappen aktiveras effekten direkt. Observera dock att om nivån är satt till noll händer ingenting! Klicka och dra på knappen för att ändra nivån, högerklicka och använd reglaget _level_, eller använd APC40-fadrarna.
{% endhint %}

#### Effekter och clipens zonfördröjning

Effekter tar över inställningen för zonfördröjning från varje clip som körs just nu. Om ditt clip till exempel har en fördröjning som rör sig från vänster till höger, och du lägger till blinkeffekten, fördröjs blinkningen också från vänster till höger.

{% hint style="info" %}
Hur clipens zonfördröjning ärvs av effekter är en sådan sak som är extremt svår att beskriva men självklar när du provar den!

Jag skulle säga att det är ett av de roligaste och mest kreativa verktygen som är inbyggda i Liberation. Testa så ser du vad jag menar!
{% endhint %}

#### Effektparametrar

Lägg till en parameter i din effekt med en _Parameter node._ Parametersystemet är ett sätt att justera flera inställningar inuti effekten utifrån. Se [Parameter Control](clip-editor/oscillators/parameter-control.md "mention") för mer information.

Använd vridreglagen 1–8 för att justera _parameter_ för varje effekt. Du kan också högerklicka på effektknappen och justera parameterreglaget/reglagen. Parameterändringen gör olika saker beroende på hur effekten är uppbyggd. Se listan nedan för standardeffekterna och vad deras parametrar gör.

{% hint style="info" %}
Vridreglagen 1–8 sitter längs ovansidan på en APC40 Mk2 och uppe till höger på Mk1. Se även: [APC40-referens](reference/apc40-reference.md "mention")
{% endhint %}

{% hint style="info" %}
De små siffrorna du ser på effektknapparna visar effektens _level_ och _parameter_. _level_ styrs av fadern på APC40, eller så kan du klicka och dra på knappen. Parametern justeras med vridreglagen på APC40, eller så kan du högerklicka och justera med musen.
{% endhint %}

#### Standardeffekterna

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Lägger till en kaotisk rörelse på clip-output. Parametern justerar mängden/hastigheten på kaoset.
2. **Sine wave** :\
   Förvränger allt innehåll längs en rörlig sinusvåg. Parametern justerar våglängden.
3. **Rotation** :\
   Roterar allt. Parametern justerar rotationshastigheten.
4. **Horizontal flip** :\
   Klämmer ihop och sträcker ut allt horisontellt. Parametern justerar hastigheten.
5. **Scale** :\
   Skalar upprepade gånger allt från fullt till noll. Parametern justerar hastigheten.
6. **Hue** :\
Ändrar nyansen på allt, men ändrar inte mättnaden (dvs. allt som är vitt förblir vitt). Parametern justerar nyansen.
7. **Saturation and hue** :\
Ändrar nyansen på allt och mättar även färgen helt (dvs. allt som är vitt ändras till färgen). Parametern justerar nyansen.
8. **Flash** :\
   Blinkar upprepade gånger ljusstyrkan på allt från fullt till noll. Parametern justerar blinkhastigheten.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Det finns ytterligare 16 färgeffekter längs den nedersta raden som använder förinställda värden för nyans och mättnad.

Observera att detta är standardeffekterna, men de kan redigeras till att göra nästan vad du vill!

### Apply to groups

Du kan välja vilka grupper som påverkas av effekten. Högerklicka och växla gruppkryssrutorna märkta _Apply to groups._

Jag använder främst den här inställningen när jag arbetar med canvasgrafik och laserstrålar separat. Jag tilldelar alla canvas-clips till grupp 5 och exkluderar sedan den gruppen från effekter som jag inte vill ska påverka dessa grafiska clips.

Du kan också använda det för att live applicera två olika färgändringar på två grupper av lasrar samtidigt. Skapa två färgändringseffekter och välj vilka clip-grupper varje effekt ska appliceras på.

### MX group

Förkortning för _Mutually Exclusive_. Det här är ett sätt att gruppera effekter så att bara en effekt i gruppen kan vara aktiv åt gången. Lägg märke till att bara en av standardeffekterna för färgändring kan vara aktiv samtidigt. Det beror på att de alla ligger i MX Group 1.

Den här funktionen är avstängd om inställningen _MX Group_ är 0.

### Redigera effekter

Högerklicka på valfri effekt och klicka på knappen _EDIT EFFECT_ för att öppna effekteditorn. Observera att den här editorn är identisk med Clip Editor!

Redigera din effekt på samma sätt som du skulle redigera vilket clip som helst. Se [clip-editor](clip-editor/ "mention").

Du behöver ha minst en creator-nod; det kan vara vad som helst (linje, cirkel, form, till och med text!), men du bör förmodligen välja något som är mest logiskt i förhandsvisningen på effektknappen.

När effekter appliceras ersätts alla creator-noder i effekten med utdata från de clips som körs just nu.

{% hint style="warning" %}
Av extremt tråkiga tekniska skäl är "trails"-noderna inte aktiverade inuti en effekt. Detsamma gäller inställningen "delay" inuti pattern-noder (de använder samma system). Detta kommer att åtgärdas i framtida versioner.
{% endhint %}
