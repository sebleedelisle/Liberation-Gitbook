---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Zmiana koloru

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Zmiana koloru

Zmienia kolory całej treści przychodzącej. Możesz ustawić stałe wartości HSB albo przełączyć się na system gradientów i pobierać kolory z własnego gradientu.

* **hue, saturation, brightness** - wartości koloru, zobacz [Ustawienia koloru i HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - odcień nie jest zmieniany
  * FIXED - odcień elementów jest ustawiany na wartość hue
  * SHIFT - odcień elementów jest przesuwany o tę wartość, więc elementy o różnych kolorach pozostaną różne, ale zostaną przesunięte na skali odcienia.
* **saturation mode** -
  * OFF - nasycenie nie jest zmieniane
  * FIXED - nasycenie jest ustawiane na określoną wartość.
* **brightness mode** -
  * OFF - jasność nie jest zmieniana
  * FIXED - jasność elementów jest ustawiana na wartość brightness
  * MULTIPLY - jasność elementów jest łączona z wartością brightness, więc jeśli migają, nadal będą migać, ale tylko do jasności określonej tutaj.
* **gradient mode** - przełącza ze stałych suwaków HSB na edytor gradientu. node pobiera jeden kolor z gradientu, a następnie stosuje go przy użyciu powyższych trybów barwy, nasycenia i jasności.
* **gradient position** - wybiera punkt gradientu, z którego pobierany jest kolor. Animuj tę wartość od 0% do 100% za pomocą Sawtooth Oscillator, aby z czasem przechodzić przez cały gradient.
* **blend** - jak silnie stosowana jest zmiana koloru: 0% oznacza brak wpływu, 100% pełne zastosowanie, a 50% połączenie istniejącego koloru z nowymi wartościami.

{% hint style="info" %}
node Colour Change pobiera z gradientu jeden kolor dla całego wejścia. Jeśli chcesz, aby gradient przebiegał przez kształt zależnie od pozycji, użyj zamiast tego [modyfikatorów opartych na pozycji](position-based-changers.md "mention").
{% endhint %}

### Edytor gradientu

Gdy **gradient mode** jest włączony, edytor gradientu pojawia się pod głównymi kontrolkami.

* Kliknij pasek gradientu, aby dodać punkt koloru.
* Kliknij punkt lewym przyciskiem myszy, aby go zaznaczyć, a następnie przeciągnij go w bok, aby go przesunąć.
* Przeciągnij zaznaczony punkt w dół, poza pasek, albo naciśnij Delete/Backspace, aby go usunąć. Gradient zawsze zachowuje co najmniej dwa punkty.
* Kliknij punkt prawym przyciskiem myszy, aby edytować go za pomocą próbnika kolorów.
* Użyj **Position**, **Hue**, **Saturation** i **Brightness**, aby precyzyjnie edytować zaznaczony punkt.
* **interpolation** wybiera sposób mieszania kolorów między punktami:
* **HSB** - miesza barwę, nasycenie i jasność. To najlepszy wybór do płynnego ruchu w stylu tęczy po kole barw.
* **RGB** - miesza bezpośrednio wartości czerwieni, zieleni i niebieskiego. Często przypomina to bardziej przejście kolorów na ekranie lub w konsolecie oświetleniowej.
* **NONE** - przeskakuje z jednego punktu do następnego bez mieszania.
* **hue direction** jest dostępne przy interpolacji HSB:
* **AUTO** - wybiera najkrótszą drogę po kole barw.
* **FORWARDS** - zawsze przechodzi do przodu przez wartości barwy.
* **BACKWARDS** - zawsze przechodzi do tyłu przez wartości barwy.
