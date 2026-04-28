---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Ładowanie i zapisywanie

Liberation stale zapisuje swój stan na dysku, więc w razie awarii zasilania lub problemu z systemem uruchomi się dokładnie w miejscu, w którym praca została przerwana. Nie powinno dojść do utraty stref, timeline ani innych treści.

Możesz jednak wyeksportować swoją konfigurację, aby utworzyć kopię zapasową lub przenieść ją na inny komputer.

### Project Import/Export

Plik Project przechowuje prawie wszystko z bieżącej konfiguracji, w tym:

* Wszystko opisane poniżej w [#laser-settings-import-export](loading-and-saving.md#laser-settings-import-export)
* Clips, efekty oraz ustawienia grup
* Wszystkie timeline (bez multimediów audio i wideo)
* Konfigurację Artnet
* Ustawienia wysyłania/odbierania MIDI
* Ustawienia tempa / synchronizacji

Obecnie nie zapisuje ani nie wczytuje:

* Ustawień wejścia dźwięku i MIDI używanych w węźle MIDI notes oraz Sound Input Oscillator (zapisuje natomiast ustawienia wysyłania/odbierania MIDI oraz wejście dźwięku timecode)
* Skalowania interfejsu
* Multimediów dla obrazów pomocniczych Canvas
* Multimediów audio i wideo dla timeline
* Czcionek używanych w węźle Text

{% hint style="danger" %}
Pliki dźwiękowe i wideo w timeline nie są zapisywane razem z plikami projektu, więc zapisz je osobno, jeśli chcesz przenieść projekt na inny komputer. Zobacz [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Laser settings Import / Export

* Ustawienia laserów dla każdego lasera
* Beam zones
* Obszary docelowe Canvas
* DMX zones
* Przypisanie kontrolera laserowego (oraz aliasy wszystkich kontrolerów, którym zmieniono nazwy)
* Ustawienia i presety kalibracji skanerów laserowych oraz kolorów
* Ustawienia i presety 3D visualiser

### Clip Deck Import / Export

* Wszystkie clips oraz ich przypisania do stref, ustawienia i parametry
* Wszystkie ustawienia grup, flash mode, czasy fade in/out itd.

Obecnie nie zapisuje ani nie wczytuje:

* Wszystkich efektów oraz ich parametrów i ustawień

{% hint style="info" %}
**Wczytywanie clips z pliku projektu bez wczytywania całego projektu**

Aby zaimportować z projektu tylko clips, wybierz _**Clips->Import Clip Deck**_, a następnie zamiast pliku clip deck (.cpdk) wybierz plik projektu.
{% endhint %}

### Append clip deck

Za pomocą _Append Clip Deck_ możesz dodać clips z wyeksportowanego pliku clip deck do bieżącego projektu. Clips zostaną dodane na końcu obecnego clip deck, ale efekty i ustawienia grup znajdujące się w pliku nie zostaną zaimportowane.

### Export Selected Clips

Wszystkie aktualnie zaznaczone clips zostaną wyeksportowane do pliku. Ustawienia grup i efekty nie zostaną zapisane — tylko clips. Pamiętaj, że aktualnie uruchomione aktywne clips nie są eksportowane, chyba że również są zaznaczone.

{% hint style="info" %}
Aby zaznaczyć clips, użyj Option/Alt - shift - kliknięcie (albo użyj lassa). Zaznaczone clips rozpoznasz po grubej białej obwódce. Zobacz [starting-stopping-clips.md](clips/starting-stopping-clips.md)
{% endhint %}

### Effects Import / Export

Wczytuje i zapisuje wszystkie efekty wraz z ich ustawieniami grup i parametrami.

{% hint style="info" %}
**Wczytywanie efektów z pliku projektu bez wczytywania całego projektu**

Aby zaimportować z projektu tylko efekty, wybierz _**Effects->Import Effects**_, a następnie zamiast pliku efektów (.efts) wybierz plik projektu.
{% endhint %}

### Timeline Export

Eksportuje plik timeline zawierający jedną lub więcej timeline. Pamiętaj, że clipdeck jest zawsze dołączany do eksportowanych plików timeline (możesz jednak wybrać, które clips zaimportować z powrotem — zobacz [#timeline-import](loading-and-saving.md#timeline-import) poniżej).

Jeśli plik projektu zawiera więcej niż jedną timeline, otworzy się panel, w którym możesz wybrać timeline do eksportu.

{% hint style="danger" %}
Pliki dźwiękowe i wideo w timeline nie są zapisywane razem z plikami timeline, więc zapisz je osobno, jeśli chcesz przenieść zawartość na inny komputer. Zobacz [#important-note-about-timeline-media-files](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Timeline Import

Importuje jedną lub więcej timeline z pojedynczego pliku timeline. Po wybraniu pliku timeline otworzy się panel z wieloma opcjami importu.

Jeśli plik timeline zawiera więcej niż jedną timeline, wszystkie zostaną wyświetlone na liście. Zaznacz te, które chcesz uwzględnić.

* Replace existing timelines\
  Usunie wszystkie bieżące timeline i zastąpi je importowanymi
* Import used clips only\
  Zaimportuje tylko używane clips i ułoży je w grupach — po jednej dla każdej timeline. Jeśli ta opcja nie jest zaznaczona, cały clip deck z pliku timeline zostanie dopisany do istniejących clips.
* Replace existing clip deck\
  Zastępuje bieżący clip deck clips z pliku timeline. Dostępne tylko wtedy, gdy zaznaczono _Replace existing timelines_.

{% hint style="info" %}
**Wczytywanie timeline z pliku projektu bez wczytywania całego projektu**

Aby zaimportować z projektu tylko timeline, wybierz _**Timeline->Import Timeline(s)**_, a następnie zamiast pliku timeline (.ltml) wybierz plik projektu.
{% endhint %}

### DMX / Artnet import / export

Zapisuje i wczytuje węzły Artnet wraz z ich adresami IP. Obejmuje także DMX zones oraz wszystkie presety DMX.

### Ważna informacja o plikach multimedialnych timeline

Pliki dźwiękowe i wideo **nie są** obecnie eksportowane razem z plikiem timeline, więc jeśli musisz przenieść zawartość na inny komputer, upewnij się, że je dołączysz.

{% hint style="info" %}
**Jak timeline szuka plików multimedialnych**

Po wczytaniu timeline szuka plików w tym samym folderze co plik timeline (lub projekt) oraz w jego podfolderach. Jeśli więc pliki znajdują się w tym samym folderze albo w podfolderze (np. _/videos_ lub _/sound_), zostaną odnalezione podczas wczytywania.
{% endhint %}
