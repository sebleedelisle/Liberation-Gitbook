---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Węzły Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Tworzy pojedynczą kropkę / wiązkę.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **Colour** - kolor kropki. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Tworzy linię / płaszczyznę światła.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **Size** - długość linii
* **Colour** - kolor linii. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kąt linii w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ określa punkt początkowy i środek obrotu linii
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Tworzy okrąg / stożek.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **radius** - promień okręgu
* **Colour** - kolor okręgu. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* **resolution** - zobacz [Resolution](fundamentals/resolution.md "mention")
* **Fill state** - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Tworzy wielokąt równoboczny: trójkąt, kwadrat, pięciokąt itd.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **size** - odległość od środka do każdego z narożników
* **Colour** - kolor wielokąta. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kąt obrotu kształtu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md "mention")
* **Fill state** - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Wczytuje plik SVG dla własnych kształtów.

{% hint style="warning" %}
Liberation jest zgodny z formatem _SVGTiny_. Zalecamy InkScape, ale większość aplikacji do grafiki wektorowej potrafi eksportować w tym formacie. Przed eksportem upewnij się, że cały tekst został przekonwertowany na kształty. Liberation będzie renderować obrysy i opcjonalnie używać wypełnień jako masek. Upewnij się, że linie nie są czarne, bo bez modyfikatora koloru nie będą widoczne!
{% endhint %}

* **Import SVG** - wczytuje plik SVG z dysku.

{% hint style="info" %}
Po wczytaniu SVG zawartość zostaje przekonwertowana i zapisana w klipie, więc nie musisz zachowywać odniesienia do pliku, chyba że później zechcesz zmienić ustawienia masek.
{% endhint %}

* **Use fills as masks** - przetwarza każdy wypełniony kształt jako maskę, tj. wypełnia go czernią. To ustawienie zostanie włączone automatycznie, jeśli SVG zawiera jakiekolwiek wypełnione kształty. Jeśli nie ma wypełnionych kształtów, zostanie wyłączone. Zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - jeśli kształty w SVG nie mają obrysu, nie możemy ich narysować! Ta opcja dodaje obrys (czyli _stroke_) do każdego wypełnionego kształtu. Jeśli SVG nie zawiera żadnych kształtów z obrysem, ustawienie zostanie włączone automatycznie. Jeśli nie zawiera żadnych wypełnionych kształtów, zostanie wyłączone.
* **Invert black lines** - jeśli wszystkie linie w SVG są czarne, nie będzie ich widać! Ta opcja zmienia je na białe. Zostanie włączona automatycznie, jeśli SVG zawiera tylko czarne kształty, ale pozostanie wyłączona, jeśli nie ma ich wcale.
* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **scale** - dostosowuje rozmiar SVG. Wartość jest obliczana automatycznie podczas wczytywania SVG (aby obraz był widoczny), ale później można ją ręcznie zmienić.
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kąt obrotu obrazu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Tworzy animację z sekwencji plików SVG.

* **Import SVG Sequence** - wybierz folder zawierający wszystkie pliki SVG. Pamiętaj, że są one wczytywane w kolejności alfanumerycznej.

{% hint style="info" %}
Po wczytaniu sekwencji SVG zawartość zostaje przekonwertowana i zapisana w klipie, więc nie musisz zachowywać odniesienia do plików, chyba że później zechcesz zmienić ustawienia masek.
{% endhint %}

