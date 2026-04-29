---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Szybki start

## Wprowadzenie

Witamy w **Liberation** — nowej generacji oprogramowania do pokazów laserowych.

Liberation to rozbudowane i zaawansowane nowoczesne oprogramowanie. Zostało oparte na zasadach użyteczności i niezawodności, aby dać Ci swobodę twórczej pracy. Jest szybkie, wydajne i płynne w obsłudze. Skorzystaj z tego _Szybkiego startu_, aby błyskawicznie rozpocząć pracę!

### Zarządzanie laserami

Liberation jest na tyle elastyczne, że możesz konfigurować i wizualizować lasery nawet bez podłączonych fizycznych laserów. Gdy wszystko będzie gotowe, możesz płynnie przypisać każde wyjście do kontrolera lasera.

{% hint style="info" %}
W Liberation możesz skonfigurować i wizualizować dowolną liczbę laserów. Poziomy licencji (Hobbyist, Pro itd.) ograniczają tylko liczbę laserów, które możesz _uzbroić_. Oznacza to, że nawet z darmową licencją możesz projektować pokazy laserowe ze 100 laserami. Rozszerzenie licencji jest potrzebne dopiero wtedy, gdy chcesz uruchomić pokaz na rzeczywistych laserach.
{% endhint %}

Domyślnie projekt zawiera 8 laserów rozmieszczonych poziomo, ale możesz dostosować to ustawienie do własnych potrzeb. Na początek najlepiej zostawić konfigurację domyślną, dopóki poznajesz program, a później dopasować ją do swojego sprzętu. (Zobacz [Konfigurowanie projektu](setting-up/setting-up-your-project.md))

{% hint style="warning" %}
Ważne: zanim uzbroisz jakiekolwiek lasery, upewnij się, że rozumiesz związane z tym ryzyka i dokładnie przejdź przez rozdział [Przegląd procesu konfiguracji laserów](setting-up/setting-up-lasers.md).
{% endhint %}

## Omówienie programu

### Awaryjne wyłączenie

Podczas pracy z laserami zawsze musisz mieć pod ręką **sprzętowy przycisk awaryjnego zatrzymania** (zobacz [Zatrzymanie awaryjne / blokady bezpieczeństwa](hardware/emergency-stop-interlocks.md)). Jeśli jednak chcesz rozbroić wszystko w mniej pilnym trybie, możesz użyć przycisku _**DISARM ALL**_, klawisza `Escape` albo klawisza _**SESSION**_ na APC40. Możesz też zmniejszyć jasność globalną suwakiem na ekranie lub głównym faderem na APC40.

### Suwaki

W Liberation znajdziesz różne suwaki i elementy sterujące.

{% hint style="info" %}
Kliknij suwak z przytrzymanym `Cmd / Ctrl`, aby wpisać nową wartość, jeśli potrzebujesz większej precyzji niż pozwala na to sam suwak.
{% endhint %}

### Skróty klawiaturowe

Pełną listę skrótów klawiaturowych znajdziesz tutaj: [Skróty klawiaturowe](reference/keyboard-shortcuts.md)

### Układ ekranu

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nie wiesz, do czego służy dany przycisk? Najedź na niego kursorem myszy, aby zobaczyć opis!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

W menu znajdziesz wszystkie opcje importu i eksportu plików oraz możliwość otwierania paneli. Tutaj znajduje się też opcja autoryzacji komputera w ramach subskrypcji (_Liberation -> Authorise/Deauthorise this computer_).

#### Pasek ikon

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Tutaj znajdują się często używane funkcje, takie jak uzbrajanie i rozbrajanie wszystkich laserów, jasność globalna, wzorzec testowy oraz przełączanie między widokami 3D, Canvas i Output.

### Widoki

Duży obszar w lewym górnym rogu ekranu może pokazywać jeden z 3 głównych widoków: **3D**, **CANVAS** oraz **OUTPUT.** Przełączasz je przyciskami na pasku ikon (albo klawiszem `Tab`, aby przełączać się między widokami 3D i OUTPUT, a następnie kolejno przechodzić przez wyjścia poszczególnych laserów).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Widok 3D

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

