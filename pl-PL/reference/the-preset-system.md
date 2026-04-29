---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ System presetów

System presetów jest używany w różnych miejscach Liberation wszędzie tam, gdzie trzeba przechowywać wiele ustawień możliwych do wyboru z listy _presetów_.

Obecnie system ten jest używany dla:

* ustawień skanerów
* ustawień kalibracji kolorów
* ustawień kamery 3D Visualiser
* ustawień lasera w 3D Visualiser
* profili DMX

Jeśli więc dostroisz ustawienia skanera dla swoich nowych skanerów CT6210, możesz zapisać je jako preset, nazwać go „CT6210”, a potem będzie on dostępny na liście presetów zawsze, gdy będzie potrzebny, oraz w menu rozwijanym.

Wszystkie presety są zapisywane razem z projektem (lub ustawieniami lasera), niezależnie od tego, czy ich używasz. Dlatego za każdym razem, gdy wczytasz jeden z tych plików, wszystkie znajdujące się w nim presety zostaną dodane do istniejących presetów. Jeśli jeden z wczytywanych presetów ma taką samą nazwę jak jeden z istniejących, zastąpi istniejący preset.

Możesz także importować i eksportować pliki presetów za pomocą przycisku load/save (ikona dyskietki) obok listy rozwijanej presetów. Otwiera on okno podręczne z przyciskami importu/eksportu oraz opcją usunięcia jednego lub kilku presetów.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Menu podręczne otwierane po kliknięciu ikony load/save</p></figcaption></figure>

Jeśli edytujesz preset, na przykład ustawienie skanera o nazwie _Default_, pamiętaj, że pozostałe lasery nie zostaną automatycznie zaktualizowane. Zamiast tego każde z ich ustawień skanera będzie teraz oznaczone jako _Default(edited)_. Aby zaktualizować je do nowego presetu _Default_, wybierz go ponownie z listy rozwijanej.

{% hint style="info" %}
Jeśli masz wiele laserów i chcesz zaktualizować ustawienia skanerów we wszystkich z nich, użyj systemu _COPY LASER SETTINGS_. Zobacz [Kopiowanie ustawień między laserami](../setting-up/copy-laser-settings.md)
{% endhint %}

Jeśli usuniesz preset używany w innym miejscu, nie stracisz tego ustawienia — zamiast tego zobaczysz je oznaczone jako _(deleted)._
