---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Modyfikatory ścieżki

## &#x20;Dotter

Ten węzeł zastępuje linie i kształty równomiernie rozmieszczonymi kropkami (istniejące kropki pozostają bez zmian).

* **Colour** – kolor kropek. Ignorowany, jeśli włączono _Inherit Colour_, patrz niżej. _Zobacz też_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – odległość między kropkami, mierzona w pikselach. Mniejsze wartości = więcej kropek, większe wartości = mniej.
* **Offset** – przesuwa pozycję początkową kropek jako procent wartości spacing. Można animować (np. za pomocą węzła Oscillator Node z przebiegiem piłokształtnym), aby tworzyć efekty „wędrujących” kropek.
* **Keep Original** – jeśli włączone, oryginalne linie/kształty są zachowane, a kropki są rysowane na wierzchu.
* **Render Profile** – wybiera jakość renderowania. _Zobacz_ [render-profile.md](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – automatycznie dostosowuje odstępy, tak aby długość ścieżki dzieliła się równomiernie.
* **Fade Out Ends** – stopniowo zmniejsza jasność kropek w kierunku początku i końca ścieżki. Przydatne podczas animowania **Offset** za pomocą węzła Oscillator Node z przebiegiem piłokształtnym, dzięki czemu kropki płynnie pojawiają się i znikają, gdy przesuwają się do końca kształtu.

## &#x20;Trimmer

Ten węzeł przycina widoczną długość linii i kształtów, pozwalając je odsłaniać, ukrywać lub animować w czasie.

* **Offset** – określa, gdzie zaczyna się widoczna część kształtu. Nawet przy _Trim Size_ ustawionym na 0%, animowanie Offset od 0% → 100% sprawia, że kształt się rysuje, staje się w pełni widoczny przy 50%, a następnie ponownie znika.
* **Trim Size** – ustawia, jaka część kształtu zostaje zachowana, jako procent jego całkowitej długości.
* **Loop** – traktuje kształt jako ciągłą pętlę, więc koniec łączy się z początkiem zamiast znikać.
* **All Shapes** – łączy wszystkie kształty wejściowe i przycina je tak, jakby były jedną ścieżką. Jeśli wyłączone, każdy kształt jest przycinany osobno.
* **Add Dot at Start / Add Dot at End** – dodaje kropkę w wybranym kolorze w punktach przycięcia. (Jeśli nie zastosowano przycięcia, kropki nie są dodawane).
* **Colour** – kolor kropek przycięcia. _Zobacz też_ [colour-settings-and-hsb.md](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – wybiera profil renderowania dla kropek. _Zobacz_ [render-profile.md](../fundamentals/render-profile.md)