Widok 3D pokazuje, jak będą wyglądać Twoje lasery, i można go skonfigurować tak, aby odpowiadał Twojemu rzeczywistemu zestawowi. Kliknij i przeciągnij, aby obracać kamerę, a kółkiem myszy przesuwaj się do przodu i do tyłu. Wiele dodatkowych opcji znajdziesz w panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Zobacz [3D Visualiser](setting-up/3d-visualiser.md).

#### Widok Output

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Widok Output służy do konfigurowania stref i masek dla każdego lasera. (Zwróć uwagę na duży numer w lewym górnym rogu — dzięki niemu łatwo sprawdzisz, który laser aktualnie edytujesz!)

Ten widok przedstawia całe wyjście danego lasera oraz położenie każdej strefy w jego obrębie. Domyślnie na każdy laser przypada tylko jedna strefa, ale możesz dodać tyle stref, ile ma praktyczny sens, i zobaczysz je wszystkie w tym widoku.

{% hint style="info" %}
**Czym jest strefa?**

Strefa to obszar w wyjściu lasera, do którego możesz kierować treści laserowe. Jeden laser może mieć więcej niż jedną strefę. Najprostszym typem strefy jest strefa _beam_, ale dostępne są też strefy _canvas_ i _DMX_. W tym przewodniku skupimy się głównie na strefach beam, które zwykle służą do tworzenia atmosferycznych efektów wiązek w powietrzu.
{% endhint %}

Laser do edycji możesz wybrać na jeden z tych sposobów:

* przyciski z numerami na pasku u góry
* naciśnięcie klawisza numeru wybranego lasera _(klawisze 1–9)_
* klawisz `Tab`, aby przechodzić kolejno od jednego lasera do następnego

Dodaj nowy laser do konfiguracji, naciskając przycisk _+_. (W panelu _Laser Overview_ znajduje się też przycisk _ADD LASER_)

Usuń laser z konfiguracji, naciskając czerwony przycisk ⊖ w panelu _Laser Overview_.

Możesz powiększać i pomniejszać widok kółkiem myszy, a także kliknąć i przeciągnąć w dowolnym miejscu, w którym nie ma strefy, aby przesunąć widok.

Kliknij strefę, aby ją zaznaczyć, a następnie dostosuj jej punkty narożne myszą. Przytrzymaj klawisz `Alt / Option` podczas przeciągania narożnika, aby zmieniać go nierównomiernie. Kliknij strefę prawym przyciskiem myszy, aby zobaczyć więcej opcji, w tym zmianę typu strefy.

Po lewej stronie znajduje się pasek z ikonami. Najedź na dowolny przycisk, aby zobaczyć opis jego działania. Przyciski na tym pasku pozwalają dodawać strefy beam, strefy canvas i maski. Są tu też opcje ustawienia wzorca testowego tylko dla tego lasera oraz ustawienia siatki i przyciągania.

Więcej informacji znajdziesz w [Widok Output](output-view/).

#### Canvas

System Canvas jest używany głównie do grafiki i mapowania architektonicznego. Możesz rozdzielać złożone obrazy na wiele laserów i korygować perspektywę każdej sekcji. Zobacz [Grafika i system Canvas](graphics-and-the-canvas-system/).

### Kontroler MIDI APC40

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Chociaż Liberation można obsługiwać myszą i klawiaturą, znacznie wygodniej jest używać interfejsu sterującego MIDI APC40 (najlepszy jest Mark 2, ale Mark 1 również działa).

Zobacz też: [Referencja APC40](reference/apc40-reference.md)

Dodaliśmy również obsługę APC Mini Mark 2 oraz MIDI Fighter Twister, a kolejne kontrolery są w przygotowaniu. W większości przypadków APC40 Mark 2 pozostaje jednak najlepszym wyborem.

### Klipy i efekty

{% hint style="info" %}
**Czym jest klip?**

