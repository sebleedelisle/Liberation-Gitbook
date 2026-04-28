---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Używanie Liberation z Capture

Liberation obsługuje [Capture](https://capture.se) jako zewnętrzny wizualizer (od wersji 1.0.3). Jeśli używasz już Capture w swoim procesie pracy, możesz wykorzystać go do wizualizacji wyjścia laserowego na żywo z Liberation w swojej scenie 3D.

### Jak to działa

Nie jest wymagany żaden specjalny proces łączenia ani ręczne powiązanie.

Wystarczy, że:

* Liberation i Capture są w tej samej sieci
* zapora sieciowa zezwala na połączenie

…wtedy wszystkie lasery skonfigurowane w Liberation automatycznie pojawią się w Capture jako źródła multimediów. Nie musisz konfigurować adresów IP ani włączać żadnych specjalnych opcji — źródła po prostu się pojawią.

### Wyświetlanie laserów w Capture

Wszystkie lasery skonfigurowane w Liberation pojawią się w Capture jako dostępne źródła multimediów.

Aby faktycznie zobaczyć wyjście:

* laser musi być uzbrojony w Liberation
* źródło musi być przypisane do urządzenia laserowego w Capture

Po uzbrojeniu Capture będzie wizualizować strumień wyjściowy na żywo z Liberation. Jeśli laser zostanie rozbrojony w Liberation, nadal będzie widoczny w Capture jako źródło, ale nie będzie niczego wyświetlał.

Więcej instrukcji i pomocy dotyczącej konfiguracji laserów w Capture znajdziesz w dokumentacji na [capture.se](https://www.capture.se/). <br>

### Limity licencji i uzbrojone lasery

Połączenia z Capture są traktowane dokładnie tak samo jak fizyczne wyjścia laserowe.

Oznacza to, że:

* możesz uzbroić tylko tyle laserów, na ile pozwala Twój poziom licencji
* tylko uzbrojone lasery będą aktywnie wysyłać dane do Capture

### Czy potrzebuję Capture?

Nie.

Liberation zawiera wbudowany 3D Visualiser, który jest zawsze dostępny i nie zależy od poziomu licencji. Możesz projektować i podglądać pokazy bezpośrednio w Liberation, bez żadnego zewnętrznego oprogramowania.

Capture to po prostu dodatkowa opcja, jeśli używasz go już do projektowania oświetlenia lub pokazów.

### Rozwiązywanie problemów

Jeśli lasery nie pojawiają się w Capture:

* sprawdź, czy obie aplikacje są w tej samej sieci
* sprawdź ustawienia zapory sieciowej
* upewnij się, że laser jest uzbrojony w Liberation
