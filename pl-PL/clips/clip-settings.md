---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Ustawienia Clip

### Panel Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Panel ustawień Clip</p></figcaption></figure>

Zmień rozmiar wyjściowy klipu za pomocą _Scale X_ i _Scale Y_. Są one połączone, chyba że naciśniesz klawisz _SHIFT_.

Zmień pozycję poziomą i pionową klipu za pomocą _Shift X_ i _Shift Y_.

_Zone Delay/Chase_ to na tyle ciekawa funkcja, że ma własną sekcję. [Zone Delay/Chase](zone-delay-chase.md "mention")

### Panel parametrów

Panel po prawej stronie Clip Deck pokazuje osiem parametrów kontekstowych. Gdy zaznaczony jest Clip, pierwsze kontrolki to _Shift X_, _Shift Y_ i _Zone Delay_ dla wybranego Clip, a po nich globalne kontrolki _Spin_ i _Scale_.

Te same parametry są odzwierciedlane na obsługiwanych kontrolerach MIDI. Jeśli żaden Clip nie jest zaznaczony, miejsca przeznaczone na parametry konkretnego Clip pozostają puste. Jeśli przytrzymasz przycisk grupy, dwie pierwsze kontrolki zmienią się na czasy fade in i fade out tej grupy.

### Blokowanie klipów

Jeśli klip jest zablokowany, nie można go przenieść ani usunąć. Aby zablokować klip, użyj pola wyboru _Locked_ w menu wywoływanym prawym przyciskiem myszy. W panelu Clip settings dostępnych jest kilka dodatkowych opcji.

* _UNLOCK ALL -_ odblokowuje wszystkie klipy w Clip Deck.
* _AUTO-LOCK_ - gdy _Auto-Lock_ jest włączone, każdy klip odtwarzany automatycznie (z timeline albo przez system nagrywania/odtwarzania MIDI) zostanie zablokowany. Jest to przydatne, jeśli masz zaprogramowany show w Logic Pro (lub podobnym programie) i nie chcesz przypadkowo edytować klipów używanych w show.
* _LOCKED CLIPS ZONES_ - gdy ta opcja jest włączona, nie możesz zmieniać stref dla żadnego zablokowanego klipu.
* _LOCKED CLIPS PARAMS_ - gdy ta opcja jest włączona, nie możesz zmieniać parametrów (scale, shift itp.) żadnego zablokowanego klipu.

### Menu prawego przycisku myszy

Jeśli klikniesz Clip prawym przyciskiem myszy, pojawi się menu z wybranymi opcjami dla tego Clip. Zobacz [Wprowadzenie do Clip Editor](../clip-editor/clip-editor-intro.md "mention"), [Ustawienia Clip](clip-settings.md "mention") i [Grupy klipów](groups.md "mention"), aby dowiedzieć się więcej o pierwszych pozycjach w tym menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>The clip settings right-click menu</p></figcaption></figure>

### Retrigger

Domyślnie klipy mają włączone _retrigger_. Oznacza to, że niezależnie od tego, kiedy je uruchomisz, klip zacznie odtwarzać się od tego momentu. Jeśli więc uruchomisz go za późno, animacja klipu będzie lekko opóźniona i wyjdzie z rytmu.

{% hint style="info" %}
Jeśli użyjesz _Tap Tempo_, gdy działa klip z włączonym retrigger, system „skwantyzuje” klip do tempa, nawet jeśli nie uruchomiono go dokładnie na beat.
{% endhint %}

Jeśli _Retrigger_ nie jest włączone, klip zawsze będzie w tempie — tak, jakby został uruchomiony na samym początku zegara. To dobre rozwiązanie, gdy synchronizujesz się idealnie z muzyką przez zewnętrzny sygnał zegara.

{% hint style="info" %}
Klipy często projektuje się tak, aby zapętlały się bez końca, ale możesz też przygotować je tak, aby odtworzyły się tylko raz albo kilka razy. Upewnij się, że takie klipy mają włączone _retrigger_, inaczej nie wystartują ponownie!
{% endhint %}

### Czas przejścia in/out (fade)

Każdy Clip można skonfigurować tak, aby pojawiał się i znikał płynnie przez czas mierzony w sekundach. Domyślnie czas fade jest dziedziczony z ustawień grupy (można go zmienić, klikając prawym przyciskiem myszy przycisk grupy).

Jeśli chcesz ustawić inny czas fade niż w grupie klipu, najpierw wyłącz przycisk _USE GROUP DEFAULT_, a następnie dostosuj suwaki _In time_ i _Out time_ klipu.
