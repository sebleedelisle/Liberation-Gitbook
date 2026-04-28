# ✅ Szybki start

## Wprowadzenie

Witamy w **Liberation** — nowej generacji oprogramowania do pokazów laserowych.

Liberation to rozbudowane, nowoczesne oprogramowanie o dużych możliwościach. Zostało oparte na zasadach wygody użytkowania i niezawodności, aby dać Ci swobodę twórczej pracy. Jest szybkie, wydajne i płynne w obsłudze. Ten _Szybki start_ pomoże Ci błyskawicznie rozpocząć pracę!

### Zarządzanie laserami

Liberation jest na tyle elastyczny, że możesz skonfigurować lasery i wizualizować je nawet bez podłączania fizycznych urządzeń. Gdy będziesz gotowy do pracy, możesz płynnie przypisać każde wyjście do kontrolera lasera.

{% hint style="info" %}
W Liberation możesz skonfigurować i wizualizować dowolną liczbę laserów. Poziomy licencji (Hobbyist, Pro itd.) ograniczają tylko liczbę laserów, które możesz _uzbroić_. Oznacza to, że nawet na darmowej licencji możesz zaprojektować pokaz ze 100 laserami. Aktualizacja licencji będzie potrzebna dopiero wtedy, gdy zechcesz faktycznie uruchomić pokaz na prawdziwych laserach.
{% endhint %}

Domyślnie projekt zawiera 8 laserów rozmieszczonych poziomo, ale możesz dostosować to do własnych potrzeb. Na czas poznawania programu najlepiej pozostawić ustawienia domyślne, a później dopasować je do swojej konfiguracji sprzętowej. (Zobacz [setting-up-your-project.md](../setting-up/setting-up-your-project.md))&#x20;

