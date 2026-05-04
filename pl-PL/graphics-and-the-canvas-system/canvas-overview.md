---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Przegląd Canvas

System Canvas w Liberation jest stosunkowo prosty, ale na początku może być mylący. Oto ogólny opis, który pomoże Ci zacząć.

{% hint style="info" %}
**Zaraz, czy potrzebuję systemu Canvas?**

Niekoniecznie! Jeśli po prostu wyświetlasz jedną grafikę na jednym laserze, możesz łatwo zrobić to za pomocą beam zone (choć domyślnie zawartość beam zone jest odwrócona w poziomie, więc trzeba będzie wykonać X flip klipu).

Jeśli jednak chcesz rozdzielić zawartość graficzną między więcej niż jeden laser albo podzielić ją na różne sekcje do mapowania na architekturze, system Canvas jest właśnie do tego.
{% endhint %}

### Canvas

Przede wszystkim jest sam Canvas. To właśnie widzisz w widoku _CANVAS_: dużą przestrzeń roboczą — swoiste płótno — w której możesz umieszczać zawartość w dowolnym miejscu.

### Obszary docelowe Canvas

W widoku Canvas są pokazane jako niebieskie prostokąty konturowe. Są to obszary, do których możesz wysyłać zawartość. Zawartość klipu wysyłasz do obszaru docelowego Canvas tak samo, jak wysyłasz klip do beam zone. Przyciski obszarów docelowych Canvas znajdziesz w Clip Deck po prawej stronie przycisków beam zone.

{% hint style="info" %}
Jeśli nie widzisz przycisków Canvas w Clip Deck, spróbuj przewinąć przyciski beam zone za pomocą `Shift + Left / Right Arrow`. Powinien być widoczny przycisk dla każdego obszaru docelowego Canvas, oznaczony jako _CANVAS 1, CANVAS 2_ itd.
{% endhint %}

### Strefy Canvas

Strefy Canvas to obszary wewnątrz Canvas, które wybierasz do wysłania na laser. W widoku Canvas są przedstawione jako różowe prostokąty konturowe. Możesz kliknąć prawym przyciskiem każdą strefę i wybrać lasery, do których ma być przypisana. Jeśli teraz przełączysz się na widok _OUTPUT_ dla tego lasera, zobaczysz, że pojawiła się nowa strefa.

{% hint style="danger" %}
OSTRZEŻENIE — jeśli laser jest uzbrojony, możesz nagle zacząć wyświetlać zawartość w domyślnej strefie Canvas. Najlepiej rozbroić laser przed przypisaniem do niego stref Canvas.
{% endhint %}

{% hint style="info" %}
Strefę Canvas możesz też przypisać do lasera, klikając przycisk _add canvas zone_ w widoku _OUTPUT_. Zobacz [Zones](../output-view/zones.md "mention").
{% endhint %}

### Obrazy pomocnicze

Do Canvas możesz dodać obraz pomocniczy i używać go jako szablonu dla grafiki. Warto dostosować tint koloru obrazu pomocniczego (menu po kliknięciu prawym przyciskiem) i przyciemnić go, aby łatwiej było widzieć na nim własną zawartość.

{% hint style="info" %}
Przy mapowaniu architektonicznym pomocne okazało się przygotowanie „rozłożonej” wizualizacji budynku, która przedstawia wszystkie jego powierzchnie jako płaski, niezniekształcony obraz. Korekcję perspektywy poszczególnych sekcji można wykonać za pomocą strefy Canvas w widoku _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>„Spłaszczony” obraz pomocniczy dla Saltwell Hall w Gateshead w Wielkiej Brytanii</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Strefy Canvas we wczesnej wersji Liberation (ok. 2017!). Zwróć uwagę: różowe prostokąty określają, którą część Canvas pokazać, a widoki output poniżej pokazują, do której części każdego lasera trafiają te strefy.</p></figcaption></figure>

### Canvas w 3D visualiser

Odtworzenie skomplikowanego systemu projekcji wielolaserowej w 3D visualiser byłoby prawdopodobnie co najmniej kłopotliwe. Dlatego zamiast tego możesz umieścić Canvas w przestrzeni 3D. Włącz pole wyboru _Show canvas_ w panelu _3D visualiser settings_. (Wszelkie obrazy pomocnicze znajdujące się w Canvas również pojawią się w visualiser).

{% hint style="info" %}
Pamiętaj, że visualiser nadal będzie pokazywać projekcje Canvas jako efekty atmosferyczne wychodzące z laserów. Możesz po prostu przesunąć je poza widok albo — jeśli chcesz zrobić to dokładniej — wyrównać je z Canvas.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Wyrównanie wiązek z lasera z obrazem Canvas w 3D visualiser może dać naprawdę dużo satysfakcji!</p></figcaption></figure>
