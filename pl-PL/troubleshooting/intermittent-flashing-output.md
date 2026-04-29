---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Przerywane / migające wyjście

Otwórz panel _Laser Overview_ i sprawdź kontrolkę połączenia obok lasera, z którym masz problem.

**Jeśli kontrolka połączenia NIE świeci stale na zielono:**\
Oznacza to problem z siecią albo z wydajnością CPU:

**Wydajność sieci -**

* Upewnij się, że nie masz połączenia z siecią Wi-Fi. Zawsze używaj połączenia przewodowego. Upewnij się, że system operacyjny priorytetowo traktuje sieć przewodową zamiast Wi-Fi, albo wyłącz Wi-Fi, jeśli nie masz pewności.
* Sprawdź kartę sieciową i wypróbuj inny adapter USB-C.
* Użytkownicy Windows: sprawdź / zaktualizuj sterowniki sieciowe i uruchom odpowiednie narzędzia do testowania sieci.
* Sprawdź całe okablowanie, przełączniki i routery. Metodycznie podmieniaj i testuj każdy kabel.
* Uruchom ponownie cały sprzęt sieciowy, w tym przełączniki, routery oraz każdy Ether Dream.

**Wydajność CPU**

Jeśli masz stary komputer albo maszynę o słabej specyfikacji, może być ona zbyt wolna do uruchamiania Liberation. Sprawdź wskaźnik liczby klatek po prawej stronie paska ikon.

Widać tam dwie wartości: rzeczywistą liczbę klatek i docelową liczbę klatek. Jeśli rzeczywista liczba klatek spada poniżej 30, mogą wystąpić problemy.

Pomóc mogą następujące działania:

* Usuń nieużywane lasery, np. jeśli masz podłączony tylko jeden laser, usuń pozostałe.
* Przełącz się do widoku Output lub Canvas.
* Zamknij wszystkie inne programy, sprawdź ustawienia zapory sieciowej, zamknij program antywirusowy, Dropbox itp.
* Zmniejsz rozdzielczość ekranu i zmniejsz okno Liberation.

Jeśli żadne z tych działań nie pomoże, rozważ modernizację komputera.

***

**Jeśli kontrolka połączenia świeci stale na zielono:**

Prawdopodobnie jest to problem sprzętowy. Wykracza to poza zakres tego podręcznika, ale możesz spróbować następujących działań:

* Wyłącz system SFS (Scan Fail Safety). Niektóre lasery mają funkcję, która wyłącza wyjście, jeśli skanery przestaną się poruszać, czyli gdy powstaje silna statyczna wiązka. Takie systemy bywają nieco nadmiernie ostrożne / zawodne.

{% hint style="danger" %}
Zachowaj szczególną ostrożność przy wyłączaniu systemu scan fail safety. Silne statyczne wiązki mogą powodować przypalenia! Upewnij się, że masz pod ręką przycisk awaryjnego zatrzymania oraz gaśnicę.
{% endhint %}

* Sprawdź przewody i systemy blokad bezpieczeństwa.
* Sprawdź całe okablowanie między kontrolerem a laserem.

[ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) może być niezwykle przydatnym narzędziem przy rozwiązywaniu problemów z laserem.
