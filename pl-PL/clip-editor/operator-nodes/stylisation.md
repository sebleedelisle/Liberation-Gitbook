---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Węzły Stylisation

## &#x20;Randomise

Tworzy rozproszone kopie elementów wejściowych przy użyciu spójnego pola szumu. Innymi słowy: kopiuje i przesuwa kształty oraz punkty w kontrolowany, „zaszumiony” sposób. Zamiast elementów ułożonych równo w jednym miejscu otrzymujesz wiele wersji, które przesuwają się i rozchodzą, jak cząstki poruszające się w strumieniu.

* **count** – liczba kopii na każdy element wejściowy (1–20). Przy wartości 1 otrzymujesz jedną, lekko przesuniętą wersję każdego elementu. Wyższe wartości tworzą wiele rozproszonych kopii.
* **noise offset** – przechodzi cyklicznie przez pole szumu (0–100%). Zapętla się płynnie, więc animowanie tego parametru za pomocą Oscillator Node daje gładki, ciągły ruch wszystkich kopii naraz.
* **noise jitter** – steruje skalą tekstury szumu. Niższe wartości dają szerokie, płynne zmiany. Wyższe wartości dają ciaśniejsze, bardziej chaotyczne rozmieszczenie. Zmienia to wzór, a nie siłę efektu.
* **change between points** – określa, jak bardzo każda kopia różni się od poprzedniej. Niskie wartości utrzymują kopie blisko siebie i podobne do siebie. Wysokie wartości bardziej je rozrzucają i zwiększają zróżnicowanie.
* **face direction** – obraca każdą kopię tak, aby była skierowana zgodnie z kierunkiem ruchu w polu szumu, tworząc strzałki/cząstki ustawione zgodnie z przepływem.
* **amount** – ogólna siła efektu (0–100%). Skaluje zarówno przesunięcie, jak i obrót wynikający z Face direction.

{% hint style="info" %}
Węzeł Randomise jest podstawą efektu Randomise!
{% endhint %}

## &#x20;Trails

Tworzy echa zawartości, pozostawiając za poruszającym się oryginałem zanikające lub skalowane kopie.

* **change render profile for trail** – jeśli włączone, wszystkie kopie śladu używają wybranego **render profile**. _Zobacz_ [render-profile.md](../fundamentals/render-profile.md).
* **render profile** – profil używany dla kopii śladu, gdy powyższy przełącznik jest włączony. Często używane, gdy główna zawartość jest ustawiona na **DETAIL**, a echa są renderowane jako **FAST**. Dzięki temu główne kształty zachowują wyraźne detale, a ślady są renderowane wydajniej.
* **delay** – ustawia odstęp między kopiami śladu w czasie muzycznym, mierzony w **krokach 1/64 nuty**.\
  Dla orientacji:
  * 16 = 1/16 taktu (szesnastka)
  * 32 = 1/8 taktu (ósemka)
  * 64 = 1/4 taktu (ćwierćnuta)
  * 128 = 1/2 taktu (półnuta)
  * 256 = 1 takt
* **trail size** – ile kopii śladu ma być rysowanych za bieżącą zawartością.
* **freeze trails** – zamienia płynnie poruszające się ślady w sekwencję zamrożonych migawek. Przydatne do tworzenia efektów śladu typu staccato, zsynchronizowanych z beatem.
* **brightness start / brightness end** – stosuje jasność wzdłuż śladu, od najnowszej kopii (**start**) do najstarszej (**end**). Zwykle ustaw **brightness start** na 100%, a **brightness end** na 0%, aby echa stopniowo zanikały.
* **scale start / scale end** – stosuje skalowanie wzdłuż śladu, od najnowszej kopii (start) do najstarszej (end). Aby ślady kurczyły się do zera, ustaw **scale start** na 100%, a **scale end** na 0%.

## &#x20;Shimmer

Dodaje migoczącą zmienność jasności do zawartości — od delikatnego połysku po intensywne strobowanie.

* **speed** – jak szybko shimmer zmienia się w czasie. Wyższe wartości powodują szybsze migotanie; 0 wstrzymuje efekt.
* **separation** – jak bardzo sąsiednie punkty/elementy różnią się od siebie.
  * 0: wszystko migocze jednocześnie.
  * \>0: pobliskie punkty otrzymują stopniowo różne fazy, więc shimmer zmienia się w obrębie kształtu.
  * <0: tak samo jak wyżej, ale przebieg fazy idzie w przeciwnym kierunku.
* **threshold** – zamiast płynnie zanikać, punkty migają teraz w pełni włączone albo wyłączone, zależnie od swojej jasności. Jaśniejsze elementy zapalają się częściej, ale pamiętaj, że elementy o jasności 100% są zawsze włączone, a elementy o jasności 0% są zawsze wyłączone. Przydatne do ostrych efektów brokatu lub światła gwiazd.

{% hint style="info" %}
Włączenie **threshold** to jedna z tych świetnych ukrytych funkcji, które potrafią naprawdę ożywić cząstki lub zawartość. Zamiast zanikać, punkty są szybko włączane i wyłączane na podstawie swojej jasności. Ponieważ w danej chwili rysowanych jest mniej punktów, rezultat jest jaśniejszy, a animacja płynniejsza.

Pamiętaj jednak, że jeśli zawartość ma już jasność 100%, nie zobaczysz żadnego efektu!
{% endhint %}

