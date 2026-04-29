# ✅ Szybki start

## Wprowadzenie

Witamy w **Liberation** — oprogramowaniu do pokazów laserowych nowej generacji.

Liberation to nowoczesne, zaawansowane i rozbudowane oprogramowanie. Zostało oparte na solidnych podstawach użyteczności i niezawodności, aby dać Ci swobodę twórczego działania. Jest szybkie, wydajne i płynne w obsłudze. Skorzystaj z tego _Szybkiego startu_, aby szybko rozpocząć pracę!

### Zarządzanie laserami

Liberation jest na tyle elastyczne, że możesz skonfigurować lasery i wizualizować je nawet wtedy, gdy żadne fizyczne lasery nie są podłączone. Gdy wszystko będzie gotowe, możesz płynnie przypisać każde wyjście do laser controller.

{% hint style="info" %}
W Liberation możesz skonfigurować i wizualizować dowolną liczbę laserów. Poziomy licencji (Hobbyist, Pro itd.) ograniczają tylko liczbę laserów, które mogą być w stanie _armed_. Oznacza to, że nawet z darmową licencją możesz projektować pokazy laserowe ze 100 laserami. Aktualizacja licencji jest potrzebna dopiero wtedy, gdy chcesz uruchomić pokaz na rzeczywistych laserach.
{% endhint %}

Domyślna konfiguracja zawiera 8 laserów rozmieszczonych poziomo, ale możesz dostosować ją do własnych potrzeb. Na początku najlepiej pozostawić ustawienia domyślne, a później dopasować je do swojej konfiguracji sprzętowej. Zobacz [Konfigurowanie projektu](../setting-up/setting-up-your-project.md).&#x20;

{% hint style="warning" %}
Ważne: zanim ustawisz jakikolwiek laser w stan armed, upewnij się, że rozumiesz związane z tym ryzyko, i dokładnie przejdź przez rozdział [Konfigurowanie laserów](../setting-up/setting-up-lasers.md).
{% endhint %}

## Omówienie oprogramowania

### Awaryjne wyłączenie

Za każdym razem, gdy używasz laserów, musisz mieć pod ręką **sprzętowy przycisk awaryjnego zatrzymania** (zobacz [Zatrzymanie awaryjne / blokady bezpieczeństwa](../hardware/emergency-stop-interlocks.md)). Jeśli jednak chcesz mniej pilnie przełączyć wszystko w stan disarmed, możesz użyć przycisku _**DISARM ALL**_, klawisza `Escape` albo klawisza _**SESSION**_ na APC40. Możesz też zmniejszyć Global Brightness za pomocą suwaka na ekranie albo głównego fadera na APC40.

### Suwaki i elementy sterujące

W Liberation znajdziesz różne suwaki i elementy sterujące.

{% hint style="info" %}
Kliknij suwak z wciśniętym `Cmd / Ctrl`, aby wpisać nową wartość, jeśli potrzebujesz większej precyzji niż ta, którą daje sam suwak.
{% endhint %}

### Skróty klawiaturowe

Pełną listę skrótów klawiaturowych znajdziesz tutaj: [Skróty klawiaturowe](../reference/keyboard-shortcuts.md)

### Układ ekranu

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nie wiesz, do czego służy dany przycisk? Najedź na niego kursorem myszy, aby zobaczyć opis.
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

W menu znajdziesz wszystkie opcje importu i eksportu plików oraz otwierania paneli. Tutaj znajduje się też opcja autoryzacji komputera w ramach subskrypcji: _Liberation -> Authorise/Deauthorise this computer_.

#### Pasek ikon

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Tutaj znajdują się często używane funkcje, takie jak przełączanie wszystkich laserów między stanami armed i disarmed, Global Brightness, test pattern oraz przełączanie między widokami 3D, Canvas i Output.

### Widoki

