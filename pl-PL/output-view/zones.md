---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Głównym typem strefy, którego będziesz używać w większości projektów, jest _Beam zone_. Jest to strefa przeznaczona do atmosferycznych efektów wiązek w powietrzu. Drugim typem strefy jest _Canvas zone_ (zobacz [Grafika i system Canvas](../graphics-and-the-canvas-system/)).

{% hint style="danger" %}
**OSTRZEŻENIE — zachowaj szczególną ostrożność podczas przesuwania stref przy włączonym laserze** i zmniejsz jasność do możliwie najniższego poziomu. Zobacz [Przegląd procesu konfiguracji laserów](../setting-up/setting-up-lasers.md), aby zapoznać się z kompletnym przewodnikiem bezpiecznej aktywacji i wyznaczania stref dla laserów.
{% endhint %}

Możesz klikać i przeciągać strefy myszą. Włącz wzorzec testowy, aby zobaczyć, gdzie trafia dana strefa.

{% hint style="info" %}
Użyj klawiszy strzałek, aby **precyzyjnie przesunąć** aktualnie zaznaczoną strefę/punkt. Przytrzymaj klawisz `Shift`, aby przesuwać większymi krokami.
{% endhint %}

{% hint style="info" %}
Wskazówka: możesz szybko kopiować ustawienia stref między wieloma laserami! Zobacz [Kopiowanie ustawień między laserami](../setting-up/copy-laser-settings.md)
{% endhint %}

### Dodawanie nowej strefy beam

Kliknij przycisk _Add a new beam zone_ u góry paska narzędzi, a pojawi się nowa strefa. Pamiętaj, że strefy beam są sortowane w kolejności dodawania, ale możesz zmienić ich kolejność. Zobacz [Zmiana kolejności stref wiązek](re-ordering-beam-zones.md)

### Dodawanie istniejącej strefy canvas

Kliknij przycisk _Add existing canvas zone_. Zobaczysz listę dostępnych stref canvas i możesz włączać lub wyłączać je dla tego lasera. Zobacz [Grafika i system Canvas](../graphics-and-the-canvas-system/)

### Typy kształtu strefy

Dostępne są 3 typy kształtu strefy:

* **Quad** — domyślny prostokątny kształt strefy, który może być równy (wyrównany do osi) lub zniekształcony. Najlepszy do większych prostokątnych stref albo stref canvas wymagających korekcji perspektywy.
* **Line/Curve** — strefa zdefiniowana przez 2 lub więcej punktów oraz grubość. Idealna do wąskich stref albo do zakończeń na balkonach, mostach lub innych zakrzywionych kształtach.
* **Segmented** — strefa, którą można podzielić na mniejsze czworokąty. Idealna do mapowania architektonicznego.

Kliknij prawym przyciskiem dowolną strefę, aby otworzyć jej ustawienia. W tym menu kontekstowym możesz:

* Zmienić nazwę strefy (może to pomóc w jej identyfikacji w clip deck, zwłaszcza jeśli masz dużo stref!)
* Włączyć/wyłączyć strefę
* Zablokować jej pozycję
* Zmienić typ jej kształtu
* Przywrócić ją do domyślnej pozycji
* Uzyskać dostęp do ustawień właściwych dla danego typu kształtu
* Usunąć ją
* Dodać _Alt Zone_ (zobacz [System stref Alt](alt-zone-system.md))

{% hint style="danger" %}
**OSTRZEŻENIE —** zachowaj dużą ostrożność podczas zmiany typu strefy, gdy laser jest aktywny. Strefa wróci do ostatniej pozycji/rozmiaru dla danego kształtu, więc obraz wyjściowy może nagle się zmienić. Najlepiej wyłączyć laser przed zmianą typu strefy.
{% endhint %}

### Kształt strefy Quad

Możesz przesuwać każdy narożnik Quad myszą. Kliknij narożnik z `Alt / Option`, aby przesunąć go niezależnie od pozostałych i zniekształcić Quad. Gdy Quad zostanie zniekształcony, wszystkie narożniki można przesuwać swobodnie.

Możesz usunąć zniekształcenie i przywrócić prostokąt wyrównany do osi, używając przycisku _REMOVE DISTORTION_ w menu kontekstowym.

#### Korekcja perspektywy

Tę opcję można ustawić przełącznikiem w menu kontekstowym. Określa ona metodę zniekształcania. Dla wiązek najlepiej pozostawić ją wyłączoną, ale jeśli ta strefa wyświetla grafikę na płaskiej powierzchni, włącz ją, a obraz wyjściowy zostanie skorygowany perspektywicznie.

{% hint style="info" %}
Jeśli _Perspective correction_ jest wyłączone, zawartość jest zniekształcana przy użyciu _interpolacji dwuliniowej_. Innymi słowy, zawartość jest rozmieszczana równomiernie w obrębie Quad. Dlatego ta metoda najlepiej sprawdza się dla wiązek.

Po włączeniu korekcji perspektywy zawartość jest zniekształcana z użyciem przekształcenia perspektywicznego, które kompensuje skrót perspektywiczny. Jeśli więc wyświetlasz grafikę na ścianie pod kątem, możesz użyć tej opcji, aby odkształcić obraz wyjściowy i skorygować zniekształcenie projekcji.
{% endhint %}

### Kształt strefy Line / Curve

Kształt strefy Line / Curve stał się ostatnio moim najczęściej wybieranym rozwiązaniem podczas pokazów. Można nawet argumentować, że powinien być domyślny dla stref beam.

Bardzo często moje strefy muszą być wąskie, aby zmieściły się w trudnych, ciasnych przestrzeniach w obiektach albo między oknami na budynkach. Zauważyłem, że regulowanie czterech narożników Quad, gdy są tak blisko siebie, potrafi być wyjątkowo uciążliwe. Tak powstała strefa Line / Curve!

W przypadku linii prostych wystarczą dwa punkty, a następnie ustawienie _Zone thickness_ w menu kontekstowym. To najszybszy sposób tworzenia prostych stref.

Kliknij linię z `Alt / Option`, aby utworzyć dodatkowe punkty. Punkty te są automatycznie wygładzane, tworząc płynny kształt. Możesz dostosować _Smooth level_, aby usunąć wszelkie załamania.

Kliknij punkt z `Alt / Option`, aby go usunąć.

Jeśli masz doświadczenie z aplikacjami do grafiki wektorowej (Inkscape, Illustrator itp.), możesz użyć opcji _Manually adjust bezier curves_, aby uzyskać precyzyjną kontrolę nad wszystkimi punktami sterującymi.

### Kształt strefy Segmented

Ta podzielona strefa pozwala wprowadzać bardzo szczegółowe korekty i przydaje się podczas mapowania na złożone kształty. Możesz dodawać lub usuwać podziały za pomocą przycisków + i - w menu kontekstowym.

### Jak edytować strefę całkowicie przykrytą przez inną strefę

Kliknij prawym przyciskiem strefę znajdującą się na wierzchu, a następnie kliknij przycisk kłódki, aby ją zablokować. Teraz powinno być możliwe edytowanie i dostosowanie strefy pod spodem.

<br>

{% hint style="info" %}
Po dodaniu strefy Beam do wyjścia będzie ona dostępna do dodania do klipu w clip deck.
{% endhint %}
