---
description: >-
  Lasery mogą być niebezpieczne, dlatego ważne jest przestrzeganie dobrych
  praktyk i zasad bezpieczeństwa. Ta strona zawiera przydatny przegląd, który
  przeprowadzi Cię przez proces bezpiecznej konfiguracji laserów.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ Przegląd procesu konfiguracji laserów

### Przegląd procesu bezpiecznego włączania laserów

Ten podręcznik nie zastępuje formalnego szkolenia z bezpieczeństwa laserowego, którego zdecydowanie potrzebujesz przed używaniem laserów publicznie. W niektórych krajach i regionach obowiązują dodatkowe wymogi prawne, ale niezależnie od tego zawsze należy stosować dobre praktyki bezpieczeństwa i profesjonalnej pracy.

PLASA udostępnia bezpłatny przewodnik dotyczący bezpieczeństwa laserowego, powszechnie uznawany za opis dobrych praktyk: [https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

Przed użyciem upewnij się, że rozumiesz konsekwencje bezpieczeństwa związane z laserami!

#### Wprowadzenie

Ta strona ma dać Ci ogólny obraz procesu bezpiecznego uruchamiania laserów. Szczegóły wykonania każdego kroku opisano dalej w tej sekcji, ale tutaj poznasz cały proces. Możesz też wracać do tej strony jako do listy kontrolnej przy każdej konfiguracji laserów.

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>Typowa osłona apertury lasera</p></figcaption></figure>

### Skonfiguruj sprzęt:

1. **Zamknij osłonę apertury** lasera
2. **Zamocuj laser bezpiecznie** i skieruj go we właściwą stronę
3. **Podłącz przycisk zatrzymania** do lasera
4. **Podłącz kontroler lasera** do komputera
5. **Włącz zasilanie** lasera

### Skonfiguruj Liberation:

1. **Rozbrój wszystkie lasery** oraz znajdź i podłącz kontroler w Liberation
2. **Ustaw wartość&#x20;**_**Global Brightness**_**&#x20;na 0** (użyj suwaka na pasku ikon albo _Master Fader_ na APC40)
3. **Uzbrój laser** — przy nadal zamkniętej osłonie apertury upewnij się, że żadne clips nie są aktualnie aktywne, a następnie uzbrój laser (użyj przycisku _Arm_ w panelu _Laser Overview_)
4. **Włącz pattern testowy** (użyj przycisku ☒ na pasku ikon, wybierz pattern 1 — zielony kwadrat z krzyżem)
5. **Dostosuj output zone** — oszacuj najbezpieczniejszy rozmiar i położenie strefy (na przykład może to być wysoko pod sufitem, ale zależy to od konkretnego miejsca)
6. **Upewnij się, że laser działa** — powoli zwiększaj jasność, aż zobaczysz światło za oknem apertury. Następnie zmniejsz jasność z powrotem do zera.
7. **Przetestuj przycisk zatrzymania**, aby upewnić się, że po jego naciśnięciu cały sygnał wyjściowy lasera zostaje wygaszony

### Uruchamianie sygnału wyjściowego lasera

1. **Oczyść obszar ekspozycji** — upewnij się, że nikt nie może zostać wystawiony na działanie lasera, i poinformuj cały personel, aby podczas konfiguracji laserów nie wchodził do obszaru ekspozycji. (Upewnij się też, że wszystkie kamery i projektory są zasłonięte albo mają założone osłony obiektywów!)
2. **Otwórz osłonę apertury** — stojąc z boku, poza kierunkiem wyjścia wiązki, przesuń osłonę apertury w dół. Jeśli Twoje strefy są wysoko, możesz zostawić ją częściowo zamkniętą.
3. **Zwiększ jasność, aż laser będzie ledwo widoczny** — ustaw laser tylko na tyle jasno, aby było widać strefę
4. **Dostosuj strefę lub strefy** — ustaw rozmiar, kształt i położenie strefy tak, aby znajdowała się 3 m nad podłogą względem wszystkich miejsc dostępnych publicznie oraz aby laser nie sięgał do żadnych innych miejsc dostępnych publicznie
5. **Dodaj fizyczne maskowanie** — użyj osłony apertury i/lub czarnej taśmy foliowej, aby fizycznie zamaskować wszystkie obszary poza docelową strefą. To krytycznie ważne, ponieważ każdy sprzęt lub oprogramowanie laserowe może ulec awarii.
6. **Dodaj maski programowe** — maski programowe w Liberation mogą służyć do ochrony kamer i projektorów, ale **nigdy** nie powinny zastępować fizycznego maskowania przy ochronie ludzi. Pamiętaj, że żadne oprogramowanie ani sprzęt nie są niezawodne, więc przed użyciem masek programowych upewnij się, że rozumiesz związane z tym ryzyko.

{% hint style="warning" %}
Pamiętaj, że ten przewodnik zakłada konfigurację wewnątrz budynku. Jeśli pracujesz na zewnątrz, trzeba wykonać dodatkowe kroki, aby zapewnić bezpieczeństwo statków powietrznych, w tym między innymi:

* Uzyskanie wymaganych pozwoleń od organów lotniczych, takich jak FAA lub CAA
* Koordynację z pobliskimi lotniskami i lądowiskami
* Sprawdzenie publicznych radarów lotów oraz wyznaczenie obserwatora, który będzie wypatrywał statków powietrznych

Lasery działające znacznie poniżej progu bezpieczeństwa nadal mogą spowodować katastrofalne rozproszenie uwagi pilotów.

Upewnij się, że masz wymagane kwalifikacje, licencje i pozwolenia, zanim skierujesz jakiekolwiek lasery w przestrzeń powietrzną.
{% endhint %}
