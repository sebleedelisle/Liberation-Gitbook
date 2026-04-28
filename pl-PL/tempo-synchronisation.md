---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / synchronizacja

Synchronizacja z muzyką to podstawowy element Liberation; gdy tempo i uderzenia są dopasowane do muzyki, możesz mieć pewność, że wszystko będzie zsynchronizowane. Jeśli masz dostęp do MIDI clock (lub Ableton Link), nie musisz w ogóle martwić się ręczną synchronizacją. Jeśli nie — bez obaw: możesz dopasować tempo ręcznie, korzystając z funkcji _Live_ tempo.

Jeśli masz doświadczenie z oprogramowaniem muzycznym lub oświetleniowym, ten proces będzie dla Ciebie znajomy. Jeśli nie, warto poświęcić trochę czasu na zapoznanie się z systemem i poćwiczyć w domu przed występem na żywo.

## Panel Tempo

Panel _Tempo_ jest zawsze widoczny na ekranie i zawiera wszystkie ustawienia synchronizacji. U góry zobaczysz bieżący licznik taktów/uderzeń oraz sekcję transportu z przyciskami odtwarzania/pauzy i przewijania do tyłu/do przodu.

Poniżej znajduje się znacznik rytmu: cztery kwadraty, które „pulsują” do uderzeń. Ten _beat marker_ jest wyjątkowo przydatną wizualizacją i będziesz często z niego korzystać podczas pracy z systemem _Live_ tempo.

### Ustawianie tempa

Tempo możesz ustawić na kilka sposobów:

* Kliknij i przeciągnij suwak _Tempo_
* Kliknij z klawiszem Shift i przeciągnij suwak _Tempo_, aby zmieniać tempo co 0,1
* Kliknij dwukrotnie suwak _Tempo_ i wpisz wartość ręcznie
* Użyj pokrętła _Tempo_ na APC40 (naciśnij Shift, aby zmieniać co 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo jest definiowane w „uderzeniach na minutę”, a tradyślna wartość domyślna to zwykle 120.
{% endhint %}

## Tap Tempo

Ustaw tempo automatycznie, klikając przycisk _TAP_ w rytm muzyki. Początek taktu ustaw przyciskiem _RESET_.

{% hint style="info" %}
System Tap Tempo jest na tyle inteligentny, że rozpoznaje, gdy zrobisz dłuższą przerwę w stukaniu albo pominiesz kilka uderzeń. Jeśli zaczniesz stukać w double time, zrozumie, że chcesz podwoić tempo; tak samo działa to przy stukaniu w half time.

Potrafi też wykryć, że dwie osoby jednocześnie wystukują tempo (np. jedna na klawiaturze, a druga na APC40). Liberation uśredni podwójne stuknięcia.
{% endhint %}

#### Skróty klawiaturowe:

T - tap tempo\
R - reset taktu\
Y - zaokrąglenie tempa do najbliższej wartości BPM.

{% hint style="info" %}
Ponieważ większość współczesnej muzyki powstaje cyfrowo, tempo najczęściej jest zaokrągloną liczbą całkowitą. Jeśli więc wystukane tempo wydaje się bliskie właściwemu, użyj klawisza Y (albo przesuń pokrętło tempa APC40 o jeden „klik”), aby zaokrąglić je do liczby całkowitej.
{% endhint %}

#### Sterowanie APC40:

APC40 ma dedykowany przycisk _TAP TEMPO_; możesz też użyć podłączonego przełącznika nożnego i wystukiwać tempo stopą!

Do regulacji użyj pokrętła _TEMPO_. Przytrzymaj _SHIFT_ podczas używania pokrętła _TEMPO_, aby wprowadzać dokładne korekty.

Użyj przycisku _METRONOME_, aby **zresetować takt**. (Pamiętaj, że przycisk _METRONOME_ świeci również w rytm uderzeń)

Obróć pokrętło _TEMPO_ o jeden „klik” w prawo lub w lewo, aby **zaokrąglić tempo** w górę lub w dół do pełnej wartości BPM.

Zobacz także [apc40-reference.md](reference/apc40-reference.md)

### Nudge tempo

Jeśli masz pewność, że tempo jest wystarczająco blisko właściwego, ale zauważasz, że zaczyna się rozjeżdżać z muzyką, użyj przycisków _NUDGE_, aby je skorygować.

Jeśli tempo Liberation wyprzedza muzykę, naciśnij i przytrzymaj _NUDGE -_, aby tymczasowo je zwolnić, aż ponownie się wyrówna.

Jeśli tempo Liberation zostaje za muzyką, naciśnij i przytrzymaj _NUDGE +_, aby tymczasowo je przyspieszyć, aż ponownie się wyrówna.

{% hint style="info" %}
Możesz używać przycisków NUDGE na ekranie albo dedykowanych przycisków na APC40.
{% endhint %}

### Half time / double time

Użyj przycisków _÷2_ i _x2_, aby na stałe zmniejszyć tempo o połowę lub je podwoić. W przeciwieństwie do mnożnika tempa jest to trwała zmiana bieżącego tempa.

## Tempo Multiplier

System _Tempo Multiplier_ pozwala tymczasowo zmienić tempo, a następnie wrócić do poprzedniej wartości.

Włącz lub wyłącz _Tempo Multiplier_, naciskając przycisk _TEMPO MULTIPLIER_ albo przycisk _BANK_ na APC40. Reguluj wartość suwakiem na ekranie lub suwakiem APC40 A-B. Możesz też użyć przycisków presetów _25%, 50%, 100% 200%_.

## Zewnętrzne źródła tempa

### MIDI Clock

Aby zsynchronizować się z zewnętrznym sygnałem MIDI clock, wybierz przycisk radiowy _MIDI CLOCK_ i wybierz urządzenie MIDI z menu rozwijanego. Zwróć uwagę na kolorową kontrolkę stanu obok menu rozwijanych:

* Zielony - odbierany jest sygnał MIDI clock
* Pomarańczowy - można połączyć się z urządzeniem MIDI, ale obecnie nie ma sygnału zegara
* Czerwony - nie można połączyć się z urządzeniem MIDI

{% hint style="info" %}
MIDI Clock nadaje serię ramek (24 na ćwierćnutę), ale komunikaty nie zawierają danych pozycji. Oznacza to, że pomaga utrzymać tempo, lecz nadal może być konieczne zresetowanie taktu.

Źródło tempa MIDI Clock w Liberation reaguje również na komunikaty **MIDI Machine Control (MMC)**, więc jeśli źródło zegara je przesyła, nie trzeba ręcznie resetować taktu.
{% endhint %}



### Timeline

Każda timeline ma własne tempo, które może być stałą wartością albo _Tempo Map_. _Tempo Map_ pozwala zmieniać tempo w określonych momentach na timeline.

Tempo timeline będzie używane, gdy jako źródło tempa wybrano _TIMELINE_.

{% hint style="info" %}
Timeline możesz uruchomić razem z _dowolnym_ źródłem tempa! Jeśli masz zespół grający na żywo bez kliku, możesz uruchomić timeline ręcznie i utrzymywać synchronizację za pomocą źródła tempa _LIVE_. A jeśli masz sygnał MIDI clock, możesz użyć właśnie jego!
{% endhint %}