Duży obszar w lewym górnym rogu ekranu może wyświetlać jeden z 3 głównych widoków: **3D**, **CANVAS** albo **OUTPUT**. Przełączasz je przyciskami na pasku ikon. Możesz też użyć klawisza `Tab`, aby przełączać się między widokami 3D i OUTPUT, a następnie kolejno przechodzić przez wyjście każdego lasera.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view pokazuje, jak będą wyglądały Twoje lasery, i można go skonfigurować tak, aby odpowiadał Twojej własnej konfiguracji laserów. Kliknij i przeciągnij, aby obrócić kamerę. Użyj kółka myszy, aby przesuwać się do przodu i do tyłu. Wiele innych opcji znajdziesz w panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Zobacz [3D Visualiser](../setting-up/3d-visualiser.md).

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view służy do konfigurowania zones i masks dla każdego lasera. Zwróć uwagę na duży numer w lewym górnym rogu — dzięki niemu łatwo sprawdzisz, który laser aktualnie edytujesz.

Ten widok przedstawia całe wyjście danego lasera oraz położenie każdej zone w jego obrębie. Domyślnie na jeden laser przypada tylko jedna zone, ale możesz dodać tyle zones, ile jest rozsądnie praktyczne, i wszystkie będą widoczne w tym widoku.

{% hint style="info" %}
**Czym jest zone?**

Zone to obszar w obrębie wyjścia lasera, do którego możesz kierować treść laserową. Jeden laser może mieć więcej niż jedną zone. Najprostszym typem jest _beam zone_, ale dostępne są także _canvas zone_ oraz _DMX zone_. W tym przewodniku skupimy się głównie na beam zones, które zwykle służą do tworzenia atmosferycznych efektów wiązek w powietrzu.
{% endhint %}

Laser do edycji możesz wybrać na jeden z poniższych sposobów:

* używając ponumerowanych przycisków na pasku u góry,
* naciskając klawisz z numerem wybranego lasera _(klawisze 1–9_)\_,
* naciskając klawisz `Tab`, aby przechodzić kolejno od jednego lasera do następnego.

Dodaj nowy laser do konfiguracji, naciskając przycisk _+_. W panelu _Laser Overview_ znajduje się też przycisk _ADD LASER_.

Usuń laser z konfiguracji, naciskając czerwony przycisk ⊖ w panelu _Laser Overview_.

Możesz przybliżać i oddalać widok kółkiem myszy, a także kliknąć i przeciągnąć w dowolnym miejscu, w którym nie ma zone, aby przesunąć widok.

Kliknij zone, aby ją zaznaczyć, a następnie dostosuj jej punkty narożne myszą. Przytrzymaj klawisz `Alt / Option` podczas przeciągania narożnika, aby zmieniać go niezależnie. Kliknij zone prawym przyciskiem myszy, aby zobaczyć więcej opcji, w tym zmianę typu zone.

Po lewej stronie znajduje się pasek z serią przycisków ikon. Najedź na dowolny przycisk, aby zobaczyć opis jego działania. Przyciski te pozwalają dodawać beam zones, canvas zones oraz masks. Znajdziesz tu też opcje ustawienia test pattern tylko dla tego lasera oraz ustawienia siatki i przyciągania.

Więcej informacji znajdziesz w sekcji [Widok Output](../output-view/).

#### Canvas

System Canvas jest używany głównie do grafiki i mapowania architektonicznego. Możesz rozkładać złożone obrazy na wiele laserów i korygować perspektywę każdej sekcji. Zobacz [Grafika i system Canvas](../graphics-and-the-canvas-system/).

### APC40 MIDI controller

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Choć Liberation można obsługiwać myszą i klawiaturą, znacznie wygodniej jest używać interfejsu sterującego APC40 MIDI. Najlepszy jest Mark 2, ale Mark 1 również działa.

Zobacz też: [Referencja APC40](../reference/apc40-reference.md)

Wprowadziliśmy też obsługę APC Mini Mark 2 oraz MIDI Fighter Twister, a kolejne urządzenia są w przygotowaniu. Jednak APC40 Mark 2 jest najlepszym wyborem w większości zastosowań.&#x20;

### Clips i efekty

{% hint style="info" %}
**Czym jest Clip?**