* **use whole shape** – stosuje jedną wartość shimmer równomiernie do całego kształtu. Gdy opcja jest wyłączona, węzeł dzieli kształty, aby różne części mogły migotać niezależnie, tworząc ziarnisty wygląd.

## &#x20;Particles

To eksperymentalny efekt, który generuje i animuje cząstki na podstawie zawartości. Wszystkie elementy punktowe na wejściu są traktowane jako pozycje emiterów. Ponieważ ścieżki cząstek są obliczane z wyprzedzeniem, po zmianie zawartości wejściowej może być konieczne odświeżenie lub ponowne przeliczenie cząstek (wystarczy zmienić dowolne ustawienie).

**General**

* **keep original** – jeśli włączone, oryginalna zawartość zostaje zachowana, a cząstki są dodawane na wierzchu. Przydatne, gdy punkty emitera mają pozostać widoczne.
* **number of particles** – ile cząstek jest tworzonych przy każdej emisji. Wyższe wartości dają gęstsze efekty, niższe bardziej minimalistyczne.
* **emission period** – zakres pętli (w taktach), w którym emitowane są cząstki. Przy 100% są rozłożone równomiernie w całej pętli; mniejsze wartości grupują je w krótsze serie.
* **loop length** – jak długo trwa pętla cząstek, mierzone w taktach muzycznych.
* **loop count** – ile razy pętla powtarza się przed zresetowaniem. Jeśli ustawisz 1, cząstki za każdym razem będą wykonywać dokładnie tę samą symulację, co daje pełną powtarzalność. Wyższe wartości wprowadzają więcej zróżnicowania przed resetem cyklu.
* **delay** – przesuwa czas rozpoczęcia emisji o określoną liczbę 1/64 nuty, przydatne do efektów timingowych.

**Motion**

* **speed** – jak szybko cząstki oddalają się od emitera.
* **speed variation** – dodaje losowość, aby cząstki nie poruszały się wszystkie z tą samą prędkością. Tworzy bardziej naturalne rozproszenie.
* **direction** – ustawia bazowy kierunek wystrzeliwania cząstek, określony przez **kąty x, y, z**. Kąty te obracają wektor emisji w przestrzeni 3D, dzięki czemu możesz skierować cząstki pionowo w górę, na bok albo pod dowolnym skosem. Połącz z **spread**, aby uzyskać szersze stożki lub bardziej chaotyczne wybuchy.

{% hint style="info" %}
**Euler angles**\
Liberation używa **Euler angles** do opisu orientacji w przestrzeni 3D. Są to po prostu obroty wokół trzech głównych osi:

* **X** – pochylenie do przodu/do tyłu (jak kiwanie głową)
* **Y** – obrót w lewo/w prawo (jak kręcenie głową „nie”)
* **Z** – obrót zgodnie z ruchem wskazówek zegara / przeciwnie do niego (jak przechylanie głowy na bok)

Dostosowując te trzy wartości, możesz skierować cząstki w dowolnym kierunku.
{% endhint %}

* **direction variation** – dodaje losowy rozrzut wokół tego kierunku. Przydatne do tworzenia stożków, rozpyleń lub eksplozji.
* **drag** – spowalnia cząstki w czasie. Wyższe wartości sprawiają, że wydają się cięższe i bardziej ociężałe.
* **gravity** – przyciąga cząstki w dół (wartości dodatnie) lub wypycha je w górę (wartości ujemne).
* **gravity variation** – dodaje zróżnicowanie grawitacji dla poszczególnych cząstek, przez co ruch staje się bardziej chaotyczny.

**Life**

* **life duration** – jak długo istnieją cząstki (mierzone w jednostkach 1/64 nuty). Przy krótszych wartościach cząstki znikają szybko, a przy dłuższych pozostają widoczne przez dłuższy czas.
* **life variation** – dodaje losowość czasu życia cząstek, aby nie znikały wszystkie naraz.
* **start delay / start delay variation** – opóźnia moment, w którym każda cząstka staje się widoczna (w krokach 1/64 nuty). Cząstka jest już wygenerowana i porusza się w tym czasie, ale jej jasność jest utrzymywana na poziomie 0, więc pozostaje niewidoczna do końca opóźnienia. Przydatne, jeśli chcesz uzyskać opóźnione „iskierki” fajerwerków.

**Colour & brightness**

* **hue start** – początkowy kolor cząstek.
* **hue variation** – dodaje losowość, aby cząstki nie zaczynały wszystkie od tego samego koloru.
* **hue change** – przesuwa hue w trakcie życia cząstki, tworząc ślady zmieniające kolor.
* **brightness start / brightness end** – stosuje jasność w trakcie życia cząstki. Zwykle ustaw brightness start wysoko, a brightness end nisko, aby cząstki naturalnie zanikały.
* **brightness variation** – losowo zmienia jasność początkową, dając bardziej dynamiczny wygląd.
* **saturation start / saturation end** – określa, jak intensywny jest kolor na początku i na końcu.
* **saturation variation** – losowo zmienia nasycenie, tworząc zróżnicowanie między cząstkami.

**Simulation**

* **time adjustment** – przyspiesza lub spowalnia całą symulację cząstek. Przydatne do synchronizacji z różnymi tempami albo do uwydatnienia ruchu.
