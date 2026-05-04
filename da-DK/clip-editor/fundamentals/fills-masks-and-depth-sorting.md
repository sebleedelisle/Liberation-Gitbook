---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Fills, masks og dybdesortering

### Strokes, fills og masks

Du vil bemærke, at nogle Creator-noder har indstillingen _Fill state_; du kan tegne dem med en stroke (en kontur), som en mask (der dækker ting nedenunder) eller begge dele.

Når du renderer en form som en mask, er det, som om den er udfyldt med sort, og alt under den bliver dækket.

{% hint style="info" %}
Det er nemt nok at tegne en linje (eller _stroke_) med en laser; du scanner laseren fra linjens begyndelse til linjens slutning. Så har du din linje!

Udfyldte former er sværere. Hvis du vil have en form udfyldt med farve, kan du manuelt krydsskravere ved at tegne linjer og fylde ud, men det kan Liberation ikke gøre automatisk (endnu). Og selv hvis vi gjorde det, ville du stadig kunne se andre linjer under den skinne igennem.

Det, vi til gengæld kan gøre, er at udfylde former med _sort_. Under motorhjelmen laver Liberation alle beregningerne for at fjerne indhold, der ligger under den sortudfyldte form. Og tro mig, det er noget pillearbejde!

Men det fungerer rigtig godt og giver illusionen af en sort udfyldt form.
{% endhint %}

### Dybdesortering

Da nogle former kan _dække_ andre former, skal Liberation sortere dem efter deres dybde. Som standard dybdesorteres elementer efter deres z-position. Hvis de har samme z-position, sorteres de efter deres lagposition, som kan ændres med knapperne _MOVE TO FRONT_ og _MOVE TO BACK_ inde i hver Creator.
