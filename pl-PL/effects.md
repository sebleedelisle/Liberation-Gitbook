---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Efekty

System efektów w Liberation to przyjemny i wszechstronny sposób zmieniania wyjścia klipu w czasie rzeczywistym. Efekty są całkowicie elastyczne — możesz dzięki nim sprawić, że wszystko będzie migać, obracać się, zmieniać kolory, a nawet poruszać się losowo!

Wszystko, co możesz zrobić w edytorze klipów, może zostać użyte jako efekt. Efekty edytuje się dokładnie w tym samym edytorze węzłów co klipy! Zobacz [Efekty](effects.md#editing-effects). Możliwości twórcze są praktycznie nieograniczone.

Domyślne przyciski efektów 1–8 znajdują się pod przyciskami stref, a efekty 9–24 to małe przyciski na dole.

#### Stosowanie efektu

Naciśnij przycisk efektu, aby go włączyć lub wyłączyć. Jeszcze lepiej: użyj suwaków APC40 1–8, aby płynnie wprowadzać i wyciszać efekty. Aby wprowadzić efekt bez APC40, kliknij przycisk i przeciągnij w górę lub w dół. Możesz też kliknąć przycisk efektu prawym przyciskiem myszy i dostosować suwak poziomu.

{% hint style="warning" %}
Naciśnięcie przycisku efektu natychmiast aktywuje ten efekt. Pamiętaj jednak, że jeśli poziom jest ustawiony na zero, nic się nie stanie! Kliknij/przeciągnij przycisk, aby zmienić poziom, kliknij prawym przyciskiem i użyj suwaka _level_ albo użyj faderów APC40.
{% endhint %}

#### Efekty i opóźnienie strefy klipu

Efekty przejmują ustawienie opóźnienia strefy dla każdego aktualnie uruchomionego klipu. Jeśli więc klip ma opóźnienie przechodzące od lewej do prawej, a dodasz efekt migania, błysk również będzie opóźniony od lewej do prawej.

{% hint style="info" %}
Sposób, w jaki opóźnienie strefy klipu jest dziedziczone przez efekty, to jedna z tych rzeczy, które bardzo trudno opisać, ale które stają się oczywiste, gdy się ich spróbuje!

Moim zdaniem to jedno z najciekawszych i najbardziej kreatywnych narzędzi wbudowanych w Liberation. Wypróbuj je, a zobaczysz, o co chodzi!
{% endhint %}

#### Parametry efektu

Dodaj parametr do efektu za pomocą _Parameter node._ System parametrów pozwala regulować wiele ustawień wewnątrz efektu z zewnątrz. Więcej informacji znajdziesz w [Parameter Control](clip-editor/oscillators/parameter-control.md).

Użyj kontrolerów obrotowych 1–8, aby regulować _parameter_ dla każdego efektu. Możesz też kliknąć przycisk efektu prawym przyciskiem myszy i dostosować suwaki parametrów. Zmiana parametru robi różne rzeczy w zależności od tego, jak skonfigurowany jest efekt. Poniżej znajdziesz listę domyślnych efektów oraz opis działania ich parametrów.

{% hint style="info" %}
Kontrolery obrotowe 1–8 znajdują się u góry APC40 Mk2 oraz w prawym górnym rogu APC40 Mk1. Zobacz też: [Referencja APC40](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Małe liczby widoczne na przyciskach efektów odnoszą się do _level_ i _parameter_ efektu. _level_ jest sterowany faderem na APC40 albo przez kliknięcie i przeciągnięcie przycisku. Parametr reguluje się kontrolerami obrotowymi na APC40 albo przez kliknięcie prawym przyciskiem myszy i zmianę myszą.
{% endhint %}

#### Domyślne efekty

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Dodaje chaotyczny ruch do wyjścia klipu. Parametr reguluje ilość/szybkość chaosu.
2. **Sine wave** :\
   Odkształca całą zawartość wzdłuż poruszającej się sinusoidy. Parametr reguluje długość fali.
3. **Rotation** :\
   Obraca wszystko dookoła. Parametr reguluje prędkość obrotu.
4. **Horizontal flip** :\
   Ściska i rozciąga wszystko w poziomie. Parametr reguluje prędkość.
5. **Scale** :\
   Wielokrotnie skaluje wszystko od pełnego rozmiaru do zera. Parametr reguluje prędkość.
6. **Hue** :\
   Zmienia odcień wszystkiego, ale nie zmienia nasycenia (czyli wszystko, co białe, pozostaje białe). Parametr reguluje odcień.
7. **Saturation and hue** :\
   Zmienia odcień wszystkiego i jednocześnie w pełni nasyca kolor (czyli wszystko, co białe, zmienia się na dany kolor). Parametr reguluje odcień.
8. **Flash** :\
   Wielokrotnie zmienia jasność wszystkiego od pełnej do zera. Parametr reguluje prędkość błysku.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

W dolnym rzędzie znajduje się kolejnych 16 efektów kolorystycznych, które stosują zdefiniowane wartości odcienia i nasycenia.

Pamiętaj, że są to efekty domyślne, ale można je edytować tak, aby robiły prawie wszystko, czego potrzebujesz!

### Apply to groups

Możesz wybrać, na które grupy ma działać efekt. Kliknij prawym przyciskiem myszy i przełącz pola wyboru grup oznaczone _Apply to groups._

Najczęściej używam tej konfiguracji, gdy pracuję osobno z grafiką canvas i wiązkami laserowymi. Przypisuję wszystkie klipy canvas do grupy 5, a następnie wykluczam tę grupę z efektów, które nie powinny wpływać na te klipy graficzne.

Możesz też użyć tego do stosowania na żywo dwóch różnych zmian koloru do dwóch grup laserów jednocześnie. Utwórz dwa efekty zmiany koloru i wybierz, do których grup klipów ma być stosowany każdy z nich.

### MX group

Skrót od _Mutually Exclusive_. To sposób grupowania efektów tak, aby w danej grupie aktywny mógł być tylko jeden efekt naraz. Zauważ, że tylko jeden z domyślnych efektów zmiany koloru może być aktywny w tym samym czasie. Dzieje się tak, ponieważ wszystkie należą do MX Group 1.

Ta funkcja jest wyłączona, jeśli ustawienie _MX Group_ ma wartość 0.

### Edycja efektów

Kliknij dowolny efekt prawym przyciskiem myszy i kliknij przycisk _EDIT EFFECT_, aby otworzyć edytor efektów. Zauważ, że ten edytor jest identyczny jak edytor klipów!

Edytuj efekt tak samo, jak edytujesz dowolny klip. Zobacz [Edytor Clipów](clip-editor/).

Musisz mieć co najmniej jeden węzeł typu creator; może to być cokolwiek (linia, okrąg, kształt, a nawet tekst!), ale najlepiej wybrać coś, co ma sens w podglądzie przycisku efektu.

Gdy efekty są stosowane, wszystkie węzły creator w efekcie są zastępowane wyjściem aktualnie uruchomionych klipów.

{% hint style="warning" %}
Z wyjątkowo żmudnych powodów technicznych węzły "trails" nie są włączone wewnątrz efektu. To samo dotyczy ustawienia "delay" w węzłach pattern (korzystają z tego samego systemu). Zostanie to poprawione w przyszłych wersjach.
{% endhint %}
