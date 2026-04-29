---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Obszary docelowe Canvas

Wiemy już, jak kierować fragmenty Canvas do stref w poszczególnych laserach, ale aby w ogóle umieścić treść w Canvas, potrzebne są _Canvas target areas_ — nazwa nieco myląca, ale trafna.

_Canvas target areas_ to sekcje Canvas, do których można kierować clipy. W widoku _CANVAS_ są oznaczone niebieskimi prostokątami z obrysem.

Często wystarczy jeden obszar docelowy Canvas, który następnie dzieli się na wiele stref wysyłanych do różnych laserów.

Czasem jednak warto użyć kilku obszarów docelowych Canvas, na przykład dla różnych części budynku albo aby wykorzystać między nimi opóźnienie stref. (Tak! Opóźnienie stref nadal działa między obszarami docelowymi Canvas!).

### Wysyłanie clipów do obszarów docelowych Canvas

W Clip Deck, obok przycisków stref beam, znajdują się przyciski obszarów docelowych Canvas. Aby je zobaczyć, może być konieczne przewinięcie przycisków wyjściowych — użyj `Shift + Left / Right Arrow`, przycisków ZONE PAGE na ekranie albo przycisków APC40 (zobacz [Referencja APC40](../reference/apc40-reference.md)).

Przypisuj clipy do obszarów docelowych Canvas, przełączając te przyciski dokładnie tak samo, jak przyciski stref beam.

### Dodawanie i edycja obszarów docelowych Canvas

Na górnym pasku menu wybierz _View -> Canvas Target Areas_ — zobaczysz wszystkie ustawienia każdego obszaru docelowego Canvas w projekcie.

U góry znajduje się przycisk _ADD CANVAS TARGET AREA_.

Aby usunąć obszar docelowy Canvas, użyj czerwonego przycisku ze znakiem minusa.

Rozmiar i położenie dostosujesz za pomocą suwaków. Kliknij suwak dwukrotnie, aby wpisać wartość.

### Tryb skalowania

* **FIT TO AREA** — zmniejsza treść tak, aby w całości mieściła się w obszarze docelowym Canvas, z zachowaniem proporcji. (To ustawienie domyślne)
* **FILL AREA** — skaluje treść tak, aby wypełniła obszar docelowy Canvas, z zachowaniem proporcji. Treść może zostać przycięta przy krawędziach.
* **STRETCH TO FIT** — rozciąga treść tak, aby wypełniła cały obszar docelowy Canvas, bez zachowania proporcji.
