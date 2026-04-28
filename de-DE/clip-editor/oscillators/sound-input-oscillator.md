---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input oscillator

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Wandelt den Pegel des Sound-Eingangs in einen Property-Wert um.

{% hint style="info" %}
Der Sound input oscillator verwendet das Standard-Soundinterface, du kannst es aber in _Preferences_ ändern. Öffne dazu das Menü _Liberation -> Preferences._

Unter den _Sound Input_-Einstellungen kannst du auswählen, welches Soundinterface du verwenden möchtest, sowie einige weitere Einstellungen zum Anpassen des Lautstärkepegels.
{% endhint %}

* **range min / range max** - die minimalen und maximalen Werte, auf die die Wellenform abgebildet wird
* **channel** - Wenn dein Soundinterface mehr als einen Eingangskanal hat, kannst du hier auswählen, welchen davon du verwendest.

{% hint style="info" %}
Eine interessante Technik ist es, mehrere Sound-Feeds vom Mischpult zu verwenden. So können verschiedene Clips auf unterschiedliche Musikinstrumente reagieren.
{% endhint %}

{% hint style="info" %}
Du kannst immer nur ein Soundinterface gleichzeitig für alle _Sound Inputs_ verwenden (ausgewählt im _App Settings_-Panel). Wenn du dafür mehr als ein Interface verwenden möchtest, kannst du unter macOS ein [Aggregate Device erstellen](https://support.apple.com/en-gb/HT202000), um Eingänge zu einer einzigen virtuellen Soundquelle zusammenzufassen. (Unter Windows gibt es ebenfalls viele Apps, die das können, aber ich habe sie nicht ausprobiert).
{% endhint %}

* **clamp min / clamp max** - damit wählst du aus, auf welchen Pegelbereich reagiert werden soll. Du solltest das normalerweise nicht anpassen müssen, wenn die Gate- und Limit-Einstellungen (im _App Settings_-Panel) korrekt eingestellt sind. Für kreative Effekte können diese Werte aber nützlich sein.

{% hint style="info" %}
Auf dem Clip-Button wird ein kleines Mikrofonsymbol angezeigt, sobald der Clip einen _Sound Input_ oscillator hat.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
