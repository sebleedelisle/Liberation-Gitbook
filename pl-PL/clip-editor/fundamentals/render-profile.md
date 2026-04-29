---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Profil renderowania

W każdym węźle _Creator_ dostępne jest ustawienie _Render Profile_, które określa, jak kształty są rysowane (czyli _renderowane_) laserami.

**W większości zastosowań ustawienie&#x20;**_**DEFAULT**_**&#x20;w zupełności wystarczy**. Jeśli jednak pracujesz z grafiką lub złożoną zawartością, możesz potrzebować większej kontroli nad sposobem renderowania każdego kształtu.

{% hint style="info" %}
W przeciwieństwie do większości programów laserowych Liberation generuje strumień punktów w czasie rzeczywistym, tuż przed przekazaniem go do kontrolerów laserów. Oszczędza to dużo miejsca na dysku: klipy mają zaledwie kilka kB zamiast wielu MB wstępnie wyrenderowanych strumieni punktów.

Oznacza to również, że tę samą zawartość możesz dostroić do różnych typów skanerów osobno dla każdego lasera, bez konieczności zmieniania samych klipów.

Więcej informacji znajdziesz w [◼️ Jak Liberation generuje treści laserowe](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Dostępne są trzy wstępnie zdefiniowane _Render Profiles_: _DEFAULT_, _FAST_ i _DETAIL._

_**DEFAULT**_ — dobry profil ogólny, najlepszy do większości zastosowań

_**FAST** -_ jeśli klip zawiera dużo elementów, a część z nich to bardzo proste punkty i linie proste, wybranie tej opcji może zmniejszyć migotanie.

_**DETAIL**_ — jeśli rysujesz coś, co wymaga ostrych narożników, użyj tej opcji. Pamiętaj jednak, że skanery będą poruszać się wolniej, przez co obraz może bardziej migotać.

{% hint style="info" %}
W edytorze klipów możesz przypisywać węzły Creator do różnych profili renderowania, ale każdy laser przetworzy te profile zależnie od swoich ustawień skanerów. Zobacz [◼️ Presety skanera i profile renderowania](../../advanced/scanner-presets.md)
{% endhint %}
