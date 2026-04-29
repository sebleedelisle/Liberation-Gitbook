---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Sprzęt

#### **Czy Liberation działa w systemie Windows?**

Tak — Liberation w pełni obsługuje **Windows 10 i 11 (64-bit)**, z dokładnie tymi samymi funkcjami co wersja na Maca. Każde wydanie ukazuje się jednocześnie na obu platformach.

#### **Czy Liberation działa na Macu**

Tak — Liberation w pełni obsługuje **Mac (macOS 12 Monterey i nowsze)**, z pełną zgodnością funkcji z wersją na Windows. Wszystkie aktualizacje są wydawane równocześnie.

#### **Jakie są minimalne wymagania sprzętowe?**

To zależy od tego, iloma laserami chcesz sterować. Jeśli używasz tylko kilku laserów, wystarczy komputer o niższej specyfikacji. Każdy Mac z Apple Silicon działa bardzo dobrze i powinien bez problemu sterować nawet 100 laserami. Jeśli przygotowujesz złożone pokazy o dużym znaczeniu, zalecamy najlepszy komputer, na jaki możesz sobie pozwolić.

#### **Iloma laserami mogę sterować za pomocą Liberation?**

Liberation może obsługiwać wiele laserów na jednym komputerze. Program był testowany z ponad 100 kontrolerami laserowymi, więc odpowiedź zależy od:

* procesora w komputerze
* szybkości sieci
* typu subskrypcji

#### **Jakich kontrolerów MIDI mogę używać?**

Liberation został zaprojektowany i zoptymalizowany pod kątem popularnego kontrolera MIDI APC40 Mk2. Działa także z APC40 Mk1. Zobacz [live-control-with-the-apc40.md](midi-control/live-control-with-the-apc40.md)

Stopniowo dodajemy obsługę kolejnych kontrolerów MIDI. Obecnie obsługiwane są również APC Mini Mk2 oraz MIDI Fighter Twister.

Dostępny jest też system MIDI Send/Receive, który daje dodatkowe możliwości sterowania MIDI. Zobacz [midi-send-receive.md](midi-control/midi-send-receive.md)

Więcej informacji znajdziesz w sekcji [midi-control](midi-control/).

#### **Czy mogę użyć dowolnego kontrolera MIDI?**