Clip to kontener na dowolną treść laserową w Liberation. Clips mogą zawierać wiązki albo animacje graficzne i zwykle działają jako zapętlony cykl. Można je kierować do dowolnej zone albo _Canvas target area_ i uruchamiać za pomocą przycisków Clip w Clip Deck.
{% endhint %}

#### Omówienie Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ta siatka nazywa się _Clip Deck_ i przechowuje wszystkie laserowe Clips. Została zaprojektowana tak, aby bezpośrednio odpowiadać siatce przycisków 8 x 5 na APC40.

**Poruszanie się po Clip Deck.**

Clip Deck możesz przewijać w lewo i w prawo za pomocą:

* klawiszy strzałek w lewo i w prawo. Dodaj `Cmd / Ctrl`, aby przewijać o całą stronę naraz;
* gładzika: przeciągnięcie palcem;
* myszy: jeśli mysz obsługuje przewijanie poziome, możesz użyć go po najechaniu kursorem na Clip Deck;
* pokrętła przewijania APC40;
* przycisków APC40 _<- DEVICE ->_.

Aby ułatwić orientację, u góry znajduje się miniwizualizator Clip Deck. Zobacz też [Clipy i Clip Deck](../clips/).

#### Uruchamianie i zatrzymywanie Clips

Naciśnij przycisk Clip — myszą albo na APC40 — aby uruchomić Clip. Naciśnij go ponownie, aby zatrzymać. Gdy uruchomisz Clip, wszystkie inne Clips tego samego koloru automatycznie się zatrzymają, chyba że przytrzymasz _shift_.

Niektóre Clips działają w trybie _Flash mode_ (domyślnie czerwone). W takim przypadku zatrzymają się natychmiast po zwolnieniu przycisku Clip.

Przycisk _STOP_ zatrzymuje wszystkie aktualnie uruchomione Clips.

#### Ustawianie output zones dla Clip

Pod przyciskami Clip zobaczysz przyciski zone — domyślnie beam zones od 1 do 8 (_BEAM 1_, _BEAM 2_ itd.). Przyciski zone świecą, aby wskazać, które zones są przypisane do aktualnie zaznaczonego Clip.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dwa rzędy pod przyciskami zone znajdują się przyciski odwrócenia X/Y. Przełączaj je, aby odbić Clip poziomo i pionowo.

{% hint style="info" %}
Pamiętaj, że te przypisania zone oraz ustawienia odwrócenia X/Y są powiązane z samym Clip. Zostaną zachowane przy następnym uruchomieniu tego Clip. Nie są to ustawienia globalne.
{% endhint %}

Kliknij Clip prawym przyciskiem myszy, aby edytować więcej jego ustawień. Zobacz też [Ustawienia Clip](../clips/clip-settings.md).

### Grupy

Zauważysz, że każdy Clip ma kolorową ramkę. Ten kolor wskazuje, do której _grupy_ należy. Przyciski Clip na APC40 również świecą w tym kolorze.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Grupa 1</td><td>Cyjanowy</td></tr><tr><td>Grupa 2</td><td>Pomarańczowy</td></tr><tr><td>Grupa 3</td><td>Czerwony</td></tr><tr><td>Grupa 4</td><td>Indygo</td></tr><tr><td>Grupa 5</td><td>Zielony</td></tr></tbody></table>

System grup jest bardzo elastyczny i pozwala:

* pozostawić Clips z jednej grupy uruchomione podczas przełączania Clips w innej grupie,
* szybko przypisywać zones i odwrócenia X/Y do wszystkich Clips w grupie,
* ustawić _Flash mode_ dla Clip (Grupa 3 ma domyślnie włączony _Flash mode_).

Grupy mają też ustawienia przejścia wejścia/wyjścia, które mogą być dziedziczone przez należące do nich Clips albo nadpisywane.

Grupę dla Clip możesz przypisać przyciskami w menu wywoływanym prawym przyciskiem myszy. Na APC40 możesz nacisnąć przycisk grupy i _trzymając go wciśnięty_, naciskać przyciski Clip.

Zmienianie ustawień zone dla wszystkich Clips w grupie

