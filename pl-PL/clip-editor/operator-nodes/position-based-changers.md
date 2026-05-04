---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Modyfikatory zależne od pozycji

Ta grupa węzłów modyfikuje zawartość na podstawie pozycji. Domyślnie efekt jest stosowany wzdłuż osi poziomej (od lewej do prawej), ale możesz obrócić tę oś pod dowolnym kątem. Każdy węzeł zawiera też tryb _radial_, w którym efekt zależy od kąta każdego punktu względem środka.

* **Colour Changer by Position** – stosuje gradient wzdłuż wybranej osi lub wokół kąta radialnego.\
  \&#xNAN;_Przykład: utwórz tęczowy gradient przesuwający się po linii albo użyj trybu radial na okręgu, aby uzyskać efekt koła barw._
* **Wave Shift by Position** – stosuje zniekształcenie falą sinusoidalną, przesuwając zawartość pionowo (lub prostopadle do wybranej osi).\
  \&#xNAN;_Przykład: spraw, aby linia falowała jak woda, albo użyj trybu radial, aby okrąg pulsował na zewnątrz od środka._
* **Noise Shift by Position** – stosuje zniekształcenie szumem simplex, przesuwając zawartość pionowo (lub prostopadle do wybranej osi).\
  \&#xNAN;_Przykład: jak w przykładzie Wave Shift, ale z bardziej organicznym i losowym charakterem — idealne do dodawania naturalnej zmienności._

## &#x20;Zmiana koloru według pozycji

Ten węzeł stosuje zmiany koloru w zawartości na podstawie pozycji. Domyślnie oś jest pozioma (0°), ale możesz ją obrócić lub przełączyć w tryb radial.

* **wavelength** – ustawia rozmiar powtarzającego się cyklu kolorów.
  * _Tryb Linear:_ przy 100% jeden pełny cykl obejmuje całą szerokość zawartości.
  * _Tryb Radial:_ przy 100% jeden pełny cykl obejmuje cały okrąg (360°). Wartości są procentami okręgu: np. 50% = pół okręgu (180°).
* **offset** – przesuwa punkt początkowy cyklu kolorów jako procent wartości wavelength. Możesz modulować ten parametr (np. oscylatorem piłokształtnym), aby płynnie przechodzić przez kolory.
* **repeat** – po włączeniu cykl powtarza się w zawartości. Jeśli opcja jest wyłączona, gradient zostaje zastosowany tylko raz: wszystko przed początkiem ma kolor początkowy, a wszystko za końcem ma kolor końcowy.
* **pingpong** – po włączeniu każde powtórzenie zmienia kierunek, tworząc efekt lustrzany. Jeśli _Repeat_ jest wyłączone, gradient przechodzi do przodu, a następnie raz wraca. _Uwaga: w trybie Pingpong długość wavelength obejmuje zarówno przejście do przodu, jak i powrót._
* **linear angle** – obraca oś efektu. 0° = poziomo.
* **radial** – przełącza w tryb radial, stosując kolory na podstawie kąta od środka.
* **radial smooth loop** – automatycznie dostosowuje wavelength tak, aby równo dzieliła 100% okręgu, zapobiegając widocznemu szwowi w miejscu zapętlenia cyklu.
* **legacy mode** – przełącza na starsze suwaki HSB dla początku i końca. Zostaw tę opcję wyłączoną, aby używać nowszego edytora gradientu.

**Tryby koloru**