Klip to kontener na dowolną zawartość laserową w Liberation. Klipy mogą zawierać wiązki lub animacje graficzne i zwykle działają jako zapętlony cykl. Można je kierować do dowolnej strefy (lub _Canvas target area_) i uruchamiać przyciskami klipów w Clip Deck.
{% endhint %}

#### Omówienie Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ta siatka to _clip deck_ — miejsce, w którym przechowywane są wszystkie klipy laserowe. Została zaprojektowana tak, aby bezpośrednio odpowiadać siatce przycisków 8 x 5 na APC40.

**Nawigacja po clip deck.**

Clip deck możesz przewijać w lewo i w prawo za pomocą:

* klawiszy strzałek w lewo i w prawo. Dodaj `Cmd / Ctrl`, aby przewijać o całą stronę naraz.
* gładzika: przesuń palcem
* myszy: jeśli Twoja mysz obsługuje przewijanie w bok, możesz używać go po najechaniu kursorem na clip deck
* pokrętła przewijania APC40
* przycisków APC40 _<- DEVICE ->_

Aby ułatwić orientację, u góry znajduje się miniwizualizator clip deck. Zobacz też [Clipy i Clip Deck](clips/)

#### Uruchamianie i zatrzymywanie klipów

Naciśnij przycisk klipu (myszą albo na APC40), aby go uruchomić. Naciśnij go ponownie, aby zatrzymać klip. Po uruchomieniu klipu wszystkie inne klipy w tym samym kolorze automatycznie się zatrzymają, chyba że przytrzymasz _shift_.

Niektóre klipy działają w _Flash mode_ (domyślnie są to czerwone klipy). W takim przypadku zatrzymają się natychmiast po zwolnieniu przycisku klipu.

Przycisk _STOP_ zatrzymuje wszystkie aktualnie uruchomione klipy.

#### Ustawianie stref wyjściowych dla klipu

Pod przyciskami klipów zobaczysz przyciski stref, domyślnie strefy beam od 1 do 8 (_BEAM 1_, _BEAM 2_ itd.). Przyciski stref świecą, wskazując, które strefy są przypisane do aktualnie zaznaczonego klipu.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dwa rzędy pod przyciskami stref znajdują się przyciski odwrócenia X/Y. Przełączaj je, aby odwrócić klip w poziomie i w pionie.

{% hint style="info" %}
Pamiętaj, że te przypisania stref oraz ustawienia odwrócenia X/Y są powiązane z samym klipem. Zostaną zachowane przy następnym uruchomieniu tego klipu. Nie są to ustawienia globalne.
{% endhint %}

Kliknij klip prawym przyciskiem myszy, aby edytować więcej jego ustawień. Zobacz też [Ustawienia Clip](clips/clip-settings.md)

### Grupy

Zauważysz, że każdy klip ma kolorowy obrys, a ten kolor wskazuje, do której _grupy_ należy. Przyciski klipów APC40 również świecą w tym kolorze.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyjan</td></tr><tr><td>Group 2</td><td>Pomarańczowy</td></tr><tr><td>Group 3</td><td>Czerwony</td></tr><tr><td>Group 4</td><td>Indygo</td></tr><tr><td>Group 5</td><td>Zielony</td></tr></tbody></table>

System grup jest bardzo elastyczny i pozwala:

* utrzymać działanie klipów w jednej grupie, podczas gdy przełączasz grupy w innej
* szybko przypisywać strefy i odwrócenia X/Y do wszystkich klipów w grupie
* ustawić _Flash mode_ dla klipu (Group 3 domyślnie działa w _Flash mode_)

Grupy mają też ustawienia przejść wejścia/wyjścia, które mogą być dziedziczone przez ich klipy albo nadpisywane.

Grupę klipu możesz przypisać przyciskami w menu po kliknięciu prawym przyciskiem myszy. Na APC40 możesz też nacisnąć przycisk grupy i _trzymając go wciśnięty_, naciskać przyciski klipów.

Zmiana ustawień stref dla wszystkich klipów w grupie

Na APC40 naciśnij przycisk grupy, a następnie _trzymając go wciśnięty_, użyj przycisków stref oraz X/Y, aby przełączać ustawienia stref dla wszystkich klipów w tej grupie.

