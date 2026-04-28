---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Co zrobić, jeśli Liberation się nie uruchamia?

To rzadkie, ale czasem Liberation może nie uruchomić się albo zamknąć się zaraz po otwarciu. Prawie zawsze dzieje się tak dlatego, że jeden z lokalnych plików konfiguracyjnych został uszkodzony — zwykle po awarii systemu lub innym nieoczekiwanym zdarzeniu na komputerze.

Na szczęście łatwo to naprawić, resetując ustawienia lokalne. Poniżej znajdziesz instrukcje dla macOS i Windows.

> **Ważne**
>
> * Zamknij Liberation przed wykonaniem jakichkolwiek czynności.
> * Te kroki dotyczą tylko ustawień lokalnych, logów i pamięci podręcznej. Twoja licencja i konto są bezpieczne.

***

#### Gdzie znaleźć folder roboczy

Każda wersja Liberation ma własny folder roboczy. Na przykład jeśli używasz wersji 1.0.0, folder będzie nazywać się 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Jak szybko otworzyć ten folder**

**macOS**

1. W Finderze naciśnij **Shift + Cmd + G**.
2.  Wklej tę ścieżkę i naciśnij **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Otwórz folder odpowiadający numerowi Twojej wersji, na przykład `1.0.0`.

**Windows**

1.  Naciśnij **Win + R**, wklej poniższą ścieżkę i naciśnij **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Otwórz folder odpowiadający numerowi Twojej wersji, na przykład `1.0.0`.

> **Wskazówka dla Windows**: Jeśli przeglądasz foldery w File Explorer, włącz ukryte elementy: **View > Show > Hidden items**.

***

#### Krok 1 – Bezpiecznie zresetuj plik ustawień

W folderze swojej wersji otwórz:

```
data/liberation/
```

W folderze liberation powinien znajdować się plik o nazwie se`ttings.json`. Usuń ten plik.

* **Przykład dla macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Przykład dla Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Spróbuj teraz uruchomić Liberation. Jeśli program się otworzy, problem jest rozwiązany.

***

#### Krok 2 – Sprawdź, czy problemu nie powoduje clip

Jeśli Liberation uległ awarii podczas edytowania clipu, możliwe, że problem powoduje coś w tym pliku clipu.

W tym samym folderze co plik settings.json powinien znajdować się plik o nazwie clipEdit`.json`

Utwórz kopię zapasową tego pliku w bezpiecznym miejscu (na przykład na Desktop), a następnie usuń go z folderu roboczego Liberation.

Spróbuj ponownie uruchomić Liberation. Jeśli teraz otwiera się normalnie, wyślij prosimy plik z kopii zapasowej na adres [**info@liberationlaser.com**](mailto:info@liberationlaser.com), abyśmy mogli sprawdzić, co spowodowało problem.

***

#### Krok 3 - Utwórz kopię zapasową, a następnie usuń cały folder roboczy

Jeśli Krok 1 i Krok 2 nie pomogły:

1. **Utwórz kopię zapasową** całego folderu wersji:
   * macOS: Kliknij prawym przyciskiem folder `1.0.0` i wybierz **Compress**, aby utworzyć plik zip, albo skopiuj go w bezpieczne miejsce, na przykład na Desktop.
   * Windows: Kliknij prawym przyciskiem folder `1.0.0` i wybierz **Send to > Compressed (zipped) folder**, albo skopiuj go w bezpieczne miejsce, na przykład na Desktop.
2. Po utworzeniu kopii zapasowej **usuń** oryginalny folder `1.0.0` z lokalizacji roboczej Liberation.
3. Uruchom ponownie Liberation. Program utworzy nowy, czysty folder roboczy.

Jeśli Liberation teraz się otwiera, przejdź do Kroku 4.

***

#### Krok 4 - Wyślij nam kopię zapasową

Pomoże nam to ustalić przyczynę problemu i zapobiec mu w przyszłych wersjach.

Spakuj swoją **kopię zapasową** z Kroku 3, jeśli nie została jeszcze spakowana, a następnie wyślij ją e-mailem, abyśmy mogli zdiagnozować przyczynę.

* **Do**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Temat**: Naprawa uruchamiania Liberation - kopia zapasowa folderu roboczego
* **Treść**: Dołącz:
  * System operacyjny i wersję (np. macOS 14.6 lub Windows 11 23H2)
  * Wersję Liberation (np. 1.0.0)
  * Informację, który krok rozwiązał problem, jeśli którykolwiek (Krok 1, Krok 2 lub Krok 3)
  * Krótki opis tego, co wydarzyło się przed pojawieniem się problemu
* **Załącznik**: spakowana kopia zapasowa folderu roboczego `1.0.0`.

> Jeśli plik zip jest za duży, aby wysłać go e-mailem, prześlij go na dysk w chmurze i udostępnij link.

***

#### Nadal nie uruchamia się po Kroku 3?

Jeśli Liberation nadal się nie otwiera po usunięciu folderu roboczego:

* Uruchom ponownie komputer i spróbuj jeszcze raz.
* Tymczasowo wyłącz program antywirusowy lub narzędzia zabezpieczające, które mogą blokować tworzenie nowych folderów, a następnie spróbuj uruchomić program.
* Zainstaluj ponownie najnowszą kompilację Liberation na istniejącej instalacji.
* Jeśli żadna z powyższych metod nie działa, skontaktuj się z pomocą techniczną pod adresem [**info@liberationlaser.com**](mailto:info@liberationlaser.com), podając szczegóły oraz dołączając logi awarii z podfolderu `logs`, jeśli istnieje.

***

#### Podsumowanie

1. Usuń `data/liberation/settings.json` w folderze roboczym swojej wersji.
2. Jeśli edytowałeś clip, utwórz kopię zapasową, a następnie usuń `data/liberation/clipEdit.json`.
3. Jeśli nadal się nie otwiera, utwórz kopię zapasową, a następnie usuń cały folder `1.0.0` (lub folder swojej wersji).
4. Jeśli Krok 3 rozwiąże problem (albo jeśli go nie rozwiąże), spakuj kopię zapasową i wyślij ją na adres [**info@liberationlaser.com**](mailto:info@liberationlaser.com), podając system operacyjny i wersję Liberation.
