---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Tworzenie stref DMX

1. Podłącz węzeł Art-Net i skonfiguruj go zgodnie z opisem w sekcji [Łączenie z węzłem Art-Net](../connecting-to-an-artnet-node.md "mention").
2. Otwórz **DMX Zones** i kliknij **ADD DMX ZONE**.
3. Ustaw dla strefy wartości **Node**, **Universe** i **Address** zgodnie z urządzeniem.
4. Wybierz **Preset** dla urządzenia. Preset określa, które kanały DMX otrzymują stałe wartości, wartości włączania/wyłączania zawartości, kolor RGB, pozycję X/Y, jasność albo jawne wejścia DMX Value.
5. Kliknij **Edit DMX profile/channel mapping** (ikona suwaków), aby edytować mapowanie kanałów. Domyślny preset zaczyna od kanału włączania/wyłączania zawartości oraz kanałów koloru RGB.
6. Przypisz Clips do DMX zone tak samo, jak przypisujesz je do beam zone lub canvas zone.
7. Naciśnij **ARM**, gdy strefa ma być gotowa do wysyłania DMX.

{% hint style="warning" %}
Tylko uzbrojone DMX zones wysyłają wartości na żywo. Nieuzbrojone DMX zones zerują swoje zmapowane kanały, co jest bezpieczniejsze podczas konfigurowania urządzeń.
{% endhint %}

Wyjście DMX jest też ograniczone poziomem Twojej licencji. Jeśli przycisk **ARM** jest wyłączony, sprawdź, czy Twój poziom obejmuje wyjście DMX albo czy nie osiągnięto już maksymalnej liczby uzbrojonych DMX zones.
