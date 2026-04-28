---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Kalibracja kolorów

Kalibracja kolorów zapewnia, że czerwony, zielony i niebieski laser w projektorze emitują światło w płynny i przewidywalny sposób na wszystkich poziomach jasności. Różne projektory mogą mieć nieliniowe krzywe jasności, co oznacza, że 50% czerwieni może wyglądać znacznie jaśniej lub ciemniej niż połowa intensywności 100% czerwieni. Kalibracja koryguje to zachowanie, dzięki czemu kolory mieszają się czysto, gradienty wyglądają płynnie, a biel jest zrównoważona.

#### Rozgrzewanie projektora

Diody laserowe zmieniają swoje zachowanie w miarę rozgrzewania. Przed kalibracją zawsze pozwól projektorowi się ustabilizować:

* Wyświetl jasną ramkę, na przykład **White rectangle test pattern (11)**, przez co najmniej **15–20 minut**.
* Dzięki temu ustawiony balans kolorów pozostanie stabilny podczas pokazu.

#### Jak działa test kalibracji

Do kalibracji użyj wzorców testowych (zobacz [wzorce testowe](../output-view/test-patterns.md))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Każdy z nich wyświetla cztery poruszające się linie:

* **Górna linia** – 100% jasności przy pełnej prędkości
* **Druga linia** – 75% jasności przy 75% prędkości
* **Trzecia linia** – 50% jasności przy 50% prędkości
* **Czwarta linia** – 25% jasności przy 25% prędkości

Ponieważ jednocześnie skalowane są jasność _i prędkość_, wszystkie linie powinny wyglądać na tak samo jasne. Jeśli któraś wygląda jaśniej lub ciemniej, reguluj odpowiedni suwak, aż linie będą do siebie pasować.

Każdy wzorzec testowy ma też piątą linię przy **0% jasności**, która nie powinna być widoczna. Służy ona do korekcji laserów, które nie emitują światła przy bardzo niskich poziomach. Jeśli laser pozostaje niewidoczny przy niskiej jasności, stopniowo zwiększaj **0% setting**, aż linia stanie się ledwo widoczna, a następnie lekko cofnij ustawienie, aż ponownie zniknie. Celem jest znalezienie progu, przy którym laser zaczyna świecić, i pozostanie tuż poniżej niego — tak aby przejścia fade zaczynały się naturalnie, bez odcinania dolnego zakresu.

#### Korzystanie z panelu Colour Calibration

Panel udostępnia niezależne ustawienia dla każdego kanału (czerwonego, zielonego i niebieskiego) na poziomach 100, 75, 50, 25 i 0%.

1. **Wybierz wzorzec testowy** (zacznij od czerwonego).
2. **Wyreguluj suwaki**, aby linie 100, 75, 50 i 25% wyglądały na tak samo jasne.
3. **Dostosuj suwak 0%**, jeśli linia „wyłączona” jest nadal lekko widoczna.
4. **Powtórz dla zielonego i niebieskiego.**
5. Przełącz na **White test pattern (8)**. Wszystkie cztery linie powinny wyglądać jednakowo, a biel powinna być neutralna (bez zabarwienia).

#### Regulacja balansu bieli

Tego systemu możesz też użyć do regulacji **balansu bieli**. Po skalibrowaniu każdego kanału osobno przełącz na **White test pattern (8)**. Jeśli wyjście wygląda na zabarwione (na przykład zbyt zielone lub zbyt niebieskie), dostosuj względne poziomy kanałów czerwonego, zielonego i niebieskiego, aż linie będą wyglądać na neutralnie białe. Nawet jeśli lasery znacznie różnią się mocą, kalibracja pomoże je do siebie zbliżyć i uzyskać czystsze, lepiej zrównoważone mieszanie kolorów.

#### Zapisywanie kalibracji

* Użyj **Store**, aby nadpisać bieżący preset.
* Użyj **Store As**, aby utworzyć nowy preset (przydatne, jeśli pracujesz z wieloma laserami).
