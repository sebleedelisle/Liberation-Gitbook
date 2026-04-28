---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Wypełnienia, maski i sortowanie głębokości

### Kontury, wypełnienia i maski

Zauważysz, że niektóre węzły Creator mają opcję _Fill state_; możesz rysować je jako kontur (obrys), jako maskę (zasłaniającą elementy pod spodem) albo jako jedno i drugie.

Gdy renderujesz kształt jako maskę, działa to tak, jakby był wypełniony czernią — wszystko, co znajduje się pod nim, zostanie zasłonięte.

{% hint style="info" %}
Rysowanie linii (czyli _konturu_) laserem jest dość proste: skanujesz laserem od początku linii do jej końca. I linia gotowa!

Wypełnione kształty są trudniejsze. Jeśli chcesz uzyskać kształt wypełniony kolorem, możesz ręcznie wykonać kreskowanie krzyżowe, rysując linie i wypełniając obszar, ale Liberation nie potrafi robić tego automatycznie (jeszcze). A nawet gdyby potrafił, nadal byłoby widać prześwitujące pod spodem inne linie.

Możemy natomiast wypełniać kształty _czernią_. W tle Liberation wykonuje wszystkie obliczenia potrzebne do usunięcia treści znajdujących się pod kształtem wypełnionym czernią. I uwierz — to dość żmudne!

Ale działa bardzo dobrze i tworzy iluzję kształtu wypełnionego czernią.
{% endhint %}

### Sortowanie głębokości

Ponieważ niektóre kształty mogą _zasłaniać_ inne, Liberation musi sortować je według głębokości. Domyślnie elementy są sortowane według ich pozycji z. Jeśli znajdują się na tej samej pozycji z, są sortowane według pozycji na warstwie, którą można zmienić za pomocą przycisków _MOVE TO FRONT_ i _MOVE TO BACK_ w każdym creatorze.