Określają, które aspekty korekcji koloru są stosowane do zawartości. Zobacz też: [Ustawienia koloru i HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – odcień pozostaje bez zmian.
  * _FIXED_ – odcień jest wymuszany na stałą wartość.
  * _SHIFTED_ – odcień jest przesuwany o określoną wartość (elementy o różnych kolorach nadal pozostają rozróżnialne, ale razem przesuwają się po kole barw).
* **saturation mode**
  * _OFF_ – nasycenie pozostaje bez zmian.
  * _FIXED_ – nasycenie jest ustawiane na określoną wartość.
* **brightness mode**
  * _OFF_ – jasność pozostaje bez zmian.
  * _FIXED_ – jasność jest ustawiana na określoną wartość.
  * _MULTIPLY_ – jasność jest skalowana określoną wartością. Zachowuje to dynamikę (np. migające elementy nadal migają, ale w ograniczonym zakresie jasności).

**Edytor gradientu**

Używa tego samego edytora gradientu co [Colour Changer](colour-changer.md "mention"), ale mapuje gradient na zawartość według położenia.

* Kliknij pasek gradientu, aby dodać punkt koloru.
* Kliknij punkt lewym przyciskiem myszy, aby go zaznaczyć, a następnie przeciągnij go na boki, aby go przesunąć.
* Aby usunąć punkt, przeciągnij zaznaczony punkt w dół, z dala od paska, albo naciśnij Delete/Backspace. Gradient zawsze zachowuje co najmniej dwa punkty.
* Kliknij punkt prawym przyciskiem myszy, aby edytować go za pomocą selektora koloru.
* Użyj **Position**, **Hue**, **Saturation** i **Brightness**, aby precyzyjnie edytować zaznaczony punkt.
* **interpolation** określa, jak kolory są mieszane między punktami:
* **HSB** – miesza odcień, nasycenie i jasność. To najlepszy wybór do płynnego ruchu w stylu tęczy wokół koła barw.
* **RGB** – miesza bezpośrednio wartości czerwonego, zielonego i niebieskiego. Często daje efekt bardziej podobny do przejścia kolorów na ekranie lub konsolecie oświetleniowej.
* **NONE** – przechodzi skokowo z jednego punktu do następnego, bez mieszania.
* **hue direction** jest dostępne przy interpolacji HSB:
* **AUTO** – wybiera najkrótszą drogę po kole odcieni.
* **FORWARDS** – zawsze przechodzi do przodu przez wartości odcienia.
* **BACKWARDS** – zawsze przechodzi do tyłu przez wartości odcienia.
* **blend** – miesza zmianę koloru z oryginalnymi kolorami. Przy 100% efekt całkowicie zastępuje oryginalne kolory.

**Starsze wartości początku i końca**

Jeśli **legacy mode** jest włączone, edytor gradientu zostaje zastąpiony starszymi kontrolkami:

* **start hue / end hue** – odcień na początku i końcu zakresu.
* **start saturation / end saturation** – nasycenie na początku i końcu zakresu.
* **start brightness / end brightness** – jasność na początku i końcu zakresu.

**Przykład 1: Przesuwający się tęczowy gradient**

Zaczynając od ustawień domyślnych:

1. Pozostaw węzeł w trybie **Linear** (kąt 0° = poziomo).
2. Pozostaw **wavelength** na 100% (obejmuje całą szerokość i powinno to być ustawienie domyślne).
3. Pozostaw domyślny gradient bez zmian.
4. Włącz **repeat**.
5. Dodaj **Sawtooth Oscillator** do ustawienia **offset**, tak aby przechodził od 0% do 100%.

***

**Przykład 2: Gradient czarny–biały–czarny (Pingpong)**

Zaczynając od ustawień domyślnych:

1. Pozostaw węzeł w trybie **Linear** (kąt 0° = poziomo).
2. Pozostaw **wavelength** na 100% (obejmuje całą szerokość i powinno to być ustawienie domyślne).
3. Wyłącz **repeat**.
4. Ustaw pierwszy punkt gradientu na czarny.
5. Ustaw końcowy punkt gradientu na biały.
6. Ustaw **hue mode** na OFF.
7. Ustaw **saturation mode** na FIXED, jeśli chcesz wymusić wynik w skali szarości.
8. Ustaw **brightness mode** na FIXED.
9. Włącz **pingpong**.

_Wynik: gradient przechodzi od czerni do bieli, a następnie z powrotem do czerni na całej szerokości._\
Pamiętaj, że jeśli zawartość ma zachować swój odcień i nasycenie, wyłącz Saturation mode. \\

***

**Przykład 3: Obracające się koło tęczowe (Radial)**

1. Włącz tryb **radial**.
2. Ustaw **wavelength** na 100% (pełne przejście 360°).
3. Włącz **repeat**.
4. Dodaj **Sawtooth Oscillator** do ustawienia **offset**, tak aby przechodził od 0% do 100%.

_Wynik: płynne koło barw, które nieustannie obraca się wokół okręgu._

## &#x20;Przesunięcie falą według pozycji

Ten węzeł stosuje zniekształcenie falą w zawartości, przesuwając punkty prostopadle do wybranej osi (lub radialnie od środka).

* **Wavelength** – ustawia długość cyklu fali.
  * _Tryb Linear:_ przy 100% jeden pełny cykl obejmuje całą szerokość zawartości.
  * _Tryb Radial:_ przy 100% jeden pełny cykl obejmuje pełne 360°. (Wartości są procentami okręgu: 50% = pół obrotu, 25% = ćwierć obrotu itd.)
* **Size** – steruje amplitudą fali (tym, jak daleko przesuwana jest zawartość).
* **Offset** – przesuwa falę wzdłuż osi (lub wokół okręgu w trybie radial). Jest to procent wartości wavelength, więc możesz animować ten parametr za pomocą **Oscillator Node**, aby fala się przemieszczała.
* **Radial** – przełącza z trybu liniowego na radialny, dzięki czemu przemieszczenie zależy od kąta względem środka.
* **Radial Smooth Loop** – dostosowuje wavelength tak, aby równo dzieliła 100% okręgu, zapobiegając widocznym szwom w miejscu zapętlenia.
* **Triangle** – zmienia kształt fali z sinusoidalnego na trójkątny.
* **Absolute** – przyjmuje wartość bezwzględną fali, tworząc wyłącznie przesunięcia w górę (zawijając ujemną stronę na dodatnią).
* **Angle** – obraca oś fali. 0° = poziomo.

## &#x20;Przesunięcie szumem według pozycji

Ten węzeł zniekształca zawartość za pomocą pola szumu (podobnego do turbulencji), przesuwając punkty prostopadle do wybranej osi (lub radialnie od środka). W porównaniu z _Wave Shift_ wynik jest bardziej organiczny i losowy.

* **Detail** – steruje szczegółowością szumu. Wyższe wartości = ostrzejsza, bardziej szczegółowa zmienność. Niższe wartości = gładsza zmienność.
* **Wavelength** – ustawia skalę wzoru szumu.
  * _Tryb Linear:_ przy 100% jeden pełny cykl szumu obejmuje szerokość zawartości.
  * _Tryb Radial:_ przy 100% jeden pełny cykl obejmuje pełne 360°.
* **Size** – steruje wielkością przemieszczenia (amplitudą zniekształcenia szumem).
* **Offset** – przesuwa wzór szumu wzdłuż osi (lub wokół okręgu). Jest to procent wartości wavelength, więc możesz animować ten parametr za pomocą **Oscillator Node**, aby szum „płynął”.
* **Depth Offset** – przesuwa przez pole szumu 3D, tworząc zmienność w czasie. Jest to szczególnie skuteczne po animowaniu za pomocą Oscillator Node.
* **Depth Detail** – steruje szczegółowością zmienności w wymiarze głębi.
* **Absolute** – przyjmuje wartość bezwzględną szumu, zawijając wartości ujemne na dodatnie (co daje przemieszczenie tylko w jedną stronę).
* **Angle** – obraca oś szumu w trybie liniowym. 0° = poziomo.
* **Radial** – przełącza z trybu liniowego na radialny, dzięki czemu przemieszczenie zależy od kąta względem środka.
* **Radial Smooth Loop** – dostosowuje wavelength tak, aby równo dzieliła 100% okręgu, zapobiegając widocznym szwom w trybie radial.
