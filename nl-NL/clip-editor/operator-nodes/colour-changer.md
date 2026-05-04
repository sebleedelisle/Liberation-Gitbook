---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Wijzigt de kleuren van alle binnenkomende content. Je kunt vaste HSB-waarden instellen, of overschakelen naar het gradientsysteem en kleuren uit een eigen gradient samplen.

* **hue, saturation, brightness** - de kleurwaarden, zie [Kleurinstellingen en HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - de hue wordt niet gewijzigd
  * FIXED - de hue van elementen wordt ingesteld op de hue-waarde
  * SHIFT - de hue van elementen wordt verschoven met de waarde, zodat elementen met verschillende kleuren verschillend blijven, maar alleen langs de hue-waarde worden verschoven.
* **saturation mode** -
  * OFF - de saturation wordt niet gewijzigd
  * FIXED - de saturation wordt vastgezet op de opgegeven waarde.
* **brightness mode** -
  * OFF - de brightness wordt niet gewijzigd
  * FIXED - de brightness van elementen wordt ingesteld op de brightness-waarde
  * MULTIPLY - de brightness van elementen wordt gecombineerd met de brightness-waarde, zodat ze nog steeds knipperen als ze knipperen, maar alleen tot de hier opgegeven brightness.
* **gradient mode** - schakelt van de vaste HSB-sliders naar de gradient-editor. De node samplet één kleur uit de gradient en past die vervolgens toe met de modi voor hue, saturation en brightness hierboven.
* **gradient position** - kiest welk punt in de gradient wordt gesampled. Animeer dit van 0% tot 100% met een Sawtooth Oscillator om na verloop van tijd door de gradient te lopen.
* **blend** - hoe sterk de colour changer wordt toegepast: 0% is helemaal niet, 100% is volledig, en 50% is een combinatie van de bestaande kleur en de nieuwe waarden.

{% hint style="info" %}
De Colour Change-node samplet één kleur uit de gradient voor de volledige input. Als je wilt dat de gradient op basis van positie over de vorm loopt, gebruik dan in plaats daarvan [positiegebaseerde changers](position-based-changers.md "mention").
{% endhint %}

### Gradient-editor

Wanneer **gradient mode** aan staat, verschijnt de gradient-editor onder de hoofdinstellingen.

* Klik op de gradientbalk om een kleurstop toe te voegen.
* Klik met de linkermuisknop op een stop om deze te selecteren en sleep deze vervolgens zijwaarts om hem te verplaatsen.
* Sleep een geselecteerde stop omlaag, weg van de balk, of druk op Delete/Backspace om hem te verwijderen. Een gradient houdt altijd minimaal twee stops.
* Klik met de rechtermuisknop op een stop om deze met de kleurkiezer te bewerken.
* Gebruik **Position**, **Hue**, **Saturation** en **Brightness** om de geselecteerde stop nauwkeurig te bewerken.
* **interpolation** bepaalt hoe kleuren tussen stops worden gemengd:
* **HSB** - mengt hue, saturation en brightness. Dit is het meest geschikt voor vloeiende regenboogachtige bewegingen rond het kleurenwiel.
* **RGB** - mengt rode, groene en blauwe waarden direct. Dit voelt vaak meer als een kleurfade op een scherm of lichttafel.
* **NONE** - springt van de ene stop naar de volgende zonder menging.
* **hue direction** is beschikbaar bij HSB-interpolatie:
* **AUTO** - neemt de kortste route rond het hue-wiel.
* **FORWARDS** - loopt altijd vooruit door de hue-waarden.
* **BACKWARDS** - loopt altijd achteruit door de hue-waarden.