Na APC40 naciśnij przycisk grupy, a następnie _trzymając go wciśnięty_, użyj przycisków zone i X/Y, aby przełączyć ustawienia zone dla wszystkich Clips w tej grupie.

Zobacz też [Grupy klipów](../clips/groups.md).

### Efekty

System efektów w Liberation to mocny i elastyczny sposób zmieniania wyjścia Clip w czasie rzeczywistym. Domyślne przyciski efektów 1–8 znajdują się pod przyciskami zone.

#### Stosowanie efektu

Naciśnij przycisk efektu, aby go przełączyć. Jeszcze lepiej: użyj suwaków 1–8 na APC40, aby płynnie wprowadzać i wycofywać efekty.

#### Parametry efektu

Użyj pokręteł 1–8\*, aby dostosować _parameter_ każdego efektu. Możesz też kliknąć prawym przyciskiem myszy, aby dostosować level i parameter. Zmiana parameter działa różnie w zależności od konfiguracji efektu. Lista poniżej opisuje efekty domyślne.

{% hint style="info" %}
Małe liczby widoczne na przyciskach efektów odnoszą się do _level_ i _parameter_ efektu. _Level_ jest kontrolowany faderem na APC40; możesz też kliknąć i przeciągnąć na przycisku. Parameter reguluje się pokrętłami na APC40 albo prawym przyciskiem myszy.
{% endhint %}

_\*Pokrętła 1–8 znajdują się u góry APC40 Mk2 oraz w prawym górnym obszarze Mk1. Zobacz też:_ [Referencja APC40](../reference/apc40-reference.md)

#### Domyślne efekty

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser**:\
   Dodaje chaotyczny ruch do wyjścia Clip. Parameter reguluje ilość/szybkość chaosu.
2. **Sine wave**:\
   Odkształca całą treść wzdłuż poruszającej się fali sinusoidalnej. Parameter reguluje długość fali.
3. **Rotation**:\
   Obraca wszystko wokół środka. Parameter reguluje prędkość obrotu.
4. **Horizontal flip**:\
   Ściska i rozciąga wszystko poziomo. Parameter reguluje szybkość.
5. **Scale**:\
   Wielokrotnie skaluje wszystko od pełnego rozmiaru do zera. Parameter reguluje szybkość.
6. **Hue**:\
   Zmienia odcień wszystkiego, ale nie zmienia nasycenia, czyli wszystko, co białe, pozostaje białe. Parameter reguluje odcień.
7. **Saturation and hue**:\
   Zmienia odcień wszystkiego i dodatkowo w pełni nasyca kolor, czyli wszystko, co białe, zmienia się na dany kolor. Parameter reguluje odcień.
8. **Flash**:\
   Wielokrotnie miga jasnością wszystkiego od pełnej wartości do zera. Parameter reguluje szybkość migania.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

W dolnym rzędzie znajduje się kolejnych 16 efektów kolorystycznych, które stosują gotowe wartości odcienia i nasycenia.

Pamiętaj, że są to efekty domyślne, ale można je edytować tak, aby robiły niemal wszystko, czego potrzebujesz.

#### Czym jest _aktualnie zaznaczony Clip_?

Gdy uruchomisz Clip, zostanie on podświetlony, aby wskazać, że jest aktywny. Ma też białą ramkę, która oznacza, że jest to aktualnie _zaznaczony_ Clip. Gdy przełączasz przyciski zone albo dostosowujesz ustawienia Clip, zmiany są stosowane do _aktualnie zaznaczonego Clip_.

{% hint style="info" %}
Aby zaznaczyć Clip bez jego uruchamiania, naciśnij klawisz `Alt / Option` przed naciśnięciem przycisku Clip. To dobry sposób na dostosowanie jego zones i innych ustawień bez uruchamiania.
{% endhint %}

### Panel Clip Settings

Użyj panelu _Clip Settings_, aby edytować skalowanie, pozycję X/Y oraz uzyskać dostęp do zaawansowanego systemu opóźnień zone.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

