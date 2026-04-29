---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Wprowadzenie do Clip Editor

Edytor klipów to wszechstronny sposób tworzenia treści laserowych i jeden z kluczowych elementów Liberation. Łatwo zrobisz w nim proste rzeczy, ale jest też wystarczająco elastyczny, aby tworzyć bardzo zaawansowane i złożone efekty.

{% hint style="info" %}
Edytor oparty na węzłach był pierwszą częścią Liberation, która powstała! Narodził się z rozmowy z Robem Stanleyem podczas spotkania laserowego w Wielkiej Brytanii w 2018 roku, o tym, jak mógłby wyglądać „obiektowy” projektant treści laserowych.

Choć wygląda prosto, jest to dość złożony system do zbudowania, ale na początku 2019 roku miałem już działające demo potwierdzające koncepcję — i tak zaczęła się cała ta droga!
{% endhint %}

To wizualny edytor oparty na węzłach (czyli [node graph architecture](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), który będzie znajomy, jeśli korzystasz z takich produktów jak TouchDesigner, MaxMSP lub VVVV. Clip Editor jest jednak nieco inny i trochę prostszy, ponieważ został zaprojektowany specjalnie do grafiki wektorowej.

Aby otworzyć Clip Editor, kliknij prawym przyciskiem myszy przycisk klipu i wybierz _EDIT CLIP_. Możesz też kliknąć prawym przyciskiem myszy pusty przycisk klipu i wybrać _CREATE AND EDIT CLIP_.

### Przegląd

W Clip Editor zobaczysz:

* Przyciski węzłów **Creator** i **Operator** u góry
* Przyciski węzłów **Oscillator** po lewej
* Podgląd treści w panelu po prawej, a po kliknięciu węzła także drugi podgląd pokazujący treść na samym węźle.
* Wszystkie węzły i połączenia klipu, który edytujesz (jeśli to nowy klip, obszar będzie pusty)
* Panel Clip Editor z różnymi opcjami

Podczas edycji będziesz też widzieć wygląd klipu w tle, w 3D Visualiser.

{% hint style="info" %}
Jeśli nie widzisz żadnego wyjścia w 3D Visualiser, może być konieczne użycie przycisków stref, aby włączyć wybrane strefy. Upewnij się też, że opcja _Preview to lasers_ jest włączona; zobacz [Wprowadzenie do Clip Editor](clip-editor-intro.md#clip-editor-panel) poniżej.
{% endhint %}

### Tworzenie klipu

Zwykle zaczyna się od jednego lub kilku [Węzły Creator](creator-nodes.md), a następnie łączy [Węzły operatorów](operator-nodes/) od lewej do prawej, aby przetwarzać treść. Gdy przesuwasz węzły Creator i/lub Operator blisko siebie, zauważysz, że automatycznie się łączą. Możesz je ponownie rozdzielić, przeciągając je od siebie.

### Dodawanie węzłów do klipu

Kliknij i przeciągnij jeden z przycisków węzłów u góry lub po lewej do pustego miejsca w Clip Editor.

### Zmienianie ustawień węzła

Kliknij przycisk z ikoną koła zębatego (w prawym górnym rogu węzła), aby otworzyć panel właściwości tego węzła.

### Włączanie i wyłączanie węzła

Kliknij przycisk z ikoną zasilania (w lewym górnym rogu węzła), aby włączyć lub wyłączyć węzeł. Węzeł zostanie przyciemniony, aby pokazać, że nie jest aktualnie aktywny. Pamiętaj, że treść nadal przechodzi przez operator, nawet gdy jest on wyłączony, ale węzeł nie wpływa wtedy na treść.

### Łączenie węzłów

Treść jest tworzona za pomocą węzła Creator i przekazywana przez kolejne węzły od lewej do prawej; każdy operator w jakiś sposób wpływa na treść i przekazuje ją do następnego operatora. To, co pozostanie na końcu ścieżki, staje się treścią klipu. Węzły Creator i Operator automatycznie łączą się ze sobą, gdy przesuniesz je blisko siebie. Aby je rozdzielić, ponownie przeciągnij je od siebie.

{% hint style="info" %}
Możesz podłączyć więcej niż jeden węzeł do wejścia następnego węzła. Przydaje się to do łączenia wielu elementów treści.
{% endhint %}

### Właściwości węzłów i gniazda

Każdy węzeł ma na dole zestaw gniazd, a każde z nich reprezentuje jedną właściwość węzła, taką jak jasność, pozycja, skala, obrót itp.

[Węzły Oscillator](oscillators/) można podłączać do tych gniazd od dołu i używać ich do animowania tych ustawień. Węzły Oscillator mają wyjście u góry — kliknij i przeciągnij, aby wyciągnąć połączenie, a następnie upuść je na jednym z gniazd właściwości innego węzła.

### Węzły Oscillator

Węzły Oscillator służą do zmieniania właściwości w czasie. Zwykle reprezentują przebiegi, takie jak fala piłokształtna lub sinusoidalna, ale niektóre węzły Oscillator używają jako źródła wejść zewnętrznych (na przykład poziomu wejścia mikrofonowego).

{% hint style="info" %}
Jeśli kiedykolwiek używałeś syntezatora analogowego, znasz koncepcję oscylatorów, które zwykle służą do tworzenia przebiegów lub zmieniania dźwięku w czasie. Oscylatory w Liberation pełnią podobną funkcję.

**Ciekawostka:** nazwa _Liberation_ została zainspirowana instrumentem Moog Liberation — syntezatorem typu „keytar” wydanym w 1980 roku i rozsławionym przez Herbiego Hancocka, Jeana-Michela Jarre’a, a nawet Jamesa Browna!
{% endhint %}

Oscylatory zawsze mają ustawienia _range_, które kontrolują minimalną i maksymalną wartość regulowanej właściwości. Z kolei _Wave Oscillators_ zawsze mają ustawienie _duration_, które określa, jak szybko oscylator zmienia wartość. Więcej informacji znajdziesz w [Oscylatory falowe](oscillators/wave-oscillators.md).

### Panel Clip Editor

* Timer — u góry panelu zobaczysz bieżący czas klipu w trakcie jego odtwarzania
* _RETRIGGER_ — uruchamia klip ponownie od początku; szczególnie przydatne, jeśli klip nie zapętla się
* _Preview to lasers_ — gdy ta opcja jest zaznaczona, 3D Visualiser będzie aktualizować się podczas edycji tego klipu. Jeśli ją wyłączysz, zobaczysz klipy uruchomione poza edytorem. To ustawienie globalne, a nie osobne dla każdego klipu.
* _UNDO/REDO_ — dotyczy samego Clip Editor. Przypisane również do `Cmd / Ctrl + Z` oraz `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ — zapisuje zmiany, ale ostrzega przed nadpisaniem
* _SAVE AS A COPY_ — zapisuje klip w następnym dostępnym slocie w Clip Deck. To staje się nową pozycją klipu, a wszystkie kolejne zapisy będą trafiać właśnie tam.
* _EXIT EDITOR_ — zamyka Clip Editor. Jeśli masz niezapisane zmiany, pojawi się panel potwierdzenia.