Zobacz też [Grupy klipów](clips/groups.md)

### Efekty

System efektów w Liberation to mocny i wszechstronny sposób zmieniania wyjścia klipu w czasie rzeczywistym. Domyślne przyciski efektów 1–8 znajdują się pod przyciskami stref.

#### Stosowanie efektu

Naciśnij przycisk efektu, aby włączyć lub wyłączyć efekt, a jeszcze lepiej użyj suwaków APC40 1–8, aby płynnie wprowadzać i wyprowadzać efekty.

#### Parametry efektów

Użyj kontrolerów obrotowych 1–8\*, aby dostosować _parametr_ każdego efektu. (Możesz też kliknąć prawym przyciskiem myszy, aby dostosować poziom i parametr). Zmiana parametru działa różnie w zależności od konfiguracji efektu. Poniżej znajdziesz listę efektów domyślnych.

{% hint style="info" %}
Małe liczby widoczne na przyciskach efektów odnoszą się do _level_ i _parameter_ efektu. _level_ jest sterowany faderem na APC40 albo przez kliknięcie i przeciągnięcie na przycisku. Parametr jest regulowany pokrętłami na APC40 albo prawym przyciskiem myszy.
{% endhint %}

_\*Kontrolery obrotowe 1–8 znajdują się u góry APC40 Mk2 oraz w prawym górnym rogu APC40 Mk1. Zobacz też:_ [Referencja APC40](reference/apc40-reference.md)

#### Domyślne efekty

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Dodaje chaotyczny ruch do wyjścia klipu. Parametr reguluje ilość/szybkość chaosu.
2. **Sine wave** :\
   Zniekształca całą zawartość wzdłuż poruszającej się fali sinusoidalnej. Parametr reguluje długość fali.
3. **Rotation** :\
   Obraca wszystko dookoła. Parametr reguluje prędkość obrotu.
4. **Horizontal flip** :\
   Ściska i rozciąga wszystko w poziomie. Parametr reguluje prędkość.
5. **Scale** :\
   Wielokrotnie skaluje wszystko od pełnego rozmiaru do zera. Parametr reguluje prędkość.
6. **Hue** :\
   Zmienia odcień wszystkiego, ale nie zmienia nasycenia (tzn. wszystko, co białe, pozostaje białe). Parametr reguluje odcień.
7. **Saturation and hue** :\
   Zmienia odcień wszystkiego i jednocześnie w pełni nasyca kolor (tzn. wszystko, co białe, zmienia się na dany kolor). Parametr reguluje odcień.
8. **Flash** :\
   Wielokrotnie miga jasnością wszystkiego od pełnej wartości do zera. Parametr reguluje szybkość migania.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

W dolnym rzędzie znajduje się kolejnych 16 efektów kolorystycznych, które stosują gotowe wartości odcienia i nasycenia.

Pamiętaj, że są to efekty domyślne, ale można je edytować tak, aby robiły niemal wszystko, czego potrzebujesz!

#### Czym jest _„aktualnie zaznaczony klip”_?

Gdy uruchomisz klip, podświetla się on, aby pokazać, że jest aktywny. Ma też biały obrys, który wskazuje, że jest to aktualnie _zaznaczony_ klip. Gdy przełączasz przyciski stref lub zmieniasz ustawienia klipu, zmiany są stosowane do _aktualnie zaznaczonego klipu._

{% hint style="info" %}
Aby zaznaczyć klip bez jego uruchamiania, naciśnij klawisz `Alt / Option` przed naciśnięciem przycisku klipu. To dobry sposób na dostosowanie stref i innych ustawień bez uruchamiania klipu.
{% endhint %}

### Panel Clip Settings

Użyj panelu _Clip Settings_, aby edytować skalowanie, pozycję X/Y oraz uzyskać dostęp do zaawansowanego systemu opóźnień stref.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

