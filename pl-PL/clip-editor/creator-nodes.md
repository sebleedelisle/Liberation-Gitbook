---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Węzły Creator

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Tworzy pojedynczą kropkę / wiązkę.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **Colour** - kolor kropki. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md)
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Tworzy linię / płaszczyznę światła.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **Size** - długość linii
* **Colour** - kolor linii. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md)
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* **rotation** - kąt linii w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md)
* **alignment** - _LEFT / CENTRE / RIGHT -_ określa punkt początkowy i środek obrotu linii
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Tworzy okrąg / stożek.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **radius** - promień okręgu
* **Colour** - kolor okręgu. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md)
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* **resolution** - zobacz [Resolution](fundamentals/resolution.md)
* **Fill state** - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Tworzy wielokąt równoboczny: trójkąt, kwadrat, pięciokąt itd.

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **size** - odległość od środka do każdego z narożników
* **Colour** - kolor wielokąta. Zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md)
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* **rotation** - kąt obrotu kształtu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md)
* **Fill state** - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Wczytuje plik SVG dla własnych kształtów.

{% hint style="warning" %}
Liberation jest zgodny z formatem _SVGTiny_. Zalecamy InkScape, ale większość aplikacji do grafiki wektorowej potrafi eksportować w tym formacie. Przed eksportem upewnij się, że cały tekst został przekonwertowany na kształty. Liberation będzie renderować obrysy i opcjonalnie używać wypełnień jako masek. Upewnij się, że linie nie są czarne, bo bez modyfikatora koloru nie będą widoczne!
{% endhint %}

* **Import SVG** - wczytuje plik SVG z dysku.

{% hint style="info" %}
Po wczytaniu SVG zawartość zostaje przekonwertowana i zapisana w klipie, więc nie musisz zachowywać odniesienia do pliku, chyba że później zechcesz zmienić ustawienia masek.
{% endhint %}

* **Use fills as masks** - przetwarza każdy wypełniony kształt jako maskę, tj. wypełnia go czernią. To ustawienie zostanie włączone automatycznie, jeśli SVG zawiera jakiekolwiek wypełnione kształty. Jeśli nie ma wypełnionych kształtów, zostanie wyłączone. Zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - jeśli kształty w SVG nie mają obrysu, nie możemy ich narysować! Ta opcja dodaje obrys (czyli _stroke_) do każdego wypełnionego kształtu. Jeśli SVG nie zawiera żadnych kształtów z obrysem, ustawienie zostanie włączone automatycznie. Jeśli nie zawiera żadnych wypełnionych kształtów, zostanie wyłączone.
* **Invert black lines** - jeśli wszystkie linie w SVG są czarne, nie będzie ich widać! Ta opcja zmienia je na białe. Zostanie włączona automatycznie, jeśli SVG zawiera tylko czarne kształty, ale pozostanie wyłączona, jeśli nie ma ich wcale.
* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **scale** - dostosowuje rozmiar SVG. Wartość jest obliczana automatycznie podczas wczytywania SVG (aby obraz był widoczny), ale później można ją ręcznie zmienić.
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* **rotation** - kąt obrotu obrazu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Tworzy animację z sekwencji plików SVG.

* **Import SVG Sequence** - wybierz folder zawierający wszystkie pliki SVG. Pamiętaj, że są one wczytywane w kolejności alfanumerycznej.

{% hint style="info" %}
Po wczytaniu sekwencji SVG zawartość zostaje przekonwertowana i zapisana w klipie, więc nie musisz zachowywać odniesienia do plików, chyba że później zechcesz zmienić ustawienia masek.
{% endhint %}

* **Use fills as masks** - przetwarza każdy wypełniony kształt jako maskę, tj. wypełnia go czernią. To ustawienie zostanie włączone automatycznie, jeśli którykolwiek z plików SVG zawiera wypełnione kształty. Jeśli żaden ich nie zawiera, zostanie wyłączone. Zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** - jeśli kształty w plikach SVG nie mają żadnych obrysów, nie możemy ich narysować! Ta opcja dodaje obrys (czyli _stroke_) do każdego wypełnionego kształtu. Jeśli pliki SVG nie zawierają żadnych kształtów z obrysem, ustawienie zostanie włączone automatycznie. Jeśli żaden plik nie zawiera wypełnionych kształtów, zostanie wyłączone.
* **Invert black lines** - jeśli wszystkie linie w plikach SVG są czarne, nie będzie ich widać! Ta opcja zmienia je na białe. Zostanie włączona automatycznie, jeśli pliki SVG zawierają tylko czarne kształty, ale pozostanie wyłączona, jeśli nie ma ich wcale.
* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **scale** - dostosowuje rozmiar obrazu.
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* **rotation** - kąt obrotu obrazu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md)
* **speed** - czas trwania całej animacji w taktach.
* **time per frame** - jeśli to ustawienie jest włączone, czas trwania dotyczy pojedynczej klatki, a nie całej animacji. Jeśli więc _speed_ ustawiono na ¼, każda klatka będzie trwać 1 uderzenie.
* **animation direction** -
  * _FORWARDS_ - animacja odtwarza się do przodu, a następnie zapętla od początku
  * _BACKWARDS_ - animacja odtwarza się do tyłu, a następnie zapętla od końca
  * _PINGPONG_ - animacja odtwarza się do przodu, a potem do tyłu w pętli
  * _MANUAL_ - bieżąca klatka jest ustawiana za pomocą ustawienia _position manual_
* **position manual** - ustawia bieżącą klatkę; 0% to pierwsza klatka, a 100% to ostatnia. Można ustawić ręcznie albo za pomocą zewnętrznego oscylatora.
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Tworzy tekst przy użyciu czcionki TrueType lub OpenType.

* **Text** - wpisz tutaj tekst, którego chcesz użyć
* **Font** - wybierz czcionkę, której chcesz użyć

{% hint style="info" %}
Aby dodać więcej czcionek do Liberation, skopiuj pliki .ttf lub .otf do folderu data/resources/fonts.
{% endhint %}

* **Render profile** - zobacz [Profil renderowania](fundamentals/render-profile.md)
* **horizontal alignment** - wybierz _LEFT_, _CENTRE_ albo _RIGHT_, aby ustawić wyrównanie tekstu.
* **Fill state** - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)
* **size** - rozmiar tekstu
* **colour -** zobacz [Ustawienia koloru i HSB](fundamentals/colour-settings-and-hsb.md)
* pozycja **x** i **y** - zobacz [Układ współrzędnych](fundamentals/co-ordinate-system.md)
* **rotation** - kąt obrotu obrazu w stopniach
* **resolution** - zobacz [Resolution](fundamentals/resolution.md)
* **reveal** - użyj tego ustawienia, aby stopniowo odsłaniać tekst, po jednym znaku. Gdy wartość mieści się między 0 a 50%, tekst będzie stopniowo pojawiał się od lewej do prawej. Gdy mieści się między 50% a 100%, tekst będzie znikał od lewej do prawej. Możesz podłączyć oscylator do tego gniazda, aby tworzyć animacje.
* **reveal by word** - gdy jest włączone, _reveal_ działa słowo po słowie, a nie znak po znaku.
* **countdown** - system odliczania (zaimplementowany naprędce!). Zmienia wartość co 2 uderzenia, więc jeśli chcesz uzyskać sekundy, ustaw tempo na 120 bpm.
* **countdown start** - liczba, od której ma rozpocząć się odliczanie
* _MOVE TO FRONT / MOVE TO BACK_ - zobacz [Wypełnienia, maski i sortowanie głębokości](fundamentals/fills-masks-and-depth-sorting.md)
