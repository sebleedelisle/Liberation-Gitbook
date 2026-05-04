---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Ändrar färgerna i allt inkommande innehåll. Du kan antingen ange fasta HSB-värden eller växla till gradientsystemet och hämta färger från en egen gradient.

* **hue, saturation, brightness** - färgvärdena, se [Färginställningar och HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - färgtonen ändras inte
  * FIXED - elementens färgton ställs in på värdet hue
  * SHIFT - elementens färgton förskjuts med värdet, så element med olika färger förblir olika, men flyttas längs färgtonsskalan.
* **saturation mode** -
  * OFF - mättnaden ändras inte
  * FIXED - mättnaden låses till det angivna värdet.
* **brightness mode** -
  * OFF - ljusstyrkan ändras inte
  * FIXED - elementens ljusstyrka ställs in på värdet brightness
  * MULTIPLY - elementens ljusstyrka kombineras med värdet brightness, så om de blinkar fortsätter de att blinka, men bara upp till den ljusstyrka som anges här.
* **gradient mode** - växlar från de fasta HSB-reglagen till gradientredigeraren. Denna node hämtar en färg från gradienten och använder den sedan med lägena för hue, saturation och brightness ovan.
* **gradient position** - väljer vilken punkt i gradienten som ska hämtas. Animera detta från 0 % till 100 % med en Sawtooth Oscillator för att gå igenom gradienten över tid.
* **blend** - hur starkt colour changer tillämpas. 0 % är inte alls, 100 % är fullt ut och 50 % är en kombination av den befintliga färgen och de nya värdena.

{% hint style="info" %}
Colour Change-node hämtar en färg från gradienten för hela indatan. Om du vill att gradienten ska löpa över formen baserat på position använder du [positionsbaserade ändrare](position-based-changers.md "mention") i stället.
{% endhint %}

### Gradientredigerare

När **gradient mode** är på visas gradientredigeraren under huvudkontrollerna.

* Klicka på gradientlisten för att lägga till ett färgstopp.
* Vänsterklicka på ett stopp för att markera det och dra det sedan i sidled för att flytta det.
* Dra ett markerat stopp nedåt bort från listen, eller tryck på Delete/Backspace, för att ta bort det. En gradient behåller alltid minst två stopp.
* Högerklicka på ett stopp för att redigera det med färgväljaren.
* Använd **Position**, **Hue**, **Saturation** och **Brightness** för att redigera det markerade stoppet exakt.
* **interpolation** väljer hur färger blandas mellan stopp:
* **HSB** - blandar hue, saturation och brightness. Detta passar bäst för mjuka regnbågsliknande rörelser runt färgcirkeln.
* **RGB** - blandar röda, gröna och blå värden direkt. Detta känns ofta mer som en färgövertoning på en skärm eller ett ljusbord.
* **NONE** - hoppar från ett stopp till nästa utan blandning.
* **hue direction** är tillgängligt vid HSB-interpolering:
* **AUTO** - tar den kortaste vägen runt hue-hjulet.
* **FORWARDS** - går alltid framåt genom hue-värdena.
* **BACKWARDS** - går alltid bakåt genom hue-värdena.