W panelu _Global Settings_ możesz dostosować globalne ustawienia wyjścia, które wpływają na całe wyjście we wszystkich strefach.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Włącz AUTO RESET, aby automatycznie resetować wszystkie _Global settings_, gdy nie jest odtwarzany żaden klip.

### Timing

Prawie wszystkie pokazy laserowe mają jakąś ścieżkę muzyczną, dlatego system czasu w Liberation opiera się na tempie w uderzeniach na minutę. W panelu _Tempo Panel_ zobaczysz reprezentację czasu: każdy kwadrat oznacza jedno uderzenie i miga w rytmie.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Dostępnych jest wiele opcji synchronizacji, w tym MIDI clock i Ableton Link. Jeśli znasz tempo muzyki, możesz ręcznie ustawić je suwakiem na ekranie lub pokrętłem APC40 Tempo, ale możesz też utrzymywać synchronizację z muzyką za pomocą systemu _Tap Tempo_\_ .\_

#### Tap Tempo

_Tap Tempo_ to termin często używany w aplikacjach muzycznych. Pozwala wystukiwać rytm w trakcie odtwarzania muzyki, aby ustawić tempo. Możesz użyć przycisku na ekranie, ale zalecamy używanie klawisza _T_ albo przycisku _Tap Tempo_ na APC40 (lub nawet przełącznika nożnego, jeśli wolisz).

Naciśnij klawisz _R_ albo przycisk _Metronome_ (APC40), aby zresetować tempo do początku taktu.

Naciśnij klawisz _Y_ albo obróć pokrętło _Tempo_ (APC40), aby zaokrąglić tempo do liczby całkowitej. Może to być przydatne w muzyce elektronicznej, która zwykle ma pełną liczbę uderzeń na minutę.

### Organizacja clip deck

Aby przenieść klip w clip deck, kliknij go i przeciągnij w nowe miejsce. Podczas przeciągania możesz używać klawiszy kursora (albo kółka/przycisków przewijania na APC40), aby przewijać w lewo i w prawo.

Przytrzymaj klawisz `Alt / Option` podczas przeciągania, aby utworzyć kopię.

Kliknij klip z przytrzymanym `Alt / Option`, aby zaznaczyć go bez uruchamiania.

Kliknij klip z przytrzymanym `Alt / Option + Shift`, aby zaznaczyć wiele elementów, albo kliknij i przeciągnij poza klipem, aby zaznaczyć obszar „lasso”.

Kliknięcie i przeciągnięcie przeciągnie WSZYSTKIE zaznaczone klipy.

Aby usunąć jeden lub więcej klipów, przeciągnij je poza clip deck (pojawi się ikona kosza) albo użyj przycisku DELETE z menu klipu dostępnego po kliknięciu prawym przyciskiem myszy.

### Panel Laser Overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser overview panel_ daje szybki podgląd stanu aktualnie działających laserów. Zielony kwadrat po prawej oznacza, że kontroler lasera działa prawidłowo. Jeśli zmieni się na pomarańczowy, występują sporadyczne przerwy, a jeśli na czerwony — kontroler się rozłączył. Jeśli jest szary, laser nie jest w ogóle podłączony do kontrolera.

Wykres pośrodku pokazuje historię długości klatek, a liczba po prawej to bieżąca liczba klatek na sekundę. Im bardziej złożona zawartość, tym niższa liczba klatek (czyli bardziej widoczne migotanie). Wartości poniżej około 25 fps zaczną wyglądać dość migotliwie.

### Łączenie z laserami — panel Controller Assignment

Kliknij przycisk _Assign Laser Controllers_, aby otworzyć panel _Controller Assignment_. (Dostęp do tego panelu można też uzyskać z paska menu przez _View -> Controller Assignment_).

Tutaj możesz wybrać, które wyjścia laserowe trafiają do których kontrolerów laserów. Przeciągaj kontrolery z listy po prawej do slotów po lewej. Możesz zmienić nazwy kontrolerów tak, aby odpowiadały laserom, z którymi są sparowane (użyj przycisku z ikoną ołówka).

Więcej informacji znajdziesz w rozdziale [Przypisywanie kontrolerów](setting-up/controller-assignment.md).

