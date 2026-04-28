---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/co-ordinate-system
---

# 🟩 Układ współrzędnych

Zawartość Clip używa układu współrzędnych x/y, w którym początek (0,0) znajduje się na środku ekranu.

* Na osi poziomej x lewa strona ma wartości ujemne, a prawa dodatnie.
* Na osi pionowej y góra ma wartości ujemne, a dół dodatnie.

Clip ma szerokość i wysokość 400 pikseli, więc współrzędne widocznego obszaru mieszczą się w zakresie od -200 do 200.

{% hint style="info" %}
Edytor Clip tworzy kształty _wektorowe_. Oznacza to, że nie są one zapisywane jako piksele, lecz jako zestawy współrzędnych określające sposób rysowania kształtów. Działa to podobnie jak definiowanie zawartości w Inkscape lub Illustratorze, w przeciwieństwie do Photoshopa.
{% endhint %}

### 3D

Dodatkowo możesz poruszać się w przestrzeni 3D: do przodu i do tyłu wzdłuż osi z. Domyślnie wszystko znajduje się na pozycji z równej 0.

* Na osi z ruch do tyłu, od Ciebie, ma wartości ujemne, a ruch do przodu, w Twoją stronę, ma wartości dodatnie.
