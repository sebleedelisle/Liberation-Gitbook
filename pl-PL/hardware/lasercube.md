---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Zdjęcie promocyjne LaserCube dzięki uprzejmości Wicked Lasers</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) firmy Wicked Lasers to wyjątkowo kompaktowe, zasilane akumulatorowo urządzenie laserowe dostępne w kilku konfiguracjach mocy. Jest popularne wśród hobbystów dzięki łatwej w obsłudze aplikacji na smartfon, ale nowsze modele są już na tyle zaawansowane, że można ich używać także podczas profesjonalnych pokazów.

Aplikacja na telefon, nazywana LaserOS i dostępna również na komputery stacjonarne, jest darmowa, daje dużo frajdy i w zupełności wystarcza większości użytkowników. Jeśli jednak realizujesz większe pokazy z wieloma laserami, potrzebujesz czegoś bardziej wyspecjalizowanego i wydajnego — i tu właśnie wchodzi Liberation.

### Podłączanie LaserCube

Wczesne modele LaserCube są sterowane przez USB, ale wszystkie obecne modele mają wbudowany kontroler sieciowy. Te sterowane przez sieć urządzenia są znane jako „LaserCube Wifi”. Liberation obsługuje oba typy LaserCube\* — zarówno podłączone przez USB, jak i przez sieć.

\*(Obsługa protokołu sieciowego LaserCube została wprowadzona w wersji 0.7.3)

### USB LaserCube

Podłącz LaserCube do komputera przewodem micro USB, a następnie znajdź go w panelu _Controller Assignment_ (zobacz [Przypisywanie kontrolerów](../setting-up/controller-assignment.md "mention")). Jeśli nie pojawi się automatycznie, kliknij przycisk _REFRESH_.

### Sieciowy LaserCube „Wifi”

{% hint style="danger" %}
Chociaż urządzenia „Wifi” są zaprojektowane do pracy przez sieć bezprzewodową, nie jest to zalecane — prawdopodobnie pojawią się przerwy i zakłócenia. Zamiast tego użyj gniazda RJ45, aby podłączyć LaserCube do sieci przewodowej, tak samo jak w przypadku Ether Dream.
{% endhint %}

Podłącz LaserCube do sieci przewodowej.

Przełącz LaserCube w tryb „LAN Client” i upewnij się, że w sieci znajduje się router. LaserCube otrzyma adres IP z routera i powinien pojawić się w panelu _Controller Assignment_. (Zobacz [Przypisywanie kontrolerów](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Można skonfigurować sieć bez routera i nadać wszystkim urządzeniom stałe adresy IP; jest to bardzo powszechne w branży eventowej. Osobiście wolę dodać router do sieci i polecam tę opcję każdemu, kto ma mniejsze doświadczenie z konfiguracją sieci.

Router dynamicznie przydziela adres IP wszystkim urządzeniom — moim zdaniem jest to prostsze i mniej podatne na błędy.
{% endhint %}

{% hint style="danger" %}
W przeciwieństwie do Ether Dream, _**LaserCube NIE WYGASZA LASERA**_ w przypadku niedopełnienia bufora, utraconego pakietu albo innych uszkodzonych lub nieprawidłowych danych.

Zamiast tego po prostu kontynuuje pracę od miejsca, w którym przerwał, a w niektórych przypadkach może to spowodować przejście aktywnej wiązki przez obszary poza strefami, a co gorsza — przecięcie masek programowych.

Rozmawiam z projektantami/programistami LaserCube i mam nadzieję, że rozwiążą ten problem w przyszłości aktualizacją firmware’u. Do tego czasu musisz jednak zadbać o fizyczne zamaskowanie każdego miejsca, w które laser nie powinien trafić.

Szczerze mówiąc, prawdopodobnie i tak należy to robić, ale ja sam używam masek programowych do ochrony kamer i projektorów. Pamiętaj więc, że korzystanie z protokołu sieciowego LaserCube jest pod tym względem bardziej niebezpieczne niż używanie Ether Dream, który przechodzi w tryb zatrzymania bezpieczeństwa natychmiast po wykryciu błędu lub braku danych.

Powtórzę jeszcze raz: **używaj połączenia przewodowego z LaserCube**. Wifi nie wystarczy i tylko pogorszy ten problem.
{% endhint %}
