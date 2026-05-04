---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Oscylatory falowe

## Na tej stronie:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Fala piłokształtna](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Fala trójkątna](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Fala sinusoidalna](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Fala prostokątna](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Noise](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Custom Oscillator](wave-oscillators.md#custom-oscillator-1)

## Ustawienia oscylatorów falowych

Wszystkie oscylatory falowe mają następujące ustawienia:

* **range min / range max** — określa zakres wartości właściwości sterowanej przez oscylator. Właściwość przyjmuje wartość _range min_, gdy przebieg znajduje się na dole, oraz _range max_, gdy przebieg znajduje się na górze.

{% hint style="info" %}
Na przykład: jeśli chcesz, aby punkt poruszał się w lewo i w prawo między -100 a 100, podłącz oscylator do _x property socket_, ustaw _min range_ na -100, a _max range_ na 100.
{% endhint %}

* **duration** — czas trwania jednego pełnego cyklu (czyli _loop_). Jest on liczony względem tempa, w taktach. ¼ oznacza więc pojedyncze uderzenie. 1 oznacza pełny takt itd.
* **duration multiplier** — skaluje bazowe duration o wybrany współczynnik. Na przykład, jeśli duration jest ustawione na ćwierćnutę, a mnożnik wynosi 3, oscylator będzie trwał przez trzy ćwierćnuty (półnutę z kropką). Obsługiwane są też mnożniki ułamkowe — przytrzymaj _SHIFT_ podczas przeciągania suwaka, aby ustawić wartości niecałkowite. Jest to przydatne do efektów fazowania lub tworzenia subtelnych przesunięć czasowych.
* **offset** — początkowe przesunięcie fali jako procent duration. Jeśli chcesz, aby fala zaczynała się po jednej czwartej przebiegu, ustaw tę wartość na 25%.
* **repeat count** — liczba powtórzeń pętli przed zatrzymaniem. Domyślnie jest to _FOREVER_, ale możesz to zmienić, jeśli nie chcesz, aby oscylator działał bez końca. Po zatrzymaniu właściwość zostanie ustawiona na wartość z końca fali.
* **delay count** — opóźnienie w uderzeniach przed uruchomieniem oscylatora. Zanim oscylator zacznie działać, właściwość będzie ustawiona na wartość z początku fali.

{% hint style="info" %}
Ostrożnie używając _repeat count_ i _delay count_, możesz tworzyć bardzo złożone animacje — trochę jak własną oś czasu!
{% endhint %}

## Ustawienia wspólne

* **steps** — dzieli ruch na określoną liczbę dyskretnych kroków. Przydatne, gdy chcesz, aby właściwości „przeskakiwały” między wartościami zamiast płynnie się zmieniać.

{% hint style="info" %}
Pamiętaj, że kroki są dzielone według czasu, a nie wartości. Dlatego przy fali podzielonej na 4 kroki i duration równym 1 taktowi właściwość będzie zmieniać się natychmiast co każde uderzenie.
{% endhint %}

* **clamp min / clamp max -** zwiększa skalę fali poza jej wartości minimalne lub maksymalne, a następnie ogranicza wynik.

{% hint style="info" %}
Koncepcję _clamp_ dość trudno wyjaśnić, ale wyobraź sobie przebieg wychodzący poza górną lub dolną krawędź wykresu, a następnie przycinany do tych krawędzi. Polecam poeksperymentować z tymi ustawieniami! Są bardzo przydatne, jeśli chcesz, aby fala piłokształtna zaczynała się później albo kończyła wcześniej.
{% endhint %}

* **ease function** — fale Sawtooth i Triangle mają też funkcję easing, która subtelnie zmienia krzywą animacji i pozwala tworzyć znacznie bardziej ekspresyjne ruchy.
  * **LINEAR** — ustawienie domyślne, bez easing; ruch odbywa się liniowo między wartościami min i max.
* **EASE OUT** — zaczyna szybko, a następnie zwalnia przy końcu. Bardzo dobre do symulowania fizyki, np. wyhamowania do zatrzymania.
  * **EASE IN** — zaczyna powoli i stopniowo przyspiesza. Dobre do symulowania narastającego pędu.
  * **EASE IN/OUT** — połączenie obu efektów, dające bardzo organiczny ruch.

{% hint style="warning" %}
**Easing -** warto unikać domyślnej animacji liniowej, kiedy tylko możesz, chyba że celowo chcesz uzyskać efekt mechanicznego, „robotycznego” ruchu. Easing sprawia, że animacje są znacznie bardziej płynne i organiczne!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Fala piłokształtna

Czasem nazywana też _ramp waveform_, ponieważ narasta w górę, a następnie gwałtownie opada na końcu cyklu. To prawdopodobnie najczęściej używany oscylator falowy, bo tworzy pętlę przydatną do cyklicznej zmiany właściwości takich jak _hue_ czy _rotation._

