---
description: >-
  Lasery mogą być niebezpieczne, dlatego ważne jest przestrzeganie dobrych
  praktyk i zasad bezpieczeństwa. Ta strona zawiera przydatny przegląd, który
  pomoże Ci bezpiecznie przejść przez proces konfiguracji laserów.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/setting-up-lasers
---

# ✅ Przegląd procesu konfiguracji laserów

### Przegląd procesu bezpiecznego uruchamiania laserów

Ten podręcznik nie zastępuje formalnego szkolenia z bezpieczeństwa laserowego, którego zdecydowanie potrzebujesz przed użyciem laserów publicznie. W niektórych krajach lub regionach obowiązują dodatkowe wymagania prawne, ale niezależnie od tego zawsze należy stosować najlepsze praktyki bezpieczeństwa i profesjonalnej pracy.

PLASA udostępnia bezpłatny przewodnik bezpieczeństwa laserowego, który jest powszechnie uznawany za dobrą praktykę: [https://www.plasa.org/guidance-for-display-lasers/](https://www.plasa.org/guidance-for-display-lasers/)

Przed użyciem upewnij się, że rozumiesz konsekwencje bezpieczeństwa związane z laserami!

#### Wprowadzenie

Ta strona ma dać Ci ogólny obraz procesu bezpiecznego włączania laserów. Szczegóły wykonania każdego kroku opisano dalej w tej sekcji, ale ten przegląd pomoże Ci zrozumieć całość procesu. Możesz też wracać do niego jako listy kontrolnej przy każdej konfiguracji laserów.

<figure><img src="../.gitbook/assets/laser-aperture.jpg" alt=""><figcaption><p>Typowa osłona apertury lasera</p></figcaption></figure>

### Przygotowanie sprzętu:

1. **Zamknij osłonę apertury** lasera
2. **Zamocuj laser bezpiecznie** i skieruj go we właściwą stronę
3. **Podłącz sprzętowy przycisk awaryjnego zatrzymania** do lasera
4. **Podłącz laser controller** do komputera
5. **Włącz zasilanie** lasera

### Konfiguracja Liberation:

1. **Ustaw wszystkie lasery jako disarmed** oraz znajdź i połącz controller w Liberation
2. **Ustaw&#x20;**_**Global Brightness**_**&#x20;na 0** (użyj suwaka na pasku ikon albo _Master Fader_ na APC40)
3. **Ustaw laser jako _armed_** — przy nadal zamkniętej osłonie apertury upewnij się, że nie jest aktywny żaden Clip, a następnie ustaw laser jako _armed_ (użyj przycisku _Arm_ w panelu _Laser Overview_)
4. **Włącz test pattern** (użyj przycisku ☒ na pasku ikon, wybierz pattern 1 — zielony kwadrat z krzyżykiem)
5. **Dostosuj zone dla Output** — oszacuj najbezpieczniejszy rozmiar i pozycję zone (na przykład może być skierowana wysoko w sufit, ale zależy to od konkretnego miejsca)
6. **Sprawdź, czy laser działa** — powoli zwiększaj jasność, aż zobaczysz światło za oknem apertury. Następnie zmniejsz jasność z powrotem do zera.
7. **Przetestuj przycisk awaryjnego zatrzymania**, aby upewnić się, że po jego naciśnięciu całe wyjście lasera zostaje wygaszone

### Rozpoczęcie wyjścia laserowego

1. **Oczyść obszar ekspozycji** — upewnij się, że nikt nie może zostać wystawiony na działanie lasera, i poinformuj cały personel, aby podczas konfiguracji laserów pozostawał poza obszarem ekspozycji. (Upewnij się też, że wszystkie kamery i projektory są zasłonięte albo mają założone dekielki na obiektywy!)
2. **Otwórz osłonę apertury** — stojąc z boku i z dala od wyjścia lasera, przesuń osłonę apertury w dół. Jeśli Twoje zones są ustawione wysoko, możesz zostawić ją częściowo zamkniętą.
3. **Zwiększ jasność, aż laser będzie ledwo widoczny** — ustaw laser tylko na tyle jasno, ile potrzeba, aby zobaczyć zone
4. **Dostosuj zone lub zones** — ustaw rozmiar, kształt i pozycję zone tak, aby znajdowała się 3 m nad podłogą względem wszystkich miejsc dostępnych publicznie oraz aby laser nie docierał do żadnych innych obszarów dostępnych publicznie
5. **Dodaj maskowanie fizyczne** — użyj osłony apertury i/lub czarnej taśmy foliowej, aby fizycznie zamaskować wszystko poza żądaną zone. To jest krytycznie ważne, ponieważ każdy sprzęt laserowy lub oprogramowanie może ulec awarii.
6. **Dodaj maski programowe** — masks w Liberation mogą służyć do ochrony kamer i projektorów, ale **nigdy** nie powinny zastępować maskowania fizycznego służącego ochronie ludzi. Pamiętaj, że żadne oprogramowanie ani sprzęt nie są niezawodne, więc przed użyciem masek programowych upewnij się, że rozumiesz ryzyko.

{% hint style="warning" %}
Ten przewodnik zakłada konfigurację w pomieszczeniu. Jeśli pracujesz na zewnątrz, należy wykonać dodatkowe kroki, aby zapewnić bezpieczeństwo ruchu lotniczego, w tym między innymi:

* Uzyskanie wymaganych pozwoleń od organów lotniczych, takich jak FAA lub CAA
* Koordynację z pobliskimi lotniskami i lądowiskami
* Sprawdzenie publicznego radaru lotów oraz wyznaczenie obserwatora, który będzie wypatrywał statków powietrznych

Lasery znajdujące się znacznie poniżej progu bezpieczeństwa nadal mogą powodować katastrofalne rozproszenie uwagi pilotów.

Upewnij się, że masz wymagane kwalifikacje, licencje i pozwolenia, zanim skierujesz jakiekolwiek lasery w przestrzeń powietrzną.
{% endhint %}