W panelu _Global Settings_ możesz dostosować globalne ustawienia wyjścia, które wpływają na całość output we wszystkich zones.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Włącz AUTO RESET, aby automatycznie resetować wszystkie _Global settings_, gdy nie jest odtwarzany żaden Clip.&#x20;

### Timing

Prawie wszystkie pokazy laserowe mają jakąś ścieżkę muzyczną, dlatego system timing w Liberation opiera się na tempie w uderzeniach na minutę. W _Tempo Panel_ możesz zobaczyć reprezentację czasu: każdy kwadrat oznacza jedno uderzenie i miga w rytmie.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Dostępnych jest wiele opcji synchronizacji, w tym MIDI clock i Ableton Link. Jeśli znasz tempo muzyki, możesz ustawić je ręcznie suwakiem na ekranie albo pokrętłem APC40 Tempo. Możesz też utrzymywać tempo zgodnie z muzyką za pomocą systemu _Tap Tempo_\_.

#### Tap Tempo

_Tap Tempo_ to termin często używany w aplikacjach muzycznych. Pozwala wystukiwać rytm w czasie odtwarzania muzyki, aby ustawić tempo. Możesz użyć przycisku na ekranie, ale zalecane jest użycie klawisza _T_ albo przycisku _Tap Tempo_ na APC40. Jeśli wolisz, możesz użyć nawet przełącznika nożnego.

Naciśnij klawisz _R_ albo przycisk _Metronome_ na APC40, aby zresetować tempo do początku taktu.

Naciśnij klawisz _Y_ albo obróć pokrętło _Tempo_ na APC40, aby zaokrąglić tempo do liczby całkowitej. Może to być przydatne w muzyce elektronicznej, która zwykle ma całkowitą liczbę uderzeń na minutę.

### Organizowanie Clip Deck

Aby przenieść Clip w Clip Deck, kliknij go i przeciągnij w nowe miejsce. Podczas przeciągania możesz używać klawiszy kursora albo kółka/przycisków przewijania na APC40, aby przewijać w lewo i w prawo.

Przytrzymaj klawisz `Alt / Option` podczas przeciągania, aby utworzyć kopię.

Kliknij Clip z wciśniętym `Alt / Option`, aby zaznaczyć go bez uruchamiania.

Kliknij Clip z wciśniętym `Alt / Option + Shift`, aby zaznaczyć wiele elementów, albo kliknij i przeciągnij poza Clip, aby zaznaczyć obszarowo metodą „lasso”.&#x20;

Kliknięcie i przeciągnięcie przeciągnie WSZYSTKIE zaznaczone Clips.

Aby usunąć jeden lub więcej Clips, przeciągnij je poza Clip Deck — pojawi się ikona kosza — albo użyj przycisku DELETE z menu Clip wywoływanego prawym przyciskiem myszy.

### Panel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ daje szybki wgląd w stan aktualnie działających laserów. Zielony kwadrat po prawej oznacza, że laser controller działa prawidłowo. Jeśli zmieni kolor na pomarańczowy, występują sporadyczne przerwy. Jeśli jest czerwony, połączenie zostało zerwane. Jeśli jest szary, laser nie jest w ogóle połączony z controller.&#x20;

Wykres pośrodku pokazuje historię długości klatek, a liczba po prawej to bieżąca liczba klatek na sekundę. Im bardziej złożona treść, tym niższa będzie liczba klatek, czyli efekt będzie bardziej migotliwy. Wszystko poniżej około 25 fps zacznie wyglądać dość migotliwie.&#x20;

### Łączenie z laserami — panel Controller Assignment

Kliknij przycisk _Assign Laser Controllers_, aby otworzyć panel _Controller Assignment_. Ten panel jest też dostępny z paska menu przez _View -> Controller Assignment_.

Tutaj możesz wybrać, które wyjścia laserowe trafiają do których laser controllers. Przeciągaj controllers z listy po prawej do slotów po lewej. Możesz zmienić nazwy controllers tak, aby odpowiadały laserom, z którymi są sparowane — użyj przycisku z ikoną pióra.

Więcej informacji znajdziesz w rozdziale [Przypisywanie kontrolerów](../setting-up/controller-assignment.md).