Obecnie pracujemy nad konfigurowalnym systemem MIDI, który umożliwi to w przyszłości. Na razie niektórzy użytkownicy z powodzeniem korzystają z interpretera MIDI, który potrafi przekształcać dowolne komunikaty MIDI na potrzeby systemu MIDI Send/Receive, ale jest to dość żmudny i zaawansowany proces. Poszukaj porad dotyczących takiej konfiguracji na [forum](https://forum.liberationlaser.com), jednak w praktyce najlepszym wyborem jest APC40.

## Kontrolery laserowe

#### **Które kontrolery laserowe są kompatybilne z Liberation?**

* [Ether Dream (recommended)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (może być wymagana aktualizacja firmware)
* LaserCube USB (oraz LaserDock)
* Protokół sieciowy LaserCube (przy połączeniu przewodowym)
* AVB używane przez [LASollinger lasers](https://laseranimation.com/en/) (obecnie tylko macOS, w fazie testów)

Więcej informacji znajdziesz w [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Dlaczego nie obsługujecie kontrolera laserowego \[innej marki]?**

Aby wspierać większą interoperacyjność między oprogramowaniem i sprzętem, Liberation będzie obsługiwać tylko te DAC, które mają opublikowany protokół komunikacji. Uważam, że to najlepszy kierunek rozwoju dla branży laserowej.

#### **Jak sprawdzić, czy mój laser może być używany z Liberation?**

Jeśli Twój laser ma jedną z poniższych opcji, możesz używać go z Liberation:

* Zewnętrzne **wejście ILDA** — 25-pinowe złącze D, używane ze zgodnym zewnętrznym kontrolerem.
* Wewnętrznie zainstalowany **Ether Dream**.
* Dowolny **LaserCube** (działa zarówno z LaserCube USB, jak i Wi-Fi).
* **Urządzenie X-Laser z wbudowanym systemem Mercury** (w trybie Ether Dream).
* **Projektor LaserAnimation Sollinger z wbudowanym AVB** (tylko macOS, wymaga urządzeń sieciowych zgodnych z AVB, obecnie w fazie testów).

Więcej informacji znajdziesz w [compatible-lasers-and-controllers-dacs.md](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Czy mogę używać Liberation z moim LaserCube?**

Tak, Liberation działa bezpośrednio z dowolnym LaserCube. Zobacz [lasercube.md](hardware/lasercube.md)

## Licencje

#### **Jaka jest cena licencji?**

Aktualne ceny znajdziesz na stronie [shop](https://liberationlaser.com/shop).

#### **Jakie są różnice między poziomami licencji?**

Aktualne opcje licencji znajdziesz na stronie [shop](https://liberationlaser.com/shop).

Pamiętaj, że na **każdym** poziomie, nawet darmowym, możesz konfigurować, podglądać i projektować pokazy z dowolną liczbą laserów. Nie ma też żadnych innych ograniczeń poza liczbą laserów, które można _arm_. Wszystkie pozostałe funkcje Liberation są dostępne dla wszystkich.

#### **Czy mogę przejść na wyższy poziom licencji?**

Możesz przejść na wyższy poziom w dowolnym momencie. Otrzymasz częściowy zwrot za pozostały czas obecnej licencji, a nowy plan zacznie działać od razu. Zobacz [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md)

#### **Czy mogę obniżyć poziom licencji?**

Możesz obniżyć poziom licencji w dowolnym momencie, ale zmiana zacznie obowiązywać po zakończeniu bieżącego okresu licencyjnego. Zobacz [upgrade-downgrade-your-license.md](installation/upgrade-downgrade-your-license.md)

#### **Jak autoryzować komputer za pomocą licencji?**

Po zakupie licencji możesz autoryzować komputer bezpośrednio w programie Liberation. Na ekranie _About_ zobaczysz przycisk _Authorise_, który poprosi Cię o zalogowanie się na stronie internetowej. Postępuj zgodnie z instrukcjami na ekranie, aby ukończyć proces autoryzacji. Zobacz [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md)

#### **Jak często muszę łączyć komputer z internetem?**

Za każdym razem, gdy licencja jest odnawiana, trzeba połączyć Liberation z internetem, aby zaktualizować wewnętrzną licencję programu. Przy cyklicznej płatności miesięcznej trzeba połączyć się co miesiąc.

#### **Co się stanie, jeśli po odnowieniu nie będę mógł połączyć komputera z internetem?**

Liberation daje 7-dniowy okres karencji po odnowieniu licencji, aby połączyć się z internetem i zaktualizować wewnętrzną licencję. Po tym czasie Liberation wróci do trybu _Free_.

#### **Co się stanie, jeśli moja karta kredytowa wygaśnie?**

Otrzymasz powiadomienie e-mail od naszego dostawcy płatności i trzeba będzie zaktualizować metodę płatności. Zaloguj się na stronie internetowej i użyj linku _Update payment details_ na stronie subskrypcji.

#### **Jak anulować licencję odnawialną?**

Zaloguj się na stronie internetowej, otwórz stronę _Your subscriptions_, wybierz subskrypcję, którą chcesz anulować, a następnie kliknij link _Cancel Subscription_. Możesz nadal używać Liberation do końca okresu licencyjnego.

#### **Na ilu komputerach mogę zainstalować Liberation?**

Możesz zainstalować Liberation na dowolnej liczbie komputerów. Autoryzacje licencji są wymagane tylko do włączenia wyjścia laser / DMX, a poziom licencji określa, ile komputerów może być jednocześnie autoryzowanych do wyjścia. Zobacz [how-licensing-works.md](installation/how-licensing-works.md)

#### **Jak przenieść licencję z jednego komputera na inny?**

* Otwórz Liberation na komputerze, którego nie chcesz już używać
* Upewnij się, że masz połączenie z internetem, i kliknij przycisk _De-authorise this computer_ na ekranie _About_
* Teraz otwórz Liberation na nowym komputerze
* Kliknij przycisk _Authorise this computer_ na ekranie _About_.
* Otworzy się strona internetowa — zaloguj się i postępuj zgodnie z instrukcjami na ekranie, aby ukończyć autoryzację

Możesz też zdalnie cofnąć autoryzację komputera, do którego nie masz już dostępu (z pewnymi ograniczeniami). Zobacz [authorising-and-de-authorising.md](installation/authorising-and-de-authorising.md)

#### **Czy mogę cofnąć autoryzację Liberation na komputerze, który został zgubiony lub skradziony?**

Możesz cofnąć autoryzację komputera przez stronę internetową. Jeśli instalacja Liberation nie była online od czasu ostatniego odnowienia licencji, można to zrobić od razu.

W przeciwnym razie cofnięcie autoryzacji zacznie obowiązywać po odnowieniu subskrypcji albo po połączeniu komputera z internetem — zależnie od tego, co nastąpi wcześniej. Jeśli pilnie potrzebujesz ponownie autoryzować nowy komputer, skontaktuj się z pomocą techniczną.

### Korzystanie z Liberation

#### Domyślna konfiguracja ma 8 laserów — jak to zmienić?

Zobacz [setting-up-your-project.md](setting-up/setting-up-your-project.md) oraz [adding-removing-lasers.md](setting-up/adding-removing-lasers.md)

#### Czy mogę skopiować ustawienia stref z jednego lasera do pozostałych?

Tak! Zobacz [copy-zones-between-lasers.md](output-view/copy-zones-between-lasers.md)

#### Czy mogę wpisać liczbę zamiast używać suwaka?

Tak. Kliknij suwak z przytrzymanym `Cmd / Ctrl`, a następnie wpisz wartość z klawiatury.

#### **Jak zsynchronizować Liberation z muzyką?**

Program ma inteligentny system „tap tempo”, który działa tak, jak można się spodziewać, ale możesz też użyć zewnętrznego zegara MIDI albo Ableton Link. Zobacz [tempo-synchronisation.md](tempo-synchronisation.md). Oś czasu można zsynchronizować z przychodzącym kodem czasowym LTC/SMPTE przez dowolny interfejs audio. Zobacz [timecode.md](timecode.md).

#### Jakie ustawienia trzeba dostosować, aby uzyskać najlepszy sygnał wyjściowy z lasera?

Główne ustawienie to _Colour Shift_, które kompensuje niewielkie opóźnienie między ruchem luster a zmianą jasności laserów. Jeśli kropki lub wiązki lasera mają małe „ogonki”, trzeba dostosować to ustawienie. (Przykład „ogonków” znajdziesz na zdjęciach na stronie [laser-settings.md](setting-up/laser-settings.md))

Możesz też spróbować zmienić prędkość skanerów: wolniej, jeśli skanery są podstawowe, albo szybciej, jeśli są dobre. **Używaj jednak tego ostrożnie, bo zbyt mocne obciążenie skanerów może je uszkodzić.**

Dostępne są również gotowe presety ustawień skanerów. Opcja domyślna jest zachowawcza i odpowiednia dla większości zastosowań z wiązkami laserowymi. Są jednak też inne presety dla lepszych skanerów oraz presety dostrojone pod grafikę.

Więcej informacji znajdziesz w [laser-settings.md](setting-up/laser-settings.md), a informacje o tworzeniu własnych presetów znajdziesz w [scanner-presets.md](advanced/scanner-presets.md) (zaawansowane, w przygotowaniu)

Balans kolorów możesz też skorygować za pomocą ustawień _Colour calibration_. Zobacz [colour-calibration.md](advanced/colour-calibration.md) (technika zaawansowana)

#### Do czego służy ustawienie _Latency(ms)_?

To opóźnienie ramki, czyli maksymalny czas między wygenerowaniem ramki a jej późniejszym wysłaniem do lasera. Zwykle nie trzeba go zmieniać, ale jeśli masz problemy z siecią, możesz spróbować je zwiększyć. Więcej szczegółów znajdziesz w [latency-setting.md](setting-up/latency-setting.md).

### Clips

#### Jak dostosować strefy i ustawienia klipu bez jego uruchamiania?

Kliknij z przytrzymanym `Alt / Option`, aby ustawić go jako _aktualnie zaznaczony Clip_, ale bez aktywowania. Zobacz też [starting-stopping-clips.md](clips/starting-stopping-clips.md)

#### Jak kopiować klipy?

Kliknij i przeciągnij, trzymając klawisz `Alt / Option`. Zobacz też [organising-your-clip-deck.md](clips/organising-your-clip-deck.md)

#### Jak usuwać klipy?

Kliknij je i przeciągnij poza clip deck. Zobacz też [organising-your-clip-deck.md](clips/organising-your-clip-deck.md)

#### Jak zaznaczać wiele elementów, usuwać je, łączyć clip decki itp.?

Zobacz [organising-your-clip-deck.md](clips/organising-your-clip-deck.md)

#### Co oznacza mały symbol mikrofonu i inne ikony na klipie?

Służą do pokazania, że klip korzysta z wejścia dźwięku lub MIDI, a 3 kropki oznaczają opóźnienie strefy. Zobacz [what-are-the-small-icons-on-the-clip-buttons.md](clips/what-are-the-small-icons-on-the-clip-buttons.md)
