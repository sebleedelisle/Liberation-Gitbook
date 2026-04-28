---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Kod czasowy

Liberation obsługuje synchronizację z zewnętrznym sygnałem kodu czasowego SMPTE/LTC, często używanym podczas koncertów do utrzymania świateł, pirotechniki, wideo i podkładów muzycznych w idealnym czasie.

{% hint style="info" %}
Czym jest SMPTE/LTC?

SMPTE to standard kodu czasowego, a LTC to ten kod czasowy zamieniony na sygnał audio. Jeśli go odsłuchasz, brzmi jak okropny, wysoki pisk, ale dla komputerów jest to precyzyjna informacja o czasie.

**Ciekawostki techniczne!**

Historycznie SMPTE służyło do synchronizacji obrazu i dźwięku. Przy synchronizacji z taśmą analogową jedna ścieżka mogła mieć nagrany sygnał audio z kodem czasowym — czasem nazywano to „striping” taśmy. Taka ścieżka kodu czasowego pozwalała utrzymywać kilka magnetofonów w synchronizacji albo synchronizować sekwencer MIDI z taśmą. (Dzięki temu nie trzeba było nagrywać instrumentów MIDI na taśmę — sekwencer mógł odtwarzać je na żywo podczas miksowania!)

SMPTE to skrót od Society of Motion Picture and Television Engineers, organizacji, która zdefiniowała ten standard. LTC oznacza _Linear TimeCode._
{% endhint %}

Sygnał kodu czasowego LTC możesz odebrać przez dowolny interfejs audio w komputerze, ale zalecany jest profesjonalny interfejs z co najmniej jednym regulowanym wejściem XLR i możliwością monitorowania.

Mam dobre doświadczenia z [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), ponieważ ma monitoring słuchawkowy, 2 wejścia XLR i nie wymaga żadnych specjalnych sterowników (przynajmniej w macOS). Jeśli zamierzasz używać go wyłącznie do kodu czasowego, możesz wybrać nieco tańszy [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (ma tylko jedno wejście i nie ma MIDI), ale szczerze mówiąc, każdy w miarę dobry interfejs audio powinien działać.

{% hint style="info" %}
Sygnały kodu czasowego LTC są zwykle przesyłane symetrycznymi kablami XLR, ponieważ są one wystarczająco odporne, aby przenosić sygnały audio o niskim poziomie na duże odległości. (XLR to okrągłe złącze zwykle używane z mikrofonami)
{% endhint %}

### Połączenia sprzętowe

Podłącz kabel XLR z sygnałem kodu czasowego do interfejsu audio i upewnij się, że odbierasz dobry sygnał. Wyreguluj poziom na interfejsie audio tak, aby sygnał był mocny, ale nie przesterowany. Jeśli interfejs audio ma wyjście słuchawkowe, możesz odsłuchać kod czasowy i sprawdzić, czy nie ma przerw, zakłóceń ani zbyt dużego szumu.

{% hint style="info" %}
Teoretycznie można odebrać sygnał przez gniazdo jack w MacBooku, ale wymagałoby to niestandardowego kabla. Takie gniazda to zwykle 4-polowe mini-jacki TRRS i szczerze mówiąc, nie mam pewności, które styki mogą służyć jako wejście audio. Nie mam też pewności, jaki poziom napięcia mogą przyjąć (gdzieś czytałem, że było to +/-1V, ale używasz tego na własne ryzyko!).

Moim zdaniem lepiej po prostu zdobyć tani interfejs audio USB, niż próbować takiego rozwiązania.
{% endhint %}

Jeśli interfejs audio nie ma żadnego monitorowania wejścia, możesz sprawdzić w ustawieniach systemowych macOS (w sekcji _Sound_), czy dociera sygnał. (W Windows użyj _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS pokazuje poziom wejściowy dowolnego interfejsu audio w panelu ustawień systemowych Sound</p></figcaption></figure>

### Konfiguracja w Liberation

1. Wybierz interfejs audio i właściwy kanał wejściowy w oknie Timecode settings.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Zwróć uwagę, że w menu rozwijanym są osobne opcje dla każdego kanału wejściowego w interfejsie audio.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Zwróć uwagę na kwadrat po lewej stronie. Jeśli odbierasz prawidłowy sygnał kodu czasowego, zmieni kolor na zielony. Jeśli nie, będzie czerwony.

2. Wybierz właściwą liczbę klatek na sekundę dla przychodzącego kodu czasowego. Osoba dostarczająca kod czasowy powinna być w stanie powiedzieć Ci, jaka to wartość. (Jeśli wybierzesz źle, synchronizacja nadal będzie działać, ale co sekundę zauważysz małe „przeskoczenie”)
3. Otwórz ustawienia kodu czasowego Timeline, używając małej ikony zegara na pasku timeline, i wybierz opcję SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Dostosuj przesunięcie początku (w godzinach, minutach, sekundach i klatkach), aby odpowiadało początkowi utworu. Jeśli masz kilka timelines, musisz ustawić te opcje osobno dla każdej z nich.

{% hint style="info" %}
W trasach koncertowych często stosuje się konwencję, w której każdy utwór zaczyna się od innej godziny, np. 01:00:00:00 dla pierwszego utworu, 02:00:00:00 dla drugiego itd.

Liberation automatycznie przełączy się na odpowiednią timeline zależnie od kodu czasowego, więc podczas show nie trzeba ręcznie zmieniać timelines.
{% endhint %}

Pamiętaj, że w odróżnieniu od MIDI Clock i Ableton Link, SMPTE jest _bezwzględnym_ systemem czasu, mierzonym w godzinach, minutach, sekundach i klatkach. Podstawowy system czasu w Liberation opiera się na bitach i taktach, więc po odebraniu kodu czasowego użyje tempa ustawionego w timeline. Musisz upewnić się, że to tempo jest zsynchronizowane z muzyką, która również jest zsynchronizowana z kodem czasowym.