{% hint style="danger" %}
Zanim ustawisz jakikolwiek laser w stan armed, przejdź przez rozdział [Konfigurowanie laserów](../setting-up/setting-up-lasers.md).
{% endhint %}

### Panel Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ten panel pokazuje ustawienia dla _currently selected laser_, czyli lasera wskazanego numerem u góry. Aktualnie wybrany laser możesz zmienić klawiszem _tab_, naciskając klawisz numeryczny, klikając numer lasera w panelu _Laser Overview_ albo w _Output view_.

* **Number button** przełącza laser między stanami armed i disarmed. Jeśli jest czerwony, laser jest w stanie armed.
* **Brightness** reguluje jasność lasera niezależnie od pozostałych laserów. Jest łączona z ustawieniem _global brightness_, czyli jeśli oba ustawienia są na 50%, laser będzie pracował z jasnością 25%.
* **Test Pattern** włącza test pattern tylko dla tego lasera i nadpisuje globalne ustawienie test pattern.
* **Orientation** koryguje lasery zamontowane bokiem albo do góry nogami.
* **Flip Horizontal and Flip Vertical** odwraca wyjście lasera. Przydatne do korekcji wyjścia w laserach z niespójnym okablowaniem.
* **Copy Laser Settings** otwiera panel, który pozwala kopiować różne ustawienia z tego lasera do innych.

### Ustawienia skanerów

Lasery pokazowe działają przez bardzo szybkie przesuwanie pojedynczej wiązki laserowej oraz jej włączanie i wyłączanie, aby rysować kształty w powietrzu. To, co widzisz jako linie, kształty i obrazy, jest w rzeczywistości ścieżką wiązki rysowaną szybciej, niż oko jest w stanie śledzić.

Strumień punktów to dane, które informują laser, dokąd ma przesunąć się następnie oraz kiedy wiązka ma być włączona albo wyłączona. W Liberation Clips są przekształcane w taki strumień punktów w czasie rzeczywistym, gdy są wysyłane do laserów.

Liberation daje szczegółową kontrolę nad sposobem generowania tego strumienia punktów, dzięki czemu możesz wyważyć płynność, jasność i wydajność dla każdego lasera.

{% hint style="info" %}
Jeśli korzystasz ze starszego oprogramowania laserowego, które opiera się na wcześniej obliczonych strumieniach punktów, to podejście może początkowo wydawać się inne. Generowanie punktów w czasie rzeczywistym pozwala jednak optymalizować tę samą treść inaczej dla każdego lasera. Ułatwia to pracę z wieloma laserami o różnych prędkościach lub jakości skanerów, bez duplikowania ani przebudowywania treści. Dzięki temu pliki Clip pozostają też bardzo małe — dlatego cały domyślny Clip Deck w Liberation zajmuje tylko kilka megabajtów, a nie gigabajty.
{% endhint %}

Podstawowe ustawienia skanerów to:

* **Speed** to prędkość skanera, czyli szybkość, z jaką laser porusza się, aby rysować kształty. Odpowiada to regulacji point rate w tradycyjnym oprogramowaniu laserowym, ale w Liberation możesz zmieniać szybkość ruchu lasera _niezależnie od point rate_. Zwykle nie ma potrzeby zmieniać tego ustawienia.
* **Scanner sync** (czasem znane jako _blank shift_, wcześniej Colour Shift) Skanery poruszają laserem bardzo szybko, ale zwykle zmiany jasności i koloru nie są zsynchronizowane z ruchem. Objawia się to małymi, migotliwymi „ogonami” światła na krawędziach wiązek i linii. Użyj tej regulacji, aby zsynchronizować ruch i kolor. Zobacz [Laser Settings](../setting-up/laser-settings/)

Pozostałe zaawansowane ustawienia skanerów omówiono w rozdziale [Zaawansowane](../advanced/).

### Zoning

Pełny przewodnik po konfiguracji laserów i zoning znajdziesz tutaj: [Konfigurowanie laserów](../setting-up/setting-up-lasers.md)
