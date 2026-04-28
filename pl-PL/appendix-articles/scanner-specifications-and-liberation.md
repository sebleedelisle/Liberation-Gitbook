---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Specyfikacje skanerów i Liberation

### Nieuporządkowana rzeczywistość specyfikacji skanerów

Częstotliwości punktów i specyfikacje skanerów mogą być nieco mylące. Często zobaczysz parametry typu 30kpps @ 8º albo 50kpps @ 4º, ale nie zawsze jest oczywiste, co te liczby faktycznie oznaczają.

{% hint style="info" %}
Zastrzeżenie — nie jestem specjalistą od sprzętu skanerów, ale mam lata praktycznego doświadczenia w uzyskiwaniu dobrego wyglądu skanerów o bardzo różnej jakości za pomocą oprogramowania i generowania strumienia punktów, a nie strojenia sprzętu. Ten tekst opiera się właśnie na tym doświadczeniu.
{% endhint %}

#### **Skąd biorą się te liczby**

Określenia takie jak „30K” i „50K” to skróty odnoszące się do tego, jak skanery są oceniane za pomocą wzorca testowego ILDA przy danych częstotliwościach punktów i w określonych warunkach.

Gdy skaner jest opisany na przykład jako: _30Kpps @ 8°_, w praktyce oznacza to:

> „Ten skaner potrafi odtworzyć wzorzec testowy ILDA przy 30 000 punktów/s i kącie skanowania 8°, jeśli jest prawidłowo dostrojony.”

Nie jest to pełny ani w pełni ustandaryzowany pomiar rzeczywistej wydajności. Właściwie pierwotnie nie zaprojektowano go wcale jako benchmarku — służył do **procedury strojenia**. Uruchamiasz znany wzorzec przy stałej częstotliwości punktów (np. 30 000 punktów/s), a następnie regulujesz tłumienie i wzmocnienie, aż obraz wygląda poprawnie.

Mimo to jest to nadal najpowszechniej używany punkt odniesienia, jaki mamy, i może dać dobrą orientację co do jakości skanerów, przynajmniej u renomowanych producentów. W przypadku tych _mniej renomowanych_ bywa różnie...

#### Jeśli chcesz przetestować skanery zgodnie z ich deklarowaną specyfikacją

{% hint style="danger" %}
**To zaawansowana technika i możesz uszkodzić skanery, jeśli nie zachowasz ostrożności. Nie jest zalecana, chyba że wiesz, co robisz.**
{% endhint %}

Musisz znaleźć oprogramowanie, które potrafi wyświetlić [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) — wydaje mi się, że LaserShowGen może to potrafić — i ustawić rozmiar wyjściowy tak, aby odpowiadał podanemu kątowi skanowania (np. 8°). Wskazówki dotyczące analizy obrazu znajdziesz w dokumentacji ILDA.

#### Dlaczego może to nie być dobry benchmark

Po pierwsze, wzorzec testowy może wyglądać nieprawidłowo nawet wtedy, gdy skanery są dobre, ponieważ nie są dostrojone w sposób zoptymalizowany pod ten test.

Może to być przydatna ogólna wskazówka do odróżnienia „dobrych” skanerów od „złych”, ale producenci czasem traktują te specyfikacje dość swobodnie.

#### Jak więc wybrać dobry skaner?

Moim zdaniem najlepiej upewnić się, że pochodzi od renomowanego producenta. Drożsi producenci skanerów z wyższej półki, tacy jak Cambridge Technology (CT), Eye Magic (EMS) i ScannerMAX (spółka zależna Pangolin), są zawsze dobrym wyborem i trudno tu popełnić błąd. Ale gdy para skanerów kosztuje około 1000 USD, dla wielu osób zaczynających przygodę jest to droższe niż same lasery!

Dlatego najczęściej używałem producentów chińskich. Skanery Dragon Tiger (DT) są przyzwoite i niedrogie, i wydaje mi się, że LightSpace ich używa. Wielu innych producentów (w tym OPT i Able w niektórych modelach) również stosuje systemy oparte na DT.

Phenix Technology (PT) są zwykle z niższej półki, ale szczerze mówiąc, prawdopodobnie nadają się do większości zastosowań.

**Jeśli skanery nie mają marki, to właśnie wtedy warto zacząć martwić się o jakość!**

#### Jak pomaga Liberation

Po pierwsze, do większości zastosowań naprawdę nie potrzebujesz bardzo drogich skanerów! Niedrogie DT 30kpps, a nawet PT, będą w porządku. Domyślne ustawienia skanerów są celowo zachowawcze i w większości przypadków _nie trzeba ich regulować_ (poza _Scanner sync_).

