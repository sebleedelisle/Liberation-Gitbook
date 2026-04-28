---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Wprowadzenie

3D Visualiser w Liberation to niezwykle przydatna funkcja — możesz projektować i dopracowywać swoje pokazy bez użycia jakichkolwiek laserów! Dla mnie okazała się nieocenionym narzędziem, szczególnie przy bardziej złożonych konfiguracjach z dużą liczbą laserów.

### Poruszanie się po przestrzeni 3D

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Widok 3D Visualiser</p></figcaption></figure>

* Kliknij i przeciągnij, aby obracać widok wokół punktu orbity
* Użyj kółka myszy, aby przesuwać się do przodu i do tyłu względem punktu orbity
* Kliknij i przeciągnij z wciśniętym klawiszem Shift, aby przesuwać kamerę bocznie (strafe) w lewo, w prawo, w górę i w dół wzdłuż płaszczyzny XY
* Kliknij dwukrotnie w dowolnym miejscu wizualizatora, aby zresetować pozycję kamery

### Ustawienia

Otwórz panel _3D Visualiser Settings_ z menu _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Panel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** — zmienia rozmiar wizualizatora względem reszty aplikacji
* **Brightness Adjustment** — zmienia jasność wyświetlania laserów
* **Show laser numbers** — wyświetla odpowiedni numer nad każdym laserem
* **Show zone names** — wyświetla odpowiednie nazwy stref pod każdym laserem

### Ustawienia kamery

Te ustawienia dotyczą głównie wirtualnej kamery w przestrzeni 3D. Dostępna jest lista rozwijana z presetami tych ustawień, które możesz zapisywać i ponownie wczytywać.

* **Camera distance -** Kamera jest zawsze skierowana na swój _Orbit point_. Odległość kamery określa, jak daleko znajduje się od tego punktu. Możesz też dostosować to ustawienie kółkiem myszy.
* **FOV -** Pole widzenia — określa, jak szerokokątny lub przybliżony jest obraz z kamery.
* **Orbit position** — opisuje bieżący obrót wokół punktu orbity. Pierwsza wartość to obrót wokół osi X (pitch), a druga wartość to obrót wokół osi Y (yaw).
* **Orbit centre point** — pozycja punktu orbity w przestrzeni 3D: x, y, z.
* **Grid height** — wysokość siatki względem „podłoża” (czyli miejsca, gdzie y = 0).

### Ustawienia zawartości

Te ustawienia określają, gdzie lasery (i canvas) są umieszczone w środowisku 3D. Dostępna jest lista rozwijana z presetami tych ustawień, które możesz zapisywać i ponownie wczytywać.

#### Lasery

Każdy laser ma własną grupę ustawień, którą możesz rozwinąć małym białym trójkątem.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Ustawienia laserów w 3D Visualiser</p></figcaption></figure>

* **3D Position** — pozycja lasera w osiach x, y i z.
* **3D Orientation** — obrót lasera wokół każdej z osi x, y i z.
* **Flip X / Flip Y** — odwraca wirtualne wyjście lasera. UWAGA: nie powinno to być konieczne — lepiej używać ustawień odwrócenia/orientacji lasera, aby skorygować ewentualne niespójności sprzętowe.
* **Output Range horizontal / vertical** — dotyczy maksymalnego/minimalnego kąta skanerów lasera. Standardowo jest to 60º, ale możesz dostosować tę wartość, jeśli Twoje lasery są inne.

#### Canvas

Jeśli używasz systemu canvas, możesz także wyświetlić obraz canvas w widoku 3D. Zaznacz pole wyboru, aby renderować canvas, a następnie użyj ustawień pozycji, orientacji i skali, aby określić, jak ma wyglądać w widoku 3D.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Ustawienia canvas w 3D Visualiser</p></figcaption></figure>

{% hint style="info" %}
Widzisz „widmowe” lasery? 3D Visualiser działa w pewnym stopniu niezależnie od konfiguracji laserów, dlatego w wizualizatorze może znajdować się więcej laserów niż w Liberation. Gdy dodasz laser do projektu, zostanie też dodany nowy obiekt lasera w wizualizatorze. Jeśli jednak usuniesz laser, w wizualizatorze nadal pozostanie „widmowy” obiekt lasera.

Aby usunąć wszystkie widmowe lasery, kliknij przycisk _Remove extra 3D laser objects_ (na dole panelu ustawień 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
