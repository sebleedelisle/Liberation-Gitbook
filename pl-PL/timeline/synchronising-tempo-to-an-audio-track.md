---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Synchronizacja tempa ze ścieżką audio

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchronizacja tempa ze ścieżką audio" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Timeline w Liberation jest zaprojektowany do pracy ze stałym lub zmiennym tempem, ale niezawodna synchronizacja zawsze zaczyna się od znalezienia tempa i poprawnego wyrównania audio. Ta sekcja opisuje zalecany sposób pracy.

#### 1. Wyrównaj pierwszy mocny akcent taktu

Dodaj ścieżkę audio do timeline i upewnij się, że jest przyciągnięta do uderzenia, tak aby **pierwszy mocny akcent muzyczny** ścieżki pokrywał się dokładnie z początkiem taktu.

Ten krok jest kluczowy.

Jeśli audio nie zaczyna się naturalnie od mocnego akcentu taktu, masz dwie możliwości:

* **Dostosuj opóźnienie klipu**\
  Kliknij klip audio prawym przyciskiem myszy i dostosuj wartość Delay, aż pierwszy mocny akcent wyrówna się ze znacznikiem uderzenia lub taktu.
* **Przytnij audio zewnętrznie**\
  Edytuj plik audio w zewnętrznym edytorze, takim jak Audacity, tak aby plik zaczynał się dokładnie od pierwszego mocnego akcentu, a następnie zaimportuj go ponownie.

{% hint style="info" %}
**Ważne:**\
Jeśli początek audio nie jest wyrównany do uderzenia lub taktu, odczuwalna pozycja startowa muzyki będzie przesuwać się do tyłu i do przodu podczas zmiany tempa. Bardzo utrudnia to dokładne dopasowanie tempa.
{% endhint %}

#### 2. Ustaw tempo początkowe

Jeśli masz przybliżone pojęcie o BPM, wpisz tę wartość w kontrolce tempa timeline i rozpocznij odtwarzanie od początku.

Podczas odtwarzania utworu uważnie obserwuj znaczniki uderzeń i taktów.

* Jeśli znaczniki wyprzedzają muzykę, nieznacznie zmniejsz tempo.
* Jeśli zostają w tyle, nieznacznie zwiększ tempo.
* Zatrzymaj odtwarzanie, dostosuj tempo i spróbuj ponownie.

W większości nowoczesnej muzyki tempo ma stałą, całkowitą wartość BPM. Gdy znajdziesz poprawną wartość, powinna pozostać zsynchronizowana przez cały utwór.

#### 3. Użyj przebiegu fali jako wizualnej wskazówki

Przebieg fali audio jest przydatnym punktem odniesienia podczas dopasowywania tempa.

* Transjenty i szczyty powinny pokrywać się z pionowymi znacznikami taktów.
* Przybliż widok, aby sprawdzić wyrównanie na przestrzeni kilku taktów.

**Wskazówka:**\
Użyj kółka myszy lub gestu na trackpadzie, aby przybliżać i oddalać timeline. Użyj poziomego kółka przewijania lub gestu, aby przesuwać widok w lewo i w prawo. Praca w przybliżeniu znacznie ułatwia drobne korekty.

#### 4. Utwory z niecałkowitym BPM

Jeśli utwór nie używa całkowitej wartości BPM, dryf będzie bardziej stopniowy.

* Przybliż widok jeszcze bardziej.
* Wprowadzaj mniejsze korekty tempa.
* Sprawdzaj wyrównanie na dłuższych fragmentach utworu, a nie tylko na kilku pierwszych taktach.

#### 5. Muzyka ze zmianami tempa

Jeśli muzyka przyspiesza lub zwalnia, użyj Tempo Map:

* Odtwarzaj utwór i obserwuj znaczniki uderzeń.
* Gdy dryf stanie się zauważalny, dodaj w tym miejscu zmianę tempa.
* Dostosuj tempo dla nowej sekcji, aż ponownie się zsynchronizuje.

Powtórz ten proces dla każdej zmiany tempa w muzyce.

#### 6. Zewnętrzna analiza tempa (opcjonalnie)

W ostateczności możesz przeanalizować utwór w DAW, takim jak Logic Pro, i automatycznie wygenerować mapę tempa. Pamiętaj, że często tworzy to dużą liczbę zmian tempa, czasem jedną na takt, co w przypadku większości pokazów może być bardziej szczegółowe, niż jest to potrzebne.
