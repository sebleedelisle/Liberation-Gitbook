---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Создаёт одну точку / луч.

* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **Colour** — цвет точки. См. [Настройки цвета и HSB](fundamentals/colour-settings-and-hsb.md)
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Создаёт линию / плоскость.

* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **Size** — длина линии
* **Colour** — цвет линии. См. [Настройки цвета и HSB](fundamentals/colour-settings-and-hsb.md)
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* **rotation** — угол линии в градусах
* **resolution** — см. [Разрешение](fundamentals/resolution.md)
* **alignment** — _LEFT / CENTRE / RIGHT -_ определяет начальную точку и центр вращения линии
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Создаёт круг / конус.

* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **radius** — радиус круга
* **Colour** — цвет круга. См. [Настройки цвета и HSB](fundamentals/colour-settings-and-hsb.md)
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* **resolution** — см. [Разрешение](fundamentals/resolution.md)
* **Fill state** — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Создаёт равносторонний многоугольник: треугольник, квадрат, пятиугольник и т. д.

* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **size** — расстояние от центра до каждого угла
* **Colour** — цвет многоугольника. См. [Настройки цвета и HSB](fundamentals/colour-settings-and-hsb.md)
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* **rotation** — угол поворота фигуры в градусах
* **resolution** — см. [Разрешение](fundamentals/resolution.md)
* **Fill state** — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Загружает SVG-файл для пользовательских фигур.

{% hint style="warning" %}
Liberation совместим с форматом _SVGTiny_. Рекомендуется использовать InkScape, но большинство приложений для векторной графики могут экспортировать в этот формат. Перед экспортом обязательно преобразуйте весь текст в фигуры. Liberation отрисовывает обводки и при необходимости может использовать заливки как masks. Убедитесь, что линии не чёрные, иначе без модификатора цвета они не будут видны!
{% endhint %}

* **Import SVG** — загрузить SVG-файл с диска.

{% hint style="info" %}
После загрузки SVG его содержимое преобразуется и сохраняется внутри clip, поэтому хранить ссылку на файл не нужно — кроме случаев, когда позже вы захотите изменить настройки mask.
{% endhint %}

* **Use fills as masks** — обрабатывает любую фигуру с заливкой как mask, то есть заполняет её чёрным. Этот параметр включается автоматически, если в SVG есть фигуры с заливкой. Если фигур с заливкой нет, он будет отключён. См. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** — если у фигур в SVG нет контура, мы не сможем их отрисовать! Этот параметр добавляет контур (или _stroke_) к любой фигуре с заливкой. Если в SVG нет фигур с обводкой, параметр включается автоматически. Если фигур с заливкой нет, он отключается.
* **Invert black lines** — если все линии в SVG чёрные, вы их не увидите! Этот параметр делает их белыми. Он включается автоматически, если в SVG есть только чёрные фигуры, но отключается, если таких фигур нет.
* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **scale** — изменяет размер SVG. Значение автоматически рассчитывается при загрузке SVG, чтобы изображение было видно, но затем его можно отредактировать вручную.
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* **rotation** — угол поворота изображения в градусах
* **resolution** — см. [Разрешение](fundamentals/resolution.md)
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Создаёт анимацию из последовательности SVG-файлов.

* **Import SVG Sequence** — выберите папку, в которой находятся все SVG-файлы. Обратите внимание: они загружаются в алфавитно-цифровом порядке.

{% hint style="info" %}
После загрузки последовательности SVG её содержимое преобразуется и сохраняется внутри clip, поэтому хранить ссылки на файлы не нужно — кроме случаев, когда позже вы захотите изменить настройки mask.
{% endhint %}

* **Use fills as masks** — обрабатывает любую фигуру с заливкой как mask, то есть заполняет её чёрным. Этот параметр включается автоматически, если в любом из SVG есть фигуры с заливкой. Если ни в одном SVG таких фигур нет, он будет отключён. См. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)
* **Add outlines to filled shapes** — если у фигур в SVG нет контуров, мы не сможем их отрисовать! Этот параметр добавляет контур (или _stroke_) к любой фигуре с заливкой. Если в SVG нет фигур с обводкой, параметр включается автоматически. Если ни в одном SVG нет фигур с заливкой, он отключается.
* **Invert black lines** — если все линии в SVG чёрные, вы их не увидите! Этот параметр делает их белыми. Он включается автоматически, если в SVG есть только чёрные фигуры, но отключается, если таких фигур нет.
* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **scale** — изменяет размер изображения.
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* **rotation** — угол поворота изображения в градусах
* **resolution** — см. [Разрешение](fundamentals/resolution.md)
* **speed** — длительность всей анимации в тактах.
* **time per frame** — если этот параметр включён, длительность задаётся для каждого кадра, а не для всей анимации. Например, если _speed_ установлен на ¼, каждый кадр будет длиться 1 долю.
* **animation direction** -
  * _FORWARDS_ — анимация идёт вперёд, затем зацикливается с начала
  * _BACKWARDS_ — анимация идёт назад, затем зацикливается с конца
  * _PINGPONG_ — анимация в цикле идёт вперёд, затем назад
  * _MANUAL_ — текущий кадр задаётся параметром _position manual_
* **position manual** — задаёт текущий кадр: 0% — первый кадр, 100% — последний кадр. Значение можно установить вручную или с помощью внешнего осциллятора.
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Создаёт текст с использованием шрифта TrueType или OpenType.

* **Text** — введите здесь нужный текст
* **Font** — выберите нужный шрифт

{% hint style="info" %}
Чтобы добавить в Liberation больше шрифтов, скопируйте файлы .ttf или .otf в папку data/resources/fonts.
{% endhint %}

* **Render profile** — см. [Профиль рендеринга](fundamentals/render-profile.md)
* **horizontal alignment** — выберите _LEFT_, _CENTRE_ или _RIGHT_, чтобы задать выравнивание текста.
* **Fill state** — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)
* **size** — размер текста
* **colour -** см. [Настройки цвета и HSB](fundamentals/colour-settings-and-hsb.md)
* Положение **x** и **y** — см. [Система координат](fundamentals/co-ordinate-system.md)
* **rotation** — угол поворота изображения в градусах
* **resolution** — см. [Разрешение](fundamentals/resolution.md)
* **reveal** — используйте этот параметр, чтобы постепенно показывать текст по одному символу. Когда значение находится между 0 и 50%, текст постепенно появляется слева направо. Когда значение между 50% и 100%, текст исчезает слева направо. К этому сокету можно подключить осциллятор для создания анимации.
* **reveal by word** — если включено, _reveal_ работает по словам, а не по символам.
* **countdown** — система обратного отсчёта (реализована на скорую руку!). Значение меняется каждые 2 доли, поэтому если нужны секунды, убедитесь, что темп установлен на 120 bpm.
* **countdown start** — число, с которого должен начинаться обратный отсчёт
* _MOVE TO FRONT / MOVE TO BACK_ — см. [Заливки, masks и сортировка по глубине](fundamentals/fills-masks-and-depth-sorting.md)