Nawet jeśli masz lepsze skanery, nie ma sensu obciążać ich bardziej, niż to konieczne. Znacząco wydłuży to ich żywotność.

#### Czym jest „strumień punktów”?

Prawdopodobnie spotkałeś się już z tym terminem — tak sterujemy ścieżką skanerów.

Strumień punktów to lista pozycji X/Y, z których każda ma przypisany kolor. Aby narysować na przykład białą linię, wysyłasz sekwencję punktów wzdłuż tej linii, wszystkie ustawione na biało. Skanery przemieszczają się następnie od punktu do punktu ze stałą częstotliwością — liczbą punktów na sekundę (PPS) — a wiązka odrysowuje kształt.

#### Jak działa to w tradycyjnym oprogramowaniu laserowym

Tradycyjne oprogramowanie laserowe przechowuje strumień punktów dla każdej cue. W przypadku animowanych cue zwykle oznacza to osobny strumień punktów dla każdej klatki. Kluczowe jest to, że wszystko jest całkowicie z góry określone. W rezultacie zwiększenie częstotliwości punktów sprawia, że skanery poruszają się szybciej po tych samych wcześniej przygotowanych danych.

{% hint style="info" %}
W starszym oprogramowaniu takie podejście było konieczne — komputery po prostu nie były wystarczająco szybkie, aby generować strumienie punktów w czasie rzeczywistym. Dlatego zwykle istnieje osobny edytor cue, używany do wcześniejszego wygenerowania danych dla każdej klatki animacji.

Wyjaśnia to również, dlaczego zawartość może zajmować gigabajty miejsca. W praktyce przechowujesz duże, nieskompresowane przebiegi przy dość wysokich częstotliwościach próbkowania.
{% endhint %}

#### Dlaczego „częstotliwość punktów” ma w Liberation mniejsze znaczenie

Liberation generuje strumień punktów w czasie rzeczywistym, co daje nam ogromną elastyczność. Zwróć uwagę na ustawienie "Scanner speed" w panelu Laser Settings. Pozwala ono przyspieszać i spowalniać skanery, ale co ważne, **nie** zmienia bazowej częstotliwości punktów (PPS).

#### Zaraz, co? Jak to możliwe?

Wiem, na początku brzmi to dziwnie.

Ponieważ Liberation generuje strumień punktów w czasie rzeczywistym, może go na bieżąco dostosowywać. Im bardziej punkty są od siebie oddalone, tym szybciej poruszają się skanery. Im bliżej siebie się znajdują, tym wolniej poruszają się skanery.

{% hint style="info" %}
W nowszych wersjach Liberation rzeczywista _częstotliwość punktów_ (w ustawieniach zaawansowanych) w ogóle nie wpływa na prędkość skanerów. Zamiast tego renderer dostosowuje rozkład punktów do wybranej częstotliwości punktów, zachowując niezmieniony ruch skanerów.

Ma to wpływ na „rozdzielczość” ścieżki punktów, ale ma to znaczenie głównie dla grafiki (i może pomóc w dokładniejszym ustawieniu _scanner sync_).
{% endhint %}

#### Świetnie! Co to wszystko właściwie oznacza?

Dobre pytanie. Oto moje wskazówki:

* Unikaj skanerów bez marki. Jeśli możesz kupić szybsze skanery, zrób to — minimum 30KPPS.
* W większości przypadków skanery DT30 są wystarczające, a skanery PT30 prawdopodobnie będą OK w tańszych laserach.
* Jeśli tworzysz grafikę, w większości przypadków większa liczba laserów da lepszy efekt niż szybsze skanery.
* Gdy przejdziesz do konfiguracji z wyższej półki, każda z uznanych marek premium będzie dobrym wyborem.
* Jeśli masz dostęp tylko do najtańszych skanerów bez marki, domyślne ustawienia Liberation są dość zachowawcze i prawdopodobnie uzyskasz akceptowalne rezultaty przy podstawowej pracy z wiązkami. Jeśli system sobie nie radzi, zmniejsz ustawienie **Speed** (ale nie zmieniaj częstotliwości punktów!).

#### A ILDA Test Pattern?

…nadal jest bardzo przydatny jako narzędzie kalibracyjne i referencyjne, ale nigdy nie został zaprojektowany jako kompleksowy benchmark i może być przez producentów używany niewłaściwie albo interpretowany zbyt swobodnie.
