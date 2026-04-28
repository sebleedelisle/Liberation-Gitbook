---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscylator Sound input

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Konwertuje poziom sygnału wejściowego audio na wartość właściwości.

{% hint style="info" %}
Oscylator Sound input używa domyślnego interfejsu audio, ale możesz go zmienić w _Preferences_. Otwórz menu _Liberation -> Preferences._

W ustawieniach _Sound Input_ możesz wybrać interfejs audio, którego chcesz używać, oraz skonfigurować kilka innych ustawień służących do regulacji poziomu głośności.
{% endhint %}

* **range min / range max** - minimalna i maksymalna wartość, na które mapowany jest przebieg
* **channel** - jeśli Twój interfejs audio ma więcej niż jeden kanał wejściowy, tutaj możesz wybrać, z którego kanału chcesz korzystać.

{% hint style="info" %}
Ciekawą techniką jest pobranie kilku sygnałów audio ze stołu mikserskiego. Dzięki temu różne klipy mogą reagować na różne instrumenty muzyczne.
{% endhint %}

{% hint style="info" %}
W całej aplikacji możesz używać tylko jednego interfejsu audio naraz dla wszystkich _Sound Inputs_ (wybranego w panelu _App Settings_). Jeśli chcesz używać do tego więcej niż jednego interfejsu, w macOS możesz [utworzyć Aggregate Device](https://support.apple.com/en-gb/HT202000), aby połączyć wejścia w jedno wirtualne źródło dźwięku. (W Windows jest też wiele aplikacji, które to umożliwiają, ale ich nie testowałem).
{% endhint %}

* **clamp min / clamp max** - użyj tych ustawień, aby wybrać zakres poziomów, na który chcesz reagować. Nie powinno być potrzeby ich regulowania, jeśli ustawienia gate i limit (w panelu _App Settings_) są poprawnie dobrane, ale można ich użyć do uzyskania ciekawych efektów.

{% hint style="info" %}
Na przycisku klipu zobaczysz małą ikonę mikrofonu zawsze wtedy, gdy klip ma oscylator _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