Zobacz sekcje powyżej dotyczące:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Ustawienia specyficzne dla fali piłokształtnej:

* **cycle range compensation** — dostępne, gdy ustawione jest **steps**. Przydaje się do cyklicznych wartości, np. obrotu od 0 do 360. Gdy ta opcja nie jest włączona, wartości początkowa i końcowa będą takie same, co może powodować „przyklejenie” w punkcie startowym (bo 0 i 360 oznaczają ten sam kąt). Włącz tę opcję, aby zmniejszyć maksymalny zakres i skorygować pozycje kroków.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Fala trójkątna

W przeciwieństwie do _fali piłokształtnej_, która w każdym cyklu przeskakuje z powrotem na początek, _fala trójkątna_ porusza się liniowo do przodu, a potem do tyłu.

Zobacz sekcje powyżej dotyczące:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Fala sinusoidalna

Najpłynniejszy przebieg! Delikatnie oscyluje między dwiema wartościami, jak wahadło.

Zobacz sekcje powyżej dotyczące:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Fala prostokątna

Najprostszy przebieg — po prostu przełącza się między dwiema wartościami, tam i z powrotem.

Zobacz sekcje powyżej dotyczące:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Ustawienia specyficzne dla fali prostokątnej:

* **pulse width** — czas, przez jaki fala pozostaje na wartości maksymalnej, względem całkowitego duration. Domyślnie jest to 50%, czyli dokładnie pół na pół. Jeśli chcesz, aby była „włączona” tylko przez jedną czwartą czasu, ustaw 25%. Moment wystąpienia impulsu możesz dostosować za pomocą wartości _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Noise

Jedną z mocnych stron Liberation jest możliwość generowania losowych, ale powtarzalnych efektów. Oscylator _noise_ może służyć do tworzenia organicznego, zapętlonego ruchu losowego z dowolnym poziomem szczegółowości lub drżenia.

Zobacz sekcje powyżej dotyczące:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Ustawienia specyficzne dla Noise:

* **noise type** — algorytm używany do generowania szumu.
  * **SIMPLEX** — ustawienie domyślne; falująca wartość, która płynnie narasta i opada oraz powtarza się w pętli.
  * **RANDOM** — używa bardziej tradycyjnego algorytmu liczb losowych; efekt jest całkowicie zaszumiony i chaotyczny.

{% hint style="info" %}
**Simplex noise** został opracowany przez Kena Perlina w 2001 roku jako ulepszenie jego algorytmu „Perlin noise”, który stworzył w 1983 roku podczas pracy nad filmem _Tron_ (za co otrzymał Oscara!).

Ten tak zwany szum „gradientowy” powstał z frustracji wcześniejszymi, „maszynowo” wyglądającymi obrazami generowanymi komputerowo. W świecie CGI świetnie nadaje się zwłaszcza do renderowania chmur, powierzchni wody, a nawet map wysokości realistycznego terenu.

W Liberation sprawdza się natomiast do tworzenia pozornie nieprzewidywalnego ruchu, który nadal pozostaje płynny i organiczny.
{% endhint %}

* **seed** — wartość używana do utworzenia szumu. Jeśli nie podoba Ci się wygląd bieżącej fali szumu, spróbuj zmienić tę wartość.

{% hint style="info" %}
Ciekawostka dla nerdów! Aby uzyskać idealnie zapętlony simplex noise, iteruję po okręgu na dwuwymiarowej płaszczyźnie szumu. Zmiana wartości seed przesuwa tę płaszczyznę przez trzeci wymiar!
{% endhint %}

* **simplex detail** — zmienia poziom szczegółowości lub drżenia szumu. Jeśli chcesz, aby powtarzający się wzór był mniej oczywisty, zwiększ duration i podnieś tę wartość.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Custom Oscillator

Tworzy całkowicie własne przebiegi falowe. Jest to bardzo przydatne przy tworzeniu złożonych animacji.

Zobacz sekcje powyżej dotyczące:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Poniżej znajduje się lista pozycji i wartości. Duration jest podzielone na 64 kroki, a wartość możesz umieścić w dowolnym z tych punktów.

Każdy krok ma następujące ustawienia:

* **Step** — krok czasowy w ramach duration. 0 oznacza początek, a 64 koniec.
* **Level** — poziom fali w danym kroku czasowym. Level mieści się w zakresie od 0 do 1.
* **Animation type** — menu rozwijane pozwala wybrać, jak przejść do tego poziomu z poprzedniego kroku.
  * **None** — bez przejścia; natychmiastowy skok do tego poziomu w podanym czasie.
  * **Linear** — całkowicie liniowy ruch od poprzedniego poziomu do tego poziomu.
  * **Ease in / Ease out / Ease in/out** — easing między poprzednim poziomem a tym poziomem. Opis typów animacji znajdziesz powyżej w sekcji _ease function_.

***