{% hint style="danger" %}
Zanim uzbroisz jakiekolwiek lasery, koniecznie przejdź przez rozdział [Przegląd procesu konfiguracji laserów](setting-up/setting-up-lasers.md).
{% endhint %}

### Panel Laser Output

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ten panel pokazuje ustawienia _aktualnie zaznaczonego lasera_ (wskazanego numerem u góry). Aktualnie zaznaczony laser możesz zmienić klawiszem _tab_, naciskając klawisz z numerem, klikając numer lasera w panelu _Laser Overview_ albo w widoku _output view._

* **Number button** uzbraja i rozbraja laser. Jeśli jest czerwony, laser jest uzbrojony.
* **Brightness** reguluje jasność lasera niezależnie od innych laserów (i łączy się z ustawieniem _global brightness_ — tzn. jeśli oba ustawienia wynoszą 50%, laser będzie działać na 25%).
* **Test Pattern** włącza wzorzec testowy tylko dla tego lasera (nadpisuje globalne ustawienie wzorca testowego)
* **Orientation** koryguje lasery zamontowane bokiem albo do góry nogami.
* **Flip Horizontal and Flip Vertical** odwraca wyjście lasera. Przydatne do korekcji wyjścia w laserach z niespójnym okablowaniem.
* **Copy Laser Settings** otwiera panel, który pozwala kopiować różne ustawienia z tego lasera do innych.

### Ustawienia skanerów

Lasery pokazowe działają przez bardzo szybkie poruszanie pojedynczą wiązką lasera i włączanie oraz wyłączanie jej w celu rysowania kształtów w powietrzu. To, co widzisz jako linie, kształty i obrazy, jest w rzeczywistości wiązką kreślącą ścieżki szybciej, niż Twoje oczy są w stanie śledzić.

Strumień punktów to dane, które mówią laserowi, dokąd ma przesunąć się dalej i kiedy wiązka ma być włączona lub wyłączona. W Liberation klipy są przekształcane w taki strumień punktów w czasie rzeczywistym, gdy są wysyłane do laserów.

Liberation daje szczegółową kontrolę nad generowaniem tego strumienia punktów, pozwalając równoważyć płynność, jasność i wydajność dla każdego lasera.

{% hint style="info" %}
Jeśli korzystasz ze starszego oprogramowania laserowego opartego na wstępnie obliczonych strumieniach punktów, to podejście może początkowo wydawać się inne. Generowanie punktów w czasie rzeczywistym pozwala jednak optymalizować tę samą zawartość inaczej dla każdego lasera. Ułatwia to pracę z wieloma laserami o różnych prędkościach lub jakości skanerów, bez duplikowania ani przebudowywania zawartości. Dzięki temu pliki klipów pozostają bardzo małe — dlatego cały domyślny clip deck Liberation ma tylko kilka megabajtów, a nie gigabajty.
{% endhint %}

Podstawowe ustawienia skanerów to:

* **Speed** to prędkość skanera, czyli szybkość, z jaką laser porusza się, aby rysować kształty. Odpowiada to regulacji point rate w tradycyjnym oprogramowaniu laserowym, ale w Liberation możesz zmieniać prędkość ruchu lasera _niezależnie od point rate._ Zwykle nie trzeba tego regulować.
* **Scanner sync** (czasem nazywane _blank shift, wcześniej Colour Shift_) Skanery poruszają laserem bardzo szybko, ale zwykle zmiana jasności i koloru nie jest zsynchronizowana z ruchem. Objawia się to jako małe migoczące „ogonki” światła na krawędziach wiązek i linii. Użyj tej regulacji, aby zsynchronizować ruch i kolor. Zobacz [Panel ustawień Laser output](setting-up/laser-settings.md)

Pozostałe zaawansowane ustawienia skanerów opisano w rozdziale [Zaawansowane](advanced/).

### Zoning

Pełny przewodnik po konfiguracji i strefowaniu laserów znajdziesz tutaj: [Przegląd procesu konfiguracji laserów](setting-up/setting-up-lasers.md)