{% hint style="warning" %}
Ważne: zanim uzbroisz jakikolwiek laser, upewnij się, że rozumiesz związane z tym ryzyko, i dokładnie przejdź przez rozdział [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

## Omówienie programu

### Awaryjne wyłączenie

Podczas pracy z laserami zawsze musisz mieć pod ręką **sprzętowy przycisk awaryjnego zatrzymania** (zobacz [emergency-stop-interlocks.md](../hardware/emergency-stop-interlocks.md)). Jeśli jednak chcesz mniej pilnie rozbroić wszystko naraz, możesz użyć przycisku _**DISARM ALL**_, klawisza `Escape` albo klawisza _**SESSION**_ na APC40. Możesz też zmniejszyć globalną jasność za pomocą suwaka na ekranie lub głównego fadera na APC40.

### Suwaki i elementy sterujące

W Liberation znajdziesz różne suwaki i elementy sterujące.

{% hint style="info" %}
Kliknij suwak z przytrzymanym `Cmd / Ctrl`, aby wpisać nową wartość, jeśli potrzebujesz większej precyzji niż daje sam suwak.
{% endhint %}

### Skróty klawiaturowe

Pełną listę skrótów klawiaturowych znajdziesz tutaj: [keyboard-shortcuts.md](../reference/keyboard-shortcuts.md)

### Układ ekranu

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nie wiesz, do czego służy dany przycisk? Najedź na niego myszą, aby zobaczyć opis!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

W menu znajdziesz wszystkie opcje importu i eksportu plików oraz otwierania paneli. Tutaj znajduje się też opcja autoryzacji komputera w ramach subskrypcji (_Liberation -> Authorise/Deauthorise this computer_).

#### Pasek ikon

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Znajdziesz tutaj często używane funkcje, takie jak uzbrajanie i rozbrajanie wszystkich laserów, globalna jasność, wzór testowy oraz przełączanie między widokami 3D, Canvas i Output.

### Widoki

Duży obszar w lewym górnym rogu ekranu może pokazywać jeden z 3 głównych widoków: **3D**, **CANVAS** i **OUTPUT.** Przełączaj je za pomocą przycisków na pasku ikon albo użyj klawisza `Tab`, aby przełączać się między widokami 3D i OUTPUT, a następnie kolejno przechodzić przez wyjścia poszczególnych laserów.

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### Widok 3D

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

Widok 3D pokazuje, jak będą wyglądały Twoje lasery, i można go skonfigurować tak, aby odpowiadał Twojemu rzeczywistemu ustawieniu. Kliknij i przeciągnij, aby obracać kamerę. Użyj kółka myszy, aby przesuwać się do przodu i do tyłu. Wiele dodatkowych opcji znajdziesz w panelu _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Zobacz [3d-visualiser.md](../setting-up/3d-visualiser.md).

#### Widok Output

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Widok Output służy do konfigurowania stref i masek dla każdego lasera. (Zwróć uwagę na duży numer w lewym górnym rogu — dzięki niemu łatwo sprawdzisz, na którym laserze aktualnie pracujesz!)

Ten widok przedstawia całe wyjście danego lasera oraz położenie każdej strefy w jego obrębie. Domyślnie na każdy laser przypada tylko jedna strefa, ale możesz dodać tyle stref, ile ma praktyczny sens, i wszystkie zobaczysz w tym widoku.

{% hint style="info" %}
**Czym jest strefa?**

Strefa to obszar w obrębie wyjścia lasera, do którego możesz kierować treści laserowe. Jeden laser może mieć więcej niż jedną strefę. Najprostszym typem strefy jest strefa _beam_, ale dostępne są też strefy _canvas_ i _DMX_. W tym przewodniku skupimy się głównie na strefach beam, które zwykle służą do tworzenia przestrzennych efektów wiązek w powietrzu.
{% endhint %}

Laser, który chcesz edytować, możesz wybrać za pomocą:

* numerowanych przycisków na pasku u góry
* naciśnięcia klawisza z numerem lasera _(1-9_ keys\_)\_
* klawisza `Tab`, aby przechodzić kolejno od jednego lasera do następnego

Dodaj nowy laser do konfiguracji, naciskając przycisk _+_. (Przycisk _ADD LASER_ znajduje się także w panelu _Laser Overview_).

Usuń laser z konfiguracji, naciskając czerwony przycisk ⊖ w panelu _Laser Overview_.

Możesz przybliżać i oddalać widok kółkiem myszy, a także kliknąć i przeciągnąć w dowolnym miejscu bez strefy, aby przesunąć widok.

Kliknij strefę, aby ją zaznaczyć, a następnie dostosuj jej punkty narożne myszą. Podczas przeciągania narożnika przytrzymaj klawisz `Alt / Option`, aby zmiana była niesymetryczna. Kliknij strefę prawym przyciskiem myszy, aby zobaczyć więcej opcji, w tym zmianę typu strefy.

Po lewej stronie znajduje się pasek z serią przycisków ikon. Najedź na dowolny przycisk, aby zobaczyć opis jego działania. Przyciski w tym miejscu pozwalają dodawać strefy beam, strefy canvas i maski. Dostępne są też opcje ustawienia wzoru testowego tylko dla tego lasera oraz ustawienia siatki i przyciągania.

Więcej szczegółów znajdziesz w [output-view](../output-view/).

#### Canvas

System Canvas jest używany głównie do grafiki i mapowania architektonicznego. Pozwala rozdzielać złożone obrazy na wiele laserów i korygować perspektywę każdej sekcji. Zobacz [graphics-and-the-canvas-system](../graphics-and-the-canvas-system/).

### Kontroler MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Choć Liberation można obsługiwać myszą i klawiaturą, znacznie wygodniej jest używać interfejsu sterującego MIDI APC40 (najlepiej Mark 2, ale Mark 1 również działa).

Zobacz także: [apc40-reference.md](../reference/apc40-reference.md)

Dodaliśmy też obsługę APC Mini Mark 2 oraz MIDI Fighter Twister, a kolejne kontrolery są w przygotowaniu. W większości przypadków najlepszym wyborem pozostaje jednak APC40 Mark 2.&#x20;

### Klipy i efekty

{% hint style="info" %}
**Czym jest klip?**

Klip to kontener na dowolną treść laserową w Liberation. Klipy mogą zawierać wiązki lub animacje graficzne i zazwyczaj działają w pętli. Można kierować je do dowolnej strefy (albo _Canvas target area_) i uruchamiać przyciskami klipów w clip decku.
{% endhint %}

#### Omówienie clip decku

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Ta siatka nazywa się _clip deck_ i przechowuje wszystkie klipy laserowe. Została zaprojektowana tak, aby bezpośrednio odpowiadała siatce przycisków 8 x 5 na APC40.

**Poruszanie się po clip decku.**

Clip deck możesz przewijać w lewo i w prawo za pomocą:

* klawiszy strzałek w lewo i w prawo. Dodaj `Cmd / Ctrl`, aby przewijać o całą stronę naraz.
* Trackpad: przesuń palcem
* Mysz: jeśli mysz obsługuje przewijanie poziome, możesz go użyć po najechaniu na clip deck
* pokrętła przewijania APC40
* przycisków APC40 _<- DEVICE ->_

Aby ułatwić orientację, u góry znajduje się miniwizualizacja clip decku. Zobacz także [clips](../clips/)

#### Uruchamianie i zatrzymywanie klipów

Naciśnij przycisk klipu (myszą albo na APC40), aby uruchomić klip. Naciśnij go ponownie, aby go zatrzymać. Gdy uruchomisz klip, wszystkie inne klipy tego samego koloru automatycznie się zatrzymają, chyba że przytrzymasz _shift_.

Niektóre klipy działają w _Flash mode_ (domyślnie czerwone). W takim przypadku zatrzymają się natychmiast po puszczeniu przycisku klipu.

Przycisk _STOP_ zatrzymuje wszystkie aktualnie uruchomione klipy.

#### Ustawianie stref wyjściowych dla klipu

Pod przyciskami klipów zobaczysz przyciski stref — domyślnie strefy beam od 1 do 8 (_BEAM 1_, _BEAM 2_ itd.). Przyciski stref podświetlają się, wskazując, które strefy są przypisane do aktualnie wybranego klipu.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Dwa rzędy pod przyciskami stref znajdują się przyciski odwracania X/Y. Włącz je, aby odwrócić klip poziomo i pionowo.

{% hint style="info" %}
Pamiętaj, że te przypisania stref oraz ustawienia odwrócenia X/Y są powiązane z samym klipem. Zostaną zachowane przy następnym uruchomieniu tego klipu. Nie jest to ustawienie globalne.
{% endhint %}

Kliknij klip prawym przyciskiem myszy, aby edytować więcej jego ustawień. Zobacz także [clip-settings.md](../clips/clip-settings.md)

### Grupy

Zauważysz, że każdy klip ma kolorowy obrys, a kolor ten wskazuje, do której _grupy_ należy. Przyciski klipów na APC40 również podświetlają się tym kolorem.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Cyjan</td></tr><tr><td>Group 2</td><td>Pomarańczowy</td></tr><tr><td>Group 3</td><td>Czerwony</td></tr><tr><td>Group 4</td><td>Indygo</td></tr><tr><td>Group 5</td><td>Zielony</td></tr></tbody></table>

System grup jest bardzo elastyczny i pozwala:

* utrzymywać działanie klipów w jednej grupie, jednocześnie przełączając klipy w innej
* szybko przypisywać strefy i odwrócenia X/Y do wszystkich klipów w grupie
* ustawiać _Flash mode_ dla klipu (Group 3 domyślnie działa w _Flash mode_)

Grupy mają też ustawienia przejścia wejścia/wyjścia, które mogą być dziedziczone przez klipy albo nadpisywane.

Grupę klipu możesz przypisać przyciskami w menu prawym przyciskiem myszy albo na APC40: naciśnij przycisk grupy i _trzymając go wciśnięty_, naciśnij przyciski klipów.

Zmiana ustawień stref dla wszystkich klipów w grupie

Na APC40 naciśnij przycisk grupy, a następnie _trzymając go wciśnięty_, użyj przycisków stref i X/Y, aby przełączać ustawienia stref dla wszystkich klipów w tej grupie.

Zobacz także [groups.md](../clips/groups.md)

### Efekty

System efektów w Liberation to potężny i wszechstronny sposób modyfikowania wyjścia klipu w czasie rzeczywistym. Domyślne przyciski efektów 1–8 znajdują się pod przyciskami stref.

#### Stosowanie efektu

Naciśnij przycisk efektu, aby go włączyć lub wyłączyć. Jeszcze lepiej użyć suwaków 1–8 na APC40, aby płynnie wprowadzać i wycofywać efekty.

#### Parametry efektów

Użyj kontrolerów obrotowych 1–8\*, aby dostosować _parameter_ każdego efektu. (Możesz też kliknąć prawym przyciskiem myszy, aby dostosować poziom i parametr). Zmiana parametru działa różnie w zależności od konfiguracji efektu. Poniżej znajdziesz listę domyślnych efektów.

{% hint style="info" %}
Małe liczby widoczne na przyciskach efektów odnoszą się do _level_ i _parameter_ efektu. _level_ jest kontrolowany faderem na APC40 albo przez kliknięcie i przeciągnięcie na przycisku. Parametr reguluje się pokrętłami na APC40 albo prawym przyciskiem myszy.
{% endhint %}

_\*Kontrolery obrotowe 1–8 znajdują się u góry APC40 Mk2 oraz w prawym górnym rogu APC40 Mk1. Zobacz także:_ [apc40-reference.md](../reference/apc40-reference.md)

#### Domyślne efekty

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Dodaje chaotyczny ruch do wyjścia klipu. Parametr reguluje ilość/szybkość chaosu.
2. **Sine wave** :\
   Odkształca całą treść zgodnie z poruszającą się falą sinusoidalną. Parametr reguluje długość fali.
3. **Rotation** :\
   Obraca wszystko dookoła. Parametr reguluje prędkość obrotu.
4. **Horizontal flip** :\
   Ściska i rozciąga wszystko w poziomie. Parametr reguluje szybkość.
5. **Scale** :\
   Wielokrotnie skaluje wszystko od pełnego rozmiaru do zera. Parametr reguluje szybkość.
6. **Hue** :\
   Zmienia odcień wszystkiego, ale nie zmienia nasycenia (czyli wszystko, co białe, pozostaje białe). Parametr reguluje odcień.
7. **Saturation and hue** :\
   Zmienia odcień wszystkiego i jednocześnie w pełni nasyca kolor (czyli wszystko, co białe, zmienia się na dany kolor). Parametr reguluje odcień.
8. **Flash** :\
   Wielokrotnie miga jasnością wszystkiego od pełnej wartości do zera. Parametr reguluje szybkość błysku.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

W dolnym rzędzie znajduje się kolejnych 16 efektów kolorystycznych, które stosują gotowe wartości odcienia i nasycenia.

Pamiętaj, że są to efekty domyślne, ale można je edytować tak, aby robiły prawie wszystko, czego potrzebujesz!

#### Czym jest _„aktualnie wybrany klip”_?

Gdy uruchomisz klip, podświetla się on, pokazując, że jest aktywny. Ma też biały obrys, który wskazuje, że jest to aktualnie _wybrany_ klip. Za każdym razem, gdy przełączasz przyciski stref albo zmieniasz ustawienia klipu, zmiany dotyczą _aktualnie wybranego klipu._

{% hint style="info" %}
Aby wybrać klip bez jego uruchamiania, naciśnij klawisz `Alt / Option` przed naciśnięciem przycisku klipu. To dobry sposób na dostosowanie stref i innych ustawień bez uruchamiania klipu.
{% endhint %}

### Panel Clip Settings

Użyj panelu _Clip Settings_, aby edytować skalowanie, pozycję X/Y oraz uzyskać dostęp do zaawansowanego systemu opóźnień stref.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

W panelu _Global Settings_ możesz dostosować globalne ustawienia wyjścia, które wpływają na całe wyjście we wszystkich strefach.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Włącz AUTO RESET, aby automatycznie resetować wszystkie _Global settings_, gdy nie jest odtwarzany żaden klip.&#x20;

### Timing

Prawie wszystkie pokazy laserowe mają jakiś podkład muzyczny, dlatego system Timing w Liberation opiera się na tempie w uderzeniach na minutę. W panelu _Tempo Panel_ zobaczysz reprezentację czasu: każdy kwadrat oznacza jedno uderzenie i miga zgodnie z tempem.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Dostępnych jest kilka opcji synchronizacji, w tym MIDI clock i Ableton Link. Jeśli znasz tempo muzyki, możesz ustawić je ręcznie suwakiem na ekranie albo pokrętłem Tempo na APC40. Możesz też trzymać tempo z muzyką za pomocą systemu _Tap Tempo_\_.\_

#### Tap Tempo

_Tap Tempo_ to określenie często używane w aplikacjach muzycznych. Pozwala wystukiwać rytm zgodnie z beatem, aby ustawić tempo podczas odtwarzania muzyki. Możesz użyć przycisku na ekranie, choć zalecamy klawisz _T_ albo przycisk _Tap Tempo_ na APC40 (lub nawet przełącznik nożny, jeśli wolisz).

Naciśnij klawisz _R_ albo przycisk _Metronome_ (APC40), aby zresetować tempo do początku taktu.

Naciśnij klawisz _Y_ albo obróć pokrętło _Tempo_ (APC40), aby zaokrąglić tempo do liczby całkowitej. Może to być przydatne w muzyce elektronicznej, która zwykle ma całkowitą liczbę uderzeń na minutę.

### Organizowanie clip decku

Aby przenieść klip w clip decku, kliknij go i przeciągnij w nowe miejsce. Podczas przeciągania możesz używać klawiszy kursora (albo kółka/przycisków przewijania na APC40), aby przewijać w lewo i w prawo.

Podczas przeciągania przytrzymaj klawisz `Alt / Option`, aby utworzyć kopię.

Kliknij klip z przytrzymanym `Alt / Option`, aby zaznaczyć go bez uruchamiania.

Kliknij klip z przytrzymanym `Alt / Option + Shift`, aby zaznaczyć wiele klipów, albo kliknij i przeciągnij poza klipem, aby zaznaczyć obszar „lasso”.&#x20;

Kliknięcie i przeciągnięcie przeniesie WSZYSTKIE zaznaczone klipy.

Aby usunąć jeden lub więcej klipów, przeciągnij je poza clip deck (pojawi się ikona kosza) albo użyj przycisku DELETE w menu klipu pod prawym przyciskiem myszy.

### Panel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ daje szybki wgląd w stan aktualnie działających laserów. Zielony kwadrat po prawej oznacza, że kontroler lasera działa prawidłowo. Jeśli zmieni kolor na pomarańczowy, występują sporadyczne przerwy. Jeśli jest czerwony, kontroler został rozłączony. Jeśli jest szary, nie jest w ogóle podłączony do kontrolera.&#x20;

Wykres pośrodku pokazuje historię długości klatek, a liczba po prawej to aktualna liczba klatek na sekundę. Im bardziej złożona treść, tym niższa będzie liczba klatek (czyli obraz będzie bardziej migotał). Wartości poniżej około 25 fps zaczną wyglądać dość migotliwie.&#x20;

### Łączenie z laserami — panel Controller Assignment

Kliknij przycisk _Assign Laser Controllers_, aby otworzyć panel _Controller Assignment_. (Ten panel można też otworzyć z paska menu przez _View -> Controller Assignment_).

W tym miejscu wybierasz, które wyjścia laserowe trafiają do których kontrolerów laserów. Przeciągnij kontrolery z listy po prawej do pól po lewej. Możesz zmienić nazwy kontrolerów tak, aby odpowiadały sparowanym z nimi laserom (użyj przycisku z ikoną długopisu).

Więcej szczegółów znajdziesz w rozdziale [controller-assignment.md](../setting-up/controller-assignment.md).

{% hint style="danger" %}
Zanim uzbroisz jakiekolwiek lasery, koniecznie przejdź przez rozdział [setting-up-lasers.md](../setting-up/setting-up-lasers.md).
{% endhint %}

### Panel Laser output

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Ten panel pokazuje ustawienia _aktualnie wybranego lasera_ (oznaczonego numerem u góry). Aktualnie wybrany laser możesz zmienić klawiszem _tab_, naciskając klawisz z numerem, klikając numer lasera w panelu _Laser Overview_ albo w _output view._

* **Number button** uzbraja i rozbraja laser. Jeśli jest czerwony, laser jest uzbrojony.
* **Brightness** reguluje jasność lasera niezależnie od innych laserów (jest łączona z ustawieniem _global brightness_ — czyli jeśli oba są ustawione na 50%, laser będzie świecił z jasnością 25%).
* **Test Pattern** włącza wzór testowy tylko dla tego lasera (nadpisuje globalne ustawienie wzoru testowego).
* **Orientation** koryguje lasery zamontowane bokiem lub do góry nogami.
* **Flip Horizontal and Flip Vertical** odwraca wyjście lasera. Przydatne do korekcji wyjścia w laserach z niespójnym okablowaniem.
* **Copy Laser Settings** otwiera panel, który pozwala kopiować różne ustawienia z tego lasera do innych.

### Ustawienia skanerów

Lasery pokazowe działają, poruszając pojedynczą wiązką lasera bardzo szybko i włączając ją oraz wyłączając, aby rysować kształty w powietrzu. To, co widzisz jako linie, kształty i obrazy, jest w rzeczywistości wiązką śledzącą ścieżki szybciej, niż oko jest w stanie zauważyć.

Strumień punktów to dane, które mówią laserowi, dokąd ma przesunąć się dalej i kiedy wiązka ma być włączona lub wyłączona. W Liberation klipy są konwertowane na taki strumień punktów w czasie rzeczywistym podczas wysyłania do laserów.

Liberation daje szczegółową kontrolę nad sposobem generowania strumienia punktów, pozwalając zrównoważyć płynność, jasność i wydajność dla każdego lasera.

{% hint style="info" %}
Jeśli znasz starsze oprogramowanie laserowe, które opiera się na wcześniej przeliczonych strumieniach punktów, to podejście może na początku wydawać się inne. Generowanie punktów w czasie rzeczywistym pozwala jednak optymalizować tę samą treść inaczej dla każdego lasera. Ułatwia to pracę z wieloma laserami o różnych prędkościach lub jakości skanerów bez duplikowania ani ponownego budowania treści. Dzięki temu pliki klipów pozostają też bardzo małe — dlatego cały domyślny clip deck Liberation zajmuje zaledwie kilka megabajtów, a nie gigabajty.
{% endhint %}

Podstawowe ustawienia skanera to:

* **Speed** to prędkość skanera, czyli szybkość, z jaką laser porusza się, rysując kształty. Odpowiada to regulacji point rate w tradycyjnym oprogramowaniu laserowym, ale w Liberation możesz zmieniać szybkość ruchu lasera _niezależnie od point rate._ Nie powinno być potrzeby zmiany tego ustawienia.
* **Scanner sync** (czasem znane jako _blank shift_, wcześniej Colour Shift) Skanery poruszają laserem bardzo szybko, ale zwykle zmiany jasności i koloru nie są zsynchronizowane z ruchem. Objawia się to małymi migoczącymi „ogonami” światła na krawędziach wiązek i linii. Użyj tej regulacji, aby zsynchronizować ruch i kolor. Zobacz [laser-settings](../setting-up/laser-settings/)

Pozostałe zaawansowane ustawienia skanera opisano w rozdziale [advanced](../advanced/).

### Zoning

Pełny przewodnik po konfiguracji i wyznaczaniu stref laserów znajdziesz tutaj: [setting-up-lasers.md](../setting-up/setting-up-lasers.md)