* **Use fills as masks** - przetwarza każdy wypełniony kształt jako maskę, tj. wypełnia go czernią. To ustawienie zostanie włączone automatycznie, jeśli którykolwiek z plików SVG zawiera wypełnione kształty. Jeśli żaden ich nie zawiera, zostanie wyłączone. Zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - jeśli kształty w plikach SVG nie mają żadnych obrysów, nie możemy ich narysować! Ta opcja dodaje obrys (czyli _stroke_) do każdego wypełnionego kształtu. Jeśli pliki SVG nie zawierają żadnych kształtów z obrysem, ustawienie zostanie włączone automatycznie. Jeśli żaden plik nie zawiera wypełnionych kształtów, zostanie wyłączone.
* **Invert black lines** - jeśli wszystkie linie w plikach SVG są czarne, nie będzie ich widać! Ta opcja zmienia je na białe. Zostanie włączona automatycznie, jeśli pliki SVG zawierają tylko czarne kształty, ale pozostanie wyłączona, jeśli nie ma ich wcale.
* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **scale** - dostosowuje rozmiar obrazu.
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kąt obrotu obrazu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md "mention")
* **speed** - czas trwania całej animacji w taktach.
* **time per frame** - jeśli to ustawienie jest włączone, czas trwania dotyczy pojedynczej klatki, a nie całej animacji. Jeśli więc _speed_ ustawiono na ¼, każda klatka będzie trwać 1 uderzenie.
* **animation direction** -
  * _FORWARDS_ - animacja odtwarza się do przodu, a następnie zapętla od początku
  * _BACKWARDS_ - animacja odtwarza się do tyłu, a następnie zapętla od końca
  * _PINGPONG_ - animacja odtwarza się do przodu, a potem do tyłu w pętli
  * _MANUAL_ - bieżąca klatka jest ustawiana za pomocą ustawienia _position manual_
* **position manual** - ustawia bieżącą klatkę; 0% to pierwsza klatka, a 100% to ostatnia. Można ustawić ręcznie albo za pomocą zewnętrznego oscylatora.
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Tworzy tekst przy użyciu czcionki TrueType lub OpenType.

* **Text** - wpisz tutaj tekst, którego chcesz użyć
* **Font** - wybierz czcionkę, której chcesz użyć

{% hint style="info" %}
Aby dodać więcej czcionek do Liberation, skopiuj pliki .ttf lub .otf do folderu `data/fonts` w folderze roboczym Liberation, a następnie uruchom Liberation ponownie.
{% endhint %}

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md "mention")
* **horizontal alignment** - wybierz _LEFT_, _CENTRE_ albo _RIGHT_, aby ustawić wyrównanie tekstu.
* **Fill state** - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - rozmiar tekstu
* **monospace** - rysuje każdy znak z taką samą szerokością. Jest to przydatne przy timerach i licznikach, ponieważ tekst nie przesuwa się na boki podczas zmiany cyfr.
* **character spacing** - dostosowuje odstępy między znakami. Zwiększ tę wartość, aby uzyskać szersze światło międzyliterowe, albo zmniejsz ją, aby ciaśniej złożyć tekst.
* **colour -** zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kąt obrotu obrazu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md "mention")
* **reveal** - użyj tego ustawienia, aby stopniowo odsłaniać tekst, po jednym znaku. Gdy wartość mieści się między 0 a 50%, tekst będzie stopniowo pojawiał się od lewej do prawej. Gdy mieści się między 50% a 100%, tekst będzie znikał od lewej do prawej. Możesz podłączyć oscylator do tego gniazda, aby tworzyć animacje.
* **reveal by word** - gdy jest włączone, _reveal_ działa słowo po słowie, a nie znak po znaku.
* **countdown** - zastępuje wpisany tekst odliczaniem. Gdy odliczanie dojdzie do zera, wyświetlana jest zwykła wartość **Text**.
* **use seconds** - odlicza w rzeczywistych sekundach. Gdy ta opcja jest wyłączona, odliczanie opiera się na uderzeniach: dwa uderzenia liczą się jako jedna sekunda, więc 120 bpm odpowiada rzeczywistym sekundom.
* **show minutes/seconds** - pokazuje pozostały czas w minutach i sekundach. Jeśli przekracza godzinę, uwzględnia także godziny.
* **countdown to date/time** - odlicza do określonej daty i godziny UTC zamiast odliczać od podanej liczby.
* **countdown datetime** - ustawia docelową datę i godzinę UTC, gdy włączone jest **countdown to date/time**.
* **start number** - liczba początkowa, gdy **countdown to date/time** jest wyłączone.
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Jeśli menu rozwijane czcionek jest otwarte, klawisze strzałek w górę i w dół przechodzą przez dostępne czcionki.
{% endhint %}
